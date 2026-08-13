# RFC 8446 §4 normative-obligation census (the 3-hour version)

2026-08-12 · Companion to `tls13-alert-census.md` (the 30-minute alert probe). Corpus =
every MUST/MUST NOT/SHALL sentence in RFC 8446 §4 (Handshake Protocol), n=204,
hand-classified on predicate shape from the sentence's own text (mm-residue rule 8
[= rule 8 of `codebook/classes.md` in this repository]).
**Status: TWO-rater measurement (2026-08-12): blind second rater (fresh agent, labels
withheld, same codebook) agreed 184/204 = 90.2% raw across the 10-class scheme, and
196/204 = 96.1% on the headline eliminable-vs-not distinction; the eliminable share is
81.9% (rater A) vs 79.9% (rater B).** Disagreements are NOT resolved — see the
Inter-rater section. Quote the headline as "80–82%". *[Superseded 2026-08-13: after
passes 3–4 (see close-out at the end of this file), quote the headline as **80–83%**
— the three-valid-rater range 79.9–82.8%. This status line is preserved as the
two-rater-era record.]*

## Method

- Extraction: §4 = RFC lines 1317–4282; paragraphs joined, sentences split, filtered on
  `\bMUST\b|\bSHALL\b` → 204 items (`rfc8446_s4_musts.txt`, regenerable by script
  *[correction 2026-08-13: by the recipe in this bullet — no extraction script ships]*).
- Classes: the four from `classes.md` (0 DOMAIN, 1 THRESHOLD, 2 REVOCABLE, 3 TYPESTATE)
  plus the two provisional classes the alert probe forced (CRYPTO-VERIFY, NEGOTIATION),
  plus PROCESS (algorithm/behavior rules that are not boundary predicates), POLICY,
  UNCLASSIFIED-unverifiable, META. Provisional classes are NOT yet in `classes.md` —
  they graduate only after the follow-ups below converge.
- Decision rules fixed during the pass (the judgment calls, disclosed):
  1. **Cross-MESSAGE consistency = TYPESTATE; intra-message cross-field = DOMAIN.**
     "ServerHello suite == HelloRetryRequest suite" is 3; "key_share ⊆ supported_groups
     in the same ClientHello" is 0.
  2. **CRYPTO-VERIFY requires secret/transcript material.** MAC, signature, PSK-binder
     verification = CV. DH point validation (1 < Y < p-1, point-on-curve) is **DOMAIN**:
     decidable public arithmetic on one value, no secret involved — some crypto checks
     are type-eliminable and the secret is the discriminator.
  3. **Structural bound = DOMAIN; picked policy line = THRESHOLD.** record_overflow's
     2^14+256 derives from framing (a presentation-language type); the 7-day ticket cap
     (604800s) is a chosen risk line = 1.
  4. Sender-side and receiver-side duals of one obligation both counted (they are
     separate normative sentences; the corpus measures the spec's normative surface,
     not deduplicated semantics).

## Tallies (n=204)

| class | n | % | items |
|---|---|---|---|
| TYPESTATE (3) | 94 | 46.1% | 1,2,4,5,7,8,9,10,24,25,35,37,39,40,41,42,43,44,45,46,47,61,62,63,67,82,83,87,89,94,95,96,97,98,99,100,106,108,109,111,114,115,116,118,121,127,128,129,130,135,137,138,139,142,143,144,145,146,147,148,149,152,156,159,160,161,162,163,165,166,167,170,171,172,173,174,175,181,182,183,184,185,186,192,193,194,195,196,198,199,200,202,203,204 |
| DOMAIN (0) | 73 | 35.8% | 11,12,13,14,15,16,18,19,20,21,26,28,30,31,32,33,34,36,48,49,50,51,55,56,57,58,64,65,66,68,69,70,71,72,73,74,77,78,81,84,85,86,88,90,92,93,101,102,103,104,105,107,110,122,123,131,132,136,140,141,150,151,153,154,155,157,158,168,169,176,177,191,201 |
| PROCESS | 15 | 7.4% | 17,29,38,52,53,54,59,60,76,113,119,134,164,187,197 |
| CRYPTO-VERIFY (prov.) | 6 | 2.9% | 120,125,126,178,179,180 |
| UNCLASSIFIED-unverifiable | 6 | 2.9% | 22,23,79,80,91,190 (randomness/independence/capability-honesty — no per-instance predicate exists) |
| NEGOTIATION (prov.) | 3 | 1.5% | 3,6,124 |
| REVOCABLE (2) | 2 | 1.0% | 112 (ticket-age freshness; tolerance is threshold-shaped), 133 (ticket expiry) |
| THRESHOLD (1) | 2 | 1.0% | 188,189 (7-day cap pair) |
| POLICY | 2 | 1.0% | 27,75 |
| META | 1 | 0.5% | 117 (obligation on future spec authors) |

**Headline: 167/204 = 81.9% of §4's normative surface is type-eliminable in shape**
(typestate + domain) — strikingly close to Wayland's 87.6%, in a *cryptographic*
protocol. The secret-dependent core (CRYPTO-VERIFY) is 2.9% of stated obligations;
with REVOCABLE and THRESHOLD added, everything types cannot even in principle express
is ~5%. The handshake is overwhelmingly state-machine and format discipline — which is
a quantified account of why the state-machine attack family (SMACK/FREAK) was so
fruitful: the attack surface class is ~16× (94/6 = 15.7) the size of the
cryptographic one by obligation count.

## The granularity prediction, confirmed

The alert probe predicted the alert vocabulary censors typestate (all of A.1/A.2
compresses into `unexpected_message`). Measured: alert set 20% typestate → MUST corpus
46.1%. The quotient hides a factor of ~2.3. Corollary stands: **never compare protocol
censuses at different error-code granularities; census the normative statements, not
the alert alphabet.** (A.1/A.2 state-diagram arrows were NOT separately counted — their
ordering content already appears as §4 MUST sentences; counting both would double-count.)

## Deterministic self-audit (rule 4)

Items ranked by md5 of sentence text; first 12 re-checked: [4,184,25,175,41,30,178,69,
110,76,127,98]. **11/12 held; [41] reclassified P→3** (required-response transition
duty, same rule as [192]/[202] — an internal-consistency defect of exactly the kind
the audit exists to catch). Tallies above are post-audit. This is a SELF-audit (same
rater re-reading); a blind second rater is the real control and is still owed.

## Inter-rater check (blind second pass, 2026-08-12)

A fresh agent classified all 204 with the same codebook, labels withheld. Raw
agreement 184/204 (90.2%); eliminable-vs-not agreement 196/204 (96.1%).
**DISAGREE bucket (20 items), unresolved by design:**
- **14 items on ONE boundary — guard-vs-predicate:** state-conditioned constant
  fields ([30,31,32,56,57] A:0 B:3; [67,156,159,165,184] A:3 B:0; plus [5,54,65,123]).
  The condition is history, the checked predicate is a constant; the codebook lacks a
  tie-break for which wins. Both readings are eliminable, so this mass is INTERIOR to
  the headline family — that is why headline agreement is 6 points above raw.
- [51,55,157] A:0 B:U — presence duties whose content ties to unverifiable local
  intent (capability-honesty shading).
- [27] A:POL B:0; [138] A:3 B:U (uniqueness-over-history vs generation duty);
  [189] A:1 B:2 (the 7-day cap: policy line vs expiry — flagged as ambiguous by
  rater A at classification time).
Codebook repair owed before any re-run: a guard-vs-predicate tie-break rule and a
sharper U-boundary for capability-honesty. Do NOT silently adjudicate these 20 and
re-quote a single number; the honest headline is the range 80–82%. *[Superseded
2026-08-13: 80–83% after pass 4 — see close-out.]*

*[Provenance note, 2026-08-13: rater B's full 204-item label map was never archived —
only the 16 recorded labels above plus the fact of agreement on the other 184. B's
79.9% and the 96.1% figure are arithmetically consistent with the recorded labels but
not item-recomputable for [5,54,65,123]. A provenance defect, recorded rather than
repaired; raters C and D have full archived maps.]*

## Prior-art sweep (3-hour tier)

FSM-*extraction* from RFCs is a mature genre — RFCNLP/attack-synthesis (NDSS'22,
arXiv:2202.09470), PROSPER (HotNets'23), FlowFSM, LLM-ensemble extraction for 3GPP
(arXiv:2510.14348) — and RFC 2119 modality-tagging exists in requirements engineering.
None of these measure an **enforceability-class mix** of a protocol's obligation set;
the nearest neighbors classify by modality (MUST/SHOULD/MAY) or extract transitions
for fuzzing/attack synthesis. Same null as the PromQL sweep. Positioning duty carried
over from `classes.md`: Gao/Bird/Barr ICSE'17, ODC, Seven Pernicious Kingdoms,
Dwyer'99.

## Caveats (read before quoting)

1. **Two raters, one codebook, disagreements unresolved.** The blind pass is done
   (90.2%/96.1%, see Inter-rater section); quote the headline as a RANGE (80–82%),
   never a point, until the codebook repair + re-run converge. *[Superseded
   2026-08-13: the re-runs did NOT converge — that is the recorded verdict — and the
   quoting instruction is now the three-valid-rater range **80–83%**; see close-out.]*
2. **Extraction is sentence-regex.** Compound sentences carrying several obligations
   count once; umbrella sentences ("MUST behave in one of three ways") count once;
   SHOULD-level text is absent by design. n=204 is the sentence count, not the
   obligation count.
3. **Censoring (rule 7):** §4 prose can barely express THRESHOLD (2 items — the record
   layer and §8 hold more); a MUST-sentence corpus cannot express what the spec never
   states (undeclared obligations — the median-API problem — are invisible here).
4. **Wayland falsifiability check PENDING:** the provisional classes predict CV=0 and
   NEG≈0 in the Wayland corpus (no secret material in-protocol; registry version-bind
   is the one NEG candidate). The corpus JSON is not in this directory — regenerate
   from wayland.xml + wayland-protocols and grep before asserting. Do not cite the
   prediction as a result. *[Superseded 2026-08-13: check RUN and CONFIRMED, 0/216 +
   0/216 — `../wayland/cv-neg-falsifiability.md`.]*
5. `classes.md` deliberately NOT yet updated — provisional classes graduate after
   follow-ups 1 and 4 converge. *[Superseded 2026-08-13: both classes graduated —
   see `codebook/classes.md` "CLASS GRADUATION" for the gates actually applied.]*

## Follow-ups

- [x] Blind second-rater pass over the same 204 — DONE 2026-08-12 (90.2% raw,
      96.1% headline; 20-item DISAGREE bucket recorded above, unresolved).
- [x] Codebook repair (guard-vs-predicate tie-break; capability-honesty U-boundary),
      then third blind pass under the repaired codebook. — DONE 2026-08-13: codebook
      v2 (rules 10–11) + pass 3 (INVALID — instrument paraphrase defect, see
      `rfc8446-s4-pass3.md`), codebook v3 (rules 12–14) + pass 4 under the verbatim
      rater pack (`rfc8446-s4-pass4.md`).
- [x] Wayland CV/NEG falsifiability check (caveat 4). — DONE 2026-08-13: CONFIRMED,
      CV=0/216, NEG=0/216 on a regenerated superset corpus; the one predicted NEG
      candidate is not a declared error at all (`../../census/wayland/cv-neg-falsifiability.md`).
- [x] Graduate CRYPTO-VERIFY + NEGOTIATION into `classes.md` with the secret-material
      discriminator, if they survive. — DONE 2026-08-13: both graduated (classes.md
      "CLASS GRADUATION"); CV was item-for-item identical across every rater.
- [ ] Optional: same census on a second security RFC (Noise spec or RFC 9420 MLS) —
      one protocol is one data point.

## Passes 3–4 close-out (2026-08-13) — headline updated to 80–83%

The repair-and-re-rate loop ran twice and STOPPED by pre-registered criterion
(full accounts: `rfc8446-s4-pass3.md`, `rfc8446-s4-pass4.md`). Pass 3 was
invalidated by an instrument transcription defect (a paraphrased NEG
definition annexed rule-1 territory) and is archived, not counted. Pass 4,
under the byte-identical rater pack, healed the NEG boundary (P1 PASS) but
failed the other three pre-registered predictions — the pre-committed
interpretation being that **the codebook is not yet transmissible by text
alone at item granularity**, and further rule-patching would be instrument
overfitting.

What this file's headline becomes:
- **Type-eliminable share: quote as 80–83%** — the range of the three valid
  raters, endpoints 79.9% (B) to 82.8% (D), with A at 81.9%. **Why this is
  not the "new headline" the v3 pre-registration forbade:** the
  pre-registration barred treating a failed pass as *convergence* — minting
  a converged point estimate from it. It did not, and could not, bar
  reporting the honest descriptive range over all valid raters; excluding D
  (a valid-instrument rater) to preserve the old range would be
  cherry-picking in the other direction. The asymmetry with rater C is
  principled and stated: C's instrument was defective (a mis-transcribed
  class definition moved a boundary), so C's *tallies* measure the
  paraphrase, not the codebook; D's instrument was the codebook verbatim.
  The transmissibility verdict (the pre-registered interpretation of the
  prediction failures) stands unchanged alongside the widened range.
- **Crypto core: exactly 6/204 (2.9%), the same six items for every rater
  in all four passes** — CV and META are the zero-variance classes.
  THRESHOLD and REVOCABLE are identical across A/C/D with exactly one
  recorded exception: rater B read item 189 (the 7-day cap) as REVOCABLE
  where A/C/D read THRESHOLD — an ambiguity rater A had flagged at
  classification time. The residual disagreement mass is interior to the
  eliminable family (DOMAIN/TYPESTATE/PROCESS boundaries).
- 15 items have C = D ≠ A (two fresh raters agreeing on the same alternative
  label): the measured trace of authorial context in rater A's labels. Left
  unadjudicated by design.
