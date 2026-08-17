# Locality study: is the transmissibility boundary a semantic property? (registration)

2026-08-16 · **Pre-registered before any witness is constructed.** This
registration is append-only after push; corrections, if ever needed, go in
marked brackets preserving the original wording.

## What is being tested

Seventeen raters across six model families have now classified the same
specification corpora, and the disagreement mass keeps landing on the same
boundaries. The working hypothesis, stated informally in the paper's
transmissibility discussion and operationally in codebook rule 16's litmus
("could the check be re-run on the lone datum in a vacuum and get the same
answer?"), is that the boundaries raters transmit reliably coincide with a
*semantic* property of the obligation — whether its compliance criterion is
decidable from a bounded unit of protocol data — and that the boundaries
raters contest are the places where that property is itself ambiguous.

This study makes the property formal and tests it against the archived
disagreement mass of the RFC 8446 §4 corpus (204 items, fourteen archived
full label maps). No new raters are seated. The instrument is not a
codebook but a pair of **checkable artifact forms**: a locality claim is
established by shipping an executable validator, and a non-locality claim
by shipping a distinguishing pair. Both are published for challenge.

**Relation to limitation 6 (the shared-prior confound).** If inter-rater
agreement tracked a shared training prior rather than a semantic joint,
there would be no reason for the agreement boundary to coincide with an
independently checkable property of the sentences. A measured
correspondence is therefore evidence on the confound from a different
direction than the human pass H1 (registered, awaiting its recruit): it
cannot rule out a shared
prior *about the property itself*, but it converts "the raters agree" into
"the raters agree exactly where a formal criterion says the sentence has
one defensible formalization." A failed correspondence would leave the
prior explanation standing.

## Definitions (fixed before construction)

**Datum granularities.** Two are defined, matching the census's own two
reporting levels:

- **msg** — the abstract value of ONE handshake message: its fields as
  §4's presentation language defines them, plus two pieces of framing
  metadata the record layer provides (message type; sender role
  client/server). Nothing else.
- **transcript** — the ordered sequence of plaintext handshake-message
  values of ONE connection, both directions, start to current point
  (including, for response-duty readings, the terminating alert if any).
  Encryption is abstracted away: the transcript is the post-decryption
  message sequence.

**Context** is everything outside the chosen datum: other connections,
negotiated or derived secrets (PSKs, private keys, traffic keys), clocks,
either party's configuration or capability sets, either party's internal
computation and intent, deployment policy, generation processes. Contexts
are tagged with a fixed **channel vocabulary**: `other-messages`,
`secret-material`, `clock`, `party-conduct`, `counterparty-config`,
`deployment-policy`, `private-intent`, `generation-process`,
`prior-connection`.

**Reading.** A one-sentence statement of the compliance criterion an item
is being formalized as. One normative sentence may admit several readings
(that possibility is what the study measures). Every witness names its
reading.

**Local predicate at granularity g.** A total computable predicate on one
g-datum, defined using only the datum's content and constants fixed by the
spec text.

**Locality of a reading at g.** There exists a local predicate φ at g such
that in every spec-admissible context, the obliged party complies with the
reading iff φ holds of the designated datum.

**YES-witness (validator).** Shipped executable φ taking exactly one
parameter (the g-datum), plus at least one accepting and at least one
rejecting vector, plus quoted spec text supporting the tracking claim. The
arity, the vectors, and the vector counts are checked mechanically; the
tracking claim is judgment, published for challenge.

**NO-witness (distinguishing pair).** One fixed g-datum, two
spec-admissible contexts with channel tags, opposite compliance verdicts,
each verdict supported by quoted spec text. **Lemma (the study's one
theorem, trivial but load-bearing):** a valid distinguishing pair at g
entails that NO local predicate at g decides the reading — φ(d) is
constant across the pair while compliance differs. A pair is therefore a
constructive proof of non-locality, not an opinion. The judgment residue
is whether the two verdicts are correct readings of the spec.

**Rung of a reading** = the finest granularity at which it is local:
`msg`, `transcript` (local at transcript, with a distinguishing pair at
msg against the best-candidate single-message designation — the
single-message designation a DOMAIN-voting rater would most plausibly
choose, stated in the witness; this best-candidate scoping is a disclosed
heuristic, since exhaustive per-designation pairs are not feasible), or
`nonlocal` (distinguishing pair at transcript).

**Item outcome** = the set of rungs of its successfully witnessed
*eligible* readings (eligibility defined below). A construction FAILURE is
recorded with the blocking information channel. **Asymmetry, disclosed:**
a failure to construct a validator is not a proof of non-locality (only a
shipped pair is), and a failure to construct a pair is not a proof of
locality (only a shipped validator is). Failures are honest outcomes, not
evidence of impossibility.

## Item set (mechanical; derivation tool ships with this registration)

`profile_tls.py` parses all fourteen archived full label maps for the
TLS-204 corpus — A (from the census class table), C, D, Av4, Xv4, Av6,
Xv6, Av7, Xv7, G, X, M, K, Z (from the reports' verbatim raw-label
blocks) — normalizes label spellings, strips torn flags, and verifies the
parse against nineteen pairwise agreement numbers as known-answer tests
(eighteen published counts; the Av6–Xv6 count 190 is uniquely implied by
the v6 report's published 93.1% of 204), with a perturbation self-test.
`--stable` prints the md5-ranked stable sample; `--eligibility` prints
the contested items' eligible rungs. Rater B is excluded:
its full map was never archived (provenance note in the census file).
Result: 114/204 items unanimous across all fourteen raters.

- **Contested set (27):** items where ≥4 of 14 raters depart from the
  modal label (more than one full rater-pair's worth of dissent):
  22, 30, 31, 32, 52, 55, 56, 57, 65, 66, 67, 75, 79, 80, 89, 111, 122,
  123, 124, 147, 157, 164, 184, 187, 188, 189, 197.
- **Stable sample (18):** for each class with unanimous items, the first 3
  (or all, if fewer) ranked by md5 of sentence text (the census
  self-audit's own deterministic ordering): DOMAIN {69, 110, 72},
  TYPESTATE {175, 137, 138}, CV {178, 126, 180}, PROCESS {59, 53, 60},
  NEG {3, 6}, REVOCABLE {133}, U {91, 23}, META {117}.
- **Exclusion:** item 117 (META) is excluded from the witness set: it
  obliges future specification authors, no runtime party, so neither
  witness form applies. **Witness set: 44 items.**

**Instrument-era disclosure.** The fourteen raters worked under six
instrument generations: v1 (A, the original census); v2 (C — whose pass
the pass-3 report itself declares INVALID as a codebook-v2 test due to a
paraphrased-definition transcription defect, diagnostic only as an
instrument test; C's archived labels are used here as rater data, with
that provenance noted); the frozen v3 pass-4
pack, blob `a08febba…` (D, G, X, M, K, Z — one blob, six raters); and the
v4, v6, and v7 pairs. Part of the contested mass is era-correlated —
item 188's DOMAIN votes are exactly the six v4-and-later raters applying
rule 16 *by rule*. The selection rule does not condition on the cause of
dissent; the report will include a per-era breakdown for contested
items.

**Eligibility.** For each item, a witness is *eligible* for the rungs
implied by the classes holding ≥2 of its 14 votes, under the registered
vote→rung map: DOMAIN→msg; TYPESTATE→transcript; NEG, PROCESS, CV,
REVOCABLE, POLICY, U→nonlocal; THRESHOLD→per-item, by rule 16's own two
branches: item 188's bounded quantity (ticket_lifetime value) is carried
in the datum→msg; item 189's bounded quantity (elapsed ticket age) is
clock-valued→nonlocal. The ≥2 threshold keeps single stray votes from
spawning readings. Extra-eligible witnesses (constructed beyond this
table) are permitted, marked `eligible: false`, and excluded from item
outcomes and from T7's L; exactly one is planned (T4's item-178
consequentialist validator). NEG maps to nonlocal because its class
definition requires the receiver's supported set — configuration, not
wire data. The eligibility table is embedded in `check_witnesses.py` and
re-derivable from `profile_tls.py --eligibility`.

## Non-circularity and elasticity discipline

The author constructs the witnesses and is not blind to the archived
labels. What is mechanical: signature arity, vector execution, pair
structure (one datum, two tagged contexts, opposite verdicts, quotes
present), outcome derivation, and the grading of T1–T3 and T5–T7 plus
T4's artifact-presence checks — all in the shipped `check_witnesses.py`,
fixed **before** construction. T4's correctness half (do the four
artifacts track the spec's meaning) is reader-graded, like every
tracking claim. What is judgment:
whether a validator tracks the spec's meaning and whether a pair's
verdicts are correct — every such judgment ships with quoted spec text
and is graded by readers, not by the author.

The elasticity risk — "defensible reading" stretching until every
contested item comes out multi-rung — is only partially controlled by
T6: for 18 of the 27 contested items the registration commits, in
advance and by name, that only ONE rung will survive construction, so
*uniform* elasticity would fail T6. Selective elasticity — stretching on
T5's items while declining to construct on T6's — is NOT caught by any
floor, because a recorded construction failure is unfalsifiable effort
(per the asymmetry disclosure above). The control for that residue is
publication-for-challenge: every FAILS record names the rung and reading
it failed on, and a reader who ships the validator or pair the author
"could not construct" refutes that record directly. T6 disciplines the
uniform failure mode; readers discipline the selective one.

One-shot: predictions are frozen at push; construction begins only after.
A prediction that fails, fails — it grades the author's semantic model
and licenses no revision, no re-selection, and no relabeling of any
archived pass. Witness artifacts stand or fall individually on their own
quotes regardless of prediction outcomes. No number produced here joins
any census series.

## Predictions (append-only after push)

- **T1 — stable DOMAIN {69, 110, 72}: outcome {msg}, 3/3 strict.** The
  named risk: item 110's guard ("if the client opts to do so") is intent;
  the registered msg reading is extension co-presence (early_data ⇒
  pre_shared_key, in one ClientHello). If no defensible datum-decidable
  criterion exists for it, T1 fails.
- **T2 — stable TYPESTATE {175, 137, 138}: outcome {transcript}, 3/3
  strict** — transcript validator plus msg-pair against the
  best-candidate designation for each.
- **T3 — stable non-local {53, 59, 60, 3, 6, 133, 91, 23, 126, 180}:
  outcome {nonlocal}, 10/10 strict** — a transcript-level distinguishing
  pair for each. Expected channels (reported, not graded): PROCESS →
  party-conduct; NEG → counterparty-config; REVOCABLE → clock; U →
  generation-process; CV → secret-material.
- **T4 — the CV split (the sharpest risk): four required artifacts on
  three items, presence and structure checked mechanically; their
  correctness is reader-graded from the quotes.** Every "MUST
  verify" duty admits a literal-conduct reading (verification performed),
  which is nonlocal for all of {178, 126, 180}: a valid signature never
  verified leaves the transcript identical, so a party-conduct pair
  exists. But under the consequentialist reading ("MUST NOT proceed as if
  valid when invalid"), the three split on exactly the census's own
  phrase "the secret is the discriminator" (decision rule 2): item 178's
  signature validity is computable from the transcript alone (public key
  in the Certificate message + transcript hash) — a transcript validator
  is constructible (extra-eligible, disclosed, excluded from T7's L) —
  while items 126 (PSK binder) and 180 (Finished MAC) need key material
  outside the transcript, witnessed by secret-material pairs against
  their consequentialist readings. Claim: CV's unanimity rides on the
  literal reading; the consequentialist reading exposes a finer locality
  split the class scheme cannot see.
- **T5 — contested multi-rung {22, 65, 66, 75, 79, 80, 147, 164, 184}:
  ≥2 rungs witnessed, floor ≥7/9.** Per-item predicted sets (reported
  by the grader, not graded — only the ≥2-rungs floor is graded): 22 {msg,
  nonlocal} (two duties in one sentence: sentinel structure; randomness);
  65 {msg, transcript} (intra-chain key/alg fit; CertificateVerify
  compatibility); 66 {msg, nonlocal} (located presence predicate;
  private-intent guard); 75 {msg, nonlocal} (offered-cert SHA-1
  predicate; certificate-inventory guard); 79 {transcript, nonlocal}
  (acceptance against own advertisement; preparedness conduct); 80 same
  as 79; 147 {msg, transcript} (sender-role zero-length reading;
  CertificateRequest-absence reading); 164 {msg, nonlocal} (alert-code
  vocabulary; private abort decision); 184 {msg, transcript}
  (sender-prohibition by role; client termination duty).
- **T6 — contested single-rung, exact match, floor ≥15/18:**
  {30, 31, 32, 56, 57, 188} → {msg}; {52, 67, 124} → {transcript};
  {55, 89, 111, 122, 123, 157, 187, 189, 197} → {nonlocal}.
  The registration's reasoning, disclosed (the channel names in this
  paragraph are prose glosses, not the registered channel vocabulary —
  the witness records carry the vocabulary tags): for 30/31/32/56/57 the guard
  "negotiating version X" is *encoded in the ServerHello itself* (items
  56/57 state the encoding), so the TYPESTATE reading's target is itself
  msg-local — these are vocabulary fights on one rung, and the eligible
  transcript reading is predicted to FAIL to find a target that is
  transcript-local but not msg-local. 188 is a provenance fight over a
  msg-local check. For the nine nonlocal-predicted items the eligible
  local readings are predicted to fail on a named channel (55/157
  capability-conduct; 89 internal use; 111 which-PSK-encrypted needs
  keys; 122 ignore-conduct; 123 out-of-band provisioning; 187
  API conduct; 189 clock; 197 liveness/tolerance conduct).
- **T7 — headline correspondence.** Over the 44 items, let L(i) = "some
  local rung (msg or transcript) is witnessed among eligible readings"
  and E(i) = "DOMAIN+TYPESTATE hold a strict majority of the 14 votes".
  Prediction: L = E on every item EXCEPT a named exception list where
  L ≠ E is predicted: **{75, 111, 164, 188}** (75 and 164: local
  component real, eliminable votes a minority; 111: eliminable majority,
  but the binding constraint needs secrets; 188: msg-local check, class
  majority THRESHOLD by provenance). Grading: zero unnamed mismatches
  AND ≥3/4 named mismatches realized. Both failure directions are live:
  an unnamed mismatch fails T7's universal half; named exceptions
  failing to materialize fail its existential half. Scope disclosure:
  for the 13 items whose eligibility is {nonlocal} only, L is false by
  construction and E is false in the archive, so no mismatch is
  possible there — the universal half is live on the other 31 items.

**Interpretation, pre-committed.** T1–T3 grade whether the criterion
reproduces the stable archive (comprehension floor for the formalism).
T4 grades a novel structural claim invisible to the class scheme. T5/T6
grade the central thesis: contested items are contested *because* the
sentence supports readings on different rungs (T5), and stay one-rung
where the fight is vocabulary, not information (T6). T7 grades the
correspondence between the formal property and the archive's headline
eliminable-vs-not boundary. Failures grade the author's semantic model
and the thesis — not the raters, not the codebook, not any archived
number.

## Grading

`check_witnesses.py` (shipped with this registration, before any witness
exists) validates witness structure mechanically, derives item outcomes,
grades T1–T3 and T5–T7 against the tables above plus T4's mechanical
presence half (T4's correctness is reader-graded), and self-tests its
own rejection paths (wrong arity, missing reject vectors, same-verdict pairs, unknown
channels) plus a grading mutant on every run. The witness pass produces
`witnesses.py` (the artifact under test) and a report
`rfc8446-s4-locality.md`. Run:
`python3 census/locality/check_witnesses.py`.
