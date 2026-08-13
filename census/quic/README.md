# RFC 9000 (QUIC) — corpus extraction (2026-08-13; census not yet run)

Third corpus under the frozen instrument — the test limitation 3 of the
paper calls for: whether ≈57% (MLS) to 80–83% (TLS) is a spread or the
ends of a spectrum. **Status: corpus frozen; no predictions registered
yet; no rater has seen it.**

## Corpus definition

- Source: RFC 9000 canonical text,
  `https://www.rfc-editor.org/rfc/rfc9000.txt` (8,485 lines, RFC v3
  plain-text rendering).
- Scope: **§2 (Streams) through §19 (Frame Types and Formats)**, source
  lines 495–6747 — the transport machinery. Decided on measured density
  BEFORE any classification: unlike TLS (one dominant section) QUIC
  spreads its normative mass across the whole protocol spec; this span
  holds 280 of the document's 298 MUST/SHALL-bearing lines (~94%,
  comparable to MLS's ~92% — the span-coverage asymmetry the paper's
  limitation 3 records for TLS §4 (~66%) does not recur here). Excluded:
  §1 Overview (1 line), §20 Error Codes (0), §21 Security Considerations
  (5), §22 IANA (12). Loss-recovery and congestion control live in
  RFC 9002 and packet protection in RFC 9001 — the document boundary is a
  rule-7 censor: this corpus cannot see the obligations those documents
  hold (noted for the CV prediction below).
- Recipe: identical to the MLS census — the same shipped extractor
  (`../mls/extract-corpus.py`), same paragraph/sentence/heading handling.
  Regenerate:
  `python3 ../mls/extract-corpus.py rfc9000.txt 495 6747 out.txt`.
- Result: **n = 281** (`rfc9000_s2-19_musts.txt`). Token conservation
  verified: 285 MUST/SHALL tokens in the source span, 285 in the corpus.
  (A conservation-check note: the corpus legitimately contains the
  substring "PARA" — QUIC's `TRANSPORT_PARAMETER_ERROR` — which is
  vocabulary, not a marker leak; the extractor uses no markers.)
