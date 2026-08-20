#!/usr/bin/env python3
"""MECH-PROBE-1 grader. Re-derives every TABLE CELL in README.md from shipped artifacts.

Scope, corrected 2026-08-20 (round-2 review): this derives coverage, both covered
agreements, both constant baselines, both shuffles, and the whole-corpus cells. It does
NOT derive the error counts (11/30, 8/26), the dead-pattern count, or the per-item
pattern table -- those are stated in README.md and checked by hand.

Bare invocation runs the known-answer test. Added 2026-08-20 by the cold-review
correction (C5): the shuffle baseline was previously unreproducible -- no seed,
no procedure, and PLAN.md step 5 made it load-bearing for the verdict.

Run from the repository root.
"""
import re, sys, random, collections, hashlib

CORPUS = 'census/mls/rfc9420_s5-15_musts.txt'
CENSUS = 'census/mls/rfc9420-census.md'
PRED   = 'census/mech-probe/pred.txt'
CLF    = 'census/mech-probe/mech1.py'
CLF_MD5 = 'b8739771e855ade2acc6829d9f867614'
SEED   = 20260820           # the shuffle seed, recorded here because it was not before
ALIAS  = {'UNCLASSIFIED': 'U', 'NEGOTIATION': 'NEG', 'CRYPTO-VERIFY': 'CV'}

def predictions():
    return {int(a): b for a, b in
            (l.strip().split(':') for l in open(PRED) if ':' in l)}

def archived():
    t = open(CENSUS).read()
    m = re.search(r'(?mi)^#+ .*raw labels.*$', t)
    out = []
    for b in re.findall(r'```\n(.*?)\n```', t[m.start():], re.S):
        d = {int(a): ALIAS.get(x.rstrip('?'), x.rstrip('?'))
             for a, x in re.findall(r'(\d+):([A-Z-]+\??)', b)}
        if len(d) > 100:
            out.append(d)
    return out                      # [A-prime, B-prime]

def score(pred, R, covered_only):
    keys = [i for i in sorted(pred) if i in R
            and (pred[i] != 'UNCLASSIFIED' or not covered_only)]
    norm = {i: ('U' if pred[i] == 'UNCLASSIFIED' else pred[i]) for i in keys}
    agree = sum(1 for i in keys if norm[i] == R[i])
    mode  = collections.Counter(R[i] for i in keys).most_common(1)[0]
    truth = [R[i] for i in keys]
    sh = truth[:]; random.Random(SEED).shuffle(sh)
    shuf = sum(1 for a, b in zip(truth, sh) if a == b)
    return dict(n=len(keys), agree=agree, const=mode, shuffle=shuf)

def kat():
    got = hashlib.md5(open(CLF, 'rb').read()).hexdigest()
    assert got == CLF_MD5, f'classifier md5 drift: {got}'
    pred = predictions()
    assert len(pred) == 127, len(pred)
    # (H, round 2) pred.txt must regenerate from the frozen classifier -- C4 leans on this
    # as circumstantial evidence; it is one assert away from being a standing check.
    import importlib.util
    sp = importlib.util.spec_from_file_location('_m', CLF)
    _m = importlib.util.module_from_spec(sp); sp.loader.exec_module(_m)
    regen = {}
    for ln in open(CORPUS):
        g = re.match(r'\[(\d+)\]\s*(.+)', ln.strip())
        if g:
            regen[int(g.group(1))] = _m.classify(g.group(2))[0]
    assert regen == pred, 'pred.txt does not regenerate from mech1.py'
    cov = [i for i in pred if pred[i] != 'UNCLASSIFIED']
    assert len(cov) == 56, len(cov)          # README: 56/127 = 44.1%
    A, B = archived()
    exp_cov   = [(26, 16, 14), (30, 17, 12)]  # agree, const-DOMAIN, shuffle
    exp_whole = [(34, 39), (30 + 4, 42)]      # agree, const-DOMAIN  (both 34)
    for R, ec, ew in zip((A, B), exp_cov, exp_whole):
        c = score(pred, R, covered_only=True)
        assert (c['agree'], c['const'][1], c['shuffle']) == ec, c
        w = score(pred, R, covered_only=False)
        assert (w['agree'], w['const'][1]) == ew, w
    print('KAT: md5 exact; 56/127 coverage; covered agree 26/30, const 16/17, '
          'shuffle 14/12; whole-corpus agree 34/34 vs const 39/42. VALIDATED.')

if __name__ == '__main__':
    kat()
    pred = predictions()
    for nm, R in zip(('A-prime (author, non-blind)', 'B-prime (blind)'), archived()):
        c = score(pred, R, True); w = score(pred, R, False)
        print(f"\n{nm}")
        print(f"  covered only  n={c['n']:3}  classifier {c['agree']}/{c['n']} = {c['agree']/c['n']:.1%}"
              f"   const-{c['const'][0]} {c['const'][1]/c['n']:.1%}   shuffle {c['shuffle']/c['n']:.1%}")
        print(f"  WHOLE CORPUS  n={w['n']:3}  classifier {w['agree']}/{w['n']} = {w['agree']/w['n']:.1%}"
              f"   const-{w['const'][0]} {w['const'][1]/w['n']:.1%}"
              f"   shuffle {w['shuffle']/w['n']:.1%}")
        print(f"                vs const-{w['const'][0]}: "
              f"{'BELOW' if w['agree'] < w['const'][1] else 'ABOVE'}    "
              f"vs shuffle: {'BELOW' if w['agree'] < w['shuffle'] else 'ABOVE'}"
              "   (PLAN.md step 5: must beat BOTH)")
