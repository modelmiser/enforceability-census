# v4-on-iCalendar pass — the null test (two blind raters)

2026-08-15 · Companion to `README.md` in this directory (the pre-pass
protocol, pushed at `350fae2` before any rater ran). **Status:
COMPLETE — grades: W1, W2, W3, W4 PASS in both raters; W5 PASS in
Av4i and FAIL in Xv4i — the same duplicate-text group that split under
v3, in the same cross-chunk mode, with the polarity reversed. The
owed PROCESS-churn lists are empty in both directions for both
raters.**

## Setup

Exactly as registered; no deviations.

- Instrument: `codebook/rater-pack-v4.md`, blob `4891605…`,
  hash-round-trip verified at serve time, served blind.
- Corpus: `census/ical/rfc5545_s3_musts.txt` byte-identical, n = 225.
- Rater Av4i (`claude-fable-5`, matching the pre-registered name):
  fresh instance, one input file (pack + corpus); per the author's
  harness usage record (an attestation — transcripts are not archived
  here) the rater made exactly ONE tool call, a read of that file.
- Rater Xv4i (`cursor-grok-4.6-high-fast`): five chunks on the pinned
  v3 partition (51+51+51+51+21).
- **Protocol events: NONE.** All five Xv4i chunks returned exact
  well-formed counts (single-shot per the run records — an
  attestation, as above); Av4i returned exactly 225.

## Results

| | rater Av4i (Claude) | rater Xv4i (Grok 4.6) |
|---|---|---|
| class tally | DOMAIN 199, PROCESS 22, U 3, TYPESTATE 1 | DOMAIN 195, PROCESS 22, U 5, TYPESTATE 3 |
| v4 eliminable share (v4 series — never substitutes the v3 headline) | 200/225 = 88.9% | 198/225 = 88.0% |
| match vs the archived v3 pair (W4 definition) | 224/225 = 99.6% | 222/225 = 98.7% |
| departures from BOTH archived v3 labels | 1 (item 43: U/U → DOMAIN) | 3 (43: → DOMAIN; 77: DOMAIN/DOMAIN → U; 185: TYPESTATE/TYPESTATE → DOMAIN) |

**Av4i-vs-Xv4i: raw 219/225 = 97.3% — numerically identical to the v3
pair's agreement — eliminable-vs-not 223/225 = 99.1%.** The
corpus-shared-prior caveat (paper limitation 6) applies at full force,
as everywhere in this series.

## Prediction grades (fixed at `350fae2`)

| # | prediction | outcome |
|---|---|---|
| W1 | THRESHOLD = 0, both raters | **PASS** in both — 0 and 0 |
| W2 | REVOCABLE ≤ 1 per rater | **PASS** in both — 0 and 0 |
| W3 | eliminable share in [86%, 90%] (counts 194–202) | **PASS** in both — 200 and 198 |
| W4 | match vs archived pair ≥ 219/225 | **PASS** in both — 224 and 222 |
| W5 | zero intra-group splits per rater | **PASS in Av4i** (0/14); **FAIL in Xv4i** — one split, the group {43, 79}, labeled DOMAIN in chunk 1 and U in chunk 2 |

**Owed observation lists (per the registration, counts explicit):**
- (a) v4-PROCESS against both-archived-non-PROCESS: **none** (0) for
  Av4i; **none** (0) for Xv4i.
- (b) v4-non-PROCESS against both-archived-PROCESS: **none** (0) for
  Av4i; **none** (0) for Xv4i.
- (c) the archived PROCESS-boundary split items, unconditionally:
  item 141 (archived PROCESS/U) → **PROCESS in both v4 raters**;
  item 203 (archived PROCESS/POLICY) → **PROCESS in both v4 raters**.
- No protocol-event U exists to report beside these lists.

## Findings

1. **The null held — by the metric named here: departures from both
   archived v3 labels are 1 (Av4i) and 3 (Xv4i) in 225.** The
   same-model cross-version label changes are larger — 2 (Av4i vs Ai)
   and 6 (Xv4i vs Xi) — because the departure metric nets out changes
   that land on the other archived rater's label (including the two
   closures of finding 3), and per the registration those raw changes
   are indistinguishable from rater stochasticity by this design. The
   registration also disclosed that this null outcome is the
   instrument-friendly one; it is announced with that disclosure
   restated. Every W clause that
   measures v4's protocol-boundary rules directly (W1 THRESHOLD, W2
   REVOCABLE) recorded exact zeros. Where the boundaries rules 16, 19,
   and 18 discriminate do not occur, those repairs are inert —
   measured, not
   assumed (rule 17 was not separately probed here, per the
   registration's own caveat). Sharpest form: the two v4 raters'
   PROCESS classes are
   **item-for-item identical across families** (the same 22 items,
   including both archived boundary-split items).
2. **Rule 18's measured cost did not travel.** On QUIC, v4 agreement
   fell with churn concentrated on the PROCESS boundary, hedged there
   as the lifecycle vocabulary "appearing to pull" procedure readings.
   Here both owed churn lists are empty in both directions for both
   raters. Consistent with the pull being coupled to lifecycle-like
   content rather than acting as a genre-independent vocabulary
   pressure; the genre-vs-model question about QUIC itself remains
   open, exactly as the registration scoped.
3. **Both archived PROCESS-boundary splits closed, unpredicted.**
   Items 141 (PROCESS/U under v3) and 203 (PROCESS/POLICY under v3)
   drew PROCESS from both v4 raters — cross-family unanimity on the
   two items the v3 pair split on, interior to the non-eliminable
   family both times. Recorded as an observation; nothing was
   registered about them beyond the unconditional listing duty.
4. **W5's failure is the same group, the same mode, the opposite
   polarity.** The foreign rater again split exactly {43, 79} — the
   identical-text pair straddling its first chunk boundary — but as
   DOMAIN-then-U where v3 gave U-then-DOMAIN. Across the four foreign
   readings of this pair (two per instrument version), the split
   reproduces while its direction does not: the item is stably
   liminal, and the instability is context-, not content-, driven
   (the same-family rater, seeing both items in one context, is
   deterministic under both versions — U/U under v3, DOMAIN/DOMAIN
   under v4). Three of the four v4 readings are DOMAIN against three
   of four U under v3 — a drift toward DOMAIN consistent with rule
   16's datum-bound vocabulary, though nothing here isolates that.
5. **The genre's one soft boundary is untouched by v4.** The
   192–194 cluster (value-type-of-"DTSTART" within-object
   consistency) reproduced its v3 reading exactly: DOMAIN in the
   same-family rater, TYPESTATE in the foreign one, both versions.
   v4 has no rule at this boundary — the v5 docket entry the iCal
   census filed is confirmed live by a second instrument version.
   (Xv4i also moved item 185, the archived both-rater TYPESTATE
   delegation duty, to DOMAIN — the ordering class in the foreign v4
   reading is now exactly the 192–194 cluster.)
6. **v4 shares: 88.9% / 88.0%, inside the registered [86%, 90%]
   envelope.** The v3 headline (88.0%/88.4%) stands, per the
   ring-fence; any quotation of a v4-ical share must name the
   instrument version.

## Raw labels (rater Av4i, archived verbatim)

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:U 8:DOMAIN
9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:PROCESS 14:DOMAIN 15:DOMAIN
16:PROCESS 17:DOMAIN 18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:PROCESS
23:DOMAIN 24:DOMAIN 25:PROCESS 26:DOMAIN 27:PROCESS 28:PROCESS 29:DOMAIN
30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN 35:DOMAIN 36:DOMAIN
37:PROCESS 38:DOMAIN 39:DOMAIN 40:DOMAIN 41:DOMAIN 42:DOMAIN 43:DOMAIN
44:DOMAIN 45:DOMAIN 46:PROCESS 47:PROCESS 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:DOMAIN 52:DOMAIN 53:DOMAIN 54:DOMAIN 55:DOMAIN 56:DOMAIN 57:DOMAIN
58:DOMAIN 59:DOMAIN 60:DOMAIN 61:DOMAIN 62:PROCESS 63:DOMAIN 64:DOMAIN
65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:PROCESS 70:DOMAIN 71:DOMAIN
72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:DOMAIN 77:DOMAIN 78:DOMAIN
79:DOMAIN 80:DOMAIN 81:DOMAIN 82:DOMAIN 83:DOMAIN 84:DOMAIN 85:DOMAIN
86:DOMAIN 87:DOMAIN 88:DOMAIN 89:DOMAIN 90:DOMAIN 91:PROCESS 92:DOMAIN
93:DOMAIN 94:DOMAIN 95:DOMAIN 96:DOMAIN 97:DOMAIN 98:DOMAIN 99:DOMAIN
100:DOMAIN 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN
106:DOMAIN 107:DOMAIN 108:DOMAIN 109:DOMAIN 110:DOMAIN 111:DOMAIN
112:DOMAIN 113:DOMAIN 114:DOMAIN 115:DOMAIN 116:DOMAIN 117:DOMAIN
118:PROCESS 119:DOMAIN 120:DOMAIN 121:DOMAIN 122:DOMAIN 123:DOMAIN
124:DOMAIN 125:DOMAIN 126:DOMAIN 127:DOMAIN 128:DOMAIN 129:DOMAIN
130:DOMAIN 131:DOMAIN 132:DOMAIN 133:DOMAIN 134:DOMAIN 135:DOMAIN
136:DOMAIN 137:DOMAIN 138:PROCESS 139:DOMAIN 140:DOMAIN 141:PROCESS
142:DOMAIN 143:DOMAIN 144:DOMAIN 145:DOMAIN 146:PROCESS 147:DOMAIN
148:DOMAIN 149:DOMAIN 150:PROCESS 151:DOMAIN 152:DOMAIN 153:DOMAIN
154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:DOMAIN
160:DOMAIN 161:DOMAIN 162:DOMAIN 163:DOMAIN 164:DOMAIN 165:DOMAIN
166:DOMAIN 167:DOMAIN 168:DOMAIN 169:DOMAIN 170:DOMAIN 171:DOMAIN
172:DOMAIN 173:DOMAIN 174:DOMAIN 175:DOMAIN 176:DOMAIN 177:DOMAIN
178:DOMAIN 179:DOMAIN 180:DOMAIN 181:DOMAIN 182:DOMAIN 183:DOMAIN
184:DOMAIN 185:TYPESTATE 186:DOMAIN 187:DOMAIN 188:DOMAIN 189:DOMAIN
190:DOMAIN 191:DOMAIN 192:DOMAIN 193:DOMAIN 194:DOMAIN 195:DOMAIN
196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN 200:U 201:U 202:DOMAIN
203:PROCESS 204:PROCESS 205:DOMAIN 206:DOMAIN 207:DOMAIN 208:DOMAIN
209:DOMAIN 210:PROCESS 211:DOMAIN 212:DOMAIN 213:DOMAIN 214:DOMAIN
215:DOMAIN 216:DOMAIN 217:DOMAIN 218:DOMAIN 219:DOMAIN 220:DOMAIN
221:DOMAIN 222:DOMAIN 223:DOMAIN 224:DOMAIN 225:DOMAIN
```

## Raw labels (rater Xv4i, archived verbatim)

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:U 8:DOMAIN
9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:PROCESS 14:DOMAIN 15:DOMAIN
16:PROCESS 17:DOMAIN 18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:PROCESS
23:DOMAIN 24:DOMAIN 25:PROCESS 26:DOMAIN 27:PROCESS 28:PROCESS 29:DOMAIN
30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN 35:DOMAIN 36:DOMAIN
37:PROCESS 38:DOMAIN 39:DOMAIN 40:DOMAIN 41:DOMAIN 42:DOMAIN 43:DOMAIN
44:DOMAIN 45:DOMAIN 46:PROCESS 47:PROCESS 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:DOMAIN 52:DOMAIN 53:DOMAIN 54:DOMAIN 55:DOMAIN 56:DOMAIN 57:DOMAIN
58:DOMAIN 59:DOMAIN 60:DOMAIN 61:DOMAIN 62:PROCESS 63:DOMAIN 64:DOMAIN
65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:PROCESS 70:DOMAIN 71:DOMAIN
72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:DOMAIN 77:U 78:DOMAIN
79:U 80:DOMAIN 81:DOMAIN 82:DOMAIN 83:DOMAIN 84:DOMAIN 85:DOMAIN
86:DOMAIN 87:DOMAIN 88:DOMAIN 89:DOMAIN 90:DOMAIN 91:PROCESS 92:DOMAIN
93:DOMAIN 94:DOMAIN 95:DOMAIN 96:DOMAIN 97:DOMAIN 98:DOMAIN 99:DOMAIN
100:DOMAIN 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN
106:DOMAIN 107:DOMAIN 108:DOMAIN 109:DOMAIN 110:DOMAIN 111:DOMAIN
112:DOMAIN 113:DOMAIN 114:DOMAIN 115:DOMAIN 116:DOMAIN 117:DOMAIN
118:PROCESS 119:DOMAIN 120:DOMAIN 121:DOMAIN 122:DOMAIN 123:DOMAIN
124:DOMAIN 125:DOMAIN 126:DOMAIN 127:DOMAIN 128:DOMAIN 129:DOMAIN
130:DOMAIN 131:DOMAIN 132:DOMAIN 133:DOMAIN 134:DOMAIN 135:DOMAIN
136:DOMAIN 137:DOMAIN 138:PROCESS 139:DOMAIN 140:DOMAIN 141:PROCESS
142:DOMAIN 143:DOMAIN 144:DOMAIN 145:DOMAIN 146:PROCESS 147:DOMAIN
148:DOMAIN 149:DOMAIN 150:PROCESS 151:DOMAIN 152:DOMAIN 153:DOMAIN
154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:DOMAIN
160:DOMAIN 161:DOMAIN 162:DOMAIN 163:DOMAIN 164:DOMAIN 165:DOMAIN
166:DOMAIN 167:DOMAIN 168:DOMAIN 169:DOMAIN 170:DOMAIN 171:DOMAIN
172:DOMAIN 173:DOMAIN 174:DOMAIN 175:DOMAIN 176:DOMAIN 177:DOMAIN
178:DOMAIN 179:DOMAIN 180:DOMAIN 181:DOMAIN 182:DOMAIN 183:DOMAIN
184:DOMAIN 185:DOMAIN 186:DOMAIN 187:DOMAIN 188:DOMAIN 189:DOMAIN
190:DOMAIN 191:DOMAIN 192:TYPESTATE 193:TYPESTATE 194:TYPESTATE
195:DOMAIN 196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN 200:U 201:U
202:DOMAIN 203:PROCESS 204:PROCESS 205:DOMAIN 206:DOMAIN 207:DOMAIN
208:DOMAIN 209:DOMAIN 210:PROCESS 211:DOMAIN 212:DOMAIN 213:DOMAIN
214:DOMAIN 215:DOMAIN 216:DOMAIN 217:DOMAIN 218:DOMAIN 219:DOMAIN
220:DOMAIN 221:DOMAIN 222:DOMAIN 223:DOMAIN 224:DOMAIN 225:DOMAIN
```
