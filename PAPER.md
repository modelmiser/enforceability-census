# A Census of Enforceability: Measuring What Fraction of Stated Runtime Obligations a Type System Could Discharge

**Repo-native paper · 2026-08-13 · artifact of record: this repository.**
No venue submission is planned; the repository, its commit history, and the
census artifacts it cites are the citable object.

## Abstract

Debates about how much verification "could catch" are usually conducted by
example. We measure instead: classify every stated runtime obligation in a
corpus by the **shape of its predicate** into a small set of enforceability
classes — those a type system could discharge (DOMAIN, TYPESTATE) and those
it cannot even in principle (THRESHOLD, REVOCABLE), plus classes forced by
cryptographic protocols (CRYPTO-VERIFY, NEGOTIATION) — and report the mix.
Across three corpora from three different layers we find: a monitoring-layer
corpus (1,155 Prometheus alert rules) is 78% threshold and structurally
incapable of expressing typestate; Wayland's declared protocol errors are
87.6% type-eliminable in shape (149 of the 170 client-facing errors among
172 declared); and the normative surface of RFC 8446 §4 (TLS 1.3 handshake,
204 MUST/SHALL sentences) is **80–83% type-eliminable** (three-rater range),
with a secret-dependent cryptographic core of **exactly 6/204 (2.9%) — the
same six sentences for every rater**. The numbers are the smaller half of the
contribution. The larger half is the method that survived its own failures:
classify on the predicate and never the name (a name-based pass produced a
publishable-looking headline that was retracted the day it was written);
make the classifier report a DISAGREE bucket so it can catch its own
violations; pre-register codebook amendments and their predictions before
each re-rating pass; and stop when the pre-registered criterion says stop.
A four-pass inter-rater study conducted this way — all raters LLM agents,
blind to each other and to the tallies — yields a finding we did not plan:
**classes transmit between raters only as well as their discriminators are
crisp.** The classes with mechanical discriminators showed zero or
near-zero rater variance across four passes (CRYPTO-VERIFY and META:
identical for every rater; THRESHOLD/REVOCABLE: one recorded flip on one
item by one rater), while every residual disagreement sits on boundaries
whose rules require judgment.

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
never declared — and where obligations are never declared they are never
checked, resurfacing downstream as residue nobody can explain — and each
corpus censors classes its language cannot express (§4.1). We report what
specifications say, not what software does.

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
the classes predict zero members in a non-cryptographic, non-negotiated
protocol — confirmed at CV = 0/216 and NEG = 0/216 on a from-source
regeneration of the Wayland corpus
([`census/wayland/cv-neg-falsifiability.md`](census/wayland/cv-neg-falsifiability.md));
note the check's scan is a vocabulary net whose hits were hand-adjudicated,
so it bounds false positives tightly and false negatives only via the
earlier fully hand-classified 172-item census surfacing no such predicates.
**The second ground — rater stability (§6) — was articulated at graduation
time, not pre-registered**: strong for CV (the same six items for every
rater in four passes), thinner for NEG (2–3 items across valid raters, with
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
  [`codebook/rater-pack.md`](codebook/rater-pack.md) byte-identical; each
  pass report records the pack's git blob hash. §6 is the existence proof
  that a paraphrase of a definition is a different definition.

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
boundaries." Two bounds on the claim, both from the data: the
versioned-enum limit (§2), and declaration is not universal even here — 20
of 53 extensions declare no errors at all. A regenerated superset corpus (216 errors, 2026-08-13 HEAD)
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
hand-classified on sentence predicate shape
([`census/tls13/rfc8446-s4-census.md`](census/tls13/rfc8446-s4-census.md)).
Rater A: 94 TYPESTATE (46.1%), 73 DOMAIN (35.8%), 15 PROCESS, 6
CRYPTO-VERIFY, 6 UNCLASSIFIED-unverifiable, 3 NEGOTIATION, 2 each
REVOCABLE/THRESHOLD/POLICY, 1 META.

**Headline: 80–83% of the section's normative surface is type-eliminable in
shape** — precisely, the range across three valid raters is 79.9% (B) to
82.8% (D), with A at 81.9% (§6). The secret-dependent core is **6/204 =
2.9%, identical items for every rater**. Everything types cannot even in
principle express — CV + REVOCABLE + THRESHOLD + NEG — is ~6% (5.9–6.4%
across raters).

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

### 4.5 What does *not* survive across corpora

An early cross-layer claim — "the class mix is a property of the layer" —
was **retracted the day it was written** and the retraction is preserved in
full in the codebook. The mm-lux monitor row had been classified by contract
*name*; re-read on predicates, the inversion vanished. Both misfilings
pointed in the direction of the thesis — the diagnostic signature of a
classifier tuned by its author's expectations. What survives is exactly the
per-corpus numbers above, each named with its layer and its censoring.

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
   inflated one bug's effect ~4× by crediting it with three corpus-fitted
   vocabulary expansions — the corrected story is itself a caveat on the
   87.6% figure.

## 6. The transmissibility study: four passes, a pre-registered stop

All raters in this study are fresh LLM-agent instances — blind to each
other, to the tallies, and to the authors' expectations (see limitation 6
for what that population does and does not control). The §4 census's
20-item DISAGREE bucket (raw two-rater agreement 90.2%, eliminable-vs-not
96.1%) localized two codebook gaps. We repaired them under pre-registration
and re-rated — twice — with every prediction committed to git before the
rater existed:

- **Codebook v2** (rules 10–11, predictions: gains concentrate in the 20;
  headline stays in 80–82%). **Pass 3 failed its criterion** — headline
  69.6% — and the failure localized to an *instrument* defect: the rater
  prompt had **paraphrased** NEGOTIATION ("selected value in the
  intersection") where the codebook says *emptiness* of the intersection;
  the paraphrase annexed rule-1 territory and 16 items migrated. The pass
  is archived invalid ([`rfc8446-s4-pass3.md`](census/tls13/rfc8446-s4-pass3.md));
  per the pre-registration, an out-of-band pass is evidence about the pass,
  never a new number.
- **Codebook v3** (rules 12–14 + the verbatim rater pack; predictions: NEG
  single digits, 184-item agreement ≥ 90%, headline in 80–82%, rule-10
  pattern reproduces). **Pass 4: 1 of 4 predictions passed**
  ([`rfc8446-s4-pass4.md`](census/tls13/rfc8446-s4-pass4.md)). NEG healed
  completely (23 → 2; all 16 collision items returned). But item-level
  agreement recovered only to 86.4%, the headline landed at 82.8%, and two
  guard-vs-predicate items flipped between passes. The pre-committed
  interpretation applies: **the codebook is not transmissible by text alone
  at item granularity, and that verdict — not a new headline — is the
  result.** The decision not to run a pass 5 was made at close-out (each
  further rule would be fitted to this corpus's residuals); what was
  pre-registered is the interpretation just quoted. The quoted range still
  widens to 80–83% because rater D's *instrument* was valid even though the
  predictions about D's output failed — excluding a valid rater whose
  result is inconvenient would be cherry-picking in the other direction,
  while C stays excluded because C's instrument measured a paraphrase, not
  the codebook (the full reconciliation is in the pass-4 report).

What four passes measured:

1. **Discriminator-crispness predicts transmissibility.** CV and META were
   **item-for-item identical across every rater, including the invalidated
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
   Those 15 are the census's visible error bar; they remain unadjudicated
   and are listed in the pass-4 report.

## 7. Related work

FSM-*extraction* from RFCs is a mature genre — RFCNLP / attack synthesis
(NDSS 2022, arXiv:2202.09470), PROSPER (HotNets 2023), FlowFSM, LLM-ensemble
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
3. **One protocol per layer.** Wayland is one protocol; TLS 1.3 §4 is one
   section of one RFC. The optional second security RFC (Noise or RFC 9420
   MLS) that would turn a data point into a comparison has not been run.
4. **Sentence-level extraction.** Compound sentences count once; n = 204 is
   a sentence count, not an obligation count; SHOULD-level text is absent by
   design.
5. **Item-level labels carry a measured error bar** (§6): raw inter-rater
   agreement 81–90%, 15 items with fresh-rater consensus against the
   original labels, guard-boundary judgments that flip between competent
   raters. Every headline in this paper is quoted at the granularity that
   survives that error bar.
6. **Rater population.** All raters are LLM agents — each a fresh instance
   given only its instrument and the corpus, blind to the other raters, the
   tallies, and the authors' expectations. A human-rater replication has
   not been run, and shared model priors are a residual common-cause risk
   that blindness does not remove.
7. **Rater B's full label map was never archived.** Only B's 16 recorded
   disagreement labels survive (plus agreement on the other 184); B's
   figures — including the 79.9% floor of the headline range — are
   arithmetically consistent with the recorded labels but not
   item-recomputable for four items. A provenance defect, recorded rather
   than repaired.

## 9. Conclusion

Three corpora, three layers, one codebook: a monitoring corpus that is
three-quarters policy thresholds and structurally cannot contain typestate;
a windowing protocol whose declared errors are 87.6% type-eliminable in
shape; and a cryptographic handshake whose normative surface is 80–83%
type-eliminable, with a secret-dependent core of 2.9% that every rater
agrees on item-for-item. The recurring result is that *where a protocol
boundary's obligations are declared, most of them are state-machine and
format discipline* — the kind of thing types discharge — while at the
monitoring layer the mix inverts toward thresholds and revoked facts; in
both cases the truly type-resistant residue is small at the boundary and
precisely nameable everywhere.

The method is the other half. Every headline here survived, or was produced
by, a failure: a retracted cross-layer claim, an invalidated rating pass, a
repair loop stopped by its own pre-registration. What made those failures
productive rather than embarrassing was mechanical: classify on predicates,
make disagreement loud, commit predictions before evidence, and treat "the
instrument does not transmit" as a result. A codebook, like a protocol, is
a boundary — and the same lesson applies at both: what you do not declare
crisply, you will re-litigate at runtime.

## Appendix: artifact map

| artifact | contents |
|---|---|
| `codebook/classes.md` | taxonomy, honesty rules 1–14, retraction + addendum, v2/v3 amendments, graduation record |
| `codebook/rater-pack.md` | the verbatim rating instrument (blob hash cited in pass reports) |
| `census/promql/promql-classifier.py` | n=1155 classifier, rule-9 hardened |
| `census/wayland/{wayland-classifier.py, extract-corpus.py}` | n=172/216 classifier + from-source corpus regeneration |
| `census/wayland/cv-neg-falsifiability.md` | the graduation falsifiability check (0/216, 0/216) |
| `census/tls13/tls13-alert-census.md` | 30-minute alert probe (n=25) — forced CV/NEG, granularity warning |
| `census/tls13/{rfc8446-s4-census.md, rfc8446_s4_musts.txt}` | the n=204 census, corpus, two-rater analysis, close-out |
| `census/tls13/rfc8446-s4-pass{3,4}.md` | the transmissibility study: failed pass + archived labels, stop verdict |
