# RFC 9420 (MLS) §5–§15 — two-rater census (2026-08-13)

**Headline: ≈57% of MLS's core normative surface is type-eliminable in
shape — two-rater agreement on the number is tight (A′ 56.7%, B′ 57.5%),
and it is ~25 points BELOW TLS's 80–83%.** The pre-registered model of MLS
(predictions M1–M5, commit `36890fd`, publicly timestamped before any rater
existed) was mostly wrong about the mix; per the pre-committed
interpretation those failures grade the author's structural model of MLS
and license nothing — the numbers below are what the raters recorded.

## Setup

- Corpus: n = 127 (`rfc9420_s5-15_musts.txt`, frozen at `634d68c`,
  2026-08-13T20:19Z public).
- Instrument: the TLS pass-4 rater pack, **verbatim** — git blob
  `a08febba22fd2cb117a9be41654a6209e0104e57`, extracted with
  `git cat-file` and hash-round-trip verified before serving. (Verbatim
  quirk, disclosed: the pack's title names RFC 8446 §4; its body
  instruction — "classify the corpus you are given" — is corpus-generic.
  Changing the title would have been a new instrument version.)
- Rater A′: the census author (LLM agent; context NOT controlled — see
  "Author-context events" below). Labels written to disk before B′
  returned.
- Rater B′: fresh blind LLM agent; received exactly two files (instrument +
  corpus), instructed to read nothing else. No access to the TLS census,
  the predictions, or A′'s labels.

## Scores

| measure | value |
|---|---|
| raw item agreement | 108/127 = **85.0%** |
| eliminable-vs-not agreement | 114/127 = **89.8%** |
| headline eliminable, A′ | 72/127 = **56.7%** |
| headline eliminable, B′ | 73/127 = **57.5%** |
| class tallies A′ | 39 DOMAIN, 33 TYPESTATE, 24 PROCESS, 11 U, 11 CV, 4 POLICY, 3 META, 1 THRESHOLD, 1 REVOCABLE |
| class tallies B′ | 42 DOMAIN, 31 TYPESTATE, 23 PROCESS, 10 CV, 5 U, 5 NEG, 4 POLICY, 3 THRESHOLD, 3 META, 1 REVOCABLE |

## Pre-registered prediction outcomes (bands from `README.md`, committed 36890fd)

| # | prediction (band) | outcome |
|---|---|---|
| M1 | CV share 4–10%, strictly > TLS's 2.9% | **PASS** — A′ 8.7% (11), B′ 7.9% (10) |
| M2 | NEG 0–4 items | **FAIL** — A′ 0, B′ **5** (the capability-compatibility cluster; see below) |
| M3 | eliminable 70–85%, shortfall not to PROCESS | **FAIL, decisively** — 56.7%/57.5%, 13.3 and 12.5 points below the floor, and the mass went exactly where the prediction said it wouldn't: PROCESS is 24/23 items (18.9%/18.1%), U 11/5 |
| M4 | REVOCABLE ≥ 2 | **FAIL** — 1 in both raters (the app-chosen lifetime cap classified THRESHOLD by both, leaving only the lifetime-range check) |
| M5 | THREE clauses, quoted in full: (a) raw agreement 78–90%; (b) CV/META/THRESHOLD/REVOCABLE differ by at most 1 item each; (c) "the judgment boundaries (DOMAIN/TYPESTATE/PROCESS) carry the bulk of disagreement" | **FAIL — 1 of 3 clauses passes.** (a) PASS: 85.0%, in band. (b) FAIL: META and REVOCABLE symmetric difference 0, CV 1, **THRESHOLD 2** (items 20, 126 — the AEAD-limits duties, sitting exactly on decision rule 3's structural-vs-chosen boundary). (c) FAIL under the TLS-era reading of the same sentence (both sides of the disagreement inside the family): only 8 of 19 disagreements are internal to DOMAIN/TYPESTATE/PROCESS (42%); the bulk sits on U/NEG (the capability cluster) plus THRESHOLD and CV. On the weaker at-least-one-side reading it is 16 of 19 — both counts reported; the pre-registration did not fix the reading, so the stricter one governs. |

Interpretation, as pre-committed: M2, M3, M4, and two of M5's three
clauses failing are wrong guesses about MLS, recorded as such. No
re-rating, no rule change, no exclusion, no quote discretion. *(An earlier
draft of this table quoted M5 without its third clause and graded only the
rest — caught at the pre-push cold review; the full quote and per-clause
grading above replace it.)*

## What the census found

1. **The type-eliminable share is not a security-protocol constant.** TLS
   §4: 80–83%. MLS §5–§15: ≈57%, with tight inter-rater agreement on the
   number (0.8 points apart). Same instrument, same recipe, same
   obligation granularity — so this difference is measured under matched
   method, unlike the cross-METHOD Wayland juxtaposition the TLS census
   had to disclaim. (Matched method, not matched population: TLS quotes a
   range over three valid raters; MLS has two, one of them the author.) Where the mass went: MLS states as MUSTs a large body
   of **procedure and hygiene** TLS §4 mostly does not — delete-key-material
   duties, GREASE/extensibility processing rules, key-schedule and
   tree-computation procedure (18.9%/18.1% PROCESS across the two raters,
   vs 7.4% in TLS rater A and 9.3% in TLS rater D).
2. **The discriminator-crispness law survived its first out-of-corpus
   test, with two measured edges (THRESHOLD here; NEG in finding 3).** META and REVOCABLE: identical items in
   both raters. CV: one item apart (see event E1 below — an extraction
   artifact, not a discriminator failure). THRESHOLD: two items apart, both
   AEAD-limit bounds — decision rule 3 distinguishes structural from chosen
   constants, and a limit *derived from the cipher suite's security
   analysis* is neither a framing-derived structural bound nor an
   operator-chosen line. The rule's dichotomy is incomplete for
   derived-but-not-chosen constants; recorded as a boundary observation,
   NOT patched (instrument frozen).
3. **A new judgment boundary, found by disagreement: capability-
   compatibility.** Five items (90, 111, 113, 114, 115) — duties of the
   form "member/joiner MUST support the group's extensions" — split
   three ways across the raters: U (actual support is unobservable —
   capability honesty; A′ on 90, 113, 114), TYPESTATE (advertised
   capabilities vs group state — cross-message consistency; A′ on 111,
   115), NEG (compatibility of two sets — B′ on all five). All three
   readings are rule-grounded (rules 11, 1, 12 respectively); the codebook
   has no tie-break for them. This is the same genus as the DOMAIN/PROCESS
   gap that produced rule 13 — a candidate rule 15 for a FUTURE instrument
   version, not this one. It also bears directly on NEG's graduation
   record: NEG graduated 2026-08-13 "with its small membership noted," and
   this census shows it carrying the single largest class variance between
   raters (0 vs 5) — the capability boundary is where a rule-12-only
   reading and a rule-11/rule-1 reading come apart.
4. **The DISAGREE bucket is 19 items, unresolved by design:**
   12, 20, 34, 41, 43, 44, 45, 59, 70, 71, 78, 90, 91, 104, 111, 113, 114,
   115, 126. Clusters: capability-compatibility (6, above);
   delete-key-material as PROCESS vs TYPESTATE (34, 43, 44); randomness
   duties as U vs the checkable length predicate as DOMAIN (41, 59);
   AEAD bounds (20, 126); proposal-list validity as TYPESTATE vs PROCESS
   (70, 78); and singletons 12, 45, 71, 91, 104.

## Author-context events (rule: context not controlled, so record it)

- **E1 — item 12.** The corpus sentence is "For messages sent by members,
  it MUST be set to the following value:" — "it" has no antecedent within
  the sentence. A′ consulted the RFC source (the antecedent is
  `membership_tag`, a MAC → CV); B′, holding only the corpus, read a
  field-value duty (DOMAIN). A′'s label is better-informed and
  **instrument-deviant** — the pack says classify on the sentence's own
  text. This is the sentence-granularity extraction artifact made visible:
  the one CV variance between raters is attributable to it, and it is
  counted against instrument transfer, not excused.
- **E2 — the corpus itself.** Item 103 is a pseudocode fragment (a code
  block's comment + guard) swept in by the recipe; both raters classified
  its predicate (array-length parity → DOMAIN) without incident. Recorded
  as recipe fidelity, not cleaned up.

## Raw labels (archived verbatim; `?` = rater-flagged torn)

Rater A′ (author):

```
1:TYPESTATE 2:DOMAIN 3:PROCESS 4:POLICY 5:U 6:DOMAIN 7:CV 8:DOMAIN 9:DOMAIN 10:DOMAIN
11:CV 12:CV 13:CV 14:DOMAIN 15:DOMAIN 16:PROCESS 17:U 18:DOMAIN 19:CV 20:DOMAIN
21:DOMAIN 22:TYPESTATE 23:DOMAIN 24:DOMAIN 25:U 26:DOMAIN 27:PROCESS 28:THRESHOLD 29:CV 30:TYPESTATE
31:REVOCABLE 32:DOMAIN 33:PROCESS 34:PROCESS 35:PROCESS 36:TYPESTATE 37:DOMAIN 38:DOMAIN 39:TYPESTATE? 40:TYPESTATE
41:U 42:TYPESTATE 43:PROCESS 44:PROCESS 45:TYPESTATE? 46:DOMAIN 47:CV 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:PROCESS 52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:DOMAIN 56:TYPESTATE 57:TYPESTATE 58:DOMAIN 59:U 60:TYPESTATE
61:DOMAIN 62:TYPESTATE 63:TYPESTATE 64:DOMAIN 65:CV? 66:U 67:DOMAIN 68:DOMAIN 69:META 70:TYPESTATE
71:TYPESTATE 72:TYPESTATE 73:POLICY 74:PROCESS 75:PROCESS 76:META 77:TYPESTATE 78:TYPESTATE 79:DOMAIN 80:META
81:DOMAIN 82:TYPESTATE 83:TYPESTATE 84:TYPESTATE 85:TYPESTATE 86:DOMAIN 87:TYPESTATE 88:TYPESTATE 89:PROCESS 90:U?
91:U 92:CV 93:PROCESS 94:PROCESS 95:DOMAIN 96:DOMAIN 97:CV 98:CV 99:PROCESS 100:DOMAIN
101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN 105:TYPESTATE 106:PROCESS 107:U 108:PROCESS 109:PROCESS 110:DOMAIN
111:TYPESTATE 112:TYPESTATE 113:U? 114:U? 115:TYPESTATE 116:DOMAIN 117:DOMAIN 118:PROCESS 119:PROCESS 120:PROCESS
121:PROCESS 122:POLICY 123:POLICY 124:PROCESS 125:TYPESTATE 126:TYPESTATE? 127:TYPESTATE
```

Rater B′ (blind):

```
1:TYPESTATE 2:DOMAIN 3:PROCESS 4:POLICY 5:U 6:DOMAIN 7:CV 8:DOMAIN 9:DOMAIN 10:DOMAIN
11:CV 12:DOMAIN 13:CV 14:DOMAIN 15:DOMAIN 16:PROCESS 17:U? 18:DOMAIN 19:CV 20:THRESHOLD
21:DOMAIN 22:TYPESTATE 23:DOMAIN 24:DOMAIN 25:U 26:DOMAIN 27:PROCESS 28:THRESHOLD 29:CV 30:TYPESTATE
31:REVOCABLE 32:DOMAIN 33:PROCESS 34:TYPESTATE 35:PROCESS 36:TYPESTATE 37:DOMAIN 38:DOMAIN 39:TYPESTATE 40:TYPESTATE
41:DOMAIN 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:DOMAIN 46:DOMAIN 47:CV 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:PROCESS 52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:DOMAIN 56:TYPESTATE 57:TYPESTATE 58:DOMAIN 59:DOMAIN 60:TYPESTATE
61:DOMAIN 62:TYPESTATE 63:TYPESTATE 64:DOMAIN 65:CV 66:U 67:DOMAIN 68:DOMAIN 69:META 70:PROCESS
71:DOMAIN? 72:TYPESTATE 73:POLICY 74:PROCESS 75:PROCESS 76:META 77:TYPESTATE 78:PROCESS 79:DOMAIN 80:META
81:DOMAIN 82:TYPESTATE 83:TYPESTATE 84:TYPESTATE 85:TYPESTATE 86:DOMAIN 87:TYPESTATE 88:TYPESTATE 89:PROCESS 90:NEG
91:TYPESTATE 92:CV 93:PROCESS 94:PROCESS 95:DOMAIN 96:DOMAIN 97:CV 98:CV 99:PROCESS 100:DOMAIN
101:DOMAIN 102:DOMAIN 103:DOMAIN 104:TYPESTATE 105:TYPESTATE 106:PROCESS 107:U 108:PROCESS 109:PROCESS 110:DOMAIN
111:NEG 112:TYPESTATE 113:NEG 114:NEG 115:NEG 116:DOMAIN 117:DOMAIN 118:PROCESS 119:PROCESS 120:PROCESS
121:PROCESS 122:POLICY 123:POLICY 124:PROCESS 125:TYPESTATE 126:THRESHOLD 127:TYPESTATE
```
