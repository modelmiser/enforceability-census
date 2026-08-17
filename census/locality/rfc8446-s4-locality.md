# Locality study, first pass: two honest misses of one shape, four named exceptions realized exactly

2026-08-16 · Registration: `census/locality/README.md`, pushed at main
`20b62e9` BEFORE any witness was constructed. Witnesses:
`witnesses.py` (56 artifacts + 17 recorded construction failures — one
original FAILS record was refuted at the gate and replaced by the pair
it denied; see finding 2). Graded by the pre-shipped
`check_witnesses.py`. Reproduce:
`python3 census/locality/check_witnesses.py`.

**What this pass is and is not.** The witnesses were constructed by the
registration's author, who knows the archived labels — this is disclosed
in the registration and shapes what the sheet can claim. A near-perfect
graded sheet here measures the internal consistency of one semantic
model against pre-frozen predictions, not an independent replication.
The substance a reader can grade is the artifacts themselves: every
validator ships with vectors and every distinguishing pair ships with
quoted spec text, and any reader who ships a validator the FAILS list
says could not be built refutes that record directly. No number from
this study joins any census series.

## Grades

| clause | registered | result |
|---|---|---|
| T1 stable DOMAIN {69,110,72} → {msg} | 3/3 strict | **PASS** 3/3 |
| T2 stable TYPESTATE {175,137,138} → {transcript} | 3/3 strict | **PASS** 3/3 |
| T3 stable non-local (10 items) → {nonlocal} | 10/10 strict | **PASS** 10/10 |
| T4 CV split (4 artifacts on 178/126/180) | presence mechanical | **PASS** (correctness reader-graded) |
| T5 contested multi-rung (9 items) | ≥7/9 | **PASS** 9/9 (exact sets 9/9) |
| T6 contested single-rung (18 items) | ≥15/18 exact | **PASS** 16/18 — **items 124 and 52 missed** |
| T7 headline L=E, exceptions {75,111,164,188} | 0 unnamed AND ≥3/4 named | **PASS** — unnamed ∅, named 4/4 |

Two deviations, one shape: items 124 and 52 were each registered
{transcript} and measured {transcript, nonlocal}, because in each case
the sentence hides a context dependency the author's model missed.
Both predictions fail and stand as graded — see finding 2.

## Findings

**1. The headline correspondence holds, and its failures are exactly
the four the registration named.** Over all 44 items, "some local rung
witnessed" coincides with "DOMAIN+TYPESTATE hold a vote majority"
except at {75, 111, 164, 188} — the named-exception list, realized 4/4
with zero unnamed mismatches. Each exception is itself legible: 75 and
164 carry a real msg-local component (the offered-chain predicate; the
alert vocabulary) under a non-eliminable-majority label; 111's
eliminable majority binds to a constraint only secrets can decide; 188
is a msg-local check whose vote majority is THRESHOLD on the
constant's provenance. The author's formalization tracks the archive's
eliminable-vs-not boundary exactly where information sits, and
diverges exactly where the class vocabulary encodes something other
than information (provenance, conduct wrapping a local predicate).

**2. Both misses are the same fault line — the sentence hides a
context guard — and they were found by the study's two different
control mechanisms.** Item 124 ("the server MUST ensure that it
selects a compatible PSK (if any) and cipher suite") was registered
{transcript} on the offer-consistency reading; at construction, the
RFC's own compatibility relation — the selected PSK's hash must match
the selected suite's, the relation in-corpus item 185 states for
resumption — turned out decidable only against the ticket's ISSUING
connection: a prior-connection channel. The author caught that one
while writing the witness. Item 52 was also registered {transcript},
and here the author's model FAILED twice: the original FAILS record
claimed no non-local reading existed, scoping its attempt to the
PROCESS votes' conduct angle — and never engaged the sentence's own
configuration guard, "servers ... **which also support TLS 1.2**". The
gate's cold reviewer refuted the record by constructing the
deployment-policy pair (a TLS 1.3-only server owes nothing; a
1.2-supporting server violates on the identical transcript — the same
shape as the shipped pairs for items 3 and 6). That is the
registration's selective-elasticity failure mode occurring ONCE, on
the registered prediction, and being caught by the challenge mechanism
the registration names: a shipped counter-witness falsifies a FAILS
record. The record is withdrawn in place (preserved as a comment), the
pair is adopted with reviewer provenance, T6 drops to 16/18, and both
deviations stand as graded. What the pair of misses teaches: context
dependencies buried mid-sentence ("compatible", decidable only against
the ticket's issuing connection; "which also support TLS 1.2") are
where this author's semantic model — and plausibly rater models — lose
information.

**3. The CV split has three levels, not two — "the secret is the
discriminator," now with witnesses.** Under the literal-conduct
reading ("MUST verify" = perform verification), all of {178, 126, 180}
are non-local: a valid signature never verified leaves every message
unchanged (the party-conduct pair on 178). Under the consequentialist
reading ("do not proceed when invalid"), they split: item 178's
signature validity is computable from the transcript alone — the
verification key is IN the Certificate message, the covered content is
the transcript hash — witnessed by an executable transcript validator;
items 126 and 180 need key material no message carries, witnessed by
secret-material pairs. And beneath that sits a third level the
construction surfaced (header convention 4 of `witnesses.py`): with
(EC)DHE, the Finished MAC is mathematically DETERMINED by the
transcript (the shared secret is a function of the public shares) but
not efficiently computable from it. The registered criterion says
"computable," so 180's pair honestly uses a psk_ke handshake, where
the key schedule depends on an external PSK and even
information-locality fails. The census's class scheme sees one CV
class; the locality lens sees public-key-verifiable /
efficiently-blocked / information-blocked — a distinction invisible to
all seventeen raters because the codebook never asks the question.

**4. The "guard cluster" was two different fights wearing one label.**
The DOMAIN-vs-TYPESTATE mass at {30, 31, 32, 56, 57} dissolved at
formalization: the guard "negotiating version X" is encoded in the
ServerHello itself (items 56/57 fix the encoding — pre-1.3 selection =
supported_versions absent), so every candidate transcript reading
collapses to the msg reading, and the recorded FAILS say so. Those
five items are one-rung: the archived contest is vocabulary ("does a
self-referential guard 'vary with state'?"), not information. The
genuinely two-rung guard items are {65, 67, 147, 184}, where the guard
lives in ANOTHER message — and 67 came out single-rung {transcript}
(its DOMAIN votes have no constructible single-message reading; the
FAILS record names the missing message). The archive recorded all of
this as one undifferentiated boundary; the witness forms separate it.

**5. Preparedness duties are the cleanest non-local family.** Items
{55, 79, 80, 157, 197} share a shape the construction kept
reproducing: "MUST be prepared/able to X" is a counterfactual over
cases the transcript need not exercise, so the distinguishing pair is
always available (same transcript, implementation capable vs not). A
capability duty can never be datum-local at any granularity — which is
a formal account of why the census's U-boundary and PROCESS churn
concentrate there.

**6. Two transcript witnesses lean on a disclosed convention; the
report flags them rather than buries them.** The validators for 79 and
80 rely on the attributed-abort convention (an alert names what it
responds to — `witnesses.py` header note 2). Real TLS alerts carry no
attribution, so those two locality claims are claims about the
modeled transcript, defensible exactly insofar as the convention
mirrors how the census's raters read response duties. The other
transcript validators (52, 65, 67, 124, 137, 138, 147, 175, 184) check
message sequences only and do not use attribution.

**7. The era breakdown the registration owed: part of the contested
mass is instrument evolution, cleanly visible.** Votes per era
(v1: A; v2: C; v3p4: D,G,X,M,K,Z; v4/v6/v7 pairs; labels abbreviated):

| item | v1 | v2 | v3p4 | v4 | v6 | v7 |
|---|---|---|---|---|---|---|
| 22 | U | DOM | DOMx4+TYP+U | TYPx2 | DOM+TYP | DOM+TYP |
| 30 | DOM | DOM | DOMx4+PRO+TYP | TYPx2 | DOM+TYP | DOM+TYP |
| 31 | DOM | DOM | DOMx5+TYP | TYPx2 | DOM+TYP | DOM+TYP |
| 32 | DOM | DOM | DOMx5+TYP | TYPx2 | DOM+TYP | DOM+TYP |
| 52 | PRO | NEG | DOMx2+TYPx4 | TYPx2 | PRO+TYP | TYPx2 |
| 55 | DOM | PRO | DOMx3+PROx2+U | DOM+PRO | PROx2 | PROx2 |
| 56 | DOM | DOM | DOMx4+TYPx2 | TYPx2 | TYPx2 | DOM+TYP |
| 57 | DOM | DOM | DOMx5+TYP | TYPx2 | TYPx2 | DOM+TYP |
| 65 | DOM | DOM | DOMx5+TYP | DOM+TYP | TYPx2 | TYPx2 |
| 66 | DOM | U | DOMx4+Ux2 | DOMx2 | DOM+TYP | TYPx2 |
| 67 | TYP | DOM | DOMx2+TYPx4 | DOM+TYP | TYPx2 | TYPx2 |
| 75 | POL | U | DOMx2+POLx2+Ux2 | DOM+POL | DOM+U | DOM+U |
| 79 | U | NEG | PRO+TYPx4+U | TYPx2 | TYPx2 | PRO+TYP |
| 80 | U | NEG | DOM+PRO+TYPx3+U | TYPx2 | TYPx2 | PRO+TYP |
| 89 | TYP | U | PROx4+TYP+U | PROx2 | PROx2 | PROx2 |
| 111 | TYP | DOM | CVx2+DOM+TYPx2+U | TYPx2 | TYPx2 | TYPx2 |
| 122 | DOM | PRO | DOMx2+PROx3+U | DOM+PRO | DOM+PRO | PRO+TYP |
| 123 | DOM | POL | DOM+POLx2+PRO+Ux2 | POL+PRO | PROx2 | PROx2 |
| 124 | NEG | NEG | NEGx2+TYPx4 | TYPx2 | TYPx2 | TYPx2 |
| 147 | TYP | DOM | DOMx5+TYP | TYPx2 | DOMx2 | TYPx2 |
| 157 | DOM | PRO | DOMx2+PROx3+U | DOM+PRO | DOM+PRO | DOM+PRO |
| 164 | PRO | PRO | DOMx4+PRO+U | DOM+PRO | PRO+TYP | POL+U |
| 184 | TYP | DOM | DOMx3+TYPx3 | DOM+TYP | DOM+TYP | DOM+TYP |
| 187 | PRO | PRO | PROx3+Ux3 | PROx2 | PRO+U | PROx2 |
| 188 | THR | THR | THRx6 | DOMx2 | DOMx2 | DOMx2 |
| 189 | THR | THR | REVx2+THRx4 | REVx2 | REVx2 | REVx2 |
| 197 | PRO | PRO | POL+PRO+TYP+Ux3 | PRO+TYP | PRO+TYP | PROx2 |

Read against the witness outcomes: 188 and 189 are pure instrument
evolution (THRESHOLD unanimously through v3p4, then rule 16/rule 19 by
rule — both items are one-rung here, so the era shift moved vocabulary,
not information). 124's NEG votes are all pre-v4. And the one-rung
sentinel family (30–32, 56–57) shows votes shifting TYPESTATE-ward
from v4 onward relative to the v1–v3p4 mass, with a partial v7
pullback (DOM+TYP on all five where v4 read TYPx2) — a guard-reading
fight that moved with the codebook's guard rules, on items where the
witness sheet says the guard was in-datum all along.

## What a skeptical reader should attack first

The claims most worth challenging, in order: (a) the two
attribution-dependent validators (finding 6); (b) any FAILS record —
each names the reading and blocking channel, and one shipped
counterexample refutes it, WHICH HAS ALREADY HAPPENED ONCE (finding 2:
the gate's reviewer felled the original 52 record — the mechanism is
live, not theoretical); (c) the guard-scoping convention
on items 66 and 75 (the msg validators formalize rule 17's located
predicate, with the guard disclosed as out-of-scope); (d) the
correctness of the two verdicts in any pair (each carries its quotes).

## Limitations

1. Author-constructed, archive-aware (stated at top; the registration's
   elasticity discussion applies — T6's 16/18 shows the single-rung
   commitments mostly bound, but reader challenge is the real control).
2. The abstract message model: locality claims are information-flow
   claims over modeled values, not over TLS bit-level parsers.
3. The attributed-abort convention (finding 6).
4. FAILS asymmetry: a recorded failure is not an impossibility proof
   except where a pair is also shipped — measured, not hypothetical:
   one of the original eighteen records was refuted at the gate.
5. "Spec-admissible context" is used with an implicit admissibility
   notion the frozen registration never defines: a context is
   admissible when it is consistent with every duty EXCEPT the one
   under test. The sentinel-family transcript FAILS (22, 30–32, 56,
   57) depend on it — a divergent-continuation pair there would
   require the compliant arm to violate items 56/57. The 52 pair
   needs no such lenience.
6. Two corpus sentences in the witness set (59 and 123) are truncated
   mid-clause in the frozen corpus file itself — an extraction
   artifact, disclosed in their quotes with the RFC completions in
   marked brackets. The fourteen raters rated the truncated forms;
   item 123's witnesses rest only on the clause the corpus carries
   ("MUST be set").
7. One corpus, one spec genre. Whether the correspondence holds for
   iCalendar's validity/precision boundary or QUIC's lifecycle mass is
   the natural next pass; nothing here licenses assuming it.
