# RFC 9000 (QUIC) §2–§19 — two-rater census (2026-08-13)

**Headline: ≈67–69% of QUIC's transport machinery is type-eliminable in
shape (A″ 66.9%, B″ 69.0%; raw agreement 85.1%) — landing between MLS
(≈57%) and TLS (80–83%) under the same frozen instrument. Three corpora,
one instrument: the results are consistent with a spectrum — the share
varies across censused spans and an interior value exists — and each
span's position is explainable by what it states as obligations (a
post-hoc reading, not an established mechanism; the author's pre-registered
directional model of exactly that story, Q1's "nearer TLS", partly
failed).** Predictions Q1–Q5
(commit `29fcf08`, publicly timestamped before any rater) graded below;
per the pre-committed interpretation, outcomes grade the author's
structural model of QUIC and license nothing.

## Setup

- Corpus: n = 281 (`rfc9000_s2-19_musts.txt`, frozen at `36f8334`,
  2026-08-13T22:03Z public).
- Instrument: the TLS pass-4 rater pack, **verbatim** (blob
  `a08febba22fd2cb117a9be41654a6209e0104e57`, `git cat-file` round-trip
  verified; same title-quirk disclosure as the MLS census).
- Rater A″: the census author (LLM agent; context NOT controlled). Labels
  written to disk before B″ returned.
- Rater B″: fresh blind LLM agent; two files only (instrument + corpus),
  instructed to read nothing else.

## Scores

| measure | value |
|---|---|
| raw item agreement | 239/281 = **85.1%** |
| eliminable-vs-not agreement | 251/281 = **89.3%** |
| headline eliminable, A″ | 188/281 = **66.9%** |
| headline eliminable, B″ | 194/281 = **69.0%** |
| class tallies A″ | 128 TYPESTATE, 60 DOMAIN, 48 PROCESS, 17 THRESHOLD, 12 U, 5 POLICY, 4 META, 3 REVOCABLE, 3 CV, 1 NEG |
| class tallies B″ | 133 TYPESTATE, 61 DOMAIN, 32 PROCESS, 32 THRESHOLD, 9 U, 6 POLICY, 4 META, 3 CV, 1 NEG, 0 REVOCABLE |

## Pre-registered prediction outcomes (bands from `README.md`, commit 29fcf08)

| # | prediction (band) | outcome |
|---|---|---|
| Q1 | THREE clauses, quoted in full: "the eliminable share lands between the two measured points, **nearer TLS**: band 68–80%, strictly above MLS's 57.5% top endpoint" | **FAIL — 1 of 3 clauses passes cleanly.** *Between the two points*: PASS (66.9% and 69.0% both lie strictly between 57.5% and 79.9%). *Nearer TLS*: FAIL for A″ (66.9% is 9.4 points from MLS's 57.5% endpoint and 13.0 from TLS's 79.9% floor — nearer MLS; B″'s 69.0% is marginally nearer TLS at 11.5 vs 10.9). *Band 68–80%*: FAIL for A″ (1.1 points below the floor; B″ in band). Both raters clear the 57.5% clause. The pre-registration did not fix a per-rater vs quoted-range reading; the stricter reading (every valid rater) governs, as in the MLS grading. |
| Q2 | TWO clauses, quoted in full: "the crypto core is SMALLER than TLS's: CV ≤ 4% (≤ 11 of 281)" | **PASS on both** — 3 items (1.1%) in BOTH raters, item-identical ({79, 81, 221}); 1.1% < TLS's 2.9%, and the RFC 9001 document boundary censors CV exactly as predicted (rule 7, called in advance this time). |
| Q3 | TYPESTATE largest single class, 35–50% | **PASS** — A″ 45.6%, B″ 47.3%, largest class in both. |
| Q4 | rule-3 edge recurs: THRESHOLD symdiff ≥ 1 with a spec-fixed constant among the disagreed items | **PASS** — THRESHOLD symmetric difference is **15**, the single largest disagreement axis. Ten of the fifteen sit on constants the SPEC fixed: the 20-byte CID cap and 1–20 validity range (197–200, 266), the 8-byte minimum (41), the at-least-2 parameter floor (238, 239), the 1200-byte ICMP floor (191), and the 4096-byte buffer duty (63 — the constant itself is stated in the adjacent, agreed item 62). Two track a peer-ADVERTISED number, not a spec constant (max_ack_delay deadlines: 163, 164), and three are relative-size bounds (87 — which also carries the spec-fixed 1200-byte minimum — 96, 142). The spec-fixed ten alone satisfy the prediction; the derived-but-not-chosen gap in decision rule 3 is reproducible, not an MLS artifact. |
| Q5 | TWO clauses: (a) raw agreement 78–90%; (b) META, REVOCABLE, CV each ≤ 1 item symdiff | **FAIL — 1 of 2 clauses passes.** (a) PASS: 85.1%. (b) FAIL: META 0 ✓ and CV 0 ✓, but **REVOCABLE symdiff 3** (items 69, 163, 164 — A″ read the PTO-send and ack-within-max_ack_delay duties as needs-a-clock REVOCABLE; B″ read 163/164 as inequality-vs-advertised-number THRESHOLD and 69 as procedure). |

Interpretation, as pre-committed: Q1's marginal failure and Q5's clause-b
failure are wrong guesses about QUIC, recorded as such. No re-rating, no
rule change, no exclusion, no quote discretion.

## What the census found

1. **The spectrum is real.** MLS ≈57% → QUIC ≈67–69% → TLS 80–83%, all
   under one frozen instrument at one granularity. QUIC sits in the middle
   for a legible reason: it is state-machine-dense (TYPESTATE ~46–47%,
   the largest class — stream states, flow-control-vs-advertised-limits,
   connection-ID lifecycle, migration ordering) but carries real PROCESS
   mass (11–17%) and a THRESHOLD family TLS §4 lacks (spec-fixed numeric
   limits: anti-amplification 3×, 1200-byte minimums, 20-byte caps).
2. **Document-boundary censoring, predicted and confirmed.** CV = 3/281
   (1.1%), item-identical in both raters — packet protection lives in
   RFC 9001, loss recovery in RFC 9002, and this corpus cannot see them
   (rule 7). A whole-protocol claim would need all three documents; this
   census claims only its span.
3. **The rule-3 edge is now measured twice, larger the second time.**
   15 of 42 disagreements sit on THRESHOLD-vs-{DOMAIN, PROCESS,
   REVOCABLE, TYPESTATE} splits — ten of them over constants the SPEC
   picked (not the operator, not the framing), two over a peer-advertised
   number, three over relative bounds (the Q4 row itemizes the split).
   Decision rule 3's structural-vs-chosen dichotomy has no bucket for
   spec-chosen constants, and raters fill the gap in opposite
   directions. This is the strongest candidate-rule
   evidence the census series has produced (a rule-16 candidate:
   spec-fixed constants classify as ___ — for a FUTURE instrument
   version, alongside the MLS census's rule-15 candidate).
4. **A second new edge: deadline duties.** A″:REVOCABLE vs
   B″:{THRESHOLD, PROCESS} on ack-deadline and timer duties (69, 163,
   164) — "ack within the advertised max_ack_delay" reads as a freshness
   window (clock ⇒ REVOCABLE), as an inequality against an advertised
   number (THRESHOLD), or as procedure. TLS §4 and MLS had no
   deadline-liveness duties to stress this boundary; QUIC does.
5. **The MLS capability-compatibility boundary recurs, smaller.** Items
   59, 77, 90, 145, 229 split on U-vs-{TYPESTATE, PROCESS} over
   internal-capability and liveness guards ("cannot be supported", "does
   not support", "MUST NOT delay") — the rule-11 wire-falsifiability
   boundary carrying 5 of 42 disagreements.
6. **DISAGREE bucket: 42 items (14.9%), unresolved by design.**
   Clusters: spec-constant THRESHOLD family (13: 41, 63, 87, 96, 142,
   191, 197–200, 238, 239, 266); timer/deadline family (3: 69, 163, 164);
   PROCESS-vs-DOMAIN, the rule-13 boundary (9: 33, 61, 88, 146, 185, 203,
   214, 232, 242); PROCESS-vs-TYPESTATE (7: 128, 144, 162, 176, 180, 181,
   269); U-boundary (5: 59, 77, 90, 145, 229); singletons (5: 16, 50, 84,
   152, 275).

## Author-context note

No E1-class event was detected this pass (no antecedent-less sentences
were resolved from the source; item [50] is a lead-in whose list the
extraction absorbed, classified from its own text by both raters). A″'s
context remains uncontrolled by design; the 42-item DISAGREE bucket is
the visible error bar.

## Raw labels (archived verbatim; `?` = rater-flagged torn)

Rater A″ (author):

```
1:TYPESTATE 2:PROCESS 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:TYPESTATE 7:TYPESTATE 8:TYPESTATE 9:TYPESTATE 10:TYPESTATE
11:TYPESTATE 12:PROCESS 13:PROCESS 14:PROCESS 15:TYPESTATE 16:TYPESTATE 17:TYPESTATE 18:TYPESTATE 19:TYPESTATE 20:PROCESS
21:U 22:TYPESTATE 23:POLICY 24:TYPESTATE 25:TYPESTATE 26:TYPESTATE 27:TYPESTATE 28:TYPESTATE 29:TYPESTATE 30:PROCESS
31:TYPESTATE 32:DOMAIN 33:PROCESS 34:POLICY 35:TYPESTATE 36:TYPESTATE 37:TYPESTATE 38:TYPESTATE 39:META 40:NEG?
41:DOMAIN 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:TYPESTATE 49:DOMAIN 50:DOMAIN
51:DOMAIN 52:DOMAIN 53:META 54:TYPESTATE 55:TYPESTATE 56:PROCESS 57:TYPESTATE 58:TYPESTATE 59:U 60:TYPESTATE
61:PROCESS 62:THRESHOLD? 63:PROCESS 64:TYPESTATE 65:THRESHOLD 66:THRESHOLD 67:PROCESS 68:THRESHOLD 69:REVOCABLE? 70:TYPESTATE
71:PROCESS 72:TYPESTATE 73:TYPESTATE 74:TYPESTATE 75:U 76:TYPESTATE 77:U 78:TYPESTATE 79:CV? 80:U
81:CV 82:PROCESS 83:THRESHOLD 84:TYPESTATE 85:U 86:THRESHOLD 87:TYPESTATE 88:PROCESS 89:TYPESTATE 90:U?
91:TYPESTATE 92:PROCESS 93:THRESHOLD 94:THRESHOLD 95:TYPESTATE 96:TYPESTATE 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE 100:TYPESTATE
101:TYPESTATE 102:TYPESTATE 103:PROCESS 104:TYPESTATE 105:TYPESTATE 106:TYPESTATE 107:PROCESS 108:PROCESS 109:PROCESS 110:TYPESTATE
111:TYPESTATE 112:TYPESTATE 113:TYPESTATE 114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:TYPESTATE 118:PROCESS 119:U 120:THRESHOLD?
121:THRESHOLD 122:THRESHOLD 123:TYPESTATE 124:TYPESTATE 125:TYPESTATE 126:DOMAIN 127:DOMAIN 128:PROCESS 129:THRESHOLD 130:DOMAIN
131:DOMAIN 132:TYPESTATE 133:PROCESS 134:PROCESS 135:PROCESS 136:TYPESTATE 137:U 138:POLICY 139:TYPESTATE 140:TYPESTATE
141:TYPESTATE 142:TYPESTATE 143:TYPESTATE 144:PROCESS 145:PROCESS 146:PROCESS 147:DOMAIN 148:PROCESS 149:PROCESS 150:TYPESTATE
151:TYPESTATE 152:TYPESTATE 153:TYPESTATE 154:PROCESS 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:DOMAIN 160:DOMAIN
161:DOMAIN 162:PROCESS 163:REVOCABLE? 164:REVOCABLE? 165:TYPESTATE 166:TYPESTATE 167:TYPESTATE 168:PROCESS 169:PROCESS 170:U
171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:PROCESS 177:PROCESS 178:TYPESTATE? 179:PROCESS 180:PROCESS
181:PROCESS 182:POLICY 183:DOMAIN 184:DOMAIN 185:PROCESS 186:THRESHOLD 187:THRESHOLD 188:THRESHOLD 189:THRESHOLD 190:THRESHOLD
191:PROCESS 192:PROCESS 193:PROCESS 194:TYPESTATE 195:TYPESTATE 196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN 200:DOMAIN
201:DOMAIN 202:DOMAIN 203:PROCESS 204:DOMAIN 205:TYPESTATE 206:TYPESTATE 207:PROCESS 208:TYPESTATE 209:DOMAIN 210:TYPESTATE
211:TYPESTATE 212:TYPESTATE 213:DOMAIN 214:PROCESS 215:TYPESTATE 216:TYPESTATE 217:TYPESTATE 218:TYPESTATE 219:TYPESTATE 220:TYPESTATE
221:CV 222:DOMAIN 223:TYPESTATE 224:TYPESTATE 225:TYPESTATE 226:DOMAIN 227:DOMAIN 228:DOMAIN 229:U? 230:POLICY
231:U 232:PROCESS 233:DOMAIN 234:TYPESTATE 235:DOMAIN 236:DOMAIN 237:DOMAIN 238:DOMAIN 239:DOMAIN 240:DOMAIN
241:DOMAIN 242:PROCESS 243:DOMAIN 244:DOMAIN 245:TYPESTATE 246:DOMAIN 247:DOMAIN 248:DOMAIN 249:DOMAIN 250:DOMAIN
251:DOMAIN 252:TYPESTATE 253:DOMAIN 254:TYPESTATE 255:TYPESTATE 256:TYPESTATE 257:DOMAIN 258:TYPESTATE 259:TYPESTATE 260:DOMAIN
261:TYPESTATE 262:TYPESTATE 263:TYPESTATE 264:DOMAIN 265:DOMAIN 266:DOMAIN 267:TYPESTATE 268:TYPESTATE 269:PROCESS 270:DOMAIN
271:DOMAIN 272:TYPESTATE 273:TYPESTATE 274:TYPESTATE 275:DOMAIN 276:TYPESTATE 277:TYPESTATE 278:TYPESTATE 279:DOMAIN 280:META
281:META
```

Rater B″ (blind):

```
1:TYPESTATE 2:PROCESS 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:TYPESTATE 7:TYPESTATE 8:TYPESTATE 9:TYPESTATE 10:TYPESTATE
11:TYPESTATE 12:PROCESS 13:PROCESS 14:PROCESS 15:TYPESTATE 16:DOMAIN 17:TYPESTATE 18:TYPESTATE 19:TYPESTATE 20:PROCESS
21:U 22:TYPESTATE 23:POLICY 24:TYPESTATE 25:TYPESTATE 26:TYPESTATE 27:TYPESTATE 28:TYPESTATE 29:TYPESTATE 30:PROCESS
31:TYPESTATE 32:DOMAIN 33:DOMAIN 34:POLICY 35:TYPESTATE 36:TYPESTATE 37:TYPESTATE 38:TYPESTATE 39:META 40:NEG
41:THRESHOLD 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:TYPESTATE 49:DOMAIN 50:TYPESTATE
51:DOMAIN 52:DOMAIN 53:META 54:TYPESTATE 55:TYPESTATE 56:PROCESS 57:TYPESTATE 58:TYPESTATE 59:TYPESTATE 60:TYPESTATE
61:DOMAIN 62:THRESHOLD 63:THRESHOLD 64:TYPESTATE 65:THRESHOLD 66:THRESHOLD 67:PROCESS 68:THRESHOLD 69:PROCESS 70:TYPESTATE
71:PROCESS 72:TYPESTATE 73:TYPESTATE 74:TYPESTATE 75:U 76:TYPESTATE 77:TYPESTATE 78:TYPESTATE 79:CV 80:U
81:CV 82:PROCESS 83:THRESHOLD 84:POLICY 85:U 86:THRESHOLD 87:THRESHOLD 88:DOMAIN 89:TYPESTATE 90:PROCESS
91:TYPESTATE 92:PROCESS 93:THRESHOLD 94:THRESHOLD 95:TYPESTATE 96:THRESHOLD 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE 100:TYPESTATE
101:TYPESTATE 102:TYPESTATE 103:PROCESS 104:TYPESTATE 105:TYPESTATE 106:TYPESTATE 107:PROCESS 108:PROCESS 109:PROCESS 110:TYPESTATE
111:TYPESTATE 112:TYPESTATE 113:TYPESTATE 114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:TYPESTATE 118:PROCESS 119:U 120:THRESHOLD
121:THRESHOLD 122:THRESHOLD 123:TYPESTATE 124:TYPESTATE 125:TYPESTATE 126:DOMAIN 127:DOMAIN 128:TYPESTATE 129:THRESHOLD 130:DOMAIN
131:DOMAIN 132:TYPESTATE 133:PROCESS 134:PROCESS 135:PROCESS 136:TYPESTATE 137:U 138:POLICY 139:TYPESTATE 140:TYPESTATE
141:TYPESTATE 142:THRESHOLD 143:TYPESTATE 144:TYPESTATE 145:U 146:DOMAIN 147:DOMAIN 148:PROCESS 149:PROCESS 150:TYPESTATE
151:TYPESTATE 152:DOMAIN 153:TYPESTATE 154:PROCESS 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:DOMAIN 160:DOMAIN
161:DOMAIN 162:TYPESTATE 163:THRESHOLD 164:THRESHOLD 165:TYPESTATE 166:TYPESTATE 167:TYPESTATE 168:PROCESS 169:PROCESS 170:U
171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:TYPESTATE 177:PROCESS 178:TYPESTATE 179:PROCESS 180:TYPESTATE
181:TYPESTATE 182:POLICY 183:DOMAIN 184:DOMAIN 185:DOMAIN 186:THRESHOLD 187:THRESHOLD 188:THRESHOLD 189:THRESHOLD 190:THRESHOLD
191:THRESHOLD 192:PROCESS 193:PROCESS 194:TYPESTATE 195:TYPESTATE 196:DOMAIN 197:THRESHOLD 198:THRESHOLD 199:THRESHOLD 200:THRESHOLD
201:DOMAIN 202:DOMAIN 203:DOMAIN 204:DOMAIN 205:TYPESTATE 206:TYPESTATE 207:PROCESS 208:TYPESTATE 209:DOMAIN 210:TYPESTATE
211:TYPESTATE 212:TYPESTATE 213:DOMAIN 214:DOMAIN 215:TYPESTATE 216:TYPESTATE 217:TYPESTATE 218:TYPESTATE 219:TYPESTATE 220:TYPESTATE
221:CV 222:DOMAIN 223:TYPESTATE 224:TYPESTATE 225:TYPESTATE 226:DOMAIN 227:DOMAIN 228:DOMAIN 229:PROCESS 230:POLICY
231:U 232:DOMAIN 233:DOMAIN 234:TYPESTATE 235:DOMAIN 236:DOMAIN 237:DOMAIN 238:THRESHOLD 239:THRESHOLD 240:DOMAIN
241:DOMAIN 242:DOMAIN 243:DOMAIN 244:DOMAIN 245:TYPESTATE 246:DOMAIN 247:DOMAIN 248:DOMAIN 249:DOMAIN 250:DOMAIN
251:DOMAIN 252:TYPESTATE 253:DOMAIN 254:TYPESTATE 255:TYPESTATE 256:TYPESTATE 257:DOMAIN 258:TYPESTATE 259:TYPESTATE 260:DOMAIN
261:TYPESTATE 262:TYPESTATE 263:TYPESTATE 264:DOMAIN 265:DOMAIN 266:THRESHOLD 267:TYPESTATE 268:TYPESTATE 269:TYPESTATE 270:DOMAIN
271:DOMAIN 272:TYPESTATE 273:TYPESTATE 274:TYPESTATE 275:TYPESTATE 276:TYPESTATE 277:TYPESTATE 278:TYPESTATE 279:DOMAIN 280:META
281:META
```
