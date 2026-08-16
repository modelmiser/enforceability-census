# QUIC cross-roster replication — pre-pass protocol (no rater has run)

2026-08-15 · **Status: registered BEFORE any rater; predictions Y1–Y6
fixed at this commit.** Append-only after push; corrections, if ever
needed, are appended in dated brackets.

## Why this pass — the missing cell

Three public documents in this repository (the iCalendar census, the
v4-ical protocol, and the root README's open work) name the same open
question: QUIC's THRESHOLD wobble — a fifteen-item between-rater
symmetric difference under v3, ten of them on spec-fixed constants —
was measured with one rater roster, and the format genre's total
absence of that wobble was measured with a different one, so *genre
versus rater-model era* could not be separated. This pass fills the
missing cell of the instrument × roster grid on the same frozen QUIC
corpus:

| | old pair (author + fresh same-family, 2026-08-13 models) | iCal-shape roster (`claude-fable-5` + `cursor-grok-4.6-high-fast`, no author; the v4 cell's same-family model name was not recorded — see closing section) |
|---|---|---|
| v3 instrument | raw agreement 85.1% (the census) | **this pass** |
| v4 instrument | — (unmeasurable; the old sessions are gone) | raw agreement 84.0% (`census/v4-completion/`) |

If the wobble is genre-driven (QUIC's derived-constant content meeting
decision rule 3's ambiguity), it reproduces here; if it is
roster-driven (the bundle named in the closing section), it shrinks
toward the format genre's zero. Either
answer is v5 evidence about whether rule 16 repairs an instrument
defect or an old-roster artifact.

## Instrument, corpus, raters

- Instrument: the frozen v3 pass-4 pack, git blob
  `a08febba22fd2cb117a9be41654a6209e0104e57`, extracted via
  `git cat-file blob`, hash-round-trip verified at serve time — the
  SAME bytes the 2026-08-13 QUIC census served, so instrument is held
  exactly fixed across the roster comparison.
- Corpus: `census/quic/rfc9000_s2-19_musts.txt`, byte-identical,
  n = 281.
- **Settlement sweep, run at registration:** every corpus item checked
  for shared n-grams with the pack (case/punctuation-normalized).
  6-gram and 5-gram: **zero hits**. 4-gram: exactly one hit, item 233
  sharing the generic modal phrase "MUST NOT be sent" — adjudicated
  non-settling (a phrase-frequency artifact; the pack uses it in a
  rule statement that names no QUIC content). Any settlement effect
  would in any case cancel in this design: both rosters receive the
  identical bytes.
- Raters, models pre-registered (the names govern; a differing serving
  model is a protocol event): **rater Aq** — fresh same-family
  instance, `claude-fable-5`, single input file (pack + corpus), blind
  to predictions and tallies; **rater Xq** — foreign
  `cursor-grok-4.6-high-fast` via cursor-cli, chunk partition pinned:
  1–51 / 52–102 / 103–153 / 154–204 / 205–255 / 256–281. No author
  rater.
- Malformed-label handling inherited from `census/ical/` (one
  format-only retry; residual malformed/missing scored U as protocol
  events; event-U counts as disagreement in agreement figures and
  non-eliminable in shares) and, for torn-flags, from `census/v4-ical/`
  (a trailing `?` is stripped, the base label governing every figure
  and list — applied to archived and new labels alike).

## Ring-fence

The QUIC census headline (≈67–69%, v3 instrument, old roster) stands
and is never substituted; so do the v4-completion numbers. This pass's
share is quoted only as "v3 instrument, iCal-roster replication."
Failed predictions grade the author's model; failures of Y1/Y2/Y3 are
additionally reported as roster-effect observations regardless, so the
grading frame cannot bury the answer either way. No re-rating, no
rewording, no exclusion of any valid-instrument rater, no quote
discretion; deviations recorded with reasons, never argued into
compliance.

## Pre-registered predictions Y1–Y6 (the author's model: the wobble is real but era-shrunk)

Direction-of-effect disclosure: the author's model predicts a
middle outcome — boundary still soft (vindicating rule 16's existence)
but softer than 2026-08-13 (crediting model era). Both halves flatter
something the author built (the v4 amendment; the new-roster
censuses), so both directions of failure are live. Bounds inclusive
throughout; per-rater grading where a clause names both raters (Y5,
Y6); Y1, Y2, Y3, and Y4 are pair-level clauses.

- **Y1.** The new-pair THRESHOLD symmetric difference is ≥ 4 (the
  rule-3 boundary remains soft under v3 with this roster; unanimity or
  near-unanimity on THRESHOLD fails this and locates the wobble in the
  old roster's era).
- **Y2.** Of the ten archived spec-fixed symdiff items {41, 63, 191,
  197, 198, 199, 200, 238, 239, 266}: at least 6 draw a non-THRESHOLD
  label from at least one of Aq/Xq (the newer models' DOMAIN-lean on
  datum bounds, seen on iCal, reaches QUIC's constants).
- For Y1, Y2, and Y3, protocol-event U items are EXCLUDED from the
  symdiff and label judgments and reported beside them (the N4
  convention — transport noise must not manufacture a pass in any of
  the three, whose noise direction is pass-ward).
- **Y3.** The deadline edge persists: across the six rater-item
  readings of items {69, 163, 164}, at least two distinct classes
  appear (six identical labels — full cross-item, cross-rater
  unanimity — fails this and would mark the v3 deadline edge as
  era-bound).
- **Y4.** Raw pair agreement in [82%, 88%] — counts 231–247 of 281 —
  bracketing both measured QUIC cells (85.1%, 84.0%).
- **Y5.** Per-item eliminable share in [64%, 71%] for both raters —
  counts 180–199 of 281 (the v3-old shares were 66.9%/69.0%).
- **Y6.** Per-rater match rate against the archived v3-old pair (match
  = equals rater A″'s or rater B″'s archived label, torn-flags
  stripped; an event-U is a non-match regardless) ≥ 239/281 — the
  archived pair's own exact raw-agreement count (239/281 = 85.1% as
  the census rounds it; the V7(a) convention).

**Owed both-metric reporting (the v4-ical lesson, registered here so
the report cannot choose the friendlier number):** the report quotes,
per rater, BOTH the match rate against the archived pair (Y6's metric)
AND the per-item agreement with its role-matched archived rater (Aq
vs A″, Xq vs B″ — noting both archived raters are same-family Claude,
so Xq has no own-family counterpart) — plus, for the fifteen archived THRESHOLD-symdiff items
and the three deadline items, a full per-item label table across all
four raters (A″, B″, Aq, Xq), with per-class counts per rater over
the 16 tabled items (the fifteen symdiff items ∪ the deadline trio),
stated explicitly including zero. A report omitting either metric,
the table, or an explicit "none" is out of compliance with this
registration.

## What this pass can and cannot say

It separates INSTRUMENT from ROSTER on this corpus (the v4-completion
cell shares this pass's foreign rater by pre-registered name and its
roster shape — fresh same-family + same foreign model, no author —
but the v4-completion same-family model name was never recorded, so
model-exact identity is an assumption: the v4-vs-this comparison is
near-clean on instrument, plus fresh-instance stochasticity), and completes three cells of the grid (the
fourth is unmeasurable). Stated plainly: "roster" here is a BUNDLE —
against the 2026-08-13 pair this pass changes model era, pair
composition (that pair was two same-family raters), AND
author-presence (that pair contained the census author; this one has
none — the paper's limitation-5/6 confounds), and nothing in this
design unbundles those three. It cannot revisit any prior headline,
and the corpus-shared-prior caveat applies to every agreement figure
in it.
