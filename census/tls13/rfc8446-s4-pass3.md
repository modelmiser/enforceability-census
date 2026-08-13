# RFC 8446 §4 — third rating pass (2026-08-13): INVALID as a codebook-v2 test; diagnostic as an instrument test

**Verdict up front: the headline remains the two-rater range 80–82%. Pass 3
does not update it.** *[As of this report; pass 4 — a valid-instrument pass,
see `rfc8446-s4-pass4.md` — later widened the quoted range to 80–83%.]* The pass failed its own pre-registered criterion
(headline 69.6%, outside the band; agreement on the 184 previously-agreed
items degraded 90.2% → 82.1%), and the failure localizes to an **instrument
transcription error**, not to the codebook-v2 repair rules — but per the
pre-registration, a pass that lands outside the band is evidence about the
pass, never a new number.

## What ran

Fresh blind rater (labels, tallies, and predictions withheld), all 204 items,
codebook v2 (rules 1–4 + amendments 10–11) — **as paraphrased into the rater
prompt**, which is where the defect entered. Raw labels archived; scored
against rater A (full map) and rater B (184 shared + 16 recorded DISAGREE
labels).

## Scores

| measure | value | passes 1–2 baseline |
|---|---|---|
| C vs A raw | 162/204 = 79.4% | A vs B: 90.2% |
| C vs A eliminable-vs-not | 173/204 = 84.8% | A vs B: 96.1% |
| C on the 184 previously-agreed | 151/184 = 82.1% | (prediction: no degradation) |
| C headline eliminable | 142/204 = **69.6%** | band 80–82% |

## Diagnosis: the NEG paraphrase collided with rule 1

The canonical NEGOTIATION definition (alert probe, 2026-08-12) is **narrow**:
*"emptiness/compatibility of a two-party set intersection. No history, no
clock, no single value, no number."* The §4 census applied it that way — 3
items, all abort-when-no-overlap duties.

The pass-3 rater prompt paraphrased NEG as *"the selected value is in the
intersection/compatible set of what both parties support/offered
(mutual-agreement selection duties...)"*. That broad reading annexes decision
rule 1's territory: a duty that a **selected value be consistent with an
earlier offer** is cross-message consistency = TYPESTATE. Rater C applied the
paraphrase faithfully: **23 NEG labels vs the census's 3, of which 16 sit on
items rater A classified as selection-consistency TYPESTATE** (items 4, 5, 25,
42, 61, 97, 98, 106, 127, 128, 160, 162, 163, 166, 173, 174). Since NEG is
outside the eliminable family, this single boundary migration mechanically
produced most of the headline drop. This is not rater error; the rater
followed the instrument it was handed.

Second, smaller axis: **DOMAIN → PROCESS drift** (7 items outside the
original DISAGREE bucket: 14, 18, 64, 84, 122, 141, 191 — encoding/
serialization duties read as procedure rather than wire-value predicates;
counting the two inside the bucket, 55 and 157, the drift is 9 items total).
The codebook has never had a DOMAIN/PROCESS boundary rule; PROCESS and
POLICY entered the §4 census with one-clause definitions.

## What pass 3 does show

- **On the 20 repair-target DISAGREE items, C landed within the previously
  observed A/B envelope on 14/20** *[correction 2026-08-13: 15 of the 17
  determinable items — B's labels for 5, 54, 123 were never archived, so
  envelope membership is indeterminable there; the out-of-envelope items are
  55 and 157]*, and the guard-vs-predicate cluster
  resolved with a clear rule-10 pattern (constant-whenever-applicable fields →
  DOMAIN: 30, 31, 32, 56, 57, 67, 156, 184; history-varying → TYPESTATE: 159,
  165). The repaired boundaries behaved; the un-repaired ones leaked.
- **A provisional class without a numbered discriminator is not yet a
  class.** CRYPTO-VERIFY had one (secret material) and held at exactly 6 items
  across all three raters. NEGOTIATION's narrow definition lived in prose in a
  different file from the decision rules, survived two raters by shared
  context rather than by text, and dissolved on first contact with a rater who
  had only the text. The class boundary must be a rule (→ codebook rule 12).
- **The instrument must be the codebook itself, not a paraphrase of it.**
  Transcription is where this defect entered; the fix is a versioned verbatim
  rater pack (→ `codebook/rater-pack.md`), so that what a rater reads is
  byte-identical to what the codebook says.

## Disposition

Per the census's own discipline (do NOT silently adjudicate and requote): C's
labels are archived unmodified; no post-hoc reclassification of C's NEG items
is performed or quoted. Next: append codebook rules 12–13 + the instrument
rule, build the verbatim rater pack, pre-register pass-4 predictions, run
pass 4 with a fresh rater. Pass 4 is the same protocol step done with a valid
instrument, not an additional adjudication round.

## Raw labels (rater C, archived verbatim; `?` = rater-flagged torn)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:NEG 5:NEG 6:NEG 7:TYPESTATE 8:TYPESTATE
9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN 14:PROCESS 15:DOMAIN
16:DOMAIN 17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:DOMAIN 23:U
24:TYPESTATE 25:NEG 26:DOMAIN 27:DOMAIN 28:DOMAIN 29:PROCESS 30:DOMAIN
31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN 35:TYPESTATE 36:DOMAIN 37:TYPESTATE
38:PROCESS 39:TYPESTATE 40:TYPESTATE 41:TYPESTATE 42:NEG 43:TYPESTATE
44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:DOMAIN 49:DOMAIN
50:DOMAIN 51:DOMAIN 52:NEG 53:PROCESS 54:NEG 55:PROCESS 56:DOMAIN 57:DOMAIN
58:DOMAIN 59:PROCESS 60:PROCESS 61:NEG 62:TYPESTATE 63:TYPESTATE 64:PROCESS
65:DOMAIN 66:U? 67:DOMAIN 68:DOMAIN 69:DOMAIN 70:DOMAIN 71:DOMAIN 72:DOMAIN
73:DOMAIN 74:DOMAIN 75:U? 76:PROCESS 77:DOMAIN 78:DOMAIN 79:NEG? 80:NEG?
81:DOMAIN 82:TYPESTATE 83:TYPESTATE 84:PROCESS 85:DOMAIN 86:DOMAIN
87:TYPESTATE 88:DOMAIN 89:U 90:DOMAIN 91:U 92:DOMAIN 93:DOMAIN 94:TYPESTATE
95:TYPESTATE 96:TYPESTATE 97:NEG 98:NEG 99:TYPESTATE 100:TYPESTATE 101:DOMAIN
102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN 106:NEG 107:DOMAIN 108:TYPESTATE
109:TYPESTATE 110:DOMAIN 111:DOMAIN? 112:REVOCABLE 113:PROCESS 114:TYPESTATE
115:TYPESTATE 116:TYPESTATE 117:META 118:TYPESTATE 119:PROCESS 120:CV
121:TYPESTATE 122:PROCESS 123:POLICY 124:NEG 125:CV 126:CV 127:NEG 128:NEG
129:TYPESTATE 130:TYPESTATE 131:DOMAIN 132:DOMAIN 133:REVOCABLE 134:TYPESTATE
135:TYPESTATE 136:DOMAIN 137:TYPESTATE 138:TYPESTATE 139:TYPESTATE 140:DOMAIN
141:PROCESS 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE 145:TYPESTATE
146:TYPESTATE 147:DOMAIN 148:TYPESTATE 149:TYPESTATE 150:DOMAIN 151:DOMAIN
152:TYPESTATE 153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:PROCESS
158:DOMAIN 159:TYPESTATE 160:NEG 161:DOMAIN 162:NEG? 163:NEG 164:PROCESS
165:TYPESTATE 166:NEG 167:TYPESTATE 168:DOMAIN 169:DOMAIN 170:TYPESTATE
171:TYPESTATE 172:TYPESTATE 173:NEG 174:NEG 175:TYPESTATE 176:DOMAIN
177:DOMAIN 178:CV 179:CV 180:CV 181:TYPESTATE 182:TYPESTATE 183:TYPESTATE
184:DOMAIN 185:TYPESTATE 186:TYPESTATE 187:PROCESS? 188:THRESHOLD
189:THRESHOLD 190:U? 191:PROCESS 192:TYPESTATE 193:TYPESTATE 194:TYPESTATE
195:TYPESTATE 196:TYPESTATE 197:PROCESS 198:TYPESTATE 199:TYPESTATE
200:TYPESTATE 201:DOMAIN 202:TYPESTATE 203:TYPESTATE 204:TYPESTATE
```
