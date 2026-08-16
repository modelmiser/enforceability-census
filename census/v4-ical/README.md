# v4-on-iCalendar pass — pre-pass protocol (no rater has run)

2026-08-15 · **Status: registered BEFORE any rater; predictions W1–W5
fixed at this commit.** Append-only after push; corrections, if ever
needed, are appended in dated brackets.

## Why this pass

The iCalendar census (`census/ical/`, v3 instrument) left one confound
named in its own report: the spec-fixed-constant edge behind ten of
QUIC's fifteen-item THRESHOLD rater symmetric difference did not fire
at all on the format genre — but
that census used different rater models than the QUIC one, so genre and
rater-model era could not be separated. Re-rating the SAME corpus with
the SAME rater models under **instrument v4** isolates the v3→v4
instrument delta on this genre (it does NOT resolve the genre-vs-model
question about QUIC's wobble — that would need QUIC re-rated with this
roster). It measures, outside protocol territory, two v4 behaviors the
protocol passes recorded: repair rules generalizing past their
named items (rules 16/17), and rule 18's lifecycle vocabulary
*appearing* to pull PROCESS readings beyond key contexts (v4's
measured cost on QUIC, hedged there and hedged here). A
format corpus with **zero THRESHOLD, zero REVOCABLE, and no key
material under v3** is close to a null instrument for rules 16, 19,
and 18 respectively (rule 17's complement-state test is nulled by none
of these and simply has few negotiated-state guards to bite) —
which makes it a cheap, sharp test: v4 should change almost nothing
here, and every departure is signal. This pass also feeds the v5
docket with cross-genre evidence.

## Instrument, corpus, raters

- Instrument: `codebook/rater-pack-v4.md`, git blob `4891605…` (the v3
  pack verbatim + rules 15–19 with the one disclosed elision — see the
  `census/v4-tls/` protocol AND its appended correction: the retained
  rule-16/19 seam example settles TLS items 188/189; no analogous
  content exists for this corpus, see the sweep below), served blind,
  hash-round-trip verified at serve time.
- Corpus: `census/ical/rfc5545_s3_musts.txt`, byte-identical, n = 225
  (sha256 `f45306fba7a0df3c…`).
- **Settlement sweep, run at registration:** every corpus item checked
  for any 4-word n-gram (case/punctuation-normalized) occurring
  anywhere in the v4 pack blob — **zero hits**. The v4 rules quote
  TLS/MLS/QUIC/RFC 9001 content only; no iCal item is
  worked-example-settled at phrase-overlap strength (paraphrase-level
  steering remains the sweep's blind spot, as always). A manual
  paraphrase-level comparison was therefore also run at registration:
  the corpus's DURATION/TRIGGER items are all presence, co-occurrence,
  or value-type duties — no inequality on a duration field — and the
  corpus contains zero cache/retain/elapsed-time/expiry duties, so the
  rule-16/19 seam example (ticket_lifetime; cache-no-longer-than) has
  no analogue here; the one spec-fixed inequality v3 read outside
  DOMAIN (item 203's 255-octet
  floor) is engaged by rule 16's general litmus, which is the measured
  object, not a settlement.
- Raters, models pre-registered, the iCal census's roster repeated:
  **rater Av4i** — fresh same-family instance, model `claude-fable-5`
  (the name governs; a differing serving-session model is a protocol
  event), single input file (pack + corpus), blind to predictions and
  tallies; **rater Xv4i** — foreign `cursor-grok-4.6-high-fast` via
  cursor-cli, chunk partition pinned exactly to the v3 pass's:
  1–51 / 52–102 / 103–153 / 154–204 / 205–225 (so W5's cross-context
  geometry — which duplicate groups straddle chunk boundaries — matches
  the v3 comparison). No author rater.
- Malformed-label handling and its N-interactions: inherited verbatim
  from `census/ical/README.md` (one format-only retry; residual
  malformed/missing labels scored U as protocol events; event-U counts
  as disagreement for agreement figures, non-eliminable in shares, and
  is excluded from determinism split judgments while reported beside
  them). A trailing `?` flag on a label is stripped; the base label
  governs for every W figure and every owed list.

## Ring-fence

The iCalendar census headline (88.0%/88.4%, v3 instrument) stands and
is never substituted. A v4-on-iCal share belongs to the v4 series and
is quoted only next to its instrument version. Failed predictions grade
the author's model (W5 grades the instrument's determinism) — and a
failed W1 or W2 is additionally reported as an instrument-delta
observation regardless, so the grading frame cannot soften a measured
v4 cost. No re-rating, no rewording, no exclusion of any
valid-instrument rater, no quote discretion; deviations, if any, are
recorded with reasons, never argued into compliance.

## Pre-registered predictions W1–W5 (the author's null model: v4 changes almost nothing here)

Direction-of-effect disclosure: the null model is instrument-friendly —
"the repair does no harm outside its territory" is the flattering
outcome for v4. Hence itemized, mechanically gradeable clauses, graded
per rater (bounds inclusive throughout).

- **W1.** THRESHOLD count = 0 in both v4 raters (rule 16 has little to
  move: no spec-fixed bound drew THRESHOLD under v3 — the one
  non-DOMAIN case, item 203's 255-octet floor, went PROCESS/POLICY).
- **W2.** REVOCABLE count ≤ 1 per rater (rule 19 finds at most one
  elapsed-time reading in a span that states no deadline duties under
  v3).
- **W3.** Per-item eliminable share in **[86%, 90%]** for both raters —
  a ±2-point envelope around the same-family v3 share of 88.0% (the
  foreign v3 share, 88.4%, gets 1.6 points of upper headroom);
  effective band in achievable counts: 194–202 of 225, endpoints
  unreachable exactly so no boundary tie can arise.
- **W4.** Per-rater match rate against the archived v3 iCal pair
  (a match = the v4 label equals rater Ai's or rater Xi's archived v3
  label on that item, full corpus, n = 225; a protocol-event U is a
  NON-match regardless of the archived label) **≥ 97.3%** — at least
  219 of 225 items (the v3 pair's own raw agreement, the V7(a)
  convention with its floor set by the archived pair).
- **W5.** Determinism: zero intra-group splits across the 14
  verbatim-duplicate-text groups per rater, judged on well-formed
  labels per the event rule (the iCal census's N4). Zero is
  deliberately STRICTER than the foreign rater's v3 baseline of one
  split; the count governs, and one Xv4i split fails W5 even though it
  would match v3.

The PROCESS-churn question (rule 18's vocabulary cost, QUIC's finding)
is deliberately NOT a numbered prediction: the author has no itemized
model of it here, and a count-bound aggregate clause is exactly the V7
mistake. The report instead OWES the following observation lists, with
no pass/fail attached and counts stated explicitly even when zero,
PER v4 rater: (a) every item that rater labels PROCESS against a
non-PROCESS label in both archived v3 raters; (b) every item that
rater labels non-PROCESS against PROCESS in both archived v3 raters;
(c) separately, the two archived PROCESS-boundary split items (141:
PROCESS/U and 203: PROCESS/POLICY), listed with both v4 raters'
labels UNCONDITIONALLY. Protocol-event U items are reported beside these lists, never
inside them. A report omitting any list, or omitting an explicit
"none", is out of compliance with this registration.

## What this pass can and cannot say

Same corpus, same rater models, new instrument version: departures from
the v3 labels measure the instrument delta (plus rater stochasticity —
two fresh instances of the same models, the residual noise floor this
design cannot remove). It cannot revisit the v3 headline, and the
corpus-shared-prior caveat applies to any agreement it reports.
