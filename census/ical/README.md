# Non-protocol corpus census — RFC 5545 (iCalendar) §3, pre-registration

2026-08-15 · **Status: corpus FROZEN, predictions N1–N6 REGISTERED, NO
rater has run.** This file is committed and pushed before any rater
exists; per this repository's discipline it is append-only — corrections,
if ever needed, are appended in dated brackets, never edited in place.

## Why this corpus — the selection procedure, disclosed

Every censused span so far is protocol or monitoring prose. The spectrum
reading (paper §9) says a span's type-eliminable share tracks *what that
span states as obligations* — a claim never yet tested outside the
protocol genre. The selection criteria, fixed before counting: (1)
**non-protocol** — the normative surface constrains a data artifact's
form, not a multi-party exchange; (2) standards-track RFC with RFC 2119
boilerplate, so the frozen extraction recipe transfers; (3) the largest
normative surface among qualifying candidates. Candidates counted
(MUST|SHALL-bearing lines, whole document):

| RFC | subject | lines |
|---|---|---|
| 3986 | URI syntax | **0** |
| 8259 | JSON | 8 |
| 7946 | GeoJSON | 25 |
| 8949 | CBOR | 27 |
| 9562 | UUID | 27 |
| 5322 | Internet Message Format | 36 |
| 8610 | CDDL | 2 |
| 5545 | iCalendar | **246** |
| (draft-bhutton-json-schema-01) | JSON Schema core | 112 — excluded: not an RFC |

Two selection-time observations, recorded before any rater: **data-format
RFCs are normatively thin** — they state their obligations as grammar
(ABNF), which a MUST-sentence census cannot see (rule-7 censoring by
*genre*; RFC 3986 has literally zero MUST/SHALL lines) — and RFC 5545 is
the outlier because it writes its obligations *into* its grammar, as ABNF
comments. That idiom forces the second of the three disclosed recipe refinements (below).

RFC 5545 defines a data format. The scheduling *protocol* built on it
(iTIP, RFC 5546) is a separate document: protocol duties are censored out
of this corpus by the document boundary, exactly as QUIC's crypto was —
stated here in advance (rule 7).

## Corpus freeze

- Source: `https://www.rfc-editor.org/rfc/rfc5545.txt`, sha256
  `c256f809479d98aa…`. RFC 5545 (2009) is a pre-v3 **paginated** RFC; the
  frozen recipe was written for unpaginated v3-format text.
- **Refinement 1 — depagination** (`depaginate.py`, shipped): each fixed
  page-furniture block (blanks + footer + form-feed + header + blanks) is
  replaced by a join (nothing) iff the following content starts lowercase
  or the preceding line lacks sentence-terminal punctuation, else by one
  blank line. Deterministic; 95 joins / 73 paragraph breaks on this
  document; all six joins adjacent to MUST/SHALL text were audited by eye
  at freeze time (five are mid-sentence or mid-comment-run continuations;
  the sixth abuts a comment line against following prose and is inert
  because refinement 2 keeps those streams separate). Output sha256
  `b19b0ffc973253bc…`.
- **Refinement 2 — ABNF comment stream** (`extract-corpus.py`, shipped;
  otherwise the frozen recipe verbatim): lines whose stripped form starts
  with `;` are stripped of the prefix and joined as their own paragraphs
  in place, never merging with prose; a bare `;` line breaks a comment
  paragraph as a blank line breaks prose. Reason, measured before the
  recipe was fixed: RFC 5545 states its per-property cardinality
  obligations ("…MUST NOT occur more than once") inside ABNF comments,
  mostly with no prose counterpart — excluding comments censors that
  family; including them raw glues fold-broken `;` fragments onto prose.
  Non-comment ABNF definition lines join paragraphs as ordinary lines;
  they carry no MUST/SHALL tokens in this span (verified at freeze).
- **Refinement 3 — example-data exclusion** (same script; found by the
  pre-push gate reviewer, fixed before anything was frozen): a prose
  paragraph whose first line has iCalendar *content-line* shape — an
  unquoted `NAME:`/`NAME;` at paragraph start — is literal example data,
  not prose, and is dropped (183 such paragraphs in the span). Normative
  prose always quotes property names ("DTSTART"); example values are
  free text that can contain the word MUST: exactly one such paragraph
  did ("Phoenix design team MUST attend this meeting" — fictional
  meeting-notice text inside a sample DESCRIPTION value, which the
  two-refinement recipe had emitted as a classifiable item). A
  data-format genre hazard with no analogue in the protocol corpora,
  recorded here as a finding in its own right.
- Span: §3 (iCalendar Object Specification) = depaginated lines 366–6606,
  holding 238 of the document's 255 MUST|SHALL occurrences (93.3% —
  QUIC-grade span coverage).
- Corpus: [`rfc5545_s3_musts.txt`](rfc5545_s3_musts.txt), **n = 225**,
  sha256 `f45306fba7a0df3c…`. Token conservation exact and fully
  accounted: 237 MUST|SHALL occurrences in the corpus + 1 in the single
  excluded example paragraph = 238 in the span.
- Regenerate:
  `python3 depaginate.py rfc5545.txt depag.txt && python3 extract-corpus.py depag.txt 366 6606 out.txt`

**Duplicate-text disclosure (before any rater):** the ABNF-comment
cardinality idiom yields 14 texts that each appear more than once — 48
surplus items; 177 unique texts. Largest: "The following are OPTIONAL,
but MUST NOT occur more than once." × 20 (items 88, 94, 99, 103, 105,
147, 148, 151, 152, 153, 159, 163, 168, 186, 187, 191, 195, 205, 207,
219). Identical text, different referent (one per component/property
list) — the sentence-granularity limit (paper limitation 4) in inverse
form. Both arithmetics are pre-registered to remove post-hoc choice: the
**headline is the per-item share (n = 225)**, recipe-consistent with
every prior census; the unique-text share (n = 177) is quoted beside it
as a secondary figure, counting each duplicate-text group once by its
unanimous label — if a rater splits within a group (an N4 failure), that
rater's unique-text share is quoted as the range obtained by counting
each split group as eliminable and as not; a group with no well-formed
labels at all counts as non-eliminable, per the protocol-event rule
below. Duplicate weight concentrates on the cardinality
template and is the subject of prediction N4.

## Instrument, raters, and the settlement sweep

- Instrument: the **frozen v3 pass-4 rater pack**. The served bytes are
  pinned to git blob `a08febba22fd2cb117a9be41654a6209e0104e57`
  (extracted via `git cat-file blob`, hash-round-trip verified at serve
  time) — NOT the working-tree `codebook/rater-pack.md`, which is a
  later reformatting-for-rendering of the same rule content (disclosed
  in the paper's appendix). This census extends the matched-method v3
  series (the paper's spectrum set) — *instrument*-matched, but
  **rater-model-unmatched**: the prior same-family raters ran on
  earlier-session models, which is a confound on any cross-census
  agreement comparison; the rater models below are pre-registered
  precisely so that confound is named, not hidden. A v4 replication of
  this corpus would be a separate, version-labeled arc.
- **Settlement sweep, run at freeze time (the census/v4-tls lesson,
  appended correction there):** every corpus item was checked for any
  6-word n-gram occurring anywhere in the pack — zero hits, so no item
  is settled at that phrase-overlap strength (the sweep cannot see
  paraphrase-level steering; the pack's worked examples are all
  TLS-protocol content, so none is expected). The pre-push gate
  reviewer's independent re-implementation extended this to 4-grams,
  case/punctuation-normalized, against BOTH pack byte-streams (blob and
  reformatted): zero hits.
- Raters, models pre-registered (per the model-seating agreement of
  2026-08-14, whose versioned trace is this repo's TODO; its operative
  sentence for a census: every rating series pre-registers its rater
  models, and the pre-registered NAME governs — if the serving session's
  inherited model differs at serve time, that is a protocol event, not a
  compliance argument): **rater Ai** — a fresh same-family instance,
  model `claude-fable-5`, single input file holding pack + corpus, blind
  to this file's predictions and to all tallies; **rater Xi** —
  foreign-family `cursor-grok-4.6-high-fast` via cursor-cli, chunked
  ≤ 51 items, the replication transport. **No author rater** — the
  author wrote the predictions below.
- **Malformed-label handling, inherited verbatim from the cross-family
  replication design (`census/foreign/`):** one format-only retry per
  chunk; residual malformed or missing labels are scored U and recorded
  as protocol events. The same rule applies to Ai's single completion.
  Interaction with the predictions, fixed now: a protocol-event U counts
  as a disagreement for N6 and as non-eliminable in N2's unchanged
  n = 225 denominator (both conservative); N4 grades a duplicate-text
  group as split only on differing *well-formed* labels — event items
  are excluded from the split judgment and the event is reported beside
  the grade, so transport noise cannot masquerade as instrument
  nondeterminism (nor hide).

## Pre-registered predictions N1–N6 (the author's model of the format genre)

Direction-of-effect disclosure first: N2's model is thesis-friendly — a
format-discipline corpus landing high would extend the spectrum in the
direction the thesis likes. That is exactly when this repository's
error-sign lesson applies; hence itemized predictions, a no-author-rater
pass, and the failure clause below.

- **N1.** DOMAIN is the strictly largest class for both raters (its
  count exceeds every other class's; a tie fails) — as in MLS (the one
  DOMAIN-led protocol span), and unlike TLS, QUIC, and RFC 9001
  (TYPESTATE-led) or RFC 9002 (PROCESS-led).
- **N2.** Per-item eliminable share (n = 225) lands in **[72%, 88%]**,
  bounds inclusive, for both raters — at this n the endpoints are the
  achievable counts 162 and 198, and both count as inside.
- **N3.** CV = 0 and NEG = 0, exactly, in both raters (a data format has
  no secret-material checks and no two-party intersection duties; any
  nonzero count fails this).
- **N4.** Within each rater, every duplicate-text group is single-label
  (zero intra-group splits across all 14 groups, judged on well-formed
  labels per the event rule above). This is a determinism probe of the
  instrument: identical input text should draw identical labels. The
  probe is harder for Xi than for Ai, stated in advance: the 20-item
  group spans Xi's chunk boundaries (fresh process per chunk), so Xi is
  probed for cross-context determinism, Ai for within-context.
- **N5.** REVOCABLE ≤ 2 per rater (the span states format, not clocks;
  UTC-form duties are format duties).
- **N6.** Raw pair agreement ≥ 85%, i.e., at least 192 of 225 items
  identically labeled (format prose is crisp; the v3 protocol pairs ran
  76.8–96.7% — a rater-model-unmatched comparison, per above).

**Failure interpretation, pre-committed:** a failed N1, N2, N3, N5, or
N6 grades the author's model of the format genre; a failed N4 grades the
instrument's determinism and is reported as an instrument finding —
either way a failure licenses no re-rating, no
exclusion, no rewording, and no quote discretion. The headline is the
two-rater per-item range as measured, whatever it is. Deviations, if
any, are recorded with reasons, never argued into compliance.

## What this census can and cannot say

It tests whether the spectrum reading survives its first non-protocol
point, under the same frozen instrument as the five protocol spans. It
cannot see obligations RFC 5545 states as pure grammar with no
MUST-comment (rule-7 censoring measured above at genre level), and its
document boundary censors the scheduling protocol. n = 225 is a sentence
count, with the duplicate-text weight disclosed above.
