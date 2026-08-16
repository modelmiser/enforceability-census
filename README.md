# enforceability-census

**What fraction of a specification's stated runtime obligations could a type
system have discharged?** This repository measures that question — the
*enforceability-class mix* of real obligation corpora — instead of arguing it.

> **The paper: [PAPER.md](PAPER.md)** — the repo-native consolidation of the
> codebook, the censuses, and the inter-rater studies. This repository
> is the artifact of record; no venue submission is planned. The censuses were
> run 2026-08-02 → 2026-08-15 as working artifacts and are preserved here with
> their corrections in place; numbers are quoted with their caveats or not at
> all.

## The taxonomy (the codebook)

[`codebook/classes.md`](codebook/classes.md) defines four classes by the
**shape of the predicate** — never the wording of the alert or the name of the
error:

| class | shape | type-eliminable? |
|---|---|---|
| DOMAIN | monotone predicate on one value, no history | yes — an enum/newtype |
| TYPESTATE | ordering obligation over one object's history | yes — typestate/session types across the boundary |
| REVOCABLE | a fact that was true and became false | no — needs a clock; this is the residue |
| THRESHOLD | inequality against a chosen number | no — a policy line, not a fact |

Two further classes — **CRYPTO-VERIFY** (verification requiring secret or
transcript material; the discriminator is the secret, not the word "crypto")
and **NEGOTIATION** (emptiness of a two-party intersection; never the chosen
value itself) — were forced by the TLS corpus and **graduated on 2026-08-13**
on a pre-registered falsifiability check (0 members each in the regenerated
Wayland corpus — two vocabulary hits, both hand-adjudicated false positives;
ordering witnessed by same-morning commit sequence — see the paper's
provenance note, §6) plus a stability criterion articulated at graduation time
(CV was item-for-item identical in every rater's recorded labels across four passes; NEG's
evidence is thinner — see the codebook's graduation record).

The codebook carries, in full, a **retraction** of its own first cross-layer
claim — kept verbatim because the failure (a classifier tuned by its author's
expectations, caught by error-sign analysis) is the methodological spine of
this work, and it is where rules 8 and 9 (classify on the predicate, enforce
that with a DISAGREE bucket) come from.

## The censuses

| corpus | n | headline | status |
|---|---|---|---|
| [`census/promql/`](census/promql) — awesome-prometheus-alerts | 1155 | 78.1% THRESHOLD, 21.3% REVOCABLE, 0.6% unclassified (all /1155); 0 TYPESTATE — censored by the query language | reconciled against primary sources; prior-art sweep found no comparable measurement |
| [`census/wayland/`](census/wayland) — declared protocol errors, core + extensions | 172 | **87.6% type-eliminable in shape** (149/170 client-facing; 86.6% on all 172; one protocol — versioned-boundary limit noted in codebook) | reconciled against primary sources at census time; the census-era checkout was not pinned, so the 172-item corpus is preserved as reported numbers, not as a regenerable artifact (the regenerable superset is n=216 and carries no headline) |
| [`census/tls13/`](census/tls13) — RFC 8446 §4 MUST/SHALL corpus | 204 | **80–83% type-eliminable in shape** (range over three valid raters, 79.9–82.8%; crypto core exactly 6/204, same items in every rater's recorded labels) | closed 2026-08-13 after a repair-and-re-rate loop with pre-registered predictions (passes 3–4); raters are LLM agents; disagreements unresolved by design |
| `census/tls13/tls13-alert-census.md` — TLS 1.3 alert vocabulary (30-min probe) | 25 | alert vocabulary censors typestate ~2.3× vs the MUST corpus | probe; tally corrected 2026-08-13; superseded by the §4 census for any headline |
| [`census/mls/`](census/mls) — RFC 9420 §5–§15 MUST/SHALL corpus | 127 | **≈57% type-eliminable in shape** (two raters: 56.7%/57.5% — ~25 points below TLS under the SAME instrument and recipe; ~18–19% PROCESS) | run 2026-08-13 under the frozen TLS pass-4 instrument, predictions pre-registered and publicly timestamped BEFORE any rater (M1 passed; M2–M4 failed and M5 failed 2 of its 3 clauses — graded against the author's model, per the pre-commitment); disagreements unresolved by design |
| [`census/quic-tls/`](census/quic-tls) — RFC 9001 §4–§8 MUST/SHALL corpus | 69 | **54–67% type-eliminable in shape** (quoted wide: 53.6%/66.7% — raw agreement 76.8%, the series' FIRST transfer-band breach, concentrated on PROCESS/TYPESTATE key-lifecycle splits; CV is 1.4%/2.9% — the crypto document's cryptography lives in non-normative grammar) | run 2026-08-13, frozen instrument, predictions publicly pre-timestamped; ALL FIVE K-predictions failed, graded against the author's model per the pre-commitment |
| [`census/quic-recovery/`](census/quic-recovery) — RFC 9002 §5–§7 MUST/SHALL corpus | 30 | **23.3% type-eliminable in shape** (identical in both raters; ~60% PROCESS) — the lowest of the frozen-instrument MUST-corpora | run 2026-08-13, frozen instrument, predictions publicly pre-timestamped (R1/R2/R4 passed; R3 failed by class disuse, R5 failed above-band); PROTOCOL DEVIATION disclosed: author pass abandoned after exposure to first-rater labels, replaced by a second blind rater |
| [`census/quic-family.md`](census/quic-family.md) — the three-document synthesis | 380 | within ONE protocol the share spans 23%→69% by document role; pooled family ≈61–65% (caveat in file) | the matched-family control: same protocol, era, authors — only document role varies |
| [`census/quic/`](census/quic) — RFC 9000 §2–§19 MUST/SHALL corpus | 281 | **≈67–69% type-eliminable in shape** (two raters: 66.9%/69.0%; TYPESTATE the largest class at ~46–47%; CV 1.1% — RFC 9001/9002 document boundary censors crypto and recovery) | run 2026-08-13 under the same frozen instrument, predictions publicly pre-timestamped (Q2/Q3/Q4 passed — Q4 confirmed the rule-3 spec-fixed-constant edge with THRESHOLD symdiff 15; Q1 failed marginally, Q5 failed its crisp-class clause on a new REVOCABLE/deadline edge); disagreements unresolved by design |
| [`census/ical/`](census/ical) — RFC 5545 (iCalendar) §3, the first NON-protocol corpus (data format; frozen v3 instrument) | 225 | **88.0% / 88.4% type-eliminable in shape** (two blind raters, one per family; unique-text secondary figure 85.9% / 85.9–86.4%); DOMAIN ~87% of the corpus, TYPESTATE collapses to 1/4 items, THRESHOLD/REVOCABLE/CV/NEG all 0/0; raw agreement **97.3%** — the repo's highest, cross-family (later tied by the v4-ical pair) | run 2026-08-15, predictions N1–N6 publicly pre-timestamped (`7b07de3`) before any rater; N1/N3/N5/N6 PASS both, N2 PASS Ai (exactly at the inclusive endpoint) / FAIL Xi (one item above), N4 PASS Ai / FAIL Xi (one cross-chunk split — the pre-stated cross-context mode, in a group the protocol did not name); three disclosed recipe refinements for the paginated data-format genre incl. example-data exclusion (the "Phoenix" MUST); the iTIP scheduling protocol (RFC 5546) is boundary-censored out, and grammar-stated obligations are invisible to a MUST census — both pre-registered |
| [`census/v4-tls/`](census/v4-tls) — first pass under instrument v4 (TLS §4 re-rated; NOT a new corpus, NEW instrument series) | 204 | v4 shares 81.9%/82.8% (within the closed v3 band; the v3 headline 80–83% stands and is never substituted); Av4-vs-Xv4 raw 92.2% — the corpus's highest, cross-family | run 2026-08-14 under pack blob `4891605…`; grades of the d3d4c2d pre-registration: V8 PASS both (188→DOMAIN, 189→REVOCABLE — decision rule 3's worked example flipped as predicted, TLS v3 THRESHOLD empties; example-settled by a retained seam example, weight discounted — see the protocol's correction), V6 PASS both, V4 FAIL in one rater (item 67), V7 FAIL both — rule 17 reached one sub-bucket ({30,31,32,56,57}) beyond the named items; guard boundary narrowed to 4 still-split items, not resolved |
| [`census/v4-completion/`](census/v4-completion) — v4 passes over MLS/QUIC/9001 (NOT new corpora, v4 instrument series) | 477 | v4 shares: MLS 59.1%/59.1%, QUIC 63.7%/68.7%, 9001 60.9%/58.0% (v3 headlines stand); agreement MLS 88.2% (v3: 85.0), 9001 **94.2%** (v3: 76.8 — the band-breaker now agrees best), QUIC 84.0% (v3: 85.1 — recorded as the honest negative; since decomposed by the quic-replication cell, see that row) | run 2026-08-14, six blind passes (fresh Claude + Grok per corpus), zero events; grades: V1/V3/V5 PASS both raters (V5's neither-rater 5/4 split exact in both families), V6 PASS (example-settled, discounted), V2 FAIL both on item 191 — the sole discriminating item, V7(a) 6/6 PASS, V7(b) 6/6 FAIL (rule 16 generalized past its named items: six THRESHOLD→DOMAIN; count-bound clause mis-designed — v5 owes redesign) |
| [`census/v4-ical/`](census/v4-ical) — v4 pass over the iCalendar corpus (NOT a new corpus, v4 instrument series) | 225 | v4 shares 88.9%/88.0% (v3 headline 88.0/88.4 stands); match vs the archived v3 pair 99.6%/98.7%; pair agreement 97.3% — departures from both archived v3 labels: 1 and 3 in 225 (same-model cross-version label changes: 2 and 6, indistinguishable from rater stochasticity by this design), and the two raters' PROCESS classes are item-for-item identical | run 2026-08-15, predictions W1–W5 pre-timestamped (`350fae2`); W1–W4 PASS both (THRESHOLD and REVOCABLE exactly 0 — the protocol-boundary repairs are inert here), W5 FAIL in the foreign rater — the SAME {43,79} group split, same cross-chunk mode, polarity reversed; owed PROCESS-churn lists EMPTY both directions both raters (rule 18's QUIC cost did not travel); both archived PROCESS-boundary splits (141, 203) closed to cross-family unanimity, unpredicted |
| [`census/quic-replication/`](census/quic-replication) — QUIC re-rated under v3 with the iCal roster (NOT a new corpus; the instrument×roster grid's third cell) | 281 | replication shares 67.6%/69.8% (census headline ≈67–69% stands, roster-robust); pair agreement **81.9%** — the grid's worst cell, so the v3-old→v4-new drop (85.1→84.0) decomposes as a −3.2 roster effect + a +2.1 instrument recovery on the roster-shape assumption (v4's QUIC "cost" reframed; bundle, roster-shape, and single-cell-stochasticity caveats in the report); THRESHOLD symdiff **14** vs the old pair's 15 — the wobble is the corpus's, not the roster's | run 2026-08-15, predictions Y1–Y6 pre-timestamped (`6698c4a`); Y1/Y2/Y3/Y5/Y6 PASS, Y4 FAIL by one item below its band; headline result: on the seven spec-fixed constants (+41) the role-ordered side assignment flipped item-for-item — old pair DOMAIN/THRESHOLD, new pair THRESHOLD/DOMAIN, with the fresh same-family rater on THRESHOLD in BOTH passes — a roster-invariant boundary with rater-correlated side assignment, the strongest evidence yet that v4 rule 16 repairs an instrument defect; chunk-6 doubled-emission transport deviation disclosed (no label ambiguous) |
| [`census/v5-quic/`](census/v5-quic) — first pass under instrument v5 (QUIC re-rated; NOT a new corpus, NEW instrument series) | 281 | v5 shares 67.3%/66.5% (v3 headline ≈67–69% and all v4 figures stand); pair agreement **89.7%** — the corpus's highest cell (prior: 85.1/84.0/81.9); anchor-match vs the v4 pair 92.1%/86.0% | run 2026-08-16 under pack blob `694e3a9…` (committed); registration `a35a60c` froze anchors, floors, and rule-24 audit verdicts BEFORE the raters; **all six graded clauses PASS in both raters — the series' first zero-fail sheet**, with its own qualifier: Z1/Z4-QUIC/Z6 were pre-downgraded comprehension checks, so the discriminating content is Z7 (49/49, 47/49 vs ≥42) + rule 23 (210/196 vs floor 192; 18/32 departures vs bound 36); sharpest unpredicted result: the v4 PROCESS churn on the monotonicity quartet {11,19,261,272} REVERSES to TYPESTATE under v5 (confounds named); item 105's disclosed recapture = explicit zero; Z4 overall pends TLS's first v5 pass |
| [`census/v5-completion/`](census/v5-completion) — v5 passes over TLS/9001/iCal (NOT new corpora, v5 instrument series) | 498 | v5 shares: TLS 84.8%/84.3%, 9001 59.4%/59.4%, iCal 93.8%/91.1% — the iCal figures quoted ONLY as the size of a measured instrument defect (all v3/v4 headlines stand); pair agreement TLS **93.6%** and 9001 **95.7%** = new corpus records, iCal 96.9% (its 97.3% record stands) | run 2026-08-16, six blind passes, zero events; registration `cf7e219` froze floors/bounds with measured failability BEFORE the raters; **every Z clause PASSES in every rater** — Z3's contested bridge lands TYPESTATE in both 9001 raters (same-family TORN on exactly that item), Z5's foreign rater overturns six archived TYPESTATE readings, **Z4 overall settled PASS** — but rule 23 catches real drift: iCal FAILs all four clauses (rule 21's in-grammar branch generalized to unknown-value tolerance duties, cross-family PROCESS→DOMAIN on {13,62,91,146,150,210}) = the pre-committed **instrument mis-design verdict on the format genre**; TLS 23(b) FAIL in one rater by one item; 9001 clean (both raters clear the floor no measured prior rater cleared); v6 docket: a scope boundary for rule 21 branch 1 |
| [`census/v6-pass/`](census/v6-pass) — first v6 pass over iCal/TLS/QUIC (NOT new corpora, v6 instrument series) | 710 | v6 shares: iCal **88.9%/88.9%** (reverted to the pre-conviction anchor band — the v5 elevation was the defect's size, now measured twice), TLS 81.4%/81.9% (inside the closed v3 band), QUIC 65.1%/65.1%; iCal pair agreement **98.7% raw = repo record** (prior 97.3%; claim-granularity record remains 9002's 100%) | run 2026-08-16, six blind passes, zero events; registration `e285755` pushed before any rater with the series' harshest bound (iCal both-anchor departures ≤ ZERO) — and iCal passed ALL FOUR clauses in both raters at exactly that bound; J1/J2/J3 recognition reversions transmit in both families; **J4's precision half FAILS in both raters** (150 → PROCESS; 62 holds DOMAIN — the measured boundary runs between validity and precision triggers, v7 docket); **TLS 23(a)+(b) FAIL in the foreign rater** (132 vs 134; 11 vs 6 — a bound the same-family rater passed exactly at the edge): guard-bucket + declined-item churn, 2-of-11 eliminable-ward, the FAIL stands as graded; steer-ledger settlement: the two mode-conditioned items (TLS 64, QUIC 232) reverted PROCESS-ward in all four readings; QUIC quartet+269 reversal holds in a fourth consecutive rater pair |
| [`census/foreign/`](census/foreign) — cross-family replication of the TLS §4 corpus (NOT a new corpus) | 204 | foreign quotients 76.5% (GPT-5.6 Sol) / 80.9% (Grok 4.6) vs Claude band 79.9–82.8%; Grok-vs-Claude agreement ABOVE the intra-family range (91.7% raw / 98.0% eliminable-vs-not); CV set 6/6 in every rater ever | run 2026-08-13, frozen instrument, predictions publicly pre-timestamped before any foreign rater (F1/F3/F5 passed; F2/F4 failed — F2's predicted degradation failed to appear); attacks the family-bias half of limitation 6 only; the corpus-shared-prior half needs a non-LLM rater |

**Read the caveats before quoting any number.** Every corpus censors some
class (rule 7); percentages are never comparable across layers or across
error-code granularities; the Wayland headline depends on classifier
vocabulary fitted to its corpus (the codebook's retraction addendum makes
reporting that dependency mandatory); the TLS headline is a *range* (three
raters, disagreements unresolved by design — see the pass 3/4 reports for
why the loop stopped where it did).

## Regenerating corpora

The classifiers ship; the corpora they consume are regenerable and not
vendored:

- **PromQL**: clone [`awesome-prometheus-alerts`](https://github.com/samber/awesome-prometheus-alerts)
  and feed the merged rules YAML to the classifier (needs PyYAML):
  `python3 census/promql/promql-classifier.py <rules.yml> out.json`
- **Wayland**: extract declared `<error>` entries, then classify:
  `python3 census/wayland/extract-corpus.py corpus.json <wayland>/protocol/wayland.xml <wayland-protocols>/{stable,staging,unstable,experimental}`
  then `python3 census/wayland/wayland-classifier.py corpus.json out.json`
  (sources: [`wayland`](https://gitlab.freedesktop.org/wayland/wayland),
  [`wayland-protocols`](https://gitlab.freedesktop.org/wayland/wayland-protocols)).
- **RFC 8446 §4**: `rfc8446_s4_musts.txt` is checked in (204 sentences,
  regenerable by the extraction recipe in `rfc8446-s4-census.md`).

## Open work

1. ~~Codebook repair~~, ~~re-rating passes~~, ~~Wayland falsifiability
   check~~, ~~class graduation~~, ~~PAPER.md~~ — all closed 2026-08-13
   (codebook v2/v3; passes 3–4 with pre-registered predictions and a stop
   whose interpretation was pre-registered; CV/NEG graduated; paper
   drafted and taken through a publish-gate cold round). The measured
   residual: the codebook's crisp-discriminator classes transmit with zero
   or near-zero rater variance (CRYPTO-VERIFY and META identical in every
   rater's recorded labels; one recorded THRESHOLD→REVOCABLE flip), while
   raw item agreement between raters floors in the
   low-to-mid 80s (D vs A: 83.8%; bounded B–D as low as 80.9%), including
   15 items where two fresh raters
   agree on the same alternative label against the original ratings; that
   error bar is reported, not adjudicated away.
2. ~~Optional second security RFC~~ — DONE 2026-08-13: the MLS census
   (`census/mls/`) turned one data point into a matched-method comparison;
   the type-eliminable share is NOT a security-protocol constant (TLS
   80–83% vs MLS ≈57%). Its disagreement residue names a candidate rule 15
   (capability-compatibility tie-break) for any future instrument version.
3. ~~A third corpus under the same frozen instrument~~ — DONE 2026-08-13:
   the QUIC census (`census/quic/`) lands at ≈67–69%, between MLS and TLS —
   consistent with a spectrum (57 → 67–69 → 80–83), each span's position
   explainable by what it states as obligations (a post-hoc reading; see
   the report's headline caveat). Its residue adds a rule-16
   candidate (spec-fixed constants, THRESHOLD symdiff 15) and a
   deadline-duty edge to the rule-15 candidate from MLS.
4. ~~Paper integration of the QUIC census~~ — DONE 2026-08-13. Then the
   QUIC document-family completion (RFC 9001 + 9002) was run the same day:
   see `census/quic-family.md`. Within one protocol the share spans
   23%→69% by document role — the strongest evidence yet for the
   what-the-span-states reading, measured under the matched-family
   control.
5. ~~Paper integration of the family completion~~ — DONE 2026-08-13. Then
   the cross-family replication (`census/foreign/`) re-rated the TLS
   corpus under two foreign frontier families the same day: family-bias
   weakened, CV family-invariant, and a candidate rule 17 (scope of
   "occurrence" under rule 10) measured from nine items of cross-family
   consensus.
6. ~~Instrument v4 as a deliberate, pre-registered version bump~~ — DONE
   2026-08-14: rules 15–19 + predictions V1–V8 (`codebook/classes.md`),
   then the first v4 pass (TLS, `census/v4-tls/`): V8 and V6 passed in
   both raters, V4 and V7 failed as pre-committed — the failures grade
   the author's model of rule 17's reach and are the record.
7. ~~v4 passes over MLS/QUIC/9001~~ — DONE 2026-08-14
   (`census/v4-completion/`): every v4 prediction is now graded. Wins:
   the key-lifecycle repair (9001 76.8→94.2 agreement), V5 exact in both
   families. Losses, kept as graded: V2 on its only discriminating item;
   V7(b) 6/6.
8. ~~Paper integration of the v4 series~~ — DONE 2026-08-14: PAPER.md
   §6.1 carries the amendment, all eight prediction grades, and v4's
   measured cost (QUIC) next to its gains.
9. ~~A NON-protocol corpus~~ — DONE 2026-08-15 (`census/ical/`): RFC
   5545 §3 at 88.0/88.4%, above every protocol span; PAPER integration
   DONE 2026-08-15 (§4.8). A HUMAN-rater replication
   remains the only probe that reaches the corpus-shared-prior half of
   limitation 6; the v5 amendment is now CUT — 2026-08-15,
   `codebook/classes.md` rules 20–24 with pre-registered predictions
   Z1–Z7 — covering everything the docket owed: the V7 count-bound
   redesign (rule 23), the ignore-duty seam (rule 21; QUIC 191), the
   response-duty seam (rule 20; TLS 67), the carved-out pair
   adjudicated (rule 20; QUIC 63 → THRESHOLD, RFC 9001 item 15 →
   TYPESTATE on the amendment's one disclosed contested bridge), the
   within-object boundary (rule 22; iCal 192–194 — CONFIRMED live by
   the v4-ical pass, `census/v4-ical/`), and registration hygiene
   codified (rule 24); the FIRST v5 pass ran 2026-08-16 on QUIC
   (`census/v5-quic/` — all six graded clauses passed both raters,
   the series' first zero-fail sheet, with the standing qualifier
   that Z1/Z4-QUIC/Z6 were pre-downgraded comprehension checks and
   the discrimination lived in Z7 + rule 23); the completion passes
   ran 2026-08-16 (`census/v5-completion/` — every Z clause passed
   incl. Z3's contested bridge and Z4-overall, while rule 23 caught
   an undisclosed eliminable-ward reach of rule 21 on the format
   genre: iCal failed all four clauses, the pre-committed mis-design
   verdict); the v5 PAPER integration is DONE — 2026-08-16, PAPER.md
   §6.2 ("The cycle closes"); the v6 amendment is now CUT —
   2026-08-16, `codebook/classes.md` rule 25 with pre-registered
   predictions J1–J6 — drawing the boundary the conviction owed
   (recognition predicates are receiver-relative; branch 1 requires
   a unit-local trigger), with the mixed-evidence sibling shapes
   declined and recorded, J4 (iCal 62/150 → DOMAIN, siding with two
   readings against four) as the contested edge, and integer
   leakage floors J5/J6 measured against the pre-conviction anchor
   pairs; the FIRST v6 pass ran 2026-08-16 (`census/v6-pass/`,
   registration `e285755` pushed before any rater, J4 downgraded to
   a comprehension check at registration by the pre-committed
   trigger-(c) ruling): the repair HOLDS on the corpus that
   convicted it — iCal passes all four clauses in both raters at a
   registered bound of ZERO departures, shares revert to the anchor
   band (88.9 ×2), and the pair sets the repo raw-agreement record
   (98.7%) — while J4's precision half fails in both raters (iCal
   150; the boundary runs between validity and precision triggers)
   and the TLS cell fails both rule-23 clauses in the foreign seat
   (guard-bucket + declined-item churn; the FAIL stands as graded);
   v7 docket (deliberate, unqueued): the 150 precision-trigger
   wording, and the mode-conditioned pair's consistent PROCESS-ward
   reversion (TLS 64, QUIC 232); the v6 PAPER integration is DONE —
   2026-08-16, PAPER.md §6.3 ("The verdict answered"); the v4-ical null test
   is DONE (THRESHOLD stayed exactly 0 under v4; rule 18's churn did
   not travel) — the genre-vs-model question (properly genre-vs-roster-bundle) about
   QUIC's wobble is now ANSWERED (`census/quic-replication/`): the
   wobble reproduced at symdiff 14 with the new roster, the
   role-ordered side assignment flipping item-for-item on the
   spec-fixed constants — the strongest evidence yet that rule 16
   repairs an instrument defect, not an old-roster artifact; the
   completed grid reframes v4's QUIC cost as a +2.1-point instrument
   recovery under a −3.2-point roster effect, on the roster-shape
   assumption with all three of the registration's caveats.

## License

MIT — see [LICENSE](LICENSE).
