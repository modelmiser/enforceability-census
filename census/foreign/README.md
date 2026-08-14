# Cross-family replication — TLS §4 under foreign frontier models (pre-registration)

**Status: pre-registered; committed and PUSHED before any foreign rater exists.
No foreign model has seen the corpus or the instrument at registration time.**

Every rating in this repository so far — every author pass and every blind
rater across seven corpora — came from the same model family (Anthropic
Claude). PAPER.md limitation 6 names the consequence: intra-family agreement
(raw 81–90%, eliminable-vs-not 87–96% on TLS §4) is inflated by shared
training priors to an unknown degree, and the absolute quotients are,
strictly, facts about the (document, this-family's-reading) pair.

This replication attacks the **family-bias half** of that threat: re-rate the
headline corpus under frontier models from *foreign* families. It deliberately
cannot touch the other half — the **corpus-shared prior** (all frontier LLMs
trained on the RFCs and on prose about them) is unaddressable by any LLM
replication; only a non-LLM rater (human replication, parked as future work)
bears on it. The report must keep this split explicit.

## Design (frozen at registration)

- **Corpus:** the TLS census corpus, byte-identical. `census/tls13/rfc8446_s4_musts.txt`,
  n = 204, sha256 `fc7befbcbe8343e5723f5d922156e5afc32bf45e0e1cab2a304aafb845609f0f`,
  git blob `fbc6591a53bce2c19cadc8c93dc236e1f33cb8c3`. No re-extraction.
- **Instrument:** the frozen rater pack, verbatim — git blob
  `a08febba22fd2cb117a9be41654a6209e0104e57` (codebook v3, rules 1–14), served
  by `git cat-file` with hash round-trip verification, exactly as for raters
  B‴ onward. Rule candidates 15 and 16 are NOT in this instrument and stay
  parked.
- **Raters (two foreign families), transport = cursor-cli** (`cursor-agent
  --print --output-format text --mode ask`, run from an empty directory,
  subscription-authenticated):
  - **Rater G** = OpenAI `gpt-5.6-sol-high`
  - **Rater X** = xAI `cursor-grok-4.6-high-fast`
  - Gemini is excluded: the subscription exposes only a flash-tier Gemini,
    and a weaker-tier rater confounds capability with prior divergence.
- **Blindness:** each rater receives the instrument and its corpus chunk and
  nothing else — no predictions, no other rater's labels, no running totals,
  no statement of the study's hypotheses.
- **Chunking (disclosed protocol delta):** 204 items in four chunks —
  [1–51], [52–102], [103–153], [154–204] — because a single 204-label
  completion risks truncation. Each chunk prompt = full instrument + chunk +
  output-format instruction. Chunks of one rater share no state (fresh
  process per chunk).
- **Single-shot rule:** one attempt per chunk. If a chunk's output is
  malformed (missing items, invalid class names), ONE format-only retry of
  that whole chunk (same prompt plus a restatement of the output format —
  no content feedback); items still malformed after that are scored **U**
  and recorded as a protocol event. No regeneration shopping.
- **Transport deltas (disclosed):** cursor-cli exposes no temperature
  control, and the model is served through Cursor's routing (a wrapper
  system prompt outside our control may precede our instrument). Both apply
  identically to both raters.
- **Scoring reference:** rater D (pass 4) is the comparison anchor, as the
  most recent valid Claude rater under this exact instrument; A is
  secondary. Labels compared at raw-class and eliminable-vs-not granularity,
  same as every prior pass. DISAGREE mass reported, never adjudicated.

## Pre-registered predictions (F1–F5)

Numbering namespace **F1–F5** (foreign), disjoint from P/M/Q/K/R and from
codebook rule numbers.

Claude reference points (from `census/tls13/rfc8446-s4-pass4.md`): quotients
A 81.9% / B 79.9% / D 82.8%; intra-family raw agreement 81–90%;
eliminable-vs-not 87–96%; CV set {120, 125, 126, 178, 179, 180} item-for-item
identical across all four passes.

- **F1 (band):** each foreign rater's eliminable-in-shape quotient lands in
  **76–86%** (the Claude band widened by ±3–4 points for cross-family
  drift).
- **F2 (agreement ordering):** for each foreign rater vs D, raw item
  agreement lands in **70–84%** (below the intra-family midpoint) and
  eliminable-vs-not agreement lands in **82–93%** — cross-family agreement
  is lower than intra-family at both granularities, but the quotient-level
  signal (eliminable-vs-not) degrades less than raw labels.
- **F3 (crispest class transmits):** each foreign rater labels **≥ 5 of the
  6** CV items {120, 125, 126, 178, 179, 180} as CV.
- **F4 (locus):** for each foreign rater, **more than half** of its raw
  disagreements with D are *interior* to the eliminable family (both label
  the item eliminable, different class) — the Claude pattern.
- **F5 (no LLM clique):** G-vs-X raw agreement falls within **±6 points** of
  the mean of (G vs D) and (X vs D) raw agreement — foreign raters do not
  cluster with each other against Claude, i.e., cross-family divergence is
  idiosyncratic rather than a shared non-Claude reading.

**Failure interpretation, pre-committed:** these predictions grade the
**author's model of cross-family transmissibility**, nothing else. The corpus
and instrument are frozen and already public. A failed prediction is a wrong
guess about how the codebook transmits across model families, recorded as
such — it licenses NO re-rating, NO rule change, NO exclusion of items, NO
quote discretion, and NO change to any published number.

**Headline pre-commitment:** the quoted TLS headline stays **80–83%
(three raters, one codebook lineage)** regardless of outcome — foreign
results are reported as a separate replication row, never folded into the
headline. If F1 fails low, the finding is "the codebook transmits within
family better than across families," which *narrows the scope* of the
transmissibility claim (and of limitation 6's residual) — it does not touch
the Claude-measured numbers. If F1 passes, limitation 6's family-bias half is
weakened; its corpus-shared-prior half stands untouched either way.

---

## Outcome (2026-08-13, appended after rating — the pre-registration above is unmodified)

Both raters ran same-day, single-shot, zero protocol events. Grades: **F1,
F3, F5 PASS; F2, F4 FAIL** — F2's lower-than-intra-family clause failed for
both raters (rater X agreed with rater D *above* the intra-family ranges at
both granularities).
Full results, findings (including candidate rule 17), and verbatim label
archives: `rfc8446-s4-foreign.md`.
