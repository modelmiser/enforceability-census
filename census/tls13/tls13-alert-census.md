# TLS 1.3 (RFC 8446 §6.2) error-alert census — 30-minute probe
2026-08-12 · corpus = the 25 declared error alerts, classified on definitional text (predicate shape), never name (mm-residue rule 8). Classes: 0=DOMAIN, 1=THRESHOLD, 2=REVOCABLE, 3=TYPESTATE, U=unclassified (with shape note).

| # | alert | definitional predicate (paraphrase of RFC text) | class | note |
|---|---|---|---|---|
| 1 | unexpected_message | wrong message for current handshake state / premature app data | **3** | textbook ordering-over-own-history |
| 2 | bad_record_mac | record cannot be deprotected (AEAD verify fails) | **U** | CRYPTO-VERIFY shape — exists because of the adversary, not the untyped wire |
| 3 | record_overflow | length > 2^14+256 (or negotiated limit) | **0** | bound IS a presentation-language type (`opaque<0..2^14>`); "negotiated limit" variant is threshold-dynamic |
| 4 | handshake_failure | no acceptable parameter set in offer ∩ config | **U** | NEGOTIATION shape — emptiness of two-party intersection |
| 5 | bad_certificate | corrupt cert / signatures did not verify | **U** | MIXED: parse failure (0) + crypto-verify in one alert |
| 6 | unsupported_certificate | cert type not in supported set | **0** | local-set membership (see eliminability caveat) |
| 7 | certificate_revoked | revoked by its signer | **2** | textbook revocation; clock = CRL/OCSP publication |
| 8 | certificate_expired | expired / not currently valid | **2** | lease shape; clock = wall time vs validity window |
| 9 | certificate_unknown | "some other unspecified issue" | **U** | explicitly unspecified predicate — catch-all |
| 10 | illegal_parameter | field incorrect or inconsistent with other fields (syntax OK) | **0** | cross-field consistency — needs refinement/dependent types, not enums |
| 11 | unknown_ca | chain doesn't reach a known trust anchor | **U** | LOCAL-POLICY membership — legal set is deployment state, not spec |
| 12 | access_denied | valid credential, access control declined | **U** | pure policy decision, no number |
| 13 | decode_error | field out of specified range / length wrong (syntax violation) | **0** | textbook domain — untyped wire |
| 14 | decrypt_error | handshake sig / Finished / PSK binder fails to verify | **U** | CRYPTO-VERIFY |
| 15 | protocol_version | version recognized but not supported | **0** | local-set membership |
| 16 | insufficient_security | server requires parameters MORE SECURE than offered | **1** | ordering on a security scale, line chosen by policy — textbook threshold (ordinal) |
| 17 | internal_error | allocation failure etc., unrelated to peer | **U** | OUT-OF-CORPUS — not a boundary obligation at all |
| 18 | inappropriate_fallback | invalid connection retry (fallback SCSV) | **3?** | AMBIG: history predicate over a PRIOR connection attempt — cross-connection typestate |
| 19 | missing_extension | mandatory-given-negotiated-parameters extension absent | **3** | required-by-prior-message — commit-without-attach shape |
| 20 | unsupported_extension | prohibited-in-context, or not first offered in ClientHello | **3** | echo obligation (response ⊆ request) = history; first clause alone would be 0 (mixed text) |
| 21 | unrecognized_name | no server for the SNI name provided | **0** | local-set membership |
| 22 | bad_certificate_status_response | invalid/unacceptable OCSP response | **U** | MIXED: crypto-verify + freshness (revocable) in one alert |
| 23 | unknown_psk_identity | no acceptable PSK identity | **0** | local-set membership |
| 24 | certificate_required | client cert requested, none provided | **3** | response-to-request obligation (CertificateRequest earlier) |
| 25 | no_application_protocol | ALPN offer ∩ server support = ∅ | **U** | NEGOTIATION |

## Tally (n=25)
- DOMAIN (0): **8** — 32% (record_overflow, unsupported_certificate, illegal_parameter, decode_error, protocol_version, unrecognized_name, unknown_psk_identity + first-clause share of #20 counted at #20's row class, so 7 clean + caveats)
- TYPESTATE (3): **5** — 20% (unexpected_message, inappropriate_fallback?, missing_extension, unsupported_extension, certificate_required; one AMBIG)
- REVOCABLE (2): **2** — 8%
- THRESHOLD (1): **1** — 4%
- UNCLASSIFIED: **9** — 36%
  - CRYPTO-VERIFY: 2 clean (bad_record_mac, decrypt_error) + 2 mixed (bad_certificate, bad_certificate_status_response)
  - NEGOTIATION: 2 (handshake_failure, no_application_protocol)
  - LOCAL-POLICY: 2 (unknown_ca, access_denied)
  - catch-all / out-of-corpus: 2 (certificate_unknown, internal_error)

4-class coverage: 16/25 = 64%. **The unclassified bucket is 36% and internally structured — the scheme does not cover a cryptographic protocol corpus without extension.**

## Findings (30-minute verdict: the probe SUCCEEDS by failing informatively)
1. **The corpus demands at least two new shapes, exactly as Wayland forced DOMAIN into existence:**
   - **CRYPTO-VERIFY** — verification of an adversary-controlled claim (MAC, signature, binder). NOT type-eliminable even in principle: the check exists because of the adversary, not because the wire is untyped. This is the class that separates security protocols from IPC protocols, and it is invisible to the existing taxonomy.
   - **NEGOTIATION** — emptiness/compatibility of a two-party set intersection. No history, no clock, no single value, no number.
2. **Censoring (rule 7): the alert corpus radically under-represents typestate.** The ENTIRE A.1/A.2 state machines — dozens of ordering obligations, the home of the SMACK/FREAK attack family — compress into ONE alert code (unexpected_message). Wayland gives each interface its own ordering errors (172 distinct); TLS quotients them to 25. Alert-set percentages are NOT comparable to Wayland's without normalizing granularity. The real typestate census needs the §4 MUST statements + state machines = the 3-hour version.
3. **Eliminability echo:** 5 of the 8 DOMAIN alerts are membership-in-a-LOCAL-set (SNI names, PSK store, trust anchors, supported versions) — the legal set is deployment state, not spec text, so they are domain-SHAPED but not spec-eliminable. Same boundary the WEnum::Unknown finding drew for versioned enums: a deployed boundary must admit values the spec can't enumerate.
4. **Two alerts are MIXED in their own definitional text** (bad_certificate, bad_certificate_status_response) — the spec itself multiplexes shapes into one code. A classifier without an AMBIG output would have silently absorbed them (honesty rule 2).

## Next (3-hour version, if pursued)
- Census the §4 handshake MUST/MUST NOT statements + A.1/A.2 transitions as the typestate-bearing corpus (est. n≈100+).
- Add CRYPTO-VERIFY and NEGOTIATION as provisional classes; re-run Wayland census to confirm they're empty there (they should be — falsifiable check).
- Prior-art sweep before ANY external claim: state-machine extraction from RFCs is a known genre (e.g., "Extracting protocol FSMs from RFCs" line of work); the CLASS-MIX census angle is the part that looked novel for PromQL.
