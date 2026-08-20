# MECH-PROBE-1 — feasibility plan, committed BEFORE seeing any MLS label

Date: 2026-08-20. Purpose: FEASIBILITY ONLY. The number produced here can never
be quoted as a result, and MLS is spent as a probe corpus either way.

## Question
Can a rule-based, non-LLM classifier — written from `codebook/classes.md` alone —
recover the census's predicate-shape classification on RFC prose above the
degenerate baselines?

## Protocol, committed now
1. Read codebook class definitions + decision rules. Write classifier. NO MLS
   labels are loaded or displayed before the classifier file is frozen (md5 recorded).
2. Run classifier over the MLS corpus text -> predictions.
3. ONLY THEN load archived MLS labels.
4. Report agreement vs EACH archived rater separately (A-prime and B-prime, or
   whatever the archive holds), never a cherry-picked best.
5. Report degenerate baselines on the SAME items: constant-most-common-class,
   and a seeded label shuffle. The classifier must beat both to be interesting.
6. ONE RUN. If I adjust a rule after seeing agreement, this probe is VOID and is
   reported as void. No tuning loop.

## Pre-committed reading
- Beats both degenerates by a clear margin -> feasibility established; the arc is
  live; register against a PROTECTED corpus (TLS/iCal/QUIC) and run once there.
- At or near degenerate -> predicate shape is not mechanically recoverable from
  prose at this effort level. Arc closes cheaply. This is a real outcome, not a
  failure to be retried with better regexes.
- Anything in between -> reported as inconclusive; no arc opened on a hunch.

## What this CANNOT show
Nothing about author mediation (I write the rules; the author-mediation half of
the confound is inherited whole). It probes only the shared-prior half.
