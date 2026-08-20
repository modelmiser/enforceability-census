# MECH-PROBE-1 — can a non-LLM classifier recover predicate shape from RFC prose?

> **[STATUS BANNER added 2026-08-20 (round-2 review) — marked insertion; no original
> wording below is altered or removed.]**
>
> ⚠️ **THE SECTIONS BELOW, UP TO "[CORRECTION 2026-08-20]", CONTAIN WITHDRAWN CLAIMS.**
> They are kept as legible error, not as findings. Do not quote from them without the
> corrections.
>
> Withdrawn or corrected: the causal claim that the errors are "exactly decision rule 1"
> and "not a regex-quality problem" (**one** of eleven is decision rule 1); the margin
> "16–23 points" (**17.9–32.1**); "a prior about RFC 5545" (the probe ran on **RFC 9420**);
> "identified from structure alone"; and the headline verdict itself, **downgraded in C7
> from "Negative. Arc closed." to inconclusive on the pre-committed reading.**
>
> **Reading order:** this banner → **[CORRECTION 2026-08-20]** (round 1) →
> **C7 (round 2)**, which corrects the round-1 correction. The sections between are
> provenance.

**2026-08-20 · Feasibility probe, NOT a registered pass. Negative. Arc closed.**
**MLS (RFC 9420 §5–15) is SPENT as a probe corpus by this run.**

## Why this exists

Limitation 6 records that all raters in this repository are LLM agents, and the
obfuscation probe's O1 check measured that the shared prior is real — RFC 5545
was identified from structure alone through 90 nonces. The registered human
passes H1-R2 and HL1 exist to reach that confound from outside the LLM
population; both are blocked on recruiting a blind human.

A rule-based classifier needs no recruit and **cannot hold a prior about
RFC 5545 — a regex has no training data.** This probe asked whether that route
is available. It is not, and the reason is specific enough to be worth keeping.

## Protocol (`PLAN.md`, frozen before the classifier)

`mech1.py` (md5 `b8739771e855ade2acc6829d9f867614`) was written from
`codebook/classes.md` (the four core classes, precedence rules 1, 2, 6) and
`codebook/rater-pack-v6.md` §Classes alone. Every pattern cites the definition
phrase it derives from. **No MLS label was loaded or displayed before the
classifier was frozen.** One run. No tuning loop — adjusting a rule after seeing
agreement would have voided the probe, and did not occur.

## Result: not a measurement

| | value |
|---|---|
| coverage | **56/127 = 44.1% classified; 55.9% UNCLASSIFIED** |
| agreement, covered items only, rater 1 | 26/56 = 46.4% |
| agreement, covered items only, rater 2 | 30/56 = 53.6% |
| const-DOMAIN baseline (same items) | 28.6% / 30.4% |
| seeded-shuffle baseline (same items) | 25.0% / 21.4% |

**Codebook rule 3 already calls a 29.1% unclassified bucket "never a
measurement."** This bucket is 55.9%, so the covered-item agreement is not
quotable as a result: it is accuracy on the items the instrument chose to
answer, while it declined more than half. It does beat both degenerates on that
subset by 16–23 points, so predicate shape is *partially* lexically
recoverable — just not enough of it.

## Why it failed — the errors are not scattered

**DOMAIN↔TYPESTATE confusions, in both directions, are 11/30 and 8/26 of all
errors.** That is exactly decision rule 1:

> Cross-MESSAGE consistency = TYPESTATE; intra-message cross-field = DOMAIN.

A regex cannot see message boundaries. The codebook's discriminators are
**structural** — which message a field lives in; secret versus public material
for CV; framing-derived versus chosen bound for THRESHOLD — and prose expresses
structure without dedicated vocabulary. That is what a lexical instrument
cannot reach, and it is not a regex-quality problem.

## The design finding, which outranks the number

Codebook rule 3 prescribes the repair: read the unclassified bucket, fix the
classifier, publish pre-fix and post-fix ratios side by side. **That path is
unavailable to this instrument, and noticing why is this probe's real output.**

Repairing coverage means reading the 71 unclassified sentences, deciding what
class each is, and encoding those decisions as patterns — an LLM rater with
extra steps, the author's judgment baked into the regex. The prior-freedom that
was the instrument's entire reason for existing is exactly what the repair
destroys.

Rule 3 was written for the Wayland corpus of declared error names, where author
judgment inside the regex was never the thing under test. Here it is precisely
the thing under test. **Rule 3 does not generalise to an instrument whose
independence is the measurement.**

## Consequences, recorded so they are not rediscovered

1. **MLS is spent as a probe corpus.** TLS §4, iCalendar §3 and QUIC remain
   protected and unspent — they carry the locality claims of §6.6/§6.7 and must
   not be probed, only registered against.
2. **Do not register this instrument against a protected corpus.** It answers
   fewer than half the items and its dominant error mode is a known structural
   blind spot.
3. **Limitation 6 stands as written.** The shared-prior half of the confound is
   not cheaply attackable mechanically on prose.
4. The remaining recruit-free lane — found human judgments predating the
   author's framing — addresses **author mediation only**, not the shared prior.

## Files

`PLAN.md` (protocol, frozen first) · `mech1.py` (the classifier, frozen second)
· `pred.txt` (the one run's predictions) · this record.

---

## [CORRECTION 2026-08-20 — cold review. Append-only; nothing above is altered.]

Three blind cold-review lenses read this record before it was pushed. They were
right about a great deal. **The conclusion (arc closed) survives, but neither
the route this record took to it nor the explanation it gave was correct.**
Original wording is left standing above so the error is legible.

### C1. The central causal claim is WRONG — withdrawn

Above, this record says the DOMAIN↔TYPESTATE errors are "exactly decision
rule 1" and, in bold, "**it is not a regex-quality problem**."

**That is false, and the majority of the cited errors refute it.** Dumping every
DOMAIN↔TYPESTATE error with the pattern that fired and the substring it matched:

| item | fired | matched | what it actually is |
|---|---|---|---|
| 18 | `\bre-?use` | `reuse` | inside the FIELD NAME `reuse_guard` |
| 101 | `after` | `after` | "blank nodes after the last non-blank node" — spatial |
| 102 | `until` | `until` | loop terminator, not an ordering duty |
| 70, 78 | `valid\w*` | `valid` | "verify that the list … is valid" |
| 72 | `present` | `present` | guard clause |

Of 11 errors against rater 1, **at most 4 (36, 45, 54, 82) fit the
message-boundary story; 7 are ordinary pattern over-breadth.** Item 18 is the
sharpest refutation available: matching inside a field name is exactly what the
served pack's first instruction forbids ("never on names, labels, or alert
words") and exactly what codebook rule 2 exists to catch. **The dominant error
mechanism is the regex-quality defect this record claimed it was not.**

This is a one-cause story told over a multi-cause result — the author had a
thesis (shape is structural, therefore lexically unreachable), saw the modal
confusion cell, and did not check what fired. "The errors are not scattered" is
also wrong: 37% and 31% spread over 8+ confusion cells is a modal cell, not a
concentration.

**What survives:** that predicate shape is not cheaply recoverable by THIS
instrument. **What does not:** the claim that it is unreachable in principle by
any lexical instrument. A better-engineered classifier might do better — and
that possibility is now live, not excluded.

### C2. The verdict was reached by a criterion PLAN.md did not pre-commit

`PLAN.md` froze: "Beats both degenerates by a clear margin → feasibility
established; the arc is live." The measured margins do that (see C3). This
record nonetheless headlines "Negative. Arc closed," bridging the gap with a
**coverage** criterion that appears nowhere in the pre-committed reading.
Introducing an adjudication axis after seeing the result is structurally the
cardinal sin here, even pointing the conservative way, and **`PLAN.md` was
underspecified — it did not anticipate coverage as a failure mode.** Disclosed
as a protocol event, per the standard the sibling registration sets.

**The pre-committed criterion was in fact satisfied, and this record failed to
compute it.** Scoring all 127 items with UNCLASSIFIED as the real bucket
codebook rule 2 insists it is — not as an abstention:

| | rater 1 (A′) | rater 2 (B′) |
|---|---|---|
| classifier, all 127 | 34/127 = **26.8%** | 34/127 = **26.8%** |
| const-DOMAIN, all 127 | 39/127 = 30.7% | 42/127 = 33.1% |

**The classifier is BELOW the constant baseline on the whole corpus.** PLAN.md
branch 2 ("at or near degenerate → arc closes") fires cleanly, with no coverage
argument needed. The right answer was reachable from data already in hand.

Consequently the rule-3 invocation above is downgraded: rule 3 names one
anecdote, it does not set a coverage floor. The *a fortiori* argument at 55.9%
is fair, but it is an argument, not a pre-existing rule being applied.

### C3. Corrected numbers and identities

- **"beat both degenerates by 16–23 points" is WRONG at both ends.** True
  margins: 17.9, 21.4, 23.2, 32.1. The 16 came from crossing rater 1's
  agreement against rater 2's baseline; the 23 silently dropped the shuffle
  baseline. Range is **17.9–32.1**, on covered items only.
- **"rater 1"/"rater 2" are A′ and B′**, as `PLAN.md` step 4 required and this
  record failed to state. A′ is the non-blind author rater (46.4%); B′ is blind
  (53.6%). **The classifier agrees more with the blind rater** — visible only
  once the mapping is given.
- **"cannot hold a prior about RFC 5545 — a regex has no training data"**
  overstates, and names the wrong document. The probe ran on MLS (**RFC 9420**).
  The regex has no training data; **its author does**, and it shows: four
  patterns (`confirmation tag`, `membership tag`, `psk binder`,
  `transcript hash`) appear in neither cited source and are author-supplied
  protocol vocabulary. `mech1.py`'s docstring claim that the patterns come from
  those sources "ALONE," and that "every pattern cites the definition phrase it
  derives from" (9 comments for ~80 patterns), are both **overstated**. All four
  stray patterns are dead — zero matches — so the result is unaffected.
- **"identified from structure alone"** drops the caveat its source carries. The
  obfuscation registration discloses retained lexical residuals (sibling-RFC
  citations, "rule part(s)", "observance"/"onset", the fold vocabulary) and its
  finding 1 names a lexical route. Correct form, already used elsewhere in this
  repo: **"from structure and disclosed residuals."** Also, O1 measured that the
  identification channel survives obfuscation — an unaddressability result — not
  that the prior is demonstrably operative.
- **Rule 3's main body is anchored on corpus 2 (awesome-prometheus-alerts)**,
  not Wayland; only its exception clause — the 29.1% one invoked here — is
  corpus 3a. "Rule 3 was written for the Wayland corpus of declared error names"
  is imprecise.

### C4. The ordering claim is self-report, not witnessed

`PLAN.md`, `mech1.py`, `pred.txt` and this record all landed in ONE commit, and
the md5 was published simultaneously with the file it hashes, so it freezes
nothing. Everywhere else this repo buys ordering with separately pushed commits
(`0cf32a7` before any rater; `c500361` before any agent; `8821bce` before
`6ba6f9a`). **This probe does not meet that standard and should not be read as
if it does.**

Offered as circumstantial only, and constructed by a reviewer rather than the
author: 55 of the classifier's ~82 patterns match zero MLS sentences, including
four whose terms appear nowhere in the corpus — not what someone writes with the
labelled corpus in front of them. `pred.txt` regenerates byte-identically from
the frozen `mech1.py`, so it was not hand-edited. Neither fact establishes
ordering.

### C5. The shuffle baseline is now reproducible

It was not: no seed and no procedure was recorded, while `PLAN.md` step 5 made
it load-bearing. `score_mech1.py` now ships and re-derives every cell including
the shuffle (seed `20260820`).

### What the review confirmed sound

Every archived measurement, `pred.txt`'s byte-identical regeneration, the md5,
coverage, both covered-item agreements, both const-DOMAIN baselines, the
11/30 and 8/26 counts, and every verbatim quotation of rule 3, decision rule 1
and Limitation 6. The 4-gram contamination sweep is *narrower than the truth* —
overlap is 0/60 and 0/225, not merely 0/11. A reviewer also checked whether the
MLS labels' pack version mismatched `rater-pack-v6.md` and found the `## Classes`
sections **byte-identical**, so there is no instrument-version confound.

### C1a. Precision on C1 — the structural story is weaker still

C1 above says "at most 4 (36, 45, 54, 82) fit the message-boundary story." That
figure was adopted from a reviewer and is itself generous. Checked item by item:

- **[54]** "fields of the GroupContext object **in the Welcome message** MUST be
  the same as the corresponding fields in the …" — unambiguously cross-message.
  Decision rule 1 exactly. **1 item.**
- **[82]** order of `psks` must match order in the `proposals` vector — a
  consistency duty between two parts of one structure; reads intra-message,
  which the codebook calls DOMAIN. Debatable.
- **[45]** `init_key` must be "unique among the set of KeyPackages created" — a
  uniqueness duty over a set across time. Structure the regex cannot see, but
  not decision rule 1's boundary.
- **[36]** length must equal "the length of the resolution of the copath node" —
  depends on tree state; structural, again not cross-message.

So of 11 errors, **exactly one is decision rule 1**; three more involve
structure a lexical instrument cannot see, of differing kinds; seven are pattern
over-breadth. The original record's "exactly decision rule 1" describes **1/11**
of the evidence it was drawn from.

Recorded because the correction inherited the reviewer's number without checking
it, and checking it moved the figure **against** the original claim rather than
toward it. A correction accepted unverified is the same defect in a new coat.

### C6. Why `mech1.py`'s docstring is NOT corrected

C3 records that the docstring overstates: the patterns did not come from the two
cited sources "ALONE" (four are author-supplied protocol vocabulary), and "every
pattern cites the definition phrase it derives from" describes 9 comments over
~80 patterns. **The file is deliberately left unchanged.** Its md5 is the
artifact freezing this probe, quoted in this record and asserted by
`score_mech1.py`'s KAT; editing it would break the freeze and silently rewrite
the thing the hash exists to pin. The correction lives here, where it can be
read against the frozen file — which is what a correction to a frozen artifact
is supposed to look like.

**Pointers:** rule 3 and rules 1/2/6 — [`codebook/classes.md`](../../codebook/classes.md);
decision rule 1 and the class definitions — [`codebook/rater-pack-v6.md`](../../codebook/rater-pack-v6.md);
Limitation 6 — [`PAPER.md`](../../PAPER.md) §8; O1 — [`census/obfuscation/`](../obfuscation);
the corpus and its two archived raters — [`census/mls/`](../mls), and
[`census/mls/SPENT.md`](../mls/SPENT.md) for what this run forecloses.

---

## [C7 — ROUND-2 CORRECTION 2026-08-20. Corrects the correction above.]

A second cold-review round audited the round-1 corrections. It found that **the
correction repeated the defect it named.** C1a's own closing line — "a correction
accepted unverified is the same defect in a new coat" — describes what happened
eighty lines above it. Nothing here is altered; this block corrects it.

### C7.1 — "All four stray patterns are dead — zero matches — so the result is unaffected" is FALSE

Both clauses fail, and both fail in the flattering direction.

- **`membership tag` is not dead.** It fires on item 13 (`norm()` rewrites
  `membership_tag` → `membership tag`) and is the **deciding** pattern, returning
  **CV — correctly**, since both A′ and B′ label item 13 CV.
- **The result is affected.** Removing the four strays: covered **26→25** (A′) and
  **30→29** (B′); whole-corpus **34→33** for both.
- **`psk binder` is not stray at all.** `rater-pack-v6.md` lines 27 and 48 read
  "PSK-binder verification" and "MAC/signature/PSK-binder". It comes from a cited
  source. Only **three** patterns are author-supplied, not four.

So author-supplied protocol vocabulary earns this probe a measurable point, on an
instrument whose premise is that the author's protocol prior is not in it. The
dismissal was written without running it.

### C7.2 — Item 18's diagnosis was an OVERSHOOT, and is withdrawn

C1 called item 18 "the sharpest refutation available: matching inside a field name."
**It did not match inside a field name.** `\bre-?use` fires at offset **28**, in the
ordinary prose "include the reuse guard in the"; the field-name occurrence is at
offset 47 and never fires, because `re.search` returns the first match. After
`norm()` collapses `_` the two are textually indistinguishable, so the claim is not
even demonstrable from the artifact. The independent instance (item 59) also fires on
prose: "To avoid key reuse".

The defect is real — the pattern is over-broad, and the item stays in the
over-breadth bucket, so no count moves. **What is withdrawn is the dramatization.**
An overstated self-accusation is still an inaccuracy.

Mis-citation attached: C1 says name-matching is "exactly what codebook rule 2 exists
to catch." Rule 2 is the UNCLASSIFIED-bucket rule. The on-point rule is **rule 8** —
"classify on the predicate, never the identifier." The sibling correction D3 fixes
exactly this genre of error; the standard existed and was not applied here.

### C7.3 — "Dumping every DOMAIN↔TYPESTATE error" omitted two

A′'s eleven are `[18, 36, 45, 54, 70, 72, 78, 82, 101, 102, 104]`. **Item 104**
(`before`, in "before using the tree") appears nowhere in this file. B′'s **item 59**
(`reuse`) likewise. Both are over-breadth, so the count "7 are ordinary pattern
over-breadth" is right — but it is right only if 104 is silently counted, and a
correction whose method is "dump the evidence rather than tell a story about it" has
to dump all of it.

### C7.4 — The verdict is DOWNGRADED: inconclusive, not clean

C2 declared "branch 2 fires cleanly, with no coverage argument needed." That
overstates. On the whole corpus the classifier is **below** the constant degenerate
(26.8% vs 30.7%/33.1%) but **above** the shuffle (26.8% vs 12.6% at the declared
seed, ~21% at a 2000-seed mean). `PLAN.md` step 5 requires beating **both**.

Failing one rules out branch 1. It does **not** cleanly select branch 2
("at or near degenerate") over branch 3 ("anything in between → inconclusive"). A
result that beats one degenerate by 14 points and loses the other by 4–6 is the
textbook in-between. **Choosing branch 2 was itself a post-hoc adjudication — the
same move C2 convicts the original record of, pointing the same conservative way.**

**Revised standing verdict:** on the pre-committed reading this probe is
**branch 3 — INCONCLUSIVE**. The author's decision not to pursue rests on the design
finding (the repair path is self-defeating), which C1 already re-scoped and which is
weaker than first stated: once most errors are ordinary over-breadth, narrowing a
pattern is a precision fix derivable from the pack's own rule 8, not an act of baking
in label knowledge. **"Negative. Arc closed." is withdrawn in favour of "inconclusive;
not pursued, for a stated and contestable reason."**

Also corrected: C2's sentence "The pre-committed criterion was in fact satisfied"
reads as branch 1 while the table below it fires branch 2. Read "decisive", not
"satisfied".

### C7.5 — `UNCLASSIFIED` is not the pack's `U`, and the equation is unstated

The whole-corpus figure equates them. They are different objects: the classifier's
`UNCLASSIFIED` means **no pattern fired** — an abstention — while the pack's `U` is a
substantive class, "no per-instance predicate exists even in principle". **8 of A′'s
34 and 4 of B′'s 34** whole-corpus agreements are that coincidence: a silent regex
failure credited as a correct call of "unverifiable in principle".

Codebook rule 2 says report the bucket; it does not license scoring it as a class
prediction, and C2's appeal to it is a mis-citation. The convention is **generous to
the classifier**. Scoring abstentions as misses instead gives **26/127 = 20.5%** and
**30/127 = 23.6%** — still below both constant baselines, so the direction survives,
but the headline 34 is inflated by an equation that was never stated.

### C7.6 — C4 and C6 reconciled

C4 says the md5 "freezes nothing"; C6 rests on the md5 "freezing this probe". Both
are true of different properties and neither said so: **the md5 establishes no
temporal ordering** (it was published with the file it hashes — C4's point) **but
does pin content identity going forward** (C6's point). C6 is also oversold: git
already provides an immutable blob, so editing `mech1.py` would not destroy the
record, only desynchronise the hash quoted here and asserted by the KAT. The choice
to leave it stands; the argument for it is narrower than stated.

### C7.7 — "Structure alone" — the attribution was wrong, and the source is now fixed

C3 said the phrase "drops the caveat its source carries". It does not: the source
itself, `census/obfuscation/rfc5545-obf-probe.md` finding 4, said "identification
precedes rating through structure alone", unqualified. This record inherited it
faithfully. C3's substance was right (finding 1 does name a lexical route, and the
residual list is real); its blame was misplaced. The primary artifact has now been
corrected in place with a marked note, so the claim no longer stands anywhere.

### C7.8 — Grader scope, and two hardenings

`score_mech1.py`'s docstring claimed to "re-derive every number in README.md". It
derives every **table cell**; it does not derive the error counts, the dead-pattern
count, or the per-item table. Docstring corrected. The grader now also (a) asserts
`pred.txt` regenerates from the frozen classifier — C4 leaned on that as
circumstantial evidence and it is now a standing check — and (b) prints the
whole-corpus **shuffle** alongside the constant baseline, since C3 faulted the
original for reporting one degenerate and the whole-corpus line was doing the same.

### What round 2 confirmed sound

Every archived measurement; the whole-corpus table; all four margins and the
reconstruction of the original "16"; rater identities (A′ non-blind, B′ blind, and
the classifier does agree more with the blind rater); 11/30 and 8/26; "55 of 82
patterns dead"; `pred.txt`'s byte-identical regeneration; the rule-3 anchoring; and
the 4-gram sweep at **0/11, 0/60, 0/225**. Both reviewers who re-implemented that
sweep initially got a large false overlap and traced it to their own bounds error.
On the shuffle seed: the published pair (14, 12) arises in only ~1.3% of seeds, which
is good evidence the shipped procedure is the original one rather than a seed fitted
to the answer.
