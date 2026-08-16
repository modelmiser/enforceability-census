# Human-rater pass H1 — registration (PUSHED BEFORE ANY RATER RATES)

**What this is, and is not.** The first non-LLM rating pass in this
repository — the probe of limitation 6's *corpus-shared-prior*
confound (every frontier LLM trained on these RFCs; a shared reading
learned from the corpus would reproduce the archived agreements).
The obfuscation probe (`census/obfuscation/`) measured that lexical
obfuscation does not reach this confound — RFC 5545 stayed
identifiable from structure and disclosed residuals at 95/98% — and
its report's argued extension is that no lexical design would; a
non-LLM rater is thereby the sole remaining route, and this pass is
that rater. It is NOT a census: the sample below is deliberately
stratified toward the corpus's soft residue, so **no share headline
exists here by design** — a stratified sample must not be read as a
census, and no number from this pass ever joins, replaces, or
requalifies any series figure. What it measures is *agreement*: does
the frozen instrument transmit to a human at levels comparable to
the archived LLM band?

**Honest bounds, stated first.** One human, one corpus, one 60-item
sample. A strong result weakens the confound; it cannot eliminate it
(n = 1). A weak result is AMBIGUOUS between (i) shared-LLM-prior
inflation of the archived agreements and (ii) individual human-rater
noise or effort — this design cannot separate those two with one
rater, and the registration says so now, before any outcome is
known. Either way: no census number changes, no re-rating occurs,
and nothing here reflects on any instrument grade. The human's
labels grade the hypothesis space, never the human. One further
disclosed asymmetry: the archived raters labeled all 225 items in
one context; their restricted-to-sample numbers below were produced
with full-corpus context the human will not have.

## The rater seat (owner decision recorded 2026-08-16)

**H1: one recruited non-author human**, who has not read this
repository, its reports, or any account of its findings — the clean
seat, chosen over author-as-rater (which would have carried a
disclosed exposure confound: the owner knows the archived agreement
levels and the corpus's class skew). Recruitment is the owner's;
identity (a pseudonym is fine) and a one-line blindness attestation
are recorded in a **marked, append-only addendum to this file before
rating begins**. Rating conditions, verbatim in the packet: one
sitting, roughly 90 minutes; only the packet — no RFC lookups, no
web, no AI assistance, no discussing items until labels are
returned; one `NUMBER:LABEL` line per item; a trailing `?` for
genuinely torn. Any deviation from these conditions is a protocol
event, disclosed in the report.

## The sample (n = 60, frozen at this registration)

Three strata, mutually disjoint by construction, served **unmarked
and in corpus order** — the rater never sees strata:

- **S-OUT (20)** — the v6 registration's iCalendar outside set, the
  corpus's enumerated residual soft mass (`census/v6-pass/README.md`):
  {1, 2, 7, 37, 46, 47, 69, 77, 79, 118, 138, 141, 185, 192, 193,
  194, 200, 201, 203, 204}.
- **S-FAM (11)** — the recognition family {13, 16, 22, 25, 27, 28,
  91, 146, 210} plus the J4 pair {62, 150}.
- **S-J5 (29)** — a seeded draw from the 194-item both-anchor DOMAIN
  set (J5, enumerated in `census/v6-pass/README.md`): Python
  `random.Random("enforceability-census-human-h1").sample(S194, 29)`,
  sorted — {3, 17, 21, 23, 26, 34, 40, 63, 64, 65, 81, 82, 84, 92,
  98, 111, 114, 115, 122, 124, 134, 148, 149, 151, 169, 175, 180,
  213, 214}. The scorer re-derives this draw from the seed at every
  run; a mismatch is a protocol event.

Item texts are taken verbatim from the frozen corpus
`census/ical/rfc5545_s3_musts.txt`, original numbering kept.

## The instrument, served

The FROZEN v6 pack, `codebook/rater-pack-v6.md`, blob
`f4f9e0b1c478cc05370e8b4ba7f612320698d8f0` — rule 14 verbatim; this
pass cuts no pack. The packet (`packet-h1.md`) embeds the pack
between machine-checked markers; the scorer's known-answer test
asserts byte-identity between the packet's pack section and the
repository file on every run. The preamble (transport, not
instrument) names the corpus — RFC 5545 §3 — as the LLM servings
did (the obfuscation registration discloses that the standard
preamble names the format; anonymization there was the exception).
Beyond the sample-vs-full-corpus asymmetry disclosed above, the
information diet matches the LLM raters': pack, items, nothing
else.

## Pre-registered clauses (committed before any rater)

Namespace H. No measured prior exists for human raters anywhere in
this repository, so both floors are written-justification numbers,
and their failure interpretation is the pre-committed ambiguity
above — a failure licenses nothing except its own honest report.

Both floors follow one stated principle: **the smallest integer that
every measured fail branch fails** — measurement-forced, with no
unacknowledged margin.

- **H1 (DOMAIN-mass transmission):** of the 29 S-J5 items — all
  both-anchor DOMAIN, every archived rater 29/29 on them — at least
  **25** land DOMAIN. Floor justification, measured: a
  label-shuffle mutant (Fisher–Yates of Av6's 225 labels, seed
  `human-mutant-1`) scores **24/29** on this clause — the shuffled
  map is 88.4% DOMAIN (Av6's 199/225), so shuffling barely dents
  DOMAIN mass, and a floor of 24 would be a check the shuffle
  degenerate PASSES. 25 is the smallest floor the shuffle's 24
  fails; the floor is exactly that minimum, and it grants the
  human a 4-item (~14%) allowance below the archived raters'
  uniform 29/29. DISCLOSED PLAINLY: a rater who answers DOMAIN for
  everything passes H1 by construction (measured: 29/29) — H1
  alone refutes neither degenerate; the H1+H2 pair refutes both.
- **H2 (the recognition family):** of the 9 S-FAM recognition items,
  at least **6** land PROCESS. Archived branches, measured on
  exactly this clause: six raters at 9/9; **Av5 at 0/9 and Xv5 at
  5/9 FAIL it** (their convicted DOMAIN drift); the shuffle mutant
  scores 1/9 and constant-DOMAIN 0/9 — both FAIL. 6 is the
  smallest floor that fails every measured branch (the largest,
  Xv5's, is 5); the floor is exactly that minimum, granting the
  human a 3-item allowance below the six 9/9 raters. Correlation
  disclosed: the nine items are two near-duplicate textual
  clusters — three "MUST ignore" items (13, 91, 210) and six "MUST
  treat …the same way as they would the ⟨default⟩ value" items —
  so the nine outcomes are correlated and "of 9" overstates
  independence (Xv5's measured 5/9 shows splits do occur). A human
  PASS is single-rater evidence that the adjudication transmits
  outside the LLM population; a FAIL carries the pre-committed
  ambiguity.

**Report-only quantities** (measured, never graded): match-vs-either-v6
over the 60 (each item counts if the label matches either v6 rater's
archived original-corpus label, normalization as below), quoted
beside the measured context band; per-stratum breakdown; the J4 pair
{62, 150} item-by-item; the 20 S-OUT items item-by-item against the
v6 pair; torn count; per-class distribution. Label normalization,
as in every pass since v5: torn `?` stripped for scoring, base label
governs; U ≡ UNCLASSIFIED, NEG ≡ NEGOTIATION, CV ≡ CRYPTO-VERIFY.

**The measured context band** (every archived iCalendar rater,
restricted to this sample; computed at registration, asserted by the
scorer's KAT):

| rater | H1 (of 29) | H2 (of 9) | match-vs-either-v6 (of 60) |
|---|---|---|---|
| Ai | 29 | 9 | 58 |
| Xi | 29 | 9 | 54 |
| Av4i | 29 | 9 | 59 |
| Xv4i | 29 | 9 | 54 |
| Av5 | 29 | **0** | 50 |
| Xv5 | 29 | 5 | 55 |
| Av6 | 29 | 9 | 60 |
| Xv6 | 29 | 9 | 60 |
| shuffle mutant | **24** | **1** | 31 |
| constant-DOMAIN | 29 | **0** | 36 |

By-construction cells, flagged: Av6/Xv6's match 60/60 is self-match
(match is vs-either-v6), and Av4i/Xv4i's H1 29/29 is definitional
(J5 *is* their DOMAIN intersection). The measured **non-anchor**
band is 50–59 of 60 (83–98%); the two degenerate strategies sit at
31 and 36. The human's match number is reported
against this band, not graded against a floor — inventing a floor
where no rater-class prior exists would be a guess wearing a
clause's clothes.

## Scoring

`score_h1.py` (shipped here) is the only grader. Its known-answer
test: re-derives the frozen draw from its seed; verifies the
packet's pack section byte-identical to `codebook/rater-pack-v6.md`;
re-scores all eight archived raters and asserts the table above
exactly; exhibits both fail branches (shuffle mutant, constant-
DOMAIN). Every check was watched to fail before registration: a
perturbed KAT expectation fails at the perturbed rater, and a
one-byte packet perturbation fails the byte-identity assert. The
rater's labels will be archived verbatim in the report and
round-trip parsed before push.
