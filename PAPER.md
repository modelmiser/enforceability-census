# A Census of Enforceability: Measuring What Fraction of Stated Runtime Obligations a Type System Could Discharge

**Repo-native paper · 2026-08-13, extended 2026-08-14 (v4 series, §6.1), 2026-08-15 (the
non-protocol corpus, §4.8), 2026-08-16 (v5 series, §6.2; v6 series, §6.3; obfuscation probe, limitation 6; second cross-family replication, §6.4; v7 series, §6.5; locality study, §6.6), and 2026-08-17 (second locality passes, §6.7) · artifact of record: this repository.**
No venue submission is planned; the repository, its commit history, and the
census artifacts it cites are the citable object.

> **⚠️ CURRENCY NOTE (added 2026-08-20).** This paper does **not** cover four
> artifacts that exist in the repository as of this date, and a reader treating it as
> the complete artifact of record will get a stale picture of them:
>
> - `census/human/` — the human-rater pass **H1 was superseded by H1-R2 on 2026-08-20**
>   after a disclosed defect in its packet (format examples leaked real archive labels
>   on graded items; one leak lifts the largest measured failing branch to a PASS at
>   the H2 floor). **Limitation 6's description of "the parked human replication" does
>   not reflect this.** Neither pass has been run.
> - `census/human-locality/` — the binary human pass **HL1**, registered 2026-08-17,
>   also unrun.
> - `census/mech-probe/` — **MECH-PROBE-1**, a non-LLM rule-based classifier probe
>   whose pre-registration turned out unable to adjudicate the result. It carries
>   three rounds of corrections, including withdrawal of its original causal claim and
>   of its original verdict.
> - `census/mls/SPENT.md` — **MLS is spent as a probe corpus.** The MLS *census* and
>   every figure quoted from it are unaffected; future instrument probes against MLS
>   are foreclosed.
>
> No number in this paper changes as a result. Limitation 6 stands as written — the
> shared-prior confound remains unaddressed, and both instruments built to address it
> are unrun.

## Abstract

Debates about how much verification "could catch" are usually conducted by
example. We measure instead: classify every stated runtime obligation in a
corpus by the **shape of its predicate** into a small set of enforceability
classes — those a type system could discharge (DOMAIN, TYPESTATE) and those
it cannot (THRESHOLD, whose constant is a policy choice with no fact of the
matter for a type to certify, and REVOCABLE, whose truth needs a clock),
plus classes forced by cryptographic protocols (CRYPTO-VERIFY,
NEGOTIATION) — and report the mix. Across eight corpora from four
different settings — an operations-monitoring rule base, a windowing
protocol, the specifications of three cryptographic/transport
protocols including QUIC's complete three-document family, and a
calendar data format — we find: a monitoring-layer
corpus (1,155 Prometheus alert rules) is 78% threshold, in a query
language whose grammar cannot express typestate — its TYPESTATE count of 0
is a design invariant of PromQL, not a census measurement (§4.1); Wayland's declared protocol errors are
87.6% type-eliminable in shape (149 of the 170 client-facing errors among
172 declared; classifier vocabulary fitted to that corpus, **and — uniquely
among these corpora — the census-era checkout was never pinned, so this figure is
preserved as reported numbers rather than as a regenerable artifact** — §4.2); and the
normative surface of RFC 8446 §4 (TLS 1.3 handshake,
204 MUST/SHALL sentences) is **80–83% type-eliminable in shape** (three-rater range),
with a secret-dependent cryptographic core of **exactly 6/204 (2.9%) — the
same six sentences in every TLS-study rater's recorded labels** (one
rater's four unarchived labels are inferred non-CV; limitation 7). A fourth census, run
after this paper's first publish gate under the TLS study's frozen
instrument, shows the share is **not a security-protocol constant**: the
core normative surface of RFC 9420 (MLS, §5–§15, 127 MUST/SHALL sentences)
is **≈57% type-eliminable in shape** (two raters, 56.7%/57.5%) — ~25
points below TLS under matched method, because the MLS span states as
MUSTs the procedure and hygiene TLS §4 leaves tacit (~18–19% PROCESS;
§4.5). A fifth census under the same frozen instrument places QUIC's
transport machinery (RFC 9000 §2–§19, 281 MUST/SHALL sentences) between
them at **≈67–69%** (66.9%/69.0%), TYPESTATE its largest class — three
censused spans, one instrument, results **consistent with a spectrum**
(≈57% → ≈67–69% → 80–83%) whose positions are explainable, post hoc, by
what each span states as obligations — not an established mechanism; the
author's pre-registered directional model of it partly failed (§4.6).
Completing QUIC's document family (§4.7) put that reading through its
sharpest available control — one protocol, one working group, the
document's role varying (rater pairs, spans, and n vary too; §4.7) — and
the share ranged from **23.3%** (RFC 9002's
loss-recovery shell, identical in two blind same-family raters — the
shared-prior caveat of §6 applies) through 54–67% (RFC 9001)
to ≈67–69% (transport): within one protocol, document role tracks the
mix. The same completion qualified two things this abstract would
otherwise overclaim: the "crypto document" is NOT crypto-dense (CV
1.4%/2.9% — its verification lives in non-normative prose the census
cannot see, censoring INSIDE a document), and RFC 9001 produced the
series' first below-band inter-rater agreement (76.8%), concentrated on
the PROCESS/TYPESTATE key-lifecycle boundary. An eighth census (§4.8,
run last, under the same frozen instrument — the first census to
pre-register its full rater roster, same-family model name included)
took the frozen-instrument series outside the protocol
genre: the core object specification of RFC 5545 (iCalendar, 225
MUST/SHALL sentences) is **88.0%/88.4% type-eliminable in shape** —
above every frozen-instrument protocol span — with DOMAIN alone ~87%
of the corpus,
TYPESTATE (the largest class of the TLS, QUIC, and RFC 9001 spans)
collapsed to 1
and 4 items, and cross-family raw agreement of 97.3%, then the repository's
highest (its own v6 pair later reached 98.7%, §6.3); the author's pre-registered band missed the foreign rater by
exactly one item, and the genre's censoring (a sibling scheduling
protocol; obligations stated as grammar rather than MUSTs) is
pre-registered in the census. A cross-family
replication (§6) re-rated the TLS corpus blind under the same frozen
instrument with two foreign frontier model families: the author's
pre-registered degradation model failed — one foreign rater agreed with a
Claude rater *above* the intra-family agreement ranges, and all six
core-CV sentences kept their CV label under every rater ever recorded —
weakening the family-bias half of the rater-monoculture caveat while
leaving its corpus-shared-prior half untouched (limitation 6). A
second replication (§6.4) later widened the panel to five foreign
families — three more lineages landing inside the pre-registered
band, the CV core fifteen-for-fifteen across six families — while
finding the first replication's nine-item foreign consensus is not
seat-general: one new family sides with the Claude anchor's archived
reading, which is itself its own family's outlier on those items. A
v7 amendment then settled the v6 pass's two docket edges (§6.5) —
both adjudications transmitted in both families, TLS posted the
series' first fully clean no-regression sheet — while the leakage
and churn tripwires convicted the author's calibration for a second
consecutive release, on items no rule version has claimed. A
locality study (§6.6) then formalized the boundary the raters keep
agreeing on: over a registered 44-item set drawn from all fourteen
archived TLS label maps, the agreement boundary coincided with a
constructively witnessed semantic property — datum-locality at two
granularities — everywhere except four pre-named exceptions; the
contested mass split into vocabulary fights and genuine ambiguities;
and the study's reader-challenge mechanism fired on its first
outing, the gate's reviewer refuting a recorded impossibility
claim by constructing the pair it denied. Second locality passes
(§6.7) then generalized the criterion to the iCalendar and QUIC
archives: the correspondence held with class-shaped, pre-named
divergence — QUIC's conn-carried THRESHOLD family is
connection-local yet sits off the headline's eliminable side, its
cross-connection 0-RTT state is eliminable-voted yet no
within-connection witness stands, and a second recorded
impossibility claim fell at the gate to a reviewer-constructed
witness. The
instrument itself was then repaired under pre-registration and the
repair graded (§6.1): a v4 amendment wrote five rules at the series'
measured edges, with itemized predictions V1–V8 committed before any v4
rater existed and every v3 number ring-fenced. Eight blind rating
passes — a same-family and a foreign rater per corpus — graded them
all: the key-lifecycle repair took RFC 9001, the band-breaking corpus,
to what was then the series' best cross-family agreement (94.2%, from
76.8%; the same corpus's v5 pair later reached 95.7%, §6.2); TLS's
two v4 raters agreed at 92.2% raw, above every prior pair on that
corpus; and the amendment's disclosed most counterintuitive prediction
— flipping decision rule 3's own worked example and emptying TLS's v3
THRESHOLD class — held in both raters, though a seam example retained
in the pack names both items' content, so that flip is a comprehension
result more than a discrimination one (a disclosure gap found at this
integration's own gate and corrected in the protocol). The author's
model of the repair's *reach* failed too: the no-regression
prediction's count-bound half failed in all eight rater-corpus grades
— partly zero-tolerance arithmetic on zero-spread classes, partly two
rules moving items beyond their named sets (a repair rule acts on a
boundary, not an item list) — while its match-rate half passed in all
eight; two predictions failed on precisely their hardest items; and
QUIC's agreement declined (84.0% vs 85.1%) — recorded as v4's
measured cost, and since decomposed by a registered cross-roster
replication into a −3.2-point roster effect and a +2.1-point
instrument recovery on that roster-shape (§6.1). All v4 shares are a new, version-labeled series
(TLS lands at 81.9%/82.8%, inside the closed v3 band); the v3
headlines stand unchanged. A v5 amendment cut from that grading
record then closed the loop (§6.2): declaring its own named-item
predictions comprehension checks by construction, it moved the
discriminating load to stability sets and registered
floors-with-measured-failability — and its eight blind passes graded
every pre-registered clause PASS on the predictions while the
redesigned no-regression machinery caught the amendment's *own*
undisclosed reach on the format corpus (both raters, both clauses —
the pre-committed instrument-mis-design verdict, with the v5
iCalendar shares quoted only as that defect's size), reversed the v4
churn it had named undecided, and set three of four corpus
pair-agreement records; v5 shares are a third separate series. The
verdict was then answered (§6.3): a v6 amendment cut from the
conviction wrote one rule at the convicted boundary — recognition
predicates are receiver-relative; a suppression trigger must be a
pure function of the serialization unit — declined every
mixed-evidence sibling shape, and registered its first pass with the
series' harshest tolerance: on the convicted corpus, a no-regression
budget of ZERO departures. The corpus passed every clause in both
raters at exactly that bound, its shares reverted to the
pre-conviction band, and its rater pair set the repository's
raw-agreement record (98.7%) — while one pre-downgraded adjudication
half failed to transmit in both raters and the TLS cell failed its
no-regression clauses in the foreign seat, both standing as graded;
v6 shares are a fourth separate series. The numbers are the smaller half of the
contribution. The larger half is the method that survived its own failures:
classify on the predicate and never the name (a name-based pass produced a
publishable-looking headline that was retracted the day it was written);
make the classifier report a DISAGREE bucket so it can catch its own
violations; pre-register codebook amendments and their predictions before
each re-rating pass; and where the outcome outran what was pre-registered —
a failure mode the committed dichotomy had not anticipated (pass 3), a
quoted range the failure clause said would not change (pass 4) — record a
deviation with its reason rather than argue compliance (§6).
A four-pass inter-rater study conducted this way — all raters LLM agents,
the three non-author raters blind to each other, to the tallies, and to the
authors' expectations — yields a finding we did not plan:
**classes transmit between raters only as well as their discriminators are
crisp.** The classes with mechanical discriminators showed zero or
near-zero rater variance across four passes (CRYPTO-VERIFY and META:
identical in every rater's recorded labels; THRESHOLD/REVOCABLE: one recorded flip on one
item by one rater), while every residual disagreement sits on boundaries
whose rules require judgment. (Directional, not a quantitative law: the
zero-or-near-zero-variance classes total 11 of 204 items, and perfect
agreement on rare, distinctive items is weaker evidence than the same rate
on a large class — the confound is stated in §6 and in the codebook's
graduation record.)

## 1. The question, and why counting beats arguing

"What fraction of bugs can types catch?" invites survivorship-biased answers
(Gao, Bird & Barr's 15% is measured against bugs that already survived
testing and review, a caveat their paper itself states). We ask a
better-posed question: of the runtime obligations a system's own
documentation *declares* — protocol error codes, RFC MUST sentences, alert
rules — what fraction has a predicate whose shape a type system could
discharge at compile time?

This reframing has three properties. It is *census-able*: obligation corpora
are finite, enumerable, and public. It is *falsifiable at the item level*:
every classification can be re-derived from the sentence or error text by an
independent rater. And it *localizes disagreement*: when two raters differ,
the difference is a specific boundary in a specific codebook rule, not a
worldview.

The unit of measurement is the **declared obligation**, and this bounds every
claim in this paper: a corpus of declared obligations cannot see obligations
never declared (which may still be checked ad hoc — but outside any declared
surface a census can count), and each corpus censors classes its language
cannot express (§4.1). We report what specifications say, not what software
does.

## 2. The codebook

[`codebook/classes.md`](codebook/classes.md) is the versioned instrument; it
defines classes by predicate shape:

| class | shape | eliminable? | canonical example |
|---|---|---|---|
| DOMAIN | monotone predicate on one value, no history | yes — enum/newtype/refinement | "transform must be one of 8 values" |
| TYPESTATE | ordering obligation over one object's history | yes — typestate/session types across the boundary | "commit without a prior attach" |
| REVOCABLE | a fact that was true and became false | no — needs a clock; this is the residue | "certificate revoked" |
| THRESHOLD | inequality against a chosen number | no — a policy line, not a fact | "p99 > 250ms" |
| CRYPTO-VERIFY | verification requiring secret/transcript material | no (at the type layer) | MAC, signature, PSK-binder checks |
| NEGOTIATION | emptiness of a two-party set intersection | no | "abort if offer ∩ config = ∅" |

plus bookkeeping classes (PROCESS, POLICY, META) and a **mandatory
UNCLASSIFIED bucket** that is reported, never absorbed.

Two structural findings are part of the codebook itself:

**Eliminability has a boundary even for DOMAIN.** A versioned,
forward-compatible boundary must admit values the current spec forbids
(wayland-rs generates `WEnum<T> = Value(T) | Unknown(u32)` deliberately), so
domain checks at versioned boundaries are not fully type-eliminable. This
limit was found in the data and bounds the thesis rather than inflating it.

**CRYPTO-VERIFY's discriminator is the secret, not the word "crypto."** DH
point validation (1 < Y < p-1, point-on-curve) is public arithmetic on one
value — DOMAIN, and type-eliminable. Some cryptographic checks are cheap to
discharge statically; the ones that are not all touch secret or
transcript-derived material.

### 2.1 Graduation discipline

CRYPTO-VERIFY and NEGOTIATION entered as *provisional* classes when the TLS
alert probe forced them, and graduated on two grounds of different strength,
stated separately. **One gate was pre-registered**: a falsifiability check —
registered as "CV = 0 and NEG ≈ 0 in the Wayland corpus," with registry
version-bind named as the one NEG candidate — confirmed at CV = 0/216 and
NEG = 0/216 on a from-source regeneration of the Wayland corpus, the named
candidate resolving below the declared-error layer (the check's sharpening)
([`census/wayland/cv-neg-falsifiability.md`](census/wayland/cv-neg-falsifiability.md));
note the check's scan is a vocabulary net whose hits were hand-adjudicated,
so it bounds false positives tightly and false negatives only weakly: the
fitted 172-item census — classifier-labeled on predicate text, with hand
adjudication of its flagged/ambiguous items and a deterministic hand-audit
sample — surfaced no secret-material or intersection-emptiness predicates,
but no full manual re-read of that corpus for CV/NEG shape has been done.
**The second ground — rater stability (§6) — was articulated at graduation
time, not pre-registered**, and NEG's first out-of-corpus contact promptly
tested it: the MLS census (§4.5) recorded a 0-vs-5 rater split on
capability-compatibility duties, exactly the dissolve-on-transmission risk
the graduation record flagged for a small-membership class (candidate
rule 15 in the census); on QUIC (§4.6), by contrast, NEG was
item-identical across both raters — a single item, the
application-protocol negotiation duty. Stability is strong for CV (the same six items in every
rater's recorded labels across four passes; one rater's four unarchived
labels inferred non-CV — limitation 7), thinner for NEG (2–3 items across
valid raters, with
its pass-3 blow-up under a paraphrased definition as the cautionary record).
A class that cannot fail a falsification test is vocabulary, not
measurement.

## 3. Method: the honesty rules

The codebook carries numbered rules; the load-bearing ones:

- **Rule 8 — classify on the predicate, never the identifier.** Names encode
  the author's intent, not the predicate's shape. Corpora classified by
  different methods are not comparable, and any finding that depends on
  comparing them is an artifact until re-run under one method.
- **Rule 9 — enforce rule 8 with a DISAGREE bucket, not discipline.** Both
  shipped classifiers classify each item twice — on the predicate (the
  measurement) and on the name (a hypothesis) — and report loudly where the
  two confident views differ. A name-based classifier fails *silently*; the
  unclassified bucket only protects you where the classifier knows it is
  guessing.
- **Rule 7 — name the class your corpus censors before reporting any
  percentage.** PromQL cannot express typestate; a protocol-error corpus can
  barely express thresholds; a MUST-sentence corpus cannot express what the
  spec never states. There is no uncensored corpus.
- **Rules 10–13** (added in two pre-registered amendment rounds, §6):
  guard-vs-predicate tie-break by *which type would discharge the
  obligation*; UNCLASSIFIED bounded by *wire-falsifiability*; NEGOTIATION
  restricted to the *existence* of a compatible choice, never the choice
  itself; DOMAIN/PROCESS split on whether a wire-observable configuration is
  obliged.
- **Rule 14 — the instrument is the codebook, verbatim.** Raters receive
  their instrument version's frozen pack byte-identical
  ([`codebook/rater-pack.md`](codebook/rater-pack.md) for v3); each
  pass report records the pack's git blob hash. §6 is the existence proof
  that a paraphrase of a definition is a different definition.
- **Rules 15–19** (the v4 amendment — one pre-registered round written
  after the five frozen-instrument censuses and the first foreign
  replication (§6),
  graded in §6.1): capability-compatibility duties resolve to
  transcript-checkable *containment*; spec-fixed bounds on datum
  quantities are DOMAIN however the constant was chosen; rule 10's
  "occurrence" is scoped by an in-corpus complement-state test;
  key-lifecycle duties split packet-class discipline (TYPESTATE) from
  key-material hygiene (PROCESS); deadline duties are REVOCABLE. The v4
  instrument is its own verbatim pack
  ([`codebook/rater-pack-v4.md`](codebook/rater-pack-v4.md)); every
  pre-v4 number in this repository was measured under v3 or an earlier
  frozen instrument and stays the quoted number for its corpus — v4
  results are a separate, version-labeled series (§6.1).

Deterministic self-audits (items ranked by content hash, first ~12
re-checked) are used within passes; blind re-rating by fresh raters between
passes; disagreements are **reported as ranges, never silently
adjudicated** into a point estimate.

## 4. The censuses

### 4.1 Monitoring layer: awesome-prometheus-alerts (n = 1,155)

Every alert rule in the corpus, classified on the query's predicate shape
([`census/promql/promql-classifier.py`](census/promql/promql-classifier.py)):
**902 THRESHOLD / 246 REVOCABLE (the classifier's STATE bucket) / 7
unclassified** — 78.1% / 21.3% /
0.6% of all 1,155, or 78.6% / 21.4% of the 1,148 classified (state both
denominators; the two ways of quoting differ by half a point and mixing them
is exactly the kind of error this project exists to prevent). TYPESTATE is
0 — and reporting that 0 as a fact about software would be wrong: **PromQL
cannot express "these events arrived out of order," so the 0 is a fact about
the query language** (rule 7). A prior-art sweep found no comparable
predicate-shape census of an alerting corpus.

### 4.2 Protocol layer: Wayland declared errors (n = 172)

Every declared `<error>` in core `wayland.xml` plus the extension corpus,
all seven classifier buckets: 82 TYPESTATE, 67 DOMAIN, 8 THRESHOLD, 6
REVOCABLE, 2 RESOURCE (server-side failure, not a client obligation), 5
AMBIGUOUS, 2 UNCLASSIFIED = 172. **87.6% of client-facing declared errors
are type-eliminable in shape** — 149/170, where 170 = 172 − 2 RESOURCE; on
all 172 declared errors the figure is 86.6% (both denominators, per our own
rule). One protocol; the number does not generalize to "protocol
boundaries." A reproducibility caveat unique to this corpus: the census-era
checkout was never pinned, so the 172-item corpus behind 87.6% is preserved
as reported numbers rather than as a regenerable artifact — running the
shipped pipeline today yields the n=216 superset, which carries no headline
(11.1% unclassified, plus an unresolved 24-item DISAGREE bucket disjoint
from it). The TLS and PromQL censuses do not share this gap
(TLS: full corpus shipped with full label maps for raters A, C, and D —
B's is partial, limitation 7; PromQL: byte-exact reproduction).
Three bounds on the claim, all from the data: the
versioned-enum limit (§2); the classifier's vocabulary was **fitted to this
corpus** (the retraction addendum makes reporting that dependency
mandatory, and the superset run — 79.0% of 214 client-facing (78.2% of all
216) at 11.1% unclassified — shows the sensitivity is real); and declaration is not universal even here — roughly
a third of extension files declare no errors (20 of 65 in the regenerable
superset checkout, experimental included; the census-era count was 20 of 53
on a checkout not shipped here). A regenerated superset corpus (216 errors, 2026-08-13 HEAD)
exists for the falsifiability check; its classifier run carries an 11.1%
unclassified bucket (post-census protocols, unfitted vocabulary) and
therefore has **no headline** — recorded as a live demonstration of the
corpus-fitted-vocabulary caveat.

### 4.3 Cryptographic protocol, alert granularity: TLS 1.3 alerts (n = 25)

The 30-minute probe ([`census/tls13/tls13-alert-census.md`](census/tls13/tls13-alert-census.md))
that forced the scheme to grow: 4-class coverage was only 60% (15/25; the
probe's original tally said 64% and was corrected at the publish gate — the
correction block in the probe file reconciles tally against item table),
with the uncovered mass internally structured — CRYPTO-VERIFY and
NEGOTIATION emerged here. It also produced the **granularity warning**: the entire TLS
state machine compresses into one alert code (`unexpected_message`), so
alert-vocabulary percentages under-represent typestate.

### 4.4 Cryptographic protocol, obligation granularity: RFC 8446 §4 (n = 204)

Every MUST/MUST NOT/SHALL sentence of the Handshake Protocol section,
classified sentence-by-sentence on predicate shape by rater A (an LLM agent; §6)
([`census/tls13/rfc8446-s4-census.md`](census/tls13/rfc8446-s4-census.md)).
Rater A: 94 TYPESTATE (46.1%), 73 DOMAIN (35.8%), 15 PROCESS, 6
CRYPTO-VERIFY, 6 UNCLASSIFIED-unverifiable, 3 NEGOTIATION, 2 each
REVOCABLE/THRESHOLD/POLICY, 1 META.

**Headline: 80–83% of the section's normative surface is type-eliminable in
shape** — precisely, the range across three valid raters is 79.9% (B) to
82.8% (D), with A at 81.9% (§6). The secret-dependent core is **6/204 =
2.9%, identical items in every rater of this study's recorded labels
(limitation 7)**.
The classes whose predicates types cannot even in principle discharge — CV
+ REVOCABLE + THRESHOLD + NEG — total ~6% (5.9–6.4% across raters; B's
endpoint assumes its four unarchived labels fall outside these classes).
The rest of the non-eliminable share is bookkeeping mass (PROCESS, POLICY,
META, U), not a type-resistance claim.

The granularity prediction from §4.3 is confirmed quantitatively: the alert
vocabulary shows 20% typestate where the obligation corpus shows 46% — a
compression factor of ~2.3. **Never compare protocol censuses at different
error-code granularities.**

Reading: the TLS 1.3 handshake's stated obligations are overwhelmingly state
machine and format discipline — by obligation count, the state-machine
surface class is roughly 16× (94/6) the size of the cryptographic one. That
proportion is consistent with, though it does not by itself explain, how
fruitful the state-machine attack family (SMACK/FREAK) proved against TLS
implementations.

(This corpus was later re-rated blind by two foreign model families under
the frozen instrument — the cross-family replication, §6 — again by
two blind raters under the repaired v4 instrument, §6.1 — and later
by three more foreign families in a second replication, §6.4.)

### 4.5 Cryptographic group protocol under the frozen instrument: RFC 9420 (MLS, n = 127)

Run 2026-08-13, after this paper's first publish gate, as the
second-security-RFC follow-up the TLS census left open — and designed to close the
provenance gap that study disclosed: the corpus (127 MUST/SHALL sentences,
§5–§15, same extraction recipe with the extractor shipped) and predictions
M1–M5 were committed **and pushed to the public repository before any
rater existed**. The instrument is the TLS pass-4 rater pack, verbatim
(blob `a08febba…`, hash-round-trip verified); one author pass (A′, labels
on disk before the blind pass returned) and one fresh blind rater (B′).
Full report: [`census/mls/rfc9420-census.md`](census/mls/rfc9420-census.md).

**Result: ≈57% type-eliminable in shape (A′ 56.7%, B′ 57.5%), raw
agreement 85.0%, eliminable-vs-not 89.8%.** Because instrument and
granularity match the TLS census exactly — and the recipe matches up to
two disclosed mechanical refinements (shipped extractor, within-paragraph
splitting; census README) — the TLS–MLS pair began this repository's one
**matched-method comparison**, extended to a triple by QUIC (§4.6)
(matched method, not matched population: TLS quotes three valid raters,
MLS and QUIC two each, one of them the author): the type-eliminable share
of a cryptographic protocol's censused normative surface ranges at least
from ≈57% to 80–83%. Where the mass went: MLS
obliges as MUSTs what TLS §4 leaves tacit — key-material deletion,
GREASE/extensibility processing, key-schedule procedure — putting PROCESS
at 18.9%/18.1% against 7.4% (TLS rater A) and 9.3% (rater D; B's is not
item-recomputable, limitation 7). The crypto core is
larger (CV 8.7%/7.9% vs 2.9%) and the mix is measurably *less*
state-machine-shaped.

Of the five pre-registered predictions, **only M1 (larger crypto core)
passed**; M2–M4 failed and M5 failed two of its three clauses — graded, per
the pre-commitment, against the author's structural model of MLS, with no
discretion over what to quote. The two instructive residues: THRESHOLD
split on *derived-but-not-chosen* constants (AEAD usage limits — decision
rule 3's structural-vs-chosen dichotomy is incomplete there), and NEG went
0-vs-5 between raters on **capability-compatibility** duties ("joiner MUST
support the group's extensions"), where rules 11, 1, and 12 each ground a
different reading (U / TYPESTATE / NEG). That three-way boundary is
recorded in the census as candidate rule 15 for a *future* instrument
version — under the frozen one, it stands as the measured edge of the
transmissibility law (§6). (That future version now exists: rule 15 of
the v4 amendment, whose prediction V1 — the five capability items land
TYPESTATE, NEG 0 — passed in both v4 raters, vocabulary-steered per the
pre-pass protocol; §6.1.)

### 4.6 Transport protocol under the frozen instrument: RFC 9000 (QUIC, n = 281)

Run 2026-08-13, immediately after the MLS census, as the third-corpus test
limitation 3 called for. Same discipline, same instrument (blob
`a08febba…`), predictions Q1–Q5 committed and pushed before any rater;
span §2–§19 (the transport machinery), which holds ~94% of the document's
MUST/SHALL-bearing lines — so the TLS-style span-coverage asymmetry does
not recur here. Full report:
[`census/quic/rfc9000-census.md`](census/quic/rfc9000-census.md).

**Result: ≈67–69% type-eliminable in shape (A″ 66.9%, B″ 69.0%), raw
agreement 85.1% — the third corpus in a row inside the TLS-measured
agreement band.** QUIC sits between MLS and TLS for a legible reason:
TYPESTATE is its largest class (45.6%/47.3% — stream states, flow control
against peer-advertised limits, connection-ID lifecycle, migration
ordering), but the span carries real PROCESS mass (17.1%/11.4%) and a
THRESHOLD family TLS §4 lacks (spec-fixed numeric limits). The crypto
core is 3/281 = 1.1%, item-identical in both raters — RFC 9001/9002 hold
QUIC's packet protection and loss recovery, and the document boundary
censors them out of this corpus (rule 7, predicted in advance this time).

Prediction outcomes: Q2 (smaller crypto core, document-boundary censoring)
and Q3 (TYPESTATE largest) passed; Q1 failed 2 of its 3 clauses (the
author's "nearer TLS" directional model missed — A″ landed below the
68–80% band floor and nearer MLS); Q4 **passed**: the rule-3
derived-but-not-chosen edge measured on MLS reproduced at scale, with
THRESHOLD's symmetric difference at 15 — ten of them spec-fixed constants
(20-byte connection-ID caps, the 1200-byte ICMP floor, an at-least-2 floor) —
now a candidate rule 16; and Q5 failed its crisp-class clause through a
**new** edge: REVOCABLE split 3-vs-0 on deadline duties ("acknowledge
within the peer-advertised max_ack_delay" reads as clock ⇒ REVOCABLE,
inequality ⇒ THRESHOLD, or procedure — a boundary TLS §4 and MLS never
stressed because they state no liveness deadlines). The MLS
capability-compatibility boundary also recurred, smaller (5 items on the
rule-11 U-boundary). All graded per the pre-committed interpretation:
wrong guesses about QUIC, licensing nothing. (The rule-16 candidate and
the deadline-duty edge became rules 16 and 19 of the v4 amendment,
graded in §6.1.)

### 4.7 The QUIC document family: RFC 9001 (n = 69) and RFC 9002 (n = 30)

Run 2026-08-13, immediately after the transport census, to cash its
rule-7 disclosure: QUIC's packet protection lives in RFC 9001 and its
loss recovery in RFC 9002, and a claim about "QUIC" from RFC 9000 alone
sees neither. Same discipline (corpora frozen and predictions K1–K5,
R1–R5 pushed publicly before any rater; instrument blob `a08febba…`
verbatim). Full reports:
[`census/quic-tls/rfc9001-census.md`](census/quic-tls/rfc9001-census.md),
[`census/quic-recovery/rfc9002-census.md`](census/quic-recovery/rfc9002-census.md),
synthesis [`census/quic-family.md`](census/quic-family.md).

**RFC 9001 (the TLS shell): 54–67% eliminable, quoted wide because raw
agreement was 76.8% — the first census below the pre-registered 78–90%
transfer band (itself set from TLS's measured 81–90%).** All five
pre-registered predictions failed, led by the central one: CV was
predicted at 25–45% ("the crypto document") and measured at **1.4%/2.9%**.
The document's MUST-sentences state the shell around its cryptography —
key lifecycle, phase gates, AEAD limits — while verification itself is
described in non-normative grammar a MUST-sentence census cannot see:
rule-7 censoring operating *inside* a document, not at its boundary. The
band break localizes: ten of sixteen disagreements are one boundary
(author read key-lifecycle duties as internal PROCESS; the blind rater
read eight as connection-phase TYPESTATE and two as DOMAIN), on the corpus densest in exactly the
judgment boundary the codebook already knew was soft. The five AEAD-limit
items, meanwhile, were THRESHOLD item-identical in both raters — the
rule-3 edge predicted to split here did not (a prediction of disagreement
falsified by unanimity). (The v4 amendment's rule 18 was written at the
key-lifecycle boundary; under it, this corpus re-rated at 94.2%
cross-family agreement — §6.1.)

**RFC 9002 (the recovery shell): 23.3% eliminable — the low end of the
frozen-instrument MUST-corpora — with identical item sets in both raters
and agreement of 96.7%; ~60% PROCESS.** One protocol deviation, disclosed in the
report's setup: the first blind rater's labels were seen by the author
before the author pass had run, so the author pass was abandoned and
replaced by a second fresh blind rater — this census has two blind
raters, no author rater, no authorial error bar, and the
shared-model-prior caveat (limitation 6) applies at full force to its
high agreement.

**The family synthesis:** within one protocol — era and authorship held
fixed; rater pairs, spans, and n varying — the eliminable
share spans 23% → 69% by document role. Pooled across the family, with
the pooling caveat stated in the synthesis before the number: **≈61–65%
of QUIC's stated normative surface is type-eliminable in shape**, ~4–6
points below the transport document's own figure.

### 4.8 A data format under the frozen instrument: RFC 5545 (iCalendar, n = 225)

Run 2026-08-15, after the v4 cycle of §6.1, as the frozen-instrument
series' first
NON-protocol corpus — every prior span is protocol or monitoring prose,
so the spectrum reading had never been tested across a genre change.
Selection was by pre-fixed criteria (non-protocol; standards-track
RFC 2119 genre; largest normative surface) over eight counted RFC
candidates plus a ninth counted-and-excluded non-RFC draft, and the counting itself produced a finding: **data-format
RFCs are normatively thin** — URI syntax (RFC 3986) contains literally
zero MUST/SHALL lines; format documents state their obligations as
grammar a MUST census cannot see. RFC 5545 is the usable outlier
because it writes obligations *into* its grammar as ABNF comments, and
its corpus needed three disclosed mechanical recipe refinements
(depagination of a pre-2019 RFC; an ABNF-comment paragraph stream; and
exclusion of example data, after the pre-push gate found a sample
calendar entry whose free text — "Phoenix design team MUST attend this
meeting" — had been extracted as a classifiable obligation). The full
rater roster was pre-registered — same-family model name included, a
first for the series (a fresh same-family
instance and Grok 4.6; no author rater) — and predictions N1–N6 pushed
before any rater. Full protocol and report:
[`census/ical/`](census/ical/README.md),
[`census/ical/rfc5545-census.md`](census/ical/rfc5545-census.md).

**Result: 88.0%/88.4% type-eliminable in shape — above every
frozen-instrument protocol span — with raw agreement 97.3%, then the
highest between any two raters in
this repository [since surpassed by the same corpus's v6 pair at
98.7% — §6.3] (cross-family, n = 225; the prior record was 96.7% on
RFC 9002's 30 items; later tied exactly by the corpus's own v4
re-rating, §6.1; the corpus-shared-prior caveat of limitation 6
applies at full force to agreement this high, per the census
report).** The composition carries the reading: DOMAIN
alone is ~87% of the corpus; TYPESTATE, the largest class of TLS,
QUIC, and RFC 9001, collapses to 1 (same-family) and 4 (foreign)
items — this span states no counterparty duties, part genre and part
document boundary (its scheduling counterpart lives in iTIP), and the
only both-rater TYPESTATE item is a delegation-inheritance duty, the
remnant of ordering. THRESHOLD, REVOCABLE, CV, and NEG are all
**zero in both raters** (CV = NEG = 0 was the pre-registered
falsifiability prediction, N3) — and the zero THRESHOLD is itself a
result: the spec-fixed-constant edge behind ten of QUIC's fifteen-item
THRESHOLD symmetric difference did not fire at all here — 45
cardinality duties ("MUST NOT occur more than once") went DOMAIN
unanimously in both raters (same instrument, different rater models;
the confound is named in the protocol). Prediction grades, per the
frozen wording: N1/N3/N5/N6 passed in both raters; **N2 failed in the
foreign rater by exactly one item** (88.4% against an inclusive
[72%, 88%] band, while the same-family rater landed exactly on the
endpoint); **N4 — a determinism probe over 14 groups of
verbatim-duplicate texts — failed in the foreign rater** with one
identical-text pair split across chunk contexts (the same-family rater
was 14/14 deterministic). Two censoring caveats are pre-registered and
bound the genre claim: the scheduling protocol (iTIP) is a separate
document, and grammar-stated obligations are invisible to this census.

### 4.9 What does *not* survive across corpora

An early cross-layer claim — "the class mix is a property of the layer" —
was **retracted the day it was written** and the retraction is preserved in
full in the codebook. The mm-lux row (a private runtime-monitor codebase
whose contracts formed an additional, unshipped corpus) had been classified by
contract *name*; re-read on predicates, the inversion vanished. Both misfilings
pointed in the direction of the thesis — the diagnostic signature of a
classifier tuned by its author's expectations. What survives is the
per-corpus numbers above, each named with its layer and its censoring —
plus the one cross-corpus artifact built to survive: the frozen-instrument
comparison set (TLS–MLS–QUIC, QUIC's document family, and the
iCalendar corpus, §4.4–§4.8),
which is admissible precisely because those spans were rated under a
single frozen instrument instead of being read across methods (with
the iCalendar point rater-model-unmatched to the rest, per its
protocol).

## 5. The retraction as method: error-sign analysis

The retraction (codebook, "RETRACTION — 2026-08-02" and its addendum) is
included verbatim because its failure modes generalize:

1. **A silently-confident classifier is worse than no classifier.** The
   name-based pass placed every item confidently and produced a wrong
   headline with no distress signal. The unclassified bucket cannot catch
   this; only a second, independent view of the same item can (rule 9's
   DISAGREE bucket — which, applied retroactively, catches both original
   misfilings).
2. **When every error points toward the thesis, the instrument is tuned.**
   Two misfilings, both pro-thesis, is not bad luck; it is
   expectation-leakage, and checking error *signs* is cheaper than checking
   error rates.
3. **A fix is new content and needs the same verification.** The addendum's
   accuracy lens found that the codebook's own `\b`-regex war story had
   credited one regex bug with four interventions' effect (the bug alone
   explains 15.2 of the credited 27.9 percentage points; three corpus-fitted
   vocabulary expansions did the rest) — the corrected story is itself a
   caveat on the 87.6% figure.

## 6. The transmissibility study: four passes, and a stop whose interpretation was pre-registered

Raters B, C, and D are fresh LLM-agent instances — blind to each other, to
the tallies, and to the authors' expectations. Rater A is the census
author: an author-rater whose context is by definition not controlled —
finding 3 below measures exactly that leakage. (See limitation 6 for what
this rater population does and does not control.) The §4 census's
20-item DISAGREE bucket (raw two-rater agreement 90.2%, eliminable-vs-not
96.1%) localized two codebook gaps. We repaired them under pre-registration
and re-rated — twice — with every prediction committed to git before the
rater existed. (Provenance, stated before a reader discovers it: this
repository was scaffolded from working artifacts on the morning the passes
ran — the scaffold commit discloses the migration — so the ordering claims
are witnessed by the in-repo commit sequence and the cited blob hashes,
with minutes-scale gaps consistent with LLM-agent raters; there is no
older-timestamped record. One more provenance grain: pre-gate commit
*messages* carry pre-gate wording — one asserts THRESHOLD/REVOCABLE
transmitted with zero variance, which the files correct to "one recorded
flip" — and messages cannot be amended without rewriting history, so the
files, not the messages, are the corrected record.)

- **Codebook v2** (rules 10–11, predictions: gains concentrate in the 20;
  headline stays in 80–82%). **Pass 3 failed its criterion** — headline
  69.6% — and the failure localized to an *instrument* defect: the rater
  prompt had **paraphrased** NEGOTIATION ("selected value in the
  intersection") where the codebook says *emptiness* of the intersection;
  the paraphrase annexed decision-rule-1 territory (the census's
  cross-message-consistency rule) and 16 items migrated. The pass
  is archived invalid ([`rfc8446-s4-pass3.md`](census/tls13/rfc8446-s4-pass3.md)).
  The pre-registered failure clause ("evidence the repair is mis-designed,
  not evidence of a new result") is honored on the number — none is taken
  from this pass — while its blame assignment (repair mis-designed) is
  overridden by the post-hoc instrument diagnosis, a failure mode the
  pre-registered dichotomy did not anticipate; the pass-3 report records
  this as a deviation-with-reason, not compliance.
- **Codebook v3** (rules 12–14 + the verbatim rater pack; predictions: NEG
  single digits, 184-item agreement ≥ 90%, headline in 80–82%, rule-10
  pattern reproduces). **Pass 4: 1 of 4 predictions passed**
  ([`rfc8446-s4-pass4.md`](census/tls13/rfc8446-s4-pass4.md)). NEG healed
  completely (23 → 2; all 16 collision items returned). But item-level
  agreement recovered only to 86.4%, the headline landed at 82.8%, and two
  guard-vs-predicate items flipped between passes. The pre-committed
  interpretation applies: **the codebook is not transmissible by text alone
  at item granularity.** The decision not to run a pass 5 was made at
  close-out (each further rule would be fitted to this corpus's residuals);
  what was pre-registered is the interpretation just quoted. The quoted
  range widening to 80–83% is a **recorded post-hoc deviation** from the
  same pre-registration, whose failure clause promised "that verdict, not a
  new headline": rater D's *instrument* was valid even though the
  predictions about D's output failed, and excluding a valid rater whose
  result is inconvenient would be cherry-picking in the other direction —
  but the pre-registration made no valid-instrument carve-out, so this is
  an update with a stated reason, not compliance. C stays excluded because
  C's instrument measured a paraphrase, not the codebook (the full
  reconciliation, including the pass-3/pass-4 asymmetry this creates, is in
  the pass-4 report).

What four passes measured:

1. **Discriminator-crispness predicts transmissibility.** CV and META were
   **item-for-item identical in every rater's recorded labels, including the invalidated
   pass**; THRESHOLD and REVOCABLE were identical across the other three
   raters with exactly one recorded exception (rater B read one flagged
   item, the 7-day cap, as REVOCABLE rather than THRESHOLD). All residual
   disagreement lives on judgment boundaries (DOMAIN/TYPESTATE via rule
   10's "does the required value vary with history?"; DOMAIN/PROCESS).
   Two qualifications: the zero-variance classes are small (1–6 items), so
   perfect agreement there is weaker evidence than the same rate on a
   90-item class; and citing the invalidated pass here is principled
   because its defect was localized (the NEG boundary), leaving concordance
   on untouched classes evidential. Inter-rater agreement is a per-class
   property, predictable from the shape of the rule — directionally, not
   as a quantitative law.
2. **The headline is robust at claim granularity even where items are
   not:** across all valid-rater pairs (A–B, A–D, B–D), eliminable-vs-not
   agreement spans 87–96% against raw item agreement 81–90% (A–B 90.2/96.1,
   A–D 83.8/89.2, B–D bounded 80.9–82.8 / 86.8–88.7 because four of B's
   labels were never archived) — most disagreement is interior to the
   eliminable family.
3. **Authorial context leaks into labels, measurably.** 15 items have both
   fresh raters agreeing on the same alternative label against rater A.
   (Rater C's participation here survives pass 3's invalidation by the same
   localization standard used for CV: none of C's labels on the 15 items is
   NEG, so the paraphrase defect does not touch them — checked against the
   archived labels.) Those 15 are the census's visible error bar; they
   remain unadjudicated and are listed in the pass-4 report.

The law in finding 1 got its first out-of-corpus test later, on MLS
(§4.5): agreement landed inside the TLS-measured band, META/REVOCABLE
transferred with zero variance, and CV came within one item (the
extraction artifact of limitation 4), but two edges surfaced — THRESHOLD
moved on derived-but-not-chosen constants, and NEG split 0-vs-5 on a
boundary the codebook has no rule for. The second test, on QUIC (§4.6),
sharpened the picture: agreement again in band (85.1%), CV/META/NEG at
zero variance — but the THRESHOLD edge reproduced at scale (symmetric
difference 15) and a new REVOCABLE edge appeared on deadline duties. The
third and fourth tests (§4.7) bounded the story in both directions:
RFC 9002 agreed at 96.7% (above the band — two blind same-family raters,
so shared priors and crisp procedure are confounded there), while
RFC 9001 fell BELOW the band at 76.8% — the first breach, with ten of
its sixteen disagreements on one already-known judgment boundary
(PROCESS/TYPESTATE over key lifecycle) that its corpus happens to stress
harder than any other. The fifth test (`census/foreign/`) varied the
*rater* instead of the corpus: two foreign frontier model families —
GPT-5.6 Sol and Grok 4.6, run blind over the TLS corpus under the frozen
instrument, with predictions pre-registered and publicly pushed before
either rater existed — and the predicted cross-family degradation failed
to appear at claim granularity for either rater, with raw-granularity
degradation at most mild. Grok agreed with rater D *above* the
intra-family ranges (91.7% raw / 98.0% eliminable-vs-not); GPT sat at the
raw floor against D (81.4%) and just below the range against A (80.4%);
and every item of the CV set drew a CV label from all six raters then
recorded — four Claude-family passes and both foreign families — hit
exactly by five of the six (rater B's exactness by inference; limitation
7; both v4 raters later extended the streak, §6.1), while GPT extends
its CV class to three additional key-schedule sentences (a third family's reading of the same key-lifecycle boundary
RFC 9001 and MLS stress). Their quotients: 80.9% (inside the Claude band) and 76.5%
(below it — the gap fully accounted for by GPT's 18-item U habit;
resolving its 16 non-consensus refusals to D's labels yields 82.4%,
inside the band). Twelve items of cross-family consensus against D
concentrate on two nameable edges; nine of them are checks conditioned on
negotiated or prior-message state — three from the original
guard-vs-predicate DISAGREE mass that rule 10 was written to tie-break —
and are candidate rule 17: the residue of a repair, found by raters from
families that share none of the repairer's training lineage. The law survives with its edges
now mapped rather than merely suspected — transfer is a property of how
hard the corpus leans on the soft boundaries, whichever family reads it —
and the edges are where the next instrument version's rules (candidates
15–17, plus the key-lifecycle and deadline observations) were then in
fact written — the v4 amendment, graded next.

### 6.1 The instrument repaired: the v4 amendment and its grades

Every edge the study mapped was written into the instrument on
2026-08-14. The v4 amendment
([`codebook/classes.md`](codebook/classes.md), commit `d3d4c2d` —
appended, never edited in place, per the v2/v3 discipline) adds five
rules at the five measured boundaries: rule 15
(capability-compatibility resolves to transcript-checkable containment
— the MLS three-way split), rule 16 (spec-fixed constants: THRESHOLD
requires a non-datum quantity — the QUIC/MLS derived-constant edge),
rule 17 (a complement-state test scoping rule 10's "occurrence" — the
foreign-consensus residue), rule 18 (key/phase lifecycle: packet-class
discipline is TYPESTATE, key-material hygiene is PROCESS — the RFC 9001
band-breaker), and rule 19 (deadline duties are REVOCABLE — the QUIC
deadline edge). Because the amendment's net predicted direction is
thesis-friendly, the error-sign lesson (§5) was applied to the
instrument itself: eight itemized predictions (V1–V8) were
pre-registered in the same commit, before any v4 pack or rater existed;
every v3 number was ring-fenced (a v4 result never replaces a v3
headline — v4 shares are a new, version-labeled series); and the
amendment states in advance that movement beyond the itemized
predictions is evidence of instrument mis-design, not a new result. V8
is the design's tell: it predicts the amendment will flip decision rule
3's own worked example (TLS item 188 THRESHOLD→DOMAIN, item 189
THRESHOLD→REVOCABLE), emptying the v3 TLS THRESHOLD class — a
pre-registered bet against the codebook's own canonical illustration.

One methodological cost is disclosed before each pass rather than
discovered after: the v4 rules quote real corpus items as worked
examples, so a prediction about a quoted item is settled by
construction. The pre-pass protocols
([`census/v4-tls/README.md`](census/v4-tls/README.md),
[`census/v4-completion/README.md`](census/v4-completion/README.md))
therefore name, per prediction, which items the pack settles and which
carry evidence — a distinction the grades below depend on. (That
disclosure itself had one omission: the pack's retained rule-16/19 seam
example names the content of V8's two items. It was found at this
paper's own publish gate, is corrected in the protocol and the report,
and V8 below carries the resulting discount.)

Eight blind rating passes ran on 2026-08-14, two per corpus: a fresh
same-family instance given the pack and corpus as a single file, and
Grok 4.6 over the replication's cursor-cli transport. The instrument is
[`codebook/rater-pack-v4.md`](codebook/rater-pack-v4.md) (blob
`4891605…` — the v3 pack verbatim plus the v4 rules, with one disclosed
elision), served blind; there were zero protocol events across all
eight passes. The grades, fixed at `d3d4c2d`: **V1, V3, V5, and V8
passed in both raters — V1 vocabulary-steered and V8 example-settled,
discounts recorded; V6 passed in all eight rater-corpus grades (most of
its items pack-settled); V2, V4, and V7 failed.** Full reports:
[`census/v4-tls/rfc8446-s4-v4pass.md`](census/v4-tls/rfc8446-s4-v4pass.md),
[`census/v4-completion/rfc-v4-completion.md`](census/v4-completion/rfc-v4-completion.md).

What the eight passes measured:

1. **The key-lifecycle repair transmits.** V5's predicted 5/4 split of
   RFC 9001's lifecycle cluster — which sides with *neither* archived
   v3 rater — reproduced exactly in both families, including all five
   items the pack does not name. RFC 9001, the corpus that broke the v3
   agreement band at 76.8%, agreed at **94.2%** cross-family under v4,
   its between-rater share gap narrowing from 13.1 points to 2.9. (One
   caveat on the v3→v4 agreement deltas: the v3 pairs for MLS, QUIC,
   and RFC 9001 each contain the author rater and the v4 pairs do not,
   so on those corpora instrument version and
   rater composition change together — V5's item-level reproduction is
   the part that isolates the rule.) The
   TLS corpus set its own record: Av4-vs-Xv4 raw 92.2% /
   eliminable-vs-not 96.1%, a cross-family pair above every v3 pair on
   that corpus (since surpassed by the corpus's v5 pair at 93.6%, §6.2) (RFC 9002's 96.7% on its 30-item corpus was then the
   repository-wide record — since surpassed by the iCalendar pair's
   97.3%, §4.8, and again by its v6 pair's 98.7%, §6.3). MLS rose to 88.2% (v3: 85.0%). And both v4 TLS
   raters kept the CV class at exactly the same six items — the six CV
   items have now drawn CV labels from seventeen TLS raters, exactly
   six in thirteen of them (G extends the class by three, §6; the v5
   same-family rater by one, torn, §6.2; both v6 raters exactly six,
   §6.3; the second replication's Gemini by one and Kimi by four,
   GLM exactly six, §6.4; both v7 raters exactly six, §6.5; B's
   exactness by
   inference, limitation 7).
2. **The rules generalize past their named items — one of the two
   reasons the no-regression clause failed everywhere.** V7's match-rate clause
   passed in all eight rater-corpus grades (TLS: 94.2% in each rater
   against an 83.8% floor; QUIC's same-family rater cleared its floor
   with zero items to spare). Its count-bound clause failed in all
   eight — under both readings of its own ambiguous wording, a fork
   discovered at grading time and recorded, not repaired; zero-spread
   classes carry zero tolerance, so a single moved item fails them. Two
   of the failures are the finding: both raters independently moved the
   five-item sub-bucket {30, 31, 32, 56, 57} — the state-conditioned
   sub-bucket of TLS's original 14-item guard-vs-predicate DISAGREE
   mass, rater B's
   2026-08-12 reading — from DOMAIN to TYPESTATE (rule 17 reaching one
   sub-bucket past the items the author named), and both moved six
   un-named QUIC THRESHOLD items to DOMAIN (rule 16 generalizing the
   same way). A repair rule acts on a boundary, not an item list; the
   author's named-sets were systematically too narrow; the grades
   stand, and a v5 owes a per-item-scoped no-regression clause
   (delivered: rule 23, §6.2).
3. **Two predictions failed on precisely their hardest items.** The
   protocol had disclosed that rule 16's examples settle eight of V2's
   nine predicted QUIC items; all eight landed as told (evidentially
   empty), and the sole un-named item — 191, an ignore-duty triggered
   by a datum bound — landed PROCESS in both raters against the
   predicted DOMAIN. V4 missed on exactly the item its history flagged:
   TLS item 67, the one member of its nine whose complement evidence is
   a response duty rather than a field value — DOMAIN in the
   same-family rater, TYPESTATE in the foreign one. Both failures grade
   the rule texts, license nothing, and are recorded as seams for a
   future version.
4. **QUIC is v4's measured cost.** Its cross-family agreement (84.0%)
   sits below the v3 pair (85.1%) — then the only corpus where v4
   agreement was not the best on record (after v5, the v4 pair led
   only on iCalendar, where it ties the v3 record at 97.3%; §6.2's
   pairs lead TLS, QUIC, and RFC 9001, and after v6 the iCalendar
   lead passed to the v6 pair at 98.7% — §6.3) — with churn concentrated on the PROCESS
   boundary: rule 18's lifecycle vocabulary appears to pull procedure
   readings beyond key/phase contexts, and the same-family v4 share
   (63.7%) fell below the v3 band. An instrument version now has its
   gains and its price as numbers, side by side. [Since decomposed:
   the cross-roster replication below re-measured QUIC under v3 with
   the new roster-shape at 81.9%, so the 85.1 → 84.0 drop splits into
   a −3.2-point roster effect and a +2.1-point instrument recovery,
   with the replication's three caveats.]

The v4 shares (new series, never mixed with v3): TLS 81.9%/82.8% —
inside the closed v3 band, one rater at its exact upper endpoint; MLS
59.1% in both raters; QUIC 63.7%/68.7%; RFC 9001 60.9%/58.0%. The
spectrum's shape is unchanged. Two items the amendment carved out
without prediction (QUIC 63 and RFC 9001 item 15) split between the v4
raters and remained unruled under v4 [since adjudicated by v5's rule
20 and graded as Z1/Z3 — comprehension checks, both PASS — §6.2].

One later data point joins the transmissibility record: the iCalendar
census (§4.8), run after this cycle under the frozen v3 instrument,
paired an ~87%-DOMAIN corpus with what was then the repository's
highest raw agreement (97.3%, cross-family; the corpus's v6 pair
later reached 98.7% — §6.3) — the crisp-discriminator law's
cheapest extreme, with the shared-prior and rater-model caveats stated
in §4.8 — while its N4 determinism probe recorded the series' first
identical-text label split, by the foreign rater across chunk
contexts. A pre-registered v4 re-rating of the same corpus with the
same rater models (`census/v4-ical/`) then ran the amendment's null
test: departures from both archived v3 labels were 1 and 3 in 225,
THRESHOLD and REVOCABLE stayed exactly zero, and the owed
PROCESS-churn lists were empty in both directions for both raters —
rules 16, 19, and 18 are inert where their boundaries do not occur,
and rule 18's QUIC cost did not travel to a genre without lifecycle
content. Its pair agreement tied the v3 record at 97.3%; its one
failed prediction reproduced the v3 foreign rater's identical-text
split on the same group, polarity reversed.

A second registered replication (`census/quic-replication/`) then
re-rated QUIC under the frozen v3 instrument with the same
roster(-shape), completing three cells of an instrument × roster grid:
the THRESHOLD wobble reproduced at symmetric difference 14 (old pair:
15), with the role-ordered side assignment flipping item-for-item on
eight of the ten spec-fixed constants and the fresh same-family rater landing
THRESHOLD in both passes — persistence across a complete roster change
that marks decision rule 3's gap as an instrument defect, the
strongest evidence yet for rule 16's repair target. Its one failed
prediction fell low (pair agreement 81.9%, the worst measured cell),
which decomposes the v3-old → v4-new drop (85.1% → 84.0%) into a
−3.2-point roster effect and a +2.1-point instrument recovery — v4's
QUIC "cost" (finding 4 above) reframed, under the replication's three
caveats (an unrecorded v4 same-family model name; a roster bundle of
era, composition, and author-presence; single-cell stochasticity) and
with its error-sign stated in the report: the reframe exists only
because the pass's sole failed prediction failed low.

### 6.2 The cycle closes: the v5 amendment and its passes

Where v4 was cut from a census series, v5 (2026-08-15, same
append-only discipline) was cut from a *grading record* — eight v4
prediction grades, two format-genre passes, and the cross-roster
replication — and that difference forced a design admission stated at
cut time: an amendment whose rules must describe the seams they
repair settles its own named-item predictions by construction, and no
elision can restore discrimination when the settling text *is* the
rule body. The v5 amendment (rules 20–24: reaction-duty content
selection; nonaction arrival-channel discrimination; the designated
serialization unit; a per-item-scoped no-regression redesign after
the count-bound clause's eight measured failures; and registration
hygiene with a mechanical settlement-downgrade trigger) therefore
declares its five adjudication predictions (Z1–Z5) comprehension
checks up front and moves the discriminating load to stability
predictions (Z7's 49-item both-rater DOMAIN set, which the rules
never name, its bound derived from measured disagreement counts; Z6,
itself downgraded to a comprehension check at registration when rule
24's ICMP trigger fired) and
to rule 23's registered floors and bounds — each frozen per pass with
measured *failability* (on QUIC, one archived rater fails both
clauses; on RFC 9001, the floor is one no measured prior rater had
cleared; on iCalendar, the departure budget is one item).

Eight blind passes then ran across the four re-rated corpora
(`census/v5-quic/`, `census/v5-completion/`; per corpus a fresh
same-family instance and Grok 4.6, both pre-registered by model name
per rule 24, zero protocol events across all eight). **Every Z clause
passed in every rater** — including Z3, the amendment's disclosed
contested bridge, which sided with one archived reading in four and
landed TYPESTATE in both RFC 9001 raters, the same-family one
emitting the series' most telling torn-flag (`TYPESTATE?`) on exactly
that item; and Z5, whose served pack contains zero iCal-specific text
and whose foreign rater overturned all six of its family's archived
TYPESTATE readings. Z4's two-corpus conjunction settled PASS. Three
results carry the section's weight:

1. **A full instrument-evolution cycle closed on the QUIC churn.**
   The monotonicity-guard quartet (items 11, 19, 261, 272) was
   TYPESTATE in 14 of 16 v3-era readings, flipped to PROCESS in both
   v4 raters (the churn §6.1's finding 4 recorded), and reverted to
   TYPESTATE in both v5 raters — under a pack whose only
   quartet-naming text says rule 21 does *not* decide them.
   v4 introduced a churn; the replication located its cause in the
   instrument; v5 named the boundary undecided; the churn reversed
   (consistent-with, not established: the v4 same-family model name
   was never recorded, and the flip's direction sits inside rule 20's
   disclosed reach). QUIC's v5 pair agreed at 89.7%, its best
   measured cell.
2. **The redesigned no-regression machinery caught the amendment's
   own undisclosed reach — the pre-committed mis-design verdict,
   delivered by the instrument against itself.** On iCalendar both
   v5 raters failed both rule-23 clauses (matches 211 and 215
   against a floor of 219; departures 11 and 7 against a budget
   of 1), with a six-item cross-family consensus core of tolerance duties —
   four verbatim "MUST ignore x-param / iana-token values they don't
   recognize" items, two adjacent (invalid-part and
   precision-acceptance duties) — that the v3/v4 raters read PROCESS
   and rule 21's in-grammar branch reads DOMAIN. The same shape
   drives a marginal TLS failure (one rater, one item over its
   bound) on "MUST ignore unrecognized extensions" items. This is
   the third instance of the series' recurring phenomenon — a
   repaired rule reaching items its author never enumerated (rule 16
   in §6.1, rule 17 in the v4 TLS pass, rule 21 here) — but the
   first the registered tolerances converted from a silent
   eliminable-ward share improvement into recorded FAILs and a named
   defect: the amendment disclosed rule-level reach for rules 20 and
   22 and not for rule 21. The v5-iCal shares (93.8%/91.1%, against
   88–89% in both earlier series) are quoted *only* as the size of
   that defect; the v3 and v4 iCalendar headlines stand, and a v6
   owes rule 21's branch-1 scope boundary (delivered — §6.3).
3. **On the corpora where the disturbance was absent or marginal,
   agreement kept rising.**
   RFC 9001 was the completion's cleanest cell — both raters cleared
   the previously uncleared floor, the v4 amendment's signature 5/4
   lifecycle split held item-for-item in all four v4/v5-era raters,
   and the pair set the corpus record at 95.7%; TLS's v5 pair set
   its corpus record at 93.6%. iCalendar's 97.3% record stood (the
   v5 pair, drifting from the anchors together, agreed at 96.9%; the
   v6 pair has since taken the record to 98.7% — §6.3).

The v5 shares (a third version-labeled series, never mixed with the
others): QUIC 67.3%/66.5%; TLS 84.8%/84.3% — above the closed v3
band, an eliminable-ward drift the error-sign accounting attributes
to the same rule-21 reach, within tolerance for one rater and one
item over for the other; RFC 9001 59.4%/59.4%; iCalendar quarantined
per finding 2. The series' standing law gets its sharpest
formulation from this cycle: a versioned instrument does not just
transmit better as its discriminators sharpen — properly
pre-registered, it can catch its own author's next error, in public,
with the verdict written before the evidence — as it did here.

### 6.3 The verdict answered: the v6 amendment and its first pass

The v6 amendment (2026-08-16, rule 25 with pre-registered predictions
J1–J6) is the first in the series cut from an *upheld* pre-committed
instrument-mis-design verdict on the classifying rules themselves.
Its one rule draws the boundary the conviction demanded by applying
rule 16's existing locality litmus to the suppression trigger: rule
21's first branch requires a predicate that is a pure function of the
designated serialization unit, and a predicate on the receiver's
capability set — an element it "does not recognize" or support, from
a deliberately open space — is decidable by no unit-local validator
and classifies as conduct. The rule deliberately sides with neither
rater cohort (the drifted recognition family reverts to the archived
consensus, while the validity- and precision-triggered pair the
conviction's core also carried is predicted to STAY with the v5
readings against all four pre-v5 raters), and it *declines* every
sibling shape whose archived evidence is mixed — mode- and
state-conditioned, history-conditioned, designated-field,
conjoined-trigger, and compound-sentence duties — recording their
archived histories rather than ruling on them. Its own gate caught
the series' author-friendly omission class twice more in the
amendment's draft: QUIC histories quoted over six readings where the
archive holds eight, and a first-pass precedent undercounted ("one
archived precedent" where a second is derivable from the pass-2
archive) — both leaning the author's way.

The first v6 pass (`census/v6-pass/`; iCalendar, TLS, and QUIC — the
three corpora rule 25 touches — six blind passes, zero protocol
events) hardened the registration machinery again before any rater
ran: the settlement audit's paraphrase judgment was exercised by the
registration's own cold reviewer and recorded verbatim (J4, the
amendment's contested edge, was DOWNGRADED to a comprehension check
— each candidate phrase in the served rule maps to exactly one live
corpus item); the no-regression outside sets exclude the stability
predictions' enumerated items, per the v5-quic precedent; and the
convicted corpus was registered at the series' harshest tolerance —
a both-anchor departure budget of ZERO, an achieved, measured count.
Three results carry the section:

1. **The repair holds exactly where the instrument was convicted.**
   iCalendar passed all four rule-23 clauses in both raters at the
   zero bound — no outside-set item moved from both anchors in
   either family — every recognition item reverted to PROCESS
   (J1/J2/J3 passed in all six rater-corpus readings), both shares
   landed at 88.9%, inside the pre-conviction anchor band, and the
   pair's raw agreement of **98.7% is the repository's record**
   (prior: the same corpus's 97.3%; at eliminable-vs-not granularity
   the corpus's own v3 pair remains higher, and RFC 9002's 100%
   record stands). The J5 stability floor passed at its exact edge in
   both raters, on different single items; the TLS floor passed with
   room, one rater perfect.
2. **One adjudication failed to transmit, in both raters — and it
   maps a boundary sharper than the rule that drew it.** J4's
   validity half held (item 62: DOMAIN in all four v5/v6-era
   readings, after four pre-v5 PROCESS), but its precision half
   failed (item 150: PROCESS in both v6 raters, six of its eight
   readings ever) — raters transmit grammar-validity as parsing
   contract and refuse precision-acceptance, even served text
   claiming both. The registration's downgrade of J4 was thereby
   vindicated and its stated premise falsified at once: the ruling
   held that the served text *settles* the item, and the item
   declined to be settled. Registration-time rulings about what an
   instrument's text settles are themselves falsifiable predictions;
   this pass graded one. A v7 owes the precision-trigger wording
   *(delivered — rule 26, §6.5)*.
3. **The no-regression machinery convicted the author again — this
   time on calibration, in the thesis-unfriendly direction.** The
   TLS cell failed both clauses in the foreign rater (match 132
   against a floor of 134; 11 departures against a budget of 6 that
   the same-family rater passed exactly at the edge). The mechanism
   is not rule 25's: the departure mass sits on the
   guard-vs-predicate sub-bucket (flipping to the census author
   rater A's own archived v3 reading), on a declined mode-conditioned
   item, and on long-soft preparedness/alert items — two of eleven
   eliminable-ward — while the rater's DOMAIN stability set was
   perfect (56/56). What the FAIL convicts, per the pre-committed
   interpretation, is the author's registered model of cross-family
   churn; it stands as graded.

The steer ledger settled with one finding the v7 docket inherits
*(decided — rule 27, §6.5)*: the
two mode-conditioned duties (TLS 64, QUIC 232) reverted PROCESS-ward
in all four v6 readings — consistent, cross-family movement on
exactly the shape rule 25 declined, budget-charged as registered. The
QUIC churn quartet and its history-conditioned sibling held TYPESTATE
in four consecutive raters — a second consecutive rater pair. The v6 shares (a fourth
version-labeled series, never mixed): iCalendar 88.9%/88.9%, TLS
81.4%/81.9% — inside the closed v3 band — QUIC 65.1%/65.1%. Every v6
share sits at or below its v5 counterpart; the error-sign sheet's one
conviction points against the thesis. The cycle statement §6.2 closed
now has its next turn: the amendment an upheld verdict demanded was
cut, pre-registered, and graded — and the corpus that convicted the
instrument returned its cleanest sheet in the series, at the
strictest tolerance the series has ever registered, while the same
machinery kept enough teeth to convict the author's calibration one
corpus over.

### 6.4 The panel widens: a second cross-family replication

The first replication (§6) had excluded a third foreign family with a
recorded reason — the serving subscription exposed only a flash-tier
Gemini, and a weaker-tier rater confounds capability with prior
divergence. On 2026-08-16 that reason measurably vanished (a pro-tier
Gemini appeared in the transport's model list), and a second
replication was registered the same day (`census/foreign2/`, pushed
before any seated model had seen instrument or corpus): the TLS
corpus, the same frozen v3 pass-4 pack, three new foreign families —
Gemini 3.1 Pro (Google), Kimi K3 (Moonshot), GLM 5.2 (Zhipu) — with
clauses F6–F10 continuing the first replication's namespace, each
clause carrying a mutant-exhibited fail branch and F10's floor set
at the smallest integer every measured fail branch fails,
and a fourth candidate family (Cursor's in-house Composer) excluded
with its own recorded reason: an unattributable base lineage is a
confound for a family-bias measurement.

Four of the five clauses passed in all three raters. The quotients —
78.9%, 78.9%, 77.0% — landed inside the pre-registered 76–86% band,
and the five foreign quotients measured under the frozen instrument
now span 76.5–80.9%,
four of the five below the lowest Claude quotient (79.9%): a
family-level tendency toward slightly lower eliminable shares whose
per-rater mechanism the report decomposes (non-eliminable-ward,
PROCESS/U-dominated, for two
raters; for Kimi, four of its nine departures
from D-eliminable
items are CV *extensions*, a class-boundary reading rather than a
refusal). Agreement did not systematically degrade again:
every one of the ten foreign–foreign pairs sits at 79.9–88.2% raw
(four pairs below the 81–90% intra-family span's floor; none above
its ceiling),
and the existential band-reach clause — at least ONE of three
families reaching the intra-family edge against rater D — passed
universally (175, 184, 170 of 204), the second
replication in which the author's pre-registered degradation model
proved too pessimistic. The CV core went six-for-six in all three
raters — fifteen raters across six model families had then kept all
six (B's by inference, limitation 7; seventeen since, §6.5), with
the *penumbra*
reproducing too: Kimi's four CV extensions
{111, 181, 199, 203} are exactly the GPT rater's three plus
Gemini's one, independent lineages extending the class at the same
items and never shrinking it.

The informative result is the clause that failed. F10 asked whether
the first replication's nine-item foreign consensus — the
negotiated-state cluster behind candidate rule 17 — is general:
each new rater was predicted to read at least six of the nine
TYPESTATE. Gemini (7/9) and GLM (7/9) did, with different
departures; **Kimi read eight of the nine DOMAIN**, siding with
rater D's archived reading against the G=X consensus. The failure
grades the author's generality model, per the registration, and the
seat tally is the finding: four of five foreign seats side with the
TYPESTATE consensus, one with D — and D is the Anthropic archive's
own outlier on this cluster (its other archived same-family
readings run 7–9 of 9 TYPESTATE). The rule-17 boundary is real,
contested across seats and within the one archive deep enough to
show internal disagreement, and owned by no side — the docket entry
for any future instrument version inherits that structure. One
transport protocol event (a single item emitted twice with the same
label, deduplicated) is disclosed in the report; no number from
either replication joins any census series.

### 6.5 Two docket edges settled: the v7 amendment and its first pass

The v6 report left two entries for a future version — the
precision-trigger wording its J4 grade owed, and the mode-conditioned
pair's consistent PROCESS-ward reversion. A v7 amendment cut both
(rules 26 and 27), stated plainly at cut: unlike v6, it repairs no
conviction — cut from the v6 pass's two measured docket
edges. Rule 26 narrows rule
25's unit-local list to suppression dispositions (an acceptance duty
with a degradation license is conduct — siding with six of eight
archived readings on the precision item while preserving the validity
half), and rule 27 applies the locality litmus to operating state,
deciding the decline rule 25 had recorded. The registration's audit
fired the amendment's own pre-flagged downgrade — the served text
settles the validity item twice over, so its prediction graded as a
comprehension check — leaving the discriminating load entirely on the
leakage and churn tripwires; the iCal zero bound re-derived (achieved
by three archived raters this time), and the TLS leakage floor moved
one item looser because the archive had grown, not because the
derivation changed.

Six blind passes, zero protocol events, and the sheet splits exactly
along the registered load line. Everything the amendment adjudicated
transmitted in both families: the precision item PROCESS in both
raters (eight of its ten archived readings; only the convicted v5
pair ever read DOMAIN), the validity item DOMAIN in six
consecutive readings since v5, both mode-conditioned items PROCESS in all four
v7 readings (four consecutive each since the wall), the recognition
nine at 18/18. TLS posted the series' first fully clean sheet — in
the corpus that had convicted v6's calibration — with the CV core
reaching seventeen consecutive raters across six families (one by
inference, limitation 7). And the
tripwires convicted the author three ways: the iCal leakage clause
failed in the foreign seat (191 against 193 — the set's two
perennial flicker sites plus its first-ever third leak), the iCal
zero bound convicted both raters on one item each (77 and 79, the
series' perennial U-boundary flickers, neither carrying the new
rules'
vocabulary), and the QUIC churn budget broke in both seats (11 and
15 against 7), the foreign rater moving three history-conditioned
items PROCESS-ward — breaking a four-rater TYPESTATE streak on
exactly the shape rule 27's wall declined to claim, with two
unlicensed thesis-ward departures stated on the error-sign sheet.
The v7 shares (a fifth version-labeled series, never mixed):
iCalendar 88.4%/87.6%, TLS 80.9%/80.9%, QUIC 63.0%/63.3% — every
one at or below its v6 counterpart. The loop's fourth turn reads
cleanly: the adjudications transmit where the rules aim, and the
residual drift lives where it has always lived — on U-boundary,
class-boundary, and
history-conditioned shapes no instrument version has claimed.

### 6.6 The boundary formalized: a locality study over the archive

Finding 1 of the four-pass study said inter-rater agreement is a
per-class property predictable from the rule's shape — directionally,
not as a quantitative law. A locality study (`census/locality/`) made
the direction formal and tested it against the archive with no new
raters. Rule 16's litmus ("could the check be re-run on the lone datum
in a vacuum and get the same answer?") becomes a semantic property: a reading of an obligation
is *datum-local at a granularity* — one handshake message, or one
connection's transcript, matching the census's own two reporting
levels — and the
property is established constructively rather than by judgment:
locality by shipping an executable validator over the modeled datum,
non-locality by shipping a distinguishing pair (one datum, two
spec-admissible contexts, opposite compliance verdicts — a proof,
since any datum-local predicate is constant across the pair). The
registration froze a 44-item set derived mechanically from all
fourteen archived TLS label maps (the 27 items where at least four of
fourteen raters dissent from the modal label, plus a hash-selected
stable sample), seven predictions with floors, and the grader itself,
before any witness existed. The witnesses were then constructed by
the census author, archive-aware — so the graded sheet measures the
internal consistency of one semantic model, and the checkable product
is the artifacts, not the pass-rate.

Every clause passed; the informative cells are the exceptions and the
deviations. The headline correspondence — "some local rung witnessed"
coincides with "eliminable classes hold the vote majority" — held on
every item except the four the registration named in advance (75,
111, 164, 188: real local components under non-eliminable-majority
labels, a secrets-bound constraint under an eliminable one, a
provenance fight over a message-local check). The contested mass
split into two kinds the class vocabulary cannot distinguish:
one-rung vocabulary fights (the downgrade-sentinel family, where the
"negotiated version" guard is encoded in the ServerHello itself, so
DOMAIN and TYPESTATE voters were labeling the same information) and
genuine two-rung ambiguities (guards living in another message).
CRYPTO-VERIFY — its core items unanimous across all seventeen
raters — split three ways under the lens: signature verification is
transcript-computable (the verification key is in the Certificate
message), Finished verification under (EC)DHE is
information-determined by the transcript but not efficiently
computable from it, and PSK-keyed checks are not even
information-local — decision rule 2's "the secret is the
discriminator," now with witnesses attached. Two registered
single-rung predictions failed, both the same shape — the sentence
hides a context dependency ("compatible," decidable only against the
ticket's issuing connection; "which also support TLS 1.2") — and one
failure arrived as a refutation: the gate's cold reviewer constructed
the distinguishing pair the author's recorded FAILS entry claimed
could not exist — before any witness was pushed — the
reader-challenge mechanism the registration names firing on its first
outing and withdrawing the record in place. The study's numbers join no census series; its bearing on the
shared-prior caveat is stated in limitation 6.

### 6.7 The criterion generalizes: second locality passes over iCalendar and QUIC

One corpus is one point, so a second registration
(`census/locality2/`) ran the same criterion — same witness forms,
same lemma, granularities instantiated per genre (one content line /
one iCalendar object; one UDP datagram / one connection) — over the
two remaining boundary masses: 23 iCalendar items from all ten
archived maps (the corpus's entire 14-item multi-rater dissent mass,
plus a hash-selected stable sample) and 49 QUIC items from all twelve
(the 31 most-contested items with the dropped tiers enumerated, plus
a stable sample), with the item sets, per-item predictions,
per-family correspondence floors, and grader frozen before
construction. Every clause passed; 71 of 72 item outcomes matched
their registered predictions exactly; and the registration's central
structural bet — that where the formal property and the archive's
eliminable-vote boundary diverge, they diverge along nameable,
class-shaped families rather than item noise — realized all 22
pre-named exceptions with zero unnamed, which across the three
corpora now stands at 26 pre-named divergences, none unnamed, over
116 witnessed items.

The QUIC bend is systematic in both directions and both directions
are now witnessed. The headline boundary UNDERCOUNTS locality on the
THRESHOLD family with connection-carried quantities and bounds —
sixteen items: the thirteen-item limit cluster, QUIC's largest
disagreement cluster, era-split at rule 16's v4 arrival (all four
v3-era raters TYPESTATE throughout; seven of eight later raters
THRESHOLD on twelve of the thirteen), plus three THRESHOLD-unanimous
stable samples — so the cluster's THRESHOLD-vs-TYPESTATE fight is a
vocabulary fight over a one-rung check the eliminable line cannot
see. And it OVERCOUNTS on state
that crosses the connection: item 58, TYPESTATE-unanimous across all
twelve raters, came out with an EMPTY witnessed outcome — the
registration's boldest single prediction — because "the remembered
values of the parameters" live in a prior connection, where the
census's transcript unit tops out; 0-RTT parameter consistency is
exactly the state a resumption-aware type discipline could carry and
a per-connection transcript cannot witness. On the format side, the
iCalendar DOMAIN monolith split into line-local and object-only
checks, and its three exceptions {62, 77, 79} are all one shape —
datum-local TRIGGER, conduct- or world-guarded COMPLIANCE — the
structure rule 25 turned into its litmus, carried here by shipped
pairs instead of votes. A designed control sharpened the point:
items 43 and 79 are byte-identical corpus sentences whose
eliminable-vote counts straddle the majority line, so the
correspondence mismatch had to land on exactly one of them, and it
landed where registered — the archive's headline boundary carries
position noise that no sentence-level semantic property can track.
The per-era breakdown adds a third geometry: the iCalendar
ignore/accept conduct quintet's DOMAIN votes ({13, 91, 146, 150,
210}) are exactly the two raters of the convicted v5 instrument —
the criterion sides with the other eight against precisely the
mis-designed era — while exception item 62's DOMAIN votes survived
the repair (v5, v6, and v7 alike), making it a standing boundary,
not an instrument artifact; and item 185's dissent splits by SEAT
(all four X-seat raters of the v4-through-v7 eras against every
Claude-family seat plus Xi), where the criterion's answer is that
both seats hold one rung each of a genuinely two-rung sentence. The
challenge interface fired again: the gate's reviewer refuted the
author's recorded impossibility claim for item 235 by constructing
the packet-level validator it denied — the second refuted FAILS
record in as many studies, both pre-push, and the sole exact-sheet
miss. These passes' numbers join no census series.

## 7. Related work

FSM-*extraction* from RFCs is a mature genre — RFCNLP / attack synthesis
(IEEE S&P 2022, arXiv:2202.09470), PROSPER (HotNets 2023), FlowFSM, LLM-ensemble
extraction for 3GPP specs (arXiv:2510.14348) — and RFC 2119 modality tagging
exists in requirements engineering. These classify by modality or extract
transitions for fuzzing; none measures an enforceability-class mix of an
obligation set. The taxonomy itself must be positioned against: Gao, Bird &
Barr (ICSE 2017) for the "types catch 15% of bugs" line and its survivorship
caveat; Chillarege et al.'s Orthogonal Defect Classification (IEEE TSE 1992;
triggers 1995), which owns "the observed distribution is a function of the
observation point" on the process-phase axis where we work on the
declaration-layer axis; Tsipenyuk, Chess & McGraw's Seven Pernicious
Kingdoms (2005), where three of our four base classes have 2005 ancestors
(Input Validation ≈ DOMAIN, API Abuse ≈ TYPESTATE, Time and State ≈
REVOCABLE) — THRESHOLD appears new because defect taxonomies classify bugs,
not monitors; and Dwyer, Avrunin & Corbett (ICSE 1999) as the methodological
precedent for classifying a specification corpus into a small scheme and
reporting the mix. Prior-art sweeps at each census (PromQL, TLS) found no
comparable predicate-shape census; that null is one sweep deep per corpus,
not a proof of novelty.

## 8. Limitations

1. **Declared obligations only.** Undeclared obligations are invisible here
   by construction — and we have not measured what fraction of any
   boundary's real obligations get declared, so no claim about that
   fraction appears in this paper.
2. **Shape-eliminability, not engineering-eliminability.** "Type-eliminable
   in shape" claims a discharging type *exists*, not that deploying it is
   practical; the versioned-enum limit shows even DOMAIN has deployment
   bounds.
3. **One span per document; six spans under one instrument.** Wayland
   is one protocol; TLS 1.3 §4, RFC 9420 §5–§15, RFC 9000 §2–§19,
   RFC 9001 §4–§8, RFC 9002 §5–§7, and RFC 5545 §3 are each one span of
   one RFC. Six
   frozen-instrument spans (three protocols — one a complete
   document family — and a data format) support "consistent with a
   spectrum" and the
   family-scoped role observation — not a distribution and not a
   mechanism. The spans cover their documents unequally: MLS ~92%
   (132/144 MUST/SHALL-bearing lines), QUIC transport ~94% (280/298),
   RFC 9002 ~97% (33/34), RFC 9001 ~86% (70/81), iCalendar §3 ~95%
   (233/246), TLS §4 ~66% (217/330) —
   RFC 8446 states key-schedule and record-layer procedure as MUSTs
   *outside* its censused span — so every comparison is between censused
   surfaces, not whole protocols (the QUIC family, taken together, is
   the one near-whole-protocol view, and its pooled figure carries its
   own caveat in the synthesis).
4. **Sentence-level extraction.** Compound sentences count once; n = 204,
   127, 281, 69, 30, and 225 are sentence counts, not obligation counts;
   SHOULD-level text is absent by design. The iCalendar corpus adds the
   inverse defect: 14 sentence texts recur verbatim (48 surplus items)
   with different referents, so identical-text items carry distinct
   obligations — both arithmetics (per-item and unique-text) are quoted
   in that census. The MLS census surfaced this limit's sharpest
   form: one corpus sentence carries an antecedent-less "it", and the
   author-rater resolved it from the RFC source — an instrument
   deviation, since the pack says classify on the sentence's own text,
   counted against transfer in the census — while the compliant blind
   rater could not (event E1) — sentence granularity can sever a
   predicate from the noun it constrains.
5. **Item-level labels carry a measured error bar** (§6): raw inter-rater
   agreement 81–90% on TLS (MLS: 85.0% and QUIC: 85.1%, inside that band;
   RFC 9001: 76.8%, BELOW it; RFC 9002: 96.7%, above it — §6 and §4.7
   carry both stories; under the repaired v4 instrument the four
   re-rated spans pair at TLS 92.2%, MLS 88.2%, QUIC 84.0%, RFC 9001
   94.2% — the error bar moves with the instrument version, though the
   v4 pairs also swap the author rater for a fresh instance, two
   variables at once; §6.1; the iCalendar pair, v3 instrument with
   later rater models, sits at 97.3% — §4.8; the v5-series pairs at
   QUIC 89.7%, TLS 93.6%, RFC 9001 95.7%, iCalendar 96.9% — §6.2;
   the v6-series pairs at iCalendar 98.7%, TLS 93.1%, QUIC 89.3% —
   §6.3; the v7-series pairs at iCalendar 97.8%, TLS 92.2%, QUIC
   86.5% — §6.5;
   the two-variables caveat against the v3 pairs applies except on
   iCalendar, whose v3 pair already used these rater models), 15 TLS items
   with fresh-rater consensus against the original labels, guard-boundary
   judgments that flip between competent raters. Every headline in this paper is quoted at the granularity that
   survives that error bar.
6. **Rater population.** All raters are LLM agents. Raters B–D (TLS),
   B′ (MLS), B″ (QUIC), B‴ (RFC 9001), and B₁⁗/B₂⁗ (RFC 9002) are fresh
   same-family instances, and raters G and X (TLS cross-family
   replication, §6) fresh foreign-family instances — as are the v4
   passes' eight raters (§6.1): per corpus, one fresh same-family
   instance and one fresh foreign-family (Grok) instance, no author
   rater among them — given only their
   instrument and the corpus — blind to the
   other raters, the tallies, and the authors' expectations; raters A
   (TLS), A′ (MLS), A″ (QUIC), and A‴ (RFC 9001) are the census author
   and are *not* blind to authorial context (the 15-item consensus
   finding and MLS event E1 are the measured consequences). The
   iCalendar census (§4.8) has no author rater — a fresh same-family
   rater Ai and a foreign rater Xi, and it is the first census to
   pre-register its full rater roster including the same-family model
   name (earlier protocols pre-named only the foreign models), making
   the rater-model confound on cross-census comparisons explicit rather
   than silent; the v5 passes' eight raters (§6.2) — per corpus one
   fresh same-family instance and one foreign instance, no author
   rater — continue that discipline, which v5's rule 24 makes
   mandatory for every future registration, as do the v6 pass's six
   raters (§6.3), the second replication's three fresh foreign
   instances, one per new family (§6.4), and the v7 pass's six
   (§6.5). RFC 9002 has
   NO author rater — its intended author pass was abandoned after the
   author saw the first blind rater's labels (deviation disclosed in its
   report) — so its two raters are both blind same-family instances and
   its 96.7% agreement carries the shared-prior caveat undiluted. The
   monoculture risk splits in two, and the halves now differ in status.
   The *family-bias* half — every rater from one vendor's lineage — was
   measured and weakened by the cross-family replication
   (`census/foreign/`, §6): raters G (GPT-5.6 Sol) and X (Grok 4.6),
   blind under the frozen instrument, landed at 76.5%/80.9% eliminable
   with agreement that did not systematically degrade (X above the
   intra-family ranges; G at or just below the raw floor) and every
   CV-set item keeping its CV label in both — then further weakened
   by the second replication (`census/foreign2/`, §6.4): Gemini 3.1
   Pro, Kimi K3, and GLM 5.2, three more lineages, landed at
   77.0–78.9% inside the pre-registered band with all ten
   foreign–foreign pairs at 79.9–88.2% raw and the CV core
   fifteen-for-fifteen across six families, seventeen since the v7
   pass (§6.5; one nine-item cluster
   reads seat-dependently — §6.4). The *corpus-shared-prior* half — every frontier LLM
   trained on these RFCs and on prose about them — is unaddressable by
   any LLM replication from any family: a shared reading learned from the
   corpus would reproduce these same agreements. That unaddressability
   is now measured rather than argued: a registered obfuscation probe
   (`census/obfuscation/` — a probe of this caveat's memorization
   component, not a census; its
   numbers join no series) reversibly nonce-substituted the iCalendar
   corpus's memorizable identity — 90 tokens (the scheduling-domain
   nouns among them) and both extension stems — and its pre-committed
   manipulation check
   FAILED in both arms: fresh agents identified RFC 5545 from what
   obfuscation left (among it the content-line grammar, the recurrence
   architecture, the constraint shapes, the leap-second and escaping
   rules, and the retained sibling-citation set) at 95% and 98% stated
   confidence. By the registration's own downgrade clause that
   identification re-admits memorized readings for the graded cells
   that followed — both blind raters under the frozen v6 pack matched
   the v6 pair's original-corpus labels at 224/225 each and paired at
   222/225, so identifier removal cost approximately nothing, but
   under an
   identified corpus that stability cannot be credited to shape
   alone. The probe's measured lesson is this caveat's: a
   specification's identity survives lexical obfuscation in its
   structure and disclosed residuals, so no LLM-side design isolates
   the memorization
   channel. Only a non-LLM rater
   reaches it; the parked human replication is that non-LLM probe —
   its sole-route status now measured rather than argued — and it has
   not been run. The v4, iCalendar, and v5 passes, LLM raters all, inherit
   this caveat whole — including their record agreements (§6.1, §4.8,
   §6.2), and the v6 pass (§6.3) inherits it at full force: the
   higher the agreement, the harder this caveat bites, and the v6
   pair's 98.7% record carries it undiluted. Shared priors remain a residual
   common-cause risk that blindness does not remove. One study bears
   on this caveat from a third direction (§6.6, `census/locality/`):
   over a registered 44-item set, the archive's agreement boundary
   coincided — with four pre-named exceptions — with an independently
   checkable semantic property (datum-locality, established by
   executable witnesses and distinguishing pairs rather than by rater
   judgment). A prior shared only as corpus memorization would have no
   particular reason to align with witness-constructibility, so the
   measured correspondence is evidence that the agreement tracks a
   semantic joint in the specification language; but the witnesses
   were constructed by the census author with the archive in view, and
   a prior shared at the level of the property itself — author and
   raters trained on the same semantics conventions — is not excluded.
   The second passes (§6.7, `census/locality2/`) widen that evidence
   without changing its ceiling: the same class-shaped exception
   pattern reproduced in two unrelated genres under per-genre
   granularities, which a merely lexical prior has still less reason
   to produce — but the author-constructed caveat applies to them
   identically. The correspondence narrows this caveat from a new
   side; only the human pass closes any part of it.
7. **Rater B's full label map was never archived.** Only B's 16 recorded
   disagreement labels survive (plus agreement on the other 184); B's
   figures — including the 79.9% floor of the headline range — are
   arithmetically consistent with the recorded labels but not
   item-recomputable for four items. A provenance defect, recorded rather
   than repaired.

## 9. Conclusion

Eight corpora, one codebook: a monitoring rule base that is three-quarters
policy thresholds and structurally cannot contain typestate; a windowing
protocol whose client-facing declared errors are 87.6% type-eliminable in
shape; a cryptographic handshake whose normative surface is 80–83%
type-eliminable, with a secret-dependent core of 2.9% that every
same-family rater's recorded labels agree on item-for-item (all nine
foreign raters ever run on that corpus kept the six CV items —
seventeen raters in all, across six model families; one foreign rater
extends the class by three, another by exactly those three plus the
one a third adds, and the v5 same-family rater by one,
torn; both v6 raters and both v7 raters kept exactly the six — §6,
§6.1, §6.2, §6.3,
§6.4, §6.5); a cryptographic group protocol at
≈57%; a transport protocol at ≈67–69%; that transport protocol's two
sibling documents at 54–67% and 23.3%; and a calendar data format at
88.0–88.4% — above every frozen-instrument protocol span, its
ordering class all but empty (§4.8) — six spans rated under the TLS
study's frozen instrument (which also supplied TLS's own final rater),
and the TLS span additionally re-rated by five foreign model
families across two replications
with no systematic degradation in agreement (§6, §6.4). The instrument's
measured edges were then repaired as v4 and graded under
pre-registration (§6.1): the repair transmitted best exactly where its
new discriminator was crispest (RFC 9001, 76.8% → 94.2% cross-family,
with limitation 5's rater-composition caveat) and appeared to cost agreement where
its vocabulary overreached (QUIC, 85.1% → 84.0% — since decomposed
into a roster effect and an instrument recovery, §6.1), with every v3
number
ring-fenced and the v4 shares a separate, version-labeled series.
A v5 cut from that grading record then graded clean on every named
prediction while the machinery it introduced caught its own
undisclosed reach on the format genre — the pre-committed mis-design
verdict, delivered by the instrument against its author (§6.2) — and
reversed the v4 churn it had explicitly declined to decide (the
reversal consistent-with, not established — §6.2): the loop a
versioned instrument exists to close, closed twice in one release,
once in each direction. The v6 amendment cut from that verdict then
answered it (§6.3): the convicted corpus passed every registered
clause at a zero-departure budget with the repository's record
agreement, one adjudication half failed to transmit in both raters —
mapping a validity-versus-precision boundary sharper than the rule
that drew it — and the no-regression machinery convicted the
author's churn calibration on a neighboring corpus. The v7 amendment
then settled both of that pass's docket edges (§6.5): the settled
adjudications transmitted in both families, the convicting corpus
posted the series' first fully clean sheet — and the tripwires
convicted the author's calibration again, on the shapes no version
has claimed; the loop's fourth
full turn, each closed by machinery written before its evidence.
We still resist summing these into one cross-corpus law: the first three
corpora were classified by different methods (rule 8 makes such
comparisons artifacts until re-run under one method), and the codebook's
own retraction records what happened the last time a cross-layer pattern
was read into this data (§4.9). The frozen-instrument set is the one
exception — same instrument, same recipe up to disclosed mechanical
refinements (two shared by the protocol spans; three genre-specific
ones for the paginated data-format corpus, §4.8) — and what it
licenses is a description, not a law: the
results are consistent with a spectrum of type-eliminable shares, each
span's position explainable post hoc by *what that span of the
specification chooses to state as obligations* — not a property of
"security protocols" as a kind, and not yet an established mechanism
(the author's pre-registered directional models keep partly failing:
QUIC's "nearer TLS" missed, all five predictions about RFC 9001
failed, and the iCalendar band missed the foreign rater by one item —
§4.8). The QUIC document family (§4.7) is the reading's sharpest
support: one protocol, one era, and the share spans 23%→69% with the
document's role the salient varying factor (rater pairs, spans, and n
vary too — the synthesis carries the caveat). Each number stands alone, named with its corpus and its
censoring. What can be said of the protocol corpora separately:
Wayland's and TLS's declared obligations are dominated by state-machine
and format discipline — the kind of thing types discharge — with a
small, precisely nameable type-resistant residue; the MLS span shows
that a normative surface which writes its procedural hygiene into MUSTs
pulls that dominance down to ≈57%; QUIC shows a state-machine-dense span
holding the middle while its crypto and recovery live censored in
sibling documents whose own shells measure 54–67% and 23.3%. And the
one non-protocol span shows what a span with no stated counterparty
duties looks like — part genre, part document boundary, per its census:
ordering obligations all but vanish, and the mix is ~87% single-value
format discipline — with the genre's own censoring (grammar-stated
obligations, a sibling scheduling protocol) pre-registered beside the
number (§4.8).

The method is the other half. Every headline here survived, or was produced
by, a failure: a retracted cross-layer claim, an invalidated rating pass, a
repair loop halted on its pre-registered interpretation, an amendment
whose count-bound no-regression clause failed in all eight of its own
grades — partly zero-tolerance arithmetic, partly rules that repaired
more than their author predicted. What made those failures
productive rather than embarrassing was mechanical: classify on predicates,
make disagreement loud, commit predictions before evidence, and treat "the
instrument does not transmit" as a result. A codebook, like a protocol, is
a boundary — and the same lesson applies at both: what you do not declare
crisply, you will re-litigate at runtime.

## Appendix: artifact map

| artifact | contents |
|---|---|
| `codebook/classes.md` | taxonomy, honesty rules 1–27, retraction + addendum, v2/v3/v4/v5/v6/v7 amendments (v4 carries pre-registered predictions V1–V8; v5 carries Z1–Z7; v6 carries J1–J6; v7 carries L1–L7), graduation record |
| `codebook/rater-pack.md` | the verbatim v3 rating instrument (pass-4 instrument = blob `a08febba…`; later reformatted for rendering, rule content unchanged) |
| `codebook/rater-pack-v4.md` | the verbatim v4 rating instrument (blob `4891605…` — v3 pack + rules 15–19, one disclosed elision) |
| `census/promql/promql-classifier.py` | n=1155 classifier, rule-9 hardened |
| `census/wayland/{wayland-classifier.py, extract-corpus.py}` | n=172/216 classifier + from-source corpus regeneration |
| `census/wayland/cv-neg-falsifiability.md` | the graduation falsifiability check (0/216, 0/216) |
| `census/tls13/tls13-alert-census.md` | 30-minute alert probe (n=25) — forced CV/NEG, granularity warning |
| `census/tls13/{rfc8446-s4-census.md, rfc8446_s4_musts.txt}` | the n=204 census, corpus, two-rater analysis, close-out |
| `census/tls13/rfc8446-s4-pass{3,4}.md` | the transmissibility study: failed pass + archived labels, stop verdict |
| `census/mls/{README.md, rfc9420_s5-15_musts.txt, extract-corpus.py}` | MLS corpus (n=127), shipped extractor, publicly pre-timestamped predictions M1–M5 |
| `census/mls/rfc9420-census.md` | the matched-method MLS census: two raters, archived labels, prediction grades, candidate rule 15 |
| `census/quic/{README.md, rfc9000_s2-19_musts.txt}` | QUIC corpus (n=281, ~94% doc coverage), publicly pre-timestamped predictions Q1–Q5 |
| `census/quic/rfc9000-census.md` | the QUIC census: two raters, archived labels, prediction grades, rule-16 candidate + deadline-duty edge |
| `census/quic-tls/`, `census/quic-recovery/` | the family completion: frozen corpora (n=69, n=30), pre-timestamped predictions K1–K5/R1–R5, both census reports with archived labels |
| `census/quic-family.md` | the three-document synthesis: role tracks the mix 23→69%; pooled ≈61–65% with its caveat |
| `census/foreign/` | cross-family replication of the TLS corpus: pre-timestamped predictions F1–F5, report with both foreign raters' archived labels, candidate rule 17 |
| `census/ical/` | the non-protocol corpus (RFC 5545 §3, n=225): pre-registration with nine-candidate selection table, three genre refinements + shipped depaginator/extractor, frozen corpus, pre-timestamped predictions N1–N6 with pre-registered rater models, census report with both raters' archived labels |
| `census/v4-tls/` | first pass under instrument v4: pre-pass protocol with worked-example settlements, two blind raters (one per family) over the TLS corpus, archived labels, grades of V4/V6/V7/V8 |
| `census/v4-completion/` | v4 completion: pre-pass protocol, six blind passes over MLS/QUIC/RFC 9001, archived labels, grades of V1–V3/V5–V7 |
| `codebook/rater-pack-v5.md` | the verbatim v5 rating instrument (blob `694e3a9…` — v4 pack + pipeline and rules 20–22, two disclosed elisions) |
| `census/v4-ical/` | the v4 null test on the iCalendar corpus: pre-pass protocol W1–W5, two blind raters, archived labels — rules 16/18/19 inert where their boundaries do not occur |
| `census/quic-replication/` | QUIC under v3 with the new roster-shape: protocol Y1–Y6, archived labels, the four-rater boundary table, the instrument×roster grid decomposition |
| `census/v5-quic/` | first v5 pass: registration with mechanical rule-24 audits and rule-23 floors of measured failability, two blind raters, archived labels, grades of Z1/Z4-QUIC/Z6/Z7 |
| `census/v5-completion/` | v5 completion over TLS/RFC 9001/iCal: registration with the three-way steer taxonomy, six blind passes, archived labels, grades of Z2/Z3/Z5/Z4-overall and the iCalendar mis-design verdict |
| `codebook/rater-pack-v6.md` | the verbatim v6 rating instrument (blob `f4f9e0b…` — v5 pack + rule 25, seven disclosed elisions) |
| `census/v6-pass/` | first v6 pass over iCal/TLS/QUIC: registration with the verbatim trigger-(c) ruling and the zero-departure iCalendar bound, six blind passes, archived labels, grades of J1–J6 and rule 23 per corpus — the zero-departure conviction-corpus sheet, the 98.7% record pair, and the two standing failures |
| `census/obfuscation/` | registered probe of limitation 6's memorization component: seeded reversible obfuscation of the iCalendar corpus (shipped script + full map), two-arm manipulation check FAILED — RFC 5545 identified at 95/98% from what obfuscation left — clauses O2–O4 with both raters' archived labels — the measurement behind limitation 6's only-a-non-LLM-rater sentence |
| `census/foreign2/` | second cross-family replication of the TLS corpus (three new families: Gemini 3.1 Pro, Kimi K3, GLM 5.2): registration F6–F10 with mutant-exhibited fail branches, shipped scorer, three blind passes with archived labels — F6–F9 pass ×3, F10's informative failure (the rule-17 cluster is seat-dependent; the Claude anchor is its own family's outlier) |
| `codebook/rater-pack-v7.md` | the verbatim v7 rating instrument (blob `a6f4321…` — v6 pack + rules 26–27, three disclosed elisions) |
| `census/v7-pass/` | first v7 pass over iCal/TLS/QUIC: registration with the fired L2 downgrade and the re-derived zero bound, shipped scorer with 24-cell KAT, six blind passes, archived labels, grades of L1–L7 and rule 23 per corpus — both adjudications transmit, TLS's first fully clean sheet, and the three calibration convictions |
| `census/locality/` | the locality study (§6.6): pre-registered formalization of rule 16's litmus as datum-locality at message/transcript granularity, the distinguishing-pair lemma, a 14-map agreement profiler with 19 known-answer tests, grader shipped before construction, 56 witness artifacts + 17 recorded construction failures — the four named exceptions realized exactly, two prediction failures of one shape, one FAILS record refuted and withdrawn at the gate |
| `census/locality2/` | the second locality passes (§6.7): one registration over both remaining archives (iCalendar 23 items from ten maps, QUIC 49 from twelve; 37 known-answer tests), per-genre granularities (prop/object, pkt/conn), per-family correspondence floors, FAILS coverage enforced by the frozen grader, 77 witness artifacts + 24 standing construction-failure records — 71/72 exact outcomes, all 22 pre-named exceptions realized with zero unnamed, the predicted-EMPTY outcome for QUIC 58 realized, and a second FAILS record (235-pkt) refuted at the gate by a reviewer-constructed validator, withdrawn in place |
