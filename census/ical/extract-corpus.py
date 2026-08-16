#!/usr/bin/env python3
r"""Extract the MUST/SHALL sentence corpus from an RFC v3 .txt — the frozen
recipe of the RFC 8446/MLS/QUIC censuses (restrict to a line range, join
paragraphs, split sentences within paragraphs, filter \bMUST\b|\bSHALL\b;
numbered section-heading lines dropped), plus TWO disclosed mechanical
refinements for the iCalendar genre:

  (a) ABNF comment lines (stripped form starts with ';') are stripped of
  their ';' prefixes and joined as their OWN paragraphs, in document
  order; they never join with surrounding prose or ABNF definition lines,
  and a bare ';' line breaks a comment paragraph the way a blank line
  breaks prose.

  (b) A prose paragraph whose FIRST line has iCalendar content-line shape
  (an unquoted NAME immediately followed by ':' or ';' — regex
  ^\s*[A-Z][A-Z0-9-]*[;:]\S) is EXAMPLE DATA and is dropped: RFC 5545's
  normative prose always quotes property names ("DTSTART"), while its
  example blocks are literal content lines whose free-text VALUES can
  contain the word MUST (the "Phoenix design team MUST attend this
  meeting" hazard — sample calendar data, not an RFC 2119 obligation).
  MUST/SHALL tokens inside dropped example paragraphs are counted and
  reported so token conservation stays exact.

Reason (measured before this recipe was fixed): RFC 5545 states its
per-property cardinality obligations ("...MUST NOT occur more than once")
inside ABNF comments, mostly with no prose counterpart — excluding comment
lines would censor that family; including them raw glues fold-broken ';'
fragments onto prose. Prose handling is otherwise the frozen recipe
verbatim: non-comment ABNF definition lines join paragraphs exactly as any
other non-blank line, which is safe because they carry no MUST/SHALL
tokens and are blank-line-separated from prose (both verified for the
censused span at freeze time).

Usage: extract-corpus.py rfc.txt START END out.txt   (1-indexed, inclusive)"""
import re, sys

HEADING = re.compile(r'^\d+(\.\d+)*\.\s+\S')
COMMENT = re.compile(r'^\s*;')

def sentences(par):
    protected = re.sub(r'\b(e\.g|i\.e|cf|vs|etc)\.', r'\1<DOT>', par)
    protected = re.sub(r'(Section(?:s)? \d+(?:\.\d+)*)\.(?=\d)', r'\1<DOT>', protected)
    return [s.replace('<DOT>', '.').strip()
            for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"(])', protected)]

CONTENT_LINE = re.compile(r'\s*[A-Z][A-Z0-9-]*[;:]\S')

def main(path, start, end, out):
    lines = open(path).read().split('\n')[start-1:end]
    paras, prose, com, dropped = [], [], [], []
    def flush(buf):
        if not buf: return
        if buf is prose and CONTENT_LINE.match(buf[0]):
            dropped.append(' '.join(buf))
        else:
            paras.append(' '.join(buf))
        buf.clear()
    for l in lines:
        if HEADING.match(l):
            flush(prose); flush(com); continue
        if not l.strip():
            flush(prose); flush(com); continue
        if COMMENT.match(l):
            flush(prose)
            body = l.strip().lstrip(';').strip()
            if body: com.append(body)
            else: flush(com)
        else:
            flush(com)
            prose.append(l.strip())
    flush(prose); flush(com)
    pat = re.compile(r'\bMUST\b|\bSHALL\b')
    hits = [s for p in paras for s in sentences(p) if pat.search(s)]
    with open(out, 'w') as f:
        for i, s in enumerate(hits, 1):
            f.write(f"[{i}] {s}\n")
    src_tokens = sum(len(pat.findall(l)) for l in lines)
    out_tokens = sum(len(pat.findall(s)) for s in hits)
    ex_tokens = sum(len(pat.findall(p)) for p in dropped)
    print(f"{len(hits)} MUST/SHALL sentences -> {out}; token conservation "
          f"{out_tokens}+{ex_tokens} excluded-example = {out_tokens+ex_tokens}"
          f"/{src_tokens} span MUST|SHALL occurrences; "
          f"{len(dropped)} example paragraphs dropped")
    for p in dropped:
        if pat.search(p): print(f"  EXCLUDED-EXAMPLE (carries MUST/SHALL): {p[:120]}")

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
