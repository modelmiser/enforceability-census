# QUIC cross-roster replication — the third cell (two blind raters)

2026-08-15 · Companion to `README.md` in this directory (the pre-pass
protocol, pushed at `6698c4a` before any rater ran). **Status:
COMPLETE — grades: Y1, Y2, Y3, Y5, Y6 PASS; Y4 FAIL by exactly one
item below its lower bound. The THRESHOLD wobble reproduced at nearly
full magnitude with the new roster — and the role-ordered side
assignment flipped item-for-item on the spec-fixed constants.**

## Setup

As registered, with one transport deviation disclosed here.

- Instrument: v3 pass-4 pack, blob `a08febba…`, hash-round-trip
  verified at serve time, served blind — the same bytes as the
  2026-08-13 census.
- Corpus: `census/quic/rfc9000_s2-19_musts.txt` byte-identical,
  n = 281.
- Rater Aq (`claude-fable-5`, matching the pre-registered name): fresh
  instance, one input file; per the author's harness usage record (an
  attestation — transcripts not archived here) the rater made exactly
  ONE tool call. Aq emitted three torn-flags (25:REVOCABLE?,
  143:TYPESTATE?, 170:U?) — stripped per the registered rule, base
  labels governing; the flags are preserved in the archive below.
- Rater Xq (`cursor-grok-4.6-high-fast`): six chunks on the pinned
  partition. **Transport deviation, disclosed:** chunk 6 (items
  256–281) returned a DOUBLED emission — a partial stream through item
  271 that restarted mid-line (one glued, unparseable line) followed
  by a complete clean emission of all 26 items (this description, like
  the single-shot claims, is an attestation from the run records —
  transcripts not archived here). Adjudication, recorded
  before scoring: every index 256–281 is covered by at least one
  well-formed line, and the two emissions agree label-for-label on all
  16 legible overlapping indices — no label is missing or ambiguous,
  so the registered format-retry (which exists for missing/malformed
  labels) was not triggered. Chunks 1–5 returned exact counts
  single-shot (an attestation, as above).
- **Protocol events: NONE** (the deviation above produced no event-U).

## Results

| | rater Aq (Claude) | rater Xq (Grok 4.6) |
|---|---|---|
| class tally | TYPESTATE 134, DOMAIN 56, PROCESS 29, THRESHOLD 29, U 17, POLICY 5, META 4, NEG 3, CV 3, REVOCABLE 1 | TYPESTATE 134, DOMAIN 62, PROCESS 38, THRESHOLD 25, U 12, POLICY 3, META 3, NEG 2, CV 2 |
| eliminable share (v3 instrument, iCal-roster replication — never substitutes the census headline) | 190/281 = 67.6% | 196/281 = 69.8% |
| match vs archived pair (Y6 metric) | 264/281 = 94.0% | 254/281 = 90.4% |
| role-matched agreement (both-metric duty; per the registration, both archived raters are same-family Claude, so Xq has no own-family counterpart) | vs A″: 231/281 = 82.2% | vs B″: 235/281 = 83.6% |

**Aq-vs-Xq: raw 230/281 = 81.9%, eliminable-vs-not 249/281 = 88.6%.**
The corpus-shared-prior caveat applies throughout.

## Prediction grades (fixed at `6698c4a`)

| # | prediction | outcome |
|---|---|---|
| Y1 | new-pair THRESHOLD symdiff ≥ 4 | **PASS, decisively** — symdiff = **14** (old pair: 15); items {32, 41, 63, 142, 165, 182, 190, 197, 198, 199, 200, 238, 239, 266} |
| Y2 | ≥ 6 of the archived spec-fixed ten draw a non-THRESHOLD label from Aq/Xq | **PASS** — 9/10 (all but 191) |
| Y3 | ≥ 2 distinct classes across the six deadline-trio readings | **PASS** — three: PROCESS, THRESHOLD, TYPESTATE |
| Y4 | raw pair agreement in [82%, 88%] (counts 231–247) | **FAIL** — 230/281 = 81.9%, one item below the lower bound; below BOTH measured cells (85.1%, 84.0%) |
| Y5 | eliminable share in [64%, 71%] (counts 180–199), both raters | **PASS** in both — 190 and 196 |
| Y6 | match vs archived pair ≥ 239/281 per rater | **PASS** in both — 264 and 254 |

Per the registration: Y4's failure grades the author's model (the
"era-shrunk" half of it — see finding 1); Y1/Y2/Y3 outcomes are
additionally reported as roster-effect observations below, as owed.

## The owed four-rater table (the 16 boundary items)

|  item | A″ (v3-old) | B″ (v3-old) | Aq (this pass) | Xq (this pass) |
|---|---|---|---|---|
| 41 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |
| 63 | PROCESS | THRESHOLD | THRESHOLD | TYPESTATE |
| 69 | REVOCABLE | PROCESS | PROCESS | TYPESTATE |
| 87 | TYPESTATE | THRESHOLD | TYPESTATE | TYPESTATE |
| 96 | TYPESTATE | THRESHOLD | TYPESTATE | TYPESTATE |
| 142 | TYPESTATE | THRESHOLD | TYPESTATE | THRESHOLD |
| 163 | REVOCABLE | THRESHOLD | THRESHOLD | THRESHOLD |
| 164 | REVOCABLE | THRESHOLD | THRESHOLD | THRESHOLD |
| 191 | PROCESS | THRESHOLD | THRESHOLD | THRESHOLD |
| 197 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |
| 198 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |
| 199 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |
| 200 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |
| 238 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |
| 239 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |
| 266 | DOMAIN | THRESHOLD | THRESHOLD | DOMAIN |

Per-class counts over the 16, stated per rater: A″ — DOMAIN 8,
TYPESTATE 3, REVOCABLE 3, PROCESS 2, THRESHOLD 0, others 0; B″ —
THRESHOLD 15, PROCESS 1, others 0; Aq — THRESHOLD 12, TYPESTATE 3,
PROCESS 1, others 0; Xq — DOMAIN 8, TYPESTATE 4, THRESHOLD 4,
others 0.

## Findings

1. **The wobble is the corpus's, not the roster's — and the author's
   "era-shrunk" model half-failed.** The new pair's THRESHOLD
   symmetric difference is 14 against the old pair's 15, with ten
   items shared between the two symdiffs (old-only: {87, 96, 163, 164,
   191}; new-only: {32, 165, 182, 190}); agreement did not improve
   (Y4 failed low). Whatever produces the rule-3 boundary's softness
   on QUIC survives a complete change of rater roster under the fixed
   v3 instrument. The genre half of the author's model (boundary still
   soft) passed; the era half (softer than 2026-08-13) failed.
2. **The seven-constant polarity flip is the sharpest result: the
   role-ordered side assignment flipped item-for-item.** On the seven
   spec-fixed constants {197, 198, 199, 200, 238, 239, 266} plus 41,
   the archived pair read DOMAIN (the context-uncontrolled author) vs
   THRESHOLD (fresh same-family); the new pair reads THRESHOLD (fresh
   same-family) vs DOMAIN (foreign) — all eight items. Note the
   observed structure, which the table shows plainly: the one rater
   TYPE present in both passes — a fresh same-family instance — landed
   THRESHOLD both times on all eight, while DOMAIN was drawn by the
   author-context rater (old pass) and the foreign rater (new pass).
   Side assignment is therefore rater-correlated, not random; what IS
   roster-invariant is the boundary's location — two competent
   readings persist across a complete roster change under the fixed
   instrument. That persistence is the strongest evidence yet that
   v4's rule 16 repairs an instrument defect rather than an
   old-roster artifact (displacing the previous strongest, the
   v4-completion passes' six-item rule-16 generalization) — the
   question this pass was registered to answer.
3. **The completed grid reframes v4's QUIC "honest negative."** The
   three measured cells: v3 × old pair 85.1%; v3 × this roster
   **81.9%** (the worst cell); v4 × this roster-shape 84.0%. Under the
   same roster(-shape), moving v3 → v4 IMPROVES QUIC agreement by 2.1
   points; the drop that the v4-completion report recorded as v4's
   cost (85.1 → 84.0) decomposes as a −3.2-point roster effect and a
   +2.1-point instrument recovery. The registration's caveats apply in
   full: the v4 cell's same-family model name was never
   recorded (roster-shape, not roster-exact), and "roster" bundles
   model era, pair composition, and author-presence — this pass
   cannot unbundle them — and a third caveat from the registration
   applies with them: the ±terms are differences between single
   unreplicated cells, so fresh-instance stochasticity (observed by the
   v4-ical pass at 2–6 labels between same-model instances,
   indistinguishable from stochasticity by that design)
   is inside them. One error-sign
   note, stated plainly: this reframe exists only because Y4 — the
   pass's sole failed prediction — failed LOW; an in-band result would
   have erased it, so the miss direction flatters the reframe
   (mitigation: the chunk-6 adjudication's noise direction was
   pass-ward for Y4, and Y4 still failed). What the pass can say: the
   instrument-version comparison on this roster-shape favors v4,
   reversing the sign the bundled comparison suggested.
4. **The deadline edge persists across both measured rosters.** Items
   {69, 163, 164} have now drawn REVOCABLE (A″), PROCESS (B″ on 69,
   Aq on 69), THRESHOLD (B″, Aq, Xq on 163/164), and TYPESTATE (Xq on
   69) — four classes across four raters. The rule-19-shaped boundary
   is real in QUIC's text under both measured rosters.
5. **The census headline is roster-robust.** 67.6%/69.8% against the
   archived 66.9%/69.0% — the ≈67–69% quote survives a full roster
   change (quoted here as the replication series, never substituting
   the census).
6. **Match rates beat the archived pair's own agreement by 5–9
   points** (94.0%/90.4% vs 239/281): most new-rater labels land
   inside the archived pair's span — disagreement between rosters
   largely re-walks the disagreements within the old one.

## Raw labels (rater Aq, archived verbatim — torn-flags preserved)

```
1:TYPESTATE 2:PROCESS 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:TYPESTATE
7:TYPESTATE 8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:TYPESTATE 12:U
13:PROCESS 14:PROCESS 15:TYPESTATE 16:DOMAIN 17:TYPESTATE 18:TYPESTATE
19:TYPESTATE 20:U 21:U 22:TYPESTATE 23:TYPESTATE 24:TYPESTATE
25:REVOCABLE? 26:TYPESTATE 27:TYPESTATE 28:TYPESTATE 29:U 30:PROCESS
31:TYPESTATE 32:NEG 33:TYPESTATE 34:POLICY 35:TYPESTATE 36:TYPESTATE
37:TYPESTATE 38:TYPESTATE 39:META 40:NEG 41:THRESHOLD 42:TYPESTATE
43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE
48:TYPESTATE 49:DOMAIN 50:TYPESTATE 51:DOMAIN 52:DOMAIN 53:META
54:PROCESS 55:PROCESS 56:PROCESS 57:TYPESTATE 58:TYPESTATE 59:NEG
60:TYPESTATE 61:DOMAIN 62:THRESHOLD 63:THRESHOLD 64:TYPESTATE
65:THRESHOLD 66:THRESHOLD 67:PROCESS 68:THRESHOLD 69:PROCESS
70:TYPESTATE 71:U 72:TYPESTATE 73:TYPESTATE 74:TYPESTATE 75:U
76:TYPESTATE 77:TYPESTATE 78:TYPESTATE 79:CV 80:U 81:CV 82:U
83:THRESHOLD 84:POLICY 85:U 86:THRESHOLD 87:TYPESTATE 88:DOMAIN
89:TYPESTATE 90:U 91:TYPESTATE 92:PROCESS 93:THRESHOLD 94:THRESHOLD
95:TYPESTATE 96:TYPESTATE 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE
100:TYPESTATE 101:TYPESTATE 102:TYPESTATE 103:PROCESS 104:TYPESTATE
105:TYPESTATE 106:TYPESTATE 107:PROCESS 108:PROCESS 109:THRESHOLD
110:TYPESTATE 111:TYPESTATE 112:TYPESTATE 113:TYPESTATE 114:TYPESTATE
115:TYPESTATE 116:TYPESTATE 117:TYPESTATE 118:PROCESS 119:U
120:THRESHOLD 121:THRESHOLD 122:THRESHOLD 123:TYPESTATE 124:TYPESTATE
125:TYPESTATE 126:DOMAIN 127:DOMAIN 128:U 129:THRESHOLD 130:DOMAIN
131:DOMAIN 132:TYPESTATE 133:PROCESS 134:PROCESS 135:U 136:TYPESTATE
137:U 138:POLICY 139:TYPESTATE 140:TYPESTATE 141:TYPESTATE
142:TYPESTATE 143:TYPESTATE? 144:TYPESTATE 145:U 146:PROCESS
147:DOMAIN 148:PROCESS 149:PROCESS 150:TYPESTATE 151:TYPESTATE
152:DOMAIN 153:TYPESTATE 154:PROCESS 155:DOMAIN 156:DOMAIN 157:DOMAIN
158:DOMAIN 159:DOMAIN 160:DOMAIN 161:DOMAIN 162:TYPESTATE
163:THRESHOLD 164:THRESHOLD 165:TYPESTATE 166:TYPESTATE 167:TYPESTATE
168:PROCESS 169:PROCESS 170:U? 171:TYPESTATE 172:TYPESTATE
173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:TYPESTATE 177:PROCESS
178:TYPESTATE 179:PROCESS 180:TYPESTATE 181:TYPESTATE 182:POLICY
183:DOMAIN 184:DOMAIN 185:DOMAIN 186:THRESHOLD 187:THRESHOLD
188:THRESHOLD 189:THRESHOLD 190:TYPESTATE 191:THRESHOLD 192:PROCESS
193:PROCESS 194:TYPESTATE 195:TYPESTATE 196:DOMAIN 197:THRESHOLD
198:THRESHOLD 199:THRESHOLD 200:THRESHOLD 201:DOMAIN 202:DOMAIN
203:DOMAIN 204:DOMAIN 205:TYPESTATE 206:TYPESTATE 207:PROCESS
208:TYPESTATE 209:DOMAIN 210:TYPESTATE 211:TYPESTATE 212:TYPESTATE
213:DOMAIN 214:DOMAIN 215:TYPESTATE 216:TYPESTATE 217:TYPESTATE
218:TYPESTATE 219:TYPESTATE 220:TYPESTATE 221:CV 222:DOMAIN
223:TYPESTATE 224:TYPESTATE 225:TYPESTATE 226:DOMAIN 227:DOMAIN
228:DOMAIN 229:PROCESS 230:POLICY 231:U 232:DOMAIN 233:DOMAIN
234:TYPESTATE 235:TYPESTATE 236:DOMAIN 237:DOMAIN 238:THRESHOLD
239:THRESHOLD 240:DOMAIN 241:DOMAIN 242:PROCESS 243:DOMAIN 244:DOMAIN
245:TYPESTATE 246:DOMAIN 247:DOMAIN 248:DOMAIN 249:DOMAIN 250:DOMAIN
251:DOMAIN 252:TYPESTATE 253:DOMAIN 254:TYPESTATE 255:TYPESTATE
256:TYPESTATE 257:DOMAIN 258:TYPESTATE 259:TYPESTATE 260:DOMAIN
261:TYPESTATE 262:TYPESTATE 263:TYPESTATE 264:DOMAIN 265:DOMAIN
266:THRESHOLD 267:TYPESTATE 268:TYPESTATE 269:TYPESTATE 270:DOMAIN
271:DOMAIN 272:TYPESTATE 273:TYPESTATE 274:TYPESTATE 275:TYPESTATE
276:TYPESTATE 277:TYPESTATE 278:TYPESTATE 279:DOMAIN 280:META 281:META
```

## Raw labels (rater Xq, archived verbatim — canonical per-index set; chunk-6 doubled emission disclosed in Setup)

```
1:TYPESTATE 2:U 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:TYPESTATE
7:TYPESTATE 8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:PROCESS 12:PROCESS
13:PROCESS 14:PROCESS 15:TYPESTATE 16:DOMAIN 17:TYPESTATE 18:TYPESTATE
19:PROCESS 20:PROCESS 21:U 22:TYPESTATE 23:TYPESTATE 24:TYPESTATE
25:TYPESTATE 26:TYPESTATE 27:TYPESTATE 28:TYPESTATE 29:TYPESTATE
30:PROCESS 31:TYPESTATE 32:THRESHOLD 33:PROCESS 34:POLICY 35:TYPESTATE
36:NEG 37:TYPESTATE 38:TYPESTATE 39:META 40:NEG 41:DOMAIN 42:TYPESTATE
43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE
48:TYPESTATE 49:DOMAIN 50:TYPESTATE 51:DOMAIN 52:DOMAIN 53:META
54:TYPESTATE 55:TYPESTATE 56:PROCESS 57:TYPESTATE 58:TYPESTATE
59:TYPESTATE 60:TYPESTATE 61:PROCESS 62:THRESHOLD 63:TYPESTATE
64:TYPESTATE 65:THRESHOLD 66:THRESHOLD 67:PROCESS 68:THRESHOLD
69:TYPESTATE 70:TYPESTATE 71:PROCESS 72:TYPESTATE 73:TYPESTATE
74:TYPESTATE 75:U 76:TYPESTATE 77:TYPESTATE 78:TYPESTATE 79:PROCESS
80:U 81:PROCESS 82:PROCESS 83:THRESHOLD 84:POLICY 85:U 86:THRESHOLD
87:TYPESTATE 88:DOMAIN 89:TYPESTATE 90:PROCESS 91:TYPESTATE 92:PROCESS
93:THRESHOLD 94:THRESHOLD 95:TYPESTATE 96:TYPESTATE 97:TYPESTATE
98:TYPESTATE 99:TYPESTATE 100:TYPESTATE 101:TYPESTATE 102:TYPESTATE
103:PROCESS 104:TYPESTATE 105:TYPESTATE 106:TYPESTATE 107:PROCESS
108:PROCESS 109:THRESHOLD 110:TYPESTATE 111:TYPESTATE 112:TYPESTATE
113:TYPESTATE 114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:TYPESTATE
118:PROCESS 119:U 120:THRESHOLD 121:THRESHOLD 122:THRESHOLD
123:TYPESTATE 124:TYPESTATE 125:TYPESTATE 126:DOMAIN 127:DOMAIN 128:U
129:THRESHOLD 130:DOMAIN 131:DOMAIN 132:CV 133:PROCESS 134:TYPESTATE
135:U 136:CV 137:U 138:DOMAIN 139:TYPESTATE 140:TYPESTATE 141:DOMAIN
142:THRESHOLD 143:TYPESTATE 144:DOMAIN 145:U 146:PROCESS 147:DOMAIN
148:PROCESS 149:PROCESS 150:TYPESTATE 151:TYPESTATE 152:TYPESTATE
153:TYPESTATE 154:PROCESS 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN
159:DOMAIN 160:DOMAIN 161:DOMAIN 162:TYPESTATE 163:THRESHOLD
164:THRESHOLD 165:THRESHOLD 166:TYPESTATE 167:TYPESTATE 168:TYPESTATE
169:PROCESS 170:PROCESS 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE
174:TYPESTATE 175:TYPESTATE 176:TYPESTATE 177:PROCESS 178:TYPESTATE
179:PROCESS 180:TYPESTATE 181:TYPESTATE 182:THRESHOLD 183:DOMAIN
184:DOMAIN 185:DOMAIN 186:THRESHOLD 187:THRESHOLD 188:THRESHOLD
189:THRESHOLD 190:THRESHOLD 191:THRESHOLD 192:PROCESS 193:PROCESS
194:TYPESTATE 195:TYPESTATE 196:DOMAIN 197:DOMAIN 198:DOMAIN
199:DOMAIN 200:DOMAIN 201:DOMAIN 202:DOMAIN 203:PROCESS 204:DOMAIN
205:TYPESTATE 206:TYPESTATE 207:PROCESS 208:TYPESTATE 209:DOMAIN
210:TYPESTATE 211:TYPESTATE 212:TYPESTATE 213:DOMAIN 214:PROCESS
215:TYPESTATE 216:TYPESTATE 217:TYPESTATE 218:TYPESTATE 219:TYPESTATE
220:TYPESTATE 221:DOMAIN 222:DOMAIN 223:TYPESTATE 224:TYPESTATE
225:TYPESTATE 226:DOMAIN 227:DOMAIN 228:DOMAIN 229:U 230:POLICY 231:U
232:PROCESS 233:DOMAIN 234:TYPESTATE 235:DOMAIN 236:DOMAIN 237:DOMAIN
238:DOMAIN 239:DOMAIN 240:DOMAIN 241:DOMAIN 242:PROCESS 243:DOMAIN
244:DOMAIN 245:TYPESTATE 246:DOMAIN 247:DOMAIN 248:DOMAIN 249:DOMAIN
250:DOMAIN 251:DOMAIN 252:TYPESTATE 253:DOMAIN 254:TYPESTATE
255:TYPESTATE 256:TYPESTATE 257:DOMAIN 258:TYPESTATE 259:TYPESTATE
260:DOMAIN 261:TYPESTATE 262:TYPESTATE 263:TYPESTATE 264:DOMAIN
265:TYPESTATE 266:DOMAIN 267:TYPESTATE 268:TYPESTATE 269:TYPESTATE
270:DOMAIN 271:DOMAIN 272:TYPESTATE 273:TYPESTATE 274:TYPESTATE
275:TYPESTATE 276:TYPESTATE 277:TYPESTATE 278:TYPESTATE 279:TYPESTATE
280:META 281:PROCESS
```
