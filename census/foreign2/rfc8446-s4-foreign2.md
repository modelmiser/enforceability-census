# RFC 8446 §4 — second cross-family replication: three new families (2026-08-16)

Registration: `census/foreign2/README.md`, pushed at `7d5d5a8` before
any of the three seated models had seen the instrument or the corpus.
Served exactly as registered: frozen corpus (n = 204), frozen v3
pass-4 pack (blob `a08febba…`, hash-round-trip verified at serve
time), four pinned chunks, fresh process per chunk, blind.

**Raters:** M = `gemini-3.1-pro` (Google), K = `kimi-k3-max`
(Moonshot), Z = `glm-5.2-high` (Zhipu), via `cursor-agent`
2026.08.11-e8db854, `--print --output-format text --mode ask --trust`.

**Protocol events: ONE, disclosed.** Rater Z's chunk 3 emitted item
112 twice with the SAME label (`REVOCABLE`, `REVOCABLE`) — akin to
the doubled emission recorded at QUIC chunk 6 (there a full-chunk
re-emission; here a single item); no label ambiguous, deduplicated
mechanically, the format-only retry was not exercised. All other eleven chunk calls
returned exactly 51 well-formed labels on the first attempt. No
missing, out-of-range, conflicting, or invalid labels from any
rater; zero torn flags from all three raters; no item scored U by
the malformed-label rule.

## Grades (F6–F10)

| clause | M (Gemini) | K (Kimi) | Z (GLM) | verdict |
|---|---|---|---|---|
| F6 — quotient in 76–86% | 161/204 = 78.9% | 161/204 = 78.9% | 157/204 = 77.0% | **PASS** ×3 |
| F7 — CV core 6/6 | 6/6 | 6/6 | 6/6 | **PASS** ×3 |
| F8 — raw vs D ≥ 143 | 175 | 184 | 170 | **PASS** ×3 |
| F9 — ≥1 rater ≥ 166 vs D | 175 | 184 | 170 | **PASS** — all three, not just one |
| F10 — TS cluster ≥ 6/9 each | 7/9 | **1/9** | 7/9 | **FAIL** (rater K) |

Four of five clauses pass; F10 fails, and per the registration its
failure grades the author's family-generality model — it licenses
nothing about rater D, the census, or any instrument grade.

## Results

| | M (Gemini) | K (Kimi) | Z (GLM) |
|---|---|---|---|
| eliminable in shape (DOMAIN+TYPESTATE) | 161/204 = 78.9% | 161/204 = 78.9% | 157/204 = 77.0% |
| vs D: raw / eliminable-vs-not | 175 / 190 | 184 / 194 | 170 / 188 |
| vs A: raw / eliminable-vs-not | 172 / 184 | 161 / 178 | 173 / 186 |
| CV: core / extensions | 6/6 / {111} | 6/6 / {111, 181, 199, 203} | 6/6 / — |
| TS cluster (of 9) | 7 (dep {129, 130}) | 1 (kept only 10) | 7 (dep {159, 165}) |
| →U cluster {187, 190, 197} | PROCESS, U, U | PROCESS, U, PROCESS | U, U, POLICY |

Per-class distributions (G and X quoted for comparison — G's
U-inflation, 18 items, was the first replication's mechanism
finding; none of the three new raters reproduces it):

| class | M | K | Z | G | X |
|---|---|---|---|---|---|
| TYPESTATE | 90 | 74 | 93 | 92 | 96 |
| DOMAIN | 71 | 87 | 64 | 64 | 69 |
| PROCESS | 20 | 23 | 21 | 14 | 19 |
| U | 8 | 3 | 8 | 18 | 5 |
| CV | 7 | 10 | 6 | 9 | 6 |
| NEG | 3 | 2 | 3 | 2 | 2 |
| REVOCABLE | 3 | 2 | 2 | 2 | 2 |
| THRESHOLD | 1 | 2 | 2 | 2 | 2 |
| POLICY | 0 | 0 | 4 | 0 | 2 |
| META | 1 | 1 | 1 | 1 | 1 |

Pairwise raw / eliminable-vs-not agreements, all ten foreign–foreign
pairs (of 204):

| | K | Z | G | X |
|---|---|---|---|---|
| **M** | 168 / 186 | 163 / 184 | 171 / 191 | 180 / 192 |
| **K** | | 163 / 186 | 164 / 193 | 175 / 196 |
| **Z** | | | 164 / 183 | 180 / 192 |
| **G** | | | | 176 / 191 |

## Findings

1. **The band holds in three more families — and the foreign
   quotients cluster low.** All three land inside F6's 76–86% band,
   at 77.0–78.9%. The five foreign quotients ever measured now span
   76.5–80.9% (G, Z, M, K, X in order); four of the five sit BELOW
   the lowest Claude quotient (79.9%), with only X inside the Claude
   band. Reported, not graded: a family-level tendency toward
   slightly lower eliminable shares. The mechanism differs by
   rater (decomposed against D's map): M's out-flow from
   D-eliminable items is PROCESS 5 / U 4 / CV 1 / NEG 1 and Z's is
   PROCESS 7 / U 3 / POLICY 3 / NEG 1 — non-eliminable-ward — but
   four of the nine in K's (CV 4 / PROCESS 4 / U 1) are its CV
   extensions, a class-boundary reading, not a refusal.
2. **The CV core is now 15-for-15 across six families.** All six
   CV-set items kept CV in every rater ever run on this corpus —
   twelve prior raters (rater B's 6/6 by the documented inference,
   limitation 7) plus M, K, Z — across six model families and
   every instrument version. And the *penumbra* reproduces too:
   K's four extensions {111, 181, 199, 203} are exactly G's three
   {181, 199, 203} plus M's one {111} — independent families extend
   the class at the same items, never shrink it.
3. **F9 passed maximally — the author's existential model was again
   too weak.** The clause predicted at least ONE family reaching
   166; all three did (175/184/170). This repeats the F2 pattern
   from the first replication: predicted cross-family degradation
   keeps failing to appear. Ten of ten foreign–foreign pairs sit at
   163–180 raw (79.9–88.2%), at or just below the 81–90%
   intra-family span (four pairs sit below its floor; none above
   its ceiling).
4. **F10 FAILS: the candidate-rule-17 reading is not
   seat-general.** Kimi read eight of the nine negotiated-state
   cluster items DOMAIN — siding with rater D's archived reading
   against the G=X foreign consensus — while Gemini (7/9) and GLM
   (7/9) sided with the consensus, each with different departures
   ({129, 130} vs {159, 165}; item 10 is TYPESTATE in all five
   foreign raters). Seat tally: of the five foreign seats, four
   side with the TYPESTATE consensus and one (Kimi) with D. And D
   itself is the Anthropic OUTLIER on this cluster, not the
   family: the other archived same-family readings are
   TYPESTATE-majority (A 8/9 by its per-class rosters, C 7/9,
   Av4 8/9, Av5 9/9, Av6 9/9) — per the registration's own rule,
   a rater is one sample of a family, and no family-level tally is
   made here. The pre-commitment stands: F10's failure grades the
   author's generality model, and the rule-17 docket entry gains
   the split's structure — the boundary is real, contested both
   across seats and within the Anthropic archive (xAI's four
   archived readings are essentially uncontested at 8–9 of 9), and
   no side owns it.
5. **Item 190 drew U from all five foreign raters — and splits the
   same-family archive.** The →U cluster's middle item
   (fresh-ticket-value generation) is U in G, X, M, K, and Z, and
   in author-rater A (roster) — but D, Av5 (torn), and Av6
   archived it TYPESTATE, a split the first replication's report
   already recorded. 187 and 197 scatter across PROCESS/U/POLICY.
   The rule-11 wire-falsifiability boundary drew the same refusal
   from every foreign family; the same-family record shows the
   refusal is not universal.

**Interpretation, restated from the registration:** family-bias
evidence only; one rater per family; no number here joins,
replaces, or requalifies any census figure. The corpus-shared-prior
half of limitation 6 is untouched by construction — these are all
LLMs — and the registered human pass remains its probe.

## Raw labels (rater M, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE 8:TYPESTATE
9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN 14:PROCESS 15:DOMAIN 16:DOMAIN
17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:DOMAIN 23:U 24:TYPESTATE
25:TYPESTATE 26:DOMAIN 27:DOMAIN 28:DOMAIN 29:PROCESS 30:DOMAIN 31:DOMAIN 32:DOMAIN
33:DOMAIN 34:DOMAIN 35:TYPESTATE 36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE 40:TYPESTATE
41:TYPESTATE 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:DOMAIN
49:DOMAIN 50:DOMAIN 51:DOMAIN 52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:PROCESS 56:DOMAIN
57:DOMAIN 58:DOMAIN 59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE 63:TYPESTATE 64:PROCESS
65:TYPESTATE 66:U 67:TYPESTATE 68:DOMAIN 69:DOMAIN 70:DOMAIN 71:DOMAIN 72:DOMAIN
73:DOMAIN 74:DOMAIN 75:U 76:U 77:DOMAIN 78:DOMAIN 79:PROCESS 80:PROCESS
81:DOMAIN 82:TYPESTATE 83:TYPESTATE 84:PROCESS 85:DOMAIN 86:DOMAIN 87:TYPESTATE 88:DOMAIN
89:PROCESS 90:DOMAIN 91:U 92:DOMAIN 93:DOMAIN 94:PROCESS 95:TYPESTATE 96:TYPESTATE
97:TYPESTATE 98:TYPESTATE 99:PROCESS 100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN
105:DOMAIN 106:TYPESTATE 107:DOMAIN 108:DOMAIN 109:DOMAIN 110:DOMAIN 111:CV 112:REVOCABLE
113:TYPESTATE 114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:META 118:TYPESTATE 119:PROCESS 120:CV
121:TYPESTATE 122:PROCESS 123:U 124:NEG 125:CV 126:CV 127:TYPESTATE 128:TYPESTATE
129:DOMAIN 130:DOMAIN 131:DOMAIN 132:DOMAIN 133:REVOCABLE 134:TYPESTATE 135:TYPESTATE 136:DOMAIN
137:TYPESTATE 138:TYPESTATE 139:TYPESTATE 140:DOMAIN 141:PROCESS 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE
145:TYPESTATE 146:TYPESTATE 147:TYPESTATE 148:TYPESTATE 149:TYPESTATE 150:DOMAIN 151:DOMAIN 152:TYPESTATE
153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN 158:DOMAIN 159:TYPESTATE 160:TYPESTATE
161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:DOMAIN 165:TYPESTATE 166:TYPESTATE 167:TYPESTATE 168:DOMAIN
169:DOMAIN 170:TYPESTATE 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:DOMAIN
177:DOMAIN 178:CV 179:CV 180:CV 181:TYPESTATE 182:TYPESTATE 183:TYPESTATE 184:TYPESTATE
185:TYPESTATE 186:TYPESTATE 187:PROCESS 188:THRESHOLD 189:REVOCABLE 190:U 191:DOMAIN 192:TYPESTATE
193:TYPESTATE 194:TYPESTATE 195:TYPESTATE 196:TYPESTATE 197:U 198:TYPESTATE 199:TYPESTATE 200:TYPESTATE
201:DOMAIN 202:TYPESTATE 203:TYPESTATE 204:TYPESTATE
```

## Raw labels (rater K, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE 8:TYPESTATE
9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN 14:PROCESS 15:DOMAIN 16:DOMAIN
17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:DOMAIN 23:U 24:TYPESTATE
25:TYPESTATE 26:DOMAIN 27:DOMAIN 28:DOMAIN 29:PROCESS 30:DOMAIN 31:DOMAIN 32:DOMAIN
33:DOMAIN 34:DOMAIN 35:TYPESTATE 36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE 40:TYPESTATE
41:PROCESS 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:DOMAIN
49:DOMAIN 50:DOMAIN 51:DOMAIN 52:DOMAIN 53:PROCESS 54:TYPESTATE 55:DOMAIN 56:DOMAIN
57:DOMAIN 58:DOMAIN 59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE 63:DOMAIN 64:PROCESS
65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:DOMAIN 70:DOMAIN 71:DOMAIN 72:DOMAIN
73:DOMAIN 74:DOMAIN 75:DOMAIN 76:PROCESS 77:DOMAIN 78:DOMAIN 79:TYPESTATE 80:DOMAIN
81:DOMAIN 82:TYPESTATE 83:TYPESTATE 84:PROCESS 85:DOMAIN 86:DOMAIN 87:TYPESTATE 88:DOMAIN
89:PROCESS 90:DOMAIN 91:U 92:DOMAIN 93:DOMAIN 94:TYPESTATE 95:TYPESTATE 96:TYPESTATE
97:TYPESTATE 98:TYPESTATE 99:TYPESTATE 100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN
105:DOMAIN 106:TYPESTATE 107:DOMAIN 108:DOMAIN 109:DOMAIN 110:DOMAIN 111:CV 112:REVOCABLE
113:PROCESS 114:DOMAIN 115:DOMAIN 116:TYPESTATE 117:META 118:DOMAIN 119:PROCESS 120:CV
121:TYPESTATE 122:DOMAIN 123:PROCESS 124:TYPESTATE 125:CV 126:CV 127:TYPESTATE 128:TYPESTATE
129:DOMAIN 130:DOMAIN 131:DOMAIN 132:DOMAIN 133:REVOCABLE 134:TYPESTATE 135:TYPESTATE 136:DOMAIN
137:TYPESTATE 138:TYPESTATE 139:DOMAIN 140:DOMAIN 141:PROCESS 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE
145:DOMAIN 146:TYPESTATE 147:DOMAIN 148:TYPESTATE 149:TYPESTATE 150:DOMAIN 151:PROCESS 152:DOMAIN
153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:PROCESS 158:DOMAIN 159:DOMAIN 160:TYPESTATE
161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:DOMAIN 165:DOMAIN 166:TYPESTATE 167:TYPESTATE 168:DOMAIN
169:DOMAIN 170:TYPESTATE 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:DOMAIN
177:DOMAIN 178:CV 179:CV 180:CV 181:CV 182:TYPESTATE 183:TYPESTATE 184:DOMAIN
185:TYPESTATE 186:TYPESTATE 187:PROCESS 188:THRESHOLD 189:THRESHOLD 190:U 191:PROCESS 192:TYPESTATE
193:TYPESTATE 194:TYPESTATE 195:TYPESTATE 196:TYPESTATE 197:PROCESS 198:TYPESTATE 199:CV 200:PROCESS
201:DOMAIN 202:TYPESTATE 203:CV 204:TYPESTATE
```

## Raw labels (rater Z, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE 8:TYPESTATE
9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN 14:PROCESS 15:DOMAIN 16:DOMAIN
17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN 21:DOMAIN 22:U 23:U 24:TYPESTATE
25:TYPESTATE 26:DOMAIN 27:POLICY 28:DOMAIN 29:PROCESS 30:PROCESS 31:DOMAIN 32:DOMAIN
33:DOMAIN 34:DOMAIN 35:TYPESTATE 36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE 40:TYPESTATE
41:PROCESS 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:TYPESTATE
49:DOMAIN 50:DOMAIN 51:U 52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:PROCESS 56:TYPESTATE
57:TYPESTATE 58:DOMAIN 59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE 63:TYPESTATE 64:PROCESS
65:DOMAIN 66:DOMAIN 67:TYPESTATE 68:DOMAIN 69:DOMAIN 70:DOMAIN 71:DOMAIN 72:DOMAIN
73:DOMAIN 74:DOMAIN 75:POLICY 76:POLICY 77:DOMAIN 78:DOMAIN 79:TYPESTATE 80:TYPESTATE
81:TYPESTATE 82:TYPESTATE 83:TYPESTATE 84:PROCESS 85:DOMAIN 86:DOMAIN 87:TYPESTATE 88:DOMAIN
89:TYPESTATE 90:DOMAIN 91:U 92:DOMAIN 93:DOMAIN 94:TYPESTATE 95:TYPESTATE 96:TYPESTATE
97:TYPESTATE 98:TYPESTATE 99:TYPESTATE 100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN
105:DOMAIN 106:TYPESTATE 107:DOMAIN 108:TYPESTATE 109:TYPESTATE 110:DOMAIN 111:TYPESTATE 112:REVOCABLE
113:PROCESS 114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:META 118:PROCESS 119:PROCESS 120:CV
121:TYPESTATE 122:U 123:DOMAIN 124:NEG 125:CV 126:CV 127:TYPESTATE 128:TYPESTATE
129:TYPESTATE 130:TYPESTATE 131:DOMAIN 132:DOMAIN 133:REVOCABLE 134:PROCESS 135:TYPESTATE 136:DOMAIN
137:TYPESTATE 138:TYPESTATE 139:TYPESTATE 140:DOMAIN 141:U 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE
145:TYPESTATE 146:DOMAIN 147:DOMAIN 148:TYPESTATE 149:TYPESTATE 150:DOMAIN 151:DOMAIN 152:TYPESTATE
153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:PROCESS 158:DOMAIN 159:DOMAIN 160:TYPESTATE
161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:PROCESS 165:DOMAIN 166:TYPESTATE 167:TYPESTATE 168:DOMAIN
169:DOMAIN 170:TYPESTATE 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:DOMAIN
177:DOMAIN 178:CV 179:CV 180:CV 181:TYPESTATE 182:TYPESTATE 183:TYPESTATE 184:TYPESTATE
185:TYPESTATE 186:TYPESTATE 187:U 188:THRESHOLD 189:THRESHOLD 190:U 191:PROCESS 192:TYPESTATE
193:TYPESTATE 194:TYPESTATE 195:TYPESTATE 196:TYPESTATE 197:POLICY 198:TYPESTATE 199:TYPESTATE 200:PROCESS
201:DOMAIN 202:TYPESTATE 203:DOMAIN 204:TYPESTATE
```
