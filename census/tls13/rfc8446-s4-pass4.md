# RFC 8446 §4 — fourth rating pass (2026-08-13): 1/4 predictions pass; STOP verdict per pre-registration

Fresh blind rater (D), instrument = `codebook/rater-pack.md` **verbatim**
(git blob `a08febba22fd2cb117a9be41654a6209e0104e57`; md5 of the copy served
to the rater verified identical), corpus = the same 204 sentences. Scored
against rater A (full map) and B (184 shared + 16 recorded labels).

## Scores

| measure | D | baseline |
|---|---|---|
| vs A raw | 171/204 = 83.8% | A-vs-B 90.2% |
| vs A eliminable-vs-not | 182/204 = 89.2% | A-vs-B 96.1% |
| on the 184 previously-agreed | 159/184 = 86.4% | — |
| headline eliminable | 169/204 = **82.8%** | A 81.9 / B 79.9 |
| class tallies | 88 TYPESTATE, 81 DOMAIN, 19 PROCESS, 6 CV, 2 each NEG/U/REVOCABLE/THRESHOLD, 1 each POLICY/META | — |

## Pre-registered prediction outcomes (codebook v3)

| # | prediction | outcome |
|---|---|---|
| P1 | NEG returns to single digits; the 16 collision items land TYPESTATE | **PASS** — NEG = 2 ({3, 6}); all 16 collision items TYPESTATE. The rule-12 litmus also moved A's own item 124 (NEG → TYPESTATE), a legitimate application, not a leak. |
| P2 | 184-item agreement recovers to ≥ 90% | **FAIL** — 86.4% |
| P3 | headline inside 80–82% | **FAIL** — 82.8% (+0.8 above the band) |
| P4 | rule-10 pattern from pass 3 reproduces | **FAIL** — items 159 and 165 flipped (C: TYPESTATE, D: DOMAIN); D sided with rater B on all five A:TYPESTATE/B:DOMAIN guard items |

Codebook v3 pre-committed the interpretation: *"Any of these failing means
the codebook is still not transmissible by text alone — that verdict, not a
new headline, would be the result."* That is the verdict. **No pass 5:**
each further rule would be fitted to this corpus's residuals — instrument
overfitting with a growing risk of tuning the codebook to a desired number.

## What is now measured (the stable findings)

1. **Discriminator-bearing classes are perfectly transmissible.** CV
   ({120, 125, 126, 178, 179, 180}), THRESHOLD ({188, 189}), REVOCABLE
   ({112, 133}), and META ({117}) are **item-for-item identical across every
   rater, including the invalid-instrument pass 3**. The crypto core is
   exactly 6/204 = 2.9%, with zero rater variance.
2. **The headline is robust at claim granularity.** Valid raters: A 81.9%,
   B 79.9%, D 82.8%. Quote the type-eliminable share of RFC 8446 §4's
   normative surface as **80–83%** (three raters, one codebook lineage,
   disagreements unresolved by design). Eliminable-vs-not agreement is
   89–96% while raw item agreement is 80–91%: most residual disagreement is
   *interior* to the eliminable family.
3. **Item-level transmission has a measured floor.** Under text-only
   transmission the raw agreement floor sits in the mid-80s, and the
   remaining mass localizes to two named boundaries: DOMAIN/PROCESS
   (encoding duties read as wire-predicate vs procedure — 7 items where C
   and D both read PROCESS against A's DOMAIN) and the rule-10
   history-varying judgment itself (5 guard items where B and D read DOMAIN
   against A's TYPESTATE).
4. **Author context leaks into labels — measured, not suspected.** 15 items
   have C = D ≠ A: two independent raters who never saw the census agree on
   the same alternative label. Those 15 are the census's error bar made
   visible; they are listed in the scoring output and remain unadjudicated
   (the census's no-silent-adjudication rule).

## Raw labels (rater D, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE
8:TYPESTATE 9:TYPESTATE 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:DOMAIN 14:PROCESS
15:DOMAIN 16:DOMAIN 17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN 21:DOMAIN
22:DOMAIN 23:U 24:TYPESTATE 25:TYPESTATE 26:DOMAIN 27:DOMAIN 28:DOMAIN
29:PROCESS 30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN 35:TYPESTATE
36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE 40:TYPESTATE 41:TYPESTATE
42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE 46:TYPESTATE
47:TYPESTATE 48:DOMAIN 49:DOMAIN 50:DOMAIN 51:DOMAIN 52:DOMAIN 53:PROCESS
54:TYPESTATE 55:DOMAIN 56:DOMAIN 57:DOMAIN 58:DOMAIN 59:PROCESS 60:PROCESS
61:TYPESTATE 62:TYPESTATE 63:TYPESTATE 64:PROCESS 65:DOMAIN 66:DOMAIN
67:DOMAIN 68:DOMAIN 69:DOMAIN 70:DOMAIN 71:DOMAIN 72:DOMAIN 73:DOMAIN
74:DOMAIN 75:DOMAIN 76:PROCESS 77:DOMAIN 78:DOMAIN 79:TYPESTATE
80:TYPESTATE 81:DOMAIN 82:TYPESTATE 83:TYPESTATE 84:PROCESS 85:DOMAIN
86:DOMAIN 87:TYPESTATE 88:DOMAIN 89:PROCESS 90:DOMAIN 91:U 92:DOMAIN
93:DOMAIN 94:TYPESTATE 95:TYPESTATE 96:TYPESTATE 97:TYPESTATE 98:TYPESTATE
99:TYPESTATE 100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN
105:DOMAIN 106:TYPESTATE 107:DOMAIN 108:TYPESTATE 109:TYPESTATE 110:DOMAIN
111:TYPESTATE 112:REVOCABLE 113:PROCESS 114:TYPESTATE 115:TYPESTATE
116:TYPESTATE 117:META 118:TYPESTATE 119:PROCESS 120:CV 121:TYPESTATE
122:PROCESS 123:POLICY 124:TYPESTATE 125:CV 126:CV 127:TYPESTATE
128:TYPESTATE 129:DOMAIN 130:DOMAIN 131:DOMAIN 132:DOMAIN 133:REVOCABLE
134:TYPESTATE 135:TYPESTATE 136:DOMAIN 137:TYPESTATE 138:TYPESTATE
139:DOMAIN 140:DOMAIN 141:PROCESS 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE
145:TYPESTATE 146:TYPESTATE 147:DOMAIN 148:TYPESTATE 149:TYPESTATE
150:DOMAIN 151:DOMAIN 152:DOMAIN 153:DOMAIN 154:DOMAIN 155:DOMAIN
156:DOMAIN 157:DOMAIN 158:DOMAIN 159:DOMAIN 160:TYPESTATE 161:TYPESTATE
162:TYPESTATE 163:TYPESTATE 164:DOMAIN 165:DOMAIN 166:TYPESTATE
167:TYPESTATE 168:DOMAIN 169:DOMAIN 170:TYPESTATE 171:TYPESTATE
172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE 176:DOMAIN
177:DOMAIN 178:CV 179:CV 180:CV 181:TYPESTATE 182:TYPESTATE 183:TYPESTATE
184:DOMAIN 185:TYPESTATE 186:TYPESTATE 187:PROCESS 188:THRESHOLD
189:THRESHOLD 190:TYPESTATE 191:PROCESS 192:TYPESTATE 193:TYPESTATE
194:TYPESTATE 195:TYPESTATE 196:TYPESTATE 197:TYPESTATE 198:TYPESTATE
199:TYPESTATE 200:PROCESS 201:DOMAIN 202:TYPESTATE 203:TYPESTATE
204:TYPESTATE
```
