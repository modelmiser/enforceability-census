# First rating pass under instrument v4 — TLS §4 (two blind raters)

2026-08-14 · Companion to `README.md` in this directory (the pre-pass
protocol, pushed at `76ad6c7` before any rater ran) and to the v4 amendment
(`codebook/classes.md`, `d3d4c2d`, which carries predictions V1–V8).
**Status: COMPLETE — grades: V8 PASS in both raters; V6-TLS PASS in both;
V4 FAIL in Av4 (item 67) and PASS in Xv4; V7 FAIL in both raters — clause
(a) passed with room, clause (b) failed on DOMAIN/TYPESTATE counts, and
the failure's anatomy is the pass's most informative result (finding 2).**

## Setup

Exactly as the pre-pass protocol registered; no deviations.

- Instrument: `codebook/rater-pack-v4.md`, blob `4891605…` (v3 pack
  verbatim + v4 rules 15–19 with the one disclosed elision), served blind.
- Corpus: `census/tls13/rfc8446_s4_musts.txt` byte-identical, n = 204.
- Rater Av4: fresh same-family (Claude) instance; its entire input was one
  file holding the pack and the corpus. Per the author's harness usage
  record (an attestation — the transcript is not archived in this
  repository), the rater made exactly two tool calls, both reads of that
  file. NO author pass exists, by design (the author wrote V1–V8).
- Rater Xv4: xAI `cursor-grok-4.6-high-fast` via cursor-cli, four chunks,
  same transport as the cross-family replication.
- **Protocol events: NONE.** All four Xv4 chunks returned exactly 51
  well-formed labels single-shot; Av4 returned exactly 204.

## Results

| | rater Av4 (Claude, fresh) | rater Xv4 (Grok 4.6) |
|---|---|---|
| v4 eliminable share (NEW series — never substitutes the v3 headline) | 167/204 = 81.9% | 169/204 = 82.8% |
| class tally | TYPESTATE 104, DOMAIN 63, PROCESS 21, CV 6, U 3, REVOCABLE 3, NEG 2, META 1, POLICY 1 | TYPESTATE 108, DOMAIN 61, PROCESS 19, CV 6, REVOCABLE 3, U 3, NEG 2, META 1, POLICY 1 |
| raw agreement vs A / vs D (v3 raters, context) | 82.8% / 88.2% | 85.8% / 86.3% |
| CV set {120,125,126,178,179,180} | 6/6, CV class exactly 6 | 6/6, CV class exactly 6 |

**Av4-vs-Xv4: raw 188/204 = 92.2%, eliminable-vs-not 196/204 = 96.1%** —
the highest raw agreement between any two raters on this 204-item corpus
(prior best 91.7%, X-vs-D), and it is a cross-family pair (v3
intra-family raw ran 81–90%). The repository-wide record remains RFC
9002's 96.7% on its 30-item corpus.

## Prediction grades (V4, V6-TLS, V7-TLS, V8 — fixed at `d3d4c2d`)

| # | prediction | outcome |
|---|---|---|
| V4 | nine items {10,52,67,129,130,139,152,159,165} TYPESTATE in every v4 rater; 156 DOMAIN | **FAIL** — Xv4: all nine TYPESTATE ✓ and 156 DOMAIN ✓; Av4: eight of nine ✓ but **67 = DOMAIN**; 156 DOMAIN ✓ in both |
| V6-TLS | {181, 199, 203} TYPESTATE, CV count 0 on them | **PASS** in both raters (181's weight discounted per the pre-pass disclosure — the pack names it; 199 and 203 carry the evidence) |
| V7-TLS (a) | outside-set match rate (vs A-or-D) ≥ 83.8% | **PASS** in both — 178/189 = 94.2% for each rater |
| V7-TLS (b) | outside-set class counts within the A–D spread | **FAIL** in both — DOMAIN 60/59 vs bounds around [71,73]; TYPESTATE 93/96 vs bounds around [82,85]; other classes inside the loose bounds, though Av4's PROCESS (21 vs the pair's [14,19]) sits outside the strict reading (finding 6) |
| V8 | 188 DOMAIN; 189 REVOCABLE | **PASS** in both raters |

Per the amendment's pre-committed interpretation, V4's and V7's failures
grade the rule texts and the author's model of their reach; they license
NO re-rating, NO rewording within v4, and NO change to any v3 number.

## Findings

1. **V8 held, in both families.** Item 188 landed DOMAIN and item 189
   REVOCABLE in both raters — the amendment's disclosed most
   counterintuitive prediction. Under v4, TLS's v3 THRESHOLD class
   ({188, 189} exactly) empties, as pre-registered: 188's spec-fixed
   bound on a field value is carried by the format, and 189's retention
   window is a clock duty. Decision rule 3's worked example flipped
   because the rule that replaced it discriminates on the quantity, not
   the constant's provenance — and two independent raters, one per
   family, executed that flip from the rule text alone.

2. **V7(b)'s failure is the pass's central measurement: rule 17's reach
   extends one full sub-bucket beyond the items the author named.** Both
   raters — independently, across families — moved exactly
   {30, 31, 32, 56, 57} from A/D's DOMAIN to TYPESTATE. Those five are
   the state-conditioned constant-field sub-bucket of the census's
   original 14-item guard-vs-predicate DISAGREE mass
   ("[30,31,32,56,57] A:0 B:3") — the items on which rater B had split
   from A in 2026-08-12's first blind pass. Rule 17's complement-state
   test, written to settle the nine foreign-consensus items, settles
   these five the same way: B's reading, now reproduced by two v4
   raters. V7(b) fails as written because the author's named-set was one
   sub-bucket too narrow, and the grade stands: agreement gains were
   required to concentrate in the named items and did not. The boundary
   as a whole is narrowed, NOT resolved: of the original 14-item mass,
   ten items now sit in v4 rater agreement ({30,31,32,56,57} on B's
   reading; 159, 165, 5, 54 TYPESTATE; 156 DOMAIN), while four —
   65, 67, 123, 184 — remain split between the two v4 raters
   themselves. What the failure measures is stated for the record and
   adjudicates nothing.

3. **V4 missed by exactly the item its history flagged.** Av4 put 67 at
   DOMAIN. Item 67 ("…client has not sent a signature_algorithms
   extension → abort") is the one item of the nine where the complement
   evidence is a *response duty* rather than a value requirement on a
   field — the case rule 17's narrowed evidence source ("value or
   structure," consumer-use duties excluded) deliberately pushes toward
   the silence branch. Xv4 read it TYPESTATE. The nine-item cluster's
   one internal seam was already visible in v3 (67 was A-vs-D split, and
   both foreign raters had sided with A); v4 narrowed but did not close
   it. Interior to the eliminable family either way. For completeness,
   each rater's full outside-set movement beyond BOTH v3 anchors is
   eleven items: Av4 = {22, 30, 31, 32, 33, 34, 56, 57} → TYPESTATE plus
   {55, 157} → PROCESS and 113 → TYPESTATE; Xv4 = {22, 30, 31, 32, 56,
   57, 58, 64, 65, 81} → TYPESTATE plus 123 → PROCESS. Item 22 (A:U,
   D:DOMAIN) moved to TYPESTATE in BOTH raters — a shared unpredicted
   flip off the guard boundary, recorded here rather than absorbed into
   finding 2's story.

4. **The repaired instrument transmits better across families than v3
   transmitted within one.** Av4-vs-Xv4 raw agreement (92.2%) exceeds
   every v3 pair — intra-family (81–90%) and cross-family (81.4%, 91.7%)
   alike — with eliminable-vs-not at 96.1%. Consistent with the series'
   standing law (classes transmit as well as their discriminators are
   crisp: v4 added five discriminators to the softest boundaries), and
   carrying the usual caveat: two raters, one corpus, and the
   corpus-shared-prior confound untouched.

5. **The v4 eliminable shares (81.9% / 82.8%) land within the closed v3
   band (79.9–82.8%) — one mid-band, one exactly at its upper endpoint.**
   (A numerical coincidence worth recording plainly: Av4's eliminable
   count equals rater A's exactly, 167, and Xv4's equals rater D's, 169,
   with different item compositions.) The predicted drift envelope (≤ +1.0 attributable to
   named items) is consistent with what occurred; the unpredicted
   guard-mass movement is interior to the eliminable family and does not
   move the share. The v3 headline (80–83%) stands, per the amendment's
   ring-fence; any quotation of a v4 share must name the instrument
   version.

6. **A V7(b) wording ambiguity was discovered at grading time and is
   recorded, not repaired:** "may differ from the pair's counts … by more
   than that pair's own spread" admits a strict reading (stay within
   [min, max] of the pair) and a loose one ([min − spread, max +
   spread]). Both raters' DOMAIN and TYPESTATE counts fail under BOTH
   readings, so the verdict is unaffected — but the fork is live in this
   very pass: Av4's outside-set PROCESS count (21, vs the pair's
   [14, 19] with spread 5) is inside the loose bound and outside the
   strict one. A v5 should fix the wording.

## Raw labels (rater Av4, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE
8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN
14:PROCESS 15:DOMAIN 16:DOMAIN 17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN
21:DOMAIN 22:TYPESTATE 23:U 24:TYPESTATE 25:TYPESTATE 26:DOMAIN 27:DOMAIN
28:DOMAIN 29:PROCESS 30:TYPESTATE 31:TYPESTATE 32:TYPESTATE 33:TYPESTATE
34:TYPESTATE 35:TYPESTATE 36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE
40:TYPESTATE 41:TYPESTATE 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE
45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:DOMAIN 52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:PROCESS 56:TYPESTATE
57:TYPESTATE 58:DOMAIN 59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE
63:TYPESTATE 64:PROCESS 65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:DOMAIN
70:DOMAIN 71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:PROCESS
77:DOMAIN 78:DOMAIN 79:TYPESTATE 80:TYPESTATE 81:DOMAIN 82:TYPESTATE
83:TYPESTATE 84:PROCESS 85:DOMAIN 86:DOMAIN 87:TYPESTATE 88:DOMAIN
89:PROCESS 90:DOMAIN 91:U 92:DOMAIN 93:DOMAIN 94:TYPESTATE 95:TYPESTATE
96:TYPESTATE 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE 100:TYPESTATE 101:DOMAIN
102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN 106:TYPESTATE 107:DOMAIN
108:TYPESTATE 109:TYPESTATE 110:DOMAIN 111:TYPESTATE 112:REVOCABLE
113:TYPESTATE 114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:META
118:TYPESTATE 119:PROCESS 120:CV 121:TYPESTATE 122:PROCESS 123:POLICY
124:TYPESTATE 125:CV 126:CV 127:TYPESTATE 128:TYPESTATE 129:TYPESTATE
130:TYPESTATE 131:DOMAIN 132:DOMAIN 133:REVOCABLE 134:TYPESTATE
135:TYPESTATE 136:DOMAIN 137:TYPESTATE 138:TYPESTATE 139:TYPESTATE
140:DOMAIN 141:PROCESS 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE
145:TYPESTATE 146:TYPESTATE 147:TYPESTATE 148:TYPESTATE 149:TYPESTATE
150:DOMAIN 151:DOMAIN 152:TYPESTATE 153:DOMAIN 154:DOMAIN 155:DOMAIN
156:DOMAIN 157:PROCESS 158:DOMAIN 159:TYPESTATE 160:TYPESTATE 161:TYPESTATE
162:TYPESTATE 163:TYPESTATE 164:DOMAIN 165:TYPESTATE 166:TYPESTATE
167:TYPESTATE 168:DOMAIN 169:DOMAIN 170:TYPESTATE 171:TYPESTATE
172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:DOMAIN
177:DOMAIN 178:CV 179:CV 180:CV 181:TYPESTATE 182:TYPESTATE 183:TYPESTATE
184:DOMAIN 185:TYPESTATE 186:TYPESTATE 187:PROCESS 188:DOMAIN 189:REVOCABLE
190:U 191:PROCESS 192:TYPESTATE 193:TYPESTATE 194:TYPESTATE 195:TYPESTATE
196:TYPESTATE 197:PROCESS 198:TYPESTATE 199:TYPESTATE 200:PROCESS 201:DOMAIN
202:TYPESTATE 203:TYPESTATE 204:TYPESTATE
```

## Raw labels (rater Xv4, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE
8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN
14:PROCESS 15:DOMAIN 16:DOMAIN 17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN
21:DOMAIN 22:TYPESTATE 23:U 24:TYPESTATE 25:TYPESTATE 26:DOMAIN 27:DOMAIN
28:DOMAIN 29:PROCESS 30:TYPESTATE 31:TYPESTATE 32:TYPESTATE 33:DOMAIN
34:DOMAIN 35:TYPESTATE 36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE
40:TYPESTATE 41:TYPESTATE 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE
45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:DOMAIN 52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:DOMAIN 56:TYPESTATE
57:TYPESTATE 58:TYPESTATE 59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE
63:TYPESTATE 64:TYPESTATE 65:TYPESTATE 66:DOMAIN 67:TYPESTATE 68:DOMAIN
69:DOMAIN 70:DOMAIN 71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:POLICY
76:PROCESS 77:DOMAIN 78:DOMAIN 79:TYPESTATE 80:TYPESTATE 81:TYPESTATE
82:TYPESTATE 83:TYPESTATE 84:PROCESS 85:DOMAIN 86:DOMAIN 87:TYPESTATE
88:DOMAIN 89:PROCESS 90:DOMAIN 91:U 92:DOMAIN 93:DOMAIN 94:TYPESTATE
95:TYPESTATE 96:TYPESTATE 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE
100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN
106:TYPESTATE 107:DOMAIN 108:TYPESTATE 109:TYPESTATE 110:DOMAIN
111:TYPESTATE 112:REVOCABLE 113:PROCESS 114:TYPESTATE 115:TYPESTATE
116:TYPESTATE 117:META 118:TYPESTATE 119:PROCESS 120:CV 121:TYPESTATE
122:DOMAIN 123:PROCESS 124:TYPESTATE 125:CV 126:CV 127:TYPESTATE
128:TYPESTATE 129:TYPESTATE 130:TYPESTATE 131:DOMAIN 132:DOMAIN
133:REVOCABLE 134:TYPESTATE 135:TYPESTATE 136:DOMAIN 137:TYPESTATE
138:TYPESTATE 139:TYPESTATE 140:DOMAIN 141:PROCESS 142:TYPESTATE
143:TYPESTATE 144:TYPESTATE 145:TYPESTATE 146:TYPESTATE 147:TYPESTATE
148:TYPESTATE 149:TYPESTATE 150:DOMAIN 151:DOMAIN 152:TYPESTATE 153:DOMAIN
154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:TYPESTATE
160:TYPESTATE 161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:PROCESS
165:TYPESTATE 166:TYPESTATE 167:TYPESTATE 168:DOMAIN 169:DOMAIN
170:TYPESTATE 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE
175:TYPESTATE 176:DOMAIN 177:DOMAIN 178:CV 179:CV 180:CV 181:TYPESTATE
182:TYPESTATE 183:TYPESTATE 184:TYPESTATE 185:TYPESTATE 186:TYPESTATE
187:PROCESS 188:DOMAIN 189:REVOCABLE 190:U 191:PROCESS 192:TYPESTATE
193:TYPESTATE 194:TYPESTATE 195:TYPESTATE 196:TYPESTATE 197:TYPESTATE
198:TYPESTATE 199:TYPESTATE 200:PROCESS 201:DOMAIN 202:TYPESTATE
203:TYPESTATE 204:TYPESTATE
```
