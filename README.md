# enforceability-census

**What fraction of a specification's stated runtime obligations could a type
system have discharged?** This repository measures that question — the
*enforceability-class mix* of real obligation corpora — instead of arguing it.

> **The paper: [PAPER.md](PAPER.md)** — the repo-native consolidation of the
> codebook, the censuses, and the four-pass inter-rater study. This repository
> is the artifact of record; no venue submission is planned. The censuses were
> run 2026-08-02 → 2026-08-13 as working artifacts and are preserved here with
> their corrections in place; numbers are quoted with their caveats or not at
> all.

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

Two further classes — **CRYPTO-VERIFY** (verification requiring secret or
transcript material; the discriminator is the secret, not the word "crypto")
and **NEGOTIATION** (emptiness of a two-party intersection; never the chosen
value itself) — were forced by the TLS corpus and **graduated on 2026-08-13**
on a pre-registered falsifiability check (0 hits each in the regenerated
Wayland corpus) plus a stability criterion articulated at graduation time
(CV was item-for-item identical across every rater in four passes; NEG's
evidence is thinner — see the codebook's graduation record).

The codebook carries, in full, a **retraction** of its own first cross-layer
claim — kept verbatim because the failure (a classifier tuned by its author's
expectations, caught by error-sign analysis) is the methodological spine of
this work, and it is where rules 8 and 9 (classify on the predicate, enforce
that with a DISAGREE bucket) come from.

## The censuses

| corpus | n | headline | status |
|---|---|---|---|
| [`census/promql/`](census/promql) — awesome-prometheus-alerts | 1155 | 78.1% THRESHOLD, 21.3% REVOCABLE, 0.6% unclassified (all /1155); 0 TYPESTATE — censored by the query language | reconciled against primary sources; prior-art sweep found no comparable measurement |
| [`census/wayland/`](census/wayland) — declared protocol errors, core + extensions | 172 | **87.6% type-eliminable** (149/170 client-facing; 86.6% on all 172; one protocol — versioned-boundary limit noted in codebook) | reconciled against primary sources |
| [`census/tls13/`](census/tls13) — RFC 8446 §4 MUST/SHALL corpus | 204 | **80–83% type-eliminable** (range over three valid raters, 79.9–82.8%; crypto core exactly 6/204, same items for every rater) | closed 2026-08-13 after a repair-and-re-rate loop with pre-registered predictions (passes 3–4); raters are LLM agents; disagreements unresolved by design |
| `census/tls13/tls13-alert-census.md` — TLS 1.3 alert vocabulary (30-min probe) | 25 | alert vocabulary censors typestate ~2.3× vs the MUST corpus | probe; tally corrected 2026-08-13; superseded by the §4 census for any headline |

**Read the caveats before quoting any number.** Every corpus censors some
class (rule 7); percentages are never comparable across layers or across
error-code granularities; the Wayland headline depends on classifier
vocabulary fitted to its corpus (the codebook's retraction addendum makes
reporting that dependency mandatory); the TLS headline is a *range* (three
raters, disagreements unresolved by design — see the pass 3/4 reports for
why the loop stopped where it did).

## Regenerating corpora

The classifiers ship; the corpora they consume are regenerable and not
vendored:

- **PromQL**: clone [`awesome-prometheus-alerts`](https://github.com/samber/awesome-prometheus-alerts)
  and feed the merged rules YAML to the classifier (needs PyYAML):
  `python3 census/promql/promql-classifier.py <rules.yml> out.json`
- **Wayland**: extract declared `<error>` entries, then classify:
  `python3 census/wayland/extract-corpus.py corpus.json <wayland>/protocol/wayland.xml <wayland-protocols>/{stable,staging,unstable,experimental}`
  then `python3 census/wayland/wayland-classifier.py corpus.json out.json`
  (sources: [`wayland`](https://gitlab.freedesktop.org/wayland/wayland),
  [`wayland-protocols`](https://gitlab.freedesktop.org/wayland/wayland-protocols)).
- **RFC 8446 §4**: `rfc8446_s4_musts.txt` is checked in (204 sentences,
  regenerable by the extraction recipe in `rfc8446-s4-census.md`).

## Open work

1. ~~Codebook repair~~, ~~re-rating passes~~, ~~Wayland falsifiability
   check~~, ~~class graduation~~, ~~PAPER.md~~ — all closed 2026-08-13
   (codebook v2/v3; passes 3–4 with pre-registered predictions and a stop
   whose interpretation was pre-registered; CV/NEG graduated; paper
   drafted and taken through a publish-gate cold round). The measured
   residual: the codebook transmits perfectly where discriminators are
   crisp, while raw item agreement between raters floors in the
   low-to-mid 80s (D vs A: 83.8%; bounded B–D as low as 80.9%), including
   15 items where two fresh raters
   agree on the same alternative label against the original ratings; that
   error bar is reported, not adjudicated away.
2. Optional second security RFC (Noise or RFC 9420 MLS) to turn one data
   point into a comparison.

## License

MIT — see [LICENSE](LICENSE).
