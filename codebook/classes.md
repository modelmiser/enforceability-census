# The classes of runtime assertion

> ⛔ **RETRACTED 2026-08-02, same day: "the class mix is a property of the
> LAYER" is FALSE and the 88%-vs-2% inversion below must not be cited.** Cold
> review falsified it and the falsification was verified against sources. The
> mm-lux row was classified by contract NAME, not predicate; re-reading the
> contract descriptions puts its `wayland.*` subset at **62.5% typestate against
> the spec's 47.7%** — the monitor has MORE typestate than the spec, and the
> inversion vanishes on like-for-like comparison. Full account in the
> **Retraction** section at the end. The four CLASSES remain useful; the
> cross-layer CLAIM does not.
>
> **Revised 2026-08-02 after corpus 3.** This document described three classes.
> A Wayland corpus — which, unlike a metrics corpus, *can* express protocol
> obligations — required a fourth (**DOMAIN**).


A reliability check exists because *something could be wrong at runtime*. But not
all runtime checks are the same kind of thing, and the differences decide what
you can do about them. Three classes *[historical: four after the 2026-08-02
revision; six after the 2026-08-13 graduation at the end of this file]*,
distinguished by **the shape of the predicate**, not by the wording of the alert.

---

## Class 1 — THRESHOLD on a continuous quantity

**Shape:** an inequality against a number. `p99 > 250ms`, `cpu_pressure > 1.5`,
`disk_avail / disk_total < .10`.

**Why it is at runtime:** it has no truth value at all until somebody picks the
number. There is no fact of the matter about "elevated." The predicate is a
*policy decision* wearing the costume of an observation.

**What you can do:** nothing at the type layer, ever. This class is not a
verification target. The engineering questions are different ones — who chose
the constant, what is the hysteresis, what happens at 1.49, does the threshold
self-calibrate against a measured reference rather than a literal.

**Sub-class worth tracking: THRESHOLD-dynamic.** The right-hand side is another
measured quantity rather than a literal (`temp_celsius > temp_max_celsius`,
`connections >= settings_max_connections`). Same class — a line on a continuous
scale — but a *better-engineered* one, because the line moves with the system
instead of rotting in a config file. When auditing, flag literal thresholds that
have a dynamic counterpart available.

**Related, and deliberately not merged:** this class has the shape of Lamport's
*Buridan's Principle* — a discrete decision on a continuous-valued input cannot
be made in bounded time. Whether that is the same obstruction or a rhyme is not
settled here.

---

## Class 2 — REVOCABLE FACT (the residue)

**Shape:** equality, absence, or supersession on a discrete status.
`up == 0`, `absent(job)`, `changes(...)`, `observed_generation != metadata_generation`,
`surface.leave` for an output the surface never entered *[2026-08-13: this
last example is the `leave_orphan` misfiling the RETRACTION below names —
its predicate is a history predicate, shape TYPESTATE, not REVOCABLE; kept
here bracketed because deleting it would hide the very error the retraction
documents]*.

**Why it is at runtime:** the fact was true and became false. Tracking that needs
an ordering — a clock — and no static structure is a clock. A type, a seal, a
brand, a session type: each witnesses a fact *at a point*. The boundary here is
the CALM theorem's monotonicity frontier (Hellerstein & Alvaro's
consistency-as-logical-monotonicity line): monotone facts can be certified once
and forever, non-monotone facts — facts that can be *un*-made — cannot, and no
type discipline changes which side of that line a predicate sits on.

**What you can do:** name the clock. For every check in this class the audit
should be able to answer *what ordering decides staleness here* — an epoch, a
generation counter, a lease, a version, a sequence number. A revocable fact with
no named clock is the actual defect; the alert is only its symptom.

**Recurring sub-shapes:** staleness (a read that was fresh), eviction (a resource
that was resident), supersession (a generation that was current), revocation (a
grant that was valid), membership (a set you were in). We explicitly do
**not** claim these are one object — only that they share a shape.

---

## Class 0 — DOMAIN: a monotone predicate on one value

**Shape:** a check on a single argument, with no reference to history, no clock,
no threshold. `transform must be one of 8 enum values`. `format is not known`.
`surface is not an xdg_toplevel`. `fd not seekable`.

**Why it is at runtime:** the boundary is untyped. The wire carries a `uint32`
and somebody has to check it is one of the eight legal values. Nothing deeper is
going on.

**What you can do:** this is the **cheapest** class to eliminate — cheaper than
typestate, because it needs no ordering. A real enum or newtype in the generated
binding makes the illegal value unrepresentable. No session type required.

**It only appears in corpora that describe a boundary.** Metrics corpora have no
class 0 at all, because a monitor never validates an argument — by the time a
number reaches a time series it has already been accepted. Discovering this class
is what forced the revision to this document; folding it into TYPESTATE would
have been exactly the absorb-into-the-nearest-bucket error rule 2 warns about.

---

## Class 3 — TYPESTATE across a boundary

**Shape:** an ordering obligation over one object's own history.
`commit` without a prior `attach`. `commit` without acking the pending
`configure`. Use-after-close. Double-free.

**Why it is at runtime:** *only* because the enforcing compiler does not own both
sides of the boundary. The fact is monotone and perfectly typeable in-process —
Rust typestate, session types, a linear type. It escaped to runtime at a process,
protocol, FFI, or plugin boundary.

**What you can do:** this is the one class verification actually eliminates. Each
item here is an unexercised option, not a law of nature. The fix is to push the
type across the wire: generated protocol bindings with typestate, session types
on the channel, a capability that cannot be constructed in the wrong order.

**Rare at the monitoring layer, dominant at the protocol layer.** 4/107 and
0/1155 in metrics corpora; 47% in both Wayland corpora. That gap is the point —
see below. *[2026-08-13: read this sentence against the RETRACTION below — the
cross-layer "gap" thesis was retracted; the mm-lux figure's denominator (107) is
itself declared unknown by the retraction addendum. The per-corpus numbers
stand; the layer generalization does not.]*

---

## Classes added after the original four — where their definitions live

**CRYPTO-VERIFY** and **NEGOTIATION** (graduated 2026-08-13) are defined in
`rater-pack.md` §Classes, with their discriminators as decision rules 2 and
12; the graduation record at the end of this file states the evidence. The
bookkeeping classes **PROCESS**, **POLICY**, **META**, and
**UNCLASSIFIED-unverifiable** are likewise defined in `rater-pack.md`
§Classes (POLICY also in rule 13; the U-boundary in rule 11). The four
sections above are the original codebook and keep their historical form.

---

## Calibration: measured class ratios

Four corpora, independently authored, different domains, different assertion
languages. None was written with this taxonomy in mind. (Corpus numbering
used in the rules below: corpus 2 = awesome-prometheus-alerts, corpus 3a =
wayland-protocols declared errors, corpus 3b = smithay `post_error` sites;
corpus 1 = the mm-lux contract set, private.)

| Corpus | Layer | n | Domain | Typestate | Revocable | Threshold | Uncl. |
|---|---|---|---|---|---|---|---|
| wayland-protocols (core + 36 ext) | protocol **spec** | 172 | 39.0% | 47.7% | 3.5% | 4.7% | 1.2% |
| smithay `post_error` sites | protocol **impl** | 66 | 36.4% | 47.0% | 1.5% | 9.1% | 4.5% |
| `mm-lux` contracts | runtime **monitor** | 107 | — | ~4% | ~24% | ~76% | 18% |
| `awesome-prometheus-alerts` | ops **monitor** | 1155 | — | 0% | 21.4% | 78.6% | 0.6% |

*[Denominator note, 2026-08-13: the PromQL row mixes denominators — 21.4/78.6
are per-1148 classified while 0.6 is per-1155; on one denominator (all 1155)
the row reads 0% / 21.3% / 78.1% / 0.6%. The Wayland row's per-class figures
are per-172; the 87.6% headline quoted elsewhere is per-170 client-facing
(172 − 2 RESOURCE), i.e., 149/170; on n=172 it is 86.6%. The mm-lux row's
entries (~4 + ~24 + ~76 + 18 ≈ 122) cannot share any single denominator —
that row's denominator is declared unknown by the addendum below. The two
protocol rows also do not total 100% because the table has no columns for
the RESOURCE and AMBIGUOUS buckets (on n=172 those hold 1.2% + 2.9%). This
is exactly the mixed-denominator trap rule 3's spirit warns about, caught at
the publish gate.]*

## ⛔ RETRACTED CLAIM — The class mix is a property of the LAYER, not of software

*[This section and the calibration table above it are preserved verbatim under
the retraction banner at the top of this file; see RETRACTION below. The mm-lux
row comes from a private codebase; the smithay row's analysis is not shipped
here (smithay itself is public); neither row is reproducible from this
repository. The wayland-protocols and PromQL rows are.]*

The four corpora do not disagree. They are measuring different altitudes of the
*same* stack — mm-lux literally monitors Wayland, and cosmic-comp is built on
smithay — and the mix inverts almost perfectly as you climb:

- **At a protocol boundary: 84–88% of declared obligations are eliminable by a
  type** (domain + typestate). Residue is 1.5–3.5%. Thresholds are 5–9%.
- **At the monitoring layer: 0–4% is eliminable.** Residue is ~22%, thresholds
  ~78%, and class 0 does not occur at all.

The mechanism is straightforward once stated: **the eliminable classes are
consumed where they are caught.** A protocol error kills the client at the
boundary; it never becomes a metric. Everything that survives to the monitoring
layer has already been filtered of the things a type could have caught, which is
why a monitor sees only revocable facts and thresholds. Both measurements are
correct. Neither generalises to "software."

**So the useful question is not "what fraction of bugs can verification catch?"
It is "does this boundary have a declared obligation set at all?"** Wayland is
unusual: 172 errors, specified, versioned, machine-readable. The median internal
API has zero. Where obligations are never declared they are never checked, and
they resurface downstream as residue nobody can explain — which reads as
irreducible complexity but is really an undeclared spec.

### Corollaries worth acting on

- **Class 0 is nearly free and nobody collects it.** 36–39% of Wayland's
  declared errors are single-argument validation. A generated binding with real
  enums and newtypes removes them without any ordering machinery.
- **A spec-vs-impl gap is measurable.** smithay emits 62 of the 172 declared
  errors — **36% spec coverage** — while matching the spec's *class mix* almost
  exactly (36.4/47.0 vs 39.0/47.7). Implementations under-enforce uniformly
  rather than selectively, so coverage is a volume problem, not a priority one.
- **Don't compare percentages across layers.** Always report the layer.

### Censoring — read this before quoting any typestate number

PromQL cannot express "these events for this object arrived out of order." A
Prometheus corpus is **structurally incapable** of containing class 3, and its
`0` is a fact about the query language, not about software. Symmetrically, a
protocol-error corpus is near-incapable of containing class 1: it has no access
to continuous quantities, which is why thresholds there are 5–9% rather than
~78%. **Every corpus censors some class.** Name which one before reporting.

---

## Classifying: precedence and honesty rules

*(Format note, 2026-08-13: rules are set as bold headings, not markdown
ordered lists, so the written rule numbers survive rendering — markdown
renumbers ordered lists sequentially, which would break every "rule N"
cross-reference in this repository. The non-sequential order of rules 1–7 is
historical: rules keep their numbers from the order they were added.)*

**Rule 1 — Test class 2 before class 1.** `up == 0` is an equality and must not be
   swallowed by a generic comparison rule. Revocation first, thresholds second.

**Rule 2 — Always keep an UNCLASSIFIED bucket and always report it.** A classifier
   that cannot say "I don't know" will silently absorb ambiguous items into
   whichever rule its regex hit first. On the first mm-lux pass an over-greedy
   regex pulled ~20 D-Bus bus names and unrelated `verify.*` facts into the
   contract set; the visible unclassified bucket is what caught it.

**Rule 3 — Fix the classifier, then report both numbers.** Reading the unclassified
   bucket will suggest fixes. Apply them — but publish the pre-fix and post-fix
   ratios side by side. If a fix swings the headline, you tuned to the answer.
   (On corpus 2, fixes moved 33 items and the ratio moved 0.4 points. That is
   what robustness looks like.)
   **Exception, and know which case you are in:** a run with a large
   unclassified bucket has no headline to swing. Corpus 3a went 29.1% → 1.2%
   unclassified and its ratios moved 12+ points — that is not tuning, because
   the 29.1% run was never a measurement. The rule applies to swings from
   *already-good* coverage. State the pre-fix coverage so a reader can tell.
   *[2026-08-13: the addendum's reconstruction of this anecdote uses a 29.7%
   v1 baseline (its own re-derivation of the v1 classifier) against this
   section's contemporaneous 29.1%; the half-point gap is reconstruction
   noise between two v1 approximations, and the addendum's larger point —
   the single regex bug explains only 29.7→14.5 of the swing — stands on
   either baseline.]*

**Rule 6 — Watch `\b` against snake_case.** `_` is a word character, so `\balready\b`
   does **not** match `already_captured` and `\bunsupported\b` does not match
   `unsupported_buffer`. On corpus 3a this silently voided nearly every match
   against the identifier and parked 50 items in unclassified. Normalise `_` to
   a space before matching. This defect is invisible without the bucket.

**Rule 7 — Name the class your corpus censors** before reporting any percentage.
   Metrics corpora cannot express typestate; protocol corpora cannot express
   thresholds. There is no uncensored corpus.

**Rule 4 — Hand-audit a deterministic sample.** Rank items by a hash of their name and
   check the first ~12 by hand. Deterministic beats random: it is reproducible
   across runs and cannot be re-rolled until it looks good.

**Rule 5 — Do not report a class-3 count from a corpus that cannot express class 3.**

---

# RETRACTION — 2026-08-02

The "class mix is a property of the layer" claim above was falsified by cold
review on the day it was written. Recorded here in full because the failure is
more instructive than the claim was.

*[Note for public readers, 2026-08-13: `mm-lux` is a private codebase; its
file references in this section (`wayland_contract.rs`, `verify_contract.rs`,
`wayland_tracker.rs`) are preserved for the historical record and are not
resolvable from this repository. The wayland-rs reference
(`wayland-backend/src/protocol.rs`) is public.]*

## What was wrong

**The mm-lux row was classified by contract NAME, not by predicate.** Re-reading
each contract's own description string in `active/mm-lux/src/wayland_contract.rs`
and comparing only the Wayland subset against the Wayland spec — the sole
like-for-like pairing available:

| | mm-lux `wayland.*` (monitor) | wayland-protocols (spec) |
|---|---|---|
| n | 24 | 172 |
| typestate | **62.5%** | 47.7% |
| domain | 8.3% | 39.0% |
| threshold | 16.7% | 4.7% |
| revocable | 0% | 3.5% |

The monitor carries *more* typestate than the spec. There is no inversion.

Two misfilings drove the original result, **both in the direction of the
thesis** — the diagnostic signature of a classifier tuned by its author's
expectations:

- `wayland.surface.leave_orphan` — "leave for an output the surface *never
  entered*" — filed REVOCABLE while the gloss quoted a history predicate.
- `wayland.server_new_id.range` — a bounds check on a single value
  (`wayland_contract.rs:836`) — filed TYPESTATE, in support of a claim that
  monitors never validate arguments.

## Two further structural errors

**Subject-matter mismatch.** Roughly three-quarters of mm-lux is kernel and
hardware telemetry — PSI, block-IO percentiles, scheduler latency, thermal,
cgroup OOM — which has no counterpart in a protocol corpus. "One stack at four
altitudes" was false for the row carrying the finding: its threshold share
tracked *what the author felt like instrumenting*, not altitude.

**An unrun counter-corpus.** D-Bus sits at the same altitude, in the same
desktop stack, and is already monitored by mm-lux. Its ~33 standard error
constants classify to roughly 36% eliminable, not 88%. One within-layer corpus
falsifies "the mix is a property of the layer," and it was available the whole
time.

## What survives

- **Wayland's declared error set is 87.6% eliminable by a type.** A claim about
  one protocol. It does not generalise to "protocol boundaries."
- **smithay emits 62 of 172 declared errors (36%) while matching the spec's
  class mix almost exactly** — under-enforcement is uniform, not selective.
  *[Superseded by the addendum below, same review round: the 36% is
  unmeasured (name-join ambiguity; true figure somewhere in 36–59%) and the
  uniformity claim is unsupported. Kept in this list only because the
  addendum postdates it; it does NOT survive.]*
- **The PromQL predicate-shape census** (n=1155, 78.6% threshold, 0.6%
  unclassified *[denominators mixed in this bullet: 78.6 is per-1148
  classified, 0.6 per-1155 — see the denominator note under the calibration
  table]*). A prior-art sweep found nothing comparable in the literature.
  Methodologically the strongest corpus here and the most defensible result.

## A wrong finding replaced by a better one

"Domain errors are nearly free and nobody collects them" is **false** for
wayland-rs. `wayland-scanner` already generates real Rust enums; the generated
type is `WEnum<T> = Value(T) | Unknown(u32)`
(`wayland-backend/src/protocol.rs:296`), and `Unknown` is deliberate. A
**versioned, forward-compatible boundary must admit values the current spec
forbids**, or it breaks against newer peers.

So: domain errors are not fully type-eliminable at a versioned boundary. That is
a real limit on eliminability, it was found in the data, and it is a better
finding than the one it replaces because it bounds the thesis instead of
inflating it.

## Prior art this taxonomy must position against

- **Gao, Bird & Barr, "To Type or Not to Type," ICSE 2017** — the canonical
  "types catch 15% of bugs" number, which *already states* the survivorship
  caveat about evaluating against bugs that survived testing and review.
- **Chillarege et al., Orthogonal Defect Classification, IEEE TSE 1992**, and
  **Chillarege & Bassin, ODC triggers, 1995** — already own "the observed
  distribution is a function of the observation point," on the process-phase
  axis rather than the altitude axis.
- **Tsipenyuk, Chess & McGraw, "Seven Pernicious Kingdoms," 2005** — Input
  Validation ≈ domain, API Abuse ≈ typestate, Time and State ≈ revocable. Three
  of the four classes have a 2005 ancestor at the same joints. Only THRESHOLD
  appears to be new, because defect taxonomies classify bugs, not monitors.
- **Dwyer, Avrunin & Corbett, ICSE 1999** — methodological precedent for
  classifying a specification corpus into a small scheme and reporting the mix.

## The method lesson, corrected

Rule 2 of the honesty rules credits the mandatory unclassified bucket. That
stands — it caught the `\b`-vs-snake_case defect. But the far more damaging
error, the one that produced a false headline, **never touched the bucket**: a
name-based classifier placed every item confidently and reported 76% threshold
with no distress signal at all.

**A check that fails loudly catches defects. A check that fails silently is
worse than no check, because it launders a wrong answer into a
publishable-looking number.** The bucket only protects you where the classifier
knows it is guessing. Add rule 8:

**Rule 8 — Classify on the predicate, never the identifier — and when you must use
   names, treat the result as a hypothesis, not a measurement.** Names encode
   the author's intent, not the predicate's shape. If two corpora are classified
   by different methods, they are not comparable, and any finding that depends
   on comparing them is an artifact until re-run under one method.

**Rule 9 — Enforce rule 8 with a disagreement bucket, not discipline.** Rule 8 is only
   a habit until the classifier can catch its own violation. **Both classifiers**
   (`wayland-classifier.py` and `promql-classifier.py`) now classify each item
   twice — on the predicate (the measurement: `summary`+`desc` for Wayland, the
   query for PromQL) and on the name (a hypothesis) — and report a **DISAGREE**
   bucket where the two are both confident but differ, plus a name-based hint
   bucket (**NAME-ONLY** when there is no predicate text; **NAME-HINT** when the
   predicate view is UNCLASSIFIED but the name suggests a class). *[2026-08-13:
   as implemented, each classifier ships one hint bucket, and the Wayland
   classifier's NAME-ONLY flag fires on "predicate-view UNCLASSIFIED and
   name-view confident" — including items that do have predicate text; the
   two-bucket description here is the design sketch, not the shipped
   behavior. No quoted number depends on the hint buckets.]* A non-empty
   DISAGREE bucket means the name-view and predicate-view of the corpus disagree;
   resolve those by hand before quoting any ratio. This is the check that, had it
   existed, would have caught the retraction below on the first pass —
   `leave_orphan` (name→REVOCABLE, predicate→history) and `server_new_id.range`
   (name→TYPESTATE, predicate→bounds) both land in DISAGREE. The name-based
   classifier could not raise it because it placed every item confidently; the
   fix is a "these two views disagree" signal, not another "I don't know" bucket.

## Addendum — the accuracy lens (same review round)

A fourth lens recomputed every figure from the raw JSON and primary sources. It
found eight further critical defects. Recorded because together they change the
verdict from "one claim retracted" to **"the study needs re-running before any
of it is reportable except two corpora."**

- **`verify.*` are REGISTERED CONTRACTS, and excluding them was the error.**
  `mm-lux/src/verify_contract.rs` — *"Registers into the existing
  ContractRegistry, evaluated by the existing 500ms evaluation loop"*, `pub fn
  register()` at line 431, 20 `register_*` helpers taking
  `&mut ContractRegistry`. The census dropped 21 of them as regex junk and the
  blog draft (an unpublished draft, not in this repository) cited the
  dropping as a methodological success. They are also the
  claim-vs-ground-truth family — the most residue-relevant class in the repo.
- **The `\b` anecdote was inflated ~4×.** Reconstructing v1 and applying *only*
  the underscore normalisation gives 29.7% → 14.5% unclassified, not
  29.1% → 1.2%. Three further vocabulary expansions — each fitted to the corpus
  *after reading it* — did the rest. The write-up credited one regex bug with
  four interventions' effect. **The 48% typestate figure depends on
  corpus-fitted vocabulary and must be reported as such.**
- **The showcase obligation pair was a false identification.**
  `xdg_surface.not_constructed` is a *role* obligation; mm-lux's
  `commit_without_attach` **explicitly excludes xdg-role surfaces**
  (`wayland_tracker.rs:2002`, comment: *"role assignment before first attach is
  normal for xdg_surface initial configure"*). Committing an xdg_surface with no
  buffer is *required* by xdg-shell. Not one obligation at two altitudes — two
  different obligations over disjoint populations.
- **"36% spec coverage" is unmeasured.** The join is one-to-one on error NAME
  across all interfaces. 27 of 172 names appear in multiple interfaces (`role`
  ×9); smithay posts `Error::Role` from six distinct interfaces and the join
  records one row. Counting every declaration gives 101/172 = 58.7%. True figure
  lies somewhere in 36–59% and the spread is the join's ambiguity. The derived
  claim "under-enforces uniformly, not selectively" is likewise unsupported.
- **"1,500 assertions" double-counts.** 62 of smithay's 66 rows *are* rows in
  the 172, joined and re-classified **from the spec's own summary/desc text** —
  so corpus 3b never independently read what smithay enforces. Distinct
  assertions ≈ 1,438.
- **20 of wayland-protocols' 53 extensions declare no errors at all**, and 3 of
  the 37 files used are from the `misc`/`experimental` sets, not
  wayland-protocols. Declaration is not universal even at the exemplar boundary.
  *[2026-08-13: on the regenerable superset checkout (experimental included),
  the count is 20 of 65 extension files; the 20/53 figure is tied to the
  census-era checkout, which is not shipped.]*
- **The mm-lux denominator is unknown.** 107 includes extraction artifacts
  (`memory.current`/`memory.high` are cgroup filenames; `psi.cpu`/
  `system.psi.cpu` are test fixtures). The project's docs say 87 in one place
  and a live runtime count of 115 in another — 107 may over- *or* under-shoot.
- **Three "deliberately ambiguous" entries were decided by regex precedence.**
  `wp_commit_timer_v1.surface_destroyed` and `wp_fifo_v1.surface_destroyed`
  carry the same meaning as the five held ambiguous but were captured by
  REVOKE's `no longer` before the AMBIG test ran. The abstention was partly
  accidental — a defect the unclassified bucket structurally cannot catch.
  *[2026-08-13: only these two are identifiable in the regenerable corpus;
  the third was tied to the unpinned census-era checkout and cannot be
  named from shipped artifacts.]*

**What reconciles exactly against primary sources, and is therefore reportable:**
the Wayland spec census (172 errors / 77 interfaces; 82 typestate, 67 domain, 8
threshold, 6 revocable; 87.6% eliminable — one protocol) and the PromQL census
(902 / 246 / 7 of 1155; percentages must be stated on one denominator).
Everything else requires a re-run.

---

# CODEBOOK v2 AMENDMENTS — 2026-08-13

**Appended, never edited in place:** ratings taken under v1 must stay
interpretable against the text they were taken under. Motivated by the 20-item
DISAGREE bucket of the RFC 8446 §4 two-rater pass
(`census/tls13/rfc8446-s4-census.md`), which localizes to two codebook gaps —
14 items on a guard-vs-predicate boundary, 3 on the UNCLASSIFIED-unverifiable
boundary.

**Pre-registered before the third rating pass** (this section is committed
before any third rater sees the corpus). Predictions, stated in advance so the
repair can be judged rather than trusted:

- Agreement gains should CONCENTRATE in the 20 DISAGREE items; agreement on
  the other 184 should not degrade.
- Because both readings of the 14 guard-vs-predicate items are interior to the
  eliminable family (DOMAIN vs TYPESTATE) *[scope correction 2026-08-13: true
  for the 10 label-recorded guard items; the 196/204 binary-agreement figure
  forces 3 of the 4 unarchived items [5,54,65,123] to be cross-family, and
  A:54 = PROCESS — see the census's Inter-rater section]*, and resolving the 3
  U-boundary items toward wire-observability stays inside the existing
  two-rater spread, the headline eliminable share should **tighten within the
  current 80–82% band**, not move outside it. A material shift outside the band under these
  rules is evidence the repair is mis-designed, not evidence of a new result.

**Rule 10 — Guard-vs-predicate tie-break: classify by the discharging type.** Many
obligations have the form *"when/after history H, field F MUST satisfy
P"* — a history guard around a value predicate. Neither the guard nor the
predicate wins by syntactic position. Ask instead what type would
discharge the obligation:

- If a single context-free refinement of F's type satisfies every
  occurrence of the obligation — the guard only *locates* where the
  obligation applies, and the required value/set is the same whenever it
  does — the check is **DOMAIN**.
- If the required value/set *varies with history or negotiated state* (the
  same field must hold different values depending on what happened
  before), no context-free type can express it; the discharging type must
  be state-indexed, and the check is **TYPESTATE**.

This generalizes the §4 census's decision rule 1 (cross-message
consistency = TYPESTATE): "ServerHello suite == the suite offered
earlier" varies with history; "legacy_version == 0x0303" does not,
however the sentence happens to be guarded.

**Rule 11 — UNCLASSIFIED-unverifiable boundary: wire-falsifiability.** Classify the
strongest obligation that a conformance observer of the wire — holding
the public transcript, holding neither endpoint's private state — could
falsify:

- If the sentence obliges an *observable configuration* (send / don't
  send / set a field, in circumstances the observer can establish from
  the transcript), classify that observable predicate in the ordinary
  classes, even when the sentence's motivation is honesty about
  capability or intent.
- **UNCLASSIFIED-unverifiable is reserved for sentences whose entire
  normative content is unobservable** — truthfulness of an advertisement,
  randomness or independence of generated values, willingness to act in
  the future. Test: delete the unobservable clause; if no checkable
  obligation remains, the item is U.

Operational form: *could a test harness holding only a packet capture
ever emit a conformance FAIL for this sentence alone?* If no — U. If
yes — classify what the FAIL would check.

---

# CODEBOOK v3 AMENDMENTS — 2026-08-13 (after pass 3)

Motivated by the pass-3 failure (`census/tls13/rfc8446-s4-pass3.md`): a
paraphrased NEGOTIATION definition annexed rule-1 territory and a never-ruled
DOMAIN/PROCESS boundary drifted. Appended before any pass-4 rater exists.

**Pre-registered pass-4 predictions:** NEG returns to single digits (the 16
collision items land TYPESTATE); raw agreement with rater A on the 184
previously-agreed items recovers to ≥ the A-vs-B baseline (90%); the headline
lands inside 80–82%; the guard-vs-predicate pattern from pass 3
(constant-whenever-applicable → DOMAIN; history-varying → TYPESTATE)
reproduces. Any of these failing means the codebook is still not
transmissible by text alone — that verdict, not a new headline, would be the
result.

**Rule 12 — NEGOTIATION discriminator: the predicate is the EXISTENCE of a
compatible choice, never the choice itself.** NEG covers obligations on
the emptiness/compatibility of a two-party set intersection: abort when
offer ∩ config = ∅, proceed only if a mutually supported parameter
exists. The moment the sentence constrains a *specific selected value*
against what was previously offered ("the server's selected X MUST be
one the client offered"), it is cross-message consistency and rule 1
already classifies it: TYPESTATE. Litmus: does the predicate mention a
chosen value? Then it is not NEG.

**Rule 13 — DOMAIN vs PROCESS: classify the wire-observable configuration if the
sentence obliges one.** "MUST set/encode field F to X" is a predicate on
a wire value: DOMAIN (or TYPESTATE via rule 10 if the required value is
history-dependent). PROCESS is reserved for sentences obliging a
computation or procedure with **no wire-observable predicate of their
own** ("derive the secret using HKDF", "iterate in preference order",
"validate before using"). POLICY, for the record, is an
operator/deployment-discretion duty with no per-instance wire predicate
(e.g., "MAY-style profiles a deployment MUST choose among").

**Rule 14 — The instrument is the codebook, verbatim — never a paraphrase.**
Raters receive `codebook/rater-pack.md` byte-identical; each pass report
records the pack's git blob hash. Pass 3 is the existence proof for this
rule: two raters had agreed at 90.2% partly through shared authorial
context, and the first rater who received only a paraphrase diverged
along exactly the boundaries the paraphrase moved. A codebook that
cannot be transmitted by its text alone is not yet a measurement
instrument. *(The pack itself sets rules as bold headings, not markdown
ordered lists, for the rendering reason in the format note above; the
pass-4 instrument is blob `a08febba…`, which used list form — the
reformat postdates pass 4 and changes no rule content.)*

---

# CLASS GRADUATION — 2026-08-13

**CRYPTO-VERIFY and NEGOTIATION graduate from provisional to full classes**,
their definitions as in `rater-pack.md` (CV: verification requiring secret or
transcript-derived material, per decision rule 2; NEG: emptiness/compatibility
of a two-party set intersection, per rule 12).

The gates, stated precisely: **one gate was pre-registered** — the
falsifiability check the §4 census wrote down as its caveat 4 — and it
passed: CV = 0/216, NEG = 0/216 on a regenerated superset corpus; the classes
pick out nothing in a protocol with no cryptography and no negotiation
surface among its declared errors
(`census/wayland/cv-neg-falsifiability.md`). The census's other stated
condition ("graduate after follow-ups 1 and 4 converge") was written before
the passes ran; the passes did *not* converge (that non-convergence is the
recorded pass-4 verdict), so the second basis for graduation is a **stability
criterion articulated at graduation time**, not a pre-registered gate, and it
reads differently per class:

- **CV:** item-for-item identical — the same six items — in every rater's
  recorded labels across four passes, including the invalid-instrument pass
  (B: inference on its four unarchived labels, as for NEG below). The strongest
  stability evidence in the scheme.
- **NEG:** thinner. A applied it to 3 items, D (under rule 12) to 2 of the
  same 3; B's *recorded* labels add no NEG beyond A's three (A's three items
  are outside the recorded 20-item disagreement set, but B's four unarchived
  labels are not archive-forced non-NEG — the same provenance gap flagged in
  the census and the paper's limitation 7); pass 3's blow-up to 23 items
  under a *paraphrased* definition is the cautionary record that motivated
  rule 12 (and rule 14). NEG graduates on its discriminator plus the
  falsifiability result, with its small membership noted.

Standing observation from the same passes: **classes transmit only as well as
their discriminators are crisp.** CV and META: zero variance across all four
raters' recorded labels; THRESHOLD/REVOCABLE: identical across A/C/D with one recorded
exception (rater B read item 189, the 7-day cap, as REVOCABLE — an ambiguity
flagged by A at classification time). The DOMAIN/TYPESTATE/PROCESS
boundaries, whose rules require judgment ("does the required value vary with
history?"), carry all residual disagreement. Confound, stated: the
zero-variance classes are small (1–6 items); perfect agreement on rare,
distinctive items is weaker evidence than the same rate on a 90-item class —
the observation is directional, not a quantitative law. A future class
proposal should still arrive with its discriminator or expect to dissolve on
first text-only transmission.
