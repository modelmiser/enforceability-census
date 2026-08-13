# RFC 9420 (MLS) — corpus extraction (2026-08-13; census not yet run)

Second security-RFC census (the TLS census's optional follow-up: turn one
data point into a comparison). **Status: corpus frozen; no predictions
registered yet; no rater has seen it.**

## Corpus definition

- Source: RFC 9420 canonical text, `https://www.rfc-editor.org/rfc/rfc9420.txt`
  (7,040 lines; RFC v3 plain-text rendering, no page furniture).
- Scope: **§5 (Cryptographic Objects) through §15 (Application Messages)**,
  source lines 1131–5307 — the protocol machinery an implementation must
  obey, the analog of the TLS census's §4 scope. Decided on measured
  density BEFORE any classification: this span holds 132 of the document's
  144 MUST/SHALL-bearing lines. Excluded: §1–4 (intro/terminology/overview/
  concepts — zero normative lines outside §2's RFC 2119 boilerplate and
  presentation-language rules), §16 Security Considerations (2 lines),
  §17 IANA (4 lines), matching the TLS census's exclusion of everything
  outside its handshake section.
- Recipe: identical to the TLS census (join paragraphs, split sentences,
  filter `\bMUST\b|\bSHALL\b`), with two mechanical refinements, both
  recorded here because the TLS census had to bracket-correct its
  "regenerable by script" claim: (1) the extractor SHIPS
  (`extract-corpus.py`); (2) sentences are split within paragraphs and
  numbered heading lines are dropped, so no marker text or heading can glue
  into an item. Blank-line-separated bullets become individual items.
- Result: **n = 127** (`rfc9420_s5-15_musts.txt`). Token conservation
  verified: 133 MUST/SHALL tokens in the source span, 133 in the corpus.

Regenerate: `python3 extract-corpus.py rfc9420.txt 1131 5307 out.txt`
(fetch the RFC text from the URL above; it is not vendored).

## What happens next (order is the method)

1. Pre-registered predictions committed BEFORE any rater exists (class-mix
   direction vs TLS: crypto core, NEG mass, TYPESTATE share), as a dated
   section here or in the codebook — the rater pack itself stays frozen at
   blob `a08febba…`; any pack change would be a new instrument version.
2. Author pass (rater A') + at least one fresh blind rater under the
   verbatim pack.
3. Report with the TLS↔MLS comparison; DISAGREE bucket unresolved by
   design, as always.
