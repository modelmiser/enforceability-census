# Second cross-family replication — the family panel widens (pre-registration)

**PUSHED BEFORE ANY RATER SEES THE INSTRUMENT OR THE CORPUS.** The
three models seated below have, at registration time, seen nothing of
this study; each was sent exactly one one-word echo prompt ("Reply
with exactly the single word: PONG") on 2026-08-16 to verify
transport reachability — no census content.

**What this is.** The TLS §4 corpus re-rated blind under THREE more
foreign model families, widening the family panel from two (OpenAI,
xAI — `census/foreign/`) to five. This probes the **family-bias**
half of limitation 6 only: the corpus-shared-prior half is untouched
by construction (all raters here are LLMs; the registered human pass
`census/human/` — currently awaiting its recruit — remains the sole
route there, as the obfuscation probe measured and its report
argued). No number from this
replication joins, replaces, or requalifies any census figure.

**Why now, and why these families.** The first replication's
registration recorded, at selection time: *"Gemini is excluded: the
subscription exposes only a flash-tier Gemini, and a weaker-tier
rater confounds capability with prior divergence."* Verified
2026-08-16: `cursor-agent --list-models` now exposes
`gemini-3.1-pro` — the recorded exclusion reason no longer holds, so
the family is seated. Moonshot (Kimi) and Zhipu (GLM) lineages are
newly exposed and have never been seated anywhere in this
repository; their training provenance is maximally distinct from the
three families rated so far (Anthropic, OpenAI, xAI), which is
exactly what a family-bias probe wants. **Composer 2.5 is excluded with a recorded reason:** it
is Cursor's in-house model of undisclosed base lineage — an
unattributable family is a confound for a family-bias measurement.

## Corpus and instrument (both frozen, nothing new cut)

- **Corpus:** `census/tls13/rfc8446_s4_musts.txt` (n = 204),
  unchanged.
- **Instrument:** the SAME serving as `census/foreign/` — the frozen
  v3 pass-4 rater pack, git blob
  `a08febba22fd2cb117a9be41654a6209e0104e57`, extracted via
  `git cat-file blob` and hash-round-trip verified at serve time.
  DELIBERATELY v3, not the current v6: the point is comparability
  with the F-series band and the Claude reference points, which were
  all measured under this exact blob. (A family panel under v6 would
  be a separate arc with different anchors.) Known inherited steer,
  disclosed since the v6-pass registration: the v3 pack's DH worked
  example shares a 4-gram with item 101 ("1 < Y < p-1").

## Raters (pre-registered by exact id; a differing serving model is a protocol event)

| seat | family | cursor model id | tier rationale |
|---|---|---|---|
| **M** | Google | `gemini-3.1-pro` | the only non-flash Gemini exposed |
| **K** | Moonshot | `kimi-k3-max` | the family's canonical tier (display name "Kimi K3", no qualifier) |
| **Z** | Zhipu | `glm-5.2-high` | the family's canonical tier (display name "GLM 5.2", no qualifier) |

All three verified reachable 2026-08-16 via `cursor-agent`
2026.08.11-e8db854 (the same binary version pinned at the v6
registration; the model list is server-side).

**Transport, identical to `census/foreign/` except one disclosed
delta:** `cursor-agent --print
--output-format text --mode ask --trust` — the `--trust` flag was
not in the first replication's invocation; it is carried from the
v6-pass transport (`census/v6-pass/README.md`) and applies
identically to all three raters. Run from an empty
directory; 204 items in four chunks [1–51], [52–102], [103–153],
[154–204]; each chunk prompt = full instrument + chunk +
output-format instruction; fresh process per chunk, no shared state.
Single-shot rule: one attempt per chunk; ONE format-only retry on
malformed output (no content feedback); items still malformed after
that are scored U and recorded as a protocol event. No regeneration
shopping. Cursor exposes no temperature control and may prepend a
wrapper prompt outside our control — both apply identically to all
three raters. **Blindness:** each rater receives the instrument and
its corpus chunk and nothing else.

## Pre-registered clauses (F6–F10; namespace continues census/foreign's F1–F5)

Scoring reference: rater **D** (pass 4) is the comparison anchor, as
in the first replication; A secondary. Normalization: torn `?`
stripped, base label governs; U ≡ UNCLASSIFIED, NEG ≡ NEGOTIATION,
CV ≡ CRYPTO-VERIFY; eliminable = DOMAIN + TYPESTATE.

- **F6 (band):** each new rater's eliminable-in-shape quotient lands
  in **76–86%** (F1's band, unchanged; measured occupancy: all five
  prior raters inside — A 81.9, B 79.9, D 82.8, G 76.5 at the
  floor, X 80.9). Failability disclosed honestly: the quotient
  is invariant under label shuffles (a shuffle preserves the class
  histogram), so the shuffle degenerate CANNOT fail F6; the measured
  fail branch is a relabel mutant (X's map with every TYPESTATE set
  to PROCESS: 69/204 = 33.8%, FAIL).
- **F7 (the CV core):** all six CV-set items {120, 125, 126, 178,
  179, 180} keep CV in each new rater, 6/6 strict. This extends the
  repository's strongest streak — every rater ever run on this
  corpus, twelve so far across three families and every instrument
  version the corpus has been rated under (the invalidated pass-3
  rater included), has kept all six — so a single break is maximally
  informative and would be reported as such. Measured fail branch:
  the shuffle mutant scores 0/6.
- **F8 (agreement floor, universal):** each new rater's raw
  agreement vs D ≥ **143/204** (70%). Measured exhibits: G 166, X
  187; the shuffle mutant scores 80, FAIL. A rater below this floor
  is diverging beyond anything measured in any family so far.
- **F9 (band-reach, existential):** at least ONE of the three new
  raters posts raw-vs-D ≥ **166/204** (81.4% — exactly G's measured
  value, at the lower edge of the 81–90% intra-family raw span,
  whose own floor pair is B–D bounded with B's four labels
  unarchived). The author's model, updated by F2's failure:
  cross-family agreement is family-dependent with at least one
  family typically reaching the intra-family span (X exceeded it; G
  touched its lower edge). Measured fail branch (the all-three-below
  case): three independent shuffle mutants score 80, 63, and 65
  vs D — aggregate FAIL, exhibited in the scorer's KAT.
- **F10 (the candidate-rule-17 cluster):** each new rater reads at
  least **6 of 9** of the foreign-consensus DOMAIN→TYPESTATE cluster
  {10, 52, 67, 129, 130, 139, 152, 159, 165} as TYPESTATE. Floor
  justification, measured (the smallest integer every measured fail
  branch fails): D scores 0/9, the relabel mutant 0/9, and the
  shuffle mutant **5/9** — X's map is 96/204 ≈ 47% TYPESTATE, so a
  shuffle expects ~4.2/9 and this seed lands 5; a floor of 5 would
  be a check the shuffle degenerate passes. Measured pass exhibits:
  G and X at 9/9 (by construction of the consensus — disclosed).
  Interpretation pre-committed: a PASS across the new families
  strengthens candidate rule 17's evidence that the
  negotiated-state reading is family-general (v7 docket input); a
  FAIL grades the author's family-generality model and licenses
  nothing about D's labels, the census, or any instrument grade.

**Report-only quantities** (measured, never graded): the →U
consensus cluster {187, 190, 197} item-by-item; all pairwise
foreign–foreign raw agreements (with G and X, ten pairs across five
families); per-class distributions (G's U-inflation mechanism is the
comparison point); torn counts; per-rater vs-A agreement; the
malformed/U protocol-event count.

**Interpretation, restated:** this arc measures family-bias
robustness only. One rater per family — a rater is one sample of a
family, not the family; family-level claims stay at "consistent
with," never "characterizes." All F-series and census numbers are
ring-fenced; failed predictions grade the author's models.

## Scoring

`score_f2.py` (shipped here) is the only grader. Its known-answer
test re-parses the archived raters G, X (census/foreign/) and D
(census/tls13/rfc8446-s4-pass4.md) and asserts every measured number
quoted above — quotients 156/165/169 of 204, vs-D raw 166/187,
eliminable-vs-not 187/200, G-vs-X 176/191, CV 6/6/6, cluster
9/9/0 — and exhibits every graded clause's fail branch, F9's via the
three shuffle mutants (80/63/65, aggregate FAIL) with its pass
branch checked at the exact 166 edge. The pairwise-agreement helper
(`agree`) for the report's ten-pair table ships in the same file;
vs-A agreement is computed at report time from the census's
per-class rosters, the same way the first replication's report did
(rater A has no flat archived map). Both parse paths reject
duplicate item labels. Watched to fail before registration: a
perturbed KAT expectation fails at the perturbed rater. Labels will
be archived verbatim in the report and round-trip parsed before
push.
