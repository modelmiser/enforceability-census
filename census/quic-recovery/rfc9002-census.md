# RFC 9002 (QUIC Loss Detection and Congestion Control) §5–§7 — two-blind-rater census (2026-08-13)

**Headline: 23.3% type-eliminable in shape — identical in both raters,
raw agreement 96.7% (one item apart) — the LOWEST share among the
spec MUST-corpora measured under the frozen instrument, and the far end
of their measured range: 23% (recovery) → ≈57% (MLS) → ≈67–69% (QUIC
transport) → 80–83% (TLS §4). (The repository's non-MUST corpora sit
outside this comparison by rule 8: PromQL's classifier census is lower
still, Wayland's higher — different methods, not comparable.)
The algorithmic document's normative shell is procedure and constants
almost all the way down (PROCESS 60%/63%).** Predictions R1–R5 (commit
`44883f5`, publicly timestamped before any rater) graded below.

## Setup — including a disclosed PROTOCOL DEVIATION

- Corpus: n = 30 (`rfc9002_s5-7_musts.txt`, frozen at `58bde79`). Small-n
  caveat pre-registered in the README applies: each item is 3.3 points.
- Instrument: the TLS pass-4 pack, **verbatim** (blob `a08febba…`,
  round-trip verified).
- **Deviation from the census-series design, disclosed:** the intended
  design was author pass + one blind rater, as in the sibling censuses.
  The first blind rater's labels arrived and were SEEN by the author
  before the author pass had been performed; an author pass performed
  after that exposure would not have been independent. The author pass
  was therefore ABANDONED (never performed) and replaced by a **second
  fresh blind rater**. Consequences: this census has no author-context
  measurement, and its two raters are both blind fresh instances of the
  same model family — the shared-model-prior common-cause risk
  (limitation 6 of the paper) applies with full force to the striking
  96.7% agreement below, and no authorial error bar exists for this
  corpus.
- Raters B₁⁗ and B₂⁗: fresh blind LLM agents; two files only, launched
  independently.

## Scores

| measure | value |
|---|---|
| raw item agreement | 29/30 = **96.7%** (one item apart: [30], POLICY vs PROCESS) |
| eliminable-vs-not agreement | 30/30 = **100%** |
| headline eliminable, both raters | 7/30 = **23.3%** (identical: same 7 items) |
| class tallies B₁⁗ | 18 PROCESS, 5 TYPESTATE, 3 THRESHOLD, 2 DOMAIN, 2 POLICY |
| class tallies B₂⁗ | 19 PROCESS, 5 TYPESTATE, 3 THRESHOLD, 2 DOMAIN, 1 POLICY |

## Pre-registered prediction outcomes (bands from `README.md`, commit 44883f5)

| # | prediction (band) | outcome |
|---|---|---|
| R1 | THREE clauses, quoted in full: "the eliminable share is the LOWEST measured on any corpus in this repository: band 15–45%, below MLS's 56.7% bottom endpoint" | **PASS on the two operational clauses** — 23.3% in both raters, in band and below MLS. The dropped-at-first-draft opening clause is **ill-posed as pre-registered**: "any corpus in this repository" is a cross-method comparison the repo's own rule 8 forbids (the PromQL classifier census sits lower still). On the only admissible comparison set — frozen-instrument MUST-corpora — it holds. Recorded as a defect in the pre-registration's wording, not waved through. |
| R2 | PROCESS + THRESHOLD + REVOCABLE ≥ 50% | **PASS** — 70.0% (B₁⁗) / 73.3% (B₂⁗). |
| R3 | deadline/timer edge recurs: REVOCABLE symdiff ≥ 1 | **FAIL — by disuse.** Neither rater used REVOCABLE at all (0 items each, symdiff 0); the PTO/RTT-window duties went to PROCESS and THRESHOLD in both. A prediction of disagreement falsified by unanimous avoidance of the class. |
| R4 | CV = 0 in both raters | **PASS** — 0 and 0; the family's CV lives in RFC 9001 exactly as the document boundary implies (and even there it is nearly censored — see the sibling report). |
| R5 | raw agreement 78–90% (with the pre-registered small-n quantization note) | **FAIL — above the band.** 96.7% exceeds the ceiling the author wrote. The frozen small-n note is direction-neutral ("a near-miss is read against the granularity"), but 96.7 is two items above 90 — not a near-miss — so the two-sided band as written is graded as written: wrong in the unmodeled direction. |

Interpretation, as pre-committed: R3 and R5 failing are wrong guesses
about RFC 9002, recorded as such; nothing is licensed.

## What the census found

1. **The far low end of the measured range, and the family's inside-out
   censoring.** The recovery document holds its content in prose and
   pseudocode — 34 MUST/SHALL-bearing lines in 2,070 (recorded at
   extraction, before classification) — and the shell that IS stated is
   6-of-10ths procedure: how to estimate RTT, how to detect loss, how to
   adjust the congestion window. The stated-obligation surface of the
   QUIC family thus splits by document role exactly as the
   what-the-span-states reading proposes: transport (state machine) ≈
   67–69% eliminable, crypto shell 54–67%, algorithmic shell 23%.
2. **REVOCABLE went unused where the deadline edge was predicted.** On
   QUIC-transport, deadline duties split raters three ways including
   REVOCABLE; here, both raters read the timer/window duties as
   PROCESS/THRESHOLD and never reached for the clock class. One
   consistent reading: 9002's duties are about *computing* with time
   (procedure), not about facts *expiring* — but with two same-family
   blind raters and n = 30, this is noted, not established.
3. **Both-blind agreement at 96.7% is evidence about the instrument AND
   about shared priors, inseparably.** This is the highest agreement in
   the series and the only census with no author rater; the paper's
   limitation-6 caveat (shared model priors are a residual common cause
   that blindness does not remove) is the operative one and this corpus
   is its cleanest exhibit.

## Raw labels (archived verbatim; `?` = rater-flagged torn)

Rater B₁⁗ (blind, first):

```
1:PROCESS 2:PROCESS 3:PROCESS 4:PROCESS 5:THRESHOLD 6:PROCESS 7:THRESHOLD 8:PROCESS 9:TYPESTATE 10:PROCESS
11:PROCESS 12:PROCESS 13:TYPESTATE 14:TYPESTATE 15:TYPESTATE 16:TYPESTATE 17:DOMAIN 18:PROCESS 19:POLICY 20:THRESHOLD
21:PROCESS 22:PROCESS 23:PROCESS 24:PROCESS 25:PROCESS 26:PROCESS 27:PROCESS 28:DOMAIN 29:PROCESS 30:POLICY
```

Rater B₂⁗ (blind, second):

```
1:PROCESS 2:PROCESS 3:PROCESS 4:PROCESS 5:THRESHOLD 6:PROCESS 7:THRESHOLD 8:PROCESS 9:TYPESTATE 10:PROCESS
11:PROCESS 12:PROCESS 13:TYPESTATE 14:TYPESTATE 15:TYPESTATE 16:TYPESTATE 17:DOMAIN 18:PROCESS 19:POLICY 20:THRESHOLD
21:PROCESS 22:PROCESS 23:PROCESS 24:PROCESS 25:PROCESS 26:PROCESS 27:PROCESS 28:DOMAIN 29:PROCESS 30:PROCESS?
```
