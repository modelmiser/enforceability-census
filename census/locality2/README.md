# Locality passes 2: does the boundary criterion generalize? (registration)

2026-08-16 · **Pre-registered before any witness is constructed.** This
registration is append-only after push; corrections, if ever needed, go in
marked brackets preserving the original wording.

## What is being tested

The first locality study (`census/locality/`, PAPER §6.6) formalized
codebook rule 16's litmus as datum-locality and found, on the TLS-204
archive, that "some local rung witnessed" coincides with the archive's own
eliminable-vote majority on 40 of 44 items, with exactly the four
pre-named exceptions. One corpus is one point. This registration runs the
same criterion — same witness forms, same lemma, same one-shot discipline
— over the two remaining large boundary masses in the archive:

- **RFC 5545 §3 (iCalendar, n = 225, ten archived raters)** — the format
  genre, the crispest corpus in the repository (203/225 unanimous across
  all ten raters), whose small dissent mass includes items 62 and 150 —
  the validity/precision readings the rule-25 arc singled out as
  NON-recognition-predicated — and the census's one recurring soft
  boundary (the 192–194 cross-property cluster).
- **RFC 9000 §2–19 (QUIC, n = 281, twelve archived raters)** — the
  transport genre, the largest absolute dissent mass in the archive
  (163/281 unanimous),
  carrying the THRESHOLD-vs-TYPESTATE flow-control cluster, the
  cross-connection 0-RTT family, and the capability/liveness boundary.

The cross-corpus thesis being tested: **the correspondence between formal
locality and the archive's eliminable boundary is genre-dependent in its
RATE but class-structured in its SHAPE** — where the two part ways, they
part along nameable families predictable from sentence structure, not
item-by-item noise. TLS needed four named exceptions in 44 items. The
tables below pre-name three exceptions of 23 for iCalendar and nineteen
of 49 for QUIC — the QUIC prediction is that the correspondence *visibly
bends* there, in two specific class-shaped ways, and nowhere else.

No new raters are seated. No number produced here joins any census
series. Both passes reuse the first study's definitions verbatim except
where a granularity is genre-specific; differences are stated, not
implied.

**Relation to limitation 6** is inherited from the first study: a
correspondence between agreement boundaries and an independently
checkable semantic property is evidence against a *merely lexical* shared
prior, and cannot exclude a prior about the property itself; only the
human pass closes any part of that. A second and third corpus sharpen the
instrument: if the correspondence were an artifact of one corpus's
structure, unrelated genres should not reproduce its class-shaped
exception pattern.

## Definitions (fixed before construction)

The **reading**, **local predicate**, **YES-witness (validator)**,
**NO-witness (distinguishing pair)**, **lemma**, **rung**, **item
outcome**, and **FAILS asymmetry** are exactly the first study's
(`census/locality/README.md` §Definitions), with the granularity pair
instantiated per corpus:

**iCalendar granularities.**
- **prop** — ONE unfolded content line: property name, parameters, value,
  plus the enclosing component-type chain (e.g., VALARM-in-VEVENT) as
  metadata. Nothing else.
- **object** — ONE complete iCalendar object: its ordered components and
  content lines, start to end. A prop-local predicate is object-local
  once its line is designated; the converse fails exactly where a check
  spans lines — that gap is what the two rungs measure.

**iCalendar channels:** `other-props` (other content lines of the same
object — the fine-granularity context), `other-artifacts` (other
iCalendar objects and iTIP scheduling transactions), `party-conduct`,
`deployment-policy` (own configuration, including an application's
recognized-vocabulary set), `private-intent`, `generation-process`,
`world-fact` (facts about the world outside any exchange: leap-second
history, actual time-zone law), `clock`.

**QUIC granularities.**
- **pkt** — ONE UDP datagram as received: source/destination address and
  port, sender role, and its decrypted content — the coalesced QUIC
  packets with their header fields and contained frames. Encryption is
  abstracted away, as in the first study.
- **conn** — the ordered bidirectional sequence of such datagrams of ONE
  connection (Version Negotiation and Retry included, through close).
  Both endpoints' transport parameters are conn-carried: they travel in
  the handshake.

**QUIC channels:** `other-dgrams` (other datagrams of the same connection
— the fine-granularity context), `prior-connection` (other connections of the same endpoint, prior or
concurrent), `secret-material`,
`clock`, `party-conduct`, `counterparty-config`, `deployment-policy`,
`private-intent`, `generation-process`, `network-path` (path properties:
PMTU, address reachability, middlebox behavior).

## Item set (mechanical; derivation tool ships with this registration)

`profile2.py` parses every archived full label map for both corpora —
ten for RFC 5545 (Ai, Xi; Av4i, Xv4i; Av5i, Xv5i; Av6i, Xv6i; Av7i,
Xv7i), twelve for RFC 9000 (Aq3, Bq3 = the census report's A″, B″; Aq,
Xq; Av4q, Xv4q; Aq5, Xq5; Av6q, Xv6q; Av7q, Xv7q) — normalizes label
spellings, strips torn flags, and verifies the parse against
**thirty-seven published numbers as known-answer tests**: fifteen for
iCalendar (five era-pair raw agreements + ten per-rater eliminable
counts) and twenty-two for QUIC (six era-pair + four cross-era raw
agreements + twelve per-rater eliminable counts), with a perturbation
self-test. Counts stated in the reports as percentages enter as the
uniquely implied integer (iCal v6: 222 pair / 200+200 eliminable; QUIC
v4: 236 pair; QUIC v6: 251 pair / 183+183 eliminable); each band admits
exactly one numerator at the published corpus size.

**Instrument-era disclosure.** Each roster spans five instrument
generations — two raters per era for iCalendar; QUIC's v3 era seats
four (the census pair and the replication pair), its later eras two. Both corpora's first pairs rated under
the frozen v3 pass-4 blob `a08febba…` (for QUIC, four raters did: the
census pair and the replication pair). The v5 iCalendar pair (Av5i,
Xv5i) rated under the instrument whose iCalendar application the
v5-completion report itself graded as the **mis-design measurement**
(rule 21's undisclosed reach, later narrowed by rule 25); their labels enter as
rater data with that provenance noted — the same treatment the first
study gave TLS rater C. Part of both contested masses is era-correlated
(iCal 62's DOMAIN votes are exactly the v5/v6/v7 raters, while 150's are
the v5 pair alone, reverting at the v6 repair; the QUIC limit family's
THRESHOLD votes arrive with rule 16 at v4 — TYPESTATE in all four
v3-era raters for all thirteen limit-family items, THRESHOLD in seven
of the eight v4-and-later raters for twelve of them; item 18 seats six
of eight, Xv4q and Xv7q holding TYPESTATE). The
selection rule does not condition on the cause of dissent; the report
will include per-era breakdowns for contested items.

**Selection thresholds (per-corpus, disclosed).** A rater departs on an
item when its label differs from the item's modal label across the
roster.
- **iCalendar — contested = ≥2 of 10 departures (14 items):** 13, 43,
  62, 77, 79, 91, 116, 146, 150, 185, 192, 193, 194, 210. The corpus is
  crisp enough to take its ENTIRE multi-rater dissent mass; the excluded
  9:1 tier (items 14, 16, 22, 25, 27, 28, 141, 203) cannot seat a second
  eligible reading under the ≥2-votes rule below, so the cut loses no
  eligible structure.
- **QUIC — contested = ≥5 of 12 departures (32 items, minus one META
  exclusion below = 31).** QUIC's ≥2-departure mass is 99 items — nearly
  twice the TLS archive's 53 under the same rule, and 3.7 times the
  27-item contested set the first study actually witnessed — and
  witnessing it whole is not feasible in one pass. The cap takes the MOST contested tiers and enumerates what it
  drops (no silent caps): d=4 (23 items: 61, 68, 86, 87, 93, 96, 105,
  129, 132, 135, 165, 185, 186, 187, 188, 203, 214, 229, 232, 244, 246,
  269, 279), d=3 (19 items), d=2 (25 items); the d=3/d=2 memberships are
  derivable from the shipped tool (`profile2.py quic --profile`). A
  reader extending the witness pass to a dropped tier extends the
  study; nothing about the dropped tiers is claimed here.
- **Stable samples** (per unanimous class, first 3 by md5 of sentence
  text — the census self-audit's ordering, as in the first study):
  iCalendar DOMAIN {63, 84, 143}, PROCESS {69, 118, 1}, U {201, 200, 7}
  — the corpus has NO unanimous TYPESTATE, THRESHOLD, CV, NEG,
  REVOCABLE, POLICY, or META items, so the sample is three classes.
  QUIC DOMAIN {236, 249, 49}, TYPESTATE {171, 78, 58}, PROCESS {207,
  107, 92}, THRESHOLD {94, 62, 83}, U {80, 119, 75}, NEG {40}, POLICY
  {230, 34}, META {280, 53 — excluded below}.
- **META exclusions (QUIC 53, 280, 281):** by the first study's item-117
  criterion — the obliged party is a specification or extension author,
  no runtime party, so neither witness form applies. For 281 the exclusion is itself a
  judgment call this registration is making, not reporting: five of
  twelve raters (PROCESS 3 + TYPESTATE 2, against META 7) read a runtime duty
  into it, unlike TLS 117 and QUIC 53/280, which are unanimous META —
  and the call drops a d=5 item from a set whose rationale is "most
  contested". A reader contests it by shipping a runtime-party witness
  for 281 under the registered forms; the registration predicts none
  exists whose obliged party is not the extension's SPECIFICATION. **Witness sets: iCalendar 23 items, QUIC 49 items.**
- **Duplicate-text disclosure:** iCalendar items 43 and 79 are
  byte-identical sentences (the census's own N4 split-group). Both are
  in the witness set; prediction IC5 turns the coincidence into a
  control.

**Eligibility.** As in the first study: a witness is *eligible* for the
rungs implied by the classes holding ≥2 of the item's votes, under the
registered vote→rung maps. Genre-specific assignments, with their rules:

- iCalendar: DOMAIN→prop unless the compliance criterion references
  content outside one content line (another property, an occurrence
  count over the object) — then object (items 116, 143, 185, 192, 193,
  194); TYPESTATE→object for in-object cross-property state (192–194),
  nonlocal where the referenced state is cross-artifact (185's
  inheritance across the scheduling transaction); PROCESS, U, POLICY →
  nonlocal.
- QUIC: DOMAIN→pkt; TYPESTATE→conn; THRESHOLD→per-item by rule 16's own
  branches on where the quantity and bound live — conn when both are
  conn-carried (peer-advertised limits, cumulative counts: 4, 9, 10, 17,
  18, 26, 27, 62, 83, 94, 142, 254, 255, 258, 259, 262, 263), nonlocal
  when clock- or path-valued (109, 190); NEG, PROCESS, CV, REVOCABLE,
  POLICY, U → nonlocal.

The tables are embedded in `check_witnesses2.py` and re-derivable from
`profile2.py <corpus> --eligibility`; the checker cross-checks them
against the derivation on every run, unconditionally. Extra-eligible
witnesses are permitted, marked `eligible: false`, and excluded from item
outcomes and from L.

**Anaphora designations (disclosed heuristic, as with the first study's
best-candidate message designations).** Three selected sentences carry
demonstratives whose antecedents the corpus extraction did not capture:
iCal 143 "This property" (a calendar-level Conformance clause; the
validator designates VERSION as best candidate — the adjacent item 142
carries PRODID's parallel "The property" clause — and the reading notes
the check's shape is property-independent), iCal 192/193 "This property"
(designated RECURRENCE-ID, whose description carries this text), QUIC 236
"this transport parameter" (designated preferred_address, whose
connection-ID field the sentence constrains). Each witness states its
designation; a reader who thinks the antecedent is otherwise attacks the
quote, which is the designed challenge surface.

## Non-circularity and elasticity discipline

Identical to the first study, and inherited with its scar: the author
constructs witnesses unblinded to the archive; everything mechanical
(arity, vectors, pair structure, outcome derivation, all grading) is
frozen in `check_witnesses2.py` before construction; every judgment ships
with quoted spec text. The selective-elasticity residue is controlled by
publication-for-challenge — each FAILS record names the reading, rung,
and blocking channel it failed on, and a reader who ships the denied
artifact refutes the record directly. That challenge interface is not
hypothetical: it fired once in the first study, at the gate, on item 52.
New in this registration, and frozen now because it can only be frozen
now: the checker mechanically enforces FAILS COVERAGE — every registered
eligible rung must either be witnessed or carry a FAILS record naming
its blocking channel. An unwitnessed rung cannot be silently dropped;
the choice at construction time is a shipped artifact or a shipped,
challengeable impossibility claim. One further disclosure for the
report: the three corpora's contested selections run at different
depths (TLS d≥4 of 14, iCalendar d≥2 of 10, QUIC d≥5 of 12), so any
cross-corpus comparison of mismatch RATES compares differently deep
dissent tiers and will say so.
Quote fidelity follows the first study's limitation 6: corpus sentences
are quoted corpus-verbatim, with any completion from RFC text in marked
brackets — both truncation and completion of a quote are defects.

One-shot: predictions are frozen at push; construction begins only
after. A failed prediction grades the author's semantic model and
licenses no revision, no re-selection, and no relabeling of any archived
pass. Witness artifacts stand or fall individually on their own quotes
regardless of prediction outcomes.

## Predictions — iCalendar (append-only after push)

- **IC1 — stable DOMAIN, per-item exact, 3/3 strict: 63 → {prop}, 84 →
  {prop}, 143 → {object}.** The class scheme's single DOMAIN label spans
  two rungs: a BYDAY/FREQ co-constraint and a sign-character rule live
  inside one content line; a once-per-object cardinality does not. The
  registered claim is that the split is witnessable, which the class
  scheme cannot see (the first study's CV-split analog, in the format
  genre).
- **IC2 — stable PROCESS {69, 118, 1} and U {201, 200, 7}: outcome
  {nonlocal}, 6/6 strict.** Expected channels (reported, not graded):
  PROCESS → party-conduct (ignore/generate/unfold conduct); 200, 201 →
  generation-process (global uniqueness spans all objects ever
  generated); 7 → private-intent (whether two values are "language
  variants of the same value" is the generator's intent).
- **IC3 — contested single-rung, exact match, floor ≥10/12:** {13, 43,
  62, 77, 79, 91, 146, 150, 210} → {nonlocal}; {192, 193, 194} →
  {object}. The reasoning, disclosed: the nine are conduct-, intent-, or
  world-guarded duties whose eligible prop readings are predicted to
  FAIL on named channels — 13, 91, 146, 210 (ignore/treat-as conduct
  conditioned on the application's own recognized set: party-conduct,
  deployment-policy), 150 (accept-conduct), 62 (ignore-conduct on a
  prop-local trigger), 43, 79 (the fixed-time duty guarded by what the
  generator meant to communicate: private-intent), 77 (whether an
  instant is a real positive leap second: world-fact). 192–194 are the
  census's soft boundary and are predicted ONE-rung: the DOMAIN-vs-
  TYPESTATE fight is vocabulary — both classes point at the same
  within-object cross-property consistency check, with a prop-level pair
  (channel other-props) showing no single line decides it.
- **IC4 — contested multi-rung {116, 185}: ≥2 rungs witnessed, floor
  2/2 strict.** Predicted sets (reported by the grader): 116 {object,
  nonlocal} — the parenthetical's UNTIL-equals-last-generated-onset
  consistency needs the observance's DTSTART (object), while "known to
  have an effective end date" needs time-zone law (world-fact). 185
  {object, nonlocal} — co-listed delegator/delegate ATTENDEE consistency
  (DELEGATED-FROM/DELEGATED-TO) is object-checkable; inheritance from
  the delegating REQUEST itself crosses artifacts (other-artifacts).
- **IC5 — duplicate-text control (mechanical).** Items 43 and 79 are
  byte-identical (asserted at load). L is computed from the sentence, so
  the study MUST produce outcome(43) = outcome(79). The archive's E
  differs across the two positions (5 vs 7 DOMAIN votes of 10) — so at
  most one can match, and the mismatch is predicted to land on 79 and
  not 43. A same-sentence pair whose E straddles the majority line is a
  measured demonstration that the archive's headline boundary carries
  position noise no sentence-level semantic property can track — and
  the grader checks all three parts.
- **IC6 — correspondence.** L(i) = "some local rung (prop or object)
  witnessed among eligible readings"; E(i) = "DOMAIN+TYPESTATE hold a
  strict majority of the 10 votes" (≥6). Prediction: L = E on every item
  EXCEPT the named exceptions **{62, 77, 79}** — all one shape: duties
  whose TRIGGER is datum-local but whose compliance is conduct or
  world-guarded, pulling eliminable votes — the trigger/duty split that
  rule 25 turned into its datum-local litmus, here witnessed rather
  than voted on (only 62 among the three is even adjacent to the v5
  conviction; the conviction itself sat on the recognition nine). Grading: zero
  unnamed mismatches AND ≥2/3 named realized. Scope disclosure: the six
  stable PROCESS/U items are eligible only for nonlocal, so L is false
  by construction and E false in the archive — the universal half is
  live on the other 17 items.

## Predictions — QUIC (append-only after push)

- **QC1 — stable DOMAIN {236, 249, 49}: outcome {pkt}, 3/3 strict.**
  Named risk: 49's required parameters come from BOTH endpoints; the pkt
  reading rides on the sender-role metadata (each endpoint's own
  transport-parameter block must carry its role's required IDs) — if
  that reading is not defensible, QC1 fails.
- **QC2 — stable TYPESTATE, per-item exact, 3/3 strict: 171 → {conn},
  78 → {conn}, 58 → {} (empty).** The empty set is this registration's
  strongest single claim: item 58 is TYPESTATE-unanimous across all
  twelve raters, yet its binding information ("the remembered values of
  the parameters") lives in a PRIOR connection — the eligible conn
  reading is predicted to FAIL (channel prior-connection, FAILS record
  shipped), and no other rung is eligible. Any reader (or the gate's
  reviewer) who constructs a conn validator for 58 refutes the
  prediction outright. For 78, the immediate-use half is conn-local
  (Retry then token-bearing Initial in one connection's datagram
  sequence); the
  cannot-reuse-in-subsequent-attempts half is predicted to FAIL at conn
  on prior-connection, disclosed here, with the item's outcome riding on
  the first half.
- **QC3 — stable NEG {40}, POLICY {230, 34}, PROCESS {207, 107, 92},
  U {80, 119, 75}: outcome {nonlocal}, 9/9 strict.** Expected channels
  (reported, not graded): 40 counterparty-config; 230, 34
  deployment-policy; 207, 107, 92 party-conduct; 80, 119, 75
  generation-process.
- **QC4 — stable THRESHOLD, per-item exact, 3/3 strict: 94 → {conn},
  83 → {conn}, 62 → {conn}.** All three are THRESHOLD-unanimous with
  conn-carried quantities and bounds (anti-amplification accounting;
  the 4096-byte CRYPTO buffering floor read as "must not signal
  buffer-exceeded while out-of-order data ≤ 4096"). Together with QC5's
  limit family, this grounds the L∧¬E exception family in QC7.
- **QC5 — contested single-rung, exact match, floor ≥24/28:**
  {4, 9, 10, 17, 18, 26, 27, 254, 255, 258, 259, 262, 263, 235, 142} →
  {conn}; {54, 55, 59, 29, 32, 33, 81, 84, 109, 138, 23, 128, 190} →
  {nonlocal}. The reasoning, disclosed: the flow-control/limit family is
  QUIC's largest disagreement cluster, and its THRESHOLD-vs-TYPESTATE
  fight is predicted to be VOCABULARY — the advertised limit and the
  cumulative quantity are both conn-carried, so both classes point at
  one conn-local check (the analog of the first study's guard-cluster
  dissolution). 235's pkt-eligible reading is predicted to FAIL
  (the transport parameter and the connection-ID choice may travel in
  different datagrams: other-dgrams); 142's trigger and response sizes
  are both conn-visible, with the maintains-state guard reported as
  extra structure. The nonlocal thirteen fail their eligible local
  readings on named channels: 54, 55 prior-connection (remembered
  values); 59 counterparty-config ("cannot be supported"); 29
  party-conduct (internal forgetting); 32, 33 deployment-policy
  (supported-version set; the section's config-dependent circumstances);
  81 secret-material (token integrity keys); 84 prior-connection
  (replay across connections); 109 clock; 138 deployment-policy (a
  property of the deployment's encoding scheme, not of one datagram);
  23 prior-connection (the OTHER concurrent connections); 128
  private-intent/party-conduct ("wishes", "if it is able"); 190
  network-path (PMTU determination).
- **QC6 — contested multi-rung {152, 162, 144}: ≥2 rungs witnessed,
  floor ≥2/3.** Predicted sets (reported by the grader): 152 {pkt, conn}
  (the abstract packet-number bound 2^62−1 is field-local; ceasing to
  send after reaching it is conn-visible); 162 {conn, nonlocal}
  (no ACK before the acknowledged packet number appears is conn-local
  ordering; "all frames contained in the packet have been processed" is
  internal conduct); 144 {conn, nonlocal} (a conn-visible
  semantic violation must be followed by CONNECTION_CLOSE — conn; "corruption
  of state that affects an entire connection" is internal).
- **QC7 — correspondence, with the bend pre-named.** L(i) = "some local
  rung (pkt or conn) witnessed among eligible readings"; E(i) =
  "DOMAIN+TYPESTATE strict majority of the 12 votes" (≥7). Prediction:
  L = E on every item EXCEPT nineteen named exceptions in two
  rule-shaped families — **(a) L∧¬E, 16 items** {4, 9, 10, 17, 18, 26,
  27, 254, 255, 258, 259, 262, 263, 94, 83, 62}: the THRESHOLD family
  with conn-carried quantities and bounds — the archive's eliminable
  line (DOMAIN+TYPESTATE) excludes THRESHOLD even where the check is
  formally conn-local, so the headline boundary systematically
  UNDERCOUNTS locality here; **(b) ¬L∧E, 3 items** {32, 58, 59}:
  eliminable-vote majorities on duties whose binding information leaves
  the connection (a config-guarded trigger; cross-connection remembered
  state; a capability guard) — the boundary OVERCOUNTS locality there.
  Grading: zero unnamed mismatches AND per-family sub-floors — ≥13/16
  of family (a) AND ≥2/3 of family (b) realized (a single overall floor
  would let the three-item family fail invisibly behind the sixteen).
  Both failure directions are live. Scope disclosure: twelve items are
  eligible only for nonlocal ({81, 84, 109} and the nine QC3 items), so
  no mismatch is possible there — the universal half is live on the
  other 37 items.

**Interpretation, pre-committed.** IC1–IC2 and QC1–QC4 grade whether the
criterion reproduces each stable archive (comprehension floor, plus the
class-splitting structural claims). IC3–IC4 and QC5–QC6 grade the central
thesis on the contested mass. IC5 is a designed control on E's position
noise. IC6/QC7 grade the cross-corpus form of the first study's headline:
correspondence with class-shaped, pre-named divergence. Failures grade
the author's semantic model and the thesis — not the raters, not the
codebook, not any archived number.

## Grading

`check_witnesses2.py` (shipped with this registration, before any witness
exists) validates witness structure mechanically, derives item outcomes,
grades every clause above, and self-tests its own rejection paths, FAILS
validation, per-clause grading mutants, and the embedded
eligibility/E_MAJ tables against the archive derivation on every run —
unconditionally. The witness pass produces `witnesses_ical.py` and
`witnesses_quic.py` (the artifacts under test) and a report
`rfc5545-rfc9000-locality.md`. Run:
`python3 census/locality2/check_witnesses2.py`.
