# RFC 9001 (QUIC-TLS) §4–§8 — two-rater census (2026-08-13)

**Headline: 54–67% type-eliminable in shape — quoted wide (A‴ 53.6%,
B‴ 66.7%) because raw agreement was 76.8%, the FIRST corpus in this
series to fall below the 78–90% transfer band. All five pre-registered
predictions failed, including the central one: the crypto document's
normative surface is NOT crypto-verification-dense (CV = 1.4%/2.9%, vs
the predicted 25–45%).** Predictions K1–K5 (commit `44883f5`, publicly
timestamped before any rater) graded below; per the pre-committed
interpretation, outcomes grade the author's structural model and license
nothing.

## Setup

- Corpus: n = 69 (`rfc9001_s4-8_musts.txt`, frozen at `58bde79`).
- Instrument: the TLS pass-4 rater pack, **verbatim** (blob `a08febba…`,
  `git cat-file` round-trip verified).
- Rater A‴: the census author (context NOT controlled); labels written to
  disk before the blind pass returned.
- Rater B‴: fresh blind LLM agent; two files only.

## Scores

| measure | value |
|---|---|
| raw item agreement | 53/69 = **76.8%** — below the 78–90% band that held on TLS, MLS, and QUIC |
| eliminable-vs-not agreement | 58/69 = **84.1%** |
| headline eliminable, A‴ | 37/69 = **53.6%** |
| headline eliminable, B‴ | 46/69 = **66.7%** |
| class tallies A‴ | 20 TYPESTATE, 18 PROCESS, 17 DOMAIN, 5 META, 5 THRESHOLD, 2 NEG, 1 CV, 1 POLICY |
| class tallies B‴ | 28 TYPESTATE, 18 DOMAIN, 5 META, 5 THRESHOLD, 4 PROCESS, 4 NEG, 2 CV, 2 U, 1 REVOCABLE |

## Pre-registered prediction outcomes (bands from `README.md`, commit 44883f5)

| # | prediction (band) | outcome |
|---|---|---|
| K1 | CV largest or second-largest class, band 25–45% | **FAIL, decisively** — CV is 1/69 (A‴) and 2/69 (B‴): 1.4%/2.9%. See finding 1. |
| K2 | THREE clauses, quoted in full: "the eliminable share is the lowest of the protocol corpora so far measured under this instrument: band 40–60%, below QUIC's 66.9% bottom endpoint" | **FAIL — 1 of 3 clauses passes.** *Lowest protocol corpus so far*: FAIL for B‴ (66.7% is above both MLS raters' 56.7/57.5). *Band 40–60%*: FAIL for B‴ (6.7 above the ceiling; A‴ in band). *Below QUIC's 66.9%*: PASS on both raters (B‴ by 0.2). Strict per-rater reading governs. |
| K3 | AEAD-limit duties draw a THRESHOLD-vs-other split (symdiff ≥ 1 with an AEAD-limit item among them) | **FAIL — by unanimity.** THRESHOLD symmetric difference is 0; the five AEAD-limit items ({26, 51, 52, 53, 55}) are item-identical across both raters. The rule-3 edge predicted here did not appear: a prediction of disagreement, falsified by agreement. |
| K4 | TWO clauses, quoted in full: "TYPESTATE is substantial but not dominant: band 20–35%" | **FAIL — both clauses.** *Not dominant*: FAIL — TYPESTATE is the largest class for BOTH raters (A‴ 20 vs PROCESS 18; B‴ 28 outright). *Band*: A‴ 29.0% in band; B‴ 40.6% above it. |
| K5 | TWO clauses: (a) raw agreement 78–90%; (b) CV symdiff ≤ 2 as a dominant class | **FAIL — 1 of 2 clauses passes.** (a) FAIL: 76.8%, 1.2 points below the floor — the first census to fall BELOW the band (at n = 69, one item ≈ 1.45 points; the breach is one item deep). (b) PASS vacuously reframed: CV symdiff is 1 (item 30), within ≤ 2 — but CV was never a dominant class (see K1), so the clause's premise ("under load") never obtained. Graded PASS on the letter, with the premise-failure noted. |

Interpretation, as pre-committed: all five failures are wrong guesses
about RFC 9001, recorded as such. No re-rating, no rule change, no
exclusion, no quote discretion — and the wide 54–67% headline is the
honest consequence of quoting what two valid raters recorded.

## What the census found

1. **The crypto document's normative surface is not made of crypto
   duties — verification is censored INSIDE the document.** RFC 9001's
   MUST/SHALL sentences state key lifecycle (discard/retain/update),
   phase ordering, limits, and TLS-interface constraints. The AEAD
   protection and verification themselves are described procedurally
   ("packets are protected with...") and as inline conditions ("cannot be
   unprotected"), not as sentence-level MUST-verify duties — so a
   MUST-sentence census barely sees them. This is the same rule-7
   censoring the sibling report records for RFC 9002's pseudocode, one
   level deeper: not "the obligations live in another document" but "the
   obligations live in this document's non-normative grammar." A census
   of stated obligations measures what specs STATE; RFC 9001 states the
   shell around its cryptography, not the cryptography.
2. **The transfer-band breach localizes to one boundary.** Ten of the 16
   disagreements are A‴:PROCESS vs B‴:TYPESTATE-or-DOMAIN on key-lifecycle
   duties (items 13, 14, 15, 18, 20, 34, 36, 37, 38, 43 — discard keys at
   phase transitions, don't process before handshake completion, reset
   stream state; item 15, alert-fatality handling, rides with the cluster
   by label pair though not by subject): the author read internal key/state management as
   procedure; the blind rater read connection-phase obligations as
   history-indexed state. This is the PROCESS/TYPESTATE judgment boundary
   (rule 10/13 territory) concentrated by a document whose whole subject
   is key state — the census-series' measured floor (78–90%) broke on the
   corpus with the highest density of exactly the boundary the codebook
   already knows requires judgment.
3. **The AEAD-limit family transmitted perfectly here** — five items,
   both raters, THRESHOLD, item-identical — while the same family drew
   splits on QUIC. Same instrument, same class, different corpus context:
   boundary crispness is not even a per-class constant; it interacts with
   the surrounding corpus. (Recorded as an observation against the rule-16
   candidate's framing, not as evidence for a new rule.)
4. **DISAGREE bucket: 16 items (23.2%), unresolved by design:** the
   key-lifecycle cluster above (10), U-boundary (2: 31, 46), NEG boundary
   (2: 25 — B‴ read "MUST NOT reject unsupported cipher suite offers" as
   negotiation-tolerance; 60 — error-code duty read as NEG), CV boundary
   (1: 30, unprotection-failure handling), REVOCABLE (1: 21, the
   discard-within-3×PTO deadline — the deadline edge again, one item).

## Author-context note

A‴'s labels were on disk before B‴ returned — a claim resting on the
session record, which is not in this repository; a reader cannot verify
it independently (the same holds for all pushed-before-rater timing
claims, whose public witnesses are the GitHub timestamps). No E1-class
antecedent lookups occurred. The
author-side PROCESS concentration (18 vs 4) is itself plausibly an
authorial-context artifact — A‴ rated knowing the MLS census's
delete-key-material convention — and is left as the visible error bar.

## Raw labels (archived verbatim; `?` = rater-flagged torn)

Rater A‴ (author):

```
1:TYPESTATE 2:TYPESTATE 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:DOMAIN 7:DOMAIN 8:CV 9:TYPESTATE 10:TYPESTATE
11:DOMAIN 12:DOMAIN 13:PROCESS 14:PROCESS 15:PROCESS 16:TYPESTATE 17:TYPESTATE 18:PROCESS 19:TYPESTATE 20:PROCESS
21:PROCESS? 22:META 23:PROCESS 24:DOMAIN? 25:PROCESS 26:THRESHOLD 27:META 28:DOMAIN 29:TYPESTATE 30:PROCESS?
31:POLICY? 32:META 33:DOMAIN 34:PROCESS 35:TYPESTATE 36:PROCESS 37:PROCESS 38:PROCESS 39:DOMAIN 40:DOMAIN
41:TYPESTATE 42:TYPESTATE 43:PROCESS 44:TYPESTATE 45:TYPESTATE 46:PROCESS 47:PROCESS 48:TYPESTATE 49:TYPESTATE 50:PROCESS
51:THRESHOLD 52:THRESHOLD 53:THRESHOLD 54:PROCESS 55:THRESHOLD 56:META 57:META 58:DOMAIN 59:NEG 60:DOMAIN
61:TYPESTATE 62:NEG 63:TYPESTATE 64:DOMAIN 65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:DOMAIN
```

Rater B‴ (blind):

```
1:TYPESTATE 2:TYPESTATE 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:DOMAIN 7:DOMAIN 8:CV 9:TYPESTATE 10:TYPESTATE
11:DOMAIN 12:DOMAIN 13:TYPESTATE 14:TYPESTATE 15:DOMAIN 16:TYPESTATE 17:TYPESTATE 18:TYPESTATE 19:TYPESTATE 20:TYPESTATE
21:REVOCABLE 22:META 23:PROCESS 24:DOMAIN 25:NEG 26:THRESHOLD 27:META 28:DOMAIN 29:TYPESTATE 30:CV
31:U 32:META 33:DOMAIN 34:DOMAIN 35:TYPESTATE 36:TYPESTATE 37:TYPESTATE 38:TYPESTATE 39:DOMAIN 40:DOMAIN
41:TYPESTATE 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:U 47:PROCESS 48:TYPESTATE 49:TYPESTATE 50:PROCESS
51:THRESHOLD 52:THRESHOLD 53:THRESHOLD 54:PROCESS 55:THRESHOLD 56:META 57:META 58:DOMAIN 59:NEG 60:NEG
61:TYPESTATE 62:NEG 63:TYPESTATE 64:DOMAIN 65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:DOMAIN
```
