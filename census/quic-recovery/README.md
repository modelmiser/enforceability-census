# RFC 9002 (QUIC Loss Detection and Congestion Control) — corpus extraction (2026-08-13; census not yet run)

Part of the **QUIC document-family completion** (see `../quic-tls/`).
**Status: corpus frozen; no predictions registered yet; no rater has seen
it.**

## Corpus definition

- Source: `https://www.rfc-editor.org/rfc/rfc9002.txt` (2,070 lines, v3
  rendering).
- Scope: **§5 (Estimating the Round-Trip Time) through §7 (Congestion
  Control)**, source lines 312–1249 — the algorithmic core, holding 33 of
  the document's 34 MUST/SHALL-bearing lines (~97%). Excluded: §1–4
  (1 line, RFC 2119 boilerplate), §8 Security Considerations (0).
- **Density observation, recorded at extraction (before any
  classification): this document is an order of magnitude sparser in
  normative keywords than its siblings** — 34 MUST/SHALL lines in 2,070
  (RFC 9000: 298 in 8,485; RFC 9001: 81 in 2,756). The algorithmic
  document states its content as prose and pseudocode, not as RFC 2119
  duties. Whatever the census finds, the corpus it finds it on is the
  small normative shell around a largely non-normative algorithm — a
  rule-7 censor operating INSIDE a document, not just at its boundary.
- Recipe: the shipped extractor (`../mls/extract-corpus.py`), unchanged.
  Regenerate: `python3 ../mls/extract-corpus.py rfc9002.txt 312 1249 out.txt`
- Result: **n = 30** (`rfc9002_s5-7_musts.txt`). Token conservation
  verified: 33 = 33. (Comparable in size to the TLS alert probe, n = 25;
  quote-with-caveat granularity applies.)

## Pre-registered predictions (2026-08-13, committed and PUSHED before any rater exists)

Namespace: **R1–R5**. **Instrument: FROZEN** (blob `a08febba…`, codebook
v3; candidates 15/16 NOT adopted). **Failure interpretation,
pre-committed, same as the sibling censuses:** predictions grade the
author's structural model only; failures license nothing. Append-only.

- **R1 — the eliminable share is the LOWEST measured on any corpus in
  this repository: band 15–45%**, below MLS's 56.7% bottom endpoint. The
  normative shell of an algorithmic document should be procedure, timers,
  and constants, not wire predicates.
- **R2 — PROCESS + THRESHOLD + REVOCABLE together ≥ 50%** of the 30.
- **R3 — the deadline/timer edge measured on QUIC recurs: REVOCABLE
  symmetric difference ≥ 1** (PTO and RTT-window duties read as clock vs
  inequality vs procedure).
- **R4 — CV = 0 in both raters** (no cryptographic verification duties in
  the recovery document; the family's CV lives in RFC 9001).
- **R5 — transfer holds at small n: raw agreement 78–90%** (n = 30 makes
  each item worth 3.3 points; the band is wide precisely because the
  quantization is coarse — noted here so a near-miss is read against the
  granularity, not silently excused).
