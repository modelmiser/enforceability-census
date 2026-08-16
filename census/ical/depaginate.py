#!/usr/bin/env python3
"""Depaginate a pre-v3 (paginated) RFC .txt so the frozen sentence-extraction
recipe (written for unpaginated v3-format RFCs) applies.

Page furniture in these files is the fixed block
    [blank lines] footer("... [Page N]") FF-line header("RFC NNNN ... YYYY") [blank lines]
inserted between any two content lines — mid-paragraph or between
paragraphs. Each maximal furniture block is replaced by either

  - NOTHING (the two sides rejoin into one paragraph), iff the first
    non-blank content line after the block starts with a lowercase letter
    (after stripping an ABNF-comment ';' prefix), OR the last non-blank
    content line before it does not end in sentence-terminal punctuation
    ([.?!:]); or
  - ONE blank line (an ordinary paragraph break) otherwise.

The rule is deterministic; every JOIN decision is printed with its
surrounding text so the freeze-time audit can verify each one by eye.

Usage: depaginate.py in.txt out.txt
"""
import re, sys

FOOTER = re.compile(r'\[Page \d+\]\s*$')

def main(inp, out):
    lines = open(inp).read().split('\n')
    n = len(lines)
    keep, i, joins, breaks = [], 0, [], 0
    while i < n:
        if FOOTER.search(lines[i]) and i + 2 < n and '\f' in lines[i+1]:
            j = len(keep)
            while j > 0 and not keep[j-1].strip():
                j -= 1
            keep[:] = keep[:j]                      # drop blanks before footer
            k = i + 3                               # skip footer, FF, header
            while k < n and not lines[k].strip():
                k += 1                              # skip blanks after header
            prev = keep[-1] if keep else ''
            nxt = lines[k] if k < n else ''
            nxt_body = nxt.strip().lstrip(';').strip()
            join = bool(prev.strip()) and bool(nxt_body) and (
                (nxt_body[:1].islower()) or not re.search(r'[.?!:]\s*$', prev))
            if join:
                joins.append((prev.strip()[-60:], nxt.strip()[:60]))
            else:
                keep.append('')
                breaks += 1
            i = k
        else:
            keep.append(lines[i])
            i += 1
    with open(out, 'w') as f:
        f.write('\n'.join(keep))
    print(f'{len(joins)} joins, {breaks} paragraph breaks, {len(keep)} lines -> {out}')
    for a, b in joins:
        print(f'  JOIN: ...{a} || {b}...')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
