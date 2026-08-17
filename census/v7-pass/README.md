# v7 pass — registration (PUSHED BEFORE ANY RATER EXISTS)

First pass under instrument v7, over the three corpora the amendment
names: iCalendar (n = 225), TLS (n = 204), QUIC (n = 281). Six blind
passes (two raters per corpus, one per family), grading L1–L7 and
rule 23's per-pass clauses. v7 shares are a FIFTH version-labeled
series, never mixed with v3/v4/v5/v6 figures; the amendment's
direction-of-effect disclosure (committed at `70dddbe`) governs, and
its failure interpretation is restated at the bottom of this file.

## The instrument, served

`codebook/rater-pack-v7.md`, git blob
`a6f43218a92893fcd33444725809ed3a18ea6c1b` — the frozen v6 pack
(byte-identical prefix, asserted at build) + the standard section
heading ("CODEBOOK v7 RULES … apply together with everything
above") + rules 26 and 27, with
THREE disclosed elisions relative to the amendment's committed rule
bodies, all archive-referencing clauses (measurement provenance, not
classification content):

- **E1** rule 27's ", in the direction the archived readings
  settled" (the decision clause keeps "that decline is hereby
  decided").
- **E2** rule 27 wall (1)'s "(their archived evidence is mixed)".
- **E3** rule 27 wall (2)'s "; its archived evidence points
  TYPESTATE-ward, a different shape".

After elision the served v7 section contains **no item number, no
prediction name, and no pointer to unserved text** (asserted
mechanically at build). Every elided text remains verbatim in
`codebook/classes.md`; the exact removals are recoverable by diffing
the pack's v7 section against that file's rule bodies — both
committed.

## Rule-24 audits (run at registration, archived here)

**Settlement sweep — trigger (a), normalized ≥4-gram, run over ALL
items of all three corpora, for both the v7-ADDED text and the FULL
pack.** The v7-added text (rules 26 + 27 as served) hits **zero
items anywhere** — additionally swept at cut time against MLS,
RFC 9001, and RFC 9002 with zero hits. The full pack's whole-corpus
hits are all INHERITED text, served identically in the archived v6
passes, and the inventory matches the v6 registration's — plus two
inherited hits that inventory omitted, restored here from the
`census/v5-quic/` disclosure and this sweep: rule 25's
predicate vocabulary on TLS 14; rule 17's guard phrase on TLS
159/165; rule 18's worked example on TLS 181; rule 21's
history-conditioned clause on the QUIC quartet {11, 19, 261, 272};
the v3 base pack's DH example on TLS 101 (the one 4-gram hit inside
a stability set, noted at L7 below); rule 18's worked-example
phrase on TLS 133 and rule 19's PTO-expiry example on QUIC 69 (the
latter adjudicated and disclosed since `census/v5-quic/`, inherited
in every pass since); and generic short phrases ("a
client must not", "must not be sent", "the server's selected") on
scattered items, anchor-neutral. The sweep was self-tested with a
planted 4-gram and detected it.

**Trigger (b), distinctive identifiers/constants — one deliberate
delta, disclosed.** The v6 audit verified "precision" and "truncate"
ABSENT from the v6 pack; the v7 pack CARRIES both, in rule 26's body,
below the 4-gram threshold — they are item 150's characteristic
tokens, and the adjudication is made of them (disclosed at cut,
per the trigger-(b) precedent). This confirms rather than changes
L1's status: comprehension-by-construction, declared at cut.
"Stateless" and "disabled" occur in the pack only inside rule 25's
inherited scope wall ("a stateless operating mode, a disabled
feature"), served identically to both v6 raters; rule 27's added
text carries neither token. One further inherited identifier,
disclosed under the S49 convention (stability-set items are
prediction-named): the v4 seam text carries `ticket_lifetime ≤
604800` with an in-text rule-16 disposition — TLS 188's constant
and an L7-set item, adjudicated pass-ward in the served text,
inherited since the v4 pack and served identically in every pass
since (the TLS 101 parallel). No other named item's distinctive
identifier appears in the added text.

**L2 trigger audit — the cut's pre-flagged candidate FIRES.** The
served pack settles item 62 twice over: rule 25's "Grammar-invalidity"
(already ruled settling by the v6 registration's trigger-(c) ruling,
which this registration inherits) and rule 26's wall (1)
("Suppression of content VIOLATING a stated bound remains rule 21/25
branch-1 territory"). Per the amendment's own contingency, **L2
downgrades to a comprehension check**, and with L1/L3/L4/L5 declared
comprehension-by-construction at cut, **the discriminating load of
this registration falls entirely to L6, L7, and rule 23's per-pass
clauses.** All seven L-clauses are still graded and reported; the
downgrades bound what a pass certifies, exactly as J1–J4's did.

## Rule 23 instantiated (anchors, outside sets, floors, bounds)

Anchors per the amendment's stated default — the most recent archived
full pair per corpus, the **v6-series raters** (Av6/Xv6 for all
three). Outside set = all items no prediction names, including the
L5/L6/L7 enumerated sets (the S49 precedent): iCal excludes {62, 150},
the nine recognition items, and L6's 194 → **20 items** — exactly the
v6 registration's iCal outside set, {1, 2, 7, 37, 46, 47, 69, 77, 79,
118, 138, 141, 185, 192, 193, 194, 200, 201, 203, 204}; TLS excludes
{64} and L7's 56 → **147**; QUIC excludes 232 → **280**.

| corpus | outside n | 23(a) floor (= anchor-pair agreement) | 23(b) bound |
|---|---|---|---|
| iCal | 20 | match ≥ 19/20 | departures ≤ **0** |
| TLS | 147 | match ≥ 134/147 | departures ≤ **8** |
| QUIC | 280 | match ≥ 250/280 | departures ≤ **7** |

Bound construction, per precedent: the most recent archived
non-anchor pair, measured at registration against THESE anchors on
the outside set, smaller of the pair — iCal: Av5 0 / Xv5 0 → **0**
(a zero bound for the second consecutive iCal registration, this
time achieved by three archived raters, not one); TLS: Av5 8 /
Xv5 8 → **8**; QUIC: Aq5 7 / Xq5 11 → **7**.

**Measured failability (24 archived rater-corpus scores, every
branch exhibited; asserted by the shipped scorer's KAT on every
run).** Match / departures of every archived non-anchor full map
against the v6 anchors, outside set only:

- iCal — Ai 19/1 (PASSES (a) exactly at the floor, FAILS (b));
  Xi 15/5 (FAILS both); Av4i 20/0 (PASSES both); Xv4i 15/5 (FAILS
  both); Av5 20/0 and Xv5 20/0 (PASS both).
- TLS — Av5 136/8 and Xv5 138/8 and X 136/8 (PASS both, (b) exactly
  at the bound); Av4 139/7 and Xv4 142/4 (PASS both); D 131/14,
  G 127/17, M 127/18, K 120/25, Z 127/15 (all FAIL both).
- QUIC — Aq5 269/7 (PASSES both, (b) exactly at the bound); Xq5
  267/11 (PASSES (a), FAILS (b)); Av4 261/16 (PASSES (a), FAILS
  (b)); A2 242/34, B2 236/40, Xv4 243/33, Aq 231/45, Xq 226/47
  (all FAIL both).

## L-clauses, with measured branches

Frozen sets: L6's 194-item set and L7's 56-item set are re-derived
mechanically from the v6 registration's enumerations at every scorer
run; a mismatch is a protocol event. Measured values of every
archived rater on every clause (asserted by the KAT):

- **L1 (iCal 150 PROCESS):** pass exhibited by six archived raters,
  FAIL by Av5/Xv5 (DOMAIN).
- **L2 (iCal 62 DOMAIN; downgraded above):** pass by the four most
  recent raters, FAIL by the four pre-v5 (PROCESS).
- **L3 (TLS 64 PROCESS):** pass by nine archived raters, FAIL by
  Av5 (DOMAIN?), Xv5 (DOMAIN), Xv4 (TYPESTATE) — and by rater A's
  roster reading and rater B's derivable one (both DOMAIN, per the
  amendment's tally).
- **L4 (QUIC 232 PROCESS):** pass by six, FAIL by B″, Aq, Aq5, Xq5
  (DOMAIN).
- **L5 (the nine recognition items, 9/9 PROCESS):** pass by six,
  FAIL by Av5 (0/9) and Xv5 (5/9).
- **L6 (iCal 194-set, ≥193 DOMAIN):** all eight archived raters pass
  (Ai 193, Xi 193, Av4i 194, Xv4i 194 — the v4 anchors' 194s are BY
  CONSTRUCTION, the set being their DOMAIN intersection — Av5 194,
  Xv5 193, Av6 193,
  Xv6 193); FAIL branch by shuffle mutant (Fisher–Yates of Av6's
  iCal labels, seed `v7-mutant-ical`): **170/194, FAIL** — recorded
  as a number, not a promise.
- **L7 (TLS 56-set, ≥52 DOMAIN):** all eleven archived non-anchor
  raters pass, rater Z **exactly at the floor** (52; the others
  53–56, rater A's roster count the 53; the v4 anchors' 56/56 are
  by construction; the v6 anchors, measured on this v4-derived
  set: Av6 55,
  Xv6 56);
  FAIL branch by shuffle mutant (seed `v7-mutant-tls`): **24/56,
  FAIL**. The floor of 52 is the amendment's, derived over the
  enlarged archive (bound 4 = Z's measured count). The pack's one
  in-set 4-gram hit sits here: the v3 DH example on TLS 101,
  pass-ward for L7 on that one item, inherited since the first
  pass — as is the v4 seam text's in-text disposition abutting
  TLS 188 (trigger-(b) disclosure above).

## Steer ledger (rule-26/27-adjacent unpredicted items — the duty the amendment assigns)

Movement on these is licensed, unconstrained in direction, and MUST
be reported item-by-item — and every such flip still counts against
the rule-23 budgets as an ordinary outside-set departure (the v6
rule, restated: the ledger creates a reporting duty, never an
excuse; iCal 203 sits under the zero bound like every other
outside-set item). The items: the declined designated-field
value-ignores
TLS 60 and QUIC 203/214; the declined compound TLS 54 and conjoined
QUIC 32; the history-conditioned QUIC quartet {11, 19, 261, 272} and
item 269 (rule 27 wall (2) declines them); QUIC 231 (rule 27's
vocabulary is adjacent — a randomized-disabling duty, U/THRESHOLD
family in ten archived readings, not a suppression duty); iCal 203
and QUIC 194 (each carries a "truncate" token — iCal 203 is a
truncation PROHIBITION, QUIC 194 a sender-side encoding duty;
neither is rule 26's acceptance-with-license shape).

## Raters (pre-registered per rule 24; a differing serving model is a protocol event)

- **Av7 (each corpus):** fresh same-family instance,
  `claude-fable-5`, via the Agent tool; single input file per corpus
  (pack + full corpus), blind — no census artifacts, no label
  archives, no expectations; one-read attestation required.
- **Xv7 (each corpus):** foreign `cursor-grok-4.6-high-fast` via
  cursor-cli (`cursor-agent --print --output-format text --mode ask
  --trust`, binary 2026.08.11-e8db854, verified). Chunk partitions
  pinned identical to every prior pass: iCal 1–51 / 52–102 /
  103–153 / 154–204 / 205–225; TLS 1–51 / 52–102 / 103–153 /
  154–204; QUIC 1–51 / 52–102 / 103–153 / 154–204 / 205–255 /
  256–281.
- No author rater. Malformed-label handling, torn-flags, and the
  label-U-vs-event-U distinction exactly as in
  `census/v5-quic/README.md`. Labels extracted mechanically, archived
  verbatim, round-trip parsed before push.

## Scoring

`score_v7.py` (shipped here) is the only grader. Its KAT re-derives
the frozen sets and outside sets, re-scores all 24 archived
rater-corpus cells against the v6 anchors asserting the tables above
exactly, and exhibits the L6/L7 mutant fail branches. Watched to
fail before registration: a perturbed KAT expectation fails at the
perturbed rater. The CLI path rejects any duplicate item label; the
archive path raises on adjacent duplicates and relies on the
per-rater completeness asserts for the rest (a non-adjacent repeat
is indistinguishable from a new rater block by index alone —
stated so the guarantee is not overclaimed).

## Owed observations (report duties, restated per the v6 precedent)

The report MUST carry: full departure lists per rater-corpus cell
(item and both labels, not counts alone); the L1–L5 item histories
extended (the recognition family and both J4 items, all archived
readings plus v7's); the steer-ledger items item-by-item; per-class
distributions and shares (v7 series only, never mixed); torn
counts; protocol events including malformed-label retries; and both
raters' labels archived verbatim, round-trip parsed before push.

**Failure interpretation, restated from the amendment:** L-clause
failures grade rules 26/27's texts and the author's model of their
reach — no re-rating, no relabeling, no substitution of any earlier
series' figure. Rule 23 failures are per-pass calibration verdicts
on the author's registered model, as v6's TLS cell demonstrated.
Share movement beyond the amendment's direction disclosure is
evidence of instrument mis-design, not a new result.
