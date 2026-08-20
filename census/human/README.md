# Human-rater pass H1 — registration (PUSHED BEFORE ANY RATER RATES)

> **[STATUS BANNER added 2026-08-20 — marked insertion; no original wording is
> altered or removed. Placed at the top because the operative instruction was
> otherwise 390 lines below, where a reader entering here would not reach it.]**
>
> ⛔ **THIS REGISTRATION IS SUPERSEDED.** `packet-h1.md` carries a disclosed
> defect: its format examples leaked real archive labels on graded items, and
> one of them converts the largest measured FAILING branch into a PASS at the
> H2 floor. **Serve `packet-h1r2.md`. NEVER serve `packet-h1.md`.**
>
> Read in this order: this registration (below, unaltered) → the defect
> disclosure and its measurement → **H1-R2, the live superseding registration**
> → the cold-review corrections. `score_h1.py` still validates `packet-h1.md`
> and will grade against the compromised instrument without complaint; use
> `score_h1r2.py`.

**What this is, and is not.** The first non-LLM rating pass in this
repository — the probe of limitation 6's *corpus-shared-prior*
confound (every frontier LLM trained on these RFCs; a shared reading
learned from the corpus would reproduce the archived agreements).
The obfuscation probe (`census/obfuscation/`) measured that lexical
obfuscation does not reach this confound — RFC 5545 stayed
identifiable from structure and disclosed residuals at 95/98% — and
its report's argued extension is that no lexical design would; a
non-LLM rater is thereby the sole remaining route, and this pass is
that rater. It is NOT a census: the sample below is deliberately
stratified toward the corpus's soft residue, so **no share headline
exists here by design** — a stratified sample must not be read as a
census, and no number from this pass ever joins, replaces, or
requalifies any series figure. What it measures is *agreement*: does
the frozen instrument transmit to a human at levels comparable to
the archived LLM band?

**Honest bounds, stated first.** One human, one corpus, one 60-item
sample. A strong result weakens the confound; it cannot eliminate it
(n = 1). A weak result is AMBIGUOUS between (i) shared-LLM-prior
inflation of the archived agreements and (ii) individual human-rater
noise or effort — this design cannot separate those two with one
rater, and the registration says so now, before any outcome is
known. Either way: no census number changes, no re-rating occurs,
and nothing here reflects on any instrument grade. The human's
labels grade the hypothesis space, never the human. One further
disclosed asymmetry: the archived raters labeled all 225 items in
one context; their restricted-to-sample numbers below were produced
with full-corpus context the human will not have.

## The rater seat (owner decision recorded 2026-08-16)

**H1: one recruited non-author human**, who has not read this
repository, its reports, or any account of its findings — the clean
seat, chosen over author-as-rater (which would have carried a
disclosed exposure confound: the owner knows the archived agreement
levels and the corpus's class skew). Recruitment is the owner's;
identity (a pseudonym is fine) and a one-line blindness attestation
are recorded in a **marked, append-only addendum to this file before
rating begins**. Rating conditions, verbatim in the packet: one
sitting, roughly 90 minutes; only the packet — no RFC lookups, no
web, no AI assistance, no discussing items until labels are
returned; one `NUMBER:LABEL` line per item; a trailing `?` for
genuinely torn. Any deviation from these conditions is a protocol
event, disclosed in the report.

## The sample (n = 60, frozen at this registration)

Three strata, mutually disjoint by construction, served **unmarked
and in corpus order** — the rater never sees strata:

- **S-OUT (20)** — the v6 registration's iCalendar outside set, the
  corpus's enumerated residual soft mass (`census/v6-pass/README.md`):
  {1, 2, 7, 37, 46, 47, 69, 77, 79, 118, 138, 141, 185, 192, 193,
  194, 200, 201, 203, 204}.
- **S-FAM (11)** — the recognition family {13, 16, 22, 25, 27, 28,
  91, 146, 210} plus the J4 pair {62, 150}.
- **S-J5 (29)** — a seeded draw from the 194-item both-anchor DOMAIN
  set (J5, enumerated in `census/v6-pass/README.md`): Python
  `random.Random("enforceability-census-human-h1").sample(S194, 29)`,
  sorted — {3, 17, 21, 23, 26, 34, 40, 63, 64, 65, 81, 82, 84, 92,
  98, 111, 114, 115, 122, 124, 134, 148, 149, 151, 169, 175, 180,
  213, 214}. The scorer re-derives this draw from the seed at every
  run; a mismatch is a protocol event.

Item texts are taken verbatim from the frozen corpus
`census/ical/rfc5545_s3_musts.txt`, original numbering kept.

## The instrument, served

The FROZEN v6 pack, `codebook/rater-pack-v6.md`, blob
`f4f9e0b1c478cc05370e8b4ba7f612320698d8f0` — rule 14 verbatim; this
pass cuts no pack. The packet (`packet-h1.md`) embeds the pack
between machine-checked markers; the scorer's known-answer test
asserts byte-identity between the packet's pack section and the
repository file on every run. The preamble (transport, not
instrument) names the corpus — RFC 5545 §3 — as the LLM servings
did (the obfuscation registration discloses that the standard
preamble names the format; anonymization there was the exception).
Beyond the sample-vs-full-corpus asymmetry disclosed above, the
information diet matches the LLM raters': pack, items, nothing
else.

## Pre-registered clauses (committed before any rater)

Namespace H. No measured prior exists for human raters anywhere in
this repository, so both floors are written-justification numbers,
and their failure interpretation is the pre-committed ambiguity
above — a failure licenses nothing except its own honest report.

Both floors follow one stated principle: **the smallest integer that
every measured fail branch fails** — measurement-forced, with no
unacknowledged margin.

- **H1 (DOMAIN-mass transmission):** of the 29 S-J5 items — all
  both-anchor DOMAIN, every archived rater 29/29 on them — at least
  **25** land DOMAIN. Floor justification, measured: a
  label-shuffle mutant (Fisher–Yates of Av6's 225 labels, seed
  `human-mutant-1`) scores **24/29** on this clause — the shuffled
  map is 88.4% DOMAIN (Av6's 199/225), so shuffling barely dents
  DOMAIN mass, and a floor of 24 would be a check the shuffle
  degenerate PASSES. 25 is the smallest floor the shuffle's 24
  fails; the floor is exactly that minimum, and it grants the
  human a 4-item (~14%) allowance below the archived raters'
  uniform 29/29. DISCLOSED PLAINLY: a rater who answers DOMAIN for
  everything passes H1 by construction (measured: 29/29) — H1
  alone refutes neither degenerate; the H1+H2 pair refutes both.
- **H2 (the recognition family):** of the 9 S-FAM recognition items,
  at least **6** land PROCESS. Archived branches, measured on
  exactly this clause: six raters at 9/9; **Av5 at 0/9 and Xv5 at
  5/9 FAIL it** (their convicted DOMAIN drift); the shuffle mutant
  scores 1/9 and constant-DOMAIN 0/9 — both FAIL. 6 is the
  smallest floor that fails every measured branch (the largest,
  Xv5's, is 5); the floor is exactly that minimum, granting the
  human a 3-item allowance below the six 9/9 raters. Correlation
  disclosed: the nine items are two near-duplicate textual
  clusters — three "MUST ignore" items (13, 91, 210) and six "MUST
  treat …the same way as they would the ⟨default⟩ value" items —
  so the nine outcomes are correlated and "of 9" overstates
  independence (Xv5's measured 5/9 shows splits do occur). A human
  PASS is single-rater evidence that the adjudication transmits
  outside the LLM population; a FAIL carries the pre-committed
  ambiguity.

**Report-only quantities** (measured, never graded): match-vs-either-v6
over the 60 (each item counts if the label matches either v6 rater's
archived original-corpus label, normalization as below), quoted
beside the measured context band; per-stratum breakdown; the J4 pair
{62, 150} item-by-item; the 20 S-OUT items item-by-item against the
v6 pair; torn count; per-class distribution. Label normalization,
as in every pass since v5: torn `?` stripped for scoring, base label
governs; U ≡ UNCLASSIFIED, NEG ≡ NEGOTIATION, CV ≡ CRYPTO-VERIFY.

**The measured context band** (every archived iCalendar rater,
restricted to this sample; computed at registration, asserted by the
scorer's KAT):

| rater | H1 (of 29) | H2 (of 9) | match-vs-either-v6 (of 60) |
|---|---|---|---|
| Ai | 29 | 9 | 58 |
| Xi | 29 | 9 | 54 |
| Av4i | 29 | 9 | 59 |
| Xv4i | 29 | 9 | 54 |
| Av5 | 29 | **0** | 50 |
| Xv5 | 29 | 5 | 55 |
| Av6 | 29 | 9 | 60 |
| Xv6 | 29 | 9 | 60 |
| shuffle mutant | **24** | **1** | 31 |
| constant-DOMAIN | 29 | **0** | 36 |

By-construction cells, flagged: Av6/Xv6's match 60/60 is self-match
(match is vs-either-v6), and Av4i/Xv4i's H1 29/29 is definitional
(J5 *is* their DOMAIN intersection). The measured **non-anchor**
band is 50–59 of 60 (83–98%); the two degenerate strategies sit at
31 and 36. The human's match number is reported
against this band, not graded against a floor — inventing a floor
where no rater-class prior exists would be a guess wearing a
clause's clothes.

## Scoring

`score_h1.py` (shipped here) is the only grader. Its known-answer
test: re-derives the frozen draw from its seed; verifies the
packet's pack section byte-identical to `codebook/rater-pack-v6.md`;
re-scores all eight archived raters and asserts the table above
exactly; exhibits both fail branches (shuffle mutant, constant-
DOMAIN). Every check was watched to fail before registration: a
perturbed KAT expectation fails at the perturbed rater, and a
one-byte packet perturbation fails the byte-identity assert. The
rater's labels will be archived verbatim in the report and
round-trip parsed before push.

---

## [ADDENDUM 2026-08-20 — instrument defect disclosed at the artifact. Append-only; nothing above is altered.]

Recorded here rather than deferred to H1's eventual report, because H1 is
paused indefinitely and a contingent report is not a disclosure vehicle. No
rater has seen this packet; nothing below is result-contingent, because there
is no result.

**The defect.** `packet-h1.md` states its return format with two worked
examples that use REAL graded item numbers carrying REAL archive labels.
Quoted verbatim from the frozen packet (lines 27–30), original wording
preserved:

> - Return one line per item, in the form `NUMBER:LABEL`
>   (e.g. `13:PROCESS`). If you are genuinely torn between two
>   … (e.g. `62:DOMAIN?`).

**Measured, not asserted.** Against the eight archived iCalendar raters
(`score_h1.archived()`, run 2026-08-20):

| item | archived labels | in sample | graded under |
|---|---|---|---|
| 13 | PROCESS ×6, DOMAIN ×2 (v5 pair) | S-FAM recognition family | **H2 (graded)** |
| 62 | PROCESS ×4, DOMAIN ×4 | S-FAM, J4 pair | report-only |

So `13:PROCESS` is the modal archived label for a graded item, and
`62:DOMAIN?` is one side of a genuinely contested item presented WITH the
torn marker the archive's 4–4 split would justify. Neither example is
arbitrary; both name the archive's own answers.

**Severity, stated plainly and not minimized.**

1. **Item 13 is one of H2's nine.** H2 requires ≥6 of 9 landing PROCESS. The
   packet supplies one of those six before the rater begins. H2 is the clause
   that carries the instrument: this registration already discloses that a
   constant-DOMAIN rater passes H1 by construction and that only the H1+H2
   pair refutes both degenerates. The leak is on the discriminating half.
2. **Cluster amplification — a stated risk, not a measurement.** This
   registration discloses that the nine are two near-duplicate textual
   clusters, one being the three "MUST ignore" items **13, 91, 210**. A rater
   who takes the cue from 13 has a template for its two near-identical
   siblings. That is a route to 3 of 9 against a floor of 6, where the
   largest measured FAILING branch (Xv5) scored 5. Whether a human would in
   fact carry the cue across the cluster is unmeasured and unmeasurable
   without serving the packet.
3. **Item 62 is milder.** The J4 pair is report-only, never graded. The leak
   there touches a reported quantity and the torn count, not a clause.

**What this does NOT do.** It does not amend the packet, the sample, the
clauses, or the floors — all stay frozen exactly as registered. It does not
affect HL1, whose gate caught the same defect shape (`13:NO`, `62:YES?`)
before registration and fixed it; HL1's examples are drawn from a
deliberately foreign domain for this reason. It does not touch any archived
label, any witness artifact, or any census figure — no published number
depends on this packet, which has never been served.

**Open, and owner's to decide — recorded, not resolved here.** H1 as frozen
should not be served on H2 without this defect being carried into any
resulting report as a first-class caveat on that clause. Three paths, none
taken as of this addendum:

- serve as frozen and report H2 as compromised at the floor (the number would
  be hard to interpret, which is itself an honest outcome);
- demote H2 to report-only for this pass and grade H1 alone — but the
  registration's own analysis says H1 alone refutes neither degenerate, so
  this yields little;
- supersede with a fresh registration carrying a corrected packet
  (foreign-domain examples, per HL1's fix), preserving this one verbatim as
  the superseded instrument. Legitimate precisely because no rater has been
  served: the append-only rule guards against result-contingent revision, and
  there is no result to be contingent on.

Discovered 2026-08-20 while auditing what obligations survive the human-pass
decision. The prior record of this defect lived only in the workspace TODO as
a disclosure owed to a report that might never be written; that is why it is
now stated at the artifact.

### [ADDENDUM 2026-08-20, continued — severity point 2 upgraded from inference to measurement]

The block above recorded cluster amplification as "a stated risk, not a
measurement." That hedge is **superseded**; the original wording is left
standing above so the inference-then-measurement order stays visible. What
follows was measured with `score_h1.archived()` on 2026-08-20, and it is
stronger than the risk it replaces.

**The leak is exactly the size of the entire discriminating margin.**

- H2's floor is **6** of 9.
- The largest measured FAILING branch is **Xv5 at 5/9** — the registration
  says so, and the scorer's own run reproduces it. The floor was set as "the
  smallest integer that every measured fail branch fails," so the gap between
  the archive's worst failing rater and a PASS is **exactly one item**.
- The packet leaks **exactly one answer**: `13:PROCESS`.
- **Item 13 is one of Xv5's four misses.** Xv5's H2 misses are precisely
  `[13, 91, 146, 210]` (Xv5 labels 13 as DOMAIN).

Therefore, mechanically: **a rater reproducing Xv5's convicted DOMAIN drift,
handed this packet, scores 6/9 and PASSES H2 at the floor.** The format
example converts the archive's own recorded fail branch into a pass. H2 as
frozen does not refute the thing H2 was built to refute.

Sharper still: three of Xv5's four misses — 13, 91, 210 — are exactly the
three "MUST ignore" near-duplicate items this registration already names as a
correlated cluster, and the leaked example is a member of that cluster. If
the cue carries across the cluster, Xv5's branch reaches 8/9. Whether a human
carries it remains unmeasured; that a single-item cue alone already flips the
branch does not.

**Consequence for the three paths above.** Path 1 (serve as frozen, report H2
as compromised) is now the weakest of the three, not the most conservative:
it would produce a number that provably cannot separate a genuine pass from
the archive's convicted drift. Path 3 (supersede with a corrected packet,
this one preserved verbatim, no rater ever served) is the only one that
recovers a clause capable of failing. Still owner's decision; still not taken
here.

**Not affected, verified rather than assumed:** `score_h1.py` self-test run
after this addendum — 8 archived scores exact, both fail branches exhibited,
packet pack section byte-identical, SCORER VALIDATED. No published figure,
witness artifact, or archived label depends on this packet.

---

# H1-R2 — superseding registration (2026-08-20)

**Pre-registered before any rater sees any packet. H1 above is superseded, not
amended: its registration text, packet, sample, clauses, floors and grader all
stand exactly as written and remain in the repository as the superseded
instrument.** This section is append-only from here.

## Why supersede

The addendum above discloses, and measures, a defect in `packet-h1.md`: its
return-format examples were `13:PROCESS` and `62:DOMAIN?` — real graded item
numbers carrying the archive's own labels. Item 13 is one of H2's nine and one
of Xv5's four H2 misses `[13, 91, 146, 210]`. H2's floor is 6/9 and the largest
measured FAILING branch is Xv5 at 5/9, so that single token converts the
archive's recorded fail branch into a PASS at the floor. H2 as frozen could not
refute what H2 exists to refute.

**Superseding is legitimate here for one reason, stated plainly: no rater has
ever been served.** The append-only discipline guards against *result-contingent*
revision. There is no result. Nothing below is chosen with knowledge of any
human's answers, because no human has answered.

## What changed — exactly four lines, and nothing else

`packet-h1r2.md` is byte-identical to `packet-h1.md` except lines 27–30.
Original wording preserved above and in the superseded packet:

```
-  (e.g. `13:PROCESS`). If you are genuinely torn between two
-  classes, give your best single label with a trailing `?`
-  (e.g. `62:DOMAIN?`).
+  number, a colon, then exactly one label from the list above. If you
+  are genuinely torn between two classes, give your best single label
+  with a trailing `?` — the number, a colon, your label, then `?`.
```

No item number and no class token appears. This loses the rater nothing: the
packet already enumerates all ten valid labels in the bullet immediately above,
and the pack's own Output section repeats them. The examples were redundant
with an unbiased enumeration sitting four lines higher.

**Unchanged, and verified rather than asserted:** the 60-item sample and its
three strata; the seeded S-J5 draw; both clause definitions; both floors; the
embedded rater pack (byte-identical to `codebook/rater-pack-v6.md`); every item
text; and all scoring logic. Evidence: `score_h1r2.py` reproduces all eight
archived rater scores exactly and exhibits both fail branches, identical to
`score_h1.py` — `Ai/Xi/Av4i/Xv4i` 9/9 on H2, `Av5` 0/9 and `Xv5` 5/9 FAIL,
shuffle mutant 1/9, constant-DOMAIN 0/9.

## The contamination surface was audited, not spot-fixed

The defect was found in two known places; the fix is bounded because the whole
surface was swept, 2026-08-20:

- **Number-shaped:** the only `NUMBER:CLASS` tokens anywhere in the instrument
  outside the item list were lines 28 and 30. Zero others.
- **Text-shaped:** zero 4-gram overlap between any of the eleven S-FAM item
  texts and the embedded rater pack (0/11).
- The pack's single iCalendar mention is rule 16/17's per-corpus datum
  designation ("iCalendar at the transmitted calendar object") — instrument
  content the rater legitimately needs, uniform across all items, not targeted
  at any graded one. Left as is.

## New mechanical guard, negative-controlled

`score_h1r2.py` adds `verify_no_answer_leak()`: no answer-shaped
`NUMBER:CLASS` token may appear before the item list. **Watched to fail on
purpose** — the KAT asserts the guard fires on the superseded packet and names
exactly `[('13','PROCESS'), ('62','DOMAIN')]`, then asserts it is clean on the
R2 packet. A guard never seen failing is not a guard.

Stated for future registrations: **byte-identity checks freeze content; they
cannot see that the content is an answer key.** The v1 grader verified packet
byte-identity, re-derived the seeded draw, exhibited both fail branches and
fired grading mutants — and passed cleanly with the leak in place, because the
leak lived in the instructions rather than the data.

## Disclosed, and deliberately NOT fixed: H2 has zero margin by construction

H2's floor was set by a principled rule — the smallest integer that every
measured fail branch fails. That is why the gap between the worst failing
branch (Xv5, 5/9) and a PASS is exactly one item. The floor is **not** changed
here. Changing a floor after analysing its fragility would be exactly the
result-contingent revision this discipline forbids, and the rule that produced
6 still produces 6.

What follows from it is a reading instruction, not a new number: **H2 is
maximally sensitive to any single contamination**, so an H2 PASS should be read
as evidence only in company with the audit above. Minimum-floor discipline and
leak-tolerance are in direct tension; this registration accepts the former and
discloses the latter.

## Inherited unchanged

The rater seat decision (recorded 2026-08-16), the sample, both clauses, all
report-only quantities, the protocol (one sitting ~90 min, packet only, no
lookups, no AI assistance, no discussion until answers are returned; deviations
are protocol events disclosed as such; no re-serve to the same rater), and the
pre-committed interpretation. Serve `packet-h1r2.md`, never `packet-h1.md`.
Seat requirements also inherit HL1's constraint: an H1-R2 rater must not be an
HL1 rater.

## Grading

`python3 census/human/score_h1r2.py labels.txt`. Bare invocation runs the
known-answer test: eight archived scores exact, both fail branches exhibited,
pack section byte-identical, answer-leak guard clean and negative-controlled.

### [H1-R2 addendum, 2026-08-20 — serving path verified end to end]

Recorded because it had never been done, on H1 or H1-R2: the known-answer test
exercises *archived rater* label maps, not a human's returned lines. The path a
recruit's answers actually travel was unverified in both registrations.

Verified 2026-08-20, after registration and before any serving:

- **Round trip.** An archived rater (Av6) re-expressed exactly as this packet
  instructs a human to write — full names where the packet lists them
  (`UNCLASSIFIED` rather than `U`), torn `?` markers on every seventh line —
  scores **identically** to its archived form: H1 29/29 PASS, H2 9/9 PASS,
  match 60/60, torn 9, all report-only quantities produced.
- **Every alias and case form.** The serving parser plus normalisation was
  exercised on all thirteen forms a rater could plausibly return:
  `CRYPTO-VERIFY`, `CRYPTO-VERIFY?`, `NEGOTIATION`, `NEGOTIATION?`,
  `UNCLASSIFIED`, `CV`, `NEG`, `U`, `U?`, surrounding whitespace, lowercase,
  `META`, `POLICY`. All parse and normalise into the scorer's VALID set.
  *Disclosed: the round-trip above alone would NOT have shown this — Av6's
  labels on this sample contain no CV or NEG item, so two of the three aliases
  were unexercised until tested directly.*
- **Label list consistency.** The packet's "Valid labels" bullet holds exactly
  ten tokens, and normalises token-for-token onto the scorer's VALID set
  (checked mechanically, not by reading).

No defect found; nothing changed as a result. Recorded because "the serving path
works" was an assumption in both registrations until it was run.

### [H1-R2 addendum, 2026-08-20 — cold-review corrections. Append-only; nothing above is altered.]

Three blind cold-review lenses read the H1 addenda and the H1-R2 registration
before push. The supersession itself was checked hard and held — every
supporting number reproduced, no floor moved, no sample changed, no frozen
artifact touched. The following are the errors they found in the surrounding
text. Original wording stands above.

**D1 — The HL1 comparison is WRONG, and its quoted evidence is unrecoverable.**
The addendum says HL1's gate "caught the same defect shape (`13:NO`,
`62:YES?`)" and that "HL1's examples are drawn from a deliberately foreign
domain for this reason." Both parts fail:
- Those two tokens appear **nowhere in this repository except that sentence**.
  `packet-hl1.md` has a single commit, so no pre-fix state exists in git. The
  claimed gate finding came from the author's working notes and **cannot be
  checked against the artifact**. It should not have been stated as though it
  could.
- HL1's actual fix was **not** foreign-domain examples. Its format spec uses
  arbitrary numbers plus an explicit non-membership disclaimer: "(Numbers in
  these two examples are arbitrary and do not appear below.)" The
  foreign-domain pair (book chapters; dictionary consultation) is a *separate*
  device — the two worked YES/NO instances — with a different stated rationale.
  Conflating them invents a third option this addendum never considered:
  **arbitrary-and-disclaimed numbers.** H1-R2 went further (no number, no class
  token), which is defensible, but the record should not misdescribe the sibling.
- Consequence worth stating so nobody copies the wrong template: **HL1 is not
  protected by absence.** Its examples are still number-shaped; its protection
  is not-in-set plus a disclaimer. Verified by hand that 8 and 104 are genuinely
  absent from HL1's 23 items, so there is no live defect — but `score_hl1.py`
  has no mechanical equivalent of `verify_no_answer_leak()`.

**D2 — Item 62 is "milder" for the wrong reason.** The addendum calls
`62:DOMAIN?` "one side of a genuinely contested item," on a 4–4 raw split. The
split is **temporal, not live**: all four early raters say PROCESS, all four
later ones DOMAIN — and the report-only quantity it feeds is *match-vs-either-v6*,
where **both v6 raters label 62 DOMAIN**. Against the actual scoring reference
`62:DOMAIN` is the unambiguously correct answer, not a contested one. "Milder
because report-only" stands; "genuinely contested" is withdrawn.

**D3 — Two mis-citations.** The pack's iCalendar datum designation is **rule 22**
("The datum's boundary is the designated serialization unit"), which serves
rules 10/16/17 — not "rule 16/17" as written. And rule 3's main body is anchored
on corpus 2 (awesome-prometheus-alerts); only its exception clause is Wayland.

**D4 — The quoted diff shows three lines while claiming four.** The count of
four is correct (`diff` reports `27,30c27,30`); the displayed hunk omits the
line-27 change on both sides. The evidence block understates its own claim.

**D5 — "names exactly" described a membership assertion.** The KAT asserted
`('13','PROCESS') in v1 and ('62','DOMAIN') in v1`, which a third leak would
have passed. **Fixed rather than reworded:** the assertion is now exact-set
equality, and `answer_leaks` now matches case-insensitively and tolerates
whitespace around the colon (`13 : process` previously passed silently).

**D6 — "Verified end to end" was true but unshipped; now mechanized.** The three
serving-path checks were real (a reviewer reproduced all three independently)
but lived nowhere in the repository, so re-running the KAT gave no coverage of
the human-answer path — the path this registration exists to certify. That is
precisely what "a guard never seen failing is not a guard" forbids.
`score_h1r2.py`'s KAT now exercises the serving parser directly: the Av6 round
trip, all thirteen alias/case forms, **four malformed returns that must be
rejected**, and the packet's label list against VALID.

**Grader change disclosed.** `score_h1r2.py` was strengthened after its
registration section was written (D5, D6). No sample, clause, floor, or scoring
logic changed — the eight archived KAT scores and both fail branches are
unchanged and still exact. Legitimate for the same reason the supersession is:
**no rater has been served, so nothing here is result-contingent.** Stated
rather than left for a reader to diff.
