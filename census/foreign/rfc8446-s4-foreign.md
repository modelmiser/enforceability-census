# Cross-family replication — RFC 8446 §4 under two foreign frontier models

2026-08-13 · Companion to `README.md` in this directory (the pre-registration,
committed and pushed at `e3995f0` before any foreign rater existed) and to the
TLS census (`census/tls13/`). **Status: COMPLETE — two foreign raters, full
204-item maps archived below; predictions graded 3/5 (F1, F3, F5 pass; F2,
F4 fail — F2's predicted degradation failed to appear at claim granularity
for either rater).**

## Setup

Exactly as pre-registered; no deviations.

- Corpus: `census/tls13/rfc8446_s4_musts.txt` byte-identical (sha256
  `fc7befbc…`, blob `fbc6591a…`), n = 204, served in four chunks
  ([1–51], [52–102], [103–153], [154–204]).
- Instrument: frozen rater pack, blob `a08febba…`, hash round-trip verified
  at serving time. Codebook v3 (rules 1–14); candidates 15/16 not present.
- Raters, transport cursor-cli (`cursor-agent --print --output-format text
  --mode ask`, empty working directory, fresh process per chunk):
  - **Rater G** = OpenAI `gpt-5.6-sol-high`
  - **Rater X** = xAI `cursor-grok-4.6-high-fast`
- Blindness: instrument + chunk only. No predictions, no other labels, no
  running totals, no hypotheses.
- **Protocol events: NONE.** All eight chunk calls returned exactly 51
  well-formed `N:CLASS` labels on the first attempt — the single-shot rule
  was never exercised. No missing, duplicate, out-of-range, or invalid
  labels from either rater.
- Comparison anchors: rater D (pass 4, full archive) primary, rater A
  (census, full map from per-class rosters) secondary. Rater B has no
  archived full map (see the census report's provenance note) and is not
  compared.

## Results

| | rater G (GPT-5.6 Sol) | rater X (Grok 4.6) |
|---|---|---|
| eliminable in shape (DOMAIN+TYPESTATE) | **156/204 = 76.5%** | **165/204 = 80.9%** |
| vs D: raw / eliminable-vs-not | 166/204 = 81.4% / 187/204 = 91.7% | 187/204 = 91.7% / 200/204 = 98.0% |
| vs A: raw / eliminable-vs-not | 164/204 = 80.4% / 179/204 = 87.7% | 178/204 = 87.3% / 184/204 = 90.2% |
| CV set {120,125,126,178,179,180} | 6/6 | 6/6 |
| disagreements vs D (interior to eliminable) | 38 (15 = 39.5%) | 17 (12 = 70.6%) |
| class tally | TYPESTATE 92, DOMAIN 64, U 18, PROCESS 14, CV 9, NEG 2, THRESHOLD 2, REVOCABLE 2, META 1 | TYPESTATE 96, DOMAIN 69, PROCESS 19, CV 6, U 5, NEG 2, POLICY 2, REVOCABLE 2, THRESHOLD 2, META 1 |

G-vs-X: raw 176/204 = 86.3%, eliminable-vs-not 191/204 = 93.6%.

Claude reference points: quotients A 81.9 / B 79.9 / D 82.8; intra-family raw
agreement 81–90%; eliminable-vs-not 87–96%.

## Predictions graded (F1–F5)

| # | prediction | outcome |
|---|---|---|
| F1 | each foreign quotient in 76–86% | **PASS** — G 76.5% (at the floor), X 80.9% |
| F2 | each foreign rater vs D: raw in 70–84% and elim-vs-not in 82–93% — "cross-family agreement is lower than intra-family at both granularities, but the quotient-level signal (eliminable-vs-not) degrades less than raw labels" | **FAIL** — numeric bands: G inside both (81.4 / 91.7), X above both (91.7 / 98.0). The lower-than-intra-family clause fails for BOTH raters: G's 91.7% eliminable-vs-not sits inside the intra-family range (above A-vs-D's 89.2%), and X sits above the ranges at both granularities |
| F3 | each rater labels ≥5/6 CV-set items CV | **PASS** — 6/6 and 6/6 |
| F4 | each rater: >50% of disagreements vs D interior to eliminable | **FAIL** — X 70.6% passes; G 39.5% fails (mechanism: U-inflation, finding 6) |
| F5 | G-vs-X raw within ±6 pts of mean(G vs D, X vs D) | **PASS** — 86.3% vs mean 86.5%, delta 0.2 pts |

Per the pre-committed interpretation, the two failures grade the author's
model of cross-family transmissibility and license nothing else. F2's failure
direction matters and is stated plainly: I predicted cross-family agreement
would sit *below* intra-family agreement at both granularities, and neither
rater's eliminable-vs-not agreement did; one rater (X) landed *above* the
intra-family ranges at both granularities.

## Findings

1. **The headline does not move, per pre-commitment; the five-rater spread is
   76.5–82.8%.** X's quotient (80.9%) lands inside the three-Claude-rater
   band (79.9–82.8%); G's (76.5%) lands 3.4 points below it. The quoted TLS
   headline stays 80–83% (three raters, one codebook lineage); the foreign
   quotients are this separate replication row.

2. **Cross-family agreement is not systematically below intra-family
   agreement — the family-bias half of limitation 6 is weakened.** X vs D:
   raw 91.7% and eliminable-vs-not 98.0%, both *above* the intra-family
   ranges (81–90% / 87–96%); X vs A sits inside them (87.3% / 90.2%). G vs D
   (81.4% raw) sits at the intra-family floor with eliminable-vs-not (91.7%)
   inside the range; G vs A raw (80.4%) falls just below the range. Under the pre-registered degradation model this is F2 failing upward: a
   frontier model from a different family, reading the frozen pack cold,
   agreed with a Claude rater more closely than Claude raters agree with
   each other. What this does NOT show: it cannot separate "the codebook is
   crisp" from "all frontier LLMs share a corpus prior about TLS" — that is
   the unaddressed half (see Scope, below).

3. **The zero-variance class is now zero-variance across families.** The CV
   set {120, 125, 126, 178, 179, 180} was labeled CV 6/6 by every rater in
   the study's history — four Claude passes and now two foreign families.
   The crypto-core figure (2.9% of the corpus, exactly these six items) is
   the most family-robust number in the repository. G additionally labeled
   three items CV that no other rater does ({181, 199, 203} — encrypt-
   under-the-appropriate-key duties in the key-schedule sections, TYPESTATE
   to Claude raters and to X): a third reading of the key-lifecycle
   boundary that RFC 9001 measured as PROCESS-vs-TYPESTATE and MLS measured
   under capability-compatibility. The soft boundary keeps being the same
   boundary; which side of it a family lands on varies.

4. **Twelve items of cross-family consensus against D — the census's error
   bar, re-measured with foreign families.** On 12 items G and X
   independently chose the *same* alternative to D's label (the cross-family
   analog of pass 4's C=D≠A finding). Two exact clusters:
   - **Nine DOMAIN→TYPESTATE** ({10, 52, 67, 129, 130, 139, 152, 159,
     165}): checks whose applicability or required value is conditioned on
     negotiated or prior-message state — e.g., [159] "The certificate type
     MUST be X.509v3 … *unless explicitly negotiated otherwise*". D read
     the discharged check as single-message format discipline (DOMAIN);
     both foreign raters read the negotiated-state condition as
     state-indexing the obligation (TYPESTATE), a reading of rule 10's
     "required value/set varies with … negotiated state" clause. Rule 10's
     DOMAIN bullet does answer the plain guard case (the guard "only
     locates where the obligation applies" and a constant check is DOMAIN
     "however the sentence happens to be guarded"); what its text does not
     settle is narrower: whether an "unless explicitly negotiated
     otherwise" clause is required-value *variation* (TYPESTATE bullet) or
     applicability *scoping* (DOMAIN bullet) — that is, what "every
     occurrence of the obligation" quantifies over. Three of these items
     ({67, 159, 165}) were in the census's original guard-vs-predicate
     DISAGREE mass — the boundary rule 10 was written to tie-break — so
     this cluster is the measured residue of that repair. A measured
     instrument edge, not a rater error: **candidate rule 17** (scope of
     "occurrence" under rule 10), parked for a future instrument version
     alongside candidates 15 and 16. Not adjudicated here.
   - **Three →U** ({187, 190, 197}): reporting an SNI value to the calling
     application; generating a fresh ticket value; being prepared for
     client-authentication delay. Two of the three were already contested
     intra-family (A and D split on 190 and 197; 187 was uncontested —
     A, B, and D all read it PROCESS), and all three sit at the
     rule-11 wire-falsifiability boundary — obligations whose observable is
     outside the peer's wire view.

5. **The author-context finding reproduces across families.** Pass 4 found
   15 items where two context-free Claude raters agreed on the same
   alternative to author-rater A's label (C = D ≠ A). On those 15, G sides
   with D on 11 and X on 13; each sides with A on exactly 2 (item 67 for
   both — which also belongs to the nine-item cluster above — plus G on
   122, X on 184). On 13 of the 15, then, two foreign families
   independently confirm that A's readings were author-context artifacts no
   fresh reader recovers; the recovered exceptions concentrate on the
   rule-17 edge (item 67, recovered by both) plus one item per rater.

6. **Where U lands is family-dependent, and it is by itself sufficient to
   explain G's below-band quotient.** G placed 18 items in U, X 5; among
   Claude raters, A placed 6, D 2, and B 10 (inferred — B's six agreements
   with A's U items plus four recorded B:U disagreements; B's full map is
   unarchived). Both foreign raters include the two-rater Claude consensus
   items {23, 91}; G's remaining 16 drain mostly from D's DOMAIN/TYPESTATE
   (items like 55, 66, 96, 111, 145, 157 — checks A, D, and X all consider
   classifiable). This conservative-refusal habit crosses the
   eliminable-vs-not boundary, which is why F4 fails for G; resolving G's
   16 non-consensus U items to D's labels would yield 168/204 = 82.4%,
   *inside* the Claude band. The class *boundaries* transmit (findings
   2–3); the *willingness to classify* is a family trait.

## Scope — what this replication does and does not answer

This was pre-registered as attacking the **family-bias half** of limitation
6, and that is all it does. Family bias is weakened: agreement does not
*systematically* degrade across the family boundary — one rater shows none
(X, above the intra-family ranges), one at most mild degradation (G, at or
just below the raw floor) (finding 2); the crispest class is family-invariant
(finding 3); and cross-family disagreement concentrates on two nameable
instrument edges rather than diffusing (finding 4). The
**corpus-shared-prior half stands untouched**: G and X were trained on RFC
8446 and on decades of prose about TLS, exactly as the Claude raters were. A
shared reading learned from the corpus would produce these same agreements.
No LLM replication, from any family, can separate that from genuine codebook
crispness; only a non-LLM rater (the parked human replication) bears on it.

## Raw labels (rater G, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE
8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN
14:PROCESS 15:DOMAIN 16:DOMAIN 17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN
21:DOMAIN 22:TYPESTATE 23:U 24:TYPESTATE 25:TYPESTATE 26:DOMAIN 27:DOMAIN
28:DOMAIN 29:PROCESS 30:TYPESTATE 31:TYPESTATE 32:TYPESTATE 33:DOMAIN
34:DOMAIN 35:TYPESTATE 36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE
40:TYPESTATE 41:TYPESTATE 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE
45:TYPESTATE 46:TYPESTATE 47:TYPESTATE 48:DOMAIN 49:DOMAIN 50:DOMAIN
51:DOMAIN 52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:U 56:TYPESTATE 57:DOMAIN
58:DOMAIN 59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE 63:TYPESTATE
64:PROCESS 65:DOMAIN 66:U 67:TYPESTATE 68:DOMAIN 69:DOMAIN 70:DOMAIN
71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:U 76:U 77:DOMAIN 78:DOMAIN 79:U
80:U 81:DOMAIN 82:TYPESTATE 83:TYPESTATE 84:PROCESS 85:DOMAIN 86:DOMAIN
87:TYPESTATE 88:DOMAIN 89:U 90:DOMAIN 91:U 92:DOMAIN 93:DOMAIN 94:TYPESTATE
95:TYPESTATE 96:U 97:TYPESTATE 98:TYPESTATE 99:TYPESTATE 100:TYPESTATE
101:DOMAIN 102:DOMAIN 103:DOMAIN 104:DOMAIN 105:DOMAIN 106:TYPESTATE
107:DOMAIN 108:TYPESTATE 109:TYPESTATE 110:DOMAIN 111:U 112:THRESHOLD
113:TYPESTATE 114:TYPESTATE 115:TYPESTATE 116:TYPESTATE 117:META
118:TYPESTATE 119:PROCESS 120:CV 121:TYPESTATE 122:DOMAIN 123:U
124:TYPESTATE 125:CV 126:CV 127:TYPESTATE 128:TYPESTATE 129:TYPESTATE
130:TYPESTATE 131:DOMAIN 132:DOMAIN 133:REVOCABLE 134:TYPESTATE
135:TYPESTATE 136:DOMAIN 137:TYPESTATE 138:TYPESTATE 139:TYPESTATE
140:DOMAIN 141:PROCESS 142:TYPESTATE 143:TYPESTATE 144:TYPESTATE 145:U
146:TYPESTATE 147:DOMAIN 148:TYPESTATE 149:TYPESTATE 150:DOMAIN 151:DOMAIN
152:TYPESTATE 153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:U 158:DOMAIN
159:TYPESTATE 160:TYPESTATE 161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:U
165:TYPESTATE 166:DOMAIN 167:TYPESTATE 168:DOMAIN 169:DOMAIN 170:TYPESTATE
171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE 175:TYPESTATE
176:DOMAIN 177:DOMAIN 178:CV 179:CV 180:CV 181:CV 182:TYPESTATE
183:TYPESTATE 184:DOMAIN 185:TYPESTATE 186:TYPESTATE 187:U 188:THRESHOLD
189:REVOCABLE 190:U 191:PROCESS 192:TYPESTATE 193:TYPESTATE 194:TYPESTATE
195:TYPESTATE 196:TYPESTATE 197:U 198:TYPESTATE 199:CV 200:PROCESS
201:DOMAIN 202:TYPESTATE 203:CV 204:TYPESTATE
```

## Raw labels (rater X, archived verbatim)

```
1:TYPESTATE 2:TYPESTATE 3:NEG 4:TYPESTATE 5:TYPESTATE 6:NEG 7:TYPESTATE
8:TYPESTATE 9:TYPESTATE 10:TYPESTATE 11:DOMAIN 12:DOMAIN 13:DOMAIN
14:PROCESS 15:DOMAIN 16:DOMAIN 17:PROCESS 18:PROCESS 19:DOMAIN 20:DOMAIN
21:DOMAIN 22:DOMAIN 23:U 24:TYPESTATE 25:TYPESTATE 26:DOMAIN 27:DOMAIN
28:DOMAIN 29:PROCESS 30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN
35:TYPESTATE 36:DOMAIN 37:TYPESTATE 38:PROCESS 39:TYPESTATE 40:TYPESTATE
41:TYPESTATE 42:TYPESTATE 43:TYPESTATE 44:TYPESTATE 45:TYPESTATE
46:TYPESTATE 47:TYPESTATE 48:DOMAIN 49:DOMAIN 50:DOMAIN 51:DOMAIN
52:TYPESTATE 53:PROCESS 54:TYPESTATE 55:DOMAIN 56:DOMAIN 57:DOMAIN 58:DOMAIN
59:PROCESS 60:PROCESS 61:TYPESTATE 62:TYPESTATE 63:TYPESTATE 64:PROCESS
65:DOMAIN 66:DOMAIN 67:TYPESTATE 68:DOMAIN 69:DOMAIN 70:DOMAIN 71:DOMAIN
72:DOMAIN 73:DOMAIN 74:DOMAIN 75:POLICY 76:PROCESS 77:DOMAIN 78:DOMAIN
79:TYPESTATE 80:TYPESTATE 81:TYPESTATE 82:TYPESTATE 83:TYPESTATE 84:PROCESS
85:DOMAIN 86:DOMAIN 87:TYPESTATE 88:DOMAIN 89:PROCESS 90:DOMAIN 91:U
92:DOMAIN 93:DOMAIN 94:TYPESTATE 95:TYPESTATE 96:TYPESTATE 97:TYPESTATE
98:TYPESTATE 99:TYPESTATE 100:TYPESTATE 101:DOMAIN 102:DOMAIN 103:DOMAIN
104:DOMAIN 105:DOMAIN 106:TYPESTATE 107:DOMAIN 108:TYPESTATE 109:TYPESTATE
110:DOMAIN 111:DOMAIN 112:REVOCABLE 113:PROCESS 114:TYPESTATE 115:TYPESTATE
116:TYPESTATE 117:META 118:TYPESTATE 119:PROCESS 120:CV 121:TYPESTATE
122:PROCESS 123:POLICY 124:TYPESTATE 125:CV 126:CV 127:TYPESTATE
128:TYPESTATE 129:TYPESTATE 130:TYPESTATE 131:DOMAIN 132:DOMAIN
133:REVOCABLE 134:TYPESTATE 135:TYPESTATE 136:DOMAIN 137:TYPESTATE
138:TYPESTATE 139:TYPESTATE 140:DOMAIN 141:PROCESS 142:TYPESTATE
143:TYPESTATE 144:TYPESTATE 145:TYPESTATE 146:TYPESTATE 147:DOMAIN
148:TYPESTATE 149:TYPESTATE 150:DOMAIN 151:DOMAIN 152:TYPESTATE 153:DOMAIN
154:DOMAIN 155:DOMAIN 156:DOMAIN 157:PROCESS 158:DOMAIN 159:TYPESTATE
160:TYPESTATE 161:TYPESTATE 162:TYPESTATE 163:TYPESTATE 164:DOMAIN
165:TYPESTATE 166:TYPESTATE 167:TYPESTATE 168:DOMAIN 169:DOMAIN
170:TYPESTATE 171:TYPESTATE 172:TYPESTATE 173:TYPESTATE 174:TYPESTATE
175:TYPESTATE 176:DOMAIN 177:DOMAIN 178:CV 179:CV 180:CV 181:TYPESTATE
182:TYPESTATE 183:TYPESTATE 184:TYPESTATE 185:TYPESTATE 186:TYPESTATE 187:U
188:THRESHOLD 189:THRESHOLD 190:U 191:PROCESS 192:TYPESTATE 193:TYPESTATE
194:TYPESTATE 195:TYPESTATE 196:TYPESTATE 197:U 198:TYPESTATE 199:TYPESTATE
200:PROCESS 201:DOMAIN 202:TYPESTATE 203:TYPESTATE 204:TYPESTATE
```
