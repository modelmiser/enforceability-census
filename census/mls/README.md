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

## Pre-registered predictions (2026-08-13, committed and PUSHED before any rater exists)

Numbering namespace: **M1–M5** — deliberately distinct from the TLS study's
P1–P4 and from all codebook rule numbers (the pass-3 lesson: colliding
namespaces are how instruments drift).

**Instrument: FROZEN.** The rater pack is the TLS pass-4 instrument, verbatim
(git blob `a08febba22fd2cb117a9be41654a6209e0104e57`); the codebook is v3
(rules 1–14). No amendment of either occurs between this commit and the
completion of the rating passes. Any post-rating amendment would be a new
instrument version applied only in a future pass, never retroactively.

**Failure interpretation, pre-committed:** these predictions grade the
**author's structural model of MLS**, nothing else. The instrument was
validated on TLS and is frozen; the corpus is frozen (n = 127, commit
`634d68c`). Therefore: a failed prediction is a wrong guess about MLS,
recorded as such — it licenses NO re-rating, NO rule change, NO exclusion of
any valid-instrument rater, and NO discretion over what to quote. The quoted
MLS numbers are whatever the valid rating passes record — as a range if
raters disagree — regardless of how many predictions fail. (This block is
append-only; corrections, if ever needed, go in dated brackets.)

The predictions:

- **M1 — the crypto core is bigger than TLS's.** CV share strictly above
  TLS's 2.9%; band **4–10%** of 127 (5–13 items). Reason: MLS verifies
  secret/transcript-dependent artifacts per message and per join —
  signatures, confirmation_tag, membership_tag, PSK binders, parent-hash
  chains bound to signed leaves — where TLS concentrates them at handshake
  edges. (Public-arithmetic hash recomputation over public tree contents is
  DOMAIN by rule 2, not CV; the band accounts for that split.)
- **M2 — NEG stays in low single digits: 0–4 items.** MLS fixes the cipher
  suite at group creation; capability checks are mostly containment against
  established group state (cross-message consistency → rule 1/12 TYPESTATE
  territory or DOMAIN), not existence-of-a-compatible-choice.
- **M3 — type-eliminable share lands in 70–85%.** Directionally at or below
  TLS's 80–83%, with the shortfall going to the larger crypto core (M1),
  not to PROCESS.
- **M4 — REVOCABLE ≥ 2 items.** Credential expiry/revocation and
  KeyPackage lifetime duties put was-true-became-false predicates in scope
  (§5.3.2's normative surface is thin, so this is a weak-band prediction:
  ≥ 2, no upper bound claimed).
- **M5 — the discriminator-crispness law transfers to a new corpus** (the
  scientifically load-bearing one — first out-of-corpus test): between the
  author pass and the fresh blind rater, raw item agreement lands in
  **78–90%** (the TLS-measured floor band), and the crisp-discriminator
  classes (CV, META, THRESHOLD, REVOCABLE) differ by **at most 1 item
  each**, while the judgment boundaries (DOMAIN/TYPESTATE/PROCESS) carry
  the bulk of disagreement.
