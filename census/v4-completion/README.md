# v4 completion passes — MLS, QUIC, RFC 9001 (pre-pass protocol)

**Status at this commit: protocol registered; NO rater has run.** These
three passes grade the remaining predictions of the v4 amendment
(`codebook/classes.md`, `d3d4c2d`): **V1, V3, V6-MLS** (MLS), **V2,
V6-QUIC** (QUIC), **V5, V6-9001** (RFC 9001), plus **V7** instantiated per
corpus. V4/V8 (TLS) were graded in `census/v4-tls/`. This file adds no
predictions; it fixes mechanics and states the evidential discounts.

## Instrument

`codebook/rater-pack-v4.md`, blob `4891605…` — identical to the v4-tls
pass, including its one disclosed elision (a TLS-prediction sentence;
irrelevant to these corpora but kept for blob identity).

## Worked-example settlements — the honesty section, read before grading

The v4 rules were distilled FROM these corpora's measured disagreements,
and their texts quote real items as examples. A rule that names an item
settles it by construction: the rater is told, not asked. Stated per
prediction, what the pack gives away and where discriminating evidence
remains:

- **V2 (QUIC nine):** rule 16's examples name the 20-byte CID cap
  (→ items 197–200, 266), the 8-byte minimum (→ 41), and the
  at-least-2 parameter floor (→ 238, 239). **Eight of the nine are
  settled by example; the discriminating item is 191 alone** (63 is
  carved out by the amendment).
- **V3 (MLS AEAD pair):** rule 16 names "AEAD *usage* limits" as its
  cumulative example (→ 126 settled). **The contrast's discriminating
  half is item 20** (the per-message datum side, which the pack does not
  name).
- **V1 (MLS capability five):** no item numbers appear, but rule 15's
  vocabulary ("a LeafNode") is MLS's own and the rule was built from
  these items' form. Steered, not itemized — graded with that noted.
- **V5 (9001 lifecycle split):** rule 18's condensed-examples note names
  items **37, 34, 14, 18** (two per side — settled). **Discriminating
  items: 13, 36, 38 (predicted TYPESTATE) and 20, 43 (predicted
  PROCESS).**
- **V6:** heavily example-settled: rule 19 quotes QUIC 69's and
  163/164's duties and 9001 item 21's sentence nearly verbatim; rule
  18's PROCESS example matches MLS 34's delete-duty phrasing, and rule
  19's bare-adverb clause ("as soon as", "immediately") touches MLS 43.
  **Only MLS 44 is fully un-named.** V6 is graded per the
  pre-registration but is closer to a comprehension check than a
  discrimination test; stated here so the report cannot quietly claim
  otherwise.
- **V7 (per corpus):** the outside sets are untouched by any example and
  carry the bulk of this arc's real evidence.

## Corpora, raters, mechanics

- Corpora byte-identical to their censuses: MLS n=127, QUIC n=281,
  RFC 9001 n=69.
- Per corpus, two blind raters, as in `census/v4-tls/`: a fresh
  same-family (Claude) instance (single file: pack + corpus; no other
  input) and foreign `cursor-grok-4.6-high-fast` via cursor-cli
  (chunks of ≤51 items: MLS 3, QUIC 6, RFC 9001 2). Single-shot rule
  and malformed-label handling inherited from `census/foreign/README.md`.
  NO author passes (the author wrote the predictions).
- **V7 instantiation** (amendment wording, applied): outside sets =
  corpus minus the items named in the predictions for that corpus —
  MLS: 127 − {90,111,113,114,115, 20,126, 34,43,44} → **117 items**;
  QUIC: 281 − {41,191,197,198,199,200,238,239,266, 63, 69,163,164} →
  **268 items**; RFC 9001: 69 − {13,14,15,18,20,34,36,37,38,43, 21} →
  **58 items**. Match = equals either archived v3 rater's label (both
  raters' full maps are archived in each census report; archived `?`
  torn-flags are stripped, the label stands). Floors = each corpus's
  archived raw inter-rater agreement: **85.0% (MLS), 85.1% (QUIC),
  76.8% (RFC 9001)** — single archived numbers, no fork. Clause (b)
  bounds from the archived pair's per-class counts on the outside set,
  reported under BOTH readings of the spread clause (the fork found in
  `census/v4-tls/` finding 6, unrepaired until v5).
- v3 headlines stand for all three corpora; v4 shares are a new series
  quoted only with their instrument version.
