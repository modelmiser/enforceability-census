#!/usr/bin/env python3
"""
Corpus 3a: Wayland protocol declared errors (core + wayland-protocols).

This corpus can express the class PromQL censors, so the taxonomy has to grow.
Classes declared BEFORE looking at counts:

  DOMAIN     monotone predicate on ONE value, no history.  "transform must be
             one of 8 enum values."  Eliminable by a plain type in generated
             bindings.  Cheapest possible fix.
  TYPESTATE  ordering / linearity obligation over one object's history.
             "already used", "committed before ack", "role assigned twice".
             Eliminable by a session or linear type across the wire.
  REVOCABLE  a fact that was true and became false.  "object is inert",
             "no longer exists".  The residue.  Needs a clock.
  THRESHOLD  bound on a numeric quantity.  Expected to be near-absent here.
  RESOURCE   the server itself failed (OOM, internal bug).  Not a client
             obligation at all; reported separately, never merged.
  AMBIGUOUS  genuinely undecidable from the declared text -- notably
             "already destroyed", which is TYPESTATE if the client destroyed
             it (use-after-free, a linearity break) and REVOCABLE if the
             server did (the fact expired underneath the client).  The
             protocol text usually does not say which.  Hand-audited.
  UNCLASSIFIED  everything else.  Mandatory.  Never absorbed.

Precedence: RESOURCE, then ordering-TYPESTATE, then REVOCABLE, then AMBIGUOUS,
then THRESHOLD, then DOMAIN.  DOMAIN is last because "invalid" is the corpus's most common word
and would otherwise swallow ordering errors that merely mention an invalid arg.

Rule-8 hardening (2026-08-09): each item is classified TWICE -- on the predicate
(summary + desc; the measurement) and on the name (a hypothesis only) -- and two
loud-failure buckets are reported that a name-based classifier structurally
cannot raise:
  DISAGREE   name-class and predicate-class are both confident but differ.  This
             is the exact shape of the 2026-08-02 retraction (`leave_orphan`,
             `server_new_id.range`); it never touched the unclassified bucket
             because the name-based classifier placed each item confidently.
  NAME-ONLY  predicate-view UNCLASSIFIED while the name-view is confident,
             so the class is a guess off the name (the item may still carry
             predicate text the vocabulary did not match).
A run with a non-empty DISAGREE bucket is telling you the two views of the corpus
do not agree -- resolve those by hand before quoting any ratio.
"""
import json, re, sys, hashlib, collections

def norm(s):
    # v2 FIX 1 (the big one): `\b` treats `_` as a WORD character, so
    # `\balready\b` never matched `already_captured` and `\bunsupported\b`
    # never matched `unsupported_buffer`.  Every snake_case entry name in this
    # corpus -- which is all of them -- silently failed to match.  Normalising
    # `_` to a space before matching repairs every boundary at once.
    return (s or '').lower().replace('_', ' ')

RESOURCE = re.compile(r'\b(no_memory|out of memory|implementation error|internal error)\b')

# ordering / linearity over one object's history
ORDER = re.compile(
    r'\b(already|twice|second time|more than once|re-?used|reassign|'
    r'before .*(commit|ack|destroy|configure|create)|'
    r'(commit|ack|destroy|configure|request|attach)\w*\s+(before|prior|after)|'
    r'untimely|out of order|not yet|has not been|never (been )?(sent|committed|acked)|'
    r'not (fully )?constructed|unconfigured|without (first|prior|having)|'
    r'destroyed before|still (in use|attached|active)|'
    r'another role|has a role|role .*(already|assigned)|duplicate|'
    # v2 FIX 2 -- PREREQUISITE-NOT-MET is typestate: the object is not yet in a
    # state where the request is legal.  Found by reading the unclassified
    # bucket, where it was the single largest missed shape.
    r'no \w+ was (set|attached|added)|sent without|requested a \w+ without|'
    r'incomplete|empty lease|not ready|inactive|requires .{0,24}to be |'
    r'has not ended|no acquire|no release|no keymap|no buffer|'
    r'not the topmost|tried to \w+ after|cannot be performed after|'
    r'sent after|while locked|not allowed)\b')

# a fact that was true and became false
REVOKE = re.compile(
    r'\b(inert|no longer|defunct|expired|stale|superseded|revoked|'
    r'destroyed object|object (was |is )?(already )?destroyed|'
    r'not (a )?(sibling|child|parent|member)|dead|gone|invalidated)\b')

AMBIG = re.compile(r'\b(already destroyed|destroyed)\b')

# v2 FIX 3 -- bounds vocabulary this corpus actually uses ("out of bounds",
# "extends outside of", "too much"), plus timeouts, which are a threshold on a
# continuous quantity wearing protocol clothing ("didn't respond to a ping in
# time" is `elapsed > deadline`).
THRESH = re.compile(r'\b(too (large|small|many|big|much)|exceed\w*|'
                    r'out of (range|bounds)|extends outside|outside of|'
                    r'negative|overflow|limit|maximum|minimum|in time|timed out)\b')

DOMAIN = re.compile(
    r'\b(invalid|unsupported|unknown|not (a )?(valid|known|supported)|'
    r'malformed|bad |illegal|unrecognized|wrong (value|type|format|device)|'
    r'missing capability|not supported|'
    # v2 FIX 4 -- relational and structural predicates on the ARGUMENTS of a
    # single request.  No history, no clock: a generated binding with real
    # types makes them unrepresentable.
    r'is not an? \w+|not seekable|could not be imported|conflicting|'
    r'incompatible|does not satisfy|nested|unauthorized|is not integer|'
    r'null buffer|does not accept|doesn.t accept|does not support)\b')


def classify_text(t):
    if RESOURCE.search(t):            return 'RESOURCE', 'server-side failure'
    if ORDER.search(t):               return 'TYPESTATE', 'ordering/linearity'
    if REVOKE.search(t):              return 'REVOCABLE', 'fact expired'
    if AMBIG.search(t):               return 'AMBIGUOUS', 'destroyed: by whom?'
    if THRESH.search(t):              return 'THRESHOLD', 'numeric bound'
    if DOMAIN.search(t):              return 'DOMAIN', 'predicate on one value'
    return 'UNCLASSIFIED', ''


def classify(r):
    # Rule 8 (added after the 2026-08-02 retraction): classify on the PREDICATE
    # (summary + desc), NEVER the identifier.  The name is classified separately
    # and used only as a hypothesis and a disagreement signal -- never as the
    # measurement.  The old classifier folded the name into the match blob, which
    # is exactly what produced the retracted headline: `leave_orphan` filed
    # REVOCABLE by its name while its gloss was a history predicate, and
    # `server_new_id.range` filed TYPESTATE by name while its predicate was a
    # bounds check.  A name-only classifier places every item confidently and so
    # can NEVER raise the two loud-failure signals set below.
    pred = norm((r.get('summary') or '') + ' ' + (r.get('desc') or ''))
    name = norm(r.get('name') or '')
    if pred.strip():
        cls_pred, why = classify_text(pred)
    else:
        cls_pred, why = 'UNCLASSIFIED', 'no predicate text'
    cls_name, _ = classify_text(name)
    r['cls'], r['why'] = cls_pred, why        # PRIMARY measurement = predicate
    r['cls_name'] = cls_name
    # DISAGREE: predicate and name both land confidently in DIFFERENT classes --
    # the signal a name-only classifier structurally cannot raise.  This is the
    # check that, had it existed, would have caught the retraction on pass 1.
    r['disagree'] = (cls_pred != 'UNCLASSIFIED' and cls_name != 'UNCLASSIFIED'
                     and cls_pred != cls_name)
    # NAME-ONLY: no usable predicate text, so the name guess is a hypothesis,
    # not a measurement -- flag it rather than silently reporting it as data.
    r['name_only'] = (cls_pred == 'UNCLASSIFIED' and cls_name != 'UNCLASSIFIED')
    return cls_pred, why


def main(path):
    rows = json.load(open(path))
    for r in rows:
        r['cls'], r['why'] = classify(r)
        # Legacy (name-inclusive) class, kept ONLY to show the rule-8 swing.
        r['cls_legacy'], _ = classify_text(norm(
            (r.get('name') or '') + ' ' + (r.get('summary') or '')
            + ' ' + (r.get('desc') or '')))
    c = collections.Counter(r['cls'] for r in rows)
    n = len(rows)
    print(f'CORPUS 3a — Wayland declared protocol errors, n={n}')
    print(f'  ({len({r["file"] for r in rows})} protocol files, '
          f'{len({r["iface"] for r in rows})} interfaces)\n')
    for k in ('DOMAIN','TYPESTATE','REVOCABLE','THRESHOLD','RESOURCE',
              'AMBIGUOUS','UNCLASSIFIED'):
        print(f'  {k:14s} {c.get(k,0):4d}  {100.0*c.get(k,0)/n:5.1f}%')

    elim = c.get('DOMAIN',0) + c.get('TYPESTATE',0)
    client = n - c.get('RESOURCE',0)
    print(f'\n  eliminable-by-a-type (DOMAIN+TYPESTATE): {elim}/{client} client-'
          f'facing = {100.0*elim/client:.1f}%')

    # Rule 3: report the swing from enforcing rule 8 (predicate-only) against the
    # old name-inclusive blob.  A large swing measures how much the headline had
    # been leaning on identifiers -- the very thing the 2026-08-02 retraction was.
    cL = collections.Counter(r['cls_legacy'] for r in rows)
    if any(c.get(k,0) != cL.get(k,0) for k in set(c) | set(cL)):
        print('\n  rule-8 swing (predicate-only vs legacy name-inclusive):')
        for k in ('DOMAIN','TYPESTATE','REVOCABLE','THRESHOLD','RESOURCE',
                  'AMBIGUOUS','UNCLASSIFIED'):
            if c.get(k,0) != cL.get(k,0):
                print(f'    {k:14s} {c.get(k,0):4d}  '
                      f'(legacy {cL.get(k,0):4d}, Δ{c.get(k,0)-cL.get(k,0):+d})')
    else:
        print('\n  rule-8 swing: none — predicate-only and name-inclusive agree.')

    dis = [r for r in rows if r['disagree']]
    nmo = [r for r in rows if r['name_only']]
    print(f'\n  DISAGREE (name-class != predicate-class, both confident): {len(dis)}')
    print(f'  NAME-ONLY (predicate-view unclassified; name is only a hypothesis):  {len(nmo)}')

    print('\n=== AUDIT SAMPLE (deterministic by md5) ===')
    rk = sorted(rows, key=lambda r: hashlib.md5(
        (r['iface']+r['name']).encode()).hexdigest())
    for r in rk[:16]:
        print(f'[{r["cls"]:12s}] {r["iface"]}.{r["name"]}')
        print(f'{"":15s}{(r["summary"] or r["desc"])[:96]}')

    for bucket in ('AMBIGUOUS','UNCLASSIFIED'):
        print(f'\n=== ALL {bucket} ===')
        for r in rows:
            if r['cls'] == bucket:
                print(f'  {r["iface"]}.{r["name"]}')
                print(f'      {(r["summary"] or r["desc"])[:100]}')

    # The loud-failure buckets — the whole point of the rule-8 hardening.
    print('\n=== DISAGREE — name-class vs predicate-class (2026-08-02 retraction signal) ===')
    print('  Each row is a place a name-based classifier would have mis-filed silently.')
    for r in sorted(dis, key=lambda r: r['iface'] + r['name']):
        print(f'  {r["iface"]}.{r["name"]}:  name->{r["cls_name"]}  predicate->{r["cls"]}')
        print(f'      {(r["summary"] or r["desc"])[:100]}')
    print('\n=== NAME-ONLY — hypothesis, not measurement (predicate-view unclassified) ===')
    for r in sorted(nmo, key=lambda r: r['iface'] + r['name']):
        print(f'  {r["iface"]}.{r["name"]}:  name->{r["cls_name"]}')

    json.dump(rows, open(sys.argv[2], 'w'), indent=1)

if len(sys.argv) != 3:
    sys.exit('usage: wayland-classifier.py CORPUS.json OUT.json  (CORPUS.json from extract-corpus.py)')
main(sys.argv[1])
