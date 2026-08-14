# First rating pass under instrument v4 — TLS §4 (pre-pass protocol)

**Status at this commit: protocol registered; NO v4 rater has run.** The
predictions this pass grades are already public: V4, V6 (its TLS third),
V7 (TLS instantiation), and V8 of the v4 amendment
(`codebook/classes.md`, commit `d3d4c2d`, 2026-08-14) — pre-registered
before this pass was commissioned. This file adds no predictions; it fixes
the pass mechanics.

## Instrument

- **Pack:** `codebook/rater-pack-v4.md`, git blob
  `4891605689bc6062cc5c65d9a3cd3dfda80467ea` = the frozen v3 pack (blob
  `a08febba…`) verbatim, plus a "CODEBOOK v4 RULES" section containing the
  v4 precedence paragraph and rules 15–19 verbatim from the amendment,
  with ONE disclosed elision: the seam paragraph's final sentence — "The
  archived TLS pair {188, 189} sits one on each side, and both v4
  predictions are stated below (V8)." — is omitted because it states two
  of the predictions this pass grades. Nothing else is changed; the
  amendment's motivation, direction-disclosure, and prediction sections
  are not part of the pack (they are not instrument).
- **Worked-example settlements, disclosed:** the v4 rule texts, like the
  v3 pack's rule-10 example, settle some corpus items by construction.
  Rule 18's condensed-examples note names RFC 8446 item 181 (so a v4
  rater is TOLD its class family; V6's TLS evidential weight therefore
  rests on items 199 and 203, which the pack does not name). Rule 17's
  evidence-source paragraph discusses items 52, 53, and 60 as
  consumer-use duties in the course of its legacy_version example. Both
  steers are inherited from the amendment's frozen text, not introduced
  by the pack.

## Corpus

`census/tls13/rfc8446_s4_musts.txt`, byte-identical, n = 204 (sha256
`fc7befbc…`, blob `fbc6591a…`).

## Raters

- **Rater Av4** — a fresh same-family (Claude) instance, blind: receives
  the v4 pack and the corpus, nothing else. (There is deliberately NO
  author pass: the author wrote predictions V1–V8 and is maximally
  contaminated.)
- **Rater Xv4** — foreign family (xAI `cursor-grok-4.6-high-fast`), same
  transport and four-chunk protocol as the cross-family replication
  (`census/foreign/README.md`), blind identically.
- Single-shot rule and malformed-label handling: inherited verbatim from
  the cross-family replication's design.

## Grading

Exactly the procedures fixed in the amendment: V4 (nine items TYPESTATE;
156 DOMAIN), V6-TLS ({181, 199, 203} TYPESTATE, CV count 0 on them, with
181's weight discounted per the disclosure above), V7-TLS (outside set =
the 204 minus the 15 named items {the nine} ∪ {156} ∪ {181, 199, 203} ∪
{188, 189}; match = equals A's or D's archived label; rate ≥ 83.8%;
class-count drift within the A–D spread on that set), V8 (188 DOMAIN,
189 REVOCABLE). Predictions are graded per rater. The v3 headline
(80–83%) stands regardless; a v4 eliminable share is a NEW series, and
this report will quote it only next to its instrument version.

## CORRECTION — 2026-08-14, post-pass (found at the paper-integration publish gate)

[The "Worked-example settlements, disclosed" bullet above is incomplete:
it omits V8. The elision removed the seam paragraph's final sentence —
the one naming {188, 189} and the predictions — but the seam paragraph
itself remained in the pack, and its retained text names item 188's
field and constant ("a duration field such as ticket_lifetime ≤ 604800" →
rule-16 territory, DOMAIN when spec-fixed) and item 189's duty
near-verbatim ("retain, cache, or use no longer than T after an event" →
rule-19 territory, REVOCABLE). By this protocol's own standard, V8
is therefore largely settled by construction — a comprehension check
like V6's item 181, not a discrimination test. The original wording
above is preserved; the grades in the companion report are unchanged;
V8's evidential weight is discounted accordingly (the report carries
the matching correction at its finding 1). The omission survived the
pre-pass gate and both rating passes, and was caught only when a fresh
reviewer at the paper-integration gate read the pack next to the
corpus — recorded as another instance of this repository's
flattering-direction defect class.]
