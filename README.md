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
on a pre-registered falsifiability check (0 members each in the regenerated
Wayland corpus — two vocabulary hits, both hand-adjudicated false positives;
ordering witnessed by same-morning commit sequence — see the paper's
provenance note, §6) plus a stability criterion articulated at graduation time
(CV was item-for-item identical in every rater's recorded labels across four passes; NEG's
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
| [`census/wayland/`](census/wayland) — declared protocol errors, core + extensions | 172 | **87.6% type-eliminable in shape** (149/170 client-facing; 86.6% on all 172; one protocol — versioned-boundary limit noted in codebook) | reconciled against primary sources at census time; the census-era checkout was not pinned, so the 172-item corpus is preserved as reported numbers, not as a regenerable artifact (the regenerable superset is n=216 and carries no headline) |
| [`census/tls13/`](census/tls13) — RFC 8446 §4 MUST/SHALL corpus | 204 | **80–83% type-eliminable in shape** (range over three valid raters, 79.9–82.8%; crypto core exactly 6/204, same items in every rater's recorded labels) | closed 2026-08-13 after a repair-and-re-rate loop with pre-registered predictions (passes 3–4); raters are LLM agents; disagreements unresolved by design |
| `census/tls13/tls13-alert-census.md` — TLS 1.3 alert vocabulary (30-min probe) | 25 | alert vocabulary censors typestate ~2.3× vs the MUST corpus | probe; tally corrected 2026-08-13; superseded by the §4 census for any headline |
| [`census/mls/`](census/mls) — RFC 9420 §5–§15 MUST/SHALL corpus | 127 | **≈57% type-eliminable in shape** (two raters: 56.7%/57.5% — ~25 points below TLS under the SAME instrument and recipe; ~18–19% PROCESS) | run 2026-08-13 under the frozen TLS pass-4 instrument, predictions pre-registered and publicly timestamped BEFORE any rater (M1 passed; M2–M4 failed and M5 failed 2 of its 3 clauses — graded against the author's model, per the pre-commitment); disagreements unresolved by design |
| [`census/quic-tls/`](census/quic-tls) — RFC 9001 §4–§8 MUST/SHALL corpus | 69 | **54–67% type-eliminable in shape** (quoted wide: 53.6%/66.7% — raw agreement 76.8%, the series' FIRST transfer-band breach, concentrated on PROCESS/TYPESTATE key-lifecycle splits; CV is 1.4%/2.9% — the crypto document's cryptography lives in non-normative grammar) | run 2026-08-13, frozen instrument, predictions publicly pre-timestamped; ALL FIVE K-predictions failed, graded against the author's model per the pre-commitment |
| [`census/quic-recovery/`](census/quic-recovery) — RFC 9002 §5–§7 MUST/SHALL corpus | 30 | **23.3% type-eliminable in shape** (identical in both raters; ~60% PROCESS) — the lowest of the frozen-instrument MUST-corpora | run 2026-08-13, frozen instrument, predictions publicly pre-timestamped (R1/R2/R4 passed; R3 failed by class disuse, R5 failed above-band); PROTOCOL DEVIATION disclosed: author pass abandoned after exposure to first-rater labels, replaced by a second blind rater |
| [`census/quic-family.md`](census/quic-family.md) — the three-document synthesis | 380 | within ONE protocol the share spans 23%→69% by document role; pooled family ≈61–65% (caveat in file) | the matched-family control: same protocol, era, authors — only document role varies |
| [`census/quic/`](census/quic) — RFC 9000 §2–§19 MUST/SHALL corpus | 281 | **≈67–69% type-eliminable in shape** (two raters: 66.9%/69.0%; TYPESTATE the largest class at ~46–47%; CV 1.1% — RFC 9001/9002 document boundary censors crypto and recovery) | run 2026-08-13 under the same frozen instrument, predictions publicly pre-timestamped (Q2/Q3/Q4 passed — Q4 confirmed the rule-3 spec-fixed-constant edge with THRESHOLD symdiff 15; Q1 failed marginally, Q5 failed its crisp-class clause on a new REVOCABLE/deadline edge); disagreements unresolved by design |

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
   residual: the codebook's crisp-discriminator classes transmit with zero
   or near-zero rater variance (CRYPTO-VERIFY and META identical in every
   rater's recorded labels; one recorded THRESHOLD→REVOCABLE flip), while
   raw item agreement between raters floors in the
   low-to-mid 80s (D vs A: 83.8%; bounded B–D as low as 80.9%), including
   15 items where two fresh raters
   agree on the same alternative label against the original ratings; that
   error bar is reported, not adjudicated away.
2. ~~Optional second security RFC~~ — DONE 2026-08-13: the MLS census
   (`census/mls/`) turned one data point into a matched-method comparison;
   the type-eliminable share is NOT a security-protocol constant (TLS
   80–83% vs MLS ≈57%). Its disagreement residue names a candidate rule 15
   (capability-compatibility tie-break) for any future instrument version.
3. ~~A third corpus under the same frozen instrument~~ — DONE 2026-08-13:
   the QUIC census (`census/quic/`) lands at ≈67–69%, between MLS and TLS —
   consistent with a spectrum (57 → 67–69 → 80–83), each span's position
   explainable by what it states as obligations (a post-hoc reading; see
   the report's headline caveat). Its residue adds a rule-16
   candidate (spec-fixed constants, THRESHOLD symdiff 15) and a
   deadline-duty edge to the rule-15 candidate from MLS.
4. ~~Paper integration of the QUIC census~~ — DONE 2026-08-13. Then the
   QUIC document-family completion (RFC 9001 + 9002) was run the same day:
   see `census/quic-family.md`. Within one protocol the share spans
   23%→69% by document role — the strongest evidence yet for the
   what-the-span-states reading, measured under the matched-family
   control.
5. Paper integration of the family completion; possibly a NON-protocol
   corpus later; instrument v4 (rule candidates 15/16 + the
   REVOCABLE-deadline and key-lifecycle boundary observations) only as a
   deliberate, pre-registered version bump.

## License

MIT — see [LICENSE](LICENSE).
