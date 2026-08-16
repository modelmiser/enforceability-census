# First rating pass under instrument v5 — QUIC (pre-pass protocol; no rater has run)

2026-08-15 · **Status: registered BEFORE any rater; every graded clause
below is fixed at this commit.** Append-only after push; corrections,
if ever needed, are appended in dated brackets.

## Why this pass, and what it can actually test

The v5 amendment (`codebook/classes.md`, rules 20–24, predictions
Z1–Z7) disclosed at cut time that Z1–Z5 are comprehension checks BY
CONSTRUCTION — the rule bodies adjudicate their own items. QUIC
carries the amendment's largest gradeable mass: Z1 (item 63), the QUIC
conjunct of Z4 (item 191), Z6 (items 192–193), Z7 (the 49-item
stability set), and rule 23's outside-set clauses. This registration
runs rule 24's mechanical audits and reports their verdicts below;
the honest headline of those audits, stated before any rater: **after
downgrades, this pass's only unsteered graded instruments are Z7 (44
of its 49 items) and rule 23's two clauses.** Everything else measures
whether an in-pack adjudication transmits.

## Instrument — the v5 pack

- **Pack:** `codebook/rater-pack-v5.md`, git blob
  `694e3a9efab29252a815b00150a8c3ecf83a90b6`, committed with this
  registration. Construction: the v4 pack (blob `4891605…`,
  byte-identical — the same bytes served in `census/v4-completion/`) +
  one appended section headed verbatim
  `## CODEBOOK v5 RULES (2026-08-15) — apply together with everything
  above`, holding the v5 precedence pipeline and rules 20–22 verbatim
  from `codebook/classes.md`, with exactly two disclosed elisions
  (the committed file, not this recipe sketch, is the byte authority):
  1. rule 20's clause naming prediction Z3 ("…and Z3, the prediction
     that rests on it, is weighted accordingly" → the sentence ends at
     "contested bridge."), and
  2. rule 21's dangling cross-reference "— see the partial-ruling
     disclosure above" (the referenced section contains archived label
     information and is not served; the residue sentence itself — the
     duty "is NOT decided by this rule" — is served intact).
  Rules 23 and 24 are not served (they are measurement-protocol rules;
  the served pipeline sentence saying they "classify nothing" explains
  their absence to the rater). No other text differs from the
  codebook. Hash round-trip is verified at serve time.
- **Corpus:** `census/quic/rfc9000_s2-19_musts.txt`, byte-identical,
  n = 281.

## Rule-24 audit results (run at registration, archived here)

**Settlement sweep** (pack vs corpus, case/punctuation-normalized
n-grams, the `census/quic-replication/` procedure): 6-gram **zero
hits**. 5-gram: one real cluster — items 11, 19, and 261 share "frames
that do not increase" with rule 21's undecided-residue clause, which
quotes that duty form as its example of what the rule does NOT decide;
all three (and 272, a 4-gram hit on the same clause) are outside-set
items, and the steer's direction is "undecided," not any label — their
outcomes are owed as observations below. 4-gram residue, the full hit
set {54, 69, 77, 116, 211, 225, 233, 240}: "a client must not" ×6
(items 54, 77, 116, 211, 225, 240 — adjudicated non-settling here,
fresh, by the same phrase-frequency reasoning the replication
registration applied to its one hit), item 233's "must not be sent"
(that previously adjudicated hit itself), and item 69's "send a packet
on," inherited from the v4 pack's rule-19 example and present in every
pass since `d3d4c2d`.

**Downgrade triggers** (rule 24, mechanical): the identifier **ICMP**
occurs in rule 21's body and is a distinctive identifier of items 191,
192, and 193 → trigger (b) fires: **the Z4-QUIC conjunct and Z6 are
downgraded to comprehension checks at this registration**, joining the
amendment's cut-time downgrades. Within Z7's set, five items are
steered: 126, 127, 160 (the identifier **CONNECTION_CLOSE** occurs in
rule 20's falsification clause — trigger (b)) and 130, 147 (rule 21's
"a malformed or too-small packet" and rule 22's
"no-coalescing-across-connection-IDs rule" are paraphrases of their
content — trigger (c)). **Z7 is graded on its registered form** (the
codebook text governs; no reword), and the report additionally quotes
the steered-excluded count (DOMAIN-held items among the 44 unsteered)
beside it, reported, not graded. Item 63's duty is paraphrased in rule
20's body ("a running total against an expandable limit") — trigger
(c), consistent with Z1's cut-time downgrade.

**Identifier scan over the full corpus (not just predicted items):**
the pack's distinctive-identifier hits over all 281 items are exactly
two identifiers — ICMP and CONNECTION_CLOSE ("0-RTT" in the served
pipeline was already in the v4 blob the anchor raters saw, so it is
anchor-neutral). CONNECTION_CLOSE occurs in EIGHT corpus items: the
three S49 members named above and five OUTSIDE-SET items {125, 128,
144, 152, 190} (anchor labels: 125/144/152 both-TYPESTATE; 128
U/TYPESTATE; 190 PROCESS/TYPESTATE). The pack's sole occurrence sits
in rule 20's TYPESTATE-branch falsification clause, so its direction
on these five is mixed — anchor-ward (pass-ward for clause (a)) where
the anchors read TYPESTATE, anchor-away on first-branch readings —
and it is named here so the closing section cannot overclaim. Steer
directions within Z7's set, stated: 130 and 147 are steered toward
DOMAIN (pass-ward for Z7 as graded); 126/127/160 sit under a
TYPESTATE-branch mention (fail-ward or ambiguous for Z7).

## Raters — models pre-registered (the names govern; a differing serving model is a protocol event)

- **Rater Aq5:** fresh same-family instance, `claude-fable-5`, single
  input file (pack + corpus), blind to predictions, tallies, and every
  archived label.
- **Rater Xq5:** foreign `cursor-grok-4.6-high-fast` via cursor-cli,
  chunk partition pinned as in every QUIC pass: 1–51 / 52–102 /
  103–153 / 154–204 / 205–255 / 256–281.
- No author rater. Malformed-label handling inherited from
  `census/ical/` (one format-only retry; residual malformed/missing
  scored U as protocol events; event-U counts as disagreement in
  agreement figures and non-eliminable in shares); torn-flags per
  `census/v4-ical/` (trailing `?` stripped, base label governs).
  **Noise direction, stated in advance:** an event-U is
  failure-ward for every graded clause of this pass (it can never
  equal a predicted label, match an anchor, or count as DOMAIN in Z7),
  so no exclusion protocol is needed to prevent a manufactured pass.
  Distinguish it from a well-formed rater-emitted U, which is a LABEL,
  not an event: a label-U matches an anchor U — the registered
  baselines count it so, and both anchor-source passes record zero
  protocol events, so every archived U is a label-U. Applying "U never
  matches" to label-Us would silently deflate clause (a) below its own
  measured baseline convention and is out of compliance.

## Rule 23 instantiated (anchors, sets, and integers — all fixed here)

- **Anchor pair:** Av4/Xv4, the QUIC raters of
  `census/v4-completion/` — the most recent archived full pair under
  v4, the instrument version nearest v5 (rule 23's default; no
  departure). Agreement: 236/281 full-corpus (archived in the
  v4-completion report); **192/228 on the outside set** (recomputed
  here from that report's archived label blocks) — clause (a) is
  computed on the outside set for both sides (the apples-to-apples
  reading, fixed here; the full-corpus-rate reading lands on the same
  integer, ⌈236/281 × 228⌉ = 192).
- **Prediction-named items for this corpus:** {63, 191, 192, 193} ∪
  S49, where S49 is Z7's set — the 49 items labeled DOMAIN by both
  `census/quic-replication/` raters (recomputable from that report's
  archived blocks). The two sets are disjoint. **Outside set = the
  remaining 228 items.**
- **Clause (a):** per rater, outside-set match count vs the anchors
  (match = equals Av4's or Xv4's label) **≥ 192 of 228** (84.2%).
  Failability, measured: the replication's own rater Aq scores 188/228
  against these anchors and would fail this floor; Xq scores exactly
  192/228.
- **Clause (b):** per rater, outside-set items departing from BOTH
  anchors **≤ 36** — the smaller of the two measured cross-pass
  departure counts against these anchors (Aq 40, Xq 36; both crossed
  an instrument version, as this pass also does, v5 extending v4).
  Registered here, never computed at grading.
- **Clause (c):** the report publishes, per rater, the full
  both-anchor departure list and per-class deltas with explicit zeros;
  plus both owed metrics — match-vs-anchors AND role-matched
  agreement (Aq5 vs Av4; Xq5 vs Xv4).

## Graded clauses (per rater, integers restated)

| clause | pass condition per rater | status after audit |
|---|---|---|
| Z1 | item 63 = THRESHOLD | comprehension check (cut-time + trigger (c)) |
| Z4-QUIC conjunct | item 191 = PROCESS | comprehension check (trigger (b): ICMP) — Z4 overall stays open until TLS's first v5 pass |
| Z6 | items 192 AND 193 = PROCESS | comprehension check (trigger (b): ICMP) |
| Z7 | ≥ 42 of S49 = DOMAIN | **graded, discriminating** (44/49 items unsteered; steered-excluded count reported beside) |
| 23(a) | outside-set anchor-match ≥ 192/228 | **graded, discriminating** |
| 23(b) | outside-set both-anchor departures ≤ 36 | **graded, discriminating** |

Downgraded clauses are still graded and reported — a failed
comprehension check is evidence the adjudication does not transmit
even when stated in the rater's own instrument, the strongest possible
transmission failure.

## Owed observations (explicit outcomes, including zeros)

1. **Item 105** (rule 20's disclosed eliminable-ward recapture
   candidate): both raters' labels, quoted against the v4 PROCESS
   consensus. No prediction; rule 23's clauses bound it.
2. **Items 11, 19, 261, 272** (rule 21's explicitly undecided residue,
   whose duty form the pack quotes): both raters' labels. No
   prediction either way; the v4 consensus (PROCESS) and the v3
   readings are both licensed.
3. A label table over {11, 19, 63, 105, 191, 192, 193, 261, 272}
   across Av4, Xv4, Aq5, Xq5.
4. Eliminable shares per rater, quoted only as the v5 series (v3
   headline ≈67–69% and the v4-series figures stand, never
   substituted). Named-item accounting predicts ZERO
   eliminable-line crossings against these anchors (63: THRESHOLD vs
   anchors' THRESHOLD/PROCESS — no crossing; 191: PROCESS = both
   anchors; 192/193: PROCESS = both anchors); rule-level reach (rule
   20 on reaction sentences, eliminable-ward) is bounded by clauses
   (a)/(b).

## Ring-fence and failure interpretation

The QUIC census headline (≈67–69%, v3) and the v4-series figures
stand and are never substituted; this pass's numbers are quoted only
as "v5 instrument series." Failed clauses grade the v5 rule texts and
the author's model of their reach; they license NO re-rating, NO
rewording within v5, NO retroactive relabeling of any archived pass,
and NO exclusion of any valid-instrument rater. Deviations are
recorded with reasons, never argued into compliance. Direction
disclosure: the pass's instrument-friendly outcome is high anchor
agreement with Z7 holding; the audits above name every steer the
mechanical triggers surface — including the five outside-set
CONNECTION_CLOSE items and the pass-ward direction of the 130/147
steers — and clauses (a)/(b) plus Z7's 44 unsteered items are where
the pass can fail against un-steered content.
