#!/usr/bin/env python3
"""Extract the MUST/SHALL sentence corpus from an RFC v3 .txt (same recipe as
the RFC 8446 s4 census: restrict to a line range, join paragraphs, split
sentences, filter \bMUST\b|\bSHALL\b). Sentences are split within paragraphs
(a sentence never crosses a paragraph boundary); numbered section-heading
lines are dropped so they cannot glue onto the following paragraph.

Usage: extract_mls.py rfc.txt START END out.txt   (1-indexed, inclusive)"""
import re, sys

HEADING = re.compile(r'^\d+(\.\d+)*\.\s+\S')

def sentences(par):
    protected = re.sub(r'\b(e\.g|i\.e|cf|vs|etc)\.', r'\1<DOT>', par)
    protected = re.sub(r'(Section(?:s)? \d+(?:\.\d+)*)\.(?=\d)', r'\1<DOT>', protected)
    return [s.replace('<DOT>', '.').strip()
            for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"(])', protected)]

def main(path, start, end, out):
    lines = open(path).read().split('\n')[start-1:end]
    paras, cur = [], []
    for l in lines:
        if HEADING.match(l):
            if cur: paras.append(' '.join(cur)); cur = []
            continue
        if l.strip():
            cur.append(l.strip())
        elif cur:
            paras.append(' '.join(cur)); cur = []
    if cur: paras.append(' '.join(cur))
    pat = re.compile(r'\bMUST\b|\bSHALL\b')
    hits = [s for p in paras for s in sentences(p) if pat.search(s)]
    with open(out, 'w') as f:
        for i, s in enumerate(hits, 1):
            f.write(f"[{i}] {s}\n")
    print(f"{len(hits)} MUST/SHALL sentences -> {out}")

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
