# The obfuscation probe: identification survives obfuscation, and so does every graded label — the check failed exactly as designed, and its failure is the finding

**Setup.** Exactly as registered (`README.md` in this directory,
pushed at `c500361` before any rater or check agent existed): the
frozen v6 instrument (blob `f4f9e0b…`) over the shipped obfuscated
derivation of the iCalendar corpus, two manipulation-check arms run
first, then two blind raters — **Ao** (fresh `claude-fable-5`, single
input file, one-read attestation held: one tool call) and **Xo**
(`cursor-grok-4.6-high-fast`, five pinned chunks, all rc=0, full
coverage, no retries). Zero protocol events. Labels extracted
mechanically; scorer known-answer-tested per the registration (eight
archived scores exact, O3/O4 fail branches exhibited by archived
raters, O2's by the shipped-spec mutant at 170/194) before any live
output was scored.

## Grades

| clause | registered | result |
|---|---|---|
| O1a (corpus-only identification) | answer names no format identity | **FAIL** — names iCalendar/RFC 5545 at ~95% confidence; scan hits {icalendar, ical, ics, 5545, 2445} |
| O1b (as-served identification) | same, on pack + corpus | **FAIL** — ~98% confidence; scan hits {icalendar, vcalendar, 5545, 2445} |
| O2 (DOMAIN-mass, ≥185/194 per rater) | | **PASS** — Ao **194/194**, Xo **194/194** |
| O3 (recognition family, ≥8/9 PROCESS per rater) | | **PASS** — 9/9 both |
| O4 (within-object trio, 3/3 DOMAIN per rater) | | **PASS** — 3/3 both |

Per the pre-committed interpretation, the O1b failure DOWNGRADES the
O2–O4 passes: with the format identified in the as-served condition,
they cannot separate shape-reading from memorized readings. They are
reported under that downgrade, and nothing here touches any census
number — the probe's shares (Ao 89.8%, Xo 88.9%) are probe numbers
only and join no series.

## Findings

1. **The manipulation check's failure is the probe's result: this
   corpus's identity lives in its structure, not its vocabulary — so
   the memorization channel cannot be closed by lexical means.** Both
   check arms identified RFC 5545 through 90 nonced tokens, two
   nonced extension stems, and eight nonced domain nouns, at 95% and
   98% stated confidence — and their archived reasoning shows the
   route: the content-line fold/unfold grammar, the recurrence-rule
   architecture (a required first rule part, two mutually exclusive
   bound parts, the BY*-table note), the paired-property constraint
   shapes (end-xor-duration), the leap-second and escaping rules,
   and the sibling-citation set (RFC 2368/2045/3986 — which the
   as-served arm used to rule out the predecessor revision, while the
   corpus-only arm settled the same question from deprecation
   language and the UID persistence clause).
   Both arms read nonces back to their originals in passing. This is
   the registered check doing precisely what a check that can fail is
   for, and it converts limitation 6's assertion — that no LLM-side
   design reaches the corpus-shared-prior confound, and only a
   non-LLM rater does — from an argument into a measurement.
2. **Under the downgrade, what the rating cells still measure:
   removing the memorizable vocabulary costs approximately
   nothing.** Both raters matched the v6 pair's original-corpus
   labels on 224 of 225 items (99.6% each — the top of the measured
   95.6–99.6% context band), and each rater's single departure is a
   U-boundary item, not a classification flip: Ao classifies item 7
   (DOMAIN) where the v6 pair recorded U; Xo goes U-torn on item 77
   where the v6 pair had DOMAIN. The obfuscated pair agrees at
   **222/225 = 98.7% raw — exactly tying, item-count for item-count,
   the repository record the v6 pair set on the original corpus** —
   and both raters post 194/194 on the DOMAIN-mass set — matching
   the anchors' by-construction 194 and Av5's measured 194, above
   the other four archived raters' 193. The J4
   pair reproduces the v6 readings exactly (62 DOMAIN ×2, 150
   PROCESS ×2 — the validity/precision boundary transmits with the
   RECUR identifier nonced), and item 185 splits TYPESTATE/DOMAIN
   along family lines for a fourth consecutive pass, now under
   nonces. Whatever drives these readings — shape or memory, which
   this probe cannot now separate — it is insensitive to every
   identifier and domain noun the corpus contained.
3. **What would have distinguished the hypotheses did not occur.**
   If labels rode on memorized identifier-keyed readings, nonce
   substitution should have produced scatter somewhere — the
   registration's floors granted an eight-item allowance on O2 and a
   one-item allowance on O3 for exactly that possibility. Measured
   cost: zero items on O2 in both raters, zero on O3, zero on O4.
   The nonce-comprehension confound the registration named (a FAIL
   would have been ambiguous) never engaged; the probe's asymmetry
   ran in the informative direction, but the O1b downgrade caps what
   the passes certify.
4. **The residual path to the confound is unchanged and now
   evidenced.** The probe was registered as reaching only the
   memorization component; the measured result is that even that
   component cannot be isolated from an LLM seat, because
   identification precedes rating through structure alone. The
   parked human-rater replication remains the only probe that
   reaches the shared-prior confound — a statement limitation 6 made
   on argument and this probe now makes on measurement.

## Report-only tables (registration duties)

The 20-item soft residue (the v6-pass outside set), both raters —
seventeen pair-unanimous and v6-matching, the three exceptions being
the pair's only disagreements: 1 PROCESS ×2; 2 PROCESS ×2; 7
DOMAIN/UNCLASSIFIED (the Ao-side departure); 37 PROCESS ×2; 46
PROCESS ×2; 47 PROCESS ×2; 69 PROCESS ×2; 77 DOMAIN/UNCLASSIFIED?
(the Xo-side departure); 79 DOMAIN ×2; 118 PROCESS ×2; 138 PROCESS
×2; 141 PROCESS ×2; 185 TYPESTATE/DOMAIN (the family split); 192,
193, 194 DOMAIN ×2 (the O4 grade); 200 UNCLASSIFIED ×2; 201
UNCLASSIFIED ×2; 203 PROCESS ×2; 204 PROCESS ×2.

Watch items, both raters (v6-pair readings in parentheses): 37
PROCESS ×2 (P/P); 69 PROCESS ×2 (P/P); 43 DOMAIN ×2 (D/U — the
liminal item sits with Av6 here); 79 DOMAIN ×2 (D/D); 116 DOMAIN ×2
(U/D — with Xv6); 141 PROCESS ×2 (P/P); 185 TYPESTATE/DOMAIN
(TYPESTATE/DOMAIN — the family split, reproduced); 203 PROCESS ×2
(P/P). Pair disagreements, all three: 7 (DOMAIN vs UNCLASSIFIED), 77
(DOMAIN vs UNCLASSIFIED?), 185 (the family split). Xo's one torn
flag: 77.

The two check-arm answers are archived verbatim below with the
raters' labels; the mechanical O1 scans that graded them are the
registered word-boundary token scans, self-tested on planted and
near-miss strings.

## Raw labels (rater Ao, then rater Xo — archived verbatim)

Rater Ao:

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:DOMAIN
8:DOMAIN 9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:PROCESS 14:DOMAIN
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
91:PROCESS 92:DOMAIN 93:DOMAIN 94:DOMAIN 95:DOMAIN 96:DOMAIN 97:DOMAIN
98:DOMAIN 99:DOMAIN 100:DOMAIN 101:DOMAIN 102:DOMAIN 103:DOMAIN
104:DOMAIN 105:DOMAIN 106:DOMAIN 107:DOMAIN 108:DOMAIN 109:DOMAIN
110:DOMAIN 111:DOMAIN 112:DOMAIN 113:DOMAIN 114:DOMAIN 115:DOMAIN
116:DOMAIN 117:DOMAIN 118:PROCESS 119:DOMAIN 120:DOMAIN 121:DOMAIN
122:DOMAIN 123:DOMAIN 124:DOMAIN 125:DOMAIN 126:DOMAIN 127:DOMAIN
128:DOMAIN 129:DOMAIN 130:DOMAIN 131:DOMAIN 132:DOMAIN 133:DOMAIN
134:DOMAIN 135:DOMAIN 136:DOMAIN 137:DOMAIN 138:PROCESS 139:DOMAIN
140:DOMAIN 141:PROCESS 142:DOMAIN 143:DOMAIN 144:DOMAIN 145:DOMAIN
146:PROCESS 147:DOMAIN 148:DOMAIN 149:DOMAIN 150:PROCESS 151:DOMAIN
152:DOMAIN 153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN 157:DOMAIN
158:DOMAIN 159:DOMAIN 160:DOMAIN 161:DOMAIN 162:DOMAIN 163:DOMAIN
164:DOMAIN 165:DOMAIN 166:DOMAIN 167:DOMAIN 168:DOMAIN 169:DOMAIN
170:DOMAIN 171:DOMAIN 172:DOMAIN 173:DOMAIN 174:DOMAIN 175:DOMAIN
176:DOMAIN 177:DOMAIN 178:DOMAIN 179:DOMAIN 180:DOMAIN 181:DOMAIN
182:DOMAIN 183:DOMAIN 184:DOMAIN 185:TYPESTATE 186:DOMAIN 187:DOMAIN
188:DOMAIN 189:DOMAIN 190:DOMAIN 191:DOMAIN 192:DOMAIN 193:DOMAIN
194:DOMAIN 195:DOMAIN 196:DOMAIN 197:DOMAIN 198:DOMAIN 199:DOMAIN
200:UNCLASSIFIED 201:UNCLASSIFIED 202:DOMAIN 203:PROCESS 204:PROCESS
205:DOMAIN 206:DOMAIN 207:DOMAIN 208:DOMAIN 209:DOMAIN 210:PROCESS
211:DOMAIN 212:DOMAIN 213:DOMAIN 214:DOMAIN 215:DOMAIN 216:DOMAIN
217:DOMAIN 218:DOMAIN 219:DOMAIN 220:DOMAIN 221:DOMAIN 222:DOMAIN
223:DOMAIN 224:DOMAIN 225:DOMAIN
```

Rater Xo:

```
1:PROCESS 2:PROCESS 3:DOMAIN 4:DOMAIN 5:DOMAIN 6:DOMAIN 7:UNCLASSIFIED
8:DOMAIN 9:DOMAIN 10:DOMAIN 11:DOMAIN 12:DOMAIN 13:PROCESS 14:DOMAIN
15:DOMAIN 16:PROCESS 17:DOMAIN 18:DOMAIN 19:DOMAIN 20:DOMAIN 21:DOMAIN
22:PROCESS 23:DOMAIN 24:DOMAIN 25:PROCESS 26:DOMAIN 27:PROCESS
28:PROCESS 29:DOMAIN 30:DOMAIN 31:DOMAIN 32:DOMAIN 33:DOMAIN 34:DOMAIN
35:DOMAIN 36:DOMAIN 37:PROCESS 38:DOMAIN 39:DOMAIN 40:DOMAIN 41:DOMAIN
42:DOMAIN 43:DOMAIN 44:DOMAIN 45:DOMAIN 46:PROCESS 47:PROCESS 48:DOMAIN
49:DOMAIN 50:DOMAIN 51:DOMAIN 52:DOMAIN 53:DOMAIN 54:DOMAIN 55:DOMAIN
56:DOMAIN 57:DOMAIN 58:DOMAIN 59:DOMAIN 60:DOMAIN 61:DOMAIN 62:DOMAIN
63:DOMAIN 64:DOMAIN 65:DOMAIN 66:DOMAIN 67:DOMAIN 68:DOMAIN 69:PROCESS
70:DOMAIN 71:DOMAIN 72:DOMAIN 73:DOMAIN 74:DOMAIN 75:DOMAIN 76:DOMAIN
77:UNCLASSIFIED? 78:DOMAIN 79:DOMAIN 80:DOMAIN 81:DOMAIN 82:DOMAIN
83:DOMAIN 84:DOMAIN 85:DOMAIN 86:DOMAIN 87:DOMAIN 88:DOMAIN 89:DOMAIN
90:DOMAIN 91:PROCESS 92:DOMAIN 93:DOMAIN 94:DOMAIN 95:DOMAIN 96:DOMAIN
97:DOMAIN 98:DOMAIN 99:DOMAIN 100:DOMAIN 101:DOMAIN 102:DOMAIN
103:DOMAIN 104:DOMAIN 105:DOMAIN 106:DOMAIN 107:DOMAIN 108:DOMAIN
109:DOMAIN 110:DOMAIN 111:DOMAIN 112:DOMAIN 113:DOMAIN 114:DOMAIN
115:DOMAIN 116:DOMAIN 117:DOMAIN 118:PROCESS 119:DOMAIN 120:DOMAIN
121:DOMAIN 122:DOMAIN 123:DOMAIN 124:DOMAIN 125:DOMAIN 126:DOMAIN
127:DOMAIN 128:DOMAIN 129:DOMAIN 130:DOMAIN 131:DOMAIN 132:DOMAIN
133:DOMAIN 134:DOMAIN 135:DOMAIN 136:DOMAIN 137:DOMAIN 138:PROCESS
139:DOMAIN 140:DOMAIN 141:PROCESS 142:DOMAIN 143:DOMAIN 144:DOMAIN
145:DOMAIN 146:PROCESS 147:DOMAIN 148:DOMAIN 149:DOMAIN 150:PROCESS
151:DOMAIN 152:DOMAIN 153:DOMAIN 154:DOMAIN 155:DOMAIN 156:DOMAIN
157:DOMAIN 158:DOMAIN 159:DOMAIN 160:DOMAIN 161:DOMAIN 162:DOMAIN
163:DOMAIN 164:DOMAIN 165:DOMAIN 166:DOMAIN 167:DOMAIN 168:DOMAIN
169:DOMAIN 170:DOMAIN 171:DOMAIN 172:DOMAIN 173:DOMAIN 174:DOMAIN
175:DOMAIN 176:DOMAIN 177:DOMAIN 178:DOMAIN 179:DOMAIN 180:DOMAIN
181:DOMAIN 182:DOMAIN 183:DOMAIN 184:DOMAIN 185:DOMAIN 186:DOMAIN
187:DOMAIN 188:DOMAIN 189:DOMAIN 190:DOMAIN 191:DOMAIN 192:DOMAIN
193:DOMAIN 194:DOMAIN 195:DOMAIN 196:DOMAIN 197:DOMAIN 198:DOMAIN
199:DOMAIN 200:UNCLASSIFIED 201:UNCLASSIFIED 202:DOMAIN 203:PROCESS
204:PROCESS 205:DOMAIN 206:DOMAIN 207:DOMAIN 208:DOMAIN 209:DOMAIN
210:PROCESS 211:DOMAIN 212:DOMAIN 213:DOMAIN 214:DOMAIN 215:DOMAIN
216:DOMAIN 217:DOMAIN 218:DOMAIN 219:DOMAIN 220:DOMAIN 221:DOMAIN
222:DOMAIN 223:DOMAIN 224:DOMAIN 225:DOMAIN
```

## Archived check-arm answers (verbatim)

### O1a (corpus-only)

```
**Identification: iCalendar — RFC 5545 (Internet Calendaring and Scheduling Core Object Specification, iCal/ics format).** The obfuscated "gofa object" is the iCalendar object; possibly RFC 2445 (its predecessor), but phrases like "deprecated by this revision" and "applications that pre-date this revision" point to the revised spec, RFC 5545.

**Confidence: very high (~95%).**

**Reasoning:** The structural fingerprint is unmistakable despite token obfuscation:

- **Content-line syntax:** line folding/unfolding, COMMA-separated multi-values, SEMICOLON-separated structured values, quoted-string parameter values excluding DQUOTE, backslash escaping of `\n`, comma, semicolon (but not colon) in TEXT values — exactly RFC 5545 §3.1–3.3.
- **Recurrence rules:** "PAMI" = FREQ (REQUIRED, first for backward compatibility), "BUZE"/"KUFA" = UNTIL/COUNT (mutually exclusive in a RECUR), BYxxx rule parts, the "N/A means the BYxxx part MUST NOT be used with the FREQ value" table note, leap-second handling (second 60 only for positive leap seconds), exact-duration computation order (days, hours, minutes, seconds) — RFC 5545 §3.3.10.
- **Components:** "VENE/MITA/VOGOGO/SUMEBI/MIPERI/GEZO" map to VEVENT/VTODO/VJOURNAL/VFREEBUSY/VTIMEZONE/VALARM; "TAFAKO/MIPESO" = STANDARD/DAYLIGHT sub-components requiring DTSTART, TZOFFSETFROM/TO; "SISUSI/FUKI/LAFI/ZEPAMA/GURO" = DTSTART/DTEND/DUE/DURATION/REPEAT, including the "DTEND xor DURATION in a VEVENT" and "DURATION requires DTSTART in a VTODO" constraints.
- **Alarms:** AUDIO/DISPLAY/EMAIL actions ("LOVI/DUGADA/FOZE") with ATTACH sound resource, DESCRIPTION body, SUMMARY subject, ATTENDEE recipients; TRIGGER related to START/END — §3.6.6.
- **Properties:** "TOVO/POZUKU" = PRODID/VERSION (both required), "GITI" = UID (globally unique, 255-octet persistence — the 255-octet UTF-8 clause), "LEDI" = TZID (not applied to UTC or DATE values), GEO as two SEMICOLON-separated FLOATs, METHOD/Content-Type "method" parameter pairing, mailto URIs per RFC 2368, BASE64 inline ENCODING per RFC 2045, URIs per RFC 3986 — all matching RFC 5545's citation set.

The only residual uncertainty is 5545 vs. 2445; the "this revision deprecates value X" language (e.g., THISANDPRIOR) and the 255-octet UID persistence text favor RFC 5545.
```

### O1b (as-served)

```
**Identification: RFC 5545 — iCalendar (Internet Calendaring and Scheduling Core Object Specification)**, with the obligations drawn from its normative MUST/MUST NOT sentences (largely §3, the content-line grammar, data types, recurrence rules, components, and properties). Confidence: **very high (~98%)**.

Reasoning, briefly:

- **Structural fingerprint**: content lines with folding/unfolding ([1–2]), COMMA-separated value lists, SEMICOLON-separated structured values and parameters, quoted-string rules for values containing COLON/SEMICOLON/COMMA, DQUOTE prohibition ([3–12]) — this is verbatim the iCalendar content-line model.
- **Obfuscated token mapping is transparent**: "gofa" = iCalendar object (delimiter-string pair at first/last line = BEGIN:VCALENDAR/END:VCALENDAR, [86]); "GISEMA=BASE64" = ENCODING=BASE64 ([20], [39–40]); "LEDI" = TZID (MUST NOT apply to UTC or DATE values, [34], [44], [80]); "MIPERI" = VTIMEZONE with "TAFAKO"/"MIPESO" = STANDARD/DAYLIGHT sub-components requiring DTSTART/TZOFFSETFROM/TZOFFSETTO ([110–119], [127-analog 112]); "SISUSI" = DTSTART; "BEPI"/"PAMI"/"BUZE"/"KUFA" = RRULE recur / FREQ / UNTIL / COUNT (FREQ required once, UNTIL and COUNT mutually exclusive, [50–70]); leap-second 60 rules and exact-duration computation ([45–47], [77]); TEXT escaping with backslash-n and BACKSLASH/COMMA/SEMICOLON escapes, COLON explicitly not escaped ([71–76]); "VENE"/"MITA"/"VOGOGO"/"SUMEBI" = VEVENT/VTODO/VJOURNAL/VFREEBUSY; "GEZO" = VALARM with ACTION values AUDIO/DISPLAY/EMAIL ("LOVI"/"DUGADA"/"FOZE", [128–138]) and TRIGGER related-to START/END semantics ([213–218]); "GITI" = UID with the 255-octet persistence and UTF-8 no-mid-sequence-truncation requirement ([203]); "TOVO"/"POZUKU" = PRODID/VERSION required at calendar level ([89]); geographic position as two SEMICOLON-separated FLOATs = GEO ([149]); "MAPU"/Content-Location correspondence and Content-Type "method" parameter pairing ([139–140], [198]).
- **Which revision**: citations to RFC 2368 (mailto), RFC 2045 (BASE64), and RFC 3986 (URI), plus the phrase "deprecated by this revision" ([26], [42], [78] — the UTC-offset date-time/time forms and a deprecated value, matching RFC 5545's deprecations relative to RFC 2445, e.g. THISANDPRIOR) point to **RFC 5545**, the revision of iCalendar, rather than the original RFC 2445. The RFC 3986 citation in particular rules out 2445 (which cited RFC 1738).

The rater pack's framing ("iCalendar at the transmitted calendar object" in rule 22) is consistent with this, but the identification above rests on the corpus text itself.
```
