#!/usr/bin/env python3
"""MECH-PROBE-1 — rule-based, non-LLM classifier.

Written from codebook/classes.md (four core classes + precedence rules 1,2,6)
and codebook/rater-pack-v6.md (the ten-class definitions) ALONE. No MLS label
was loaded or displayed before this file was frozen. Every pattern below cites
the definition phrase it derives from. No pattern was added or altered after
seeing agreement -- doing so would void the probe (see PLAN.md).

Precedence, declared before running, reasoning from the definitions:
  META, CV, NEG   -- distinct addressee / distinct material / distinct shape
  TYPESTATE       -- ordering over history; must precede DOMAIN (codebook: DOMAIN
                     last, else 'invalid' swallows ordering items)
  REVOCABLE       -- was-true-became-false; codebook rule 1: class 2 before class 1
  THRESHOLD       -- inequality against a chosen number (rule 1: after REVOCABLE)
  POLICY, PROCESS -- discretion / algorithm with no wire predicate of its own
  DOMAIN          -- greedy catch, deliberately LAST among substantive classes
  UNCLASSIFIED    -- rule 2: a real bucket, always reported
"""
import re, sys

def norm(s):
    # codebook rule 6: '_' is a word character; normalise before \b matching
    return re.sub(r'_', ' ', s).lower()

# (class, [patterns]) in declared precedence order
RULES = [
 ('META', [                      # "addressed to future specification authors"
    r'\bfuture (specification|document|version)', r'\bspecifications? that define',
    r'\bthis document\b.*\bregistr', r'\biana\b', r'\bregistry\b',
    r'\bdesigners? of\b', r'\bextensions? must (define|specify)']),
 ('CV', [                        # "requires secret or transcript-derived material"
    r'\bsignature\b', r'\bverif\w+ the (signature|mac|tag)', r'\bmac\b',
    r'\bhmac\b', r'\bconfirmation tag\b', r'\bmembership tag\b',
    r'\bpsk binder\b', r'\btranscript hash\b', r'\bauthenticat\w+ (tag|data)\b']),
 ('NEG', [                       # "emptiness of a two-party set intersection"
    r'\bmutually supported\b', r'\bin common\b', r'\bintersection\b',
    r'\bboth (parties|endpoints|sides) support', r'\bno (overlap|common)\b',
    r'\bnegotiat']),
 ('TYPESTATE', [                 # "ordering obligation over one object's history"
    r'\b(after|before|until|prior to|previously|already|again|twice)\b',
    r'\bmust not be sent unless\b', r'\bin response to\b', r'\bout of order\b',
    r'\bre-?use', r'\bhas (been|already)\b', r'\bsame as .*\b(sent|received|earlier)\b',
    r'\bmatch\w* the .*\b(previous|earlier|original)\b', r'\bonce\b']),
 ('REVOCABLE', [                 # "a fact that was true and became false"
    r'\bexpir', r'\bstale\b', r'\bno longer\b', r'\brevok', r'\bsupersed',
    r'\bobsolete\b', r'\bout ?dated\b', r'\blifetime\b', r'\bfreshness\b',
    r'\bremoved from\b', r'\bcurrent\w*\b.*\bepoch\b']),
 ('THRESHOLD', [                 # "an inequality against a chosen number"
    r'\bat most\b', r'\bno more than\b', r'\bat least\b', r'\bmaximum\b',
    r'\bminimum\b', r'\bexceed', r'\bgreater than\b', r'\bless than\b',
    r'\blimit\b', r'\bmust not be larger\b']),
 ('POLICY', [                    # "operator/deployment discretion, no wire predicate"
    r'\bpolic(y|ies)\b', r'\bapplication\b.*\b(decide|determine|choose)',
    r'\bdeployment\b', r'\badministrat', r'\bconfigur\w+ by\b',
    r'\bout of scope\b', r'\bimplementation[- ]defined\b', r'\blocal policy\b']),
 ('PROCESS', [                   # "algorithm/procedure, no wire-observable predicate"
    r'\bcomput', r'\bderiv', r'\bcalculat', r'\bgenerat',
    r'\bas described in\b', r'\bin the following manner\b', r'\balgorithm\b',
    r'\biterat', r'\bprocedure\b', r'\bfollow the\b', r'\bapply the\b']),
 ('DOMAIN', [                    # "monotone predicate on one value, no history"
    r'\bvalid\w*\b', r'\bmust be one of\b', r'\bformat\b', r'\blength\b',
    r'\bpresent\b', r'\bcontain', r'\bwell[- ]formed\b', r'\bencoded\b',
    r'\bmust be (identical|equal|the same)\b', r'\bmust be a\b', r'\bnon-?empty\b']),
]

def classify(text):
    t = norm(text)
    for cls, pats in RULES:
        for p in pats:
            if re.search(p, t):
                return cls, p
    return 'UNCLASSIFIED', None

if __name__ == '__main__':
    out = {}
    for ln in open(sys.argv[1]):
        m = re.match(r'\[(\d+)\]\s*(.+)', ln.strip())
        if m:
            out[int(m.group(1))] = classify(m.group(2))[0]
    for i in sorted(out):
        print(f'{i}:{out[i]}')
