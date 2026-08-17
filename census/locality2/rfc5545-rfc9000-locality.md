# Second locality passes: the correspondence generalizes, and its exceptions are class-shaped

2026-08-17 · Witness pass for the `census/locality2/` registration
(pushed at main `8821bce` before construction). Grader:
`python3 census/locality2/check_witnesses2.py`. **Status: COMPLETE —
all six iCalendar clauses and all seven QUIC clauses PASS; 71 of the 72
item outcomes matched their registered predictions exactly; the 22
pre-named correspondence exceptions realized 22/22 with zero unnamed
mismatches. The one miss is itself an event: the gate's cold reviewer
REFUTED a recorded FAILS entry (item 235, pre-push) by constructing
the pkt validator it denied — the challenge mechanism's second firing
in two studies, both against the author's own impossibility
ledger.**

## What this is and is not

As with the first study: the artifacts — 77 witnesses and 24 recorded
construction failures across `witnesses_ical.py` and
`witnesses_quic.py` (a 25th record was refuted at the gate and stands
withdrawn in place) — are the product. Every validator executes, every
pair carries its quotes, and a reader who disputes a reading attacks
its quote directly; a reader who ships an artifact a FAILS record
declares unconstructible refutes that record (that interface fired once
in the first study). The grades measure the internal consistency of one
semantic model with the archive; they are not inter-rater statistics,
and **no number here joins any census series.** A near-perfect sheet
should be read with exactly the right suspicion: the author wrote both
the predictions and the witnesses, unblinded. What the sheet cannot
fake is the artifacts' own checkability — the registration's riskiest
calls (QC2's predicted-EMPTY outcome for a unanimously
eliminable-voted item; IC5's requirement that a mismatch land on one
specific half of a byte-identical sentence pair) were the places it
could have visibly broken, and the one place it DID break was broken
by a reader exercising the designed challenge interface (finding 7).

## Grades

| clause | registered floor | result |
|---|---|---|
| IC1 stable DOMAIN per-item {63 prop, 84 prop, 143 object} | 3/3 strict | **PASS** 3/3 |
| IC2 stable PROCESS+U → {nonlocal} | 6/6 strict | **PASS** 6/6 |
| IC3 contested single-rung exact | ≥10/12 | **PASS** 12/12 |
| IC4 contested multi-rung {116, 185} | 2/2 strict | **PASS** 2/2 (exact sets 2/2) |
| IC5 duplicate-text control (43, 79) | mechanical | **PASS** — equal outcomes; mismatch on 79 alone |
| IC6 correspondence | 0 unnamed, ≥2/3 named | **PASS** — 0 unnamed, 3/3 named |
| QC1 stable DOMAIN → {pkt} | 3/3 strict | **PASS** 3/3 |
| QC2 stable TYPESTATE {171 conn, 78 conn, 58 **empty**} | 3/3 strict | **PASS** 3/3 |
| QC3 stable NEG/POLICY/PROCESS/U → {nonlocal} | 9/9 strict | **PASS** 9/9 |
| QC4 stable THRESHOLD → {conn} | 3/3 strict | **PASS** 3/3 |
| QC5 contested single-rung exact | ≥24/28 | **PASS** 27/28 — the miss is 235, whose outcome gained the refuted record's pkt rung |
| QC6 contested multi-rung {152, 162, 144} | ≥2/3 | **PASS** 3/3 (exact sets 3/3) |
| QC7 correspondence | 0 unnamed; families ≥13/16 and ≥2/3 | **PASS** — 0 unnamed, 16/16 and 3/3 |

Witness counts: iCalendar 25 entries + 9 FAILS; QUIC 52 entries + 15
FAILS (plus the withdrawn 235 record, preserved as a comment). FAILS
coverage is checker-enforced: every registered eligible rung is
witnessed or carries a challengeable impossibility record.

## Findings

**1. The correspondence generalizes — and its failure rate is
genre-shaped while its failure SHAPE is class-shaped.** Three corpora,
one criterion: "some local rung witnessed" vs "eliminable-vote
majority" now diverges on 4/44 TLS items (first study), 3/23 iCalendar
items, and 19/49 QUIC items — every divergence pre-named, none
unnamed, across 116 witnessed items in three genres. The rates are not
comparable as measurements (the three contested selections run at
different depths — TLS d≥4 of 14, iCalendar d≥2 of 10, QUIC d≥5 of 12,
per the registration's disclosure), but the structural claim survived
its two hardest tests: where the archive's headline boundary and the
formal property part ways, they part along families predictable from
sentence structure, never item-by-item noise.

**2. QUIC's headline boundary systematically UNDERCOUNTS locality: the
THRESHOLD family is conn-local by construction.** Sixteen items —
the thirteen contested limit items plus THRESHOLD-unanimous 94, 83,
and 62 — carry checks whose quantity and bound are both conn-carried
(advertised limits travel in transport parameters and MAX_* frames;
cumulative counts are transcript sums). All sixteen produced conn
validators; all sixteen sit on the non-eliminable side of the
archive's DOMAIN+TYPESTATE line. The THRESHOLD-vs-TYPESTATE fight —
QUIC's largest disagreement cluster, era-split exactly at rule 16's
v4 arrival (all four v3-era raters TYPESTATE on all thirteen; seven of
eight later raters THRESHOLD on twelve) — is a vocabulary fight in the
first study's guard-cluster sense: both labels point at the same
one-rung check, and no vote in the cluster changes what is formally
checkable. A type system with access to the connection's own
advertisements can discharge the whole family; the class scheme's
eliminable line cannot see that.

**3. The boundary OVERCOUNTS on state that crosses the connection: the
census's transcript unit is the ceiling.** Item 58 — TYPESTATE in all
twelve raters — has an EMPTY outcome, the registration's strongest
single call, realized: "the remembered values of the parameters" live
in a prior connection, so the eligible conn reading admits no
validator, and no other rung is eligible. Its FAILS record explicitly
invites refutation-by-construction. The same prior-connection channel
blocks 54, 55, and item 78's cannot-reuse half. The class scheme reads
"state machine"; the eliminability ladder reads "ONE connection's
state machine" — 0-RTT parameter consistency is exactly the state a
session-resumption-aware type discipline could carry and a
per-connection transcript cannot witness. Items 32 and 59 complete the
family-(b) picture from the config side: eliminable-vote majorities on
duties whose binding fact is the endpoint's own version set or
capacity.

**4. The iCalendar DOMAIN monolith splits, and the split is the
rule-25 structure witnessed.** The class scheme's one dominant label
spans: pure line-local checks (63's BYDAY/FREQ co-constraint, 84's
sign discipline — prop validators), object-only checks (143's
once-per-object cardinality, the 192–194 cross-property cluster —
object validators whose prop-level pairs show no single line decides
them), and the named exception family {62, 77, 79}: duties whose
TRIGGER is datum-local but whose compliance is conduct- or
world-guarded. Those three drew eliminable-vote majorities while every
eligible local reading failed on a named channel — the trigger/duty
split that rule 25 turned into its litmus, here carried by shipped
pairs instead of votes.

**5. The duplicate-text control did what it was built to do.** Items
43 and 79 are byte-identical sentences; the criterion, computed from
the sentence, necessarily gave them identical outcomes ({nonlocal},
via the same private-intent pair). The archive gave them different
eliminable-vote counts (5 vs 7 DOMAIN of 10) straddling the majority
line — so the correspondence mismatch landed on 79 and only 79,
exactly as registered. This is a measured demonstration that E — the
archive's headline boundary — carries position noise that no
sentence-level semantic property can track, on the cleanest possible
instrument: the same bytes rated twice.

**6. The dissent has three geometries, and the criterion's verdicts
cut across all three.** Per-era vote rows for every contested item are
below. (a) *Era-shaped* (instrument evolution): the QUIC limit family
(finding 2); and the iCalendar conduct family {13, 91, 146, 150, 210},
whose DOMAIN votes are EXACTLY the v5 pair — the instrument the
v5-completion report convicted of mis-design; the locality result
(nonlocal, party-conduct) sides with the eight raters of every other
era against precisely the convicted instrument's readings. Item 62 is
the contrast: its DOMAIN votes (v5, v6, AND v7) survived the repair,
yet the formal verdict is still nonlocal — the standing exception, not
an instrument artifact. (b) *Seat-shaped*: item 185's DOMAIN votes are
exactly the four X-seat raters across every era (Xv4i, Xv5i, Xv6i,
Xv7i), against TYPESTATE from every Claude-family seat plus Xi — a
family split, not an era split (the foreign2 pass's seat-dependence
finding, recurring in the format genre). The criterion's answer is
that BOTH readings are witnessable: {object, nonlocal} — the seats are
each holding one rung of a genuinely two-rung sentence. (c)
*Item-shaped* (mixed dissent with no clean era or seat line): 128,
152, 235, 29 — where the witness pass found the sentence itself
carries the ambiguity (a capability guard, a two-rung bound, a
flight-spanning conjunction, an internal-memory duty).

**7. The challenge interface fired again — a second refuted
impossibility record in as many studies.** The original FAILS record for 235-pkt
claimed the server's transport parameters and its connection-ID choice
"can travel in different datagrams", so no single datagram decides the
conjunction. The gate's reviewer refuted it by construction: under the
witness file's own convention 1, the transport-parameter frame rides
in a packet whose header carries the server's source connection ID —
the TP-bearing datagram exhibits BOTH halves, and the shipped `v235p`
(reviewer-constructed, adopted after verification, provenance in the
file) decides the duty on that designated datum. The record stands
withdrawn in place; QC5's exact sheet paid the point (27/28); and the
selective-elasticity failure mode the registration names — an author
under-constructing on items where a FAILS is convenient — is now
measured twice across two studies, both times caught pre-push by a
reader shipping the denied artifact. Two further constructions were
reworked at the same gate without outcome changes: the 32/33 pairs
originally hung their violating verdicts on conduct the quoted
sentences do not govern (a vacuously satisfied conditional is
compliant, not violated) and were rebuilt over responding transcripts;
and the 17/262 fine pairs argued bytes where those duties count
streams, and were rebuilt on stream counts.

**8. What the FAILS ledger says about the two genres.** The 24
standing records' blocking channels: iCalendar — party-conduct 6,
private-intent 2, world-fact 1; QUIC — prior-connection 6,
deployment-policy 4, party-conduct 3, other-dgrams 1, network-path 1.
The format genre's locality failures are about MEANING and CONDUCT
(what the generator intended, what the consumer does); the transport
genre's are about SCOPE (state and configuration that outlive or
sit outside one connection). Same criterion, different walls — which
is itself evidence the criterion is measuring the genre and not the
author's habits.

## Per-era vote rows (contested items; the registration's promised breakdown)

Raters in era order. Labels: D=DOMAIN T=TYPESTATE P=PROCESS H=THRESHOLD
U=UNCLASSIFIED Y=POLICY N=NEG C=CRYPTO-VERIFY R=REVOCABLE.

iCalendar (Ai Xi | Av4i Xv4i | Av5i Xv5i | Av6i Xv6i | Av7i Xv7i):

```
 13  P P  P P  D D  P P  P P      146  P P  P P  D D  P P  P P
 43  U U  D D  D D  D U  U U      150  P P  P P  D D  P P  P P
 62  P P  P P  D D  D D  D D      185  T T  T D  T D  T D  T D
 77  D D  D U  D D  D D  D U      192  D T  D T  D D  D D  D D
 79  U D  D U  D D  D D  U D      193  D T  D T  D D  D D  D D
 91  P P  P P  D D  P P  P P      194  D T  D T  D D  D D  D D
116  D D  D D  D U  U D  D U      210  P P  P P  D D  P P  P P
```

QUIC (Aq3 Bq3 Aq Xq | Av4q Xv4q | Aq5 Xq5 | Av6q Xv6q | Av7q Xv7q):

```
  4  T T T T  H T  H H  H H  H H      59  U T N T  N T  T T  P T  P T
  9  T T T T  H T  H H  H H  H H      81  C C C P  P P  P P  C C  P C
 10  T T T T  H T  H H  H H  H H      84  T Y Y Y  Y P  Y P  P R  Y R
 17  T T T T  H T  H H  H H  H H     109  P P H H  H R  P P  P H  P R
 18  T T T T  H T  H H  H H  H T     128  P T U U  U T  P T  U T  U T
 26  T T T T  H T  H H  H H  H H     138  Y Y Y D  P D  P P  P P  Y P
 27  T T T T  H T  H H  H H  H H     142  T H T H  T T  T H  T H  T H
254  T T T T  H T  H H  H H  H H     144  P T T D  T T  P D  P T  P D
255  T T T T  H T  H H  H H  H H     152  T D D T  T T  D D  D D  T D
258  T T T T  H T  H H  H H  H H     162  P T T T  T T  T P  T P  P P
259  T T T T  H T  H H  H H  H H     190  H H T H  P T  P T  P T  P T
262  T T T T  H T  H H  H H  H H      23  Y Y T T  T Y  T P  P Y  Y T
263  T T T T  H T  H H  H H  H H       29  T T U T  P P  P T  P P  P T
                                      32  D D N H  D T  D D  P D  P P
                                      33  P D T P  D T  D D  P P  P P
                                      54  T T P T  P P  P T  P T  P P
                                      55  T T P T  P P  P T  P T  P P
                                     235  D D T D  T T  T D  T D  T T
```

## What a skeptical reader should attack first

1. **Item 40's pair** (the least standard construction in either file):
   non-locality of "explicitly negotiate an application protocol" rides
   on the claim that WHICH protocol the stream bytes belong to is
   endpoint interpretation, not wire content. If you think ALPN
   presence in the model transcript settles the duty by itself, the
   pair's second context is your target.
2. **QUIC 62's reading** ("MUST support buffering at least 4096
   bytes"): the shipped conn validator checks the duty's observable
   face — no buffer-exhaustion signal while ≤4096 bytes are
   outstanding. If "support" is a pure capability duty with no
   observable face, the right outcome is a nonlocal pair instead, and
   QC4 drops to 2/3 (still passing; the mismatch set would shrink by
   one, weakening family (a) to 15/16 — floors hold either way, but
   the finding-2 count changes).
3. **The response-duty pairs built by one template** (`responder_pf`):
   six close-on-violation items share one fine-pair shape. The shape
   is sound per item only if each item's trigger really is
   conn-carried; the six quotes are the check.
4. **Any standing FAILS record** — especially 58's, which the
   registration elevated to its strongest claim. Constructing the conn
   validator it denies would break QC2, family (b), and the finding-3
   story in one shot. That is the designed challenge surface — and it
   is live, not rhetorical: the 235 record has already fallen to
   exactly this attack (finding 7).
5. **The reworked 32/33 pairs**: their violating verdicts now ride on
   a RESPONDING transcript (answering a datagram that the server's
   configuration required it to drop). If you think a response's
   compliance with a drop duty cannot flip on the server's version
   set or connection table, those two pairs are the target.

## Limitations

1. **Author-constructed, archive-aware** — inherited from the first
   study, at full force. The mechanical layer prevents structural
   cheating and silent rung-dropping (FAILS coverage is enforced), but
   reading quality is judgment, published for challenge.
2. **A near-perfect sheet is weak evidence of calibration.** The
   first study missed 2 of 44 exact outcomes; this pass missed 1 of
   72 — and only because the gate constructed what the author had
   recorded as unconstructible. Part of the improvement is real (the
   registration-time anaphora audit was built from the first study's
   two misses, which were both hidden mid-sentence context
   dependencies — that shape did not recur). But the 235 refutation
   shows the residual risk runs the other way now: not hidden context
   dependencies, but under-construction where a FAILS record is
   convenient. The gate's adversarial pass, not the sheet, is the
   calibration check — twice measured, twice necessary.
3. **Modeling conventions carry weight**: abstract packet numbers make
   152's pkt bound non-vacuous; the TP-frame abstraction makes
   advertised limits conn-carried (and is what made the 235 refutation
   possible); denotation-carrying UTC offsets make 84 prop-checkable;
   integer-day arithmetic stands in for calendar math; the 192–194
   fixtures place RECURRENCE-ID and DTSTART in one component, where
   RFC 5545's master/modification structure would put the RRULE-bearing
   master in a sibling — the object-rung conclusion is unaffected, the
   fixture shape is noted. Each convention is disclosed in the witness
   files' headers; a reader who rejects one rejects the witnesses
   built on it, and the affected readings are enumerable from the
   headers.
4. **Three registered channel glosses were overridden at
   construction** (channels are reported, not graded; the deltas are
   recorded here rather than silently normalized): item 59,
   counterparty-config → deployment-policy, per the first study's
   convention 3 (the obliged party's OWN configuration); item 40,
   counterparty-config → party-conduct/deployment-policy (the shipped
   pair varies what the endpoints RUN, not what they support); item
   200, generation-process → other-artifacts (the shipped pair varies
   the existence of a twin identifier elsewhere, not the generator's
   process — its sibling 201 carries the generation-process pair).
   The first draft of this report disclosed only the first; the gate
   counted.
5. **The exclusion of QUIC 281 remains a judgment call** (registered
   as such, with its challenge path). Nothing in this pass tested it.
6. **Cross-corpus rate comparisons compare different selection
   depths** (registration disclosure, repeated here): iCalendar's
   witness set reaches d≥2 dissent; QUIC's stops at d≥5. The 13.0% vs
   38.8% exception rates are not points on one scale.
7. **The v26/v27 accounting** counts the handshake connection ID
   toward the active-CID limit (per §18.2's active_connection_id_limit
   definition); an
   earlier draft of the validator had the +1 cancel out and was fixed
   before the gate. The vectors pass under both formulas — the fix
   changes the boundary case (exactly-at-limit), not any shipped
   vector, and is noted for the record.
