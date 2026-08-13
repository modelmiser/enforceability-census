# Wayland CV/NEG falsifiability check — 2026-08-13

The RFC 8446 §4 census introduced two provisional classes (CRYPTO-VERIFY,
NEGOTIATION) and pre-registered a falsifiability check (its caveat 4): the
classes predict **CV = 0 and NEG ≈ 0 among Wayland's declared protocol
errors** — no secret material moves in-protocol, and the registry
version-bind was named as the one NEG candidate. If either class appeared
freely in a corpus with no cryptography and no negotiation, the classes would
be vocabulary, not measurement.

## Method

- Corpus regenerated from source (`extract-corpus.py`): core `wayland.xml` +
  a full `wayland-protocols` checkout (stable + staging + unstable +
  experimental), 2026-08-13 HEAD. **n = 216 declared errors / 92 interfaces /
  46 files** — a superset of the 2026-08 census corpus (172/77/37).
- Scan: vocabulary regexes over `iface.name + summary + desc` —
  CV: `signature|mac|hmac|authenticat|secret|encrypt|decrypt|cipher|key
  exchange|handshake|credential|token`;
  NEG: `negotiat|version|incompatible|intersect|overlap|agree`.
- Every hit hand-adjudicated on predicate shape (rule 8) — the regex is the
  net, not the verdict.
- **Recall limitation, stated:** only regex *hits* were hand-read; the
  non-hits were not individually re-read for CV/NEG shape, so this scan
  bounds false positives tightly and false negatives only indirectly — a
  secret-material or intersection-emptiness predicate phrased without any of
  the net's vocabulary would escape it. The indirect bound: the fitted
  n=172 census hand-classified every item on predicate text (before these
  classes existed) and surfaced no such predicates anywhere in its
  seven buckets.

## Result: prediction CONFIRMED, with one sharpening

Two vocabulary hits, both false positives on predicate reading:

| hit | matched on | actual predicate | class |
|---|---|---|---|
| `xdg_activation_token_v1.already_used` | "token" | "has already been used previously" — a linearity break over the object's history | TYPESTATE |
| `wp_color_representation_surface_v1.pixel_format` | "incompatible" | "the pixel format and a set value are incompatible" — cross-field consistency within one object | DOMAIN-shaped (no peer agreement involved) |

**CV = 0/216. NEG = 0/216.**

The sharpening: the census's one predicted NEG candidate — binding a registry
global at a version above the advertised one — is **not a declared error at
all**. No declared error entry in the entire corpus mentions versions; the
version-bind duty is enforced through the generic `invalid_arguments`
mechanism. So the prediction "NEG ≈ 0, the residual being version-bind"
resolves to exactly 0 *in the declared-error corpus*, with the candidate
living below the declaration layer — an instance of the censoring rule
(rule 7): the declared-error corpus cannot express obligations the protocol
never declares as errors.

Consequence for graduation: CRYPTO-VERIFY's discriminator (secret material)
and NEGOTIATION's (the *existence* of a compatible choice — emptiness of the
two-party intersection, per codebook rule 12, never the selection itself)
pick out nothing in a non-cryptographic, non-negotiated protocol — the
classes carve at a real joint rather than shadowing vocabulary. Graduation
into `codebook/classes.md` still awaits the third-pass convergence of the
TLS census (the other gate). *[Superseded 2026-08-13, later the same day:
the passes did NOT converge — that non-convergence is the recorded pass-4
verdict — and graduation proceeded on this falsifiability result (the one
pre-registered gate) plus a stability criterion articulated at graduation
time; see `codebook/classes.md` "CLASS GRADUATION" for the precise
accounting. The original sentence's "mutual-agreement selection" gloss also
predates rule 12 and is corrected inline above — an instance of exactly the
paraphrase drift rule 14 now guards against.]*

## Incidental observation (NOT a headline — read rule 3's exception)

Running `wayland-classifier.py` on the n=216 superset gives 79.0% eliminable
with an **11.1% UNCLASSIFIED bucket** (census corpus: 87.6% at 1.2%
unclassified). The bucket tripled because post-census protocols use
vocabulary the classifier was never fitted to. Per the codebook, a run with a
large unclassified bucket has no headline; we record it as a live
demonstration of the corpus-fitted-vocabulary caveat that the retraction
addendum attached to the 87.6% figure. Re-fitting the classifier to the
superset (and reporting pre/post per rule 3) is future work; the
falsifiability verdict above does not depend on the classifier.
