#!/usr/bin/env python3
"""Witness artifacts for the locality study (see README.md — registration
pushed at main 20b62e9 BEFORE any entry below was written).

Graded by `check_witnesses.py`. Each entry names its READING (the
compliance criterion being formalized), its QUOTE (the corpus sentence,
[n] = census item number in census/tls13/rfc8446_s4_musts.txt), and the
artifact: a validator (constructive proof of locality at its rung) or a
distinguishing pair (constructive proof of non-locality — one datum, two
spec-admissible contexts, opposite verdicts).

MODELING CONVENTIONS (disclosed; they bound what the mechanical checks
certify):

1. ABSTRACT MESSAGE MODEL. A msg datum is a dict {"type", "sender",
   ...fields}; a transcript datum is a list of msg dicts in wire order
   (the plaintext handshake abstraction of the registration).
   Cryptographic verification is modeled as a computable relation over
   model components: a signature/MAC is valid iff its recorded key
   identity and coverage match the model's recomputation (see
   `model_verify`). The mechanical checks certify INFORMATION FLOW — the
   validator's inputs are the datum alone — which is the property under
   study; they do not certify cryptographic implementations.

2. ATTRIBUTED ABORTS. In the model, an abort alert may carry the
   condition it responds to ({"type": "alert", "desc": ...,
   "attributed_to": ...}). This mirrors how the census's raters read
   response duties across the archive (abort-with-alert-X duties were
   classified as orderings over observable events, not as unknowable
   intent). Validators for response duties rely on it; the report
   discusses the residue (real TLS alerts carry no attribution field).

3. CHANNEL ATTACHMENT. "party-conduct" and "private-intent" attach to
   the party the sentence obliges; "deployment-policy" covers the
   obliged party's OWN configuration (supported sets, trust anchors,
   certificate inventory); "counterparty-config" the other side's.
   Channels are reported, not graded (registration T3), except the
   secret-material presence checks in T4.

4. EFFICIENT vs INFORMATION LOCALITY (surfaced by T4, discussed in the
   report): with (EC)DHE key establishment, the Finished MAC's validity
   is mathematically determined by the transcript (the shared secret is
   a function of the public shares) but not efficiently computable from
   it. The registered criterion says "computable", so item 180's pair
   deliberately uses a psk_ke-mode handshake, where the key schedule
   depends on an external PSK and even information-locality fails.
"""

# --- model helpers ---------------------------------------------------------


def M(mtype, sender, **fields):
    d = {"type": mtype, "sender": sender}
    d.update(fields)
    return d


def th(transcript_prefix):
    """Model transcript hash: a deterministic digest of the prefix."""
    return "th(%s)" % ",".join(
        m["type"] for m in transcript_prefix)


def model_verify(cv, cert_msg, prefix):
    """Model signature verification: valid iff the signature names the
    end-entity key and covers the model transcript hash of the prefix."""
    sig = cv.get("sig", {})
    key = cert_msg["certs"][0].get("key_id")
    return sig.get("key") == key and sig.get("over") == th(prefix)


def find(tr, mtype, sender=None):
    for i, m in enumerate(tr):
        if m["type"] == mtype and (sender is None or m["sender"] == sender):
            return i, m
    return None, None


def ctx(desc, channel, verdict, quote):
    return {"desc": desc, "channel": channel, "verdict": verdict,
            "quote": quote}


def PAIR(item, reading, datum, c1, c2, eligible=True):
    return {"item": item, "reading": reading, "rung": "nonlocal",
            "eligible": eligible, "kind": "pair",
            "pair": {"datum_kind": "transcript", "datum": datum,
                     "contexts": [c1, c2]}}


def VAL(item, reading, rung, fn, accept, reject, quote, eligible=True,
        pair_msg=None):
    w = {"item": item, "reading": reading, "rung": rung,
         "eligible": eligible, "kind": "validator", "fn": fn,
         "accept": accept, "reject": reject, "quote": quote}
    if pair_msg is not None:
        w["pair_msg"] = pair_msg
    return w


def MPAIR(datum, c1, c2):
    return {"datum_kind": "msg", "datum": datum, "contexts": [c1, c2]}


# Compatibility of signature schemes with key kinds (RFC 8446 §4.2.3).
COMPAT = {("rsa_pss_rsae_sha256", "rsa"), ("rsa_pkcs1_sha256", "rsa"),
          ("ecdsa_secp256r1_sha256", "ecdsa_p256"),
          ("ecdsa_secp384r1_sha384", "ecdsa_p384"),
          ("ed25519", "ed25519")}

# RFC 8446 downgrade sentinels (§4.1.3), abbreviated model constants.
S12 = "sentinel_tls12"   # 44 4F 57 4E 47 52 44 01
S11 = "sentinel_tls11"   # 44 4F 57 4E 47 52 44 00

CERT_ALERTS = {"unsupported_certificate", "bad_certificate",
               "certificate_expired", "certificate_revoked",
               "certificate_unknown", "unknown_ca"}

Q = {
    3: 'If there is no overlap between the received "supported_groups" '
       'and the groups supported by the server, then the server MUST '
       'abort the handshake with a "handshake_failure" or an '
       '"insufficient_security" alert. [3]',
    6: 'If the server is unable to negotiate a supported set of '
       'parameters (i.e., there is no overlap between the client and '
       'server parameters), it MUST abort the handshake with either a '
       '"handshake_failure" or "insufficient_security" fatal alert (see '
       'Section 6). [6]',
    23: 'This structure is generated by the server and MUST be generated '
        'independently of the ClientHello.random. [23]',
    53: 'If this extension is present in the ClientHello, servers MUST '
        'NOT use the ClientHello.legacy_version value for version '
        'negotiation and MUST use only the "supported_versions" '
        'extension to determine client preferences. [53]',
    59: 'Clients MUST check for this extension prior to processing the '
        'rest of the ServerHello (although they will have to [59] '
        '[corpus sentence truncated at source — an extraction artifact '
        'of the frozen corpus, which is what all fourteen raters rated; '
        'the RFC continues: "parse the ServerHello in order to read '
        'the extension)."]',
    60: 'If this extension is present, clients MUST ignore the '
        'ServerHello.legacy_version value and MUST use only the '
        '"supported_versions" extension to determine the selected '
        'version. [60]',
    69: 'If the public key is carried in an X.509 certificate, it MUST '
        'use the rsaEncryption OID [RFC5280]. [69]',
    72: 'When used in certificate signatures, the algorithm parameters '
        'MUST be DER encoded. [72]',
    91: 'The key_exchange values for each KeyShareEntry MUST be '
        'generated independently. [91]',
    110: 'If the client opts to do so, it MUST supply both the '
         '"pre_shared_key" and "early_data" extensions. [110]',
    126: 'If this value is not present or does not validate, the server '
         'MUST abort the handshake. [126] (the value is the PSK binder, '
         'per the preceding sentence, item 125)',
    133: 'Clients MUST NOT attempt to use tickets which have ages '
         'greater than the "ticket_lifetime" value which was provided '
         'with the ticket. [133]',
    137: 'This message, if sent, MUST follow EncryptedExtensions. [137] '
         '(the message is CertificateRequest)',
    138: 'The certificate_request_context MUST be unique within the '
         'scope of this connection (thus preventing replay of client '
         'CertificateVerify messages). [138]',
    175: 'In addition, the signature algorithm MUST be compatible with '
         'the key in the sender\'s end-entity certificate. [175]',
    178: 'The receiver of a CertificateVerify message MUST verify the '
         'signature field. [178]',
    180: 'Recipients of Finished messages MUST verify that the contents '
         'are correct and if incorrect MUST terminate the connection '
         'with a "decrypt_error" alert. [180]',
}

WITNESSES = []

# === T1 — stable DOMAIN {69, 110, 72}: msg validators ======================

WITNESSES.append(VAL(
    69,
    "An X.509-carried public key offered for use with the RSASSA-PSS "
    "code points carries the rsaEncryption OID; decidable from the "
    "Certificate message alone.",
    "msg",
    lambda m: bool(all(e.get("key_oid") == "rsaEncryption"
                       for e in m["certs"]
                       if e.get("key_kind") == "rsa")),
    accept=[M("certificate", "server",
              certs=[{"key_kind": "rsa", "key_oid": "rsaEncryption"}]),
            M("certificate", "server",
              certs=[{"key_kind": "ecdsa_p256", "key_oid": "id-ecPublicKey"}])],
    reject=[M("certificate", "server",
              certs=[{"key_kind": "rsa", "key_oid": "id-RSASSA-PSS"}])],
    quote=Q[69]))

WITNESSES.append(VAL(
    110,
    "Early-data offering is extension co-presence: a ClientHello "
    "carrying \"early_data\" also carries \"pre_shared_key\" (opting in "
    "is observable only as the early_data extension; a client that sends "
    "neither has not exercised the duty).",
    "msg",
    lambda m: bool(not ("early_data" in m["ext"]
                        and "pre_shared_key" not in m["ext"])),
    accept=[M("client_hello", "client",
              ext=["pre_shared_key", "early_data"]),
            M("client_hello", "client", ext=["pre_shared_key"]),
            M("client_hello", "client", ext=["key_share"])],
    reject=[M("client_hello", "client", ext=["early_data"])],
    quote=Q[110]))

WITNESSES.append(VAL(
    72,
    "Algorithm parameters of certificate signatures are DER encoded; a "
    "property of the certificate bytes in the Certificate message.",
    "msg",
    lambda m: bool(all(e.get("sig_params_encoding") == "DER"
                       for e in m["certs"])),
    accept=[M("certificate", "server",
              certs=[{"sig_params_encoding": "DER"}])],
    reject=[M("certificate", "server",
              certs=[{"sig_params_encoding": "BER"}])],
    quote=Q[72]))

# === T2 — stable TYPESTATE {175, 137, 138}: transcript validators ==========


def v175(tr):
    _, cert = find(tr, "certificate", "server")
    _, cv = find(tr, "certificate_verify", "server")
    if cert is None or cv is None:
        return True
    return bool((cv["alg"], cert["certs"][0]["key_kind"]) in COMPAT)


WITNESSES.append(VAL(
    175,
    "The CertificateVerify signature algorithm is compatible with the "
    "end-entity key of the previously sent Certificate — a relation "
    "between two messages of one connection.",
    "transcript", v175,
    accept=[[M("certificate", "server",
               certs=[{"key_kind": "rsa", "key_id": "K1"}]),
             M("certificate_verify", "server", alg="rsa_pss_rsae_sha256")],
            [M("client_hello", "client", ext=[])]],
    reject=[[M("certificate", "server",
               certs=[{"key_kind": "ecdsa_p256", "key_id": "K2"}]),
             M("certificate_verify", "server", alg="rsa_pss_rsae_sha256")]],
    quote=Q[175],
    pair_msg=MPAIR(
        M("certificate_verify", "server", alg="rsa_pss_rsae_sha256"),
        ctx("The Certificate sent earlier in this connection carries an "
            "RSA end-entity key: the algorithm is compatible.",
            "other-messages", True, Q[175]),
        ctx("The Certificate sent earlier carries a P-256 ECDSA key: the "
            "same CertificateVerify message now violates the duty.",
            "other-messages", False, Q[175]))))


def v137(tr):
    icr, cr = find(tr, "certificate_request", "server")
    if cr is None:
        return True
    iee, ee = find(tr, "encrypted_extensions", "server")
    return bool(ee is not None and iee < icr)


WITNESSES.append(VAL(
    137,
    "CertificateRequest, if sent, appears after EncryptedExtensions — "
    "an ordering over the connection's message sequence.",
    "transcript", v137,
    accept=[[M("encrypted_extensions", "server"),
             M("certificate_request", "server")],
            [M("encrypted_extensions", "server")]],
    reject=[[M("certificate_request", "server"),
             M("encrypted_extensions", "server")]],
    quote=Q[137],
    pair_msg=MPAIR(
        M("certificate_request", "server", context="c0"),
        ctx("EncryptedExtensions was sent before this message in the "
            "connection: compliant.", "other-messages", True, Q[137]),
        ctx("EncryptedExtensions had not yet been sent when this message "
            "went out: violation.", "other-messages", False, Q[137]))))


def v138(tr):
    ctxs = [m["context"] for m in tr
            if m["type"] == "certificate_request"]
    return bool(len(ctxs) == len(set(ctxs)))


WITNESSES.append(VAL(
    138,
    "certificate_request_context values are pairwise distinct across the "
    "CertificateRequests of one connection — a uniqueness predicate over "
    "the connection's history.",
    "transcript", v138,
    accept=[[M("certificate_request", "server", context="a"),
             M("certificate_request", "server", context="b")],
            [M("certificate_request", "server", context="a")]],
    reject=[[M("certificate_request", "server", context="a"),
             M("certificate_request", "server", context="a")]],
    quote=Q[138],
    pair_msg=MPAIR(
        M("certificate_request", "server", context="a"),
        ctx("No earlier CertificateRequest in this connection used "
            "context \"a\": compliant.", "other-messages", True, Q[138]),
        ctx("An earlier CertificateRequest in this connection already "
            "used context \"a\": violation.", "other-messages", False,
            Q[138]))))

# === T3 — stable non-local: transcript-level distinguishing pairs ==========

WITNESSES.append(PAIR(
    53,
    "The server determines version preferences from the "
    "supported_versions list alone, never from legacy_version — a "
    "constraint on the server's selection computation.",
    [M("client_hello", "client", legacy_version=0x0303,
       ext=["supported_versions"], supported_versions=[0x0304]),
     M("server_hello", "server", ext=["supported_versions"],
       selected_version=0x0304)],
    ctx("The server computed its selection from the supported_versions "
        "list alone: compliant.", "party-conduct", True, Q[53]),
    ctx("The server consulted legacy_version in its selection logic and "
        "happened to reach the same choice: the duty is violated with an "
        "identical transcript.", "party-conduct", False, Q[53])))

WITNESSES.append(PAIR(
    59,
    "The client checks for the supported_versions extension before "
    "processing the rest of the ServerHello — an ordering over the "
    "client's internal processing.",
    [M("client_hello", "client", ext=["supported_versions"]),
     M("server_hello", "server", ext=["supported_versions"],
       selected_version=0x0304)],
    ctx("The client located the extension first, then processed the "
        "remaining fields: compliant.", "party-conduct", True, Q[59]),
    ctx("The client processed the other ServerHello fields first and "
        "checked for the extension last; every message is unchanged.",
        "party-conduct", False, Q[59])))

WITNESSES.append(PAIR(
    60,
    "The client determines the selected version from the "
    "supported_versions extension alone, ignoring "
    "ServerHello.legacy_version — a constraint on the client's "
    "computation.",
    [M("client_hello", "client", ext=["supported_versions"]),
     M("server_hello", "server", legacy_version=0x0303,
       ext=["supported_versions"], selected_version=0x0304)],
    ctx("The client read the selected version from the extension: "
        "compliant.", "party-conduct", True, Q[60]),
    ctx("The client derived the version from legacy_version, "
        "coincidentally agreeing; the transcript is identical.",
        "party-conduct", False, Q[60])))

WITNESSES.append(PAIR(
    3,
    "On empty intersection between the ClientHello's supported_groups "
    "and the groups the server supports, the server aborts — the duty's "
    "trigger references the server's own configured set.",
    [M("client_hello", "client", supported_groups=["x25519"]),
     M("server_hello", "server", group="x25519")],
    ctx("The server's configured group set includes x25519: the overlap "
        "is non-empty, no abort duty fires, proceeding is compliant.",
        "deployment-policy", True, Q[3]),
    ctx("The server's configured group set is {secp256r1} — disjoint "
        "from the offer. It was obliged to abort, yet the identical "
        "transcript shows it proceeding (selecting a group outside its "
        "configured support).", "deployment-policy", False, Q[3])))

WITNESSES.append(PAIR(
    6,
    "On failure to negotiate a supported parameter set, the server "
    "aborts with a fatal alert — triggered by the relation between the "
    "offer and the server's configured parameters.",
    [M("client_hello", "client", cipher_suites=["TLS_AES_128_GCM_SHA256"]),
     M("server_hello", "server", cipher_suite="TLS_AES_128_GCM_SHA256")],
    ctx("The server's configuration supports the offered suite: "
        "proceeding is compliant.", "deployment-policy", True, Q[6]),
    ctx("The server's configuration supports none of the offered "
        "parameters; the duty to abort fired and the identical "
        "transcript shows it proceeding instead.", "deployment-policy",
        False, Q[6])))

WITNESSES.append(PAIR(
    133,
    "A ticket is not used past the age bound its NewSessionTicket "
    "stated — deciding any use requires elapsed time since issuance.",
    [M("client_hello", "client", ext=["pre_shared_key"],
       psk_identities=["ticket-T"])],
    ctx("Ticket T was issued with ticket_lifetime 86400 s and one hour "
        "has elapsed at this use: compliant.", "clock", True, Q[133]),
    ctx("The same ticket was issued with the same lifetime and 26 hours "
        "have elapsed at this use: the identical ClientHello violates "
        "the duty.", "clock", False, Q[133])))

WITNESSES.append(PAIR(
    91,
    "key_exchange values are generated independently — a property of "
    "the generation process, not of the emitted values.",
    [M("client_hello", "client",
       key_shares=[{"group": "x25519", "kex": "A"},
                   {"group": "secp256r1", "kex": "B"}])],
    ctx("Both values came from independent draws of a CSPRNG: "
        "compliant.", "generation-process", True, Q[91]),
    ctx("The second value was derived deterministically from the first; "
        "the emitted bytes are identical.", "generation-process", False,
        Q[91])))

WITNESSES.append(PAIR(
    23,
    "The server's Random is generated independently of "
    "ClientHello.random — again a process property invisible in the "
    "values.",
    [M("client_hello", "client", random="R1"),
     M("server_hello", "server", random="R2")],
    ctx("R2 was drawn independently of R1: compliant.",
        "generation-process", True, Q[23]),
    ctx("R2 was computed as a function of R1, yielding the same bytes: "
        "violation with an identical transcript.", "generation-process",
        False, Q[23])))

# === T4 — the CV split =====================================================

WITNESSES.append(PAIR(
    178,
    "Literal-conduct reading: the receiver PERFORMS signature "
    "verification. A valid signature never verified leaves every "
    "message unchanged.",
    [M("certificate", "server", certs=[{"key_kind": "rsa",
                                        "key_id": "K1"}]),
     M("certificate_verify", "server", alg="rsa_pss_rsae_sha256",
       sig={"key": "K1", "over": "th(certificate)"}),
     M("finished", "server"), M("finished", "client")],
    ctx("The client ran signature verification before proceeding: "
        "compliant.", "party-conduct", True, Q[178]),
    ctx("The client skipped verification and proceeded; the signature "
        "happened to be valid, so the transcript is identical.",
        "party-conduct", False, Q[178])))


def v178(tr):
    icv, cv = find(tr, "certificate_verify", "server")
    if cv is None:
        return True
    _, cert = find(tr, "certificate", "server")
    if cert is None:
        return False
    if model_verify(cv, cert, tr[:icv]):
        return True
    # Signature does not verify: the connection must not proceed —
    # the next client event must be a decrypt_error alert.
    rest = tr[icv + 1:]
    client_events = [m for m in rest if m["sender"] == "client"]
    return bool(client_events
                and client_events[0]["type"] == "alert"
                and client_events[0]["desc"] == "decrypt_error")


_t178_valid = [
    M("certificate", "server", certs=[{"key_kind": "rsa",
                                       "key_id": "K1"}]),
    M("certificate_verify", "server", alg="rsa_pss_rsae_sha256",
      sig={"key": "K1", "over": "th(certificate)"}),
    M("finished", "server"), M("finished", "client")]
_t178_invalid_abort = [
    M("certificate", "server", certs=[{"key_kind": "rsa",
                                       "key_id": "K1"}]),
    M("certificate_verify", "server", alg="rsa_pss_rsae_sha256",
      sig={"key": "K-OTHER", "over": "th(certificate)"}),
    M("alert", "client", desc="decrypt_error")]
_t178_invalid_continue = [
    M("certificate", "server", certs=[{"key_kind": "rsa",
                                       "key_id": "K1"}]),
    M("certificate_verify", "server", alg="rsa_pss_rsae_sha256",
      sig={"key": "K-OTHER", "over": "th(certificate)"}),
    M("finished", "server"), M("finished", "client")]

WITNESSES.append(VAL(
    178,
    "Consequentialist reading: the receiver does not proceed as though "
    "the CertificateVerify were valid when the signature does not "
    "verify. Signature validity is computable from the transcript alone "
    "— the verification key is the end-entity key of the Certificate "
    "message, and the covered content is the transcript hash. No secret "
    "is involved (contrast items 126 and 180). EXTRA-ELIGIBLE: excluded "
    "from item outcomes per the registration. Degenerate-input note: a "
    "transcript with a CertificateVerify but no Certificate is rejected "
    "conservatively (outside the vectors; reader-graded).",
    "transcript", v178,
    accept=[_t178_valid, _t178_invalid_abort],
    reject=[_t178_invalid_continue],
    quote=Q[178] + ' Verification key and coverage: "the signature '
          'algorithm MUST be compatible with the key in the sender\'s '
          'end-entity certificate" [175]; the census\'s own decision '
          'rule 2 marks the secret as the discriminator.',
    eligible=False,
    pair_msg=MPAIR(
        M("certificate_verify", "server", alg="rsa_pss_rsae_sha256",
          sig={"key": "K1", "over": "th(certificate)"}),
        ctx("The Certificate in this connection carries key K1 and the "
            "connection continued: the signature verifies; compliant.",
            "other-messages", True, Q[178]),
        ctx("The Certificate carries a different key, the signature "
            "does not verify, and the connection continued anyway: "
            "violation — decidable only with the other message in "
            "view.", "other-messages", False, Q[178]))))

WITNESSES.append(PAIR(
    126,
    "Consequentialist reading of the binder duty: the server does not "
    "proceed when the PSK binder fails to validate. Validation is an "
    "HMAC keyed from the PSK secret, which no message carries.",
    [M("client_hello", "client", ext=["pre_shared_key"],
       psk_identities=["ext-psk-1"], binder="B"),
     M("server_hello", "server", ext=["pre_shared_key"],
       psk_selected_identity=0)],
    ctx("The externally provisioned PSK secret is S1, under which "
        "binder B validates over the ClientHello prefix: proceeding is "
        "compliant.", "secret-material", True, Q[126]),
    ctx("The PSK secret is S2, under which B does not validate: the "
        "server was obliged to abort, and the identical transcript "
        "shows it proceeding.", "secret-material", False, Q[126])))

WITNESSES.append(PAIR(
    180,
    "Consequentialist reading of Finished verification: the recipient "
    "terminates with decrypt_error when the Finished MAC is incorrect. "
    "In a psk_ke handshake the MAC key derives from the external PSK "
    "alone, so correctness is undecidable from the transcript (see "
    "header convention 4 for why psk_ke is the honest mode here).",
    [M("client_hello", "client", ext=["pre_shared_key",
                                      "psk_key_exchange_modes"],
       psk_modes=["psk_ke"], psk_identities=["ext-psk-1"]),
     M("server_hello", "server", ext=["pre_shared_key"],
       psk_selected_identity=0),
     M("finished", "server", mac="F"),
     M("finished", "client", mac="G")],
    ctx("The PSK secret is S1; the server Finished MAC F is correct "
        "under the key schedule from S1: continuing is compliant.",
        "secret-material", True, Q[180]),
    ctx("The PSK secret is S2; F is incorrect under S2's key schedule: "
        "the client was obliged to terminate with decrypt_error, and "
        "the identical transcript shows it continuing.",
        "secret-material", False, Q[180])))

# === Contested items =======================================================

Q2 = {
    22: 'The last 8 bytes MUST be overwritten as described below if '
        'negotiating TLS 1.2 or TLS 1.1, but the remaining bytes MUST be '
        'random. [22] (ServerHello.Random)',
    30: 'TLS 1.3 servers which negotiate TLS 1.2 or below in response '
        'to a ClientHello MUST set the last 8 bytes of their Random '
        'value specially in their ServerHello. [30]',
    31: 'If negotiating TLS 1.2, TLS 1.3 servers MUST set the last 8 '
        'bytes of their Random value to the bytes: [31] (the 8-byte '
        'value follows in the RFC text)',
    32: 'If negotiating TLS 1.1 or below, TLS 1.3 servers MUST, and '
        'TLS 1.2 servers SHOULD, set the last 8 bytes of their '
        'ServerHello.Random value to the bytes: [32]',
    52: 'If this extension is not present, servers which are compliant '
        'with this specification and which also support TLS 1.2 MUST '
        'negotiate TLS 1.2 or prior as specified in [RFC5246], even if '
        'ClientHello.legacy_version is 0x0304 or later. [52]',
    55: 'Servers MUST be prepared to receive ClientHellos that include '
        'this extension but do not include 0x0304 in the list of '
        'versions. [55]',
    56: 'A server which negotiates a version of TLS prior to TLS 1.3 '
        'MUST set ServerHello.version and MUST NOT send the '
        '"supported_versions" extension. [56]',
    57: 'A server which negotiates TLS 1.3 MUST respond by sending a '
        '"supported_versions" extension containing the selected version '
        'value (0x0304). [57]',
    65: 'The keys found in certificates MUST also be of appropriate '
        'type for the signature algorithms they are used with. [65]',
    66: 'Clients which desire the server to authenticate itself via a '
        'certificate MUST send the "signature_algorithms" extension. '
        '[66]',
    67: 'If a server is authenticating via a certificate and the client '
        'has not sent a "signature_algorithms" extension, then the '
        'server MUST abort the handshake with a "missing_extension" '
        'alert (see Section 9.2). [67]',
    75: 'TLS 1.3 servers MUST NOT offer a SHA-1 signed certificate '
        'unless no valid certificate chain can be produced without it '
        '(see Section 4.4.2.2). [75]',
    79: 'If TLS 1.2 is negotiated, implementations MUST be prepared to '
        'accept a signature that uses any curve that they advertised in '
        'the "supported_groups" extension. [79]',
    80: '-  Implementations that advertise support for RSASSA-PSS '
        '(which is mandatory in TLS 1.3) MUST be prepared to accept a '
        'signature using that scheme even when TLS 1.2 is negotiated. '
        '[80]',
    89: 'Clients MUST NOT act upon any information found in '
        '"supported_groups" prior to successful completion of the '
        'handshake but MAY use the information learned from a '
        'successfully completed handshake to change what groups they '
        'use in their "key_share" extension in subsequent connections. '
        '[89]',
    111: 'The PSK used to encrypt the early data MUST be the first PSK '
         'listed in the client\'s "pre_shared_key" extension. [111]',
    122: 'For identities established externally, an obfuscated_ticket_'
         'age of 0 SHOULD be used, and servers MUST ignore the value. '
         '[122]',
    123: 'For externally established PSKs, the Hash algorithm MUST be '
         'set when [123] [corpus sentence truncated at source — an '
         'extraction artifact of the frozen corpus, which is what all '
         'fourteen raters rated; the RFC continues: "the PSK is '
         'established or default to SHA-256 if no such algorithm is '
         'defined."]',
    124: 'The server MUST ensure that it selects a compatible PSK (if '
         'any) and cipher suite. [124]',
    147: 'Otherwise (in the case of server authentication), this field '
         'SHALL be zero length. [147] (certificate_request_context)',
    157: 'TLS 1.3 servers MUST be able to process ClientHello messages '
         'that include it, as it MAY be sent by clients that wish to '
         'use it in earlier protocol versions. [157] (status_request_v2, '
         'per item 156)',
    164: 'If the client cannot construct an acceptable chain using the '
         'provided certificates and decides to abort the handshake, '
         'then it MUST abort the handshake with an appropriate '
         'certificate-related alert (by default, "unsupported_'
         'certificate"; see Section 6.2 for more information). [164]',
    184: 'Servers MUST NOT send this message, and clients receiving it '
         'MUST terminate the connection with an "unexpected_message" '
         'alert. [184] (EndOfEarlyData, per items 182-183)',
    187: 'On resumption, if reporting an SNI value to the calling '
         'application, implementations MUST use the value sent in the '
         'resumption ClientHello rather than the value sent in the '
         'previous session. [187]',
    188: 'Servers MUST NOT use any value greater than 604800 seconds '
         '(7 days). [188] (ticket_lifetime)',
    189: 'Clients MUST NOT cache tickets for longer than 7 days, '
         'regardless of the ticket_lifetime, and MAY delete tickets '
         'earlier based on local policy. [189]',
    197: 'Note: Because client authentication could involve prompting '
         'the user, servers MUST be prepared for some delay, including '
         'receiving an arbitrary number of other messages between '
         'sending the CertificateRequest and receiving a response. '
         '[197]',
}

# --- The downgrade-sentinel / version-encoding family: 22, 30, 31, 32,
# --- 56, 57. The guard "negotiating version X" is encoded in the
# --- ServerHello itself (items 56/57 fix the encoding: pre-1.3 selection
# --- = supported_versions ABSENT), so the guarded duties are msg-local.

WITNESSES.append(VAL(
    22,
    "Overwrite half of [22], guard in-datum: a ServerHello whose own "
    "encoding signals pre-1.3 negotiation (no supported_versions "
    "extension, per items 56/57) carries a downgrade sentinel in its "
    "Random's last 8 bytes.",
    "msg",
    lambda m: bool("supported_versions" in m["ext"]
                   or m["random_last8"] in (S12, S11)),
    accept=[M("server_hello", "server", ext=[], random_last8=S12),
            M("server_hello", "server", ext=["supported_versions"],
              random_last8="random_tail")],
    reject=[M("server_hello", "server", ext=[],
              random_last8="random_tail")],
    quote=Q2[22]))

WITNESSES.append(PAIR(
    22,
    "Randomness half of [22]: the remaining bytes of the Random are "
    "random — a generation-process property.",
    [M("server_hello", "server", ext=[], random_first24="X24",
       random_last8=S12)],
    ctx("The first 24 bytes came from a CSPRNG: compliant.",
        "generation-process", True, Q2[22]),
    ctx("The first 24 bytes came from a deterministic counter, "
        "producing the same octets: violation with an identical "
        "message.", "generation-process", False, Q2[22])))

WITNESSES.append(VAL(
    30,
    "A ServerHello signalling pre-1.3 negotiation (no supported_versions "
    "extension) carries one of the two downgrade sentinels — the guard "
    "is the message's own version encoding.",
    "msg",
    lambda m: bool("supported_versions" in m["ext"]
                   or m["random_last8"] in (S12, S11)),
    accept=[M("server_hello", "server", ext=[], random_last8=S11)],
    reject=[M("server_hello", "server", ext=[],
              random_last8="random_tail")],
    quote=Q2[30]))

WITNESSES.append(VAL(
    31,
    "TLS 1.2 selection (no supported_versions extension; version field "
    "0x0303) requires the TLS 1.2 sentinel specifically.",
    "msg",
    lambda m: bool("supported_versions" in m["ext"]
                   or m["selected_version_legacy"] != 0x0303
                   or m["random_last8"] == S12),
    accept=[M("server_hello", "server", ext=[],
              selected_version_legacy=0x0303, random_last8=S12),
            M("server_hello", "server", ext=[],
              selected_version_legacy=0x0302, random_last8=S11)],
    reject=[M("server_hello", "server", ext=[],
              selected_version_legacy=0x0303, random_last8=S11)],
    quote=Q2[31]))

WITNESSES.append(VAL(
    32,
    "TLS 1.1-or-below selection (no supported_versions extension; "
    "version field 0x0302 or lower) requires the TLS 1.1 sentinel.",
    "msg",
    lambda m: bool("supported_versions" in m["ext"]
                   or m["selected_version_legacy"] > 0x0302
                   or m["random_last8"] == S11),
    accept=[M("server_hello", "server", ext=[],
              selected_version_legacy=0x0302, random_last8=S11)],
    reject=[M("server_hello", "server", ext=[],
              selected_version_legacy=0x0301, random_last8=S12)],
    quote=Q2[32]))

WITNESSES.append(VAL(
    56,
    "In-datum consistency of the pre-1.3 encoding: a ServerHello "
    "without the supported_versions extension carries a valid pre-1.3 "
    "selected version in its version field (the MUST-set half; the "
    "MUST-NOT-send half is this same encoding read in the other "
    "direction).",
    "msg",
    lambda m: bool("supported_versions" in m["ext"]
                   or m["selected_version_legacy"] in (0x0303, 0x0302,
                                                       0x0301)),
    accept=[M("server_hello", "server", ext=[],
              selected_version_legacy=0x0303)],
    reject=[M("server_hello", "server", ext=[],
              selected_version_legacy=0x0304)],
    quote=Q2[56]))

WITNESSES.append(VAL(
    57,
    "A ServerHello carrying the supported_versions extension carries "
    "0x0304 in it — the TLS 1.3 selection encoding is in-datum.",
    "msg",
    lambda m: bool("supported_versions" not in m["ext"]
                   or m["selected_version_ext"] == 0x0304),
    accept=[M("server_hello", "server", ext=["supported_versions"],
              selected_version_ext=0x0304)],
    reject=[M("server_hello", "server", ext=["supported_versions"],
              selected_version_ext=0x0303)],
    quote=Q2[57]))

# --- 188: the provenance fight over a msg-local check ----------------------

WITNESSES.append(VAL(
    188,
    "ticket_lifetime does not exceed 604800 — an inequality on a value "
    "carried in the NewSessionTicket (the same predicate whichever "
    "class vocabulary names the constant's provenance).",
    "msg",
    lambda m: bool(m["ticket_lifetime"] <= 604800),
    accept=[M("new_session_ticket", "server", ticket_lifetime=604800),
            M("new_session_ticket", "server", ticket_lifetime=3600)],
    reject=[M("new_session_ticket", "server", ticket_lifetime=604801)],
    quote=Q2[188]))

# --- 65: intra-chain reading (msg) + CertificateVerify reading (transcript)

WITNESSES.append(VAL(
    65,
    "Intra-chain reading: within the Certificate message, each "
    "certificate's signature algorithm is compatible with its issuer's "
    "key type (issuer = next entry in the chain).",
    "msg",
    lambda m: bool(all(
        (m["certs"][i]["sig_alg"], m["certs"][i + 1]["key_kind"])
        in COMPAT
        for i in range(len(m["certs"]) - 1))),
    accept=[M("certificate", "server",
              certs=[{"key_kind": "rsa", "sig_alg": "rsa_pss_rsae_sha256"},
                     {"key_kind": "rsa", "sig_alg": "rsa_pkcs1_sha256"}])],
    reject=[M("certificate", "server",
              certs=[{"key_kind": "rsa", "sig_alg": "rsa_pss_rsae_sha256"},
                     {"key_kind": "ecdsa_p256",
                      "sig_alg": "ecdsa_secp256r1_sha256"}])],
    quote=Q2[65]))

WITNESSES.append(VAL(
    65,
    "Cross-message reading: the key of the end-entity certificate is of "
    "appropriate type for the signature algorithm it is used with in "
    "the connection's CertificateVerify.",
    "transcript", v175,
    accept=[[M("certificate", "server",
               certs=[{"key_kind": "ecdsa_p256", "key_id": "K2"}]),
             M("certificate_verify", "server",
               alg="ecdsa_secp256r1_sha256")]],
    reject=[[M("certificate", "server",
               certs=[{"key_kind": "ecdsa_p256", "key_id": "K2"}]),
             M("certificate_verify", "server", alg="rsa_pss_rsae_sha256")]],
    quote=Q2[65],
    pair_msg=MPAIR(
        M("certificate", "server",
          certs=[{"key_kind": "ecdsa_p256", "key_id": "K2"}]),
        ctx("The connection's CertificateVerify uses "
            "ecdsa_secp256r1_sha256: the key fits its use.",
            "other-messages", True, Q2[65]),
        ctx("The connection's CertificateVerify uses "
            "rsa_pss_rsae_sha256: the same Certificate message now sits "
            "in a violating connection.", "other-messages", False,
            Q2[65]))))

# --- 66: located presence (msg) + intent guard (nonlocal) ------------------

WITNESSES.append(VAL(
    66,
    "Located-predicate reading (rule 17's silence branch: the guard "
    "locates, the required content is fixed): within its scope — "
    "clients desiring server certificate authentication — the "
    "ClientHello contains the signature_algorithms extension.",
    "msg",
    lambda m: bool("signature_algorithms" in m["ext"]),
    accept=[M("client_hello", "client",
              ext=["signature_algorithms", "supported_groups"])],
    reject=[M("client_hello", "client", ext=["supported_groups"])],
    quote=Q2[66]))

WITNESSES.append(PAIR(
    66,
    "Whole-obligation reading: the duty is guarded on the client's "
    "desire, which no message carries.",
    [M("client_hello", "client", ext=["supported_groups",
                                      "pre_shared_key"])],
    ctx("The client intends a PSK-only handshake and does not desire "
        "certificate authentication: the guard is false, omitting the "
        "extension is compliant.", "private-intent", True, Q2[66]),
    ctx("The client desires the server to authenticate via certificate: "
        "the identical ClientHello violates the duty.", "private-intent",
        False, Q2[66])))

# --- 75: offered-chain predicate (msg) + inventory guard (nonlocal) --------

WITNESSES.append(VAL(
    75,
    "Offered-chain reading: within its scope — a valid SHA-1-free chain "
    "exists — the offered Certificate contains no SHA-1-signed "
    "certificate.",
    "msg",
    lambda m: bool(all("sha1" not in e.get("sig_alg", "")
                       for e in m["certs"])),
    accept=[M("certificate", "server",
              certs=[{"sig_alg": "rsa_pkcs1_sha256"}])],
    reject=[M("certificate", "server",
              certs=[{"sig_alg": "rsa_pkcs1_sha1"}])],
    quote=Q2[75]))

WITNESSES.append(PAIR(
    75,
    "Whole-obligation reading: the unless-clause references the "
    "server's certificate inventory, which is configuration.",
    [M("certificate", "server", certs=[{"sig_alg": "rsa_pkcs1_sha1"}])],
    ctx("No valid chain without SHA-1 could be produced from the "
        "server's inventory: the unless-clause licenses this offer.",
        "deployment-policy", True, Q2[75]),
    ctx("The server's inventory contained a valid SHA-1-free chain: "
        "the identical offer violates the duty.", "deployment-policy",
        False, Q2[75])))

# --- 79/80: advertisement consistency (transcript, under the
# --- attributed-abort convention) + preparedness (nonlocal) ----------------


def v79(tr):
    _, ch = find(tr, "client_hello", "client")
    if ch is None:
        return True
    for i, m in enumerate(tr):
        if (m["type"] == "alert"
                and m.get("attributed_to") == "signature-curve"
                and m.get("curve") in ch.get("supported_groups", [])):
            return False
    return True


WITNESSES.append(VAL(
    79,
    "Advertisement-consistency reading (attributed-abort convention, "
    "header note 2): in a TLS 1.2 handshake, the implementation does "
    "not reject a signature for using a curve its own ClientHello "
    "advertised.",
    "transcript", v79,
    accept=[[M("client_hello", "client",
               supported_groups=["x25519", "secp256r1"]),
             M("peer_signature", "server", curve="secp256r1"),
             M("finished", "client")],
            [M("client_hello", "client", supported_groups=["x25519"]),
             M("alert", "client", attributed_to="certificate-trust",
               desc="unknown_ca")]],
    reject=[[M("client_hello", "client",
               supported_groups=["x25519", "secp256r1"]),
             M("peer_signature", "server", curve="secp256r1"),
             M("alert", "client", attributed_to="signature-curve",
               curve="secp256r1", desc="handshake_failure")]],
    quote=Q2[79],
    pair_msg=MPAIR(
        M("client_hello", "client",
          supported_groups=["x25519", "secp256r1"]),
        ctx("The later signature used an advertised curve and the "
            "client accepted it: compliant.", "other-messages", True,
            Q2[79]),
        ctx("The later signature used an advertised curve and the "
            "client rejected it for that reason: the same ClientHello "
            "sits in a violating connection.", "other-messages", False,
            Q2[79]))))

WITNESSES.append(PAIR(
    79,
    "Preparedness reading: MUST be PREPARED to accept — a counterfactual "
    "capability over curves the transcript never exercises.",
    [M("client_hello", "client", supported_groups=["x25519",
                                                   "secp256r1"]),
     M("peer_signature", "server", curve="secp256r1"),
     M("finished", "client")],
    ctx("The implementation would also accept an x25519 signature: "
        "prepared for every advertised curve.", "party-conduct", True,
        Q2[79]),
    ctx("The implementation has x25519 signature acceptance disabled "
        "internally — unprepared for a curve it advertised — and this "
        "run simply never exercised it.", "party-conduct", False,
        Q2[79])))


def v80(tr):
    for m in tr:
        if (m["type"] == "alert"
                and m.get("attributed_to") == "signature-scheme"
                and m.get("scheme", "").startswith("rsa_pss")):
            return False
    return True


WITNESSES.append(VAL(
    80,
    "Advertisement-consistency reading for RSASSA-PSS in TLS 1.2 "
    "(attributed-abort convention): an implementation advertising PSS "
    "does not reject a signature for using it.",
    "transcript", v80,
    accept=[[M("client_hello", "client",
               sig_algs=["rsa_pss_rsae_sha256"]),
             M("peer_signature", "server", scheme="rsa_pss_rsae_sha256"),
             M("finished", "client")]],
    reject=[[M("client_hello", "client",
               sig_algs=["rsa_pss_rsae_sha256"]),
             M("peer_signature", "server", scheme="rsa_pss_rsae_sha256"),
             M("alert", "client", attributed_to="signature-scheme",
               scheme="rsa_pss_rsae_sha256", desc="handshake_failure")]],
    quote=Q2[80],
    pair_msg=MPAIR(
        M("client_hello", "client", sig_algs=["rsa_pss_rsae_sha256"]),
        ctx("The connection's later signature used PSS and was "
            "accepted: compliant.", "other-messages", True, Q2[80]),
        ctx("The later signature used PSS and was rejected for using "
            "it: violation, decidable only with the later messages.",
            "other-messages", False, Q2[80]))))

WITNESSES.append(PAIR(
    80,
    "Preparedness reading of [80]: counterfactual acceptance capability "
    "for a scheme this transcript never exercised.",
    [M("client_hello", "client", sig_algs=["rsa_pss_rsae_sha256",
                                           "rsa_pkcs1_sha256"]),
     M("peer_signature", "server", scheme="rsa_pkcs1_sha256"),
     M("finished", "client")],
    ctx("The implementation would accept a PSS signature too: "
        "prepared.", "party-conduct", True, Q2[80]),
    ctx("The implementation would reject a PSS signature (support "
        "advertised but acceptance not implemented); this run never "
        "exercised it.", "party-conduct", False, Q2[80])))

# --- 147: role reading (msg) + CertificateRequest-echo reading (transcript)

WITNESSES.append(VAL(
    147,
    "Role reading: a server-sent Certificate carries a zero-length "
    "certificate_request_context — sender role is message metadata "
    "(registration, datum definition).",
    "msg",
    lambda m: bool(not (m["type"] == "certificate"
                        and m["sender"] == "server"
                        and m["context"] != "")),
    accept=[M("certificate", "server", context="", certs=[]),
            M("certificate", "client", context="c1", certs=[])],
    reject=[M("certificate", "server", context="c1", certs=[])],
    quote=Q2[147]))


def v147t(tr):
    for i, m in enumerate(tr):
        if m["type"] != "certificate":
            continue
        if m["sender"] == "server":
            # A server Certificate is never a response to a
            # CertificateRequest (CRs request client certificates), so
            # its context is empty even in mutual-auth flows.
            want = ""
        else:
            crs = [x for x in tr[:i]
                   if x["type"] == "certificate_request"]
            want = crs[-1]["context"] if crs else ""
        if m["context"] != want:
            return False
    return True


WITNESSES.append(VAL(
    147,
    "History reading: a Certificate's context echoes the preceding "
    "CertificateRequest's context, and is empty exactly when there was "
    "none (the server-authentication case).",
    "transcript", v147t,
    accept=[[M("certificate_request", "server", context="c1"),
             M("certificate", "client", context="c1")],
            [M("certificate", "server", context="")],
            # The standard mutual-authentication flow: the server's own
            # Certificate follows its CertificateRequest with an empty
            # context; the client's echoes the CR's.
            [M("certificate_request", "server", context="c1"),
             M("certificate", "server", context=""),
             M("certificate", "client", context="c1")]],
    reject=[[M("certificate_request", "server", context="c1"),
             M("certificate", "client", context="c2")],
            # Pins the sender-role branch in the reject direction: a
            # server Certificate must not echo the CR's context.
            [M("certificate_request", "server", context="c1"),
             M("certificate", "server", context="c1")]],
    quote=Q2[147],
    pair_msg=MPAIR(
        M("certificate", "client", context="c1"),
        ctx("The preceding CertificateRequest carried context c1: "
            "compliant echo.", "other-messages", True, Q2[147]),
        ctx("The preceding CertificateRequest carried context c2: the "
            "identical Certificate message violates.", "other-messages",
            False, Q2[147]))))

# --- 164: alert-vocabulary reading (msg) + decision guard (nonlocal) -------

WITNESSES.append(VAL(
    164,
    "Alert-vocabulary reading: within its scope — the client decided to "
    "abort over an unacceptable chain — the abort alert is "
    "certificate-related.",
    "msg",
    lambda m: bool(m["desc"] in CERT_ALERTS),
    accept=[M("alert", "client", desc="unsupported_certificate")],
    reject=[M("alert", "client", desc="illegal_parameter")],
    quote=Q2[164]))

WITNESSES.append(PAIR(
    164,
    "Whole-obligation reading: the duty's guard is the client's private "
    "abort decision and its reason.",
    [M("certificate", "server", certs=[{"sig_alg": "rsa_pkcs1_sha256"}]),
     M("alert", "client", desc="internal_error")],
    ctx("The abort was for an unrelated internal reason — the duty's "
        "guard (deciding to abort over the chain) is false; no "
        "violation.", "private-intent", True, Q2[164]),
    ctx("The client had decided to abort because it could not construct "
        "an acceptable chain, then sent internal_error: the identical "
        "transcript violates the alert-choice duty.", "private-intent",
        False, Q2[164])))

# --- 184: sender prohibition (msg) + client response duty (transcript) -----

WITNESSES.append(VAL(
    184,
    "Sender-prohibition reading: an EndOfEarlyData message with sender "
    "role server is illegal in itself.",
    "msg",
    lambda m: bool(not (m["type"] == "end_of_early_data"
                        and m["sender"] == "server")),
    accept=[M("end_of_early_data", "client"),
            M("finished", "server")],
    reject=[M("end_of_early_data", "server")],
    quote=Q2[184]))


def v184t(tr):
    i, eoed = find(tr, "end_of_early_data", "server")
    if eoed is None:
        return True
    rest = [m for m in tr[i + 1:] if m["sender"] == "client"]
    return bool(rest and rest[0]["type"] == "alert"
                and rest[0]["desc"] == "unexpected_message")


WITNESSES.append(VAL(
    184,
    "Client response reading: upon a server-sent EndOfEarlyData, the "
    "client's next act is termination with unexpected_message.",
    "transcript", v184t,
    accept=[[M("end_of_early_data", "server"),
             M("alert", "client", desc="unexpected_message")],
            [M("finished", "server"), M("finished", "client")]],
    reject=[[M("end_of_early_data", "server"),
             M("finished", "client")]],
    quote=Q2[184],
    pair_msg=MPAIR(
        M("end_of_early_data", "server"),
        ctx("The client terminated with unexpected_message upon "
            "receiving it: its duty is met.", "other-messages", True,
            Q2[184]),
        ctx("The client continued the handshake after receiving it: "
            "violation — visible only in the later messages.",
            "other-messages", False, Q2[184]))))

# --- 52 / 67 / 124: single-local-reading contested items -------------------


def v52(tr):
    _, ch = find(tr, "client_hello", "client")
    _, sh = find(tr, "server_hello", "server")
    if ch is None or sh is None:
        return True
    if "supported_versions" in ch["ext"]:
        return True
    return bool("supported_versions" not in sh["ext"])


WITNESSES.append(VAL(
    52,
    "Outcome-consistency reading, scope-conditioned: within its scope — "
    "servers which also support TLS 1.2 (the sentence's own "
    "configuration guard) — a ClientHello without supported_versions is "
    "answered with a pre-1.3 negotiation (ServerHello without the "
    "extension) — a relation between the two messages.",
    "transcript", v52,
    accept=[[M("client_hello", "client", ext=[]),
             M("server_hello", "server", ext=[],
               selected_version_legacy=0x0303)],
            [M("client_hello", "client", ext=["supported_versions"]),
             M("server_hello", "server", ext=["supported_versions"],
               selected_version_ext=0x0304)]],
    reject=[[M("client_hello", "client", ext=[]),
             M("server_hello", "server", ext=["supported_versions"],
               selected_version_ext=0x0304)]],
    quote=Q2[52],
    pair_msg=MPAIR(
        M("server_hello", "server", ext=["supported_versions"],
          selected_version_ext=0x0304),
        ctx("The ClientHello carried supported_versions: selecting "
            "TLS 1.3 is compliant.", "other-messages", True, Q2[52]),
        ctx("The ClientHello lacked supported_versions: the identical "
            "ServerHello violates the duty to negotiate TLS 1.2 or "
            "prior.", "other-messages", False, Q2[52]))))

WITNESSES.append(PAIR(
    52,
    "Configuration-guard reading: the duty's own guard — \"servers ... "
    "which also support TLS 1.2\" — references the server's deployed "
    "version support, exactly as items 3 and 6 reference its supported "
    "sets. CONSTRUCTED BY THE GATE'S COLD REVIEWER, refuting this "
    "file's original FAILS record for this rung (the registration's "
    "reader-challenge mechanism working as designed); adopted after "
    "verification against the sentence. The registered T6 prediction "
    "of {transcript} for this item therefore fails; see the report.",
    [M("client_hello", "client", ext=[], legacy_version=0x0303),
     M("server_hello", "server", ext=["supported_versions"],
       selected_version_ext=0x0304),
     M("alert", "client", desc="illegal_parameter")],
    ctx("The server is TLS 1.3-only: the guard \"which also support "
        "TLS 1.2\" is false, so item 52 imposes no duty on this "
        "response; no other corpus MUST forbids it.",
        "deployment-policy", True, Q2[52]),
    ctx("The server also supports TLS 1.2: the guard holds, and the "
        "identical transcript violates the duty to negotiate TLS 1.2 "
        "or prior even though ClientHello.legacy_version was 0x0303.",
        "deployment-policy", False, Q2[52])))


def v67(tr):
    _, ch = find(tr, "client_hello", "client")
    if ch is None or "signature_algorithms" in ch["ext"]:
        return True
    _, cert = find(tr, "certificate", "server")
    return bool(cert is None)


WITNESSES.append(VAL(
    67,
    "Response-duty reading: a server that authenticates via certificate "
    "(its Certificate appears in the transcript) after a ClientHello "
    "lacking signature_algorithms has failed the duty to abort instead.",
    "transcript", v67,
    accept=[[M("client_hello", "client", ext=[]),
             M("alert", "server", desc="missing_extension")],
            [M("client_hello", "client", ext=[]),
             M("server_hello", "server", ext=["pre_shared_key"])],
            [M("client_hello", "client", ext=["signature_algorithms"]),
             M("certificate", "server", certs=[])]],
    reject=[[M("client_hello", "client", ext=[]),
             M("certificate", "server", certs=[])]],
    quote=Q2[67],
    pair_msg=MPAIR(
        M("client_hello", "client", ext=[]),
        ctx("The server continued with a PSK handshake, sending no "
            "certificate: no duty fires.", "other-messages", True,
            Q2[67]),
        ctx("The server proceeded to authenticate via certificate "
            "without aborting: the identical ClientHello sits in a "
            "violating connection.", "other-messages", False, Q2[67]))))


def v124(tr):
    _, ch = find(tr, "client_hello", "client")
    _, sh = find(tr, "server_hello", "server")
    if ch is None or sh is None or "psk_selected_identity" not in sh:
        return True
    return bool(sh["psk_selected_identity"] < len(ch["psk_identities"])
                and sh["cipher_suite"] in ch["cipher_suites"])


WITNESSES.append(VAL(
    124,
    "Offer-consistency reading: the selection is compatible with the "
    "offer — selected_identity indexes an offered identity and the "
    "selected suite was offered.",
    "transcript", v124,
    accept=[[M("client_hello", "client", psk_identities=["t1", "t2"],
               cipher_suites=["TLS_AES_128_GCM_SHA256"]),
             M("server_hello", "server", psk_selected_identity=1,
               cipher_suite="TLS_AES_128_GCM_SHA256")]],
    reject=[[M("client_hello", "client", psk_identities=["t1"],
               cipher_suites=["TLS_AES_128_GCM_SHA256"]),
             M("server_hello", "server", psk_selected_identity=1,
               cipher_suite="TLS_AES_128_GCM_SHA256")]],
    quote=Q2[124],
    pair_msg=MPAIR(
        M("server_hello", "server", psk_selected_identity=1,
          cipher_suite="TLS_AES_128_GCM_SHA256"),
        ctx("The ClientHello offered two identities and that suite: "
            "compliant selection.", "other-messages", True, Q2[124]),
        ctx("The ClientHello offered one identity: the identical "
            "ServerHello indexes past the offer.", "other-messages",
            False, Q2[124]))))

WITNESSES.append(PAIR(
    124,
    "Hash-compatibility reading (the RFC's own compatibility relation; "
    "cf. in-corpus item 185, resumption requires the same KDF hash): "
    "whether the selected PSK's hash matches the selected suite depends "
    "on the ticket's issuing connection. CONSTRUCTED AGAINST the "
    "registered T6 prediction of {transcript} for this item — the "
    "prediction fails honestly; see the report.",
    [M("client_hello", "client", psk_identities=["ticket-T"],
       cipher_suites=["TLS_AES_128_GCM_SHA256",
                      "TLS_AES_256_GCM_SHA384"]),
     M("server_hello", "server", psk_selected_identity=0,
       cipher_suite="TLS_AES_256_GCM_SHA384")],
    ctx("Ticket T was issued on a connection using a SHA-384 suite: "
        "the selection is hash-compatible.", "prior-connection", True,
        Q2[124]),
    ctx("Ticket T was issued under a SHA-256 suite: the identical "
        "transcript selects an incompatible pair.", "prior-connection",
        False, Q2[124])))

# --- Remaining nonlocal-predicted contested items --------------------------

WITNESSES.append(PAIR(
    55,
    "Preparedness duty: the server can process such ClientHellos — a "
    "counterfactual capability the transcript need not exercise.",
    [M("client_hello", "client", ext=["supported_versions"],
       supported_versions=[0x0304]),
     M("server_hello", "server", ext=["supported_versions"],
       selected_version_ext=0x0304)],
    ctx("The implementation would correctly process a ClientHello "
        "whose supported_versions lacks 0x0304 (negotiating a prior "
        "version or aborting cleanly): prepared.", "party-conduct",
        True, Q2[55]),
    ctx("The implementation would crash on such a ClientHello; this "
        "run never exercised the case.", "party-conduct", False,
        Q2[55])))

WITNESSES.append(PAIR(
    89,
    "Usage-restraint duty: not acting on supported_groups information "
    "before completion — internal use, invisible in the messages.",
    [M("client_hello", "client", supported_groups=["x25519"]),
     M("server_hello", "server", ext=["supported_versions"],
       selected_version_ext=0x0304),
     M("encrypted_extensions", "server", supported_groups=["secp256r1"]),
     M("finished", "server"), M("finished", "client")],
    ctx("The client made no decision from the server's supported_groups "
        "before the handshake completed: compliant.", "party-conduct",
        True, Q2[89]),
    ctx("The client adjusted internal state from that information "
        "mid-handshake, with no observable difference in this "
        "connection.", "party-conduct", False, Q2[89])))

WITNESSES.append(PAIR(
    111,
    "Which PSK encrypted the early data is decidable only by trial "
    "decryption with the PSK secrets.",
    [M("client_hello", "client", ext=["pre_shared_key", "early_data"],
       psk_identities=["t1", "t2"], early_records="E"),
     M("server_hello", "server", psk_selected_identity=0)],
    ctx("Under the provisioned secrets, E decrypts under the key "
        "derived from the FIRST listed PSK: compliant.",
        "secret-material", True, Q2[111]),
    ctx("Under different provisioned secrets, the same bytes E decrypt "
        "under the key derived from the second PSK: violation.",
        "secret-material", False, Q2[111])))

WITNESSES.append(PAIR(
    122,
    "Ignore duty: the server's freshness logic does not consume the "
    "field — conduct, since the field itself is unconstrained here.",
    [M("client_hello", "client", ext=["pre_shared_key"],
       psk_identities=["ext-psk-1"], obfuscated_ticket_age=12345),
     M("server_hello", "server", psk_selected_identity=0)],
    ctx("The server ignored the value: compliant.", "party-conduct",
        True, Q2[122]),
    ctx("The server fed the value into its freshness computation, "
        "reaching the same acceptance: violation with an identical "
        "transcript.", "party-conduct", False, Q2[122])))

WITNESSES.append(PAIR(
    123,
    "The Hash association of an external PSK is fixed at provisioning "
    "time — out-of-band configuration, carried by no message.",
    [M("client_hello", "client", ext=["pre_shared_key"],
       psk_identities=["ext-psk-1"]),
     M("server_hello", "server", psk_selected_identity=0,
       cipher_suite="TLS_AES_128_GCM_SHA256")],
    ctx("Provisioning set the PSK's Hash (SHA-256): the duty is met.",
        "deployment-policy", True, Q2[123]),
    ctx("Provisioning established the PSK with no Hash algorithm set: "
        "violation of the corpus-carried clause, invisible in the "
        "messages.", "deployment-policy", False, Q2[123])))

WITNESSES.append(PAIR(
    157,
    "Tolerance duty for status_request_v2: a capability of the "
    "receiving implementation.",
    [M("client_hello", "client", ext=["supported_versions"]),
     M("server_hello", "server", ext=["supported_versions"],
       selected_version_ext=0x0304)],
    ctx("The implementation would process a ClientHello including "
        "status_request_v2: able.", "party-conduct", True, Q2[157]),
    ctx("The implementation would fail on such a ClientHello; this "
        "transcript never exercised it.", "party-conduct", False,
        Q2[157])))

WITNESSES.append(PAIR(
    187,
    "SNI reporting to the calling application — API conduct outside "
    "the wire entirely.",
    [M("client_hello", "client", ext=["server_name", "pre_shared_key"],
       sni="b.example", psk_identities=["ticket-T"])],
    ctx("The implementation reported \"b.example\" (this ClientHello's "
        "value) to the application: compliant.", "party-conduct", True,
        Q2[187]),
    ctx("The implementation reported the previous session's SNI to the "
        "application: violation.", "party-conduct", False, Q2[187])))

WITNESSES.append(PAIR(
    189,
    "The 7-day cache bound is elapsed wall-clock time since the ticket "
    "was received.",
    [M("client_hello", "client", ext=["pre_shared_key"],
       psk_identities=["ticket-T"])],
    ctx("Ticket T was received three days ago (its ticket_lifetime was "
        "14 days): using it is compliant.", "clock", True, Q2[189]),
    ctx("The same ticket was received eight days ago: the identical "
        "use violates the cap regardless of ticket_lifetime.", "clock",
        False, Q2[189])))

WITNESSES.append(PAIR(
    197,
    "Delay tolerance around client authentication — a liveness/"
    "capability property with no stated deadline.",
    [M("certificate_request", "server", context="c1"),
     M("new_session_ticket", "server"),
     M("certificate", "client", context="c1")],
    ctx("The server tolerated the delay and interleaved messages, and "
        "would tolerate arbitrary such delays: prepared.",
        "party-conduct", True, Q2[197]),
    ctx("The server times out promptly on authentication delays in "
        "general; this run happened to complete within its window.",
        "party-conduct", False, Q2[197])))

# === Recorded construction failures (honest outcomes, README asymmetry) ====

FAILS = [
    {"item": 22, "rung": "transcript",
     "reading": "A target transcript-local but not msg-local for the "
                "TYPESTATE votes",
     "reason": "The negotiated version is determined within the "
               "ServerHello itself (items 56/57 fix the encoding), so "
               "every candidate collapses to the msg reading; the "
               "remaining target — the server's private selection — is "
               "determined by no transcript.",
     "channel": "private-intent"},
    {"item": 30, "rung": "transcript",
     "reading": "A transcript-local, non-msg-local sentinel duty",
     "reason": "Same collapse as item 22: the guard is the ServerHello's "
               "own version encoding.",
     "channel": "private-intent"},
    {"item": 31, "rung": "transcript",
     "reading": "A transcript-local, non-msg-local sentinel duty",
     "reason": "Same collapse as item 22.", "channel": "private-intent"},
    {"item": 32, "rung": "transcript",
     "reading": "A transcript-local, non-msg-local sentinel duty",
     "reason": "Same collapse as item 22.", "channel": "private-intent"},
    {"item": 56, "rung": "transcript",
     "reading": "A transcript-local, non-msg-local version-encoding duty",
     "reason": "The encoding the duty constrains is the ServerHello's "
               "own; nothing in the rest of the transcript changes it.",
     "channel": "private-intent"},
    {"item": 57, "rung": "transcript",
     "reading": "A transcript-local, non-msg-local version-encoding duty",
     "reason": "Same as item 56.", "channel": "private-intent"},
    {"item": 52, "rung": "msg",
     "reading": "A single-message reading of the DOMAIN votes",
     "reason": "The duty relates the ClientHello's extension absence to "
               "the ServerHello's selection — no single message carries "
               "both.",
     "channel": "other-messages"},
    # [WITHDRAWN 2026-08-16, at the gate: a FAILS record for 52-nonlocal
    # originally stood here ("no verdict flip is constructible with the
    # transcript fixed"). The gate's cold reviewer refuted it by
    # constructing the deployment-policy pair now shipped above: the
    # attempted reading had been scoped to the PROCESS votes' conduct
    # angle and never engaged the sentence's own configuration guard
    # ("which also support TLS 1.2"). Preserved as a comment because the
    # withdrawal is itself a result — the selective-elasticity failure
    # mode the registration names, caught by the mechanism it names.
    {"item": 55, "rung": "msg",
     "reading": "A message-shape reading of the DOMAIN votes",
     "reason": "The described ClientHello is itself compliant; the duty "
               "constrains the receiving implementation's capability.",
     "channel": "party-conduct"},
    {"item": 66, "rung": "transcript",
     "reading": "A transcript reading of the TYPESTATE votes",
     "reason": "The client's desire for certificate authentication is "
               "evidenced by no message in a fixed transcript.",
     "channel": "private-intent"},
    {"item": 67, "rung": "msg",
     "reading": "A single-message reading of the DOMAIN votes",
     "reason": "The guard needs the ClientHello AND the server's "
               "authentication mode (its Certificate) — two messages.",
     "channel": "other-messages"},
    {"item": 89, "rung": "transcript",
     "reading": "A transcript reading of the TYPESTATE votes",
     "reason": "\"Acting upon\" information is internal use; even the "
               "attributed-abort convention reaches only aborts, not "
               "uses.",
     "channel": "party-conduct"},
    {"item": 111, "rung": "msg",
     "reading": "A single-message reading of the DOMAIN votes",
     "reason": "Which PSK's key encrypted the early data is undecidable "
               "from the ClientHello; trial decryption needs the "
               "secrets.",
     "channel": "secret-material"},
    {"item": 111, "rung": "transcript",
     "reading": "A transcript reading of the TYPESTATE votes",
     "reason": "The same undecidability: no message sequence reveals "
               "which key encrypted the records without the PSK "
               "secrets.",
     "channel": "secret-material"},
    {"item": 122, "rung": "msg",
     "reading": "A field-shape reading of the DOMAIN votes",
     "reason": "The MUST constrains the server's use of the field; the "
               "field's value is unconstrained here (the value-0 form "
               "is the client's SHOULD, not this duty).",
     "channel": "party-conduct"},
    {"item": 123, "rung": "msg",
     "reading": "A message reading of the DOMAIN votes",
     "reason": "The Hash association is fixed at provisioning, out of "
               "band; no Section 4 message carries it.",
     "channel": "deployment-policy"},
    {"item": 157, "rung": "msg",
     "reading": "A message-shape reading of the DOMAIN votes",
     "reason": "As item 55: the ClientHello including status_request_v2 "
               "is compliant; the duty is the server's capability.",
     "channel": "party-conduct"},
    {"item": 197, "rung": "transcript",
     "reading": "A transcript reading of the TYPESTATE votes",
     "reason": "No transcript decision rule separates tolerated delay "
               "from violation: the interleavings are legal and the "
               "duty states no deadline.",
     "channel": "party-conduct"},
]
