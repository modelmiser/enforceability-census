#!/usr/bin/env python3
"""Scorer for the human-rater pass H1 (census/human/).

Run from the repository root:
    python3 census/human/score_h1.py            # KAT self-test (no rater needed)
    python3 census/human/score_h1.py labels.txt # score a 60-line label file

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
    pkt = open('census/human/packet-h1.md').read()
    m = re.search(r'(?s)<!-- PACK-BEGIN -->\n(.*)\n<!-- PACK-END -->', pkt)
    assert m and m.group(1) == pack, "packet pack section != codebook/rater-pack-v6.md"

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
    print("KAT: 8 archived scores exact; H1/H2 fail branches exhibited; "
          "packet pack section byte-identical. SCORER VALIDATED.")
    return rows, sm

if __name__ == '__main__':
    if len(sys.argv) == 1:
        kat()
    else:
        lab = {}
        for ln in open(sys.argv[1]):
            m = re.match(r'\s*(\d+)\s*:\s*([A-Za-z?-]+)\s*$', ln)
            if m:
                lab[int(m.group(1))] = m.group(2).upper()
        rederive_sample(); verify_packet()
        s = score(lab)
        for k, v in s.items():
            print(k, v)
