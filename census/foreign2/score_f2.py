#!/usr/bin/env python3
"""Scorer for the second cross-family replication (census/foreign2/).

Run from the repository root:
    python3 census/foreign2/score_f2.py               # KAT self-test
    python3 census/foreign2/score_f2.py labels.txt    # score a 204-item label file

KAT: re-parses the archived raters G, X (census/foreign/) and D
(census/tls13/rfc8446-s4-pass4.md), re-derives every measured number the
registration quotes, and exhibits the fail branch of each graded clause
via a label-shuffle mutant. A KAT mismatch is a protocol event.
"""
import re, random, sys

ALIAS = {'UNCLASSIFIED': 'U', 'NEGOTIATION': 'NEG', 'CRYPTO-VERIFY': 'CV'}
VALID = {'DOMAIN', 'TYPESTATE', 'REVOCABLE', 'THRESHOLD', 'CV', 'NEG',
         'PROCESS', 'POLICY', 'META', 'U'}
ELIM = {'DOMAIN', 'TYPESTATE'}
N = 204
CVSET = [120, 125, 126, 178, 179, 180]
TSCLUSTER = [10, 52, 67, 129, 130, 139, 152, 159, 165]   # foreign G=X DOMAIN->TYPESTATE consensus
UCLUSTER = [187, 190, 197]                                # foreign G=X ->U consensus (report-only)

def norm(l):
    return ALIAS.get(l.rstrip('?'), l.rstrip('?')) if l else l

def parse_map(body):
    pairs = [(int(a), b) for a, b in re.findall(r'\b(\d+):([A-Z-]+\??)', body)]
    lab = dict(pairs)
    dups = [a for a in lab if [p[0] for p in pairs].count(a) > 1]
    assert not dups, f"duplicate item labels: {sorted(set(dups))}"
    return lab

def block(path, heading_rx):
    t = open(path).read()
    m = re.search(heading_rx, t)
    assert m, (path, heading_rx)
    seg = t[m.end():]
    nxt = re.search(r'(?m)^## ', seg)
    return parse_map(seg[:nxt.start()] if nxt else seg)

def archived():
    G = block('census/foreign/rfc8446-s4-foreign.md',
              r'(?m)^## Raw labels \(rater G, archived verbatim\)$')
    X = block('census/foreign/rfc8446-s4-foreign.md',
              r'(?m)^## Raw labels \(rater X, archived verbatim\)$')
    D = block('census/tls13/rfc8446-s4-pass4.md',
              r'(?m)^## Raw labels \(rater D, archived verbatim\)$')
    for nm, r in (('G', G), ('X', X), ('D', D)):
        assert sorted(r) == list(range(1, N + 1)), nm
    return G, X, D

def score(lab, D):
    missing = [i for i in range(1, N + 1) if i not in lab]
    assert not missing, f"missing labels for items {missing}"
    bad = [i for i in range(1, N + 1) if norm(lab[i]) not in VALID]
    assert not bad, f"invalid labels at items {bad}"
    elim = sum(1 for i in range(1, N + 1) if norm(lab[i]) in ELIM)
    raw_d = sum(1 for i in range(1, N + 1) if norm(lab[i]) == norm(D[i]))
    eln_d = sum(1 for i in range(1, N + 1)
                if (norm(lab[i]) in ELIM) == (norm(D[i]) in ELIM))
    cv = sum(1 for i in CVSET if norm(lab[i]) == 'CV')
    ts = sum(1 for i in TSCLUSTER if norm(lab[i]) == 'TYPESTATE')
    quot = 100.0 * elim / N
    return {'elim': elim, 'quotient_pct': round(quot, 1),
            'F6': (elim, 76.0 <= quot <= 86.0),
            'F7': (cv, cv == 6),
            'F8': (raw_d, raw_d >= 143),          # 143/204 = 70.1% >= 70%
            'F10_count': (ts, ts >= 6),
            'raw_vs_D': raw_d, 'elimnot_vs_D': eln_d,
            'ucluster': {i: lab[i] for i in UCLUSTER},
            'torn': sum(1 for i in range(1, N + 1) if lab[i].endswith('?')),
            'dist': {c: sum(1 for i in range(1, N + 1) if norm(lab[i]) == c)
                     for c in sorted({norm(lab[i]) for i in range(1, N + 1)})}}

# Measured at registration; asserted on every run.
KAT_EXPECT = {
    'G': {'elim': 156, 'raw_vs_D': 166, 'elimnot_vs_D': 187, 'cv': 6, 'ts': 9},
    'X': {'elim': 165, 'raw_vs_D': 187, 'elimnot_vs_D': 200, 'cv': 6, 'ts': 9},
    'D': {'elim': 169, 'raw_vs_D': 204, 'elimnot_vs_D': 204, 'cv': 6, 'ts': 0},
}

def agree(a, b):
    """Raw and eliminable-vs-not agreement between two full 204-item maps."""
    raw = sum(1 for i in range(1, N + 1) if norm(a[i]) == norm(b[i]))
    eln = sum(1 for i in range(1, N + 1)
              if (norm(a[i]) in ELIM) == (norm(b[i]) in ELIM))
    return raw, eln

def f9(raw_vs_d_counts):
    """F9 aggregate (existential over the three new raters): PASS iff at
    least one raw-vs-D count reaches 166."""
    return max(raw_vs_d_counts), any(r >= 166 for r in raw_vs_d_counts)

def kat():
    G, X, D = archived()
    for nm, r in (('G', G), ('X', X), ('D', D)):
        s = score(r, D)
        e = KAT_EXPECT[nm]
        if e['elim'] is not None:
            assert s['elim'] == e['elim'], (nm, s['elim'])
        assert s['raw_vs_D'] == e['raw_vs_D'], (nm, s['raw_vs_D'])
        assert s['elimnot_vs_D'] == e['elimnot_vs_D'], (nm, s['elimnot_vs_D'])
        assert s['F7'][0] == e['cv'], (nm, s['F7'])
        assert s['F10_count'][0] == e['ts'], (nm, s['F10_count'])
        print(f"{nm}: elim {s['elim']}/204 ({s['quotient_pct']}%)  "
              f"vs-D raw {s['raw_vs_D']} elim-not {s['elimnot_vs_D']}  "
              f"CV {s['F7'][0]}/6  TS-cluster {s['F10_count'][0]}/9")
    # G-vs-X cross-check (foreign report: raw 176, elim-vs-not 191)
    gx_raw = sum(1 for i in range(1, N + 1) if norm(G[i]) == norm(X[i]))
    gx_eln = sum(1 for i in range(1, N + 1)
                 if (norm(G[i]) in ELIM) == (norm(X[i]) in ELIM))
    assert (gx_raw, gx_eln) == (176, 191), (gx_raw, gx_eln)
    print(f"G-vs-X: raw {gx_raw}/204, elim-vs-not {gx_eln}/204")
    # Fail branches via shuffle mutant of X's labels (measured at registration):
    vals = [X[i] for i in range(1, N + 1)]
    random.Random("foreign2-mutant-1").shuffle(vals)
    mut = {i + 1: v for i, v in enumerate(vals)}
    sm = score(mut, D)
    assert sm['F6'][1] is True   # quotient is shuffle-invariant — F6 CANNOT
    # fail by shuffle (disclosed in the registration); its fail branch is a
    # relabel mutant: X's labels with every TYPESTATE set to PROCESS.
    relab = {i: ('PROCESS' if norm(X[i]) == 'TYPESTATE' else X[i])
             for i in range(1, N + 1)}
    sr = score(relab, D)
    assert sr['F6'] == (69, False), sr['F6']    # 69/204 = 33.8% < 76 — FAIL
    # (X's eliminable mass is TYPESTATE-heavy: 96 TYPESTATE + 69 DOMAIN)
    assert sm['F7'] == (0, False), sm['F7']
    assert sm['F8'] == (80, False), sm['F8']
    # F10's floor is 6 BECAUSE of this measurement: X's map is 96/204
    # TYPESTATE (~47%), so the shuffle scores 5/9 on the cluster — a floor
    # of 5 would be a check the shuffle degenerate passes.
    assert sm['F10_count'] == (5, False), sm['F10_count']
    assert sr['F10_count'] == (0, False), sr['F10_count']
    print(f"shuffle mutant: F7 {sm['F7']}  F8 {sm['F8']}  F10 {sm['F10_count']}"
          f"  (F6 shuffle-invariant, disclosed)")
    print(f"relabel mutant (TYPESTATE->PROCESS): F6 {sr['F6']}  F10 {sr['F10_count']}")
    # F9 fail branch: three independent shuffle mutants (one per seat) all
    # land below 166 — the all-three-below case, measured.
    muts = []
    for seed in ("foreign2-mutant-1", "foreign2-mutant-2", "foreign2-mutant-3"):
        vals = [X[i] for i in range(1, N + 1)]
        random.Random(seed).shuffle(vals)
        muts.append(score({i + 1: v for i, v in enumerate(vals)}, D)['raw_vs_D'])
    assert muts == [80, 63, 65], muts
    assert f9(muts) == (80, False), f9(muts)
    assert f9([166, 80, 63]) == (166, True)   # pass branch at the exact edge
    print(f"F9 fail branch: three shuffle mutants raw-vs-D {muts} -> {f9(muts)}")
    print("KAT: G/X/D re-derived exact; every graded clause exhibits a FAIL "
          "branch (F9's via three shuffle mutants). SCORER VALIDATED.")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        kat()
    else:
        lab, seen = {}, set()
        for ln in open(sys.argv[1]):
            m = re.match(r'\s*(\d+)\s*:\s*([A-Za-z?-]+)\s*$', ln)
            if m:
                i = int(m.group(1))
                assert i not in seen, f"duplicate item label: {i}"
                seen.add(i)
                lab[i] = m.group(2).upper()
        _, _, D = archived()
        s = score(lab, D)
        for k, v in s.items():
            print(k, v)
