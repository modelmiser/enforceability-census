#!/usr/bin/env python3
"""Scorer for HL1 — the binary human pass against the witnessed locality
boundary (see README.md in this directory; frozen at registration,
BEFORE any human sees the packet).

Input: a text file of lines `NUMBER:ANSWER`, ANSWER in {YES, NO}
(case-insensitive; Y/N accepted; a trailing `?` marks a torn call and is
stripped for scoring, reported separately). Every one of the 23 items
must appear exactly once.

Ground truth: L(i) = "some local rung (prop or object) witnessed
among eligible readings" per the shipped witness artifacts of
census/locality2 (main 6ba6f9a) — executable validators on the YES
side; vote-descended eligibility plus challengeable FAILS records on
much of the NO side (the asymmetry is disclosed in README.md). The embedded table below
is cross-checked at runtime against a fresh derivation from those
artifacts — drift is a hard failure, not a skip.

Usage: python3 census/human-locality/score_hl1.py labels.txt
       python3 census/human-locality/score_hl1.py   (self-tests only)
"""
import pathlib
import re
import sys

if not __debug__:
    raise SystemExit("this scorer's guards use assert — do not run with -O")

HERE = pathlib.Path(__file__).resolve().parent

# The 23-item witnessed iCalendar set and its L values (True = a local
# rung is witnessed; False = nonlocal only). Derived from
# census/locality2 witness outcomes; runtime-cross-checked below.
L = {
    1: False, 7: False, 13: False, 43: False, 62: False, 63: True,
    69: False, 77: False, 79: False, 84: True, 91: False, 116: True,
    118: False, 143: True, 146: False, 150: False, 185: True,
    192: True, 193: True, 194: True, 200: False, 201: False,
    210: False,
}
ITEMS = set(L)

# Registered cells (README.md §Cells). 43 is excluded from HL1b because
# its sentence is byte-identical to exception item 79; it is graded via
# the HL1d determinism control instead.
A_ITEMS = [63, 84, 143, 192, 193, 194]            # local singles
B_ITEMS = [1, 7, 13, 69, 91, 118, 146, 150, 200, 201, 210]
C_ITEMS = [62, 77, 79]                            # E-vs-L exceptions
D_PAIR = (43, 79)                                 # byte-identical pair
E_ITEMS = [116, 185]                              # two-rung, reported
A_FLOOR, B_FLOOR, C_FLOOR = 5, 9, 2
assert sorted(A_ITEMS + B_ITEMS + C_ITEMS + [43] + E_ITEMS) == \
    sorted(ITEMS)
assert all(L[i] for i in A_ITEMS + E_ITEMS)
assert not any(L[i] for i in B_ITEMS + C_ITEMS + [43])


def derive_l():
    """Re-derive L from the shipped witness artifacts (drift check)."""
    sys.path.insert(0, str(HERE.parent / "locality2"))
    import check_witnesses2
    import witnesses_ical
    cfg = check_witnesses2.CFG["ical"]
    out = check_witnesses2.outcomes(witnesses_ical.WITNESSES, cfg)
    return {i: bool(out[i] & {"prop", "object"}) for i in out}


def parse(text):
    answers, torn = {}, set()
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r"(\d+)\s*:\s*([A-Za-z]+)(\?)?", line)
        assert m, "unparseable line: %r" % raw
        n, word = int(m.group(1)), m.group(2).upper()
        assert n in ITEMS, "item %d not in the registered set" % n
        assert n not in answers, "duplicate item %d" % n
        assert word in ("YES", "NO", "Y", "N"), \
            "item %d: answer must be YES or NO, got %r" % (n, word)
        if m.group(3):
            torn.add(n)
        answers[n] = word.startswith("Y")
    missing = sorted(ITEMS - set(answers))
    assert not missing, "missing items: %s" % missing
    return answers, torn


def grade(ans):
    results = []
    a = sum(1 for i in A_ITEMS if ans[i] is True)
    results.append(("HL1a local singles answered YES >=%d/6" % A_FLOOR,
                    a >= A_FLOOR, "%d/6" % a))
    b = sum(1 for i in B_ITEMS if ans[i] is False)
    results.append(("HL1b nonlocal singles answered NO >=%d/11" % B_FLOOR,
                    b >= B_FLOOR, "%d/11" % b))
    c = sum(1 for i in C_ITEMS if ans[i] is True)
    results.append(("HL1c exception trio answered YES >=%d/3 "
                    "(prediction: the trigger-pull is human-shared)"
                    % C_FLOOR, c >= C_FLOOR, "%d/3 YES" % c))
    d_ok = ans[D_PAIR[0]] == ans[D_PAIR[1]]
    results.append(("HL1d duplicate-text determinism (43==79)", d_ok,
                    "%s/%s" % tuple("YES" if ans[i] else "NO"
                                    for i in D_PAIR)))
    report = {i: ("YES" if ans[i] else "NO") for i in E_ITEMS}
    graded21 = A_ITEMS + B_ITEMS + C_ITEMS + [43]
    agree = sum(1 for i in graded21 if ans[i] == L[i])
    return results, report, agree, len(graded21)



# ---- answer-leak guard (added 2026-08-20, after the H1 defect) ----

def answer_leaks_in(text):
    """Answer-shaped NUMBER:YES/NO tokens before the item list naming a REGISTERED item.

    H1's packet stated its return format with `13:PROCESS` and `62:DOMAIN?` — real
    graded items carrying the archive's own labels. Item 13 sat in H1's H2 clause
    and was one of the largest measured FAILING branch's misses, so that single
    token converted that branch into a PASS at the floor
    (see census/human/README.md, addenda of 2026-08-20).

    HL1 was never defective: its examples are 8 and 104, absent from the registered
    set. But its protection was a PROSE disclaimer — "Numbers in these two examples
    are arbitrary and do not appear below" — and prose is not a guard. This makes it
    mechanical.

    HL1's rule differs deliberately from H1-R2's. H1-R2 removed numbers and class
    tokens entirely; HL1 permits arbitrary numbers under its explicit disclaimer, so
    this guard fires only on a number IN the registered set.

    Scope, stated so this is not mistaken for full coverage: it sees only the
    NUMBER:ANSWER shape, only before the item list. A prose leak ("item 13 is not
    locally checkable"), or a leak inside the item list, passes silently.
    """
    head = re.split(r'(?m)^\[\d+\]', text)[0]
    return [(int(n), w.upper()) for n, w in
            re.findall(r'\b(\d+)\s*:\s*(YES|NO|Y|N)\b', head, re.I)
            if int(n) in ITEMS]


def answer_leaks(path=None):
    return answer_leaks_in((path or (HERE / "packet-hl1.md")).read_text())


def self_test():
    # Answer-leak guard, negative-controlled: it must be clean on the real packet
    # AND must fire on a synthetic packet carrying a registered item number.
    live = answer_leaks()
    assert not live, "answer-shaped leak in packet-hl1.md: %r" % (live,)
    probe = "format: `NUMBER:YES` (e.g. `13:NO`) and `62:YES?`\n\n[1] first item\n"
    fired = answer_leaks_in(probe)
    assert {n for n, _ in fired} == {13, 62}, \
        "negative control did not fire correctly: %r" % (fired,)
    # a number OUTSIDE the registered set must NOT fire (HL1 permits arbitrary numbers)
    assert not answer_leaks_in("e.g. `8:NO` … `104:YES?`\n\n[1] first item\n"), \
        "guard wrongly fires on HL1's own arbitrary example numbers"

    # Drift check against the witness artifacts — unconditional.
    derived = derive_l()
    assert derived == L, (
        "L drift: derived-only %s, embedded-only %s"
        % ({i: derived[i] for i in derived if derived.get(i) != L.get(i)},
           {i: L[i] for i in L if derived.get(i) != L.get(i)}))
    # Parse rejection mutants.
    ok_text = "\n".join("%d:%s" % (i, "YES" if L[i] else "NO")
                        for i in sorted(ITEMS))
    parse(ok_text)

    def must_fail(text, why):
        try:
            parse(text)
        except AssertionError:
            return
        raise SystemExit("parse mutant not rejected: %s" % why)

    must_fail(ok_text + "\n63:YES", "duplicate item")
    must_fail(ok_text + "\n999:YES", "unknown item")
    must_fail(ok_text.replace("63:YES", "63:MAYBE"), "bad answer word")
    must_fail("\n".join(ok_text.splitlines()[:-1]), "missing item")
    # Degenerate strategies, MEASURED (floors must sit above each
    # refusable score; the clause each strategy structurally passes is
    # disclosed in the registration).
    all_yes = {i: True for i in ITEMS}
    all_no = {i: False for i in ITEMS}
    rnd = __import__("random").Random("hl1-shuffle")
    labels = [L[i] for i in sorted(ITEMS)]
    rnd.shuffle(labels)
    shuffle = dict(zip(sorted(ITEMS), labels))
    scores = {}
    for name, ans in (("all-yes", all_yes), ("all-no", all_no),
                      ("shuffle", shuffle)):
        res, _rep, _ag, _n = grade(ans)
        scores[name] = {r[0][:4]: r[1] for r in res}
    assert scores["all-yes"]["HL1b"] is False, \
        "all-yes not refused by HL1b"
    assert scores["all-no"]["HL1a"] is False, "all-no not refused by HL1a"
    assert scores["all-no"]["HL1c"] is False, "all-no not refused by HL1c"
    assert (scores["shuffle"]["HL1a"] is False
            or scores["shuffle"]["HL1b"] is False), \
        "seeded shuffle refused by neither HL1a nor HL1b"
    # Perfect-L answers: HL1a/b/d pass; HL1c FAILS by design (the
    # registered prediction is that the human sides AGAINST L there).
    res, _rep, agree, n = grade({i: L[i] for i in ITEMS})
    byname = {r[0][:4]: r[1] for r in res}
    assert byname["HL1a"] and byname["HL1b"] and byname["HL1d"]
    assert byname["HL1c"] is False and agree == n
    # Per-clause grading mutants: flip enough answers to break each.
    base = {i: L[i] for i in ITEMS}
    base.update({62: True, 77: True})            # make HL1c pass
    res, _rep, _a, _n = grade(dict(base))
    assert all(ok for _name, ok, _d in res), "fixture should pass all"
    for flips, clause in (
            ({63: False, 84: False}, "HL1a"),
            ({1: True, 7: True, 13: True}, "HL1b"),
            ({62: False, 77: False}, "HL1c"),
            ({43: True}, "HL1d")):
        broken = dict(base)
        broken.update(flips)
        res_b, _rep, _a, _n = grade(broken)
        got = [ok for name, ok, _d in res_b if name.startswith(clause)][0]
        assert got is False, "grading mutant %s did not fire" % clause
    print("self-tests: parse rejections fire; L matches the witness "
          "derivation; degenerates measured (all-yes refused by HL1b, "
          "all-no by HL1a+HL1c, shuffle by HL1a/HL1b; all-yes passes "
          "HL1c structurally — disclosed); per-clause mutants fire")


def main():
    self_test()
    if len(sys.argv) < 2:
        print("no labels file — registration-time run, nothing to grade")
        return
    answers, torn = parse(pathlib.Path(sys.argv[1]).read_text())
    res, report, agree, n = grade(answers)
    print("torn (?) items: %s" % (sorted(torn) or "none"))
    for name, ok, detail in res:
        print("%-6s %s — %s" % ("PASS" if ok else "FAIL", name, detail))
    print("REPORT two-rung items (both answers defensible, not graded): "
          "%s" % report)
    print("REPORT raw agreement with L over the %d graded items: %d/%d "
          "(joins no series)" % (n, agree, n))


if __name__ == "__main__":
    main()
