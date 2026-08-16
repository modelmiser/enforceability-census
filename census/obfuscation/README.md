# Obfuscation probe — registration (PUSHED BEFORE ANY RATER EXISTS)

**What this is, and is not.** A probe of the corpus-memorization
component of limitation 6's shared-prior confound — NOT a census, NOT
an instrument version, NOT a new corpus series. The question: does
item-level classification survive when the corpus's memorizable
identity is mechanically removed, leaving predicate shape? If labels
under obfuscation reproduce the v6 consensus, the classification
demonstrably rests on sentence shape rather than on remembered
readings of RFC 5545 specifically. **No number from this probe ever
joins, replaces, or requalifies any iCalendar series figure**; the
probe grades the confound, nothing else. Two honest limits, stated
first: (1) the probe is asymmetric — a PASS narrows the memorization
worry, but a FAIL is ambiguous between memorization and plain
nonce-comprehension cost, and the floors below carry disclosed
allowances for that; (2) genre-level priors (how spec-language in
general reads) survive any lexical obfuscation — only the parked
human-rater replication reaches the confound whole.

## The derived corpus

`rfc5545_s3_musts_obf.txt` (n = 225, item numbering unchanged),
produced by the shipped `obfuscate.py` from the frozen corpus
`census/ical/rfc5545_s3_musts.txt`: a deterministic, seeded
(`enforceability-census-obfuscation-v1`), REVERSIBLE substitution —
90 tokens + 2 morphology-preserving stems, the full bijection shipped
as `obf_map.json`. Build guards, each of which fired at least once
during construction and was watched to fail: byte-identical
round-trip (de-obfuscation must reproduce the frozen corpus exactly),
and a residual-leak scan over all replaced tokens including plural,
capitalized, and line-wrap-split variants (FOUR real leak classes
were caught pre-registration: plural domain nouns; lowercase quoted
ABNF rule names; a branch-order bug that left quoted aliases
unreplaced; and — found by this registration's own cold gate, after
the first three — the corpus's line-wrap artifact `iana- token` in
item 37, which the stem rule and the scan both missed until both
were widened to the space-split shape). Nonces are additionally
screened against an English wordlist so no substitute injects
meaning (the first generation produced `fine(s)` for alarms and a
duration-evoking token; the screen regenerated the whole map).

Replacement tiers (registered, not improvised):

- **REPLACED**: the format name (iCalendar); every RFC-5545-specific
  property/component/parameter/constant identifier (DTSTART, VEVENT,
  RRULE, the BY* rules, the fallback constants PRIVATE/UNKNOWN/BUSY/
  NEEDS-ACTION/PARENT/REQ-PARTICIPANT, …); their lowercase quoted
  ABNF aliases (same nonce, lowercased); the x-/iana- stems
  (morphology preserved: `x-` → `q-`, `iana-` → `zeta-`, so the
  two-families-of-extension-tokens structure survives without the
  memorized names); and the scheduling-domain nouns (calendar,
  calendaring, event, to-do, journal, alarm, attendee, scheduling),
  case- and plural-preserving.
- **RETAINED (disclosed)**: normative keywords; ABNF/punctuation
  names (COMMA, DQUOTE, BACKSLASH, …); encoding/charset universals
  (BASE64, BINARY, TEXT, URI, MIME, UTF-8); temporal universals
  (DATE, TIME, DATE-TIME, UTC, duration-as-English, time zone,
  recurrence, floating, leap); structural nouns (object, property,
  parameter, component, value, type); numbers, section references,
  and sibling-RFC citations (RFC 2045/2368/3986). Additional
  identifying residuals found by this registration's gate and
  retained knowingly: the quoted "VALUE" parameter and the literal
  `;VALUE=BINARY` syntax (items 20, 38); uppercase "IANA-registered"
  (item 21 — IANA is a cross-format registry universal; the stem
  rule is lowercase-only by design); "busy time"; "rule part(s)"
  (×27, RFC 5545 §3.3.10's distinctive term); "observance"/"onset";
  "chair"; the content-line fold/unfold vocabulary (items 1–2); and
  the backslash-escape construction (item 71). Every retention is a
  disclosed residual through which genre- or domain-level priors
  may still operate — the O1 arms measure their combined effect.

**Settlement sweep (rule 24's procedure, run at registration):** the
FULL served pack shares NO normalized ≥4-gram with any item of the
obfuscated corpus — zero hits across all 225 items. (For scale: the
pack already had zero hits on the ORIGINAL iCal corpus too; the
sweep's one all-corpora hit, TLS 14, is a TLS item — obfuscation is
not credited with removing overlap this corpus never had.) Sweep
self-tested with a planted 4-gram.

## The instrument, served

The FROZEN v6 pack, `codebook/rater-pack-v6.md`, blob
`f4f9e0b1c478cc05370e8b4ba7f612320698d8f0`, byte-identical — rule 14
verbatim; this probe cuts no pack. Two disclosed transport notes:
(1) the preamble (transport, not instrument) is anonymized — it says
"a data-format specification," not "RFC 5545 (iCalendar)"; (2) the
pack's rule 22 designates units for four named corpora including
"iCalendar at the transmitted calendar object" — served verbatim as
rule 14 requires. DISCLOSED PLAINLY: of the four designations only
one is a data format, and the corpus retains temporal vocabulary
(time zone, recurrence, DATE-TIME), so a graded rater holding
pack + corpus can plausibly bind the two and thereby re-admit
memorized readings; the manipulation check below therefore runs in
BOTH conditions, and the probe's conclusions are keyed to the
as-served arm.

## Pre-registered clauses (graded at this probe; committed before any rater)

Namespace O1–O4. The interpretation is pre-committed: O2–O4 failures
grade the SHAPE-READING hypothesis (i.e., they support the
memorization component of the confound, subject to the nonce-cost
ambiguity above); they license NO change to any census number, NO
re-rating, and NO reflection on the v6 instrument's own grades. An
O1b failure downgrades the interpretation of O2–O4 passes (an
identified format in the as-served condition re-admits memorized
readings); an O1a failure alone narrows the downgrade to the
corpus-intrinsic channel.

- **O1 (manipulation check — run FIRST, before any rating), two
  arms.** O1a: a fresh same-family agent is served ONLY the
  obfuscated corpus and asked to identify what specification it
  comes from — this bounds the corpus-intrinsic identification
  channel. O1b: a second fresh agent is served the AS-SERVED
  material (anonymized preamble + frozen pack + obfuscated corpus)
  and asked the same question — this measures the channel the
  graded raters actually have, including the rule-22 designation
  route. PASS per arm = the answer names none of the format's
  identities, graded by a mechanical case-insensitive
  WORD-BOUNDARY scan for the tokens {icalendar, ical, ics,
  vcalendar, 5545, 2445} (boundary matching so "identical" or
  "hierarchical" cannot false-fail; bare RFC numbers included so
  "RFC5545" spelling variants cannot false-pass). The downgrade
  clause below is keyed to O1b, the as-served arm; O1a is reported
  as the corpus-intrinsic bound. Whether either agent infers the
  calendaring/scheduling DOMAIN generically is reported, not
  graded — the retained temporal vocabulary makes domain inference
  likely and the registration says so.
- **O2 (DOMAIN-mass stability under obfuscation):** of the 194-item
  both-v4-anchor DOMAIN set (J5's set, enumerated in
  `census/v6-pass/README.md`), at least **185** land DOMAIN in each
  obfuscated rater. No measured prior exists for obfuscated rating —
  the floor is a written-justification number: every measured
  original-corpus count is ≥ 193, and 185 (≈95%) grants an
  eight-item nonce-comprehension allowance while still refuting
  memorization-collapse on this set.
- **O3 (the recognition family without its brand tokens):** of the
  nine items {13, 16, 22, 25, 27, 28, 91, 146, 210} — served with
  `q-`/`zeta-` stems in place of the memorized `x-`/`iana-` tokens —
  at least **8** land PROCESS in each rater (the strict 9/9 is
  reported). Two disclosures bound what a PASS means. (a) These are
  the v6 pass's J2 items, there a comprehension check BY
  CONSTRUCTION — the same pack text adjudicates them, and this
  registration does not pretend otherwise: O3 is graded because the
  probe's manipulated variable is the CORPUS, and the question is
  whether the adjudication still transmits when the corpus's
  memorizable identity is gone — transmission-under-obfuscation,
  not discrimination. (b) Rule 25 keys on the trigger phrase
  ("values they don't recognize"), which obfuscation RETAINS; only
  the brand tokens are nonced, so an O3 PASS certifies that
  transmission tolerates identifier removal — it does not certify
  that the identifiers were ever load-bearing.
- **O4 (the within-object trio):** items 192, 193, 194 (the DTSTART
  value-type cluster, its anchor identifier nonced) all land DOMAIN
  in each rater.

**Report-only quantities** (measured, never graded): pair agreement
between the two obfuscated raters; each rater's match-vs-either-v6
count against the v6 pair's ORIGINAL-corpus labels, quoted beside
the measured original-corpus context band (archived raters Ai, Xi,
Av4i, Xv4i, Av5, Xv5 match the v6 pair at 223, 219, 224, 219, 215,
220 of 225 — 95.6–99.6%); shares (probe numbers only); the J4 pair
(62, 150) under obfuscation; the 20-item soft residue; items 37
and 69.

## Raters (pre-registered; a differing serving model is a protocol event)

- **Ao:** fresh same-family `claude-fable-5` via the Agent tool;
  single input file (anonymized preamble + frozen pack + obfuscated
  corpus), blind; one-read attestation.
- **Xo:** foreign `cursor-grok-4.6-high-fast` via cursor-cli, five
  chunks at the pinned iCal partition (1–51 / 52–102 / 103–153 /
  154–204 / 205–225).
- The O1 check agents are two further fresh same-family instances
  (O1a corpus-only; O1b served the full as-served material), run
  before Ao/Xo.
- Malformed-label handling, torn-flags, label normalization, and
  mechanical extraction exactly as in `census/v6-pass/`; labels
  archived verbatim; archives round-trip parsed before push.

**Scorer known-answer-testing, with measured failability:** scored
against archived ORIGINAL-corpus raters, the clauses exhibit both
branches — O2: all eight archived iCal raters pass (every measured
count ≥ 193); its FAIL branch is exhibited by a shipped-spec
mutant: take rater Av6's archived 225 labels
(`census/v6-pass/rfc-v6-pass.md`, first label block), apply a
global Fisher–Yates shuffle seeded `obf-mutant-1` (Python
`random.Random`), and score O2 on the permuted map — measured
result **170/194 DOMAIN, FAIL** (recorded here so the branch is a
number, not a promise). O3: the four pre-v5 raters and both v6
raters pass at 9/9; **Av5 fails at 0/9 and Xv5 at 5/9** (their
archived DOMAIN drift — the convicted readings — are the measured
FAIL branch). O4: six raters pass; **Xi and Xv4i fail** (archived
TYPESTATE ×3 each — both foreign-family raters, a 2-of-8 archived
failure rate on exactly this clause, stated so an O4 pass is read
against it). O1's scan is self-tested on a planted "iCalendar"
string.

**Failure interpretation, restated:** this probe measures whether
classification survives the removal of memorizable identity. It
cannot certify the absence of shared priors (genre-level priors
survive; only a non-LLM rater reaches the confound whole), and
nothing in it touches any census headline, any series figure, or
any instrument grade.
