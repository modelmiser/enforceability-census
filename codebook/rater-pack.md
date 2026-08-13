# Rater pack — RFC 8446 §4 obligation classification (codebook v3)

This document is the complete instrument. Classify every numbered sentence in
the corpus you are given. Read only the corpus and this pack. Classify on the
**shape of the predicate in the sentence's own text** — never on names,
labels, or alert words.

## Classes

- **DOMAIN** — a monotone predicate on one value with no reference to
  history: legal-value/range/format/presence checks, and cross-field
  consistency *within a single message*. Decidable public arithmetic on one
  value (e.g., DH point validation, 1 < Y < p-1) is DOMAIN — no secret is
  involved.
- **THRESHOLD** — an inequality against a chosen number: a policy line on a
  continuous quantity (e.g., a maximum age someone picked). A bound that
  derives structurally from framing/presentation-language types is DOMAIN,
  not THRESHOLD.
- **REVOCABLE** — a fact that was true and became false: expiry, staleness,
  supersession, freshness windows. Needs a clock or ordering to check.
- **TYPESTATE** — an ordering obligation over one object's or connection's
  history: "MUST be sent after X", "MUST NOT be sent unless Y happened",
  unexpected-order aborts, and *cross-message* consistency (a field in a
  later message must agree with an earlier message).
- **CV** (CRYPTO-VERIFY) — verification that requires secret or
  transcript-derived cryptographic material: MAC verification, signature
  verification, PSK-binder verification. The discriminator is the secret
  material, not the word "crypto".
- **NEG** (NEGOTIATION) — emptiness/compatibility of a two-party set
  intersection. No history, no clock, no single value, no number. Abort when
  offer ∩ config = ∅; proceed only if a mutually supported parameter exists.
- **PROCESS** — an algorithm or procedure rule with no wire-observable
  predicate of its own: how to compute, how to derive, in what order to
  iterate, to validate-before-using.
- **POLICY** — an operator/deployment-discretion duty with no per-instance
  wire predicate.
- **U** (UNCLASSIFIED-unverifiable) — no per-instance predicate exists even
  in principle (see rule 11 for the exact boundary).
- **META** — an obligation addressed to future specification authors, not to
  implementations.

## Decision rules

*(Rules keep their codebook numbers — the numbering is intentionally
non-sequential. They are set as headings, not a markdown list, so the numbers
render as written.)*

**Rule 1 — Cross-MESSAGE consistency = TYPESTATE; intra-message cross-field =
DOMAIN.** "A field of ServerHello MUST equal the corresponding field of
HelloRetryRequest" is TYPESTATE; "key_share ⊆ supported_groups within the
same ClientHello" is DOMAIN.

**Rule 2 — CV requires secret/transcript material.** MAC/signature/PSK-binder
verification = CV. Public arithmetic on one value = DOMAIN.

**Rule 3 — Structural bound = DOMAIN; picked policy line = THRESHOLD.** A length
cap that derives from record framing is DOMAIN; a chosen limit like "no
more than 7 days" is THRESHOLD.

**Rule 4 — Sender-side and receiver-side duals of one obligation are both
classified** — each sentence is its own item.

**Rule 10 — Guard-vs-predicate tie-break: classify by the discharging type.**
Many sentences have the form "when/after history H, field F MUST
satisfy P". Neither guard nor predicate wins by position; ask what type
would discharge the obligation. If a single context-free refinement of
F's type satisfies every occurrence of the obligation — the guard only
*locates* where the obligation applies, and the required value/set is
the same whenever it does — the check is DOMAIN. If the required
value/set *varies with history or negotiated state* (same field,
different required values depending on what happened before), the
discharging type must be state-indexed: TYPESTATE.

**Rule 11 — U-boundary: wire-falsifiability.** Classify the strongest obligation
a conformance observer of the wire (holding the public transcript,
neither endpoint's private state) could falsify. If the sentence
obliges an observable configuration (send / don't send / set a field in
transcript-establishable circumstances), classify that observable
predicate normally, even if the sentence's motivation is honesty about
capability or intent. U is reserved for sentences whose ENTIRE
normative content is unobservable (truthfulness of an advertisement,
randomness or independence of generated values, future willingness).
Test: could a harness holding only a packet capture ever emit a
conformance FAIL for this sentence alone? No → U. Yes → classify what
the FAIL would check.

**Rule 12 — NEGOTIATION discriminator: the predicate is the EXISTENCE of a
compatible choice, never the choice itself.** NEG covers obligations on
the emptiness/compatibility of a two-party set intersection: abort when
offer ∩ config = ∅, proceed only if a mutually supported parameter
exists. The moment the sentence constrains a *specific selected value*
against what was previously offered ("the server's selected X MUST be
one the client offered"), it is cross-message consistency and rule 1
already classifies it: TYPESTATE. Litmus: does the predicate mention a
chosen value? Then it is not NEG.

**Rule 13 — DOMAIN vs PROCESS: classify the wire-observable configuration if the
sentence obliges one.** "MUST set/encode field F to X" is a predicate
on a wire value: DOMAIN (or TYPESTATE via rule 10 if the required value
is history-dependent). PROCESS is reserved for sentences obliging a
computation or procedure with no wire-observable predicate of their
own.

## Procedure

- Compound sentences: classify the sentence's dominant/primary obligation —
  one label per item.
- Work through all items in order; re-read the sentence before labeling.
- If genuinely torn between two classes, still pick one and append `?`
  (use sparingly).

## Output

Exactly one line per item, format `n:CLASS`, using only the tokens DOMAIN,
THRESHOLD, REVOCABLE, TYPESTATE, CV, NEG, PROCESS, POLICY, U, META. No
commentary, no headers, no blank lines.
