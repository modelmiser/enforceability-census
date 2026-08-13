#!/usr/bin/env python3
"""
Predicate-shape classifier (four buckets: STATE/THRESHOLD/TYPESTATE/UNCLASSIFIED),
corpus 2: awesome-prometheus-alerts.

Usage: promql-classifier.py RULES.yml OUT.json
  RULES.yml = a single YAML file of alert rules (e.g. the merged rules file of
  a fresh awesome-prometheus-alerts clone); OUT.json = classified rows.

NOTE: the STATE bucket is the codebook's REVOCABLE class (equality/absence on
a discrete status); the code predates the unified naming.

Discriminator is the SHAPE OF THE PREDICATE, not the alert's wording:

  STATE      - equality/absence on a discrete status: a fact that was true and
               became false.  absent(), up == 0, changes(), resets(), ==/!= 0|1.
  THRESHOLD  - inequality against a numeric literal: a line somebody drew on a
               continuous quantity.  >, <, >=, <= vs a number.
  TYPESTATE  - an ordering/protocol obligation over one object's history.
               STRUCTURALLY 0: classify() has no TYPESTATE detector because
               PromQL cannot express the class (codebook rule 7); the printed
               0 is a design invariant, not a corpus measurement.
  UNCLASSIFIED - reported, never absorbed.  If this bucket is large the
               classifier is wrong and the result should not be trusted.

Precedence: STATE is tested before THRESHOLD, because `up == 0` is an equality
and must not be captured by a generic comparison rule.

Rule-9 hardening (2026-08-09, see codebook/classes.md): the query is the
measurement and `classify()` already ignores the alert name (rule 8, good). This
adds the missing half -- a hypothesis classifier over the NAME -- purely to raise
a **DISAGREE** signal where the two views of an alert diverge (e.g. `InstanceDown`
whose query is a continuous THRESHOLD, or `HighReplicationLag` whose query is a
STATE equality), plus a **NAME-HINT** signal that suggests a class for rows the
query classifier left UNCLASSIFIED. The name is never the reported class.
"""
import re, sys, json, hashlib
try:
    import yaml
except ImportError:
    sys.exit("This classifier needs PyYAML (pip install pyyaml) to read the rules file.")

STATE_PATTERNS = [
    r'\babsent\s*\(',              # the thing is gone entirely
    r'\babsent_over_time\s*\(',
    r'\bchanges\s*\(',             # it changed
    r'\bresets\s*\(',              # a counter went backwards = restart
    r'\bup\s*[=!]=\s*[01]\b',      # target up/down
    r'[=!]=\s*[01]\s*$',           # bare boolean equality at end of expr
    r'[=!]=\s*[01]\s*(unless|and|or|for)\b',
]
# metric names that denote a discrete status rather than a measure
STATE_METRIC = re.compile(
    r'_(state|status|health|healthy|ready|available|up|online|active|enabled|'
    r'connected|synced|leader|master|role|mode|present)\b', re.I)

# v2 fixes, both found by reading the UNCLASSIFIED bucket, both principled:
#
#  (1) decimal literals written without a leading zero (`> .80`) were missed
#      outright.  Pure bug.
#  (2) comparisons whose right-hand side is ANOTHER MEASURED QUANTITY
#      (`node_hwmon_temp_celsius > node_hwmon_temp_max_celsius`,
#      `pg_stat_activity_count >= pg_settings_max_connections`) are still
#      thresholds -- a line on a continuous scale.  That the line is read from
#      the system instead of hardcoded makes it a BETTER threshold, not a
#      different class.  Tracked separately as THRESHOLD-dynamic so the
#      decision stays visible rather than buried.
INEQ = re.compile(r'(>=|<=|>|<)\s*[-+]?\s*\(?\s*(?:[0-9]|\.[0-9])')
INEQ_ANY = re.compile(r'(>=|<=|>|<)(?!=)')

# equality/inequality on identity, revision or membership = supersession,
# i.e. a fact that was true for one generation and is false for the next.
SUPERSESSION = re.compile(
    r'_(generation|revision|version|replicas|members|epoch|term|ordinal|'
    r'config|settings)\b', re.I)

# continuous-measure markers: if present, an inequality is a real threshold
CONT = re.compile(
    r'\b(rate|irate|increase|delta|deriv|histogram_quantile|quantile|avg|'
    r'avg_over_time|sum|max|min|stddev|predict_linear|topk)\s*\(|'
    r'_(seconds|bytes|duration|latency|ratio|percent|usage|total|count|size|'
    r'bucket|sum)\b|/|\*\s*100', re.I)


# --- Name-side (hypothesis) classifier -------------------------------------
# Guesses the class from the alert NAME alone, by the words operators use. Used
# ONLY to raise the DISAGREE / NAME-HINT signals below, never as the reported
# class. STATE is tested before THRESHOLD, mirroring classify()'s precedence.
NAME_STATE = re.compile(
    r'\b(down|absent|missing|unavailable|unreachable|offline|not ready|'
    r'dead|gone|lost|failed|failure|restart(ed)?|flapp?ing|changed|'
    r'desync\w*|unsync\w*|out of sync|split brain|no ?data|'
    r'expired?|expiring|stale|inactive|unhealthy)\b', re.I)
NAME_THRESHOLD = re.compile(
    r'\b(high|low|too (many|much|large|big|few|small)|excess\w*|exceed\w*|'
    r'usage|full|pressure|latency|slow|saturat\w*|utiliz\w*|percent|ratio|'
    r'exhaust\w*|nearing|near (limit|full|capacity)|limit|overcommit\w*|'
    r'throttl\w*|backlog|lag|growth|spike|large|count|size)\b', re.I)


def _name_words(name):
    # Split CamelCase (InstanceDown -> Instance Down) and snake_case, then
    # lowercase, so `\b`-anchored keywords match names in any convention.
    s = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', name or '')
    return s.replace('_', ' ').lower()


def classify_name(name):
    nm = _name_words(name)
    if NAME_STATE.search(nm):
        return 'STATE'
    if NAME_THRESHOLD.search(nm):
        return 'THRESHOLD'
    return 'UNCLASSIFIED'


def classify(name, query):
    q = ' '.join(query.split())
    for p in STATE_PATTERNS:
        if re.search(p, q, re.I):
            return 'STATE', p
    if re.search(r'[=!]=', q) and STATE_METRIC.search(q):
        return 'STATE', 'equality-on-status-metric'
    if re.search(r'[=!]=', q) and SUPERSESSION.search(q):
        return 'STATE', 'supersession-generation-mismatch'
    if re.search(r'\bunless\b', q):
        return 'STATE', 'set-difference-absence'
    if INEQ.search(q):
        if CONT.search(q):
            return 'THRESHOLD', 'inequality-vs-literal-on-continuous'
        return 'THRESHOLD', 'inequality-vs-literal-bare'
    if INEQ_ANY.search(q):
        return 'THRESHOLD', 'inequality-vs-measured-quantity(dynamic)'
    return 'UNCLASSIFIED', ''


def main(path):
    doc = yaml.safe_load(open(path))
    rows = []
    for g in doc['groups']:
        for svc in (g.get('services') or []):
            for exp in (svc.get('exporters') or []):
                for r in (exp.get('rules') or []):
                    q = r.get('query')
                    if not q:
                        continue
                    cls, why = classify(r.get('name', ''), q)
                    name_cls = classify_name(r.get('name', ''))
                    rows.append({
                        'group': g.get('name'), 'service': svc.get('name'),
                        'name': r.get('name'), 'query': ' '.join(q.split()),
                        'cls': cls, 'why': why, 'cls_name': name_cls,
                        # DISAGREE: query and name both confident but differ.
                        'disagree': (cls != 'UNCLASSIFIED'
                                     and name_cls != 'UNCLASSIFIED'
                                     and cls != name_cls),
                        # NAME-HINT: query couldn't classify; the name suggests one
                        # -- triage for the untrusted UNCLASSIFIED bucket.
                        'name_hint': (cls == 'UNCLASSIFIED'
                                      and name_cls != 'UNCLASSIFIED'),
                    })

    counts = {}
    for r in rows:
        counts[r['cls']] = counts.get(r['cls'], 0) + 1
    total = len(rows)
    print(f'TOTAL RULES: {total}')
    for k in ('THRESHOLD', 'STATE', 'TYPESTATE', 'UNCLASSIFIED'):
        n = counts.get(k, 0)
        print(f'  {k:14s} {n:4d}  {100.0*n/total:5.1f}%')

    ts = counts.get('THRESHOLD', 0) + counts.get('STATE', 0)
    if ts:
        print(f'\nAmong THRESHOLD+STATE only (the comparable slice, n={ts}):')
        print(f'  THRESHOLD    {100.0*counts.get("THRESHOLD",0)/ts:5.1f}%')
        print(f'  STATE        {100.0*counts.get("STATE",0)/ts:5.1f}%')

    json.dump(rows, open(sys.argv[2], 'w'), indent=1)

    # deterministic pseudo-random audit sample: hash the name, take lowest N
    print('\n=== AUDIT SAMPLE (deterministic by md5, for hand-checking) ===')
    ranked = sorted(rows, key=lambda r: hashlib.md5(r['name'].encode()).hexdigest())
    for r in ranked[:14]:
        print(f'[{r["cls"]:12s}] {r["name"][:52]:52s} | {r["query"][:78]}')

    print('\n=== ALL UNCLASSIFIED ===')
    for r in rows:
        if r['cls'] == 'UNCLASSIFIED':
            print(f'  {r["name"][:52]:52s} | {r["query"][:88]}')

    # Rule-9 loud-failure buckets: name-view vs query-view of the same alert.
    dis = [r for r in rows if r['disagree']]
    hints = [r for r in rows if r['name_hint']]
    print(f'\n  DISAGREE (name-class != query-class, both confident): {len(dis)}')
    print(f'  NAME-HINT (query unclassified; name suggests a class): {len(hints)}')

    print('\n=== DISAGREE — alert name vs query predicate (rule 9) ===')
    print('  Each row: the name implies one class, the query computes another. Look.')
    for r in sorted(dis, key=lambda r: (r['name'] or '')):
        print(f'  {(r["name"] or "")[:46]:46s} name->{r["cls_name"]:9s} query->{r["cls"]}')
        print(f'      {r["query"][:92]}')

    print('\n=== NAME-HINT — triage for the untrusted UNCLASSIFIED bucket ===')
    for r in sorted(hints, key=lambda r: (r['name'] or '')):
        print(f'  {(r["name"] or "")[:46]:46s} name->{r["cls_name"]}')
        print(f'      {r["query"][:92]}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('usage: promql-classifier.py RULES.yml OUT.json')
    main(sys.argv[1])
