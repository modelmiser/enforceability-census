# First rating pass under instrument v5 — QUIC (two blind raters)

2026-08-16 · Companion to `README.md` in this directory (the pre-pass
registration, pushed at `a35a60c` — timestamped 2026-08-16 00:05
local, five minutes past its 2026-08-15 dateline — before any rater
ran) and to the v5
amendment (`codebook/classes.md`, rules 20–24, predictions Z1–Z7).
**Status: COMPLETE — all six graded clauses PASS in both raters, the
series' first grade sheet with zero failed clauses. Read that with the
registration's own qualifier: three of the six (Z1, Z4-QUIC, Z6) were
downgraded to comprehension checks at registration, so the sheet's
discriminating content is Z7 and rule 23's two clauses — and those
passed with margin, not at the edge.**

## Setup

Exactly as registered; no deviations.

- Instrument: `codebook/rater-pack-v5.md`, blob `694e3a9…`,
  hash-round-trip verified at serve time, served blind.
- Corpus: `census/quic/rfc9000_s2-19_musts.txt` byte-identical,
  n = 281.
- Rater Aq5 (`claude-fable-5`, matching the pre-registered name):
  fresh same-family instance, single input file (pack + corpus). Per
  the author's harness usage record (an attestation — the transcript
  is not archived here), it made exactly ONE tool call, a read of that
  file, and returned all 281 labels in its final message. Ten labels
  carried torn-flags (items 23, 50, 59, 77, 92, 120, 190, 231, 237,
  252), stripped per the registered convention; preserved in the
  archive below.
- Rater Xq5 (`cursor-grok-4.6-high-fast`, matching the pre-registered
  name): six chunks on the pinned partition, every chunk returning
  exactly its item count single-shot, zero torn-flags.
- **Protocol events: NONE.** Label extraction was mechanical (regex
  over the transcript/output files; no hand transcription).

## Results

| | rater Aq5 (Claude, fresh) | rater Xq5 (Grok 4.6) |
|---|---|---|
| v5 eliminable share (NEW series — never substitutes v3/v4 figures) | 189/281 = 67.3% | 187/281 = 66.5% |
| class tally | TYPESTATE 115, DOMAIN 74, PROCESS 46, THRESHOLD 24, U 8, POLICY 4, META 4, REVOCABLE 3, CV 2, NEG 1 | TYPESTATE 115, DOMAIN 72, PROCESS 44, THRESHOLD 25, U 11, CV 4, POLICY 3, META 3, REVOCABLE 3, NEG 1 |
| match vs anchors (Av4/Xv4), outside set | 210/228 = 92.1% | 196/228 = 86.0% |
| role-matched agreement (vs Av4 / vs Xv4) | 256/281 = 91.1% | 221/281 = 78.6% |

**Aq5-vs-Xq5: raw 252/281 = 89.7%, eliminable-vs-not 261/281 =
92.9%** — the highest pair agreement measured on this corpus (prior
cells: 85.1% v3-old, 84.0% v4, 81.9% v3-replication). The v3 QUIC
headline (≈67–69%) and every v4-series figure stand, per the
ring-fence; for the record against the v3 counts (188/194 of 281):
Aq5's 189 sits inside that band, Xq5's 187 one item below it.

## Grades (all clauses fixed at `a35a60c`)

| clause | condition per rater | Aq5 | Xq5 |
|---|---|---|---|
| Z1 (comprehension check) | 63 = THRESHOLD | **PASS** | **PASS** |
| Z4-QUIC (comprehension check) | 191 = PROCESS | **PASS** | **PASS** |
| Z6 (comprehension check) | 192 ∧ 193 = PROCESS | **PASS** | **PASS** |
| Z7 (discriminating) | ≥ 42 of S49 = DOMAIN | **PASS** — 49/49 | **PASS** — 47/49 |
| 23(a) (discriminating) | anchor-match ≥ 192/228 | **PASS** — 210 | **PASS** — 196 |
| 23(b) (discriminating) | both-anchor departures ≤ 36 | **PASS** — 18 | **PASS** — 32 |

Z7's steered-excluded counts (reported beside, not graded, per the
registration): Aq5 44/44, Xq5 42/44 — Xq5's two departures (items 244
and 246, both → TYPESTATE) are UNSTEERED items, and both are items its
role-predecessor Xv4 had also moved to TYPESTATE in the v4 pass; the
five steered items held DOMAIN in both raters, so no Z7 margin
depends on a steer. Z4 overall remains open until TLS's first v5
pass, per the registration.

## Findings

1. **The in-pack adjudications transmitted — all three comprehension
   checks passed in both families, including the one that required a
   foreign-model flip.** Item 63 drew THRESHOLD from Xq5 where the
   same foreign model's v4 seat (Xv4) had read PROCESS and its v3
   seat (Xq) TYPESTATE — the first time this item's six-reading,
   three-class history converges. Items 192/193 held PROCESS in all
   eight readings across the three rosters; item 191 held PROCESS in
   all four v4/v5 seats, but its v3-era readings were THRESHOLD in
   three of four raters — this comprehension check, too, sits on a
   flipped item. A comprehension check that fails would have been the
   strongest possible transmission failure; none did.

2. **The v4 PROCESS churn on the monotonicity-guard quartet REVERSED
   under v5 — the pass's sharpest unpredicted result.** Items 11, 19,
   261, 272 ("ignore frames/fields that do not increase a limit")
   were TYPESTATE in 14 of 16 v3-era readings (two passes × two
   raters × four items; the exceptions are Xq's PROCESS on 11 and
   19), flipped to PROCESS in BOTH v4 raters (the churn the
   completion report hedged as rule 18's vocabulary "appearing to
   pull"), and now return to TYPESTATE in BOTH v5 raters — under a
   pack whose only addition NAMING these items' duty form is a clause
   saying rule 21 does NOT decide them (the registration's disclosed
   5-gram steer, whose direction is "no label"). Consistent with the
   v4 reading having been rule-18 vocabulary pressure that the
   explicit non-ruling released — though two disclosed confounds
   share the frame: the v4 same-family seat's model name was never
   recorded (the replication's roster-shape caveat), so the v4→v5
   flip bundles the instrument change with a possible model change;
   and the flip's direction is eliminable-ward, inside rule 20's
   disclosed rule-level reach. Consistent-with, not established; the
   quartet accounts for 4 of the 13 cross-family consensus departures
   in finding 4. Recorded as an observation for rule 21's residue —
   the items remain formally undecided in the codebook.

3. **The disclosed rule-20 recapture did NOT occur: item 105 is an
   explicit zero.** PROCESS in both v5 raters, matching both v4
   anchors — though v3's four readings were unanimously TYPESTATE.
   The amendment's eliminable-ward reach disclosure named 105 as its
   candidate; the reach did not materialize there.

4. **Outside-set movement sits below the v3-era raters' on the same
   metric, and its consensus core is 13 items.** Both-anchor
   departures: 18 (Aq5) and 32 (Xq5) against the v3-era raters'
   measured 40 and 36 — v5 sits closer to the v4 anchors than the v3
   raters do, decisively in the same-family seat and narrowly in the
   foreign one, as version proximity predicts. The two raters share 15 departure
   items, 13 with the SAME v5 label — cross-family consensus against
   both v4 anchors (the phenomenon v4's grading first measured, now
   at smaller scale): TYPESTATE on {11, 19, 261, 269, 272}, DOMAIN on
   {61, 146, 152, 203, 214, 232}, PROCESS on {96, 109}. Error-sign
   duty on direction: departures skew eliminable-ward — Aq5 11-of-18
   eliminable-ward vs 4 non-eliminable-ward, Xq5 14-of-32 vs 8 — the
   instrument-friendly direction, disclosed at registration as rule
   20's predicted reach; the net full-corpus effect is nonetheless
   ≈ nil against the v3 shares (189/187 vs the v3 band's 188–194).

5. **The steer ledger, settled per the registration's duty.** Of the
   five outside-set CONNECTION_CLOSE items: 125 and 190 reproduced
   their anchor readings exactly; 128 split (PROCESS/TYPESTATE); 144
   split away from the anchors (PROCESS/DOMAIN vs both-TYPESTATE);
   152 drew consensus DOMAIN against both-TYPESTATE anchors. Both
   144 and 152 are DEPARTURES — they count against clauses (a)/(b),
   so the anchor-ward steer the registration flagged did not carry
   any grade; on 144/152 the raters moved against the steer's
   pass-ward direction. Within Z7, the pass-ward-steered 130/147
   held DOMAIN — indistinguishable from the un-steered 42-of-44
   baseline; Z7 passes without them in Aq5 (44/44), while in Xq5 the
   steered-excluded count equals the bound integer exactly (42).

6. **Same-family cross-version stability far exceeds foreign.** Aq5
   matches Av4 on 256/281 (91.1%); Xq5 matches Xv4 on 221/281
   (78.6%) — the same direction as the replication's
   match-vs-archived-pair figures (94.0% vs 90.4%); its role-matched
   pair ran the other way (82.2% vs 83.6%), so the asymmetry is
   metric-dependent there and pronounced only here. Both owed
   metrics are quoted above per the registration.

## Owed table (the registration's nine watched items)

| item | Av4 | Xv4 | Aq5 | Xq5 |
|---|---|---|---|---|
| 11 | PROCESS | PROCESS | TYPESTATE | TYPESTATE |
| 19 | PROCESS | PROCESS | TYPESTATE | TYPESTATE |
| 63 | THRESHOLD | PROCESS | THRESHOLD | THRESHOLD |
| 105 | PROCESS | PROCESS | PROCESS | PROCESS |
| 191 | PROCESS | PROCESS | PROCESS | PROCESS |
| 192 | PROCESS | PROCESS | PROCESS | PROCESS |
| 193 | PROCESS | PROCESS | PROCESS | PROCESS |
| 261 | PROCESS | PROCESS | TYPESTATE | TYPESTATE |
| 272 | PROCESS | PROCESS | TYPESTATE | TYPESTATE |

## Clause 23(c) — departure lists and per-class deltas (explicit zeros)

Aq5's 18 both-anchor departures: 11, 19, 61, 87, 96, 109, 128, 143,
144, 146, 152, 203, 214, 232, 242, 261, 269, 272.
Xq5's 32: 2, 11, 19, 23, 29, 54, 55, 61, 87, 96, 99, 109, 136, 142,
144, 146, 152, 162, 165, 166, 167, 203, 214, 229, 232, 235, 261, 265,
269, 272, 279, 281.

Outside-set class counts, each v5 rater vs the anchor pair's
[min–max] on the same 228 items — every class listed, including
zero-delta rows: Aq5 — TYPESTATE 115 [112–127], PROCESS 43 [47–50],
DOMAIN 25 [17–19], THRESHOLD 23 [9–24], U 8 [10–11], POLICY 4 [4–4],
META 4 [3–3], REVOCABLE 3 [3–5], CV 2 [1–3], NEG 1 [2–2]. Xq5 —
TYPESTATE 113 [112–127], PROCESS 41 [47–50], DOMAIN 25 [17–19],
THRESHOLD 24 [9–24], U 11 [10–11], CV 4 [1–3], POLICY 3 [4–4], META 3
[3–3], REVOCABLE 3 [3–5], NEG 1 [2–2]. (Reported per clause (c);
under rule 23 these carry no pass/fail.)

## Raw labels (rater Aq5, archived verbatim — torn-flags preserved)

```
1:TYPESTATE 2:PROCESS 3:TYPESTATE 4:THRESHOLD 5:TYPESTATE 6:TYPESTATE
7:TYPESTATE 8:TYPESTATE 9:THRESHOLD 10:THRESHOLD 11:TYPESTATE 12:PROCESS
13:PROCESS 14:PROCESS 15:TYPESTATE 16:DOMAIN 17:THRESHOLD 18:THRESHOLD
19:TYPESTATE 20:PROCESS 21:UNCLASSIFIED 22:TYPESTATE 23:TYPESTATE?
24:TYPESTATE 25:TYPESTATE 26:THRESHOLD 27:THRESHOLD 28:TYPESTATE
29:PROCESS 30:PROCESS 31:TYPESTATE 32:DOMAIN 33:DOMAIN 34:POLICY
35:TYPESTATE 36:TYPESTATE 37:TYPESTATE 38:TYPESTATE 39:META
40:NEGOTIATION 41:DOMAIN 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE
45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:TYPESTATE 49:DOMAIN
50:TYPESTATE? 51:DOMAIN 52:DOMAIN 53:META 54:PROCESS 55:PROCESS
56:PROCESS 57:TYPESTATE 58:TYPESTATE 59:TYPESTATE? 60:TYPESTATE
61:DOMAIN 62:THRESHOLD 63:THRESHOLD 64:TYPESTATE 65:THRESHOLD
66:THRESHOLD 67:PROCESS 68:DOMAIN 69:REVOCABLE 70:TYPESTATE 71:PROCESS
72:TYPESTATE 73:TYPESTATE 74:TYPESTATE 75:UNCLASSIFIED 76:TYPESTATE
77:TYPESTATE? 78:TYPESTATE 79:CRYPTO-VERIFY 80:UNCLASSIFIED 81:PROCESS
82:PROCESS 83:THRESHOLD 84:POLICY 85:UNCLASSIFIED 86:DOMAIN 87:PROCESS
88:DOMAIN 89:TYPESTATE 90:PROCESS 91:TYPESTATE 92:PROCESS? 93:DOMAIN
94:THRESHOLD 95:TYPESTATE 96:PROCESS 97:TYPESTATE 98:TYPESTATE
99:TYPESTATE 100:TYPESTATE 101:TYPESTATE 102:TYPESTATE 103:PROCESS
104:TYPESTATE 105:PROCESS 106:TYPESTATE 107:PROCESS 108:PROCESS
109:PROCESS 110:TYPESTATE 111:TYPESTATE 112:TYPESTATE 113:TYPESTATE
114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:TYPESTATE 118:PROCESS
119:UNCLASSIFIED 120:THRESHOLD? 121:THRESHOLD 122:THRESHOLD
123:TYPESTATE 124:TYPESTATE 125:TYPESTATE 126:DOMAIN 127:DOMAIN
128:PROCESS 129:TYPESTATE 130:DOMAIN 131:DOMAIN 132:TYPESTATE
133:PROCESS 134:PROCESS 135:PROCESS 136:TYPESTATE 137:UNCLASSIFIED
138:PROCESS 139:TYPESTATE 140:TYPESTATE 141:TYPESTATE 142:TYPESTATE
143:PROCESS 144:PROCESS 145:UNCLASSIFIED 146:DOMAIN 147:DOMAIN
148:PROCESS 149:PROCESS 150:TYPESTATE 151:TYPESTATE 152:DOMAIN
153:TYPESTATE 154:PROCESS 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN
159:DOMAIN 160:DOMAIN 161:DOMAIN 162:TYPESTATE 163:REVOCABLE
164:REVOCABLE 165:TYPESTATE 166:TYPESTATE 167:TYPESTATE 168:PROCESS
169:PROCESS 170:UNCLASSIFIED 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE
174:TYPESTATE 175:TYPESTATE 176:TYPESTATE 177:PROCESS 178:TYPESTATE
179:PROCESS 180:PROCESS 181:PROCESS 182:POLICY 183:DOMAIN 184:DOMAIN
185:DOMAIN 186:DOMAIN 187:DOMAIN 188:DOMAIN 189:THRESHOLD 190:PROCESS?
191:PROCESS 192:PROCESS 193:PROCESS 194:TYPESTATE 195:TYPESTATE
196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN 200:DOMAIN 201:DOMAIN
202:DOMAIN 203:DOMAIN 204:DOMAIN 205:TYPESTATE 206:TYPESTATE
207:PROCESS 208:TYPESTATE 209:DOMAIN 210:TYPESTATE 211:TYPESTATE
212:TYPESTATE 213:DOMAIN 214:DOMAIN 215:TYPESTATE 216:TYPESTATE
217:TYPESTATE 218:TYPESTATE 219:TYPESTATE 220:TYPESTATE
221:CRYPTO-VERIFY 222:DOMAIN 223:TYPESTATE 224:TYPESTATE 225:TYPESTATE
226:DOMAIN 227:DOMAIN 228:DOMAIN 229:PROCESS 230:POLICY 231:THRESHOLD?
232:DOMAIN 233:DOMAIN 234:TYPESTATE 235:TYPESTATE 236:DOMAIN
237:DOMAIN? 238:DOMAIN 239:DOMAIN 240:DOMAIN 241:DOMAIN 242:DOMAIN
243:DOMAIN 244:DOMAIN 245:TYPESTATE 246:DOMAIN 247:DOMAIN 248:DOMAIN
249:DOMAIN 250:DOMAIN 251:DOMAIN 252:TYPESTATE? 253:DOMAIN
254:THRESHOLD 255:THRESHOLD 256:TYPESTATE 257:DOMAIN 258:THRESHOLD
259:THRESHOLD 260:DOMAIN 261:TYPESTATE 262:THRESHOLD 263:THRESHOLD
264:DOMAIN 265:DOMAIN 266:DOMAIN 267:TYPESTATE 268:TYPESTATE
269:TYPESTATE 270:DOMAIN 271:DOMAIN 272:TYPESTATE 273:TYPESTATE
274:TYPESTATE 275:TYPESTATE 276:TYPESTATE 277:TYPESTATE 278:TYPESTATE
279:DOMAIN 280:META 281:META
```

## Raw labels (rater Xq5, archived verbatim)

```
1:TYPESTATE 2:UNCLASSIFIED 3:TYPESTATE 4:THRESHOLD 5:TYPESTATE
6:TYPESTATE 7:TYPESTATE 8:TYPESTATE 9:THRESHOLD 10:THRESHOLD
11:TYPESTATE 12:PROCESS 13:PROCESS 14:PROCESS 15:TYPESTATE 16:DOMAIN
17:THRESHOLD 18:THRESHOLD 19:TYPESTATE 20:PROCESS 21:UNCLASSIFIED
22:TYPESTATE 23:PROCESS 24:TYPESTATE 25:TYPESTATE 26:THRESHOLD
27:THRESHOLD 28:TYPESTATE 29:TYPESTATE 30:PROCESS 31:TYPESTATE 32:DOMAIN
33:DOMAIN 34:POLICY 35:TYPESTATE 36:TYPESTATE 37:TYPESTATE 38:TYPESTATE
39:META 40:NEGOTIATION 41:DOMAIN 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE
45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:TYPESTATE 49:DOMAIN
50:TYPESTATE 51:DOMAIN 52:DOMAIN 53:META 54:TYPESTATE 55:TYPESTATE
56:PROCESS 57:TYPESTATE 58:TYPESTATE 59:TYPESTATE 60:TYPESTATE 61:DOMAIN
62:THRESHOLD 63:THRESHOLD 64:TYPESTATE 65:THRESHOLD 66:THRESHOLD
67:PROCESS 68:DOMAIN 69:REVOCABLE 70:TYPESTATE 71:PROCESS 72:TYPESTATE
73:TYPESTATE 74:TYPESTATE 75:UNCLASSIFIED 76:TYPESTATE 77:TYPESTATE
78:TYPESTATE 79:CRYPTO-VERIFY 80:UNCLASSIFIED 81:PROCESS 82:PROCESS
83:THRESHOLD 84:PROCESS 85:UNCLASSIFIED 86:DOMAIN 87:DOMAIN 88:DOMAIN
89:TYPESTATE 90:PROCESS 91:TYPESTATE 92:PROCESS 93:DOMAIN 94:THRESHOLD
95:TYPESTATE 96:PROCESS 97:TYPESTATE 98:TYPESTATE 99:PROCESS
100:TYPESTATE 101:TYPESTATE 102:TYPESTATE 103:PROCESS 104:TYPESTATE
105:PROCESS 106:TYPESTATE 107:PROCESS 108:PROCESS 109:PROCESS
110:TYPESTATE 111:TYPESTATE 112:TYPESTATE 113:TYPESTATE 114:TYPESTATE
115:TYPESTATE 116:TYPESTATE 117:TYPESTATE 118:PROCESS 119:UNCLASSIFIED
120:THRESHOLD 121:THRESHOLD 122:THRESHOLD 123:TYPESTATE 124:TYPESTATE
125:TYPESTATE 126:DOMAIN 127:DOMAIN 128:TYPESTATE 129:THRESHOLD
130:DOMAIN 131:DOMAIN 132:CRYPTO-VERIFY 133:PROCESS 134:PROCESS
135:PROCESS 136:CRYPTO-VERIFY 137:UNCLASSIFIED 138:PROCESS 139:TYPESTATE
140:TYPESTATE 141:TYPESTATE 142:THRESHOLD 143:TYPESTATE 144:DOMAIN
145:UNCLASSIFIED 146:DOMAIN 147:DOMAIN 148:PROCESS 149:PROCESS
150:TYPESTATE 151:TYPESTATE 152:DOMAIN 153:TYPESTATE 154:PROCESS
155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:DOMAIN 160:DOMAIN
161:DOMAIN 162:PROCESS 163:REVOCABLE 164:REVOCABLE 165:PROCESS
166:PROCESS 167:PROCESS 168:PROCESS 169:PROCESS 170:UNCLASSIFIED
171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE
176:TYPESTATE 177:PROCESS 178:TYPESTATE 179:PROCESS 180:PROCESS
181:PROCESS 182:POLICY 183:DOMAIN 184:DOMAIN 185:DOMAIN 186:DOMAIN
187:DOMAIN 188:DOMAIN 189:THRESHOLD 190:TYPESTATE 191:PROCESS
192:PROCESS 193:PROCESS 194:TYPESTATE 195:TYPESTATE 196:DOMAIN
197:DOMAIN 198:DOMAIN 199:DOMAIN 200:DOMAIN 201:DOMAIN 202:DOMAIN
203:DOMAIN 204:DOMAIN 205:TYPESTATE 206:TYPESTATE 207:PROCESS
208:TYPESTATE 209:DOMAIN 210:TYPESTATE 211:TYPESTATE 212:TYPESTATE
213:DOMAIN 214:DOMAIN 215:TYPESTATE 216:TYPESTATE 217:TYPESTATE
218:TYPESTATE 219:TYPESTATE 220:TYPESTATE 221:CRYPTO-VERIFY 222:DOMAIN
223:TYPESTATE 224:TYPESTATE 225:TYPESTATE 226:DOMAIN 227:DOMAIN
228:DOMAIN 229:UNCLASSIFIED 230:POLICY 231:UNCLASSIFIED 232:DOMAIN
233:DOMAIN 234:TYPESTATE 235:DOMAIN 236:DOMAIN 237:DOMAIN 238:DOMAIN
239:DOMAIN 240:DOMAIN 241:DOMAIN 242:PROCESS 243:DOMAIN 244:TYPESTATE
245:TYPESTATE 246:TYPESTATE 247:DOMAIN 248:DOMAIN 249:DOMAIN 250:DOMAIN
251:DOMAIN 252:TYPESTATE 253:DOMAIN 254:THRESHOLD 255:THRESHOLD
256:TYPESTATE 257:DOMAIN 258:THRESHOLD 259:THRESHOLD 260:DOMAIN
261:TYPESTATE 262:THRESHOLD 263:THRESHOLD 264:DOMAIN 265:TYPESTATE
266:DOMAIN 267:TYPESTATE 268:TYPESTATE 269:TYPESTATE 270:DOMAIN
271:DOMAIN 272:TYPESTATE 273:TYPESTATE 274:TYPESTATE 275:TYPESTATE
276:TYPESTATE 277:TYPESTATE 278:TYPESTATE 279:TYPESTATE 280:META
281:TYPESTATE
```
