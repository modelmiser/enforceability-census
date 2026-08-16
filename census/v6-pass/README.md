# v6 rating pass — registration (PUSHED BEFORE ANY v6 RATER EXISTS)

Scope: the first v6 pass, covering the three corpora rule 25 touches —
**iCalendar (RFC 5545 §3, n = 225), TLS (RFC 8446 §4, n = 204), QUIC
(RFC 9000 §2–19, n = 281)** — as ONE registration per the
`census/v5-completion/` precedent: six blind passes (two raters per
corpus), grading J1–J6 plus rule 23 instantiated per corpus. RFC 9001,
9002, MLS, and Wayland are NOT rated in this pass; rule 25's
rule-level reach on them stays the amendment's disclosed,
rule-23-bounded statement, ungraded here. This registration is
committed and pushed before any rater is commissioned; a v6 result
never replaces any earlier series' figure.

## The instrument

Pack: `codebook/rater-pack-v6.md`, git blob
`f4f9e0b1c478cc05370e8b4ba7f612320698d8f0`, committed with this
registration. Recipe: the v5 pack (blob
`694e3a9efab29252a815b00150a8c3ecf83a90b6`, byte-identical prefix) +
one appended section headed exactly `## CODEBOOK v6 RULES (2026-08-16)
— apply together with everything above` + rule 25's body from
`codebook/classes.md`, verbatim except seven elisions (E1–E7), each
removing text and rewording nothing:

- **E1** ` (the shape of Z4's settled TLS conjunct)` — names a
  prediction.
- **E2** ` — TLS 64, QUIC 232` — item numbers in the mode/state
  clause (the parenthetical's generic description is retained).
- **E3** the history-conditioned parenthetical naming the quartet
  {11, 19, 261, 272}, QUIC 269, and the v5 partial ruling — item
  numbers plus a pass pointer (the v5 dangling-pointer precedent).
- **E4** the designated-field parenthetical naming QUIC 203/214 and
  TLS 60 with an evidence gloss and a pointer to unserved motivation
  text.
- **E5** ` (QUIC 32)`; **E6** ` (TLS 54)` — item numbers.
- **E7** the two protocol-facing closing sentences of scope wall (2)
  (rule-23 budget mechanics and the registration steer-ledger duty —
  measurement protocol, not classification content).

After elision the served v6 section contains **no item number, no
prediction name, and no pointer to unserved text** (asserted
mechanically at build). Every elided text remains verbatim in
`codebook/classes.md`; the exact removals are recoverable by
diffing the pack's v6 section against that file's rule-25 body —
both committed.

## Rule-24 audits (run at registration, archived here)

**Settlement sweep — trigger (a), normalized ≥4-gram, run over ALL
items of all three corpora (the v5-completion whole-corpus
standard), for both the v6-ADDED text and the FULL pack.** The
v6-added text hits exactly one item anywhere: TLS 14 (`does not
recognize support`, rule 25's predicate vocabulary). All sixteen
other prediction-named items (TLS 18/84/141/191; iCal
13/16/22/25/27/28/91/146/210; QUIC 61; iCal 62/150): no hit. The
full pack's remaining whole-corpus hits are all INHERITED v5-base
text, served identically in the archived v5 passes: rule 17's
guard phrase on TLS 159/165 and rule 18's worked example on TLS 181
(both disclosed and discounted in prior passes), rule 21's
history-conditioned clause on the QUIC quartet {11, 19, 261, 272}
(the v5-quic disclosure, no label direction), the v3 base pack's DH
example on TLS 101 — the one hit inside a stability set, noted at
J6 below — and generic short phrases ("a client must not", "must
not be sent", "the server's selected") on scattered items,
anchor-neutral. The sweep was self-tested with a planted 4-gram and
detected it.

**Trigger (b), distinctive identifiers/constants.** No named item's
distinctive identifier appears in the pack (checked: x-param,
iana-param, x-comp, iana-comp, x-name, iana-token, the five fallback
value names, RECUR, precision, truncate, unrecognized extensions,
cipher suites, certificate-extension OIDs, transport parameters). One
candidate examined and dismissed: the word "private" occurs in the
pack only inside rule 11's v3-era wire-falsifiability text
("endpoint's private state") — a different sense, not item 146's
PRIVATE fallback identifier; it was served unchanged to all four
pre-v5 iCal raters, whose archived readings of 146 were PROCESS (the
two v5 raters, served the same text, read 146 DOMAIN — the rule-21
drift the amendment records, not a "private" steer). Two further
single-token overlaps in the v6-added text, disclosed the same way:
"unrecognized" (in the generated-binding sentence) is the selector
word of TLS 18/141/191, and lowercase "unknown" (scope wall 1) abuts
iCal 16's UNKNOWN value name — both are single words, not phrases,
and both predictions they could touch (J1, J2) are already
comprehension checks by construction.

**Trigger (c), paraphrase — adjudicated by this registration's cold
reviewer (the registration gate's fresh lens), residual judgment
resolving toward downgrade, per the amendment's pre-flag.** Two
candidates put to the reviewer: rule 25's `a stated bound` against
iCal 150's precision trigger (pre-flagged at cut), and
`Grammar-invalidity` against iCal 62's
parts-that-violate-a-stated-requirement trigger. RULING, recorded
verbatim from the gate before this file was pushed:

> TRIGGER-C RULING: fires on both — J4 is downgraded to a
> comprehension check. Ground: Each candidate phrase names a trigger
> category whose live extension in the iCal corpus is exactly one
> item — 150 is the corpus's only bound/precision-triggered
> tolerance duty (203's "at least 255 octets" duty is a
> receive-and-persist capability, not a suppression trigger), and 62
> is its only validity-triggered suppression of an arriving
> in-grammar object (69's ignored instances are locally computed,
> outside rule 21's ambit by the amendment's own record) — and the
> served rule states the branch-1 DOMAIN disposition for those
> categories in-text, which is J4's predicted label. Under the
> series' own standard a served phrase mapping to one corpus item
> settles rather than discriminates: v5-quic fired trigger (c) on "a
> malformed or too-small packet" for exactly this shape, and
> v5-completion held "an extension" categorical only because it
> reached eleven items. The residual step a rater must supply for 62
> — reading "violate the above requirement" as "Grammar-invalidity"
> — is a single abstraction, and residual judgment resolves toward
> downgrade.

Per the amendment's own pre-commitment, the discriminating load now
rests entirely on J5, J6, and rule 23. J4 is still graded and
reported, weighted as a comprehension check.

**Prediction status at registration:** J1, J2, J3 — comprehension
checks BY CONSTRUCTION (cut-time declaration; trigger (a)'s TLS 14
hit is consistent with, and adds nothing to, that status). J4 —
comprehension check (trigger (c), ruling above). J5, J6 —
discriminating (set-bounds contradicting no archived rater). Rule 23
— discriminating, instantiated below.

## Rule 23 instantiated (anchors, outside sets, floors, bounds)

Anchors per the amendment's stated default — the most recent archived
full pair per corpus, the **v5-series raters**: iCal Av5/Xv5 and TLS
Av5/Xv5 (`census/v5-completion/`), QUIC Aq5/Xq5 (`census/v5-quic/`).
Outside set = all items no prediction names, **including the items
J5/J6 enumerate** (the `census/v5-quic/` S49 precedent: an
aggregate-set prediction's items are prediction-named): iCal
excludes the 11 J2+J4 items AND J5's 194, leaving 20; TLS excludes
the 5 J1 items AND J6's 56, leaving 143; QUIC excludes item 61,
leaving 280. (This registration's first draft excluded only the
point-named items — the gate corrected it to the precedent before
push; the bounds below were unchanged by the correction.) The iCal
outside set is thereby exactly the corpus's residual soft mass,
enumerated: {1, 2, 7, 37, 46, 47, 69, 77, 79, 118, 138, 141, 185,
192, 193, 194, 200, 201, 203, 204}. Label normalization for all
scoring: torn flag `?` stripped, base label governs; U ≡
UNCLASSIFIED, NEG ≡ NEGOTIATION, CV ≡ CRYPTO-VERIFY.

| corpus | outside n | 23(a) floor (= anchor-pair agreement) | 23(b) bound |
|---|---|---|---|
| iCal | 20 | match ≥ 19/20 | departures ≤ **0** |
| TLS  | 143 | match ≥ 134/143 | departures ≤ **6** |
| QUIC | 280 | match ≥ 251/280 | departures ≤ **22** |

Bound construction, per the `census/v5-quic/` precedent: the most
recent archived non-anchor pair, measured at registration against
THESE anchors on the outside set, taking the smaller of the pair —
iCal: Av4i 0 / Xv4i 5 → **0**; TLS: Av4 10 / Xv4 6 → **6**; QUIC:
Av4 22 / Xv4 44 → **22**. The iCal bound of zero is deliberate and
stated plainly: the amendment enumerated the tolerance family and
licenses no other iCal movement, so ANY outside-set both-anchor
departure is the tripwire firing — the conviction corpus gets the
harshest bound in the series, and it is an achieved, measured count
(Av4i's).

**Measured failability (every clause can fail, and archived raters
exhibit both branches).** Match counts and departures of every
archived non-anchor full map against these anchors, outside set only:

- iCal — Av4i 20/20, 0 dep (PASSES both, (b) exactly at edge); Ai
  19/20, 1 dep {79} (PASSES (a) exactly at edge, FAILS (b)); Xv4i
  15/20, 5 dep {77, 79, 192, 193, 194} (FAILS both); Xi 15/20, 5
  dep {141, 192, 193, 194, 203} (FAILS both).
- TLS — Av4 133/143, 10 dep (FAILS both); Xv4 137/143, 6 dep
  (PASSES both, (b) exactly at edge); D 121/143, 22 dep; G 126/143,
  17 dep; X 126/143, 17 dep (all three FAIL both).
- QUIC — Av4 258/280, 22 dep (PASSES both, (b) exactly at edge);
  Xv4 236/280, 44 dep; Aq 227/280, 53; Xq 227/280, 53; A″ 235/280,
  45; B″ 239/280, 41 (all five FAIL both).

The scorer is known-answer-tested on these fifteen archived
rater-corpus scores — they exhibit every PASS branch, every FAIL
branch, and four exact-edge cases (Ai at the iCal (a)-floor; Av4i,
Xv4-TLS, and Av4-QUIC at their (b)-bounds) — before any live rater
is scored.

## J5/J6 stability sets (enumerated mechanically, archived here)

**J5 (iCal): both-anchor DOMAIN set of Av4i/Xv4i, |S| = 194; pass =
≥ 193 DOMAIN per v6 rater.** Items (derived mechanically from
`census/v4-ical/rfc5545-v4pass.md`, round-trip verified, re-derived
by the scorer at grading — a mismatch is a protocol event): 3–6,
8–12, 14–15, 17–21, 23–24, 26, 29–36, 38–45, 48–61, 63–68, 70–76,
78, 80–90, 92–117, 119–137, 139–140, 142–145, 147–149, 151–184,
186–191, 195–199, 202, 205–209, 211–225. The archives contain no
torn label among them. Measured non-DOMAIN counts against S: Ai 1,
Xi 1, Av5 0, Xv5 1 (bound 1, per the amendment).

**J6 (TLS): both-anchor DOMAIN set of Av4/Xv4, |S| = 56; pass = ≥ 53
DOMAIN per v6 rater.** Items (same derivation discipline, from
`census/v4-tls/rfc8446-s4-v4pass.md`): 11–13, 15–16, 19–21, 26–28,
36, 48–51, 66, 68–74, 77–78, 85–86, 88, 90, 92–93, 101–105, 107,
110, 131–132, 136, 140, 150–151, 153–156, 158, 168–169, 176–177,
188, 201. Measured non-DOMAIN counts: A 3, D 1, G 2, X 1, Av5 2,
Xv5 2 (bound 3, per the amendment; rater C excluded per its
report's invalid-instrument status, count 2, bound unchanged). One
base-pack steer inside this set, disclosed per the S49 precedent:
the v3 pack's DH worked example shares a 4-gram with item 101
("1 < Y < p-1") — inherited since the first pass, pass-ward for J6
on that one item.
(A first draft of this registration hand-typed both enumerations and
got both wrong; the lists above replaced them from the mechanical
derivation before this file was ever pushed — recorded because the
defect class is the registry's own.)

## Raters (pre-registered per rule 24; a differing serving model is a protocol event)

- **Av6 (each corpus):** fresh same-family instance,
  `claude-fable-5`, via the Agent tool; single input file per corpus
  (pack + full corpus), blind — no census artifacts, no label
  archives, no expectations; one-read attestation required.
- **Xv6 (each corpus):** foreign `cursor-grok-4.6-high-fast` via
  cursor-cli (`cursor-agent --print --output-format text --mode ask
  --trust`), verified installed (2026.08.11-e8db854) before this
  registration. Chunk partitions pinned identical to every prior
  pass: TLS 1–51 / 52–102 / 103–153 / 154–204; iCal 1–51 / 52–102 /
  103–153 / 154–204 / 205–225 (preserving the {43, 79} cross-chunk
  geometry); QUIC 1–51 / 52–102 / 103–153 / 154–204 / 205–255 /
  256–281.
- No author rater. Malformed-label handling, torn-flags, and the
  label-U-vs-event-U distinction exactly as in
  `census/v5-quic/README.md`.
- Labels extracted mechanically from transcript/chunk outputs (zero
  hand transcription); archived label blocks are round-trip parsed
  before push (wrap with hyphen-breaking disabled — the
  CRYPTO-VERIFY lesson).

## Steer ledger (rule-25-named unpredicted items — the duty the amendment assigns)

After elisions the served pack names ZERO item numbers; what remains
are generic shape descriptions (mode/state-conditioned;
history-conditioned; designated-field value-ignores; conjoined
triggers; compound-sentence subordinate clauses) plus the v5 pack's
previously disclosed steers (rule 21's ICMP naming; the two v5
elisions), all carried unchanged. The items those shapes describe —
TLS 64, 60, 54; QUIC 203, 214, 232, 32, 269; the quartet {11, 19,
261, 272} — therefore receive no label-direction steer from the v6
addition (the round-2 amendment gate moved their label histories out
of the rule body for exactly this reason). REPORT DUTY: the report
settles this ledger — it archives every listed item's v6 labels,
states each item's movement relative to the anchors, and counts
every flip against the rule-23 budget as ordinary outside-set
departures.

## Owed observations (report duties beyond the grades)

1. Full label tables for the recognition family (J1/J2/J3 items plus
   iCal 37), the J4 pair, and every steer-ledger item, against their
   archived histories.
2. iCal {43, 79} (the stably liminal cross-chunk pair), 141, 203,
   185; TLS guard-mass {65, 123, 184} and 156.
3. Clause 23(c): full both-anchor departure lists and per-class
   deltas with explicit zeros, per corpus.
4. Shares quoted as a v6 series only; every v3/v4/v5 headline
   stands; the amendment's direction disclosure is the yardstick —
   movement beyond it is the mis-design verdict, restated.

**Failure interpretation (restated from the amendment, binding
here):** grades measure rule 25's text and the author's model of its
reach. A failed clause licenses NO re-rating, NO relabeling of any
archived pass, NO substitution of a v6 number for any earlier
series' figure, and NO rewording within v6.
