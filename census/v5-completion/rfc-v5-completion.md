# v5 completion passes — TLS, RFC 9001, iCalendar (six blind rating passes)

2026-08-16 · Companion to `README.md` in this directory (the pre-pass
registration, pushed at `cf7e219` before any rater ran) and to the v5
amendment (`codebook/classes.md`). **Status: COMPLETE — every Z clause
PASSES in every rater (Z2, Z3, Z4-TLS, Z5), which settles Z4 OVERALL
as PASS; rule 23's clauses split — PASS ×4 on RFC 9001 and on TLS's
23(a), FAIL in Av5's TLS 23(b) by exactly one item, and FAIL ×4 on
iCalendar, where the registered overreach test fired. Per the
amendment's pre-committed interpretation, the iCal failures are
evidence of instrument mis-design on the format genre — that verdict,
not the elevated v5-iCal share, is the result.**

## Setup

Exactly as registered; no deviations.

- Instrument: `codebook/rater-pack-v5.md`, blob `694e3a9…`,
  hash-round-trip verified at serve time, served blind — the same
  bytes as `census/v5-quic/`.
- Corpora byte-identical to their censuses (TLS n=204, RFC 9001 n=69,
  iCal n=225).
- Six rating passes: per corpus, rater Av5 — fresh same-family
  instance (`claude-fable-5`, matching the pre-registered name),
  single input file; per the author's harness usage record (an
  attestation — transcripts not archived here) each made exactly ONE
  tool call, a read of that file, and returned its full label list in
  its final message. Rater Xv5 —
  `cursor-grok-4.6-high-fast` (matching the pre-registered name) on
  the pinned partitions; all eleven chunks returned exact counts
  single-shot.
- Torn-flags (stripped per convention, preserved in the archives):
  Av5-TLS {64, 66, 164, 190}; Av5-9001 {15, 46, 58} — **item 15,
  the Z3 item, is torn** (`TYPESTATE?`); Xv5-9001 {29, 31}; zero in
  both iCal raters and in Xv5-TLS.
- **Protocol events: NONE** in any of the six passes. Label
  extraction mechanical throughout.

## Results

| | TLS Av5 / Xv5 | 9001 Av5 / Xv5 | iCal Av5 / Xv5 |
|---|---|---|---|
| v5 eliminable share (NEW series) | 173/204 = 84.8% / 172/204 = 84.3% | 41/69 = 59.4% / 41/69 = 59.4% | 211/225 = 93.8% / 205/225 = 91.1% — **quoted only as the mis-design measurement, per the verdict below** |
| earlier series, for context | v3 80–83%; v4 81.9/82.8 | v3 54–67%; v4 60.9/58.0 | v3 88.0/88.4; v4 88.9/88.0 |
| Av5-vs-Xv5 raw / elim-vs-not | 191/204 = 93.6% / 199/204 | 66/69 = 95.7% / 67/69 | 218/225 = 96.9% / 219/225 |
| prior best pair on the corpus | 92.2% (v4) | 94.2% (v4) | 97.3% (v3 and v4 — stands) |
| anchor-match, outside set | 189/202, 191/202 | 65/68, 66/68 | 211/222, 215/222 |
| role-matched agreement | 185/204, 190/204 | 63/69, 66/69 | 214/225, 213/225 |

## Grades (all clauses fixed at `cf7e219`)

| clause | condition per rater | Av5 | Xv5 |
|---|---|---|---|
| Z2 (TLS) | 67 = TYPESTATE | **PASS** | **PASS** |
| Z4-TLS (TLS) | 156 = DOMAIN | **PASS** | **PASS** |
| Z3 (9001) | 15 = TYPESTATE | **PASS** (torn: `TYPESTATE?`, base label governs) | **PASS** |
| Z5 (iCal) | 192 ∧ 193 ∧ 194 = DOMAIN | **PASS** | **PASS** |
| 23(a) TLS | match ≥ 187/202 | **PASS** — 189 | **PASS** — 191 |
| 23(b) TLS | departures ≤ 12 | **FAIL** — 13 | **PASS** — 11 |
| 23(a) 9001 | match ≥ 65/68 | **PASS** — 65, exactly at the floor | **PASS** — 66 |
| 23(b) 9001 | departures ≤ 6 | **PASS** — 3 | **PASS** — 2 |
| 23(a) iCal | match ≥ 219/222 | **FAIL** — 211 | **FAIL** — 215 |
| 23(b) iCal | departures ≤ 1 | **FAIL** — 11 | **FAIL** — 7 |

**Z4 overall: PASS** — QUIC 191 = PROCESS in both `census/v5-quic/`
raters and TLS 156 = DOMAIN in both raters here; the registration's
iff-condition is met with no residual discretion. Per the
pre-committed interpretation, the five clause-failures grade the v5
rule texts and the author's model of their reach; they license NO
re-rating, NO rewording within v5, and NO change to any earlier
series' number.

## Findings

1. **Every Z prediction in the v5 series has now passed in every
   rater — including the contested bridge.** Z3 predicted TYPESTATE
   for RFC 9001 item 15 against three of its four archived readings,
   resting on rule 20's disclosed extension of rule 18; both raters
   landed TYPESTATE, and the same-family rater landed it TORN
   (`TYPESTATE?`) — the instrument's own uncertainty marker surfacing
   on exactly the item whose bridge the amendment flagged as
   contested. Z5's foreign half was the strongest transmission test
   in the series (mechanically clean pack; six archived foreign
   TYPESTATE readings to overturn) and the foreign rater flipped all
   three items to DOMAIN. Z2 required the same-family rater to flip
   its own family's v4 DOMAIN reading of item 67; it did.

2. **The iCal overreach test fired, on both raters and both clauses —
   and the mechanism is identified: rule 21's branch 1 generalizing
   past its named items.** The registration set iCal's bound at 1
   deliberately; the raters produced 11 and 7 both-anchor departures,
   with a six-item cross-family consensus core — {13, 62, 91, 146,
   150, 210}: four are "Applications MUST ignore/accept
   x-param / iana-token values they don't recognize" duties verbatim
   (13, 91, 146, 210), and the other two are adjacent tolerance
   duties (62: ignore invalid RECUR rule parts; 150: accept values
   of a stated precision) — all six read PROCESS by both v4 anchors
   and DOMAIN by both v5 raters, the reading rule 21's in-grammar
   branch licenses ("a generated binding that does not surface the
   element discharges it"). The same shape drives TLS's drift: the
   shared TLS departures include 14, 18, 64, 84, 141, 191 — "MUST
   ignore unrecognized extensions/records" — read DOMAIN by both v5
   raters against PROCESS-side anchors (item 64's anchors split
   PROCESS/TYPESTATE; the other five are PROCESS/PROCESS). This is the series' recurring
   phenomenon (rule 16 in the v4 completion, rule 17 in the v4 TLS
   pass, rule 21 here): a repaired rule reaches items its author
   never enumerated, cross-family. What is new is that the
   registered tolerances CAUGHT it: the amendment disclosed
   rule-level reach for rules 20 and 22 but NOT rule 21's
   ignore-duty reach on unknown-value handling, so the movement is
   undisclosed reach beyond registered tolerances — **the
   pre-committed verdict is instrument mis-design on the format
   genre**. The v5-iCal shares (93.8/91.1, against 88–89 in every
   earlier series) are quoted ONLY as the size of that defect; the
   v3 and v4 iCal headlines stand untouched. A future v6 owes a
   scope boundary for rule 21's branch 1 (unknown-value tolerance
   duties vs parsing-contract element handling); recorded as a
   docket entry, not adjudicated here.

3. **TLS's one failure is marginal and same-direction.** Av5's 13
   both-anchor departures exceed the bound of 12 by one; Xv5's 11
   pass. The drift direction matches finding 2 (outside-set PROCESS
   13/14 against the anchors' [19–21]; DOMAIN 67/66 against
   [60–61]), and the v5 TLS shares (84.8/84.3) sit above the closed
   v3 band (79.9–82.8) and the v4 series (81.9/82.8) — an
   eliminable-ward drift on unnamed items, within tolerance for one
   rater and one item over for the other. The FAIL stands as graded.

4. **RFC 9001 is the completion's cleanest cell.** Both raters clear
   the floor that NO measured prior rater cleared (65 and 66 vs
   65/68 — Av5 exactly at it), with 3 and 2 departures against a
   bound of 6; pair agreement 95.7% sets the corpus record (prior
   94.2%, v4); and the V5 lifecycle 5/4 split — the v4 amendment's
   signature neither-rater prediction — holds item-for-item in all
   four v4/v5-era raters ({13, 34, 36, 37, 38} TYPESTATE; {14, 18,
   20, 43} PROCESS). Shares 59.4/59.4 sit inside the v4-era band.

5. **Two corpus pair-agreement records; iCal's record survives.**
   TLS 93.6% (prior best 92.2%, v4) and RFC 9001 95.7% (prior 94.2%)
   are new corpus bests, both cross-family; iCal's v5 pair lands at
   96.9%, BELOW the corpus's standing 97.3% record — the two v5
   raters drift from the anchors together (the consensus core) while
   agreeing with each other slightly less than the v3/v4 pairs did.

6. **The liminal pair {43, 79} stabilized for the first time.** All
   four v5-era readings are DOMAIN — including the foreign rater's
   cross-chunk pair (43 in chunk 1, 79 in chunk 2), the geometry
   that split in BOTH prior foreign passes with alternating
   polarity. iCal's 141 and 203 stay closed (PROCESS in all four
   v4/v5-era raters), and 185 stays split exactly along family
   lines (same-family TYPESTATE, foreign DOMAIN — both versions).

7. **Error-sign duty, stated for the record.** The completion's
   drift is uniformly eliminable-ward — TLS +2.9/+1.5 points
   role-matched against the v4 raters (84.8 vs Av4's 81.9; 84.3 vs
   Xv4's 82.8), iCal +4.9/+3.1 on the same role-matched convention
   (93.8 vs 88.9; 91.1 vs 88.0), with the
   9001 cell flat (59.4/59.4 vs 60.9/58.0) — i.e., in the thesis-friendly direction, on
   unnamed items, in both families. That is exactly the situation
   the amendment's direction disclosure and rule 23's registered
   bounds were built for, and the bounds converted it from a silent
   share improvement into five recorded FAILs and a named defect.

## Owed tables

TLS ({22, 65, 67, 123, 156, 175, 184} across Av4, Xv4, Av5, Xv5):

| item | Av4 | Xv4 | Av5 | Xv5 |
|---|---|---|---|---|
| 22 | TYPESTATE | TYPESTATE | TYPESTATE | TYPESTATE |
| 65 | DOMAIN | TYPESTATE | DOMAIN | TYPESTATE |
| 67 | DOMAIN | TYPESTATE | TYPESTATE | TYPESTATE |
| 123 | POLICY | PROCESS | PROCESS | U |
| 156 | DOMAIN | DOMAIN | DOMAIN | DOMAIN |
| 175 | TYPESTATE | TYPESTATE | TYPESTATE | TYPESTATE |
| 184 | DOMAIN | TYPESTATE | DOMAIN | TYPESTATE |

The guard-mass residue {65, 184} splits role-consistently in every
v4/v5-era pass (same-family DOMAIN, foreign TYPESTATE) — a
family-stable boundary, not noise; 123 remains three-way soft. Item
175, the registration's disclosed steer item, reproduced its
unanimous TYPESTATE (an anchor-matching reading that the steer
pointed toward — counted as a match, disclosed as steered).

RFC 9001 ({13, 14, 15, 18, 20, 34, 36, 37, 38, 43}), delivered as a
table per the registration:

| item | A‴ (v3) | B‴ (v3) | Av4 | Xv4 | Av5 | Xv5 |
|---|---|---|---|---|---|---|
| 13 | — | — | TYPESTATE | TYPESTATE | TYPESTATE | TYPESTATE |
| 14 | — | — | PROCESS | PROCESS | PROCESS | PROCESS |
| 15 | PROCESS | DOMAIN | TYPESTATE | PROCESS | TYPESTATE (torn) | TYPESTATE |
| 18 | — | — | PROCESS | PROCESS | PROCESS | PROCESS |
| 20 | — | — | PROCESS | PROCESS | PROCESS | PROCESS |
| 34 | — | — | TYPESTATE | TYPESTATE | TYPESTATE | TYPESTATE |
| 36 | — | — | TYPESTATE | TYPESTATE | TYPESTATE | TYPESTATE |
| 37 | — | — | TYPESTATE | TYPESTATE | TYPESTATE | TYPESTATE |
| 38 | — | — | TYPESTATE | TYPESTATE | TYPESTATE | TYPESTATE |
| 43 | — | — | PROCESS | PROCESS | PROCESS | PROCESS |

**Item 15's four-version history, in full (the registered duty):
PROCESS (A‴, v3) → DOMAIN (B‴, v3) → TYPESTATE (Av4) / PROCESS
(Xv4) → TYPESTATE-torn (Av5) / TYPESTATE (Xv5)** — Z3's prediction
sided with Av4 alone among the four archived readings, and both v5
raters joined it. The predicted +1 eliminable crossing on this
corpus materialized in the foreign seat, exactly as the amendment's
accounting disclosed. (The v3 columns for the other nine items are
omitted as "—" here because the registered table covers the
v4/v5-era raters; the v3 readings of the lifecycle cluster are
archived in `census/quic-tls/rfc9001-census.md`.)

iCal ({43, 79, 141, 185, 192, 193, 194, 203}):

| item | Av4i | Xv4i | Av5 | Xv5 |
|---|---|---|---|---|
| 43 | DOMAIN | DOMAIN | DOMAIN | DOMAIN |
| 79 | DOMAIN | U | DOMAIN | DOMAIN |
| 141 | PROCESS | PROCESS | PROCESS | PROCESS |
| 185 | TYPESTATE | DOMAIN | TYPESTATE | DOMAIN |
| 192 | DOMAIN | TYPESTATE | DOMAIN | DOMAIN |
| 193 | DOMAIN | TYPESTATE | DOMAIN | DOMAIN |
| 194 | DOMAIN | TYPESTATE | DOMAIN | DOMAIN |
| 203 | PROCESS | PROCESS | PROCESS | PROCESS |

## Clause 23(c) — departure lists and per-class deltas (explicit zeros)

TLS Av5 (13): 12, 13, 14, 18, 55, 64, 84, 141, 157, 164, 190, 191,
197. TLS Xv5 (11): 14, 18, 64, 66, 75, 84, 123, 141, 151, 164, 191.
9001 Av5 (3): 25, 45, 46. 9001 Xv5 (2): 25, 58. iCal Av5 (11): 13,
16, 22, 25, 27, 28, 62, 91, 146, 150, 210. iCal Xv5 (7): 13, 62, 91,
116, 146, 150, 210.

Outside-set class counts, each rater vs the anchor pair's [min–max],
all classes including zeros —
TLS Av5: TYPESTATE 104 [104–107], DOMAIN 67 [60–61], PROCESS 13
[19–21], CV 7 [6–6], U 5 [3–3], REVOCABLE 3 [3–3], NEG 2 [2–2],
META 1 [1–1], POLICY 0 [1–1], THRESHOLD 0 [0–0];
TLS Xv5: TYPESTATE 104 [104–107], DOMAIN 66 [60–61], PROCESS 14
[19–21], CV 6 [6–6], U 6 [3–3], REVOCABLE 3 [3–3], NEG 2 [2–2],
META 1 [1–1], POLICY 0 [1–1], THRESHOLD 0 [0–0];
9001 Av5: TYPESTATE 26 [26–27], DOMAIN 14 [13–15], PROCESS 11 [8–9],
THRESHOLD 5 [5–5], META 5 [5–5], NEG 3 [4–4], CV 2 [2–2],
REVOCABLE 1 [1–1], U 1 [2–2], POLICY 0 [0–0];
9001 Xv5: TYPESTATE 27 [26–27], DOMAIN 13 [13–15], PROCESS 10 [8–9],
THRESHOLD 5 [5–5], META 5 [5–5], NEG 3 [4–4], CV 2 [2–2],
REVOCABLE 1 [1–1], U 2 [2–2], POLICY 0 [0–0];
iCal Av5: DOMAIN 207 [195–196], PROCESS 11 [22–22], U 3 [3–5],
TYPESTATE 1 [0–1], all others 0 [0–0];
iCal Xv5: DOMAIN 202 [195–196], PROCESS 16 [22–22], U 4 [3–5],
TYPESTATE 0 [0–1], all others 0 [0–0].
(Reported per clause (c); no pass/fail attaches to these counts.)

## Raw labels (TLS: rater Av5, then rater Xv5 — archived verbatim, torn-flags preserved)

```
1:TYPESTATE 2:TYPESTATE 3:NEGOTIATION 4:TYPESTATE 5:TYPESTATE
6:NEGOTIATION 7:TYPESTATE 8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:DOMAIN
12:TYPESTATE 13:TYPESTATE 14:DOMAIN 15:DOMAIN 16:DOMAIN 17:PROCESS
18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:TYPESTATE 23:UNCLASSIFIED
24:TYPESTATE 25:TYPESTATE 26:DOMAIN 27:DOMAIN 28:DOMAIN 29:PROCESS
30:TYPESTATE 31:TYPESTATE 32:TYPESTATE 33:DOMAIN 34:DOMAIN 35:TYPESTATE
36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE 40:TYPESTATE 41:TYPESTATE
42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE
47:TYPESTATE 48:DOMAIN 49:DOMAIN 50:DOMAIN 51:DOMAIN 52:TYPESTATE
53:PROCESS 54:TYPESTATE 55:UNCLASSIFIED 56:TYPESTATE 57:TYPESTATE
58:DOMAIN 59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE 63:TYPESTATE
64:DOMAIN? 65:DOMAIN 66:DOMAIN? 67:TYPESTATE 68:DOMAIN 69:DOMAIN
70:DOMAIN 71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:PROCESS
77:DOMAIN 78:DOMAIN 79:TYPESTATE 80:TYPESTATE 81:DOMAIN 82:TYPESTATE
83:TYPESTATE 84:DOMAIN 85:DOMAIN 86:DOMAIN 87:TYPESTATE 88:DOMAIN
89:PROCESS 90:DOMAIN 91:UNCLASSIFIED 92:DOMAIN 93:DOMAIN 94:TYPESTATE
95:TYPESTATE 96:TYPESTATE 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE
100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN
106:TYPESTATE 107:DOMAIN 108:TYPESTATE 109:TYPESTATE 110:DOMAIN
111:TYPESTATE 112:REVOCABLE 113:PROCESS 114:TYPESTATE 115:TYPESTATE
116:TYPESTATE 117:META 118:TYPESTATE 119:PROCESS 120:CRYPTO-VERIFY
121:TYPESTATE 122:DOMAIN 123:PROCESS 124:TYPESTATE 125:CRYPTO-VERIFY
126:CRYPTO-VERIFY 127:TYPESTATE 128:TYPESTATE 129:TYPESTATE
130:TYPESTATE 131:DOMAIN 132:DOMAIN 133:REVOCABLE 134:TYPESTATE
135:TYPESTATE 136:DOMAIN 137:TYPESTATE 138:TYPESTATE 139:TYPESTATE
140:DOMAIN 141:DOMAIN 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE
145:TYPESTATE 146:TYPESTATE 147:TYPESTATE 148:TYPESTATE 149:TYPESTATE
150:DOMAIN 151:DOMAIN 152:TYPESTATE 153:DOMAIN 154:DOMAIN 155:DOMAIN
156:DOMAIN 157:UNCLASSIFIED 158:DOMAIN 159:TYPESTATE 160:TYPESTATE
161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:CRYPTO-VERIFY?
165:TYPESTATE 166:TYPESTATE 167:TYPESTATE 168:DOMAIN 169:DOMAIN
170:TYPESTATE 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE
175:TYPESTATE 176:DOMAIN 177:DOMAIN 178:CRYPTO-VERIFY 179:CRYPTO-VERIFY
180:CRYPTO-VERIFY 181:TYPESTATE 182:TYPESTATE 183:TYPESTATE 184:DOMAIN
185:TYPESTATE 186:TYPESTATE 187:PROCESS 188:DOMAIN 189:REVOCABLE
190:TYPESTATE? 191:DOMAIN 192:TYPESTATE 193:TYPESTATE 194:TYPESTATE
195:TYPESTATE 196:TYPESTATE 197:UNCLASSIFIED 198:TYPESTATE 199:TYPESTATE
200:PROCESS 201:DOMAIN 202:TYPESTATE 203:TYPESTATE 204:TYPESTATE
```

```
1:TYPESTATE 2:TYPESTATE 3:NEGOTIATION 4:TYPESTATE 5:TYPESTATE
6:NEGOTIATION 7:TYPESTATE 8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:DOMAIN
12:DOMAIN 13:DOMAIN 14:DOMAIN 15:DOMAIN 16:DOMAIN 17:PROCESS 18:DOMAIN
19:DOMAIN 20:DOMAIN 21:DOMAIN 22:TYPESTATE 23:UNCLASSIFIED 24:TYPESTATE
25:TYPESTATE 26:DOMAIN 27:DOMAIN 28:DOMAIN 29:PROCESS 30:TYPESTATE
31:TYPESTATE 32:TYPESTATE 33:DOMAIN 34:DOMAIN 35:TYPESTATE 36:DOMAIN
37:TYPESTATE 38:PROCESS 39:TYPESTATE 40:TYPESTATE 41:TYPESTATE
42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE
47:TYPESTATE 48:DOMAIN 49:DOMAIN 50:DOMAIN 51:DOMAIN 52:TYPESTATE
53:PROCESS 54:TYPESTATE 55:DOMAIN 56:TYPESTATE 57:TYPESTATE 58:DOMAIN
59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE 63:TYPESTATE 64:DOMAIN
65:TYPESTATE 66:TYPESTATE 67:TYPESTATE 68:DOMAIN 69:DOMAIN 70:DOMAIN
71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:UNCLASSIFIED 76:PROCESS
77:DOMAIN 78:DOMAIN 79:TYPESTATE 80:TYPESTATE 81:DOMAIN 82:TYPESTATE
83:TYPESTATE 84:DOMAIN 85:DOMAIN 86:DOMAIN 87:TYPESTATE 88:DOMAIN
89:PROCESS 90:DOMAIN 91:UNCLASSIFIED 92:DOMAIN 93:DOMAIN 94:TYPESTATE
95:TYPESTATE 96:TYPESTATE 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE
100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN
106:TYPESTATE 107:DOMAIN 108:TYPESTATE 109:TYPESTATE 110:DOMAIN
111:TYPESTATE 112:REVOCABLE 113:PROCESS 114:TYPESTATE 115:TYPESTATE
116:TYPESTATE 117:META 118:TYPESTATE 119:PROCESS 120:CRYPTO-VERIFY
121:TYPESTATE 122:DOMAIN 123:UNCLASSIFIED 124:TYPESTATE
125:CRYPTO-VERIFY 126:CRYPTO-VERIFY 127:TYPESTATE 128:TYPESTATE
129:TYPESTATE 130:TYPESTATE 131:DOMAIN 132:DOMAIN 133:REVOCABLE
134:TYPESTATE 135:TYPESTATE 136:DOMAIN 137:TYPESTATE 138:TYPESTATE
139:TYPESTATE 140:DOMAIN 141:DOMAIN 142:TYPESTATE 143:TYPESTATE
144:TYPESTATE 145:TYPESTATE 146:TYPESTATE 147:TYPESTATE 148:TYPESTATE
149:TYPESTATE 150:DOMAIN 151:PROCESS 152:TYPESTATE 153:DOMAIN 154:DOMAIN
155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:TYPESTATE 160:TYPESTATE
161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:UNCLASSIFIED 165:TYPESTATE
166:TYPESTATE 167:TYPESTATE 168:DOMAIN 169:DOMAIN 170:TYPESTATE
171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE
176:DOMAIN 177:DOMAIN 178:CRYPTO-VERIFY 179:CRYPTO-VERIFY
180:CRYPTO-VERIFY 181:TYPESTATE 182:TYPESTATE 183:TYPESTATE
184:TYPESTATE 185:TYPESTATE 186:TYPESTATE 187:PROCESS 188:DOMAIN
189:REVOCABLE 190:UNCLASSIFIED 191:DOMAIN 192:TYPESTATE 193:TYPESTATE
194:TYPESTATE 195:TYPESTATE 196:TYPESTATE 197:PROCESS 198:TYPESTATE
199:TYPESTATE 200:PROCESS 201:DOMAIN 202:TYPESTATE 203:TYPESTATE
204:TYPESTATE
```

## Raw labels (RFC 9001: rater Av5, then rater Xv5 — archived verbatim, torn-flags preserved)

```
1:TYPESTATE 2:TYPESTATE 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:DOMAIN
7:DOMAIN 8:CRYPTO-VERIFY 9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN
13:TYPESTATE 14:PROCESS 15:TYPESTATE? 16:TYPESTATE 17:TYPESTATE
18:PROCESS 19:TYPESTATE 20:PROCESS 21:REVOCABLE 22:META 23:PROCESS
24:DOMAIN 25:DOMAIN 26:THRESHOLD 27:META 28:DOMAIN 29:TYPESTATE
30:CRYPTO-VERIFY 31:UNCLASSIFIED 32:META 33:TYPESTATE 34:TYPESTATE
35:TYPESTATE 36:TYPESTATE 37:TYPESTATE 38:TYPESTATE 39:DOMAIN 40:DOMAIN
41:TYPESTATE 42:TYPESTATE 43:PROCESS 44:PROCESS 45:PROCESS 46:PROCESS?
47:PROCESS 48:TYPESTATE 49:TYPESTATE 50:PROCESS 51:THRESHOLD
52:THRESHOLD 53:THRESHOLD 54:PROCESS 55:THRESHOLD 56:META 57:META
58:DOMAIN? 59:NEGOTIATION 60:NEGOTIATION 61:TYPESTATE 62:NEGOTIATION
63:TYPESTATE 64:DOMAIN 65:TYPESTATE 66:TYPESTATE 67:DOMAIN 68:DOMAIN
69:DOMAIN
```

```
1:TYPESTATE 2:TYPESTATE 3:TYPESTATE 4:TYPESTATE 5:TYPESTATE 6:DOMAIN
7:DOMAIN 8:CRYPTO-VERIFY 9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN
13:TYPESTATE 14:PROCESS 15:TYPESTATE 16:TYPESTATE 17:TYPESTATE
18:PROCESS 19:TYPESTATE 20:PROCESS 21:REVOCABLE 22:META 23:PROCESS
24:DOMAIN 25:DOMAIN 26:THRESHOLD 27:META 28:DOMAIN 29:TYPESTATE?
30:CRYPTO-VERIFY 31:UNCLASSIFIED? 32:META 33:TYPESTATE 34:TYPESTATE
35:TYPESTATE 36:TYPESTATE 37:TYPESTATE 38:TYPESTATE 39:DOMAIN 40:DOMAIN
41:TYPESTATE 42:TYPESTATE 43:PROCESS 44:PROCESS 45:TYPESTATE
46:UNCLASSIFIED 47:PROCESS 48:TYPESTATE 49:TYPESTATE 50:PROCESS
51:THRESHOLD 52:THRESHOLD 53:THRESHOLD 54:PROCESS 55:THRESHOLD 56:META
57:META 58:PROCESS 59:NEGOTIATION 60:NEGOTIATION 61:TYPESTATE
62:NEGOTIATION 63:TYPESTATE 64:DOMAIN 65:TYPESTATE 66:TYPESTATE
67:DOMAIN 68:DOMAIN 69:DOMAIN
```

## Raw labels (iCalendar: rater Av5, then rater Xv5 — archived verbatim)

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:UNCLASSIFIED
8:DOMAIN 9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:DOMAIN 14:DOMAIN
15:DOMAIN 16:DOMAIN 17:DOMAIN 18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN
22:DOMAIN 23:DOMAIN 24:DOMAIN 25:DOMAIN 26:DOMAIN 27:DOMAIN 28:DOMAIN
29:DOMAIN 30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN 35:DOMAIN
36:DOMAIN 37:PROCESS 38:DOMAIN 39:DOMAIN 40:DOMAIN 41:DOMAIN 42:DOMAIN
43:DOMAIN 44:DOMAIN 45:DOMAIN 46:PROCESS 47:PROCESS 48:DOMAIN 49:DOMAIN
50:DOMAIN 51:DOMAIN 52:DOMAIN 53:DOMAIN 54:DOMAIN 55:DOMAIN 56:DOMAIN
57:DOMAIN 58:DOMAIN 59:DOMAIN 60:DOMAIN 61:DOMAIN 62:DOMAIN 63:DOMAIN
64:DOMAIN 65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:PROCESS 70:DOMAIN
71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:DOMAIN 77:DOMAIN
78:DOMAIN 79:DOMAIN 80:DOMAIN 81:DOMAIN 82:DOMAIN 83:DOMAIN 84:DOMAIN
85:DOMAIN 86:DOMAIN 87:DOMAIN 88:DOMAIN 89:DOMAIN 90:DOMAIN 91:DOMAIN
92:DOMAIN 93:DOMAIN 94:DOMAIN 95:DOMAIN 96:DOMAIN 97:DOMAIN 98:DOMAIN
99:DOMAIN 100:DOMAIN 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN
105:DOMAIN 106:DOMAIN 107:DOMAIN 108:DOMAIN 109:DOMAIN 110:DOMAIN
111:DOMAIN 112:DOMAIN 113:DOMAIN 114:DOMAIN 115:DOMAIN 116:DOMAIN
117:DOMAIN 118:PROCESS 119:DOMAIN 120:DOMAIN 121:DOMAIN 122:DOMAIN
123:DOMAIN 124:DOMAIN 125:DOMAIN 126:DOMAIN 127:DOMAIN 128:DOMAIN
129:DOMAIN 130:DOMAIN 131:DOMAIN 132:DOMAIN 133:DOMAIN 134:DOMAIN
135:DOMAIN 136:DOMAIN 137:DOMAIN 138:PROCESS 139:DOMAIN 140:DOMAIN
141:PROCESS 142:DOMAIN 143:DOMAIN 144:DOMAIN 145:DOMAIN 146:DOMAIN
147:DOMAIN 148:DOMAIN 149:DOMAIN 150:DOMAIN 151:DOMAIN 152:DOMAIN
153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN
159:DOMAIN 160:DOMAIN 161:DOMAIN 162:DOMAIN 163:DOMAIN 164:DOMAIN
165:DOMAIN 166:DOMAIN 167:DOMAIN 168:DOMAIN 169:DOMAIN 170:DOMAIN
171:DOMAIN 172:DOMAIN 173:DOMAIN 174:DOMAIN 175:DOMAIN 176:DOMAIN
177:DOMAIN 178:DOMAIN 179:DOMAIN 180:DOMAIN 181:DOMAIN 182:DOMAIN
183:DOMAIN 184:DOMAIN 185:TYPESTATE 186:DOMAIN 187:DOMAIN 188:DOMAIN
189:DOMAIN 190:DOMAIN 191:DOMAIN 192:DOMAIN 193:DOMAIN 194:DOMAIN
195:DOMAIN 196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN 200:UNCLASSIFIED
201:UNCLASSIFIED 202:DOMAIN 203:PROCESS 204:PROCESS 205:DOMAIN
206:DOMAIN 207:DOMAIN 208:DOMAIN 209:DOMAIN 210:DOMAIN 211:DOMAIN
212:DOMAIN 213:DOMAIN 214:DOMAIN 215:DOMAIN 216:DOMAIN 217:DOMAIN
218:DOMAIN 219:DOMAIN 220:DOMAIN 221:DOMAIN 222:DOMAIN 223:DOMAIN
224:DOMAIN 225:DOMAIN
```

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:UNCLASSIFIED
8:DOMAIN 9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:DOMAIN 14:DOMAIN
15:DOMAIN 16:PROCESS 17:DOMAIN 18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN
22:PROCESS 23:DOMAIN 24:DOMAIN 25:PROCESS 26:DOMAIN 27:PROCESS
28:PROCESS 29:DOMAIN 30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN
35:DOMAIN 36:DOMAIN 37:PROCESS 38:DOMAIN 39:DOMAIN 40:DOMAIN 41:DOMAIN
42:DOMAIN 43:DOMAIN 44:DOMAIN 45:DOMAIN 46:PROCESS 47:PROCESS 48:DOMAIN
49:DOMAIN 50:DOMAIN 51:DOMAIN 52:DOMAIN 53:DOMAIN 54:DOMAIN 55:DOMAIN
56:DOMAIN 57:DOMAIN 58:DOMAIN 59:DOMAIN 60:DOMAIN 61:DOMAIN 62:DOMAIN
63:DOMAIN 64:DOMAIN 65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:PROCESS
70:DOMAIN 71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:DOMAIN
77:DOMAIN 78:DOMAIN 79:DOMAIN 80:DOMAIN 81:DOMAIN 82:DOMAIN 83:DOMAIN
84:DOMAIN 85:DOMAIN 86:DOMAIN 87:DOMAIN 88:DOMAIN 89:DOMAIN 90:DOMAIN
91:DOMAIN 92:DOMAIN 93:DOMAIN 94:DOMAIN 95:DOMAIN 96:DOMAIN 97:DOMAIN
98:DOMAIN 99:DOMAIN 100:DOMAIN 101:DOMAIN 102:DOMAIN 103:DOMAIN
104:DOMAIN 105:DOMAIN 106:DOMAIN 107:DOMAIN 108:DOMAIN 109:DOMAIN
110:DOMAIN 111:DOMAIN 112:DOMAIN 113:DOMAIN 114:DOMAIN 115:DOMAIN
116:UNCLASSIFIED 117:DOMAIN 118:PROCESS 119:DOMAIN 120:DOMAIN 121:DOMAIN
122:DOMAIN 123:DOMAIN 124:DOMAIN 125:DOMAIN 126:DOMAIN 127:DOMAIN
128:DOMAIN 129:DOMAIN 130:DOMAIN 131:DOMAIN 132:DOMAIN 133:DOMAIN
134:DOMAIN 135:DOMAIN 136:DOMAIN 137:DOMAIN 138:PROCESS 139:DOMAIN
140:DOMAIN 141:PROCESS 142:DOMAIN 143:DOMAIN 144:DOMAIN 145:DOMAIN
146:DOMAIN 147:DOMAIN 148:DOMAIN 149:DOMAIN 150:DOMAIN 151:DOMAIN
152:DOMAIN 153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN
158:DOMAIN 159:DOMAIN 160:DOMAIN 161:DOMAIN 162:DOMAIN 163:DOMAIN
164:DOMAIN 165:DOMAIN 166:DOMAIN 167:DOMAIN 168:DOMAIN 169:DOMAIN
170:DOMAIN 171:DOMAIN 172:DOMAIN 173:DOMAIN 174:DOMAIN 175:DOMAIN
176:DOMAIN 177:DOMAIN 178:DOMAIN 179:DOMAIN 180:DOMAIN 181:DOMAIN
182:DOMAIN 183:DOMAIN 184:DOMAIN 185:DOMAIN 186:DOMAIN 187:DOMAIN
188:DOMAIN 189:DOMAIN 190:DOMAIN 191:DOMAIN 192:DOMAIN 193:DOMAIN
194:DOMAIN 195:DOMAIN 196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN
200:UNCLASSIFIED 201:UNCLASSIFIED 202:DOMAIN 203:PROCESS 204:PROCESS
205:DOMAIN 206:DOMAIN 207:DOMAIN 208:DOMAIN 209:DOMAIN 210:DOMAIN
211:DOMAIN 212:DOMAIN 213:DOMAIN 214:DOMAIN 215:DOMAIN 216:DOMAIN
217:DOMAIN 218:DOMAIN 219:DOMAIN 220:DOMAIN 221:DOMAIN 222:DOMAIN
223:DOMAIN 224:DOMAIN 225:DOMAIN
```
