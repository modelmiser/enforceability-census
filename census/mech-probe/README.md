# MECH-PROBE-1 — can a non-LLM classifier recover predicate shape from RFC prose?

**2026-08-20 · Feasibility probe, NOT a registered pass. Negative. Arc closed.**
**MLS (RFC 9420 §5–15) is SPENT as a probe corpus by this run.**

## Why this exists

Limitation 6 records that all raters in this repository are LLM agents, and the
obfuscation probe's O1 check measured that the shared prior is real — RFC 5545
was identified from structure alone through 90 nonces. The registered human
passes H1-R2 and HL1 exist to reach that confound from outside the LLM
population; both are blocked on recruiting a blind human.

A rule-based classifier needs no recruit and **cannot hold a prior about
RFC 5545 — a regex has no training data.** This probe asked whether that route
is available. It is not, and the reason is specific enough to be worth keeping.

## Protocol (`PLAN.md`, frozen before the classifier)

`mech1.py` (md5 `b8739771e855ade2acc6829d9f867614`) was written from
`codebook/classes.md` (the four core classes, precedence rules 1, 2, 6) and
`codebook/rater-pack-v6.md` §Classes alone. Every pattern cites the definition
phrase it derives from. **No MLS label was loaded or displayed before the
classifier was frozen.** One run. No tuning loop — adjusting a rule after seeing
agreement would have voided the probe, and did not occur.

## Result: not a measurement

| | value |
|---|---|
| coverage | **56/127 = 44.1% classified; 55.9% UNCLASSIFIED** |
| agreement, covered items only, rater 1 | 26/56 = 46.4% |
| agreement, covered items only, rater 2 | 30/56 = 53.6% |
| const-DOMAIN baseline (same items) | 28.6% / 30.4% |
| seeded-shuffle baseline (same items) | 25.0% / 21.4% |

**Codebook rule 3 already calls a 29.1% unclassified bucket "never a
measurement."** This bucket is 55.9%, so the covered-item agreement is not
quotable as a result: it is accuracy on the items the instrument chose to
answer, while it declined more than half. It does beat both degenerates on that
subset by 16–23 points, so predicate shape is *partially* lexically
recoverable — just not enough of it.

## Why it failed — the errors are not scattered

**DOMAIN↔TYPESTATE confusions, in both directions, are 11/30 and 8/26 of all
errors.** That is exactly decision rule 1:

> Cross-MESSAGE consistency = TYPESTATE; intra-message cross-field = DOMAIN.

A regex cannot see message boundaries. The codebook's discriminators are
**structural** — which message a field lives in; secret versus public material
for CV; framing-derived versus chosen bound for THRESHOLD — and prose expresses
structure without dedicated vocabulary. That is what a lexical instrument
cannot reach, and it is not a regex-quality problem.

## The design finding, which outranks the number

Codebook rule 3 prescribes the repair: read the unclassified bucket, fix the
classifier, publish pre-fix and post-fix ratios side by side. **That path is
unavailable to this instrument, and noticing why is this probe's real output.**

Repairing coverage means reading the 71 unclassified sentences, deciding what
class each is, and encoding those decisions as patterns — an LLM rater with
extra steps, the author's judgment baked into the regex. The prior-freedom that
was the instrument's entire reason for existing is exactly what the repair
destroys.

Rule 3 was written for the Wayland corpus of declared error names, where author
judgment inside the regex was never the thing under test. Here it is precisely
the thing under test. **Rule 3 does not generalise to an instrument whose
independence is the measurement.**

## Consequences, recorded so they are not rediscovered

1. **MLS is spent as a probe corpus.** TLS §4, iCalendar §3 and QUIC remain
   protected and unspent — they carry the locality claims of §6.6/§6.7 and must
   not be probed, only registered against.
2. **Do not register this instrument against a protected corpus.** It answers
   fewer than half the items and its dominant error mode is a known structural
   blind spot.
3. **Limitation 6 stands as written.** The shared-prior half of the confound is
   not cheaply attackable mechanically on prose.
4. The remaining recruit-free lane — found human judgments predating the
   author's framing — addresses **author mediation only**, not the shared prior.

## Files

`PLAN.md` (protocol, frozen first) · `mech1.py` (the classifier, frozen second)
· `pred.txt` (the one run's predictions) · this record.
