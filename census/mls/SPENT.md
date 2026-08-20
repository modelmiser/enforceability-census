# ⚠️ MLS IS SPENT AS A PROBE CORPUS — 2026-08-20

**Read this before designing anything that rates, classifies, or probes RFC 9420
§5–§15.**

`census/mech-probe/` (MECH-PROBE-1) ran a rule-based non-LLM classifier against
this corpus and **compared its output to the archived labels**. The author has
therefore seen per-item agreement on MLS.

**What that forecloses.** Any further rule-writing, pattern-tuning, or
instrument design evaluated against MLS is now a tuning loop — the author cannot
un-see the agreement, so a later "we wrote rules from the codebook alone" claim
is not credible here regardless of intent. That is the mechanism, stated plainly
because it was previously left to inference.

**What is NOT foreclosed.** The MLS census itself (`rfc9420-census.md`, its two
archived raters, and every figure quoted from it) is untouched and unaffected.
MECH-PROBE-1 changed no label, no share, and no published number. This file
constrains *future instrument probes*, not the existing census.

**Still protected and unspent:** TLS §4, iCalendar §3, and QUIC — they carry the
locality claims of PAPER §6.6/§6.7 and must be registered against, never probed.

Full record, including the cold-review correction that withdrew the probe's
original causal claim: [`census/mech-probe/README.md`](../mech-probe/README.md).
