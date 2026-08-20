# HL1 — a human judge against the witnessed locality boundary (registration)

2026-08-17 · **Pre-registered before any human sees the packet.** This
registration is append-only after push; corrections, if ever needed, go
in marked brackets preserving the original wording. Recruit identity
and blindness attestation will be appended here as a marked addendum
BEFORE any rating occurs, per the H1 precedent.

## What is being tested

The locality studies (`census/locality/`, `census/locality2/`; PAPER
§6.6–§6.7) carry a named residual: the witnesses were constructed by
the census author, and a prior shared *at the level of the property
itself* — author and LLM raters trained into the same reading habits —
is not excluded. The registered human pass H1 (`census/human/`,
untouched by this registration) probes the *classification* prior: does
a human, given the verbatim ten-class instrument, draw the archive's
boundary? HL1 probes the *property* prior from the other side, and
against a different kind of target: **does a human, given only the
sentences and a single plainly-stated question, land on the same side
of the formally witnessed boundary?**

The target is witnessed, not voted — with an asymmetry disclosed
plainly. On the YES side (cell A below), every L(i) is backed by a
shipped executable validator (`census/locality2/`, main `6ba6f9a`) —
artifacts that carry their own evidence. On the NO side the ground
truth is weaker in two registered ways: the stable items' L=false
holds partly BY CONSTRUCTION (only nonlocal readings were
vote-eligible there, per the locality2 registration's own scope
disclosure — eligibility descends from the LLM archive's votes), and
the contested items' L=false rests on shipped distinguishing pairs
plus author FAILS records, a challengeable claim class that has been
refuted twice (TLS 52, QUIC 235). A human tracking L is still not
being graded against raw LLM opinion — but the NO side inherits more
of the author's and the archive's mediation than the YES side, and a
strong HL1b result is correspondingly weaker evidence than a strong
HL1a result. What a strong result would
mean: the locality property is human-accessible semantics, not an
LLM-family convention — narrowing the author-constructed caveat from
the one direction no LLM measurement can reach. What it cannot mean:
the caveat closed (one human is one instrument, and the question text
is author-written — the mediation surface is one paragraph instead of
a codebook, disclosed below, but it is not zero).

**Relation to H1.** Sibling, not substitute. H1's packet, sample, and
floors stay frozen exactly as registered; nothing here amends them.
The two seats MUST be different people: an HL1 rater has seen 23
items from H1's corpus framed as a checkability question, and an H1 rater
has seen 60 items under the full instrument — each exposure
contaminates the other seat. Whichever runs first burns its rater for
the other.

## Instrument (the packet's question, quoted in full)

> Could a computer program decide whether this rule was followed by
> examining ONLY the complete calendar file it applies to — with no
> other information: no knowledge of what the file's author meant or
> intended, no other files or messages, no clock or calendar of
> real-world events, and no visibility into what any program or person
> actually did?

with two worked examples from a deliberately foreign domain (book
chapters; dictionary consultation) — one YES, one NO, neither sharing
vocabulary or domain with any item (the NO example deliberately
shares the producer-conduct SHAPE of several items — that shared
shape is what makes it a usable example, and it is part of the
mediation surface disclosed below). **Mediation disclosure:** the
question and examples are author-written, and their phrasing is the
channel by which the author's model of the property could steer the
rater. The exclusion list in the question ("intended", "other files",
"clock", "what any program or person actually did") names the same
context channels the studies use; a rater steered by that list toward
NO on conduct items is a real risk, accepted and disclosed — the
alternative (no guidance at all) measures reading comprehension of an
underspecified question rather than the property. The packet is
`packet-hl1.md`, frozen at this registration.

## Item set and ground truth (mechanical)

The 23 witnessed iCalendar items of `census/locality2/` — the only
items with constructive per-item L values in a genre a layperson can
read. Item selection was mechanical THERE (the corpus's entire
≥2-departure dissent mass plus the md5 stable sample); this
registration inherits the set unchanged. Ground truth: L(i) = "some
local rung (prop or object) witnessed among eligible readings",
derived from the shipped witness outcomes at `6ba6f9a`. The scorer
embeds the table AND re-derives it from the witness artifacts on every
run — drift is a hard failure.

**Cells** (every item in exactly one graded or reported cell):

- **A — local singles (6):** 63, 84, 143, 192, 193, 194. L = true.
- **B — nonlocal singles, non-exception (11):** 1, 7, 13, 69, 91,
  118, 146, 150, 200, 201, 210. L = false.
- **C — the exception trio (3):** 62, 77, 79. L = false, but the
  archived LLM vote-majority is ELIMINABLE on all three — the items
  where the formal criterion and the LLM boundary disagree.
- **D — the duplicate pair:** 43 and 79 are byte-identical corpus
  sentences. 43 is EXCLUDED from cell B (its text is identical to
  exception item 79, so grading it in B while 79 sits in C would
  double-count one sentence across cells); it is graded as a
  determinism control instead.
- **E — the two-rung pair (2, reported not graded):** 116, 185. Both
  carry a witnessed local rung AND a witnessed nonlocal reading —
  a genuinely two-sided sentence, so either answer is defensible and
  grading one as "correct" would be arbitrary.

## Predictions (append-only after push)

- **HL1a — cell A answered YES, floor ≥5/6.** The local singles
  include jargon-heavy but purely in-file checks (63's BYDAY/FREQ
  co-constraint); the floor allows one comprehension miss.
- **HL1b — cell B answered NO, floor ≥9/11.** Conduct, intent,
  generation, and global-uniqueness duties; the floor allows two
  misses (item 1's unfold-first ordering and item 7's language-variant
  guard are the named risks). A comprehension asymmetry is disclosed
  for the whole packet: several sentences carry unresolved
  antecedents from their corpus extraction ("the above requirement",
  "Such recurrence instances", "This property") which the witness
  pass resolved — via registered designations for "This property",
  and within its reading texts for the others — while the human
  resolves them blind; the sentences are served corpus-verbatim regardless, since
  completion is a quote defect in this repository.
- **HL1c — the exception trio answered YES, floor ≥2/3.** This
  clause grades the AUTHOR'S model of the human, and its direction is
  deliberate: the registered prediction is that the human sides with
  the LLM vote-majority AGAINST the formal criterion — that the pull
  of a datum-local trigger on a conduct- or world-guarded duty
  ("seconds value of 60", "rule parts that violate the above
  requirement") is shared human semantics, not an LLM artifact.
  **Both outcomes are informative and their interpretations are fixed
  now:** if HL1c passes, the archive's eliminable votes on these
  items track human surface reading, and the formal criterion is
  measuring something STRICTER than natural semantics — the
  exceptions are real divergences between natural reading and formal
  checkability, in humans too. If HL1c fails (the human sides with
  L), the trigger-pull is an LLM-population artifact and the formal
  boundary is the human-natural one — the strongest available
  evidence that L tracks human-accessible semantics. Neither outcome
  licenses relabeling anything.
- **HL1d — determinism control: answer(43) = answer(79), predicted
  PASS.** Byte-identical sentences, thirty-six corpus positions apart
  (five packet positions), unflagged in the packet. A human who answers them differently exhibits exactly
  the position noise the archive's E carries (locality2 finding 5) —
  which would itself be a finding, recorded as HL1d FAIL.
- **HL1e — reported only:** the two-rung items' answers, with no
  right answer registered.

**Degenerate strategies, measured before the floors were set** (the H1
discipline; the scorer's self-test re-measures them on every run):
all-YES scores 6/6 on HL1a and 3/3 on HL1c but 0/11 on HL1b — refused
by HL1b; all-NO scores 11/11 on HL1b but 0/6 on HL1a and 0/3 on HL1c —
refused by HL1a and HL1c; the seeded label-shuffle is refused by
HL1a/HL1b jointly; HL1d, a control rather than evidence, refuses no
constant strategy by construction. **Disclosed plainly: HL1c
structurally cannot refuse all-YES** (its predicted direction coincides with it); it is
guarded by HL1b, exactly as H1's clause pair guards its blind spots.
An overall raw-agreement-with-L number over the 21 graded items is
REPORTED and joins no series.

## Protocol

Recruit: a human who has never read this repository, recruited by the
owner; identity and a blindness attestation appended here as a marked
addendum BEFORE rating. One sitting, roughly 30 minutes, the packet
only — no lookups, no AI assistance, no discussion until answers are
returned as `NUMBER:YES`/`NUMBER:NO` lines (`?` marks a torn call).
One-shot: the packet is served once, to one pre-named rater; a second
seat may be ADDED before any rating occurs (both reported regardless —
the H1 two-seat symmetry) but never after a result is seen. The rater's returned lines
will be archived VERBATIM in the report and round-trip parsed by the
scorer before any push. Any deviation from these conditions — not
only unparseable or incomplete returns, but multiple sittings,
lookups, assistance, or discussion — is a protocol event, disclosed
in the report as such; nothing licenses a re-serve to the same
rater.

**Interpretation, pre-committed.** HL1a/HL1b grade whether the
witnessed boundary is recoverable by a non-LLM judge from the
sentences alone (the property-prior probe). HL1c grades the author's
model of where natural human reading parts from formal checkability.
HL1d is a control. Failures grade the author's model and the
property's human-accessibility — never the rater, never any archived
label, never the witnesses (which stand on their own artifacts). No
number here joins any census series, and no outcome here amends H1.

## Grading

`python3 census/human-locality/score_hl1.py labels.txt` — the scorer
ships frozen with this registration; its self-test verifies the
embedded L table against the witness artifacts, exercises the parse
rejections, re-measures the degenerate strategies, and fires
per-clause grading mutants on every run.

### [ADDENDUM 2026-08-20 — mechanical answer-leak guard added to the grader]

Append-only; the registration, packet, item set, clauses and floors above are
unchanged, and `packet-hl1.md` is byte-untouched.

The sibling registration H1 was found to carry a defect this packet does not: its
return-format examples named real graded items and gave each the archive's own
label (see `census/human/README.md`). **HL1 was never defective** — its examples use
8 and 104, which are genuinely outside this registration's 23 registered items, and
the packet states so explicitly ("Numbers in these two examples are arbitrary and do
not appear below").

But that protection was **prose**, and prose is not a guard. `score_hl1.py` now
carries `answer_leaks_in()`, checked in the self-test and negative-controlled three
ways: clean on the real packet; **fires** on a synthetic header carrying registered
items; and does **not** fire on this packet's own arbitrary example numbers.

The rule here differs from H1-R2's deliberately. H1-R2 removed numbers and class
tokens from its format spec entirely; HL1 keeps arbitrary numbers under its explicit
non-membership disclaimer. So this guard enforces **non-membership**, not absence —
copying H1-R2's rule here would fail on HL1's own compliant examples.

Scope, so it is not mistaken for coverage: it sees only the `NUMBER:YES/NO` shape,
and only before the item list. A prose leak, or a leak inside the item list, passes
silently.
