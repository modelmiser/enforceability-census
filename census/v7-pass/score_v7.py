#!/usr/bin/env python3
"""Scorer for the v7 pass (census/v7-pass/).

Run from the repository root:
    python3 census/v7-pass/score_v7.py                    # KAT self-test
    python3 census/v7-pass/score_v7.py ical labels.txt    # score a rater (corpus: ical|tls|quic)

KAT: re-derives the J5/J6 stability sets and the three outside sets,
re-scores every archived rater against the v6 anchors (asserting the
registration's measured-failability tables exactly), and exhibits the
L6/L7 fail branches via seeded label-shuffle mutants. A KAT mismatch
is a protocol event.
"""
import re, random, sys

ALIAS = {'UNCLASSIFIED': 'U', 'NEGOTIATION': 'NEG', 'CRYPTO-VERIFY': 'CV'}
VALID = {'DOMAIN', 'TYPESTATE', 'REVOCABLE', 'THRESHOLD', 'CV', 'NEG',
         'PROCESS', 'POLICY', 'META', 'U'}
N = {'ical': 225, 'tls': 204, 'quic': 281}
NINE = [13, 16, 22, 25, 27, 28, 91, 146, 210]

def norm(l):
    return ALIAS.get(l.rstrip('?'), l.rstrip('?')) if l else l

def parse_runs(body):
    """An adjacent repeated index raises (duplicate emission); a strictly
    decreasing index starts a new run (next rater's block). A non-adjacent
    repeat inside one block is indistinguishable from a new run by index
    alone — the per-rater completeness asserts downstream catch it."""
    toks = re.findall(r'\b(\d+):([A-Z-]+\??)', body)
    pairs = [(int(a), b) for a, b in toks]
    runs, cur, last = [], {}, None
    for a, b in pairs:
        if last is not None and a == last:
            raise AssertionError(f"duplicate adjacent item {a}")
        if last is not None and a < last and cur:
            runs.append(cur); cur = {}
        cur[a] = b; last = a
    if cur:
        runs.append(cur)
    return runs

def after(path, rx):
    t = open(path).read()
    m = re.search(rx, t)
    assert m, (path, rx)
    return t[m.end():]

def enum_set(rx, expect):
    reg = open('census/v6-pass/README.md').read()
    m = re.search(rx, reg, re.S)
    S = []
    for part in re.split(r',\s*', m.group(1).replace('\n', ' ')):
        part = part.strip()
        if '–' in part:
            a, b = map(int, part.split('–')); S += range(a, b + 1)
        elif part:
            S.append(int(part))
    assert len(S) == expect, len(S)
    return S

def sets():
    J5 = enum_set(r'J5.*?Items \(derived[^)]*\):\s*(.*?)\. The archives', 194)
    J6 = enum_set(r'J6.*?rfc8446-s4-v4pass\.md`\):\s*(.*?)\. Measured non-DOMAIN', 56)
    assert 62 not in J5 and 150 not in J5 and 64 not in J6
    out = {'ical': [i for i in range(1, 226)
                    if i not in set(J5) | set(NINE) | {62, 150}],
           'tls': [i for i in range(1, 205) if i not in set(J6) | {64}],
           'quic': [i for i in range(1, 282) if i != 232]}
    assert (len(out['ical']), len(out['tls']), len(out['quic'])) == (20, 147, 280)
    return J5, J6, out

def v6_anchors():
    t6 = open('census/v6-pass/rfc-v6-pass.md').read()
    s6 = re.split(r'(?m)^#+ Raw labels \((iCalendar|TLS|QUIC)[^)]*\)$', t6)
    d6 = {s6[i]: parse_runs(s6[i + 1]) for i in range(1, len(s6), 2)}
    A = {'ical': d6['iCalendar'][0], 'tls': d6['TLS'][0], 'quic': d6['QUIC'][0]}
    X = {'ical': d6['iCalendar'][1], 'tls': d6['TLS'][1], 'quic': d6['QUIC'][1]}
    for c in N:
        assert sorted(A[c]) == list(range(1, N[c] + 1))
        assert sorted(X[c]) == list(range(1, N[c] + 1))
    return A, X

FLOORS = {  # 23(a) floor (anchor-pair agreement on outside set), 23(b) bound
    'ical': (19, 0), 'tls': (134, 8), 'quic': (250, 7)}

def score(corpus, lab):
    J5, J6, OUT = sets()
    A, X = v6_anchors()
    n = N[corpus]
    missing = [i for i in range(1, n + 1) if i not in lab]
    assert not missing, f"missing labels: {missing[:8]}"
    bad = [i for i in range(1, n + 1) if norm(lab[i]) not in VALID]
    assert not bad, f"invalid labels at {bad[:8]}"
    a, x, out = A[corpus], X[corpus], OUT[corpus]
    match = sum(1 for i in out if norm(lab[i]) in (norm(a[i]), norm(x[i])))
    dep = sum(1 for i in out
              if norm(a[i]) == norm(x[i]) and norm(lab[i]) != norm(a[i]))
    fa, fb = FLOORS[corpus]
    res = {'r23a': (match, match >= fa), 'r23b': (dep, dep <= fb),
           'torn': sum(1 for i in range(1, n + 1) if lab[i].endswith('?')),
           'share': sum(1 for i in range(1, n + 1)
                        if norm(lab[i]) in ('DOMAIN', 'TYPESTATE'))}
    if corpus == 'ical':
        res['L1'] = (lab[150], norm(lab[150]) == 'PROCESS')
        res['L2'] = (lab[62], norm(lab[62]) == 'DOMAIN')
        l5 = sum(1 for i in NINE if norm(lab[i]) == 'PROCESS')
        res['L5'] = (l5, l5 == 9)
        l6 = sum(1 for i in J5 if norm(lab[i]) == 'DOMAIN')
        res['L6'] = (l6, l6 >= 193)
    if corpus == 'tls':
        res['L3'] = (lab[64], norm(lab[64]) == 'PROCESS')
        l7 = sum(1 for i in J6 if norm(lab[i]) == 'DOMAIN')
        res['L7'] = (l7, l7 >= 52)
    if corpus == 'quic':
        res['L4'] = (lab[232], norm(lab[232]) == 'PROCESS')
    return res

# ---- archived raters (measured-failability KAT) ----
def archived():
    ical, tls, quic = {}, {}, {}
    r = parse_runs(after('census/ical/rfc5545-census.md', r'(?m)^#+ [Rr]aw labels.*$'))
    ical['Ai'], ical['Xi'] = r[0], r[1]
    r = parse_runs(after('census/v4-ical/rfc5545-v4pass.md', r'(?m)^#+ [Rr]aw labels.*$'))
    ical['Av4i'], ical['Xv4i'] = r[0], r[1]
    t5 = open('census/v5-completion/rfc-v5-completion.md').read()
    secs = re.split(r'(?m)^## Raw labels \((TLS|RFC 9001|iCalendar)[^)]*\)$', t5)
    d5 = {secs[i]: parse_runs(secs[i + 1]) for i in range(1, len(secs), 2)}
    ical['Av5'], ical['Xv5'] = d5['iCalendar'][:2]
    tls['Av5'], tls['Xv5'] = d5['TLS'][:2]
    tls['D'] = parse_runs(after('census/tls13/rfc8446-s4-pass4.md', r'(?m)^#+ [Rr]aw labels.*$'))[0]
    tf = open('census/foreign/rfc8446-s4-foreign.md').read()
    tls['G'] = parse_runs(re.split(r'(?m)^## Raw labels \(rater G[^)]*\)$', tf)[1])[0]
    tls['X'] = parse_runs(re.split(r'(?m)^## Raw labels \(rater X[^)]*\)$', tf)[1])[0]
    tv4 = parse_runs(after('census/v4-tls/rfc8446-s4-v4pass.md', r'(?m)^#+ [Rr]aw labels.*$'))
    tls['Av4'], tls['Xv4'] = tv4[0], tv4[1]
    tf2 = open('census/foreign2/rfc8446-s4-foreign2.md').read()
    for s in 'MKZ':
        tls[s] = parse_runs(re.split(r'(?m)^## Raw labels \(rater %s[^)]*\)$' % s, tf2)[1])[0]
    q = parse_runs(after('census/quic/rfc9000-census.md', r'(?m)^#+ [Rr]aw labels.*$'))
    quic['A2'], quic['B2'] = q[0], q[1]
    qv4 = parse_runs(after('census/v4-completion/rfc-v4-completion.md', r'(?m)^## Raw labels \(QUIC[^)]*\)$'))
    quic['Av4'], quic['Xv4'] = qv4[0], qv4[1]
    q5 = parse_runs(after('census/v5-quic/rfc9000-v5pass.md', r'(?m)^#+ [Rr]aw labels.*$'))
    quic['Aq5'], quic['Xq5'] = q5[0], q5[1]
    qr = open('census/quic-replication/rfc9000-replication.md').read()
    quic['Aq'] = parse_runs(re.split(r'(?m)^## Raw labels \(rater Aq[^)]*\)$', qr)[1])[0]
    quic['Xq'] = parse_runs(re.split(r'(?m)^## Raw labels \(rater Xq[^)]*\)$', qr)[1])[0]
    return ical, tls, quic

# (match, dep) per archived rater vs the v6 anchors, and L-clause values —
# measured at registration; asserted on every run.
KAT23 = {
 'ical': {'Ai': (19, 1), 'Xi': (15, 5), 'Av4i': (20, 0), 'Xv4i': (15, 5),
          'Av5': (20, 0), 'Xv5': (20, 0)},
 'tls': {'Av5': (136, 8), 'Xv5': (138, 8), 'D': (131, 14), 'G': (127, 17),
         'X': (136, 8), 'Av4': (139, 7), 'Xv4': (142, 4), 'M': (127, 18),
         'K': (120, 25), 'Z': (127, 15)},
 'quic': {'A2': (242, 34), 'B2': (236, 40), 'Av4': (261, 16), 'Xv4': (243, 33),
          'Aq5': (269, 7), 'Xq5': (267, 11), 'Aq': (231, 45), 'Xq': (226, 47)},
}
KATL = {
 'ical': {'Ai': ('PROCESS', 'PROCESS', 9, 193), 'Xi': ('PROCESS', 'PROCESS', 9, 193),
          'Av4i': ('PROCESS', 'PROCESS', 9, 194), 'Xv4i': ('PROCESS', 'PROCESS', 9, 194),
          'Av5': ('DOMAIN', 'DOMAIN', 0, 194), 'Xv5': ('DOMAIN', 'DOMAIN', 5, 193)},
 'tls': {'Av5': ('DOMAIN?', 54), 'Xv5': ('DOMAIN', 54), 'D': ('PROCESS', 55),
         'G': ('PROCESS', 54), 'X': ('PROCESS', 55), 'Av4': ('PROCESS', 56),
         'Xv4': ('TYPESTATE', 56), 'M': ('PROCESS', 54), 'K': ('PROCESS', 54),
         'Z': ('PROCESS', 52)},
 'quic': {'A2': 'PROCESS', 'B2': 'DOMAIN', 'Av4': 'PROCESS', 'Xv4': 'PROCESS',
          'Aq5': 'DOMAIN', 'Xq5': 'DOMAIN', 'Aq': 'DOMAIN', 'Xq': 'PROCESS'},
}

def kat():
    J5, J6, OUT = sets()
    A, X = v6_anchors()
    ical, tls, quic = archived()
    for cname, d in (('ical', ical), ('tls', tls), ('quic', quic)):
        for nm, r in d.items():
            s = score(cname, r)
            assert (s['r23a'][0], s['r23b'][0]) == KAT23[cname][nm], \
                (cname, nm, s['r23a'], s['r23b'])
            if cname == 'ical':
                e = KATL['ical'][nm]
                assert (r[150], r[62], s['L5'][0], s['L6'][0]) == e, (nm, e)
            if cname == 'tls':
                e = KATL['tls'][nm]
                assert (r[64], s['L7'][0]) == e, (nm, e)
            if cname == 'quic':
                assert norm(r[232]) == KATL['quic'][nm], nm
            print(f"{cname:5s} {nm:5s} match {s['r23a'][0]:3d} dep {s['r23b'][0]:2d}")
    # L6/L7 fail branches via seeded shuffles of the same-family v6 anchors
    vals = [A['ical'][i] for i in range(1, 226)]
    random.Random("v7-mutant-ical").shuffle(vals)
    mi = {i + 1: v for i, v in enumerate(vals)}
    smi = score('ical', mi)
    assert smi['L6'] == (170, False), smi['L6']
    vals = [A['tls'][i] for i in range(1, 205)]
    random.Random("v7-mutant-tls").shuffle(vals)
    mt = {i + 1: v for i, v in enumerate(vals)}
    smt = score('tls', mt)
    assert smt['L7'] == (24, False), smt['L7']
    print(f"mutants: L6 {smi['L6']}  L7 {smt['L7']}  (both FAIL branches exhibited)")
    print("KAT: 24 archived rater-corpus scores exact vs the v6 anchors; "
          "every graded clause has an archived or mutant FAIL branch. "
          "SCORER VALIDATED.")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        kat()
    else:
        corpus, path = sys.argv[1], sys.argv[2]
        lab, seen = {}, set()
        for ln in open(path):
            m = re.match(r'\s*(\d+)\s*:\s*([A-Za-z?-]+)\s*$', ln)
            if m:
                i = int(m.group(1))
                assert i not in seen, f"duplicate item {i}"
                seen.add(i)
                lab[i] = m.group(2).upper()
        for k, v in score(corpus, lab).items():
            print(k, v)
