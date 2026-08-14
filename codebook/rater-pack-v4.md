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

1. **Cross-MESSAGE consistency = TYPESTATE; intra-message cross-field =
   DOMAIN.** "A field of ServerHello MUST equal the corresponding field of
   HelloRetryRequest" is TYPESTATE; "key_share ⊆ supported_groups within the
   same ClientHello" is DOMAIN.
2. **CV requires secret/transcript material.** MAC/signature/PSK-binder
   verification = CV. Public arithmetic on one value = DOMAIN.
3. **Structural bound = DOMAIN; picked policy line = THRESHOLD.** A length
   cap that derives from record framing is DOMAIN; a chosen limit like "no
   more than 7 days" is THRESHOLD.
4. **Sender-side and receiver-side duals of one obligation are both
   classified** — each sentence is its own item.
10. **Guard-vs-predicate tie-break — classify by the discharging type.**
    Many sentences have the form "when/after history H, field F MUST
    satisfy P". Neither guard nor predicate wins by position; ask what type
    would discharge the obligation. If a single context-free refinement of
    F's type satisfies every occurrence of the obligation — the guard only
    *locates* where the obligation applies, and the required value/set is
    the same whenever it does — the check is DOMAIN. If the required
    value/set *varies with history or negotiated state* (same field,
    different required values depending on what happened before), the
    discharging type must be state-indexed: TYPESTATE.
11. **U-boundary — wire-falsifiability.** Classify the strongest obligation
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
12. **NEGOTIATION discriminator — the predicate is the EXISTENCE of a
    compatible choice, never the choice itself.** NEG covers obligations on
    the emptiness/compatibility of a two-party set intersection: abort when
    offer ∩ config = ∅, proceed only if a mutually supported parameter
    exists. The moment the sentence constrains a *specific selected value*
    against what was previously offered ("the server's selected X MUST be
    one the client offered"), it is cross-message consistency and rule 1
    already classifies it: TYPESTATE. Litmus: does the predicate mention a
    chosen value? Then it is not NEG.
13. **DOMAIN vs PROCESS — classify the wire-observable configuration if the
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

---

## CODEBOOK v4 RULES (2026-08-14) — apply together with everything above

**Precedence within v4:** apply rule 19 (deadline) before rule 16 (datum
constants) before rule 18 (lifecycle); rules 15 and 17 are specific-form
tie-breaks under rules 11/12 and 10 respectively and fire only on their
named sentence forms.

**Rule 15 — Capability-compatibility tie-break: classify the transcript-checkable
containment, not the honesty and not the intersection.** Sentences of the
form "party P MUST support the set S required by the group/peer" admit
three rule-grounded readings (U via rule 11's capability-honesty; TYPESTATE
via rule 1's cross-message consistency; NEG via rule 12) — the measured
MLS three-way split. The tie-break: when P's capability *advertisement* is
on the transcript (a LeafNode, a ClientHello extension list), the
obligation's wire-falsifiable content is **containment** — advertised(P) ⊇
S, with S itself negotiated or group state — which is cross-message
consistency: **TYPESTATE**. The honesty residue ("P actually supports what
it advertised") is rule 11's U-residue and is not classified separately
(delete the unobservable clause; the containment check remains). NEG stays
reserved, per rule 12, for existence-of-a-compatible-choice duties
(abort-on-empty-intersection) that constrain no specific party's set
against a required one.

**Rule 16 — Spec-fixed constants: THRESHOLD requires a non-datum quantity, not
just a chosen number.** Decision rule 3's dichotomy (framing-derived =
DOMAIN / operator-chosen = THRESHOLD) is incomplete for constants the spec
itself fixes. The repair discriminates on the *quantity*, not the
constant's provenance:

- A bound on a quantity that is a pure function of the datum at hand
  (a length, a count of elements present, a field's value range) is
  **DOMAIN**, whoever chose the constant and however arbitrary it is —
  a context-free refinement type can carry it. (QUIC's 20-byte CID cap,
  8-byte minimum, at-least-2 parameter floor.)
- **THRESHOLD requires an inequality on a quantity that is NOT a pure
  function of the datum** — a rate, a running total across items — OR a
  constant the spec leaves to deployment discretion. (AEAD *usage*
  limits: the bounded quantity is a cumulative count of encryptions, not
  a property of any message.) For age and elapsed-time quantities the
  ORDER governs, not an exclusion: classifying-rule 1 tests REVOCABLE
  first, and rule 19 captures any duty to act within a time bound; an
  age inequality that survives both — a pure policy line on a
  time-valued metric, carrying no expiry or act-by duty (the class
  definition's original "maximum age someone picked") — remains
  THRESHOLD.

Litmus: could the check be re-run on the lone datum in a vacuum and get
the same answer? Yes → DOMAIN. Needs a counter, a clock, or a knob → not
DOMAIN. (Time-bounded duties go further, to rule 19.)

**Rule 17 — Scope of "occurrence" under rule 10: the complement-state test.**
Rule 10's DOMAIN bullet covers guards that merely *locate* ("the required
value/set is the same whenever it applies"); its TYPESTATE bullet covers
required values that *vary with negotiated state*. The measured gap: a
guard on negotiated or prior-message state around a check whose required
value is fixed *within* the guard. The tie-break is what the spec says in
the guard's complement:

- If in the complement state the same field carries a **different or
  sibling requirement** (another type is required, another structure
  applies, a response duty fires — "X.509v3 *unless explicitly negotiated
  otherwise*"), then the required value/behavior varies with state across
  the field's life: **TYPESTATE**. "Every occurrence" in rule 10
  quantifies over the field's full life, not the guarded subset.
- If in the complement state the spec imposes **no obligation** on the
  field (the guard purely locates; silence elsewhere), the check is
  **DOMAIN** — rule 10's constant-whenever-applicable reading stands,
  however the sentence is guarded.

Evidence source, fixed for blind transmission: the complement duty must
be **visible in the censused corpus and on the same field**; otherwise
the silence branch applies. (A rater holds only the corpus and this
pack — rule 17 never licenses consulting text outside them, and rule
10's worked example survives: no in-corpus sentence imposes a
complement-state requirement on legacy_version's VALUE or STRUCTURE —
the in-corpus sentences naming that field, items 52/53/60, oblige how a
reader USES it, not what it must contain, and consumer-use duties are
not sibling requirements on the field.)

**Rule 18 — Key/phase lifecycle: packet-class discipline is TYPESTATE; key-material
hygiene is PROCESS.** Sentences that gate a **named packet/message class**
on a phase event ("MUST NOT process 1-RTT packets before the handshake
completes", "MUST NOT attempt to decrypt 0-RTT packets and instead MUST
discard them", "records following a Finished MUST be encrypted under the
appropriate traffic key") oblige a phase-indexed send/accept/protect
discipline — the discharging structure is a phase-indexed session/state
type: **TYPESTATE**. Sentences whose **obliged conduct** concerns only the
storage of key material or internal state ("MUST delete outdated key
material", "MUST discard Initial keys when…", "MUST retain old keys
until…", "MUST reset the state of all streams") have no wire-observable
predicate of their own: **PROCESS**, per rule 13. The discriminator is
the gated OBJECT, not the trigger: a phase trigger may name a packet
class ("…when it first sends a Handshake packet") without changing the
duty's object; only when the obliged conduct itself is the sending,
acceptance, processing, or protection of a packet/message class does the
TYPESTATE branch apply. Selecting *which* key
protects a message class is phase discipline (TYPESTATE), **not**
CRYPTO-VERIFY — CV requires verification against secret material, not
selection among installed keys. (This rule's quoted examples are
condensed from RFC 9001 items 37, 34, 14, and 18 and RFC 8446 item 181;
the corpus texts govern.)

**Rule 19 — Deadline duties are REVOCABLE, whatever fixed the number.** A duty to
act within a time window of an event ("acknowledge within max_ack_delay",
"send a packet on PTO expiry", "discard 0-RTT keys within a short time;
the RECOMMENDED time period is three times the Probe Timeout")
is **REVOCABLE**: the license to defer expires, and no check without a
clock can discharge it. The bound's provenance — spec-fixed, derived,
peer-advertised — does not change the clock dependence and never makes
the duty THRESHOLD (a time-since-event quantity is not a pure function
of any datum, so rule 16's DOMAIN branch never captures it, and
classifying-rule 1 already orders REVOCABLE before THRESHOLD). A
deadline is a stated WINDOW after an event — numeric, derived,
advertised, or a spec-stated qualitative window carrying a recommended
numeric ("within a short time; RECOMMENDED…") — while bare ordering
adverbs ("immediately", "as soon as") that sequence a procedural step
allow no elapsed time and are not windows. Applied before
rule 18: a time-bounded key-hygiene duty is REVOCABLE, not PROCESS.

The rule-16/rule-19 seam, stated once: an inequality on a **value
carried in the datum** — including a duration field such as
ticket_lifetime ≤ 604800 — is rule-16 territory (DOMAIN when the
constant is spec-fixed); a duty over **elapsed clock time** — retain,
cache, or use no longer than T after an event — is rule-19 territory
(REVOCABLE).
