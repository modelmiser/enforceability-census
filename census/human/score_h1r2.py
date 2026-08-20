#!/usr/bin/env python3
"""Scorer for the human-rater pass H1-R2 (census/human/).

Run from the repository root:
    python3 census/human/score_h1r2.py            # KAT self-test (no rater needed)
    python3 census/human/score_h1r2.py labels.txt # score a 60-line label file

The KAT re-derives the frozen sample from its seed and the J5 set, verifies
the packet's embedded pack section is byte-identical to the frozen v6 pack,
re-scores all eight archived iCalendar raters restricted to the sample
(asserting the measured numbers recorded in the registration), and exhibits
the fail branches. A KAT mismatch is a protocol event, not something to fix
silently.
"""
import re, random, sys, os

ALIAS = {'UNCLASSIFIED': 'U', 'NEGOTIATION': 'NEG', 'CRYPTO-VERIFY': 'CV'}
VALID = {'DOMAIN', 'TYPESTATE', 'REVOCABLE', 'THRESHOLD', 'CV', 'NEG',
         'PROCESS', 'POLICY', 'META', 'U'}

def norm(l):
    return ALIAS.get(l.rstrip('?'), l.rstrip('?')) if l else l

# ---- frozen sample (registration: census/human/README.md) ----
OUT20 = [1, 2, 7, 37, 46, 47, 69, 77, 79, 118, 138, 141, 185,
         192, 193, 194, 200, 201, 203, 204]
FAM9 = [13, 16, 22, 25, 27, 28, 91, 146, 210]
J4 = [62, 150]
DRAW29 = [3, 17, 21, 23, 26, 34, 40, 63, 64, 65, 81, 82, 84, 92, 98,
          111, 114, 115, 122, 124, 134, 148, 149, 151, 169, 175, 180,
          213, 214]
SAMPLE = sorted(OUT20 + FAM9 + J4 + DRAW29)
assert len(SAMPLE) == 60 and len(set(SAMPLE)) == 60

def j5_set():
    reg = open('census/v6-pass/README.md').read()
    m = re.search(r'J5.*?Items \(derived[^)]*\):\s*(.*?)\. The archives',
                  reg, re.S)
    S = []
    for part in re.split(r',\s*', m.group(1).replace('\n', ' ')):
        part = part.strip()
        if '–' in part:
            a, b = map(int, part.split('–')); S += range(a, b + 1)
        elif part:
            S.append(int(part))
    assert len(S) == 194
    return S

def rederive_sample():
    """DRAW29 must be reproducible from the seed — a mismatch is a protocol event."""
    S = j5_set()
    rng = random.Random("enforceability-census-human-h1")
    draw = sorted(rng.sample(S, 29))
    assert draw == DRAW29, "seeded draw does not reproduce the frozen DRAW29"
    assert not set(OUT20) & set(S) and not set(FAM9) & set(S) \
        and not set(J4) & set(S)

def v6_pair():
    t = open('census/v6-pass/rfc-v6-pass.md').read()
    b = re.findall(r'```\n(.*?)\n```', t, re.S)
    A = {int(a): x for a, x in re.findall(r'(\d+):([A-Z-]+\??)', b[0])}
    X = {int(a): x for a, x in re.findall(r'(\d+):([A-Z-]+\??)', b[1])}
    assert sorted(A) == list(range(1, 226)) and sorted(X) == list(range(1, 226))
    return A, X

def verify_packet():
    """The packet's embedded pack section must be byte-identical to the frozen pack."""
    pack = open('codebook/rater-pack-v6.md').read()
    pkt = open('census/human/packet-h1r2.md').read()
    m = re.search(r'(?s)<!-- PACK-BEGIN -->\n(.*)\n<!-- PACK-END -->', pkt)
    assert m and m.group(1) == pack, "packet pack section != codebook/rater-pack-v6.md"

CLASS_TOKENS = (r'DOMAIN|THRESHOLD|REVOCABLE|TYPESTATE|CRYPTO-VERIFY|CV|'
                r'NEGOTIATION|NEG|PROCESS|POLICY|UNCLASSIFIED|META|U')

def answer_leaks(path):
    """Answer-shaped NUMBER:CLASS tokens appearing BEFORE the item list.

    The v1 packet stated its return format with two such tokens on real graded
    items (13:PROCESS, 62:DOMAIN?). Byte-identity of the embedded pack could not
    see it: the leak lived in the packet's instructions, not its data. Item 13 is
    one of H2's nine and one of Xv5's four misses, so that single token converted
    the archive's largest measured FAILING branch (5/9) into a PASS at the floor
    (6/9). This function is that check, made mechanical.
    """
    head = open(path).read().split('## The items')[0]
    return re.findall(r'\b(\d+)\s*:\s*(' + CLASS_TOKENS + r')\b', head, re.I)

def verify_no_answer_leak(path='census/human/packet-h1r2.md'):
    leaks = answer_leaks(path)
    assert not leaks, f"answer-shaped token(s) before the item list: {leaks}"


def parse_labels(lines):
    """The serving path's parser. Factored out so the KAT exercises the same code.

    Duplicate item numbers are a HARD ERROR, not last-wins. Added 2026-08-20
    (round 3): a rater who revises an answer by appending a corrected line -- an
    ordinary thing to do on paper or in a text file -- was previously scored
    silently on the last occurrence, with no warning and no protocol event. A
    silent wrong answer is worse than a loud rejection.
    """
    lab = {}
    for ln in lines:
        m = re.match(r'\s*(\d+)\s*:\s*([A-Za-z?-]+)\s*$', ln)
        if m:
            n = int(m.group(1))
            assert n not in lab, (
                "item %d answered more than once (%r then %r) -- a protocol event; "
                "resolve with the rater, do not guess" % (n, lab[n], m.group(2).upper()))
            lab[n] = m.group(2).upper()
    return lab

def verify_serving_path():
    """Exercise the path a human's returned lines actually travel.

    Added 2026-08-20 after cold review: the KAT exercised archived label MAPS and
    never the label-FILE parser, which is the path the registration exists to
    certify. Asserted-once verification is what this registration's own lesson
    ("a guard never seen failing is not a guard") rules out.
    """
    inv = {v: k for k, v in ALIAS.items()}
    av6 = dict(archived()[6][1])
    lines = []
    for n, i in enumerate(sorted(SAMPLE)):
        lab = av6[i].rstrip('?')
        lab = inv.get(lab, lab)                    # full names, as the packet lists them
        lines.append(f'{i}:{lab}' + ('?' if n % 7 == 0 else ''))
    got = score(parse_labels(lines))
    assert got['H1'] == (29, True) and got['H2'] == (9, True) \
        and got['match_v6_of_60'] == 60 and got['torn'] == 9, got
    # every alias and case form a rater could plausibly return
    forms = ['12:CRYPTO-VERIFY', '12:CRYPTO-VERIFY?', '12:NEGOTIATION', '12:NEGOTIATION?',
             '12:UNCLASSIFIED', '12:CV', '12:NEG', '12:U', '12:U?', ' 12 : DOMAIN ',
             '12:domain', '12:META', '12:POLICY']
    for f in forms:
        p = parse_labels([f])
        assert p, f'serving parser rejected {f!r}'
        raw = p[12].rstrip('?')
        assert ALIAS.get(raw, raw) in VALID, f'{f!r} -> {raw} not in VALID'
    # negative control: the parser must REJECT malformed returns
    for bad in ['12 DOMAIN', 'twelve:DOMAIN', '12:DOM AIN', '']:
        assert not parse_labels([bad]), f'parser wrongly accepted {bad!r}'
    # negative control: a duplicated item must RAISE, not silently last-wins
    try:
        parse_labels(['13:PROCESS', '13:DOMAIN'])
        raise SystemExit('duplicate-item guard did not fire')
    except AssertionError:
        pass
    # every conforming line must survive parsing -- no silent drops
    ok = [f'{i}:DOMAIN' for i in sorted(SAMPLE)]
    assert len(parse_labels(ok)) == len(ok) == 60
    # the packet's own label list must match VALID token-for-token
    head = open('census/human/packet-h1r2.md').read().split('<!-- PACK-BEGIN -->')[0]
    listed = {x.strip().rstrip('.') for x in
              re.split(r'[,\n]', re.search(r'Valid labels:(.*?)\n\n', head, re.S).group(1))
              if x.strip().rstrip('.').isupper() and len(x.strip()) > 1}
    assert {ALIAS.get(x, x) for x in listed} == set(VALID), listed


def score(lab):
    """lab: {item: label} covering at least the 60 sample items."""
    missing = [i for i in SAMPLE if i not in lab]
    assert not missing, f"missing labels for items {missing}"
    bad = [i for i in SAMPLE if norm(lab[i]) not in VALID]
    assert not bad, f"invalid labels at items {bad}"
    A6, X6 = v6_pair()
    h1 = sum(1 for i in DRAW29 if norm(lab[i]) == 'DOMAIN')
    h2 = sum(1 for i in FAM9 if norm(lab[i]) == 'PROCESS')
    match6 = sum(1 for i in SAMPLE
                 if norm(lab[i]) in (norm(A6[i]), norm(X6[i])))
    torn = sum(1 for i in SAMPLE if lab[i].endswith('?'))
    by_stratum = {'S-OUT': sum(1 for i in OUT20
                               if norm(lab[i]) in (norm(A6[i]), norm(X6[i]))),
                  'S-FAM': sum(1 for i in FAM9 + J4
                               if norm(lab[i]) in (norm(A6[i]), norm(X6[i]))),
                  'S-J5': sum(1 for i in DRAW29
                              if norm(lab[i]) in (norm(A6[i]), norm(X6[i])))}
    return {'H1': (h1, h1 >= 25), 'H2': (h2, h2 >= 6),
            'match_by_stratum': by_stratum,
            'match_v6_of_60': match6, 'torn': torn,
            'J4': {i: lab[i] for i in J4},
            'outside': {i: lab[i] for i in OUT20},
            'dist': {c: sum(1 for i in SAMPLE if norm(lab[i]) == c)
                     for c in sorted({norm(lab[i]) for i in SAMPLE})}}

# ---- archived-rater loading (same extraction as the validated probe scorer) ----
def parse_runs(body):
    toks = re.findall(r'\b(\d+):([A-Z-]+\??)', body)
    runs, cur, last = [], {}, None
    for a, b in toks:
        a = int(a)
        if last is not None and a <= last and cur:
            runs.append(cur); cur = {}
        cur[a] = b; last = a
    if cur:
        runs.append(cur)
    return runs

def blocks(p):
    t = open(p).read()
    m = re.search(r'(?m)^#+ [Rr]aw labels.*$', t)
    return parse_runs(t[m.start():])

def archived():
    Ai, Xi = blocks('census/ical/rfc5545-census.md')
    Av4i, Xv4i = blocks('census/v4-ical/rfc5545-v4pass.md')
    t5 = open('census/v5-completion/rfc-v5-completion.md').read()
    secs = re.split(r'(?m)^## Raw labels \((TLS|RFC 9001|iCalendar)[^)]*\)$', t5)
    Av5, Xv5 = {secs[i]: parse_runs(secs[i + 1])
                for i in range(1, len(secs), 2)}['iCalendar']
    A6, X6 = v6_pair()
    return [('Ai', Ai), ('Xi', Xi), ('Av4i', Av4i), ('Xv4i', Xv4i),
            ('Av5', Av5), ('Xv5', Xv5), ('Av6', A6), ('Xv6', X6)]

# KAT expectations: (H1 of 29, H2 of 9, match of 60) — measured at registration.
KAT_EXPECT = {'Ai': (29, 9, 58), 'Xi': (29, 9, 54), 'Av4i': (29, 9, 59),
              'Xv4i': (29, 9, 54), 'Av5': (29, 0, 50), 'Xv5': (29, 5, 55),
              'Av6': (29, 9, 60), 'Xv6': (29, 9, 60)}

def kat():
    rederive_sample()
    verify_packet()
    rows = []
    for nm, r in archived():
        s = score(r)
        rows.append((nm, s['H1'][0], s['H2'][0], s['match_v6_of_60']))
    for nm, h1, h2, m6 in rows:
        assert KAT_EXPECT[nm] == (h1, h2, m6), (nm, h1, h2, m6)
        print(f"{nm:6s} H1 {h1}/29  H2 {h2}/9  match {m6}/60")
    # fail branches (measured at registration, asserted here so they stay exhibited):
    # shuffle mutant — H1 24/29 FAIL (25 is the smallest floor the shuffle's 24
    # fails, and the floor is exactly 25), H2 1/9 FAIL, match 31.
    A6, _ = v6_pair()
    vals = [A6[i] for i in range(1, 226)]
    random.Random("human-mutant-1").shuffle(vals)
    mut = {i + 1: v for i, v in enumerate(vals)}
    sm = score(mut)
    assert sm['H1'] == (24, False) and sm['H2'] == (1, False) \
        and sm['match_v6_of_60'] == 31, sm
    print(f"mutant H1 {sm['H1']}  H2 {sm['H2']}  match {sm['match_v6_of_60']}/60")
    # constant-DOMAIN — passes H1 by construction (disclosed in the
    # registration: H1 alone refutes neither degenerate), fails H2, match 36.
    sc = score({i: 'DOMAIN' for i in SAMPLE})
    assert sc['H1'] == (29, True) and sc['H2'] == (0, False) \
        and sc['match_v6_of_60'] == 36, sc
    print(f"const-DOMAIN H1 {sc['H1']}  H2 {sc['H2']}  match {sc['match_v6_of_60']}/60")
    verify_no_answer_leak()
    v1 = answer_leaks('census/human/packet-h1.md')
    assert v1, "negative control did not fire: v1 packet should leak"
    assert {(a, b.upper()) for a, b in v1} == {('13', 'PROCESS'), ('62', 'DOMAIN')}, v1
    print(f"leak guard: r2 packet clean; fires on v1 packet -> {v1}")
    verify_serving_path()
    print("serving path: Av6 round-trip identical; 13 alias/case forms parse; "
          "4 malformed returns rejected; packet label list == VALID.")
    print("KAT: 8 archived scores exact; H1/H2 fail branches exhibited; "
          "packet pack section byte-identical; answer-leak guard clean "
          "and negative-controlled; serving path exercised. SCORER VALIDATED.")
    return rows, sm

if __name__ == '__main__':
    if len(sys.argv) == 1:
        kat()
    else:
        lab = parse_labels(open(sys.argv[1]))
        rederive_sample(); verify_packet(); verify_no_answer_leak()
        s = score(lab)
        for k, v in s.items():
            print(k, v)
