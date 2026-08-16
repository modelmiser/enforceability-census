# A Census of Enforceability: Measuring What Fraction of Stated Runtime Obligations a Type System Could Discharge

**Repo-native paper · 2026-08-13, extended 2026-08-14 (v4 series, §6.1) and 2026-08-15 (the non-protocol corpus, §4.8) · artifact of record: this repository.**
No venue submission is planned; the repository, its commit history, and the
census artifacts it cites are the citable object.

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
172 declared; classifier vocabulary fitted to that corpus — §4.2); and the
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
and 4 items, and cross-family raw agreement of 97.3%, the repository's
highest; the author's pre-registered band missed the foreign rater by
exactly one item, and the genre's censoring (a sibling scheduling
protocol; obligations stated as grammar rather than MUSTs) is
pre-registered in the census. A cross-family
replication (§6) re-rated the TLS corpus blind under the same frozen
instrument with two foreign frontier model families: the author's
pre-registered degradation model failed — one foreign rater agreed with a
Claude rater *above* the intra-family agreement ranges, and all six
core-CV sentences kept their CV label under every rater ever recorded —
weakening the family-bias half of the rater-monoculture caveat while
leaving its corpus-shared-prior half untouched (limitation 6). The
instrument itself was then repaired under pre-registration and the
repair graded (§6.1): a v4 amendment wrote five rules at the series'
measured edges, with itemized predictions V1–V8 committed before any v4
rater existed and every v3 number ring-fenced. Eight blind rating
passes — a same-family and a foreign rater per corpus — graded them
all: the key-lifecycle repair took RFC 9001, the band-breaking corpus,
to the series' best cross-family agreement (94.2%, from 76.8%); TLS's
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
QUIC's agreement declined (84.0% vs 85.1%) — v4's measured cost,
reported next to its gains. All v4 shares are a new, version-labeled series
(TLS lands at 81.9%/82.8%, inside the closed v3 band); the v3
headlines stand unchanged. The numbers are the smaller half of the
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
  after the five frozen-instrument censuses and the foreign replication,
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
the frozen instrument — the cross-family replication, §6 — and again by
two blind raters under the repaired v4 instrument, §6.1.)

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
frozen-instrument protocol span — with raw agreement 97.3%, the
highest between any two raters in
this repository (cross-family, n = 225; the prior record was 96.7% on
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
   that corpus (RFC 9002's 96.7% on its 30-item corpus was then the
   repository-wide record — since surpassed by the iCalendar pair's
   97.3%, §4.8). MLS rose to 88.2% (v3: 85.0%). And both v4 TLS
   raters kept the CV class at exactly the same six items — the six CV
   items have now drawn CV labels from eight TLS raters, exactly six in
   seven of them (G extends the class by three, §6; B's exactness by
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
   stand, and a v5 owes a per-item-scoped no-regression clause.
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
   sits below the v3 pair (85.1%) — the only corpus where v4 agreement
   is not the best on record — with churn concentrated on the PROCESS
   boundary: rule 18's lifecycle vocabulary appears to pull procedure
   readings beyond key/phase contexts, and the same-family v4 share
   (63.7%) fell below the v3 band. An instrument version now has its
   gains and its price as numbers, side by side.

The v4 shares (new series, never mixed with v3): TLS 81.9%/82.8% —
inside the closed v3 band, one rater at its exact upper endpoint; MLS
59.1% in both raters; QUIC 63.7%/68.7%; RFC 9001 60.9%/58.0%. The
spectrum's shape is unchanged. Two items the amendment carved out
without prediction (QUIC 63 and RFC 9001 item 15) split between the v4
raters and remain unruled.

One later data point joins the transmissibility record: the iCalendar
census (§4.8), run after this cycle under the frozen v3 instrument,
paired an ~87%-DOMAIN corpus with the repository's highest raw
agreement (97.3%, cross-family) — the crisp-discriminator law's
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
   later rater models, sits at 97.3% — §4.8), 15 TLS items
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
   than silent. RFC 9002 has
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
   CV-set item keeping its CV label in both. The *corpus-shared-prior* half — every frontier LLM
   trained on these RFCs and on prose about them — is unaddressable by
   any LLM replication from any family: a shared reading learned from the
   corpus would reproduce these same agreements. Only a non-LLM rater
   reaches it; the parked human replication is that probe, and it has not
   been run. The v4 and iCalendar passes, LLM raters all, inherit this
   caveat whole — including their record agreements (§6.1, §4.8). Shared priors remain a residual common-cause risk that
   blindness does not remove.
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
same-family rater's recorded labels agree on item-for-item (all three
foreign raters ever run on that corpus kept the six CV items; one
extends the class by
three — §6, §6.1); a cryptographic group protocol at
≈57%; a transport protocol at ≈67–69%; that transport protocol's two
sibling documents at 54–67% and 23.3%; and a calendar data format at
88.0–88.4% — above every frozen-instrument protocol span, its
ordering class all but empty (§4.8) — six spans rated under the TLS
study's frozen instrument (which also supplied TLS's own final rater),
and the TLS span additionally re-rated by two foreign model families
with no systematic degradation in agreement (§6). The instrument's
measured edges were then repaired as v4 and graded under
pre-registration (§6.1): the repair transmitted best exactly where its
new discriminator was crispest (RFC 9001, 76.8% → 94.2% cross-family,
with limitation 5's rater-composition caveat) and cost agreement where
its vocabulary overreached (QUIC, 85.1% → 84.0%), with every v3 number
ring-fenced and the v4 shares a separate, version-labeled series.
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
| `codebook/classes.md` | taxonomy, honesty rules 1–19, retraction + addendum, v2/v3/v4 amendments (v4 carries pre-registered predictions V1–V8), graduation record |
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
