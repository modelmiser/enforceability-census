# Rater packet H1 — human rater, iCalendar sample (n = 60)

> **[STATUS BANNER added 2026-08-20 — marked insertion above the packet body. No
> original wording is altered or removed, and nothing inside the embedded rater-pack
> delimiters is touched, so the pack byte-identity assertion and the four-line packet
> diff both still hold against the body below.]**
>
> ⛔ **DO NOT SERVE THIS PACKET TO A RATER. IT IS SUPERSEDED.**
>
> Its return-format examples name two real graded items and give each the archive's
> own label. One of them sits in the H2 clause and is a miss of the largest measured
> failing branch, so that example alone lifts that branch to a PASS at the floor —
> the clause cannot refute what it exists to refute.
>
> **Serve `packet-h1r2.md` instead, and grade with `score_h1r2.py`.** Full
> disclosure, measurement and the superseding registration: `README.md` in this
> directory. This file is retained unchanged as the superseded instrument of record.

You are a rater in an inter-rater reliability study. This packet is
everything you may use. Ground rules:

- **One sitting, roughly 90 minutes.** Pen and paper or a text file.
- **Use only this packet.** No RFC lookups, no web search, no AI
  assistance, no discussing the items with anyone until you have
  returned your labels.
- Below is (1) a RATER PACK — the complete classification
  instrument; read it fully and apply it exactly as written — and
  (2) 60 numbered normative obligations extracted from RFC 5545
  (iCalendar) section 3. The item numbers are their positions in a
  larger corpus; gaps are expected and mean nothing.
- A transport note on the pack: it was written across several
  earlier corpora in this study, so its title and worked examples
  name a different document (RFC 8446 / TLS). That is expected —
  the pack's classes and rules are generic and apply to the
  RFC 5545 items below exactly as written; nothing in it needs
  adapting.
- Classify EVERY item into exactly one class using only the pack.
  Valid labels: DOMAIN, TYPESTATE, REVOCABLE, THRESHOLD,
  CRYPTO-VERIFY, NEGOTIATION, PROCESS, POLICY, META, UNCLASSIFIED.
  (The pack's output section abbreviates CRYPTO-VERIFY as CV,
  NEGOTIATION as NEG, and UNCLASSIFIED as U — either the full name
  or the abbreviation is accepted.)
- Return one line per item, in the form `NUMBER:LABEL`
  (e.g. `13:PROCESS`). If you are genuinely torn between two
  classes, give your best single label with a trailing `?`
  (e.g. `62:DOMAIN?`).

The rater pack follows, then the items.

<!-- PACK-BEGIN -->
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

## CODEBOOK v5 RULES (2026-08-15) — apply together with everything above

**Precedence within v5 — one pipeline.** (i) Rule 19's guard: a
time-windowed duty is REVOCABLE whatever its trigger. (ii) Rule 18's
guard: a duty gating a NAMED packet/message class on a phase event is
rule 18's territory; its worked example stands — RFC 9001's "A client
MUST NOT attempt to decrypt 0-RTT packets it receives and instead MUST
discard them." (iii) Rules 20 and 21 then select which clause of a
reaction or nonaction sentence carries the classified content — rule
20 for duties whose obliged response EMITS something or terminates
the session (abort, close, respond-with-error), rule 21 for silent
suppression (drop, ignore, do not act upon); a silent-suppression duty
is never rule-20 territory, however its trigger reads. (iv) The
selected content — and any sentence rules 20 and 21 do not capture —
classifies under the v4 precedence (rule 19 before rule 16 before rule
18) and the ordinary rules (decision rules 1 and 10, rules 13 and 17),
with rule 22 fixing what "the datum" means wherever rules 10 and 16
use it. Rules 23 and 24 are measurement-protocol rules and classify
nothing. ("Decision rule 1" here and below is the census decision rule
— cross-message consistency = TYPESTATE — not the classifying Rule 1
above; the v4 text used both senses of "rule 1" and this amendment
does not.)

**Rule 20 — Reaction duties: the trigger's predicate classifies; the prescribed
reaction is enforcement mechanics.** For sentences of the form "when/if
C, MUST abort / close / reject / respond with error E" — reaction
meaning the obliged response emits or terminates, per the pipeline's
partition:

- If C states a validity, bound, consistency, or history predicate on
  protocol data, the classified content is C, under the ordinary rules
  (rule 16 for bounds; decision rules 1/10 for cross-message versus
  context-free). The reaction's form — which alert, which error code —
  is enforcement mechanics and never classifies the item. This has
  been the series' de facto convention since the first TLS pass (the
  DOMAIN class is built largely of abort-on-invalid sentences); making
  it explicit adjudicates the QUIC and TLS reaction splits (the third,
  RFC 9001 item 15, falls to the bare-event branch below): a running
  total against an expandable limit is rule 16's non-datum quantity
  (THRESHOLD), however the close-duty is worded; the absence of a
  required element in a prior flight is cross-message under decision
  rule 1 (TYPESTATE), however rule 17's evidence-source note reads — a
  response duty conditioned on prior-message state is decision-rule-1
  territory directly and never needed rule 17's complement test.
- If C is a bare message or signal event carrying no predicate of its
  own (any alert, any close signal) and the reaction is termination or
  non-continuation of the session, the duty is an event-gated
  cessation discipline over all subsequent traffic — stated plainly as
  an EXTENSION of rule 18's TYPESTATE branch to the unnamed universal
  class, which rule 18's own text ("a named packet/message class")
  does not reach by itself: **TYPESTATE**. A transcript observer
  falsifies it by exhibiting post-event traffic beyond the closing
  exchange the spec itself licenses (a CONNECTION_CLOSE and its
  draining-period responses; a closure alert). Disclosed limit,
  recorded at cut time: where the triggering event is locally
  generated and never appears on the wire (a locally raised alert),
  the trigger is off-transcript and rule 11's wire-falsifiability test
  pulls toward PROCESS or U — this branch is the amendment's one
  textually contested bridge.

**Rule 21 — Nonaction (ignore / do-not-act-upon / silent-discard) duties
discriminate on the ignored object's arrival channel.** A nonaction
duty suppresses silently — nothing is emitted and nothing terminates —
so rule 20 does not apply; and the pipeline's guards (i)–(ii) have
already claimed time-windowed duties and phase-gated discards. For the
rest:

- If the ignored object arrives on the protocol's own channel — an
  element of the message grammar of the censused corpus's protocol
  stack (an extension, a reserved field, a malformed or too-small
  packet) — and the handling is fixed and context-free, the duty is
  part of the receiver's parsing contract; a generated binding that
  does not surface the element discharges it: **DOMAIN**, per rule
  10's constant-whenever-applicable reading. Grammar membership is
  judged by the arrival channel, not the element's validity: an
  invalid element that arrives on the protocol's own channel is
  in-grammar. For corpora that specify a composite stack (RFC 9001's
  QUIC+TLS), any layer of that composite is "the protocol's own."
- If the ignored object arrives from OUTSIDE the protocol stack the
  corpus specifies (an ICMP message, an OS signal, out-of-band data),
  the duty is filtering conduct guarding internal state, with no
  predicate on the protocol's own transcript: **PROCESS**, per rule
  13. A numeric bound inside the trigger does not make the filter
  THRESHOLD — the compared quantity is a pure function of the foreign
  datum (rule 16's litmus), and the datum is not protocol data. Where
  the filter protects a floor the spec states elsewhere, that floor
  classifies at its own corpus items, not here.

An in-grammar nonaction duty whose HANDLING is history-conditioned
(ignore exactly the frames that do not increase a negotiated limit)
falls between these branches and is NOT decided by this rule.

**Rule 22 — The datum's boundary is the designated serialization unit.**
Wherever rule 10 asks whether a required value is context-free and
rule 16 whether a quantity is "a pure function of the datum" (rule 17
inherits rule 10's vocabulary), the datum is a complete unit that is
serialized and transmitted as one value. Because layered protocols
nest such units (frame / packet / datagram; handshake message /
record / flight), the unit is DESIGNATED per corpus — in the pass
registration for any future corpus (rule 24), and fixed now for the
measured ones: iCalendar at the transmitted calendar object; TLS 1.3
at the handshake message; QUIC and MLS at the packet/message their
framing defines. Then:

- A consistency requirement among parts of ONE designated unit,
  however many fields or properties it relates and however conditional
  its wording, is a refinement of the unit's type: **DOMAIN**. Litmus:
  could a validator holding only this one unit — and neither
  endpoint's history — check the requirement? Yes → DOMAIN.
- **TYPESTATE** requires the relation to span the unit and a DIFFERENT
  unit ordered in time, or negotiated state (decision rules 1/10).
  Co-transmission does not merge units: two handshake messages of one
  flight, or two records coalesced by the transport, remain distinct
  units, so a relation between them stays cross-message (the archived
  both-rater TYPESTATE reading of TLS's
  CertificateVerify-to-Certificate compatibility duty is preserved,
  not flipped).
- A constraint that relates distinct co-transmitted units with no time
  ordering and no negotiated state — QUIC's
  no-coalescing-across-connection-IDs rule — is a constraint on the
  carrying envelope's composition; the envelope is the datum for that
  item, and the constraint is DOMAIN-eligible.

This is the within-object shadow of decision rule 1's cross-message
consistency: the format genre presents as properties-in-one-object
what protocols present as fields-across-messages, and only the latter
needs state.

## CODEBOOK v6 RULES (2026-08-16) — apply together with everything above

**Rule 25 — Rule 21's first branch requires a unit-local trigger;
recognition predicates are receiver-relative.** A nonaction duty
enters rule 21's first branch (parsing contract, DOMAIN) only when
the predicate selecting WHAT is suppressed is a pure function of the
designated serialization unit (rule 22) plus the spec's own fixed
text — decidable by a validator holding only those two things.
Grammar-invalidity, malformedness, a stated bound, a spec-named
element's identity: the
trigger is unit-local and branch 1 stands, as rule 21 wrote it. A
predicate on the receiver's capability set — an element the receiver
does not recognize, support, implement, or (a fortiori) does not
wish to use, whatever the mandated disposition (ignore, skip,
process the rest, fall back to a named default value): decidable by
NO unit-local validator; the duty is forward-compatibility conduct
guarding no transcript predicate — **PROCESS**, per rule 13. The
generated-binding argument does not transfer to this case: a
catch-all constructor discharges "unrecognized" only relative to ONE
receiver's known set, so what it discharges is each implementation's
conduct toward an open set, not a property of the datum. This is
rule 16's locality litmus ("a pure function of the datum") applied
to the suppression trigger, with rule 22 fixing the datum. Where
rule 21's example list and this rule disagree, this rule governs:
"an extension" is branch-1 territory when the spec identifies it
(prohibited here, unused there) and NOT when the receiver's
non-recognition selects it.

Two scope walls, stated in the rule because the vocabulary invites
crossing them. (1) Rule 25 narrows rule 21 ONLY: recognition
vocabulary inside a REACTION sentence stays rule 20's territory,
where a spec that mandates treating an unknown element as an ERROR
has thereby CLOSED the element space — "unknown" there is
grammar-invalidity, unit-local, and rule 20's abort-on-invalid
convention is untouched (the tolerate-and-proceed disposition marks
an open set; the treat-as-error disposition marks a closed one).
(2) Rule 25 decides single-predicate capability triggers only. It
does NOT decide: mode- and state-conditioned suppression (a
stateless operating mode, a disabled feature);
history-conditioned suppression;
spec-designated-field VALUE-ignores; triggers CONJOINING a unit-local predicate
with a capability predicate; and subordinate ignore
clauses inside compound sentences whose classified content the
pipeline assigns elsewhere.

<!-- PACK-END -->

## The items (classify every one)

[1] When parsing a content line, folded lines MUST first be unfolded according to the unfolding procedure described above.

[2] When parsing a content line, folded lines MUST first be unfolded according to the unfolding procedure described above.

[3] Values in a list of values MUST be separated by a COMMA character.

[7] Multi-valued properties MUST NOT be used to specify multiple language variants of the same value.

[13] Applications MUST ignore x-param and iana-param values they don't recognize.

[16] Applications MUST treat x-name and iana-token values they don't recognize the same way as they would the UNKNOWN value.

[17] The individual calendar address parameter values MUST each be specified in a quoted-string.

[21] The parameter value MUST be the text for either an IANA-registered media type or a non-standard media type.

[22] Applications MUST treat x-name and iana-token values they don't recognize the same way as they would the BUSY value.

[23] The individual calendar address parameter values MUST each be specified in a quoted-string.

[25] Applications MUST treat x-name and iana-token values they don't recognize the same way as they would the NEEDS-ACTION value.

[26] The value "THISANDPRIOR" is deprecated by this revision of iCalendar and MUST NOT be generated by applications.

[27] Applications MUST treat x-name and iana-token values they don't recognize the same way as they would the PARENT value.

[28] Applications MUST treat x-name and iana-token values they don't recognize the same way as they would the REQ-PARTICIPANT value.

[34] The "TZID" property parameter MUST NOT be applied to DATE properties and DATE-TIME or TIME properties whose time values are specified in UTC.

[37] Applications MUST preserve the value data for x-name and iana- token values that they don't recognize without attempting to interpret or parse the value data.

[40] That is, all inline binary data MUST first be character encoded using the "BASE64" encoding method defined in [RFC2045].

[46] Leap seconds MUST NOT be considered when computing an exact duration.

[47] When computing an exact duration, the greatest order time components MUST be added first, that is, the number of days MUST be added first, followed by the number of hours, number of minutes, and number of seconds.

[62] These rule parts MUST be ignored in RECUR value that violate the above requirement (e.g., generated by applications that pre-date this revision of iCalendar).

[63] The BYDAY rule part MUST NOT be specified with a numeric value when the FREQ rule part is not set to MONTHLY or YEARLY.

[64] Furthermore, the BYDAY rule part MUST NOT be specified with a numeric value with the FREQ rule part set to YEARLY when the BYWEEKNO rule part is specified.

[65] The BYMONTHDAY rule part MUST NOT be specified when the FREQ rule part is set to WEEKLY.

[69] Such recurrence instances MUST be ignored and MUST NOT be counted as part of the recurrence set.

[77] The seconds value of 60 MUST only be used to account for positive "leap" seconds.

[79] To properly communicate a fixed time in a property value, either UTC time or local time with time zone reference MUST be specified.

[81] Property values with this value type MUST follow the generic URI syntax defined in [RFC3986].

[82] When a property parameter value is a URI value type, the URI MUST be specified as a quoted-string value.

[84] The HYPHEN-MINUS character MUST be specified for negative UTC offsets (i.e., behind of UTC).

[91] Applications MUST ignore x-comp and iana-comp values they don't recognize.

[92] The following are REQUIRED, but MUST NOT occur more than once.

[98] The following are REQUIRED, but MUST NOT occur more than once.

[111] The "VTIMEZONE" calendar component MUST include the "TZID" property and at least one definition of a "STANDARD" or "DAYLIGHT" sub-component.

[114] In addition, a "VTIMEZONE" calendar component, referred to by a recurring calendar component, MUST provide valid time zone information for all recurrence instances.

[115] "DTSTART" in this usage MUST be specified as a date with a local time value.

[118] *  The "DTSTART" and the "TZOFFSETFROM" properties MUST be used when generating the onset DATE-TIME values (instances) from the "RRULE".

[122] The following is OPTIONAL, but MUST NOT occur more than once.

[124] 'duration' and 'repeat' are both OPTIONAL, and MUST NOT occur more than once each; but if one occurs, so MUST the other.

[134] In an alarm in a "VTODO" calendar component set to trigger on the "END" of the to-do, either the "DUE" property MUST be present, or the "DTSTART" and "DURATION" properties MUST both be present.

[138] The "DESCRIPTION" property of the "VALARM" calendar component MUST be used as the body text of the message, and the "SUMMARY" property MUST be used as the subject text.

[141] If this property is not present in the iCalendar object, then a scheduling transaction MUST NOT be assumed.

[146] Applications MUST treat x-name and iana-token values they don't recognize the same way as they would the PRIVATE value.

[148] The following are OPTIONAL, but MUST NOT occur more than once.

[149] The value MUST be two SEMICOLON-separated FLOAT values.

[150] Receiving applications MUST accept values of this precision and MAY truncate values of greater precision.

[151] The following are OPTIONAL, but MUST NOT occur more than once.

[169] Value MUST match value type

[175] Conformance:  This property MUST be specified in a "VTIMEZONE" calendar component.

[180] Conformance:  This property MUST be specified in "STANDARD" and "DAYLIGHT" sub-components.

[185] A recipient delegated a request MUST inherit the "RSVP" and "ROLE" values from the attendee that delegated the request to them.

[192] This property MUST have the same value type as the "DTSTART" property contained within the recurring component.

[193] Furthermore, this property MUST be specified as a date with local time if and only if the "DTSTART" property contained within the recurring component is specified as a date with local time.

[194] If the value of the "DTSTART" property is a DATE type value, then the value MUST be the calendar date for the recurrence instance.

[200] Description:  The "UID" itself MUST be a globally unique identifier.

[201] The generator of the identifier MUST guarantee that the identifier is unique.

[203] Implementations MUST be able to receive and persist values of at least 255 octets for this property, but they MUST NOT truncate values in the middle of a UTF-8 multi-octet sequence.

[204] However, in such cases, the original "DTSTART" date MUST still be maintained by the calendaring and scheduling system because the original "DTSTART" value has inherent usage dependencies by other properties such as the "RECURRENCE-ID".

[210] Applications MUST ignore alarms with x-name and iana-token values they don't recognize.

[213] The trigger relationship property parameter MUST only be specified when the value type is "DURATION".

[214] Conformance:  This property MUST be specified in the "VALARM" calendar component.

