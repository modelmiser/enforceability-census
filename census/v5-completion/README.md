# v5 completion passes — TLS, RFC 9001, iCalendar (pre-pass protocol; no rater has run)

2026-08-16 · **Status: registered BEFORE any rater; every graded clause
fixed at this commit.** Append-only after push; corrections, if ever
needed, are appended in dated brackets. Companion to
`census/v5-quic/` (the first v5 pass) and the v5 amendment
(`codebook/classes.md`, rules 20–24, predictions Z1–Z7).

## Why this pass

Completing the v5 grading: Z2 (TLS 67), Z3 (RFC 9001 item 15 — the
amendment's disclosed contested-bridge prediction), Z5 (iCal
192–194), and the TLS conjunct of Z4 (item 156), which — the QUIC
conjunct having passed — settles **Z4 overall**. Six blind rating
passes: per corpus, a fresh same-family instance and the foreign
rater, both pre-registered by model name below.

**Steer taxonomy, stated up front (the mechanical audits are below).**
All of Z1–Z5 were declared comprehension checks BY CONSTRUCTION at
cut time, and that declaration governs every grade's evidential
weight. The mechanical audits of the SERVED pack nonetheless
partition this pass's predictions three ways: **mechanically steered**
— Z2 (rule 20's body serves item 67's adjudication near-verbatim:
"the absence of a required element in a prior flight … TYPESTATE")
and Z3 (rule 20's bare-event branch serves item 15's shape: "any
alert, any close signal", "a closure alert"); **mechanically clean** —
Z4-TLS (the served pack nowhere names status_request_v2 or item 156's
content; rule 21's "an extension" is generic) and Z5 (the served pack
contains ZERO shared n-grams with the iCal corpus at 6/5/4-gram
levels and no distinctive identifier of items 192–194 — the apparent
"DATE" hit is a substring artifact of "validate"). The
mechanically-clean pair, plus the six rule-23 clauses, are where this
pass can genuinely fail; Z5's foreign half additionally requires
overturning six archived foreign-family TYPESTATE readings (two
foreign raters × three items, across both instrument versions) from
rule text alone — the strongest transmission test among Z1–Z5.

## Instrument, corpora, raters

- **Pack:** `codebook/rater-pack-v5.md`, blob `694e3a9…`,
  byte-identical to the v5-quic serving; hash round-trip verified at
  serve time; served blind (no predictions, no archived labels).
- **Corpora, byte-identical to their censuses:**
  `census/tls13/rfc8446_s4_musts.txt` (n = 204),
  `census/quic-tls/rfc9001_s4-8_musts.txt` (n = 69),
  `census/ical/rfc5545_s3_musts.txt` (n = 225).
- **Raters, models pre-registered (names govern; a differing serving
  model is a protocol event):** per corpus, rater **Av5** — fresh
  same-family instance, `claude-fable-5`, single input file (pack +
  corpus), blind; rater **Xv5** — foreign `cursor-grok-4.6-high-fast`
  via cursor-cli. Chunk partitions pinned: TLS 1–51 / 52–102 /
  103–153 / 154–204 (identical to every prior TLS chunked pass);
  iCal 1–51 / 52–102 / 103–153 / 154–204 / 205–225 (identical to
  both prior iCal passes, preserving the {43, 79} cross-chunk
  geometry); RFC 9001 1–35 / 36–69 (prior passes pinned only "2
  chunks ≤ 51"; the exact bounds are pinned here for the first time).
- Malformed-label handling, torn-flags, and the label-U-vs-event-U
  distinction exactly as in `census/v5-quic/README.md` (event-U is
  failure-ward for every graded clause of this pass too; a
  well-formed rater-emitted U is a label and matches an anchor U).

## Rule-24 audit results (run at registration, archived here)

Settlement sweeps (pack vs corpus, case/punctuation-normalized
n-grams) and identifier scans over ALL items of each corpus (the
v5-quic lesson: scan the outside set, not just predicted items).
Hits partition into v4-pack-inherited (text the anchor raters
already saw — anchor-neutral for rule 23) and v5-added:

- **TLS:** whole-pack hits at 6/5-gram: item 181 only — the v4
  pack's rule-18 example quoting it, inherited. 4-gram whole-pack
  residue {101, 114, 127, 129, 133, 159, 165, 181}: all inherited
  v4-pack text or generic modal phrases; the only v5-ADDED 4-grams
  are generic ("a client must not" on 114, "must not attempt to" on
  133) — adjudicated non-settling by the standing phrase-frequency
  reasoning. Categorical vocabulary, quantified so "clean" is
  checkable: rule 21's ignore/do-not-act-upon shape reaches at least
  eleven TLS items (14, 18, 54, 60, 64, 84, 89, 122, 141, 156, 191),
  and "an extension" is corpus-pervasive — a steer on a class that
  large is categorical, not item-distinctive (contrast v5-quic's
  "too-small packet", which mapped to one item); its direction where
  it points at all is DOMAIN, bounded by clauses (a)/(b). One
  v5-added ITEM steer, disclosed: **item 175**
  (outside set) — rule 22 names "TLS's
  CertificateVerify-to-Certificate compatibility duty" and states
  its archived TYPESTATE reading is "preserved, not flipped";
  direction anchor-ward (both anchors TYPESTATE), i.e., pass-ward
  for clause (a) on one item.
- **RFC 9001:** whole-pack 6/5-gram hits {14, 18, 21, 34, 43} are
  the v4 pack's rule-18/19 quoted examples — inherited. Item 34's
  text also appears verbatim in the v5 pipeline's rule-18 guard
  example; since the v4 pack already quoted it near-verbatim, the
  steer is substantially inherited (anchors read 34 TYPESTATE, both;
  direction anchor-ward). 4-gram residue {32, 38, 69}: 38/69 share
  only "a client must not"; item 32's gram is "frames that do not" —
  a fragment of rule 21's undecided-residue clause, named here
  rather than bundled as generic (item 32's own phrase, "frames that
  do not carry application data," is semantically unrelated, and the
  clause's steer direction is "no label").
  Outside-set items containing the word "alert" — {40, 59, 60, 64,
  66} (anchor labels NEG/NEG, NEG/NEG on 59/60; DOMAIN/DOMAIN on
  40/64; DOMAIN/TYPESTATE on 66) — are noted because rule 20's
  bare-event branch names alerts generically; no item-specific
  content of theirs is served.
- **iCalendar: zero hits.** No shared 6/5/4-gram between the served
  pack and any of the 225 items; no distinctive identifier of any
  iCal item occurs in the pack (the scan's one apparent hit, "DATE,"
  is a substring artifact of "validate"/"outdated"; the standalone
  word count is zero). The served instrument contains no
  iCal-specific settling text at all.

## Rule 23 instantiated per corpus (anchors, floors, bounds — frozen here)

Anchor pairs are rule 23's default in each case — the most recent
archived full pair under v4, the version nearest v5 — with agreement
recomputed here from their archived label blocks. Bounds take the
smaller of the two measured cross-pass departure counts (the
convention set at `census/v5-quic/`), from the most recent prior
archived pair of each corpus (TLS: the foreign pair G/X; RFC 9001:
the census pair A‴/B‴; iCal: the census pair Ai/Xi).

| corpus | anchors | outside set | 23(a) floor (match ≥) | measured failability | 23(b) bound (departures ≤) | measured cross-pass departures |
|---|---|---|---|---|---|---|
| TLS | Av4/Xv4 (`census/v4-tls/`) | 202 (named: 67, 156) | **187/202** (92.6%) | G scores 179 — fails; X scores 190 — passes | **12** | G 23, X 12 |
| RFC 9001 | Av4/Xv4 (`census/v4-completion/`) | 68 (named: 15) | **65/68** (95.6%) | BOTH v3 raters fail (A‴ 56, B‴ 62) — the only floor in the series no measured prior rater clears | **6** | A‴ 12, B‴ 6 |
| iCal | Av4i/Xv4i (`census/v4-ical/`) | 222 (named: 192, 193, 194) | **219/222** (98.6%) | Ai scores 221 — passes; Xi scores 219 — passes exactly at the floor | **1** | Ai 1, Xi 3 |

iCal's bound of 1 is the tightest in the series and is deliberate: a
v5 rater producing two or more readings outside both anchors' labels
on 222 items fails 23(b) — making this cell a live overreach test
for rule 22, whose format-genre reach the amendment disclosed as
agreement-ward. Clause (c) as at v5-quic: full both-anchor departure
lists and per-class deltas with explicit zeros, plus both owed
metrics (match-vs-anchors AND role-matched agreement) per rater.

## Graded clauses (per rater, integers restated)

| clause | corpus | pass condition per rater | audit status |
|---|---|---|---|
| Z2 | TLS | item 67 = TYPESTATE | comprehension check (cut-time + mechanically steered) |
| Z4-TLS conjunct | TLS | item 156 = DOMAIN | comprehension check by cut-time declaration; mechanically CLEAN |
| Z3 | RFC 9001 | item 15 = TYPESTATE | comprehension check (cut-time + mechanically steered); rests on rule 20's disclosed contested bridge — a Z3 failure grades the bridge first |
| Z5 | iCal | items 192 ∧ 193 ∧ 194 = DOMAIN | comprehension check by cut-time declaration; mechanically CLEAN — foreign half must overturn 6 archived foreign TYPESTATE readings |
| 23(a)/23(b) | each | per the table above | discriminating, all six |

**Z4 overall** is settled by this registration's TLS conjunct: the
QUIC conjunct passed in both `census/v5-quic/` raters, so Z4 overall
PASSES iff item 156 = DOMAIN in both TLS raters here, and FAILS
otherwise — no discretion remains.

## Owed observations (explicit outcomes, including zeros)

1. **TLS:** labels on the v4-split guard residue {65, 123, 184}, on
   item 22 (the shared unpredicted v4 flip), and on item 175 (the
   disclosed steer item); a label table over {22, 65, 67, 123, 156,
   175, 184} across Av4, Xv4, and both new raters.
2. **RFC 9001:** the four-version history of item 15 stated in full
   beside its grade; labels on the V5 lifecycle split items — {13,
   34, 36, 37, 38} (TYPESTATE side) and {14, 18, 20, 43} (PROCESS
   side) — with an explicit statement whether the 5/4 split holds,
   and a table over those nine plus item 15.
3. **iCal:** labels on {43, 79} (the stably liminal cross-chunk
   pair — observation only, no grade), on 185 (the foreign v4
   ordering-class departure), and on 141/203 (the v3 splits that
   closed under v4 — do they stay closed?); a table over {43, 79,
   141, 185, 192, 193, 194, 203}.
4. Eliminable shares per rater per corpus, quoted only as the v5
   series. Named-item line-crossing accounting, restated from the
   amendment: at most +1 eliminable item on RFC 9001 (Z3 against
   Xv4's PROCESS reading); zero on TLS (Z2 interior; Z4-TLS matches
   both anchors) and zero on iCal (Z5 interior — DOMAIN vs
   TYPESTATE, both eliminable).

## Ring-fence and failure interpretation

Every archived headline stands: TLS 80–83% (v3 range) and the
v4-series 81.9/82.8; RFC 9001 54–67% (v3) and 60.9/58.0 (v4); iCal
88.0/88.4% (v3) and 88.9/88.0 (v4). This pass's shares are quoted
only as "v5 instrument series." Failed clauses grade the v5 rule
texts and the author's model of their reach; they license NO
re-rating, NO rewording within v5, NO retroactive relabeling, NO
exclusion of any valid-instrument rater. Deviations recorded with
reasons, never argued into compliance. Direction disclosure: the
instrument-friendly outcome is high anchor agreement with all Z
clauses holding; the mechanically-clean tests (Z4-TLS, Z5) and the
six rule-23 clauses — including iCal's single-departure bound — are
where this pass can fail against un-steered content, and Z3 can fail
against a steered one (its prediction sides with one archived
reading in four even with the steer).
