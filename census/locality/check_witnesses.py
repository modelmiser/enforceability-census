#!/usr/bin/env python3
"""Mechanical checker + grader for the locality study (see README.md).

Shipped at registration time, BEFORE any witness exists: the grading is
fixed first. When `witnesses.py` is absent, runs its self-tests and exits.

Witness schema (`witnesses.py` exposes WITNESSES: list, FAILS: list):

Validator entry (asserts locality of a reading at a rung):
  {"item": int, "reading": str, "rung": "msg"|"transcript",
   "eligible": bool, "kind": "validator",
   "fn": callable-of-one-parameter, "accept": [datum, ...],
   "reject": [datum, ...], "quote": str,
   # transcript rung only — the msg-level distinguishing pair against the
   # best-candidate single-message designation (README §Definitions):
   "pair_msg": <pair structure> }

Pair entry (asserts NON-locality of a reading; rung is always "nonlocal"
and datum_kind is "transcript" — the lemma then denies both rungs):
  {"item": int, "reading": str, "rung": "nonlocal", "eligible": bool,
   "kind": "pair", "pair": {"datum_kind": "transcript", "datum": obj,
   "contexts": [{"desc": str, "channel": str, "verdict": bool,
                 "quote": str}, <same, opposite verdict>]}}

FAILS entry (an attempted construction that did not succeed — an honest
outcome, not evidence of impossibility):
  {"item": int, "rung": str, "reading": str, "reason": str,
   "channel": str}

Item outcome = set of rungs of eligible entries that pass all mechanical
checks. Contradiction flag: a validator and a pair sharing an item and an
identical reading string, where the pair denies the validator's rung.
"""
import inspect
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent

CHANNELS = {"other-messages", "secret-material", "clock", "party-conduct",
            "counterparty-config", "deployment-policy", "private-intent",
            "generation-process", "prior-connection"}
RUNGS = {"msg", "transcript", "nonlocal"}

# Eligible rungs per item (README §Eligibility; re-derivable via
# `profile_tls.py --eligibility`, cross-checked in self-tests when the
# archive files are present).
ELIGIBLE = {
    22: {"msg", "transcript", "nonlocal"}, 30: {"msg", "transcript"},
    31: {"msg", "transcript"}, 32: {"msg", "transcript"},
    52: {"msg", "transcript", "nonlocal"}, 55: {"msg", "nonlocal"},
    56: {"msg", "transcript"}, 57: {"msg", "transcript"},
    65: {"msg", "transcript"}, 66: {"msg", "transcript", "nonlocal"},
    67: {"msg", "transcript"}, 75: {"msg", "nonlocal"},
    79: {"transcript", "nonlocal"}, 80: {"transcript", "nonlocal"},
    89: {"transcript", "nonlocal"},
    111: {"msg", "transcript", "nonlocal"}, 122: {"msg", "nonlocal"},
    123: {"msg", "nonlocal"}, 124: {"transcript", "nonlocal"},
    147: {"msg", "transcript"}, 157: {"msg", "nonlocal"},
    164: {"msg", "nonlocal"}, 184: {"msg", "transcript"},
    187: {"nonlocal"}, 188: {"msg"}, 189: {"nonlocal"},
    197: {"transcript", "nonlocal"},
    # stable sample
    69: {"msg"}, 110: {"msg"}, 72: {"msg"},
    175: {"transcript"}, 137: {"transcript"}, 138: {"transcript"},
    178: {"nonlocal"}, 126: {"nonlocal"}, 180: {"nonlocal"},
    59: {"nonlocal"}, 53: {"nonlocal"}, 60: {"nonlocal"},
    3: {"nonlocal"}, 6: {"nonlocal"}, 133: {"nonlocal"},
    91: {"nonlocal"}, 23: {"nonlocal"},
}
ITEMS = set(ELIGIBLE)
assert len(ITEMS) == 44

# Predicted item outcomes (README §Predictions).
PRED = {}
for i in (69, 110, 72, 30, 31, 32, 56, 57, 188):
    PRED[i] = {"msg"}
for i in (175, 137, 138, 52, 67, 124):
    PRED[i] = {"transcript"}
for i in (53, 59, 60, 3, 6, 133, 91, 23, 126, 180, 178,
          55, 89, 111, 122, 123, 157, 187, 189, 197):
    PRED[i] = {"nonlocal"}
for i, rungs in ((22, {"msg", "nonlocal"}), (65, {"msg", "transcript"}),
                 (66, {"msg", "nonlocal"}), (75, {"msg", "nonlocal"}),
                 (79, {"transcript", "nonlocal"}),
                 (80, {"transcript", "nonlocal"}),
                 (147, {"msg", "transcript"}), (164, {"msg", "nonlocal"}),
                 (184, {"msg", "transcript"})):
    PRED[i] = rungs
assert set(PRED) == ITEMS

T1_ITEMS = [69, 110, 72]
T2_ITEMS = [175, 137, 138]
T3_ITEMS = [53, 59, 60, 3, 6, 133, 91, 23, 126, 180]
T5_ITEMS = [22, 65, 66, 75, 79, 80, 147, 164, 184]
T5_FLOOR = 7
T6_ITEMS = [30, 31, 32, 56, 57, 188, 52, 67, 124,
            55, 89, 111, 122, 123, 157, 187, 189, 197]
T6_FLOOR = 15
# E(i): DOMAIN+TYPESTATE strict majority of the 14 archived votes
# (counts in profile_tls.py --profile).
E_MAJ = {22, 30, 31, 32, 52, 56, 57, 65, 66, 67, 79, 80, 111, 124, 147,
         184, 69, 110, 72, 175, 137, 138}
T7_NAMED_EXCEPTIONS = {75, 111, 164, 188}


class WitnessError(Exception):
    pass


def check_pair(pair, where):
    if pair.get("datum_kind") not in ("msg", "transcript"):
        raise WitnessError("%s: bad datum_kind" % where)
    if "datum" not in pair:
        raise WitnessError("%s: pair missing datum" % where)
    ctxs = pair.get("contexts")
    if not isinstance(ctxs, list) or len(ctxs) != 2:
        raise WitnessError("%s: pair needs exactly 2 contexts" % where)
    verdicts = []
    for c in ctxs:
        if c.get("channel") not in CHANNELS:
            raise WitnessError("%s: unknown channel %r" % (where,
                                                          c.get("channel")))
        if not isinstance(c.get("verdict"), bool):
            raise WitnessError("%s: verdict must be bool" % where)
        for k in ("desc", "quote"):
            if not (isinstance(c.get(k), str) and c[k].strip()):
                raise WitnessError("%s: empty %s" % (where, k))
        verdicts.append(c["verdict"])
    if verdicts[0] == verdicts[1]:
        raise WitnessError("%s: verdicts do not differ — not a "
                           "distinguishing pair" % where)


def check_validator(w, where):
    fn = w.get("fn")
    if not callable(fn):
        raise WitnessError("%s: fn not callable" % where)
    params = inspect.signature(fn).parameters
    if len(params) != 1:
        raise WitnessError("%s: validator must take exactly one parameter "
                           "(the datum) — it takes %d" % (where, len(params)))
    acc, rej = w.get("accept"), w.get("reject")
    if not acc or not rej:
        raise WitnessError("%s: needs >=1 accept AND >=1 reject vector "
                           "(a predicate with no reject vector is vacuous)"
                           % where)
    for v in acc:
        if fn(v) is not True:
            raise WitnessError("%s: accept vector not accepted" % where)
    for v in rej:
        if fn(v) is not False:
            raise WitnessError("%s: reject vector not rejected" % where)
    if not (isinstance(w.get("quote"), str) and w["quote"].strip()):
        raise WitnessError("%s: empty quote" % where)


def check_entry(w):
    item = w.get("item")
    where = "item %s (%s)" % (item, w.get("rung"))
    if item not in ITEMS:
        raise WitnessError("%s: not in the registered item set" % where)
    if w.get("rung") not in RUNGS:
        raise WitnessError("%s: bad rung" % where)
    if not (isinstance(w.get("reading"), str) and w["reading"].strip()):
        raise WitnessError("%s: empty reading" % where)
    if not isinstance(w.get("eligible"), bool):
        raise WitnessError("%s: eligible must be bool" % where)
    if w["eligible"] and w["rung"] not in ELIGIBLE[item]:
        raise WitnessError("%s: marked eligible but rung not in the "
                           "registered eligibility table" % where)
    if w.get("kind") == "validator":
        if w["rung"] == "nonlocal":
            raise WitnessError("%s: a validator cannot have rung nonlocal"
                               % where)
        check_validator(w, where)
        if w["rung"] == "transcript":
            if "pair_msg" not in w:
                raise WitnessError("%s: transcript rung requires pair_msg"
                                   % where)
            check_pair(w["pair_msg"], where + " pair_msg")
            if w["pair_msg"]["datum_kind"] != "msg":
                raise WitnessError("%s: pair_msg must have datum_kind msg"
                                   % where)
    elif w.get("kind") == "pair":
        if w["rung"] != "nonlocal":
            raise WitnessError("%s: pair entries assert rung nonlocal"
                               % where)
        check_pair(w.get("pair", {}), where)
        if w["pair"]["datum_kind"] != "transcript":
            raise WitnessError("%s: nonlocal pair must be at transcript "
                               "granularity" % where)
    else:
        raise WitnessError("%s: bad kind" % where)


def outcomes(witnesses):
    out = {i: set() for i in ITEMS}
    for w in witnesses:
        check_entry(w)
        if w["eligible"]:
            out[w["item"]].add(w["rung"])
    # Contradiction flag: same item + identical reading, validator vs pair
    # denying that validator's rung (the README's lemma forbids both).
    for w in witnesses:
        if w["kind"] != "validator":
            continue
        for v in witnesses:
            if (v["kind"] == "pair" and v["item"] == w["item"]
                    and v["reading"] == w["reading"]):
                raise WitnessError(
                    "item %d: validator and pair share reading %r — the "
                    "lemma forbids both; resolve in the report"
                    % (w["item"], w["reading"]))
    return out


def t4_presence(witnesses):
    """T4's mechanical half: the three required artifacts exist and have
    the registered structure. Their correctness is reader-graded."""
    have_178_pair = any(
        w["item"] == 178 and w["kind"] == "pair" and w["eligible"]
        for w in witnesses)
    have_178_validator = any(
        w["item"] == 178 and w["kind"] == "validator"
        and w["rung"] == "transcript" and not w["eligible"]
        for w in witnesses)
    secret = {}
    for i in (126, 180):
        secret[i] = any(
            w["item"] == i and w["kind"] == "pair" and w["eligible"]
            and any(c["channel"] == "secret-material"
                    for c in w["pair"]["contexts"])
            for w in witnesses)
    ok = have_178_pair and have_178_validator and secret[126] and secret[180]
    detail = ("178 eligible pair=%s, 178 extra transcript-validator=%s, "
              "126 secret-pair=%s, 180 secret-pair=%s; correctness is "
              "reader-graded" % (have_178_pair, have_178_validator,
                                 secret[126], secret[180]))
    return ok, detail


def check_fails(fails):
    for f in fails:
        for k in ("item", "rung", "reading", "reason", "channel"):
            assert isinstance(f.get(k), (int, str)) and str(f[k]).strip(), \
                "FAILS entry missing/empty %s: %r" % (k, f)
        assert f["item"] in ITEMS, "FAILS item %r not registered" % f["item"]
        assert f["rung"] in RUNGS, "FAILS rung %r unknown" % f["rung"]
        assert f["channel"] in CHANNELS, \
            "FAILS channel %r not in vocabulary" % f["channel"]


def grade(out, t4=None):
    results = []

    def clause(name, ok, detail):
        results.append((name, ok, detail))

    t1 = sum(1 for i in T1_ITEMS if out[i] == {"msg"})
    clause("T1 stable-DOMAIN {msg} 3/3", t1 == 3, "%d/3" % t1)
    t2 = sum(1 for i in T2_ITEMS if out[i] == {"transcript"})
    clause("T2 stable-TYPESTATE {transcript} 3/3", t2 == 3, "%d/3" % t2)
    t3 = sum(1 for i in T3_ITEMS if out[i] == {"nonlocal"})
    clause("T3 stable-nonlocal {nonlocal} 10/10", t3 == 10, "%d/10" % t3)
    if t4 is not None:
        clause("T4 CV split, mechanical presence half", t4[0], t4[1])
    t5 = sum(1 for i in T5_ITEMS if len(out[i]) >= 2)
    t5x = sum(1 for i in T5_ITEMS if out[i] == PRED[i])
    clause("T5 contested multi-rung >=%d/9" % T5_FLOOR, t5 >= T5_FLOOR,
           "%d/9 multi (exact-set %d/9)" % (t5, t5x))
    t6 = sum(1 for i in T6_ITEMS if out[i] == PRED[i])
    clause("T6 contested single-rung exact >=%d/18" % T6_FLOOR,
           t6 >= T6_FLOOR, "%d/18" % t6)
    mism = {i for i in ITEMS
            if bool(out[i] & {"msg", "transcript"}) != (i in E_MAJ)}
    unnamed = sorted(mism - T7_NAMED_EXCEPTIONS)
    named = len(mism & T7_NAMED_EXCEPTIONS)
    clause("T7 headline: 0 unnamed mismatches AND >=3/4 named",
           not unnamed and named >= 3,
           "unnamed=%s named=%d/4" % (unnamed, named))
    return results, mism


def self_test():
    ok_pair = {"datum_kind": "transcript", "datum": {"x": 1}, "contexts": [
        {"desc": "a", "channel": "clock", "verdict": True, "quote": "q"},
        {"desc": "b", "channel": "clock", "verdict": False, "quote": "q"}]}
    base = {"item": 133, "reading": "r", "rung": "nonlocal",
            "eligible": True, "kind": "pair", "pair": ok_pair}
    check_entry(dict(base))  # the fixture itself must pass

    def must_fail(entry, why):
        try:
            check_entry(entry)
        except WitnessError:
            return
        raise AssertionError("mutant not rejected: %s" % why)

    v = {"item": 69, "reading": "r", "rung": "msg", "eligible": True,
         "kind": "validator", "fn": lambda d: bool(d.get("ok")),
         "accept": [{"ok": 1}], "reject": [{}], "quote": "q"}
    check_entry(dict(v))
    must_fail({**v, "fn": lambda a, b: True}, "arity-2 validator")
    must_fail({**v, "reject": []}, "no reject vectors")
    must_fail({**v, "fn": lambda d: True}, "reject vector accepted")
    bad = {**base, "pair": {**ok_pair, "contexts": [
        dict(ok_pair["contexts"][0]), dict(ok_pair["contexts"][0])]}}
    must_fail(bad, "same-verdict pair")
    bad = {**base, "pair": {**ok_pair, "contexts": [
        {**ok_pair["contexts"][0], "channel": "vibes"},
        ok_pair["contexts"][1]]}}
    must_fail(bad, "unknown channel")
    must_fail({**base, "rung": "msg"}, "pair at rung msg")
    must_fail({**v, "item": 133}, "eligible validator outside table")
    # FAILS-validation mutants.
    ok_fail = {"item": 55, "rung": "msg", "reading": "r",
               "reason": "why", "channel": "party-conduct"}
    check_fails([dict(ok_fail)])
    for bad in ({**ok_fail, "channel": "vibes"},
                {**ok_fail, "rung": "wire"},
                {**ok_fail, "item": 1},
                {**ok_fail, "reason": " "}):
        try:
            check_fails([bad])
            raise SystemExit("FAILS mutant not rejected: %r" % bad)
        except AssertionError:
            pass
    # Grading mutants: perfect-prediction outcomes pass every counted
    # clause; per-clause flips must break exactly their clause.
    perfect = {i: set(PRED[i]) for i in ITEMS}
    res, _ = grade(perfect)
    for name, ok, _d in res:
        assert ok is not False, "perfect outcomes fail %s" % name

    def flipped(item, new, prefix):
        broken = {i: set(PRED[i]) for i in ITEMS}
        broken[item] = new
        res_b, _m = grade(broken)
        ok_b = [ok for name, ok, _d in res_b
                if name.startswith(prefix)][0]
        assert ok_b is False, "grading mutant %s/%s did not fire" % (
            item, prefix)

    flipped(69, {"nonlocal"}, "T1")
    flipped(175, {"msg"}, "T2")
    flipped(133, {"msg"}, "T3")
    # T5: floor 7/9 — two multi-rung items collapsing to one rung.
    broken = {i: set(PRED[i]) for i in ITEMS}
    broken[22], broken[65], broken[75] = {"msg"}, {"msg"}, {"msg"}
    res_b, _m = grade(broken)
    assert [ok for n, ok, _d in res_b if n.startswith("T5")][0] is False, \
        "T5 grading mutant did not fire"
    # T6: floor 15/18 — four exact-match misses.
    broken = {i: set(PRED[i]) for i in ITEMS}
    for i in (30, 31, 32, 56):
        broken[i] = {"msg", "transcript"}
    res_b, _m = grade(broken)
    assert [ok for n, ok, _d in res_b if n.startswith("T6")][0] is False, \
        "T6 grading mutant did not fire"
    # T7: an unnamed mismatch (52 losing its local rung).
    broken = {i: set(PRED[i]) for i in ITEMS}
    broken[52] = {"nonlocal"}
    res_b, _m = grade(broken)
    assert [ok for n, ok, _d in res_b if n.startswith("T7")][0] is False, \
        "T7 grading mutant did not fire"
    # T4 presence mutant: an empty witness list must fail the presence
    # half; a minimal synthetic trio must pass it.
    ok4, _d4 = t4_presence([])
    assert ok4 is False, "T4 presence mutant did not fire"
    sec_pair = {"datum_kind": "transcript", "datum": 0, "contexts": [
        {"desc": "a", "channel": "secret-material", "verdict": True,
         "quote": "q"},
        {"desc": "b", "channel": "secret-material", "verdict": False,
         "quote": "q"}]}
    trio = [
        {"item": 178, "kind": "pair", "eligible": True, "pair": sec_pair},
        {"item": 178, "kind": "validator", "rung": "transcript",
         "eligible": False},
        {"item": 126, "kind": "pair", "eligible": True, "pair": sec_pair},
        {"item": 180, "kind": "pair", "eligible": True, "pair": sec_pair},
    ]
    ok4, _d4 = t4_presence(trio)
    assert ok4 is True, "T4 presence check failed its positive fixture"
    # Cross-check the embedded ELIGIBLE table against the derivation tool.
    # Unconditional: the archive reports ship in this repository, so a
    # missing file is a failure, not a skip.
    sys.path.insert(0, str(HERE))
    import profile_tls
    maps, _torn = profile_tls.load_all()
    prof, _order = profile_tls.profile(maps)
    derived = profile_tls.eligibility(prof)
    for i in ITEMS:
        assert derived[i] == ELIGIBLE[i], (
            "eligibility drift at %d: derived %s, embedded %s"
            % (i, sorted(derived[i]), sorted(ELIGIBLE[i])))
    derived_emaj = {i for i in ITEMS
                    if sum(c for l, c in prof[i][0].items()
                           if l in ("DOMAIN", "TYPESTATE")) > 7}
    assert derived_emaj == E_MAJ, (
        "E_MAJ drift: derived-only %s, embedded-only %s"
        % (sorted(derived_emaj - E_MAJ), sorted(E_MAJ - derived_emaj)))
    print("self-tests: all rejection paths fire; grading mutants fire "
          "for every counted clause (T1-T3, T5-T7) and T4's presence "
          "half; FAILS validation fires; eligibility and E_MAJ tables "
          "match the archive derivation")


def main():
    self_test()
    wpath = HERE / "witnesses.py"
    if not wpath.exists():
        print("no witnesses.py yet — registration-time run, nothing to "
              "grade")
        return
    sys.path.insert(0, str(HERE))
    import witnesses
    out = outcomes(witnesses.WITNESSES)
    check_fails(witnesses.FAILS)
    print("witness entries: %d (+%d recorded construction failures)"
          % (len(witnesses.WITNESSES), len(witnesses.FAILS)))
    for i in sorted(ITEMS):
        marker = "" if out[i] == PRED[i] else "   <- predicted %s" % (
            sorted(PRED[i]),)
        print("%3d  %-25s%s" % (i, ",".join(sorted(out[i])) or "-", marker))
    res, mism = grade(out, t4=t4_presence(witnesses.WITNESSES))
    print()
    for name, ok, detail in res:
        tag = {True: "PASS", False: "FAIL", None: "REPORT"}[ok]
        print("%-6s %s — %s" % (tag, name, detail))
    print("T7 mismatch set: %s" % sorted(mism))


if __name__ == "__main__":
    main()
