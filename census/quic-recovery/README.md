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
