# RFC 9001 (Using TLS to Secure QUIC) — corpus extraction (2026-08-13; census not yet run)

Part of the **QUIC document-family completion**: RFC 9000's census (rule-7
disclosure) says its document boundary censors packet protection and
recovery into RFCs 9001/9002. This corpus and `../quic-recovery/` make
that claim cashable: same protocol, same working group, same era — the
only thing that varies is the document's role. **Status: corpus frozen; no
predictions registered yet; no rater has seen it.**

## Corpus definition

- Source: `https://www.rfc-editor.org/rfc/rfc9001.txt` (2,756 lines, v3
  rendering).
- Scope: **§4 (Carrying TLS Messages) through §8 (QUIC-Specific
  Adjustments to the TLS Handshake)**, source lines 337–1982 — the
  mechanism sections, decided on measured density before any
  classification: 70 of the document's 81 MUST/SHALL-bearing lines
  (~86%). Excluded: §1–3 (1 line, the RFC 2119 boilerplate), §7 (0),
  §9 Security Considerations (10 — excluded in every census in this
  repo), §10 IANA (0).
- Recipe: the shipped extractor (`../mls/extract-corpus.py`), unchanged.
  Regenerate: `python3 ../mls/extract-corpus.py rfc9001.txt 337 1982 out.txt`
- Result: **n = 69** (`rfc9001_s4-8_musts.txt`). Token conservation
  verified: 73 = 73.

## Pre-registered predictions (2026-08-13, committed and PUSHED before any rater exists)

Namespace: **K1–K5**. **Instrument: FROZEN** — the TLS pass-4 pack verbatim
(blob `a08febba22fd2cb117a9be41654a6209e0104e57`), codebook v3; rule
candidates 15/16 deliberately NOT adopted. **Failure interpretation,
pre-committed, same as MLS/QUIC:** predictions grade the author's
structural model only; failures license NO re-rating, NO rule change, NO
exclusion, NO quote discretion; quoted numbers are what valid passes
record, as a range if raters disagree. Append-only; corrections in dated
brackets.

- **K1 — CV is the largest or second-largest class: band 25–45%.** This is
  the document the QUIC census's rule-7 disclosure pointed at: packet
  protection, header protection, Retry integrity, key-update verification.
- **K2 — the eliminable share is the lowest of the protocol corpora so
  far measured under this instrument: band 40–60%**, below QUIC's 66.9%
  bottom endpoint, because CV mass is non-eliminable by definition.
- **K3 — the rule-3 derived-constant edge appears HERE too:** the AEAD
  confidentiality/integrity limits (§6) draw at least one
  THRESHOLD-vs-other rater split (symmetric difference ≥ 1 with an
  AEAD-limit duty among the disagreed items).
- **K4 — TYPESTATE is substantial but not dominant: band 20–35%** (key
  phase ordering, handshake-confirmation gates, key-discard duties).
- **K5 — transfer holds with CV under load: raw agreement 78–90%, and CV
  symmetric difference ≤ 2 even as a dominant class** — the secret-material
  discriminator's hardest test yet (its zero-variance record was earned on
  1–6-item slivers).
