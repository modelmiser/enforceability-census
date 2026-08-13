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
