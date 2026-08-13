# enforceability-census

**What fraction of a specification's stated runtime obligations could a type
system have discharged?** This repository measures that question — the
*enforceability-class mix* of real obligation corpora — instead of arguing it.

> **Status: consolidation in progress (2026-08-13).** The censuses below were
> run 2026-08-02 → 2026-08-12 as working artifacts; they are collected here on
> their way to a repo-native paper. Numbers are quoted with their caveats or
> not at all. This repository is the artifact of record; no venue submission is
> planned.

## The taxonomy (the codebook)

[`codebook/classes.md`](codebook/classes.md) defines four classes by the
**shape of the predicate** — never the wording of the alert or the name of the
error:

| class | shape | type-eliminable? |
|---|---|---|
| DOMAIN | monotone predicate on one value, no history | yes — an enum/newtype |
| TYPESTATE | ordering obligation over one object's history | yes — typestate/session types across the boundary |
| REVOCABLE | a fact that was true and became false | no — needs a clock; this is the residue |
| THRESHOLD | inequality against a chosen number | no — a policy line, not a fact |

Two further classes are **provisional** (forced by the TLS corpus, not yet
graduated into the codebook): CRYPTO-VERIFY (verification requiring secret or
transcript material — the discriminator is the secret, not the word "crypto")
and NEGOTIATION.

The codebook ends with a full **retraction** of its own first cross-layer
claim — kept verbatim because the failure (a classifier tuned by its author's
expectations, caught by error-sign analysis) is the methodological spine of
this work, and it is where rules 8 and 9 (classify on the predicate, enforce
that with a DISAGREE bucket) come from.

## The censuses

| corpus | n | headline | status |
|---|---|---|---|
| [`census/promql/`](census/promql) — awesome-prometheus-alerts | 1155 | 78.6% THRESHOLD, 0 TYPESTATE (censored by the query language) | reconciled against primary sources; prior-art sweep found no comparable measurement |
| [`census/wayland/`](census/wayland) — declared protocol errors, core + extensions | 172 | **87.6% type-eliminable** (one protocol; versioned-boundary limit noted in codebook) | reconciled against primary sources |
| [`census/tls13/`](census/tls13) — RFC 8446 §4 MUST/SHALL corpus | 204 | **80–82% type-eliminable** (two-rater range; crypto core ≈3%) | two-rater, 20-item DISAGREE bucket unresolved; codebook repair + third pass owed |
| `census/tls13/tls13-alert-census.md` — TLS 1.3 alert vocabulary (30-min probe) | 30 | alert vocabulary censors typestate ~2.3× vs the MUST corpus | probe; superseded by the §4 census for any headline |

**Read the caveats before quoting any number.** Every corpus censors some
class (rule 7); percentages are never comparable across layers or across
error-code granularities; the TLS headline is a *range* until the codebook
repair converges.

## Regenerating corpora

The classifiers ship; the corpora they consume are regenerable and not
vendored:

- **PromQL**: clone [`awesome-prometheus-alerts`](https://github.com/samber/awesome-prometheus-alerts);
  `promql-classifier.py` walks its YAML.
- **Wayland**: extract declared `<error>` entries from `wayland.xml` (core) +
  the [`wayland-protocols`](https://gitlab.freedesktop.org/wayland/wayland-protocols)
  tree; `wayland-classifier.py` classifies the JSON.
- **RFC 8446 §4**: `rfc8446_s4_musts.txt` is checked in (204 sentences,
  regenerable by the extraction recipe in `rfc8446-s4-census.md`).

## Open work (tracked to convergence before any paper claim)

1. Codebook repair: a guard-vs-predicate tie-break rule and a sharper
   UNCLASSIFIED boundary for capability-honesty duties (the two defects the
   20-item DISAGREE bucket localizes).
2. Third blind rating pass over the 204 under the repaired codebook.
3. Wayland falsifiability check: the provisional classes predict CV=0, NEG≈0
   in the Wayland corpus — regenerate and grep before asserting.
4. Graduate CRYPTO-VERIFY + NEGOTIATION into the codebook iff they survive.
5. Optional second security RFC (Noise or RFC 9420 MLS) to turn one data
   point into a comparison.

## License

MIT — see [LICENSE](LICENSE).
