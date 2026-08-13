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

## Pre-registered predictions (2026-08-13, committed and PUSHED before any rater exists)

Namespace: **Q1–Q5** (distinct from TLS P1–P4, MLS M1–M5, and codebook rule
numbers). **Instrument: FROZEN** — the TLS pass-4 rater pack verbatim (blob
`a08febba22fd2cb117a9be41654a6209e0104e57`), codebook v3. No amendment
between this commit and completion of the rating passes; candidate rule 15
(capability-compatibility, from the MLS census) is deliberately NOT
adopted — if the boundary recurs here, it recurs under the same frozen
text that measured it there.

**Failure interpretation, pre-committed (same as MLS, and it binds the
same way):** these predictions grade the author's structural model of
QUIC, nothing else. A failed prediction licenses NO re-rating, NO rule
change, NO exclusion of any valid-instrument rater, NO discretion over
what to quote. The quoted numbers are whatever the valid passes record, as
a range if raters disagree. This block is append-only; corrections in
dated brackets.

The predictions:

- **Q1 — the eliminable share lands between the two measured points,
  nearer TLS: band 68–80%**, strictly above MLS's 57.5% top endpoint.
  Reason: QUIC's censused span is machinery-dense — stream/connection
  state machines, flow-control consistency, packet/frame formats — and
  its procedural mass (loss recovery, congestion control) was moved into
  RFC 9002, outside this corpus.
- **Q2 — the crypto core is SMALLER than TLS's: CV ≤ 4% (≤ 11 of 281).**
  Packet protection and handshake crypto live in RFC 9001; the document
  boundary censors CV out of this corpus (rule 7 in action, predicted in
  advance this time).
- **Q3 — TYPESTATE is the largest single class, band 35–50%.** Stream
  states, connection lifecycle, flow-control limits that track
  peer-advertised values (cross-message consistency by decision rule 1),
  migration ordering.
- **Q4 — the rule-3 edge measured on MLS recurs on QUIC's spec-fixed
  constants.** QUIC obliges numeric limits chosen by the SPEC, not the
  operator and not the framing (the 3× anti-amplification limit, the
  1,200-byte minimum datagram size). Prediction: the raters split on at
  least one such item (THRESHOLD symmetric difference ≥ 1, with a
  spec-fixed constant among the disagreed items). A pass here means the
  derived-but-not-chosen gap in decision rule 3 is reproducible, not an
  MLS artifact.
- **Q5 — transfer holds on the classes Q4 does not implicate: raw
  agreement 78–90%; META, REVOCABLE, and CV each ≤ 1 item symmetric
  difference.** (THRESHOLD is deliberately excluded from this clause —
  Q4 predicts its variance; the MLS lesson about quoting all clauses of a
  prediction applies to this one in full.)
