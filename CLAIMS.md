# What this repository currently claims

One page. No narrative, no dates, no commit hashes, no grade histories — those live
in [`PAPER.md`](PAPER.md), the census directories, and `git log`. If you read one file
here, read this one.

**The question:** given a specification's *stated* runtime obligations, what fraction
could a type system have discharged? Each obligation is classified by the **shape of
its predicate**, never by its wording — see [`codebook/classes.md`](codebook/classes.md).

---

## The one caveat that binds everything below

**Every rater in this repository is an LLM.** The shared-prior confound — author and
raters trained into the same reading habits — is measured, disclosed as Limitation 6,
and **unaddressed**. Both instruments built to address it are unrun: the human passes
need a recruit, and the mechanical probe could not adjudicate. Treat every share below
as an LLM classification of sentences, replicated across raters and model families but
not outside them.

## Currently claimed

| claim | n | binding caveat |
|---|---|---|
| **The type-eliminable share is not a constant.** It spans ≈23%–88% across censused corpora | 2 500+ | every figure is a *censused span*, not a whole document |
| TLS 1.3 §4 — **80–83%** ([`census/tls13/`](census/tls13)) | 204 | range over three raters; the span omits key-schedule and record-layer MUSTs |
| iCalendar §3 — **88.0% / 88.4%** ([`census/ical/`](census/ical)) | 225 | 14 sentence texts recur verbatim with different referents |
| QUIC transport — **≈67–69%** ([`census/quic/`](census/quic)) | 281 | TYPESTATE is the largest class here (~46%) |
| MLS — **≈57%** ([`census/mls/`](census/mls)) | 127 | ~25 points below TLS under the *same* instrument |
| QUIC recovery — **23.3%** ([`census/quic-recovery/`](census/quic-recovery)) | 30 | small n; ~60% PROCESS |
| Wayland — **87.6%** ([`census/wayland/`](census/wayland)) | 172 | ⚠️ **the corpus behind this figure is not regenerable** (checkout never pinned); re-running the shipped pipeline gives **79.0%** |
| PromQL — **78.1% THRESHOLD, 0 TYPESTATE** ([`census/promql/`](census/promql)) | 1 155 | the 0 is a *language invariant*, not a measurement — the query language cannot express ordering |
| **Document role varies the share more than domain does.** Within one protocol family the span is 23%→69% ([`census/quic-family.md`](census/quic-family.md)) | 380 | pooled family figure carries its own caveat in-file |
| **Classes transmit as well as their discriminators are crisp.** CRYPTO-VERIFY is item-identical across 17 raters and 6 model families; disagreement concentrates at fuzzy boundaries | — | the discriminator is the secret material, never the word "crypto" |
| **Cross-family replication holds.** Five foreign model families land inside the pre-registered band ([`census/foreign/`](census/foreign), [`census/foreign2/`](census/foreign2)) | 204 | replication is *across LLMs*, which is the confound above, not an escape from it |
| **A datum-locality criterion corresponds to the eliminability vote**, with pre-named exceptions realized and zero unnamed ([`census/locality/`](census/locality), [`census/locality2/`](census/locality2)) | 44 + 27 | witnesses are author-constructed; that residual is what the unrun human passes exist to probe |

## Withdrawn, superseded, or foreclosed

| what | status |
|---|---|
| **"The class mix is a property of the layer, not of software"** | **RETRACTED** — a classifier tuned by its author's expectations, caught by error-sign analysis. Kept verbatim in [`codebook/classes.md`](codebook/classes.md) because the failure is the methodological spine of this work |
| **Human pass H1's packet** | **SUPERSEDED by H1-R2** — its format examples leaked real archive labels on graded items, and one leak lifts the largest measured failing branch to a PASS at the H2 floor. Serve `packet-h1r2.md`, never `packet-h1.md` ([`census/human/`](census/human)) |
| **MECH-PROBE-1's causal claim** ("the errors are exactly decision rule 1 / not a regex-quality problem") | **WITHDRAWN** — 1 of 11 errors is decision rule 1; most are pattern over-breadth ([`census/mech-probe/`](census/mech-probe)) |
| **MECH-PROBE-1's verdict** | **WITHDRAWN TWICE** — "Negative, arc closed", then "branch 3, inconclusive". Standing status: **the pre-registration cannot adjudicate the run.** Not pursued |
| **"RFC 5545 identified from structure alone"** | **CORRECTED** to "structure *and disclosed residuals*" — the obfuscation probe's own finding names a lexical route |
| **MLS as a probe corpus** | **SPENT** — see [`census/mls/SPENT.md`](census/mls/SPENT.md). The MLS *census* and every figure quoted from it are unaffected; future instrument probes against MLS are foreclosed. TLS, iCalendar and QUIC remain unspent |

## Open, and blocked on a person

Two registered human passes — [`census/human/`](census/human) (H1-R2) and
[`census/human-locality/`](census/human-locality) (HL1) — are frozen, graded, and
**unrun**, awaiting a blind recruit. They are the only instruments that reach both
halves of the confound at once. Neither has been served to anyone.

---

*Provenance for everything here — how each number was reached, which instrument
version produced it, what was tried and failed — is in [`PAPER.md`](PAPER.md) and the
census directories. This file states what is true; those state how we know.*
