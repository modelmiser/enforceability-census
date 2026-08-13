# The QUIC document family — synthesis (2026-08-13)

RFC 9000 (transport), RFC 9001 (TLS integration), and RFC 9002 (recovery)
are one protocol split across three documents by one working group in one
era — the cleanest available control for the claim that the
type-eliminable share is a property of *what a span states as
obligations*: protocol, era, and authorship are held fixed while the
document's role varies (rater pairs, spans, and n vary too — see the
pooling caveat below).

| document | span | n | eliminable (per-rater) | dominant class | census |
|---|---|---|---|---|---|
| RFC 9000 transport | §2–§19 | 281 | 66.9% / 69.0% | TYPESTATE (~46%) | [`quic/`](quic/rfc9000-census.md) |
| RFC 9001 TLS shell | §4–§8 | 69 | 53.6% / 66.7% (agreement below band — see report) | TYPESTATE/PROCESS split | [`quic-tls/`](quic-tls/rfc9001-census.md) |
| RFC 9002 recovery shell | §5–§7 | 30 | 23.3% / 23.3% | PROCESS (~60%) | [`quic-recovery/`](quic-recovery/rfc9002-census.md) |

**Within this family, document role — not protocol — tracks the mix** — within one
protocol the eliminable share spans 23% to 69% by document. The state
machine document is two-thirds type-shaped; the algorithmic document's
normative shell is one-quarter; the crypto document sits between, its
actual cryptography censored into non-normative grammar (its CV class is
1–3% despite being "the crypto document").

**Pooled whole-family figure, with its caveat stated before the number:**
pooling sums spans rated by different rater pairs (9002's pair is
blind-blind; the others author+blind), so this is a weighted average of
differently-measured quantities, quoted only at coarse granularity:
232/380 to 247/380 ≈ **61–65% of the QUIC family's stated normative
surface is type-eliminable in shape**. The RFC 9000 census's rule-7
disclosure ("the document boundary censors CV and recovery out of this
corpus") is hereby cashed: the whole-family figure is ~4 points below the
transport document's own (~4–6 points across the endpoint pairings).

Provenance: all three corpora frozen and all three prediction sets
(Q1–Q5, K1–K5, R1–R5) publicly pushed before any rater existed
(commits 36f8334/29fcf08 for 9000; 58bde79/44883f5 for 9001+9002).
