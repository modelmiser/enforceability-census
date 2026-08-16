# RFC 5545 §3 census — the non-protocol corpus (two blind raters)

2026-08-15 · Companion to `README.md` in this directory (the
pre-registration, pushed at `7b07de3` before any rater ran). **Status:
COMPLETE — grades: N1, N3, N5, N6 PASS in both raters; N2 PASS in Ai
(exactly at the band's inclusive endpoint) and FAIL in Xi (one item
above it); N4 PASS in Ai and FAIL in Xi (one split group, across a
chunk boundary — the cross-context mode the pre-registration stated in
advance, though in a group it did not name).**

## Setup

Exactly as pre-registered; no deviations.

- Instrument: git blob `a08febba22fd2cb117a9be41654a6209e0104e57` (the
  frozen v3 pass-4 pack), extracted via `git cat-file blob` and
  hash-round-trip verified (`git hash-object` reproduces the id),
  served blind.
- Corpus: `rfc5545_s3_musts.txt` byte-identical, n = 225.
- Rater Ai (`claude-fable-5`, per the pre-registered name — the serving
  session's inherited model matched): fresh instance, entire input one
  file (pack + corpus). Per the author's harness usage record (an
  attestation — the transcript is not archived here), the rater made
  exactly ONE tool call, a read of that file.
- Rater Xi (`cursor-grok-4.6-high-fast` via cursor-cli): five chunks
  (51+51+51+51+21).
- **Protocol events: NONE.** All five Xi chunks returned exact
  well-formed counts single-shot, and Ai returned exactly 225 (the
  single-shot claim is likewise an attestation from the run records;
  chunk transcripts are not archived here — what the archives prove is
  225 well-formed in-vocabulary labels per rater).

## Results

| | rater Ai (Claude) | rater Xi (Grok 4.6) |
|---|---|---|
| class tally | DOMAIN 197, PROCESS 22, U 5, TYPESTATE 1 | DOMAIN 195, PROCESS 20, U 5, TYPESTATE 4, POLICY 1 |
| per-item eliminable (headline, n = 225) | 198/225 = **88.0%** | 199/225 = **88.4%** |
| unique-text eliminable (secondary, n = 177) | 152/177 = 85.9% | [152, 153]/177 = 85.9–86.4% (range per the pre-registered split-group rule) |
| THRESHOLD / REVOCABLE / CV / NEG / META | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 |

**Ai-vs-Xi: raw 219/225 = 97.3%, eliminable-vs-not 224/225 = 99.6%** —
the highest raw inter-rater agreement recorded in this repository
(prior best: 96.7%, RFC 9002, n = 30, a same-family pair; this pair is
cross-family at n = 225). The comparison to earlier censuses is
instrument-matched but rater-model-unmatched, per the pre-registration,
and the corpus-shared-prior caveat (paper limitation 6) applies at full
force to agreement this high.

## Prediction grades (fixed at `7b07de3`)

| # | prediction | outcome |
|---|---|---|
| N1 | DOMAIN strictly largest, both raters | **PASS** in both — 197 and 195 against next-largest 22 and 20 |
| N2 | per-item share in [72%, 88%] inclusive, both raters | **PASS in Ai** — 198/225 = 88.0%, exactly the inclusive upper endpoint; **FAIL in Xi** — 199/225 = 88.4%, one item above the bound |
| N3 | CV = 0 and NEG = 0, both raters | **PASS** in both — the format genre carries no secret-material or intersection duties, as predicted |
| N4 | zero intra-group splits across the 14 duplicate-text groups | **PASS in Ai** (0/14, including the ×20 cardinality group); **FAIL in Xi** — one group split: items {43, 79} ("To properly communicate a fixed time…") labeled U in chunk 1 and DOMAIN in chunk 2 |
| N5 | REVOCABLE ≤ 2 per rater | **PASS** in both — 0 and 0 |
| N6 | raw agreement ≥ 192/225 | **PASS** — 219/225 = 97.3% |

Per the pre-registration's scoped failure clause: N2's failure grades
the author's model of the format genre (the band was one item too low
for the foreign rater); N4's failure grades the instrument and is
reported as an instrument finding (finding 4). Neither licenses
re-rating, exclusion, rewording, or quote discretion.

## Findings

1. **The first non-protocol point lands ABOVE every protocol span.**
   88.0%/88.4% type-eliminable, against 80–83% (TLS §4) at the top of
   the protocol range. The v3-instrument spectrum now reads: 23.3%
   (loss-recovery procedure) → ≈57% (group crypto) → ≈67–69%
   (transport) → 80–83% (handshake) → **≈88% (data format)** (RFC
   9001's 54–67% shell overlaps the middle, per the paper's convention)
   — still a
   description, not a law, and the new point is rater-model-unmatched
   with the old ones. The composition is the legible part: DOMAIN alone
   is ~87% of the corpus, and TYPESTATE — the largest class of TLS,
   QUIC, and RFC 9001 — collapses to 1 (Ai) / 4 (Xi) items. A format
   has no counterparty and no message order to discipline; what remains
   of ordering is exactly the span's one scheduling-flavored duty
   (item 185, delegation inheritance — TYPESTATE in both raters). Part
   of the cause is boundary, not just genre, per the pre-registration:
   the iTIP scheduling protocol is a separate RFC whose duties are
   document-censored out of this corpus, and obligations the format
   states as pure grammar are invisible to a MUST census (rule-7
   censoring at genre level). Within what the span does state,
   *what a span states as obligations determines the mix* survives its
   first change of genre.
2. **Crisp genre, record raw agreement.** 97.3% raw / 99.6% at claim
   granularity, cross-family (the claim-granularity record remains
   RFC 9002's 100% on its 30-item corpus). Consistent with the series' standing law
   (classes transmit as well as their discriminators are crisp — DOMAIN
   has the most mechanical discriminator, and this corpus is ~87%
   DOMAIN), with the same confound RFC 9002 carries: a crisp genre and
   shared training priors push the same direction, and nothing here
   separates them.
3. **N2 failed by exactly one item — after passing by exactly zero.**
   Ai landed on the band's inclusive upper endpoint (198 = 0.88 × 225);
   Xi exceeded it by one item. The author's model was right about the
   direction (high) and wrong about the ceiling; graded FAIL per the
   pre-commitment. Recorded plainly: had the pre-registration's bounds
   been exclusive rather than inclusive (a wording choice fixed at the
   pre-push gate, before any rater), BOTH raters would have failed N2.
4. **The determinism probe measured what it was built to measure.** Ai:
   identical text → identical label, 14/14 groups, including all twenty
   "The following are OPTIONAL, but MUST NOT occur more than once."
   items. Xi: one split, and it is exactly the cross-context case the
   pre-registration flagged as harder — items 43 and 79 sit in
   different chunks (fresh process each), and drew U then DOMAIN —
   the cross-context mode the pre-registration flagged via the ×20
   group (which itself passed, spanning chunks 2–5); the split landed
   in a cross-chunk group the pre-registration did not name.
   Notably Ai put BOTH at U: the item is genuinely soft (a
   how-to-communicate duty with an either/or form), so Xi's split sits
   on a real boundary, in different contexts, rather than being pure
   noise. Within-context determinism: unbroken in both raters.
5. **THRESHOLD is zero in both raters — the spec-fixed-constant edge
   did not fire.** The 46 cardinality items ("MUST NOT occur more than
   once") went DOMAIN unanimously in both raters, and even the 255-octet
   persistence floor (item 203) drew PROCESS/POLICY, not THRESHOLD.
   [CORRECTION 2026-08-15, found at the paper-integration gate: the
   count is 45, not 46 — items containing the literal duty "MUST NOT
   occur more than once" number 45; the 46 came from a gate reviewer's
   looser phrase count that included item 108, whose "more than once"
   is a MAY-permission, and was adopted here without independent
   recomputation. All 45 are DOMAIN in both raters (as are items 108
   and 211, the two loose-phrase extras), so the unanimity verdict is
   unchanged.] On
   QUIC, spec-fixed constants produced a THRESHOLD symmetric difference
   of 15 under this same v3 instrument; on the format genre the same
   instrument shows none of that wobble — counts and bounds on the
   datum at hand read as structure without needing v4's rule 16.
   (Same instrument, different rater models — the confound is named in
   the pre-registration; a v4 replication could separate genre from
   rule repair.)
6. **The six raw disagreements, in full:** 79 (U vs DOMAIN — the N4
   split's second half; the corpus's ONE claim-granularity
   disagreement); 141 (PROCESS vs U — "a scheduling transaction MUST
   NOT be assumed"); 192, 193, 194 (DOMAIN vs TYPESTATE — the
   value-type-of-"DTSTART" consistency cluster, where a format duty
   references another property's state; interior to the eliminable
   family); 203 (PROCESS vs POLICY). The 192–194 cluster is the
   genre's one recurring soft boundary: cross-property consistency
   *inside* one object — the within-object shadow of the
   cross-message-consistency reading that rule 1 gives protocols.

## Raw labels (rater Ai, archived verbatim)

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:U 8:DOMAIN
9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:PROCESS 14:DOMAIN 15:DOMAIN
16:PROCESS 17:DOMAIN 18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:PROCESS
23:DOMAIN 24:DOMAIN 25:PROCESS 26:DOMAIN 27:PROCESS 28:PROCESS 29:DOMAIN
30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN 35:DOMAIN 36:DOMAIN
37:PROCESS 38:DOMAIN 39:DOMAIN 40:DOMAIN 41:DOMAIN 42:DOMAIN 43:U
44:DOMAIN 45:DOMAIN 46:PROCESS 47:PROCESS 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:DOMAIN 52:DOMAIN 53:DOMAIN 54:DOMAIN 55:DOMAIN 56:DOMAIN 57:DOMAIN
58:DOMAIN 59:DOMAIN 60:DOMAIN 61:DOMAIN 62:PROCESS 63:DOMAIN 64:DOMAIN
65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:PROCESS 70:DOMAIN 71:DOMAIN
72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:DOMAIN 77:DOMAIN 78:DOMAIN
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
184:DOMAIN 185:TYPESTATE 186:DOMAIN 187:DOMAIN 188:DOMAIN 189:DOMAIN
190:DOMAIN 191:DOMAIN 192:DOMAIN 193:DOMAIN 194:DOMAIN 195:DOMAIN
196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN 200:U 201:U 202:DOMAIN
203:PROCESS 204:PROCESS 205:DOMAIN 206:DOMAIN 207:DOMAIN 208:DOMAIN
209:DOMAIN 210:PROCESS 211:DOMAIN 212:DOMAIN 213:DOMAIN 214:DOMAIN
215:DOMAIN 216:DOMAIN 217:DOMAIN 218:DOMAIN 219:DOMAIN 220:DOMAIN
221:DOMAIN 222:DOMAIN 223:DOMAIN 224:DOMAIN 225:DOMAIN
```

## Raw labels (rater Xi, archived verbatim)

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:U 8:DOMAIN
9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:PROCESS 14:DOMAIN 15:DOMAIN
16:PROCESS 17:DOMAIN 18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:PROCESS
23:DOMAIN 24:DOMAIN 25:PROCESS 26:DOMAIN 27:PROCESS 28:PROCESS 29:DOMAIN
30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN 35:DOMAIN 36:DOMAIN
37:PROCESS 38:DOMAIN 39:DOMAIN 40:DOMAIN 41:DOMAIN 42:DOMAIN 43:U
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
136:DOMAIN 137:DOMAIN 138:PROCESS 139:DOMAIN 140:DOMAIN 141:U
142:DOMAIN 143:DOMAIN 144:DOMAIN 145:DOMAIN 146:PROCESS 147:DOMAIN
148:DOMAIN 149:DOMAIN 150:PROCESS 151:DOMAIN 152:DOMAIN 153:DOMAIN
154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:DOMAIN
160:DOMAIN 161:DOMAIN 162:DOMAIN 163:DOMAIN 164:DOMAIN 165:DOMAIN
166:DOMAIN 167:DOMAIN 168:DOMAIN 169:DOMAIN 170:DOMAIN 171:DOMAIN
172:DOMAIN 173:DOMAIN 174:DOMAIN 175:DOMAIN 176:DOMAIN 177:DOMAIN
178:DOMAIN 179:DOMAIN 180:DOMAIN 181:DOMAIN 182:DOMAIN 183:DOMAIN
184:DOMAIN 185:TYPESTATE 186:DOMAIN 187:DOMAIN 188:DOMAIN 189:DOMAIN
190:DOMAIN 191:DOMAIN 192:TYPESTATE 193:TYPESTATE 194:TYPESTATE
195:DOMAIN 196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN 200:U 201:U
202:DOMAIN 203:POLICY 204:PROCESS 205:DOMAIN 206:DOMAIN 207:DOMAIN
208:DOMAIN 209:DOMAIN 210:PROCESS 211:DOMAIN 212:DOMAIN 213:DOMAIN
214:DOMAIN 215:DOMAIN 216:DOMAIN 217:DOMAIN 218:DOMAIN 219:DOMAIN
220:DOMAIN 221:DOMAIN 222:DOMAIN 223:DOMAIN 224:DOMAIN 225:DOMAIN
```
