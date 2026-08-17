#!/usr/bin/env python3
"""Witness artifacts for the second locality pass, RFC 9000 SS2-19 corpus
(see README.md — registration pushed at main 8821bce BEFORE any entry
below was written).

Graded by `check_witnesses2.py`. Each entry names its READING, its QUOTE
(the corpus sentence, [n] = item number in
census/quic/rfc9000_s2-19_musts.txt, corpus-verbatim), and the artifact.

MODELING CONVENTIONS (disclosed; they bound what the mechanical checks
certify — the first study's convention 1 carries over):

1. ABSTRACT DATAGRAM MODEL. A pkt datum is one UDP datagram:
   {"role" (sender role), "addr"/"dst" (source/destination endpoints),
   "size" (bytes on the wire), "packets": [{"space", "pn", "scid",
   "version", "frames": [...]}]}. A conn datum is the ordered list of
   such datagrams, both directions, decrypted. Frames are dicts
   {"type", ...fields}; transport parameters are modeled as a "TP" frame
   carried in the handshake ({"type": "TP", "params": {...}}) — the
   abstract, post-decryption form of what the crypto handshake carries.
   Packet numbers are abstract integers (so the 2^62-1 bound is a real,
   non-vacuous in-datum check). The model carries NO clock: datagram
   order is in the datum, absolute time is context. The mechanical
   checks certify INFORMATION FLOW, not transport implementations.

2. RESPONSE DUTIES read as orderings over the datagram sequence (the
   first study's attributed-abort analog, without attribution fields:
   a "close with error E" duty is checked as trigger-then-
   CONNECTION_CLOSE(E) in the transcript).

3. CHANNEL ATTACHMENT. "deployment-policy" covers the obliged party's
   OWN configuration and capability (supported versions, admin knobs,
   token schemes, buffer provisioning); "counterparty-config" the other
   side's; "prior-connection" covers other connections of the same
   endpoint, prior or concurrent (registered gloss); "network-path"
   covers path facts (PMTU). Channels on FAILS records name the
   BLOCKING channel.

4. SCOPE-CONDITIONED READINGS are disclosed inline (item 142's
   unless-guard; item 78's cross-attempt half) — the validator's
   tracking claim is scoped to the stated clause, and the residue is
   recorded as a FAILS entry or in the report.
"""

# --- model helpers ---------------------------------------------------------

CA = ("198.51.100.7", 4433)     # client address
SA = ("203.0.113.1", 443)       # server address
CB = ("198.51.100.99", 5555)    # client address after migration


def F(ftype, **fields):
    d = {"type": ftype}
    d.update(fields)
    return d


def PK(space, pn, frames, scid="s1", version=1):
    return {"space": space, "pn": pn, "scid": scid, "version": version,
            "frames": list(frames)}


def D(role, packets, size=1200, addr=None, dst=None):
    return {"role": role, "addr": addr or (CA if role == "client" else SA),
            "dst": dst or (SA if role == "client" else CA),
            "size": size, "packets": list(packets)}


def dgrams(conn, role=None):
    return [d for d in conn if role is None or d["role"] == role]


def frames(conn, ftype, role=None):
    out = []
    for i, d in enumerate(conn):
        if role is not None and d["role"] != role:
            continue
        for p in d["packets"]:
            for f in p["frames"]:
                if f["type"] == ftype:
                    out.append((i, d, p, f))
    return out


def tp(conn, role, key, default=None):
    for _i, _d, _p, f in frames(conn, "TP", role):
        if key in f["params"]:
            return f["params"][key]
    return default


def closes_with(conn, role, err, after_idx=-1):
    return any(i > after_idx and f.get("err") == err
               for i, _d, _p, f in frames(conn, "CONNECTION_CLOSE", role))


def stream_total(conn, role, sid):
    hi = 0
    for _i, _d, _p, f in frames(conn, "STREAM", role):
        if f["sid"] == sid:
            hi = max(hi, f["off"] + f["len"])
    return hi


def conn_total(conn, role):
    sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
    return sum(stream_total(conn, role, s) for s in sids)


def peer(role):
    return "server" if role == "client" else "client"


def stream_limit(conn, receiver, sid):
    """Largest stream-data limit the receiver has advertised for sid."""
    lim = tp(conn, receiver, "initial_max_stream_data", 0)
    for _i, _d, _p, f in frames(conn, "MAX_STREAM_DATA", receiver):
        if f["sid"] == sid:
            lim = max(lim, f["limit"])
    return lim


def conn_limit(conn, receiver):
    lim = tp(conn, receiver, "initial_max_data", 0)
    for _i, _d, _p, f in frames(conn, "MAX_DATA", receiver):
        lim = max(lim, f["limit"])
    return lim


def streams_limit(conn, receiver):
    lim = tp(conn, receiver, "initial_max_streams", 0)
    for _i, _d, _p, f in frames(conn, "MAX_STREAMS", receiver):
        lim = max(lim, f["limit"])
    return lim


def ctx(desc, channel, verdict, quote):
    return {"desc": desc, "channel": channel, "verdict": verdict,
            "quote": quote}


def PAIR(item, reading, datum, c1, c2, eligible=True):
    return {"item": item, "reading": reading, "rung": "nonlocal",
            "eligible": eligible, "kind": "pair",
            "pair": {"datum_kind": "conn", "datum": datum,
                     "contexts": [c1, c2]}}


def VAL(item, reading, rung, fn, accept, reject, quote, eligible=True,
        pair_fine=None):
    w = {"item": item, "reading": reading, "rung": rung,
         "eligible": eligible, "kind": "validator", "fn": fn,
         "accept": accept, "reject": reject, "quote": quote}
    if pair_fine is not None:
        w["pair_fine"] = pair_fine
    return w


def KPAIR(datum, c1, c2):
    return {"datum_kind": "pkt", "datum": datum, "contexts": [c1, c2]}


# Corpus-verbatim quotes (mechanically extracted from
# census/quic/rfc9000_s2-19_musts.txt).
Q = {
    4: 'An endpoint MUST NOT send data on any stream without ensuring '
       'that it is within the flow control limits set by its peer. [4]',
    9: 'Senders MUST NOT send data in excess of either limit. [9]',
    10: 'A receiver MUST close the connection with an error of type '
        'FLOW_CONTROL_ERROR if the sender violates the advertised '
        'connection or stream data limits; see Section 11 for details '
        'on error handling. [10]',
    17: 'Endpoints MUST NOT exceed the limit set by their peer. [17]',
    18: 'An endpoint that receives a frame with a stream ID exceeding '
        'the limit it has sent MUST treat this as a connection error of '
        'type STREAM_LIMIT_ERROR; see Section 11 for details on error '
        'handling. [18]',
    23: 'An endpoint MUST NOT use the same IP address and port for '
        'multiple concurrent connections with zero-length connection '
        'IDs, unless it is certain that those protocol features are not '
        'in use. [23]',
    26: "An endpoint MUST NOT provide more connection IDs than the "
        "peer's limit. [26]",
    27: 'After processing a NEW_CONNECTION_ID frame and adding and '
        'retiring active connection IDs, if the number of active '
        'connection IDs exceeds the value advertised in its '
        'active_connection_id_limit transport parameter, an endpoint '
        'MUST close the connection with an error of type '
        'CONNECTION_ID_LIMIT_ERROR. [27]',
    29: 'An endpoint MUST NOT forget a connection ID without retiring '
        'it, though it MAY choose to treat having connection IDs in '
        'need of retirement that exceed this limit as a connection '
        'error of type CONNECTION_ID_LIMIT_ERROR. [29]',
    32: 'Servers MUST drop smaller packets that specify unsupported '
        'versions. [32]',
    33: 'Servers MUST drop incoming packets under all other '
        'circumstances. [33]',
    34: 'Server deployments that use this simple form of load balancing '
        'MUST avoid the creation of a stateless reset oracle; see '
        'Section 21.11. [34]',
    40: 'Endpoints MUST explicitly negotiate an application '
        'protocol. [40]',
    49: 'An endpoint MUST treat the absence of the '
        'initial_source_connection_id transport parameter from either '
        'endpoint or the absence of the '
        'original_destination_connection_id transport parameter from '
        'the server as a connection error of type '
        'TRANSPORT_PARAMETER_ERROR. [49]',
    54: 'A client MUST NOT use remembered values for the following '
        'parameters: ack_delay_exponent, max_ack_delay, '
        'initial_source_connection_id, original_destination_connection_'
        'id, preferred_address, retry_source_connection_id, and '
        'stateless_reset_token. [54]',
    55: "The client MUST use the server's new values in the handshake "
        'instead; if the server does not provide new values, the '
        'default values are used. [55]',
    58: 'In particular, a server that accepts 0-RTT data MUST NOT set '
        'values for the following parameters (Section 18.2) that are '
        'smaller than the remembered values of the parameters. [58]',
    59: 'A server MUST reject 0-RTT data if the restored values for '
        'transport parameters cannot be supported. [59]',
    62: 'Implementations MUST support buffering at least 4096 bytes of '
        'data received in out-of-order CRYPTO frames. [62]',
    75: 'A token issued with NEW_TOKEN MUST NOT include information '
        'that would allow values to be linked by an observer to the '
        'connection on which it was issued. [75]',
    78: 'In comparison, a token obtained in a Retry packet MUST be used '
        'immediately during the connection attempt and cannot be used '
        'in subsequent connection attempts. [78]',
    80: 'An address validation token MUST be difficult to guess. [80]',
    81: 'For this design to work, the token MUST be covered by '
        'integrity protection against modification or falsification by '
        'clients. [81]',
    83: 'If the client IP address has changed, the server MUST adhere '
        'to the anti-amplification limit; see Section 8. [83]',
    84: 'To protect against such attacks, servers MUST ensure that '
        'replay of tokens is prevented or limited. [84]',
    92: 'This requirement MUST NOT be enforced by the endpoint that '
        'initiates path validation, as that would enable an attack on '
        'migration; see Section 9.3.3. [92]',
    94: 'However, an endpoint MUST NOT expand the datagram containing '
        'the PATH_RESPONSE if the resulting data exceeds the '
        'anti-amplification limit. [94]',
    107: 'Packets sent on the old path MUST NOT contribute to '
         'congestion control or RTT estimation for the new path. [107]',
    109: 'This timer SHOULD be set as described in Section 6.2.1 of '
         '[QUIC-RECOVERY] and MUST NOT be more aggressive. [109]',
    119: 'The flow label generation MUST be designed to minimize the '
         'chances of linkability with a previously used flow label, as '
         'a stable flow label would enable correlating activity on '
         'multiple paths; see Section 9.5. [119]',
    128: 'An endpoint that wishes to communicate a fatal connection '
         'error MUST use a CONNECTION_CLOSE frame if it is able. [128]',
    138: 'An endpoint that uses this design MUST either use the same '
         'connection ID length for all connections or encode the length '
         'of the connection ID such that it can be recovered without '
         'state. [138]',
    142: 'An endpoint MUST ensure that every Stateless Reset that it '
         'sends is smaller than the packet that triggered it, unless it '
         'maintains state sufficient to prevent looping. [142]',
    144: 'Errors that result in the connection being unusable, such as '
         'an obvious violation of protocol semantics or corruption of '
         'state that affects an entire connection, MUST be signaled '
         'using a CONNECTION_CLOSE frame (Section 19.19). [144]',
    152: 'If the packet number for sending reaches 2^62-1, the sender '
         'MUST close the connection without sending a CONNECTION_CLOSE '
         'frame or any further packets; an endpoint MAY send a '
         'Stateless Reset (Section 10.3) in response to further packets '
         'that it receives. [152]',
    162: 'A packet MUST NOT be acknowledged until packet protection has '
         'been successfully removed and all frames contained in the '
         'packet have been processed. [162]',
    171: 'ACK frames MUST only be carried in a packet that has the same '
         'packet number space as the packet being acknowledged; see '
         'Section 12.1. [171]',
    190: 'If a QUIC endpoint determines that the PMTU between any pair '
         'of local and remote IP addresses cannot support the smallest '
         'allowed maximum datagram size of 1200 bytes, it MUST '
         'immediately cease sending QUIC packets, except for those in '
         'PMTU probes or those containing CONNECTION_CLOSE frames, on '
         'the affected path. [190]',
    207: 'Version- specific rules for the connection ID therefore MUST '
         'NOT influence a decision about whether to send a Version '
         'Negotiation packet. [207]',
    230: 'Implementations MUST allow administrators of clients and '
         'servers to disable the spin bit either globally or on a '
         'per-connection basis. [230]',
    235: 'A server that chooses a zero-length connection ID MUST NOT '
         'provide a preferred address. [235]',
    236: 'Similarly, a server MUST NOT include a zero- length '
         'connection ID in this transport parameter. [236]',
    249: 'A client MUST treat receipt of a NEW_TOKEN frame with an '
         'empty Token field as a connection error of type '
         'FRAME_ENCODING_ERROR. [249]',
    254: 'The sum of the final sizes on all streams -- including '
         'streams in terminal states -- MUST NOT exceed the value '
         'advertised by a receiver. [254]',
    255: 'An endpoint MUST terminate a connection with an error of type '
         'FLOW_CONTROL_ERROR if it receives more data than the maximum '
         'data value that it has sent. [255]',
    258: 'The data sent on a stream MUST NOT exceed the largest maximum '
         'stream data value advertised by the receiver. [258]',
    259: 'An endpoint MUST terminate a connection with an error of type '
         'FLOW_CONTROL_ERROR if it receives more data than the largest '
         'maximum stream data that it has sent for the affected '
         'stream. [259]',
    262: 'An endpoint MUST NOT open more streams than permitted by the '
         'current stream limit set by its peer. [262]',
    263: 'An endpoint MUST terminate a connection with an error of type '
         'STREAM_LIMIT_ERROR if a peer opens more streams than was '
         'permitted. [263]',
}

# --- shared fixtures -------------------------------------------------------


def hs(client_params=None, server_params=None):
    """A minimal handshake: client Initial (TP) then server flight (TP)."""
    cp = {"initial_max_stream_data": 4000, "initial_max_data": 8000,
          "initial_max_streams": 4, "active_connection_id_limit": 4,
          "initial_source_connection_id": "c1"}
    sp = {"initial_max_stream_data": 4000, "initial_max_data": 8000,
          "initial_max_streams": 4, "active_connection_id_limit": 4,
          "initial_source_connection_id": "s1",
          "original_destination_connection_id": "odc"}
    cp.update(client_params or {})
    sp.update(server_params or {})
    return [
        D("client", [PK("initial", 0, [F("CRYPTO"), F("TP", params=cp)],
                        scid="c1")]),
        D("server", [PK("initial", 0, [F("CRYPTO"), F("TP", params=sp)]),
                     PK("handshake", 0, [F("CRYPTO")])]),
        D("client", [PK("handshake", 0, [F("CRYPTO")])], size=300),
    ]


def flow_conn(sent, limit, close_err=None, sid=0):
    """Handshake + client sends `sent` stream bytes against a server
    stream limit `limit`; server optionally closes with `close_err`."""
    c = hs(server_params={"initial_max_stream_data": limit,
                          "initial_max_data": limit * 4})
    c.append(D("client", [PK("app", 1,
                             [F("STREAM", sid=sid, off=0, len=sent)])],
               size=min(1200, 100 + sent % 1000)))
    if close_err:
        c.append(D("server", [PK("app", 1,
                                 [F("CONNECTION_CLOSE", err=close_err)])],
                   size=200))
    else:
        c.append(D("server", [PK("app", 1, [F("ACK", space="app",
                                              acked=[1])])], size=100))
    return c


# QC5 sender-side accept/reject conns.
FLOW_OK = flow_conn(3000, 4000)
FLOW_VIOL = flow_conn(6000, 4000)                 # sender exceeds
FLOW_VIOL_CLOSED = flow_conn(6000, 4000, "FLOW_CONTROL_ERROR")

# Connection-level (MAX_DATA) variants: two streams summing over limit.
CONN_OK = hs(); CONN_OK.append(
    D("client", [PK("app", 1, [F("STREAM", sid=0, off=0, len=3000),
                               F("STREAM", sid=4, off=0, len=3000)])]))
CONN_VIOL = hs(); CONN_VIOL.append(
    D("client", [PK("app", 1, [F("STREAM", sid=0, off=0, len=5000),
                               F("STREAM", sid=4, off=0, len=5000)])]))

# Stream-count variants (limit 4 streams).
STR_OK = hs(); STR_OK.append(
    D("client", [PK("app", 1, [F("STREAM", sid=i * 4, off=0, len=10)
                               for i in range(4)])]))
STR_VIOL = hs(); STR_VIOL.append(
    D("client", [PK("app", 1, [F("STREAM", sid=i * 4, off=0, len=10)
                               for i in range(6)])]))
CONN_VIOL_CLOSED = CONN_VIOL + [
    D("server", [PK("app", 1, [F("CONNECTION_CLOSE",
                                 err="FLOW_CONTROL_ERROR")])], size=200)]
STR_VIOL_CLOSED = STR_VIOL + [
    D("server", [PK("app", 1, [F("CONNECTION_CLOSE",
                                 err="STREAM_LIMIT_ERROR")])], size=200)]

# NEW_CONNECTION_ID variants (peer limit 4).
CID_OK = hs(); CID_OK.append(
    D("server", [PK("app", 1, [F("NEW_CONNECTION_ID", seq=i, cid="x%d" % i)
                               for i in range(1, 4)])]))
CID_VIOL = hs(); CID_VIOL.append(
    D("server", [PK("app", 1, [F("NEW_CONNECTION_ID", seq=i, cid="x%d" % i)
                               for i in range(1, 7)])]))
CID_VIOL_CLOSED = CID_VIOL + [
    D("client", [PK("app", 1, [F("CONNECTION_CLOSE",
                                 err="CONNECTION_ID_LIMIT_ERROR")])],
      size=200)]

# Retry flow.
RETRY_OK = [
    D("client", [PK("initial", 0, [F("CRYPTO")], scid="c1")]),
    D("server", [PK("retry", 0, [F("RETRY_TOKEN", token="tokR")])],
      size=120),
    D("client", [PK("initial", 1, [F("CRYPTO"), F("TOKEN", token="tokR")],
                    scid="c1")]),
]
RETRY_BAD = [
    D("client", [PK("initial", 0, [F("CRYPTO")], scid="c1")]),
    D("server", [PK("retry", 0, [F("RETRY_TOKEN", token="tokR")])],
      size=120),
    D("client", [PK("initial", 1, [F("CRYPTO")], scid="c1")]),
]
STALE_TOKEN_CONN = [
    D("client", [PK("initial", 0, [F("CRYPTO"),
                                   F("TOKEN", token="tokOld")], scid="c1")]),
    D("server", [PK("initial", 0, [F("CRYPTO")])]),
]

# ACK-space fixtures.
ACK_OK = hs() + [
    D("server", [PK("app", 5, [F("PING")])], size=100),
    D("client", [PK("app", 2, [F("ACK", space="app", acked=[5])])],
      size=100),
]
ACK_WRONG_SPACE = hs() + [
    D("client", [PK("app", 2, [F("ACK", space="app", acked=[0])])],
      size=100),
]  # server pn 0 in app space never sent; its pn 0s are initial/handshake
ACK_EARLY = hs() + [
    D("client", [PK("app", 2, [F("ACK", space="app", acked=[9])])],
      size=100),
    D("server", [PK("app", 9, [F("PING")])], size=100),
]

# Anti-amplification fixtures (3x limit, address validation not done).


def amp_conn(received, response_size):
    return [
        D("client", [PK("initial", 0, [F("CRYPTO")])], size=received),
        D("server", [PK("initial", 0, [F("CRYPTO"),
                                       F("PATH_RESPONSE", data="d")])],
          size=response_size),
    ]


def mig_conn(received_new, sent_new):
    """Handshake from CA, then client migrates to CB; server responds."""
    return hs() + [
        D("client", [PK("app", 3, [F("PING")])], size=received_new,
          addr=CB),
        D("server", [PK("app", 3, [F("PONG")])], size=sent_new, dst=CB),
    ]


def crypto_buf_conn(outstanding, closed):
    c = [D("client", [PK("initial", 0,
                         [F("CRYPTO_OOO", off=10000, ln=outstanding)])])]
    if closed:
        c.append(D("server", [PK("initial", 0,
                                 [F("CONNECTION_CLOSE",
                                    err="CRYPTO_BUFFER_EXCEEDED")])],
                   size=200))
    return c


# Stateless reset sizing.
def sreset_conn(trigger, reset):
    return [
        D("client", [PK("app", 7, [F("PING")])], size=trigger),
        D("server", [PK("sreset", 0, [F("STATELESS_RESET")])], size=reset),
    ]


# pn-cap fixtures (abstract integers, convention 1).
PNCAP = 2 ** 62 - 1
PN_OK = hs() + [D("client", [PK("app", PNCAP, [F("PING")])], size=100)]
PN_VIOL = PN_OK + [D("client", [PK("app", PNCAP, [F("PING")])], size=100),
                   ]  # any further packet after reaching the cap
# 235 fixtures.
ZLEN_OK = [
    D("client", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": "c1"})], scid="c1")]),
    D("server", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": "",
        "original_destination_connection_id": "odc"})], scid="")]),
]
ZLEN_VIOL = [
    D("client", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": "c1"})], scid="c1")]),
    D("server", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": "",
        "original_destination_connection_id": "odc",
        "preferred_address": {"cid": "p1", "cid_len": 2}})], scid="")]),
]

# 144: peer flow-control violation followed (or not) by CONNECTION_CLOSE.
SEM_VIOL_SIGNALED = FLOW_VIOL_CLOSED
SEM_VIOL_SILENT = FLOW_VIOL + [
    D("server", [PK("app", 2, [F("PING")])], size=100)]

# Ordinary quiet close-less conn (multiple uses).
PLAIN = hs() + [D("client", [PK("app", 1, [F("PING")])], size=100),
                D("server", [PK("app", 1, [F("ACK", space="app",
                                             acked=[1])])], size=100)]

# ALPN present (modeled in the crypto handshake), app data follows.
ALPN_CONN = hs() + [
    D("client", [PK("app", 1, [F("ALPN", offered=["h3"], selected="h3"),
                               F("STREAM", sid=0, off=0, len=50)])]),
]

# NEW_TOKEN issuance.
NT_CONN = hs() + [D("server", [PK("app", 1, [F("NEW_TOKEN",
                                               token="opaque-7f")])],
                    size=150)]
NT_EMPTY = D("server", [PK("app", 1, [F("NEW_TOKEN", token="")])],
             size=150)
NT_FULL = D("server", [PK("app", 1, [F("NEW_TOKEN", token="opaque-7f")])],
            size=150)

# Version fixtures for 32/33.
SMALL_UNSUPP = [
    D("client", [PK("initial", 0, [F("CRYPTO")], version=0x5A5A5A5A)],
      size=900),
]
# 0-RTT acceptance.
ZRTT_CONN = [
    D("client", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": "c1"})], scid="c1")]),
    D("client", [PK("0rtt", 0, [F("STREAM", sid=0, off=0, len=100)])],
      size=400),
    D("server", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": "s1",
        "original_destination_connection_id": "odc",
        "early_data_accepted": True})])]),
]

# Zero-length-CID conn at a fixed 4-tuple (item 23).
ZCID_CONN = [
    D("client", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": ""})], scid="")]),
    D("server", [PK("initial", 0, [F("CRYPTO"), F("TP", params={
        "initial_source_connection_id": "s1",
        "original_destination_connection_id": "odc"})])]),
]

# Migration conn without CC (128, 190 fixtures reuse PLAIN).


# --- validators ------------------------------------------------------------


def v236(dg):
    """Every server TP frame carrying preferred_address gives it a
    nonzero-length connection ID (designation: preferred_address)."""
    if dg["role"] != "server":
        return False
    ok = True
    for p in dg["packets"]:
        for f in p["frames"]:
            if f["type"] == "TP" and "preferred_address" in f["params"]:
                ok = ok and f["params"]["preferred_address"]["cid_len"] >= 1
    return ok


def v249(dg):
    """No NEW_TOKEN frame carries an empty Token field (the trigger
    predicate of the client's response duty)."""
    ok = True
    for p in dg["packets"]:
        for f in p["frames"]:
            if f["type"] == "NEW_TOKEN":
                ok = ok and len(f["token"]) >= 1
    return ok


def v49(dg):
    """Each endpoint's own TP block carries its role's required IDs
    (sender-role metadata: client needs initial_source_connection_id;
    server additionally original_destination_connection_id)."""
    ok = True
    for p in dg["packets"]:
        for f in p["frames"]:
            if f["type"] != "TP":
                continue
            ok = ok and "initial_source_connection_id" in f["params"]
            if dg["role"] == "server":
                ok = ok and ("original_destination_connection_id"
                             in f["params"])
    return ok


def v171(conn):
    """Every ACK acknowledges only packet numbers the peer sent in the
    SAME packet number space as the packet carrying the ACK."""
    ok = True
    for i, d, p, f in frames(conn, "ACK"):
        sent = {q["pn"] for e in dgrams(conn, peer(d["role"]))
                for q in e["packets"] if q["space"] == p["space"]}
        ok = ok and all(pn in sent for pn in f["acked"])
    return ok


def v78(conn):
    """If the connection attempt contains a server Retry carrying a
    token, the client's next Initial carries exactly that token
    (immediate use; the cross-attempt half is a recorded FAILS)."""
    tok = None
    for d in conn:
        for p in d["packets"]:
            if d["role"] == "server" and p["space"] == "retry":
                for f in p["frames"]:
                    if f["type"] == "RETRY_TOKEN":
                        tok = f["token"]
            elif (d["role"] == "client" and p["space"] == "initial"
                  and tok is not None):
                got = [f["token"] for f in p["frames"]
                       if f["type"] == "TOKEN"]
                return got == [tok]
    return tok is None


def v94(conn):
    """A server datagram containing PATH_RESPONSE to an unvalidated
    address keeps cumulative sent <= 3x cumulative received."""
    ok, rcvd, sent = True, 0, 0
    for d in conn:
        if d["role"] == "client":
            rcvd += d["size"]
        else:
            sent += d["size"]
            if any(f["type"] == "PATH_RESPONSE" for p in d["packets"]
                   for f in p["frames"]):
                ok = ok and sent <= 3 * rcvd
    return ok


def v83(conn):
    """After the client's source address changes, server bytes to the
    new address stay <= 3x bytes received from it."""
    ok, seen = True, {}
    for d in conn:
        if d["role"] == "client":
            seen[d["addr"]] = seen.get(d["addr"], 0) + d["size"]
        else:
            tgt = d["dst"]
            if tgt != CA:  # a migrated (non-handshake) address
                sent_new = d["size"] + seen.get(("sent", tgt), 0)
                seen[("sent", tgt)] = sent_new
                ok = ok and sent_new <= 3 * seen.get(tgt, 0)
    return ok


def v62(conn):
    """No endpoint signals crypto-buffer exhaustion while outstanding
    out-of-order CRYPTO data is <= 4096 bytes."""
    ok, out = True, {}
    for d in conn:
        for p in d["packets"]:
            for f in p["frames"]:
                if f["type"] == "CRYPTO_OOO":
                    out[d["role"]] = out.get(d["role"], 0) + f["ln"]
                if (f["type"] == "CONNECTION_CLOSE"
                        and f.get("err") == "CRYPTO_BUFFER_EXCEEDED"):
                    ok = ok and out.get(peer(d["role"]), 0) > 4096
    return ok


def v4(conn):
    """Per-stream data sent stays within the peer's advertised stream
    limit, and the connection total within the peer's connection
    limit."""
    ok = True
    for role in ("client", "server"):
        p = peer(role)
        sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
        for s in sids:
            ok = ok and stream_total(conn, role, s) <= stream_limit(
                conn, p, s)
        ok = ok and conn_total(conn, role) <= conn_limit(conn, p)
    return ok


def v10(conn):
    """If a sender exceeds the advertised limits, the receiver's
    subsequent frames include CONNECTION_CLOSE(FLOW_CONTROL_ERROR);
    vacuously true absent a violation."""
    for role in ("client", "server"):
        p = peer(role)
        sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
        viol = any(stream_total(conn, role, s) > stream_limit(conn, p, s)
                   for s in sids) or conn_total(conn, role) > conn_limit(
                       conn, p)
        if viol and not closes_with(conn, p, "FLOW_CONTROL_ERROR"):
            return False
    return True


def v17(conn):
    """Streams opened by each role stay within the peer's advertised
    stream limit."""
    ok = True
    for role in ("client", "server"):
        sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
        ok = ok and len(sids) <= streams_limit(conn, peer(role))
    return ok


def v18(conn):
    """A stream count beyond an endpoint's own advertised limit is
    followed by that endpoint's CONNECTION_CLOSE(STREAM_LIMIT_ERROR)."""
    for role in ("client", "server"):
        p = peer(role)
        sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
        if (len(sids) > streams_limit(conn, p)
                and not closes_with(conn, p, "STREAM_LIMIT_ERROR")):
            return False
    return True


def v26(conn):
    """Active connection IDs provided (issued minus retired) stay within
    the peer's active_connection_id_limit."""
    ok = True
    for role in ("client", "server"):
        issued = len(frames(conn, "NEW_CONNECTION_ID", role))
        retired = len(frames(conn, "RETIRE_CONNECTION_ID", peer(role)))
        lim = tp(conn, peer(role), "active_connection_id_limit", 2)
        # Active count includes the connection ID from the handshake.
        ok = ok and (issued - retired) + 1 <= lim
    return ok


def v27(conn):
    """An over-limit active-CID count is followed by
    CONNECTION_CLOSE(CONNECTION_ID_LIMIT_ERROR) from the holder."""
    for role in ("client", "server"):
        p = peer(role)
        issued = len(frames(conn, "NEW_CONNECTION_ID", role))
        retired = len(frames(conn, "RETIRE_CONNECTION_ID", p))
        lim = tp(conn, p, "active_connection_id_limit", 2)
        if (issued - retired) + 1 > lim and not closes_with(
                conn, p, "CONNECTION_ID_LIMIT_ERROR"):
            return False
    return True


def v254(conn):
    """Sum of final sizes across all streams stays within the receiver's
    advertised connection limit (final size = highest offset+len)."""
    ok = True
    for role in ("client", "server"):
        ok = ok and conn_total(conn, role) <= conn_limit(conn, peer(role))
    return ok


def v255(conn):
    """Received data beyond the maximum data value an endpoint has sent
    is followed by its CONNECTION_CLOSE(FLOW_CONTROL_ERROR)."""
    for role in ("client", "server"):
        p = peer(role)
        if (conn_total(conn, role) > conn_limit(conn, p)
                and not closes_with(conn, p, "FLOW_CONTROL_ERROR")):
            return False
    return True


def v258(conn):
    """Per-stream data stays within the largest stream-data value the
    receiver advertised for that stream."""
    ok = True
    for role in ("client", "server"):
        p = peer(role)
        sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
        for s in sids:
            ok = ok and stream_total(conn, role, s) <= stream_limit(
                conn, p, s)
    return ok


def v259(conn):
    """Stream data beyond an endpoint's own advertised stream limit is
    followed by its CONNECTION_CLOSE(FLOW_CONTROL_ERROR)."""
    for role in ("client", "server"):
        p = peer(role)
        sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
        if any(stream_total(conn, role, s) > stream_limit(conn, p, s)
               for s in sids) and not closes_with(
                   conn, p, "FLOW_CONTROL_ERROR"):
            return False
    return True


def v262(conn):
    return v17(conn)


def v263(conn):
    return v18(conn)


def v235p(dg):
    """CONSTRUCTED BY THE GATE'S COLD REVIEWER, refuting this file's
    original FAILS record for 235-pkt (preserved, withdrawn, below):
    the transport-parameter frame rides in a packet whose header
    carries the server's source connection ID, so the TP-bearing
    datagram exhibits BOTH the zero-length choice and the
    preferred_address — the conjunction is decidable on that datum.
    Adopted after verification against this file's own fixtures."""
    ok = True
    for p in dg["packets"]:
        for f in p["frames"]:
            if f["type"] == "TP" and "preferred_address" in f["params"]:
                ok = ok and p.get("scid") != ""
    return ok


def v235(conn):
    """A server whose packets use a zero-length source connection ID
    advertises no preferred_address."""
    zlen = any(p.get("scid") == "" for d in dgrams(conn, "server")
               for p in d["packets"])
    if zlen:
        return tp(conn, "server", "preferred_address") is None
    return True


def v142(conn):
    """Every Stateless Reset sent is smaller than the packet that
    triggered it (scope-conditioned: the unless-guard for endpoints
    maintaining loop-prevention state is a recorded residue)."""
    ok, last = True, {}
    for d in conn:
        if any(f["type"] == "STATELESS_RESET" for p in d["packets"]
               for f in p["frames"]):
            trig = last.get(peer(d["role"]))
            ok = ok and trig is not None and d["size"] < trig
        else:
            last[d["role"]] = d["size"]
    return ok


def v152p(dg):
    """No packet number exceeds 2^62-1 (abstract integers,
    convention 1)."""
    return all(p["pn"] <= PNCAP for p in dg["packets"])


def v152c(conn):
    """After a sender's packet number reaches 2^62-1, that sender emits
    nothing further (including no CONNECTION_CLOSE)."""
    capped = set()
    for d in conn:
        if d["role"] in capped:
            return False
        if any(p["pn"] >= PNCAP for p in d["packets"]):
            capped.add(d["role"])
    return True


def v162(conn):
    """No packet number is acknowledged before a peer datagram carrying
    it appears in the sequence."""
    seen = {("client",): set(), ("server",): set()}
    for d in conn:
        for p in d["packets"]:
            for f in p["frames"]:
                if f["type"] == "ACK":
                    if not all(pn in seen[(peer(d["role"]),)]
                               for pn in f["acked"]):
                        return False
        for p in d["packets"]:
            seen[(d["role"],)].add(p["pn"])
    return True


def v144(conn):
    """A conn-visible semantic violation (modeled: a flow-control
    breach) is followed by the victim's CONNECTION_CLOSE."""
    for role in ("client", "server"):
        p = peer(role)
        sids = {f["sid"] for _i, _d, _p, f in frames(conn, "STREAM", role)}
        viol = any(stream_total(conn, role, s) > stream_limit(conn, p, s)
                   for s in sids)
        if viol and not frames(conn, "CONNECTION_CLOSE", p):
            return False
    return True


# --- pair_fine builders ----------------------------------------------------


def sender_pf(item, sent=6000):
    """Fine pair for sender-side limit duties: one datagram bearing the
    STREAM frame; the advertised limit lives in other datagrams."""
    return KPAIR(
        D("client", [PK("app", 1, [F("STREAM", sid=0, off=0, len=sent)])]),
        ctx("The peer's transport parameters and MAX_* frames elsewhere "
            "in the connection advertise a limit of 8000: %d bytes are "
            "within it — compliant." % sent, "other-dgrams", True, Q[item]),
        ctx("The peer's advertisements elsewhere set the limit at 4000: "
            "the same datagram exceeds it — violation.",
            "other-dgrams", False, Q[item]))


def count_pf(item):
    """Fine pair for stream-COUNT duties (17, 262): one datagram
    opening a further stream; the peer's advertised stream limit lives
    in other datagrams."""
    return KPAIR(
        D("client", [PK("app", 1, [F("STREAM", sid=16, off=0,
                                     len=10)])]),
        ctx("The peer's advertisements elsewhere in the connection set "
            "the stream limit at 8: opening this fifth stream is "
            "within it — compliant.", "other-dgrams", True, Q[item]),
        ctx("The peer's advertisements set the limit at 4: the same "
            "datagram opens a fifth stream beyond it — violation.",
            "other-dgrams", False, Q[item]))


def responder_pf(item):
    """Fine pair for close-on-violation duties: the responder's ordinary
    (non-closing) datagram; whether a trigger occurred lives in other
    datagrams."""
    return KPAIR(
        D("server", [PK("app", 2, [F("ACK", space="app", acked=[1])])],
          size=100),
        ctx("No peer violation has occurred elsewhere in the connection: "
            "continuing without a close is compliant.",
            "other-dgrams", True, Q[item]),
        ctx("The peer breached the advertised limit earlier in the "
            "connection and no close follows anywhere in the "
            "sequence: the same continuing, non-closing datagram "
            "violates the close duty.", "other-dgrams", False, Q[item]))


WITNESSES = [
    # ---- QC1: stable DOMAIN {pkt} ----
    VAL(236, "A server transport-parameter block carrying "
             "preferred_address gives it a connection ID of nonzero "
             "length (registered designation: preferred_address).",
        "pkt", v236,
        accept=[D("server", [PK("initial", 0, [F("TP", params={
            "initial_source_connection_id": "s1",
            "original_destination_connection_id": "odc",
            "preferred_address": {"cid": "p1", "cid_len": 8}})])])],
        reject=[D("server", [PK("initial", 0, [F("TP", params={
            "initial_source_connection_id": "s1",
            "original_destination_connection_id": "odc",
            "preferred_address": {"cid": "", "cid_len": 0}})])])],
        quote=Q[236]),
    VAL(249, "A NEW_TOKEN frame with an empty Token field is invalid "
             "(the trigger predicate of the client's close duty).",
        "pkt", v249,
        accept=[NT_FULL], reject=[NT_EMPTY], quote=Q[249]),
    VAL(49, "Each endpoint's own transport-parameter block carries the "
            "parameters its role requires: initial_source_connection_id "
            "for both, original_destination_connection_id additionally "
            "for the server (decided per message via sender-role "
            "metadata).",
        "pkt", v49,
        accept=[D("server", [PK("initial", 0, [F("TP", params={
            "initial_source_connection_id": "s1",
            "original_destination_connection_id": "odc"})])]),
            D("client", [PK("initial", 0, [F("TP", params={
                "initial_source_connection_id": "c1"})])])],
        reject=[D("server", [PK("initial", 0, [F("TP", params={
            "initial_source_connection_id": "s1"})])])],
        quote=Q[49]),

    # ---- QC2: stable TYPESTATE ----
    VAL(171, "Every ACK acknowledges only packet numbers its peer sent "
             "in the same packet number space as the packet carrying "
             "the ACK.",
        "conn", v171,
        accept=[ACK_OK], reject=[ACK_WRONG_SPACE], quote=Q[171],
        pair_fine=KPAIR(
            D("client", [PK("app", 2, [F("ACK", space="app",
                                         acked=[5])])], size=100),
            ctx("Elsewhere in the connection the peer's packet number 5 "
                "was sent in the application space: same-space "
                "acknowledgment — compliant.", "other-dgrams", True,
                Q[171]),
            ctx("Elsewhere the peer's packet number 5 exists only in "
                "the handshake space: the same ACK crosses spaces — "
                "violation.", "other-dgrams", False, Q[171]))),
    VAL(78, "A token received in a Retry packet is used immediately: "
            "the client's next Initial in the same connection attempt "
            "carries exactly that token. (The cannot-be-used-in-"
            "subsequent-attempts half is a recorded FAILS — its "
            "discriminating fact is another connection.)",
        "conn", v78,
        accept=[RETRY_OK], reject=[RETRY_BAD], quote=Q[78],
        pair_fine=KPAIR(
            D("client", [PK("initial", 1, [F("CRYPTO"),
                                           F("TOKEN", token="tokR")],
                            scid="c1")]),
            ctx("A server Retry carrying token tokR immediately "
                "precedes this datagram in the same attempt — "
                "compliant immediate use.", "other-dgrams", True, Q[78]),
            ctx("No Retry precedes it in this connection; tokR was "
                "obtained via Retry during a previous connection "
                "attempt — the same Initial violates the "
                "cannot-be-used-in-subsequent-attempts clause.",
                "prior-connection", False, Q[78]))),

    # ---- QC3: stable nonlocal ----
    PAIR(40, "The application protocol actually run over the "
             "connection's streams is one the endpoints explicitly "
             "negotiated in the handshake.",
         ALPN_CONN,
         ctx("The endpoints run h3 on the streams, as the handshake's "
             "ALPN negotiation selected — compliant.",
             "party-conduct", True, Q[40]),
         ctx("Both deployments disregard the ALPN result and interpret "
             "the same stream bytes under a pre-arranged private "
             "protocol never negotiated in the handshake — violation. "
             "The datagram sequence is identical.",
             "deployment-policy", False, Q[40])),
    PAIR(230, "An administrator-facing control to disable the spin bit "
              "exists — a property of the implementation, invisible in "
              "any connection.",
         PLAIN,
         ctx("The implementation ships a global and per-connection "
             "spin-bit disable knob — compliant.",
             "deployment-policy", True, Q[230]),
         ctx("The implementation exposes no way for an administrator "
             "to disable the spin bit — violation. The connection is "
             "identical.", "deployment-policy", False, Q[230])),
    PAIR(34, "The deployment's load-balancing arrangement does not "
             "create a stateless reset oracle.",
         sreset_conn(700, 600),
         ctx("All instances behind the balancer share the reset key "
             "and answer uniformly: no oracle — compliant.",
             "deployment-policy", True, Q[34]),
         ctx("One instance's differential behavior lets an attacker "
             "test which server owns a connection ID: an oracle "
             "exists — violation. The observed connection is "
             "identical.", "deployment-policy", False, Q[34])),
    PAIR(207, "The decision to send a Version Negotiation packet was "
              "taken without consulting version-specific connection-ID "
              "rules.",
         [D("client", [PK("initial", 0, [F("CRYPTO")],
                          version=0x1A2A3A4A)], size=1300),
          D("server", [PK("vneg", 0, [F("VNEG", versions=[1])])],
            size=200)],
         ctx("The server decided from the version field alone — "
             "compliant.", "party-conduct", True, Q[207]),
         ctx("The server's decision logic also keyed on the datagram's "
             "connection-ID length violating version-specific rules — "
             "violation. The same Version Negotiation packet was "
             "sent.", "party-conduct", False, Q[207])),
    PAIR(107, "Old-path packets are excluded from the new path's "
              "congestion and RTT state — internal accounting.",
         mig_conn(1200, 900),
         ctx("The endpoint's congestion controller for the new path "
             "starts fresh, ignoring old-path samples — compliant.",
             "party-conduct", True, Q[107]),
         ctx("The endpoint seeds the new path's RTT estimate from "
             "old-path samples — violation. The datagram sequence is "
             "identical.", "party-conduct", False, Q[107])),
    PAIR(92, "The path-validation initiator does not ENFORCE the "
             "same-path requirement on PATH_RESPONSE — enforcement is "
             "the initiator's internal policy.",
         mig_conn(1200, 900),
         ctx("The initiator accepts the validation result regardless "
             "of which path carried the response — compliant.",
             "party-conduct", True, Q[92]),
         ctx("The initiator internally marks the validation failed "
             "because the response arrived on another path (no wire "
             "effect yet) — violation of MUST NOT enforce.",
             "party-conduct", False, Q[92])),
    PAIR(80, "The address validation token is difficult to guess — a "
             "property of how it was generated.",
         NT_CONN,
         ctx("The token bytes are 128 bits from a CSPRNG — compliant.",
             "generation-process", True, Q[80]),
         ctx("The same bytes came from a predictable per-boot counter "
             "an attacker can enumerate — violation.",
             "generation-process", False, Q[80])),
    PAIR(119, "Flow-label generation minimizes linkability across "
              "paths — a property of the generation scheme.",
         PLAIN,
         ctx("Flow labels derive from a keyed hash over the CID and "
             "path — unlinkable — compliant.",
             "generation-process", True, Q[119]),
         ctx("Flow labels come from a global counter, making activity "
             "across paths correlatable — violation. The observed "
             "connection is identical.",
             "generation-process", False, Q[119])),
    PAIR(75, "A NEW_TOKEN token carries nothing an observer could link "
             "back to the issuing connection — a property of the "
             "token's construction.",
         NT_CONN,
         ctx("The token is AEAD ciphertext under a server-secret key: "
             "opaque to observers — compliant.",
             "generation-process", True, Q[75]),
         ctx("The same bytes are a structured cleartext encoding of "
             "the client address and issuing connection ID, "
             "decodable by any observer who knows the format — "
             "violation.", "generation-process", False, Q[75])),

    # ---- QC4: stable THRESHOLD {conn} ----
    VAL(94, "A server datagram containing PATH_RESPONSE to an "
            "unvalidated address keeps cumulative bytes sent within "
            "three times cumulative bytes received.",
        "conn", v94,
        accept=[amp_conn(500, 1400)], reject=[amp_conn(400, 1300)],
        quote=Q[94],
        pair_fine=KPAIR(
            D("server", [PK("initial", 0, [F("CRYPTO"),
                                           F("PATH_RESPONSE",
                                             data="d")])], size=1400),
            ctx("Earlier datagrams from the unvalidated address total "
                "500 bytes: 1400 is within the 3x limit — compliant.",
                "other-dgrams", True, Q[94]),
            ctx("Earlier receipts total 400 bytes: the same 1400-byte "
                "datagram exceeds 3x — violation.",
                "other-dgrams", False, Q[94]))),
    VAL(83, "After a client address change, server bytes to the new "
            "address stay within three times the bytes received from "
            "it.",
        "conn", v83,
        accept=[mig_conn(400, 1100)], reject=[mig_conn(300, 1000)],
        quote=Q[83],
        pair_fine=KPAIR(
            D("server", [PK("app", 3, [F("PONG")])], size=1000, dst=CB),
            ctx("The migrated address has sent 400 bytes earlier in "
                "the connection: 1000 is within 3x — compliant.",
                "other-dgrams", True, Q[83]),
            ctx("The migrated address has sent only 300 bytes: the "
                "same datagram exceeds 3x — violation.",
                "other-dgrams", False, Q[83]))),
    VAL(62, "No endpoint signals crypto-buffer exhaustion while the "
            "peer's outstanding out-of-order CRYPTO data is at most "
            "4096 bytes (the support duty's observable face).",
        "conn", v62,
        accept=[crypto_buf_conn(5000, True),
                crypto_buf_conn(3000, False)],
        reject=[crypto_buf_conn(3000, True)],
        quote=Q[62],
        pair_fine=KPAIR(
            D("server", [PK("initial", 0, [F("CONNECTION_CLOSE",
                                             err="CRYPTO_BUFFER_"
                                                 "EXCEEDED")])],
              size=200),
            ctx("The peer had 5000 bytes of out-of-order CRYPTO "
                "outstanding elsewhere in the connection: signaling "
                "exhaustion is permitted — compliant.",
                "other-dgrams", True, Q[62]),
            ctx("The peer had only 3000 bytes outstanding: the same "
                "close signals exhaustion below the 4096-byte floor — "
                "violation.", "other-dgrams", False, Q[62]))),

    # ---- QC5: the limit family, single-rung {conn} ----
    VAL(4, "Stream data sent stays within the peer's advertised stream "
           "and connection flow-control limits (both advertisements "
           "are conn-carried).",
        "conn", v4, accept=[FLOW_OK], reject=[FLOW_VIOL], quote=Q[4],
        pair_fine=sender_pf(4)),
    VAL(9, "Data sent exceeds neither the stream-level nor the "
           "connection-level advertised limit.",
        "conn", v4, accept=[CONN_OK], reject=[CONN_VIOL], quote=Q[9],
        pair_fine=sender_pf(9)),
    VAL(10, "A flow-control breach by the sender is followed by the "
            "receiver's CONNECTION_CLOSE(FLOW_CONTROL_ERROR).",
        "conn", v10, accept=[FLOW_VIOL_CLOSED, FLOW_OK],
        reject=[FLOW_VIOL], quote=Q[10], pair_fine=responder_pf(10)),
    VAL(17, "Streams opened stay within the peer's advertised stream "
            "limit.",
        "conn", v17, accept=[STR_OK], reject=[STR_VIOL], quote=Q[17],
        pair_fine=count_pf(17)),
    VAL(18, "A stream ID beyond an endpoint's own advertised limit is "
            "followed by that endpoint's "
            "CONNECTION_CLOSE(STREAM_LIMIT_ERROR).",
        "conn", v18, accept=[STR_VIOL_CLOSED, STR_OK],
        reject=[STR_VIOL], quote=Q[18], pair_fine=responder_pf(18)),
    VAL(26, "Connection IDs provided (net of retirements) stay within "
            "the peer's advertised active_connection_id_limit.",
        "conn", v26, accept=[CID_OK], reject=[CID_VIOL], quote=Q[26],
        pair_fine=KPAIR(
            D("server", [PK("app", 1, [F("NEW_CONNECTION_ID", seq=5,
                                         cid="x5")])], size=150),
            ctx("The peer's transport parameters elsewhere advertise "
                "active_connection_id_limit 8 and four IDs are "
                "outstanding: issuing a fifth is within limit — "
                "compliant.", "other-dgrams", True, Q[26]),
            ctx("The peer advertised limit 2 and two are outstanding "
                "unretired: the same frame exceeds the limit — "
                "violation.", "other-dgrams", False, Q[26]))),
    VAL(27, "An active-CID count beyond an endpoint's own advertised "
            "limit is followed by its "
            "CONNECTION_CLOSE(CONNECTION_ID_LIMIT_ERROR).",
        "conn", v27, accept=[CID_VIOL_CLOSED, CID_OK],
        reject=[CID_VIOL], quote=Q[27], pair_fine=responder_pf(27)),
    VAL(254, "The sum of final sizes across all streams stays within "
             "the receiver's advertised connection data limit.",
        "conn", v254, accept=[CONN_OK], reject=[CONN_VIOL], quote=Q[254],
        pair_fine=sender_pf(254)),
    VAL(255, "Receipt of data beyond the maximum data value an endpoint "
             "has sent is followed by its "
             "CONNECTION_CLOSE(FLOW_CONTROL_ERROR).",
        "conn", v255, accept=[CONN_VIOL_CLOSED, FLOW_OK],
        reject=[CONN_VIOL], quote=Q[255], pair_fine=responder_pf(255)),
    VAL(258, "Per-stream data stays within the largest stream-data "
             "limit the receiver advertised for that stream.",
        "conn", v258, accept=[FLOW_OK], reject=[FLOW_VIOL], quote=Q[258],
        pair_fine=sender_pf(258)),
    VAL(259, "Stream data beyond an endpoint's own largest advertised "
             "stream limit is followed by its "
             "CONNECTION_CLOSE(FLOW_CONTROL_ERROR).",
        "conn", v259, accept=[FLOW_VIOL_CLOSED, FLOW_OK],
        reject=[FLOW_VIOL], quote=Q[259], pair_fine=responder_pf(259)),
    VAL(262, "Streams opened stay within the current stream limit set "
             "by the peer.",
        "conn", v262, accept=[STR_OK], reject=[STR_VIOL], quote=Q[262],
        pair_fine=count_pf(262)),
    VAL(263, "A peer's stream beyond the permitted limit is followed by "
             "CONNECTION_CLOSE(STREAM_LIMIT_ERROR).",
        "conn", v263, accept=[STR_VIOL_CLOSED, STR_OK],
        reject=[STR_VIOL], quote=Q[263], pair_fine=responder_pf(263)),
    VAL(235, "A transport-parameter block advertising a preferred "
             "address is carried in a packet whose header shows a "
             "nonzero-length source connection ID (reviewer-"
             "constructed; designated datum: the TP-bearing server "
             "datagram).",
        "pkt", v235p,
        accept=[ZLEN_OK[1],
                D("server", [PK("initial", 0, [F("TP", params={
                    "initial_source_connection_id": "s1",
                    "original_destination_connection_id": "odc",
                    "preferred_address": {"cid": "p1", "cid_len": 2}})],
                    scid="s1")])],
        reject=[ZLEN_VIOL[1]], quote=Q[235]),
    VAL(235, "A server whose packets use a zero-length source "
             "connection ID advertises no preferred address.",
        "conn", v235, accept=[ZLEN_OK], reject=[ZLEN_VIOL], quote=Q[235],
        pair_fine=KPAIR(
            D("server", [PK("handshake", 2, [F("CRYPTO")], scid="")],
              size=800),
            ctx("The server's transport parameters, carried in an "
                "earlier datagram of the flight, omit "
                "preferred_address — compliant.",
                "other-dgrams", True, Q[235]),
            ctx("The parameters in the earlier datagram include a "
                "preferred_address — the same zero-length-CID "
                "datagram now evidences a violation.",
                "other-dgrams", False, Q[235]))),
    VAL(142, "Every Stateless Reset sent is smaller than the packet "
             "that triggered it (scope-conditioned to endpoints not "
             "exercising the unless-guard; the guard is a recorded "
             "residue).",
        "conn", v142, accept=[sreset_conn(700, 600)],
        reject=[sreset_conn(500, 600)], quote=Q[142],
        pair_fine=KPAIR(
            D("server", [PK("sreset", 0, [F("STATELESS_RESET")])],
              size=600),
            ctx("The triggering client datagram elsewhere in the "
                "sequence was 700 bytes: the reset is smaller — "
                "compliant.", "other-dgrams", True, Q[142]),
            ctx("The triggering datagram was 500 bytes: the same "
                "600-byte reset is larger — violation.",
                "other-dgrams", False, Q[142]))),

    # ---- QC5: the nonlocal thirteen ----
    PAIR(54, "The client's 0-RTT behavior does not consult remembered "
             "values for the seven listed parameters.",
         ZRTT_CONN,
         ctx("The client applied the spec defaults for the listed "
             "parameters when resuming — compliant.",
             "prior-connection", True, Q[54]),
         ctx("The client applied the stateless_reset_token and "
             "ack_delay_exponent remembered from the earlier "
             "connection — violation. This connection's datagrams are "
             "identical.", "prior-connection", False, Q[54])),
    PAIR(55, "The client interprets the connection under the server's "
             "NEW values (or defaults), not remembered ones.",
         ZRTT_CONN,
         ctx("The client adopted the handshake's new values for "
             "ack_delay_exponent when decoding ACK delays — "
             "compliant.", "prior-connection", True, Q[55]),
         ctx("The client kept decoding under the remembered exponent "
             "from the prior connection — violation, with identical "
             "datagrams.", "prior-connection", False, Q[55])),
    PAIR(59, "0-RTT is rejected when the restored transport parameters "
             "cannot be supported by the server's current "
             "configuration.",
         ZRTT_CONN,
         ctx("The server's current configuration supports the restored "
             "parameters: accepting 0-RTT is permitted — compliant.",
             "deployment-policy", True, Q[59]),
         ctx("The server was reconfigured since the original "
             "connection and cannot support the restored parameters: "
             "the same acceptance violates the reject duty.",
             "deployment-policy", False, Q[59])),
    PAIR(29, "No connection ID is forgotten without being retired — "
             "the forgetting is internal memory.",
         CID_OK,
         ctx("The endpoint still holds every unretired connection ID "
             "it was issued — compliant.",
             "party-conduct", True, Q[29]),
         ctx("The endpoint silently dropped one issued connection ID "
             "from memory without sending RETIRE_CONNECTION_ID — "
             "violation. The datagram sequence is identical.",
             "party-conduct", False, Q[29])),
    PAIR(32, "A small datagram with an unsupported version is dropped "
             "— 'unsupported' is the server's own version set. "
             "(Reworked at the gate: the datum is a RESPONDING "
             "transcript, so both verdicts follow from this sentence "
             "alone.)",
         SMALL_UNSUPP + [D("server", [PK("initial", 0, [F("CRYPTO")])],
                           size=1200)],
         ctx("The server supports version 0x5a5a5a5a: this sentence's "
             "drop duty does not bind, and answering the datagram "
             "cannot violate it — compliant.",
             "deployment-policy", True, Q[32]),
         ctx("Version 0x5a5a5a5a is outside the server's supported "
             "set: the 900-byte datagram had to be dropped, and the "
             "same response violates the duty.",
             "deployment-policy", False, Q[32])),
    PAIR(33, "A packet matching none of the section's enumerated "
             "handling cases is dropped — the enumeration turns on "
             "server state and configuration. (Reworked at the gate: "
             "responding datum, same repair as 32.)",
         SMALL_UNSUPP + [D("server", [PK("initial", 0, [F("CRYPTO")])],
                           size=1200)],
         ctx("Under the server's connection table the packet matched a "
             "live connection: 'all other circumstances' does not "
             "apply, and this sentence imposes nothing on the "
             "response — compliant.",
             "deployment-policy", True, Q[33]),
         ctx("Under the server's state the packet matches no "
             "connection and no acceptance rule: it falls under 'all "
             "other circumstances', the drop was mandatory, and the "
             "same response violates the duty.",
             "deployment-policy", False, Q[33])),
    PAIR(81, "The Retry token is covered by integrity protection — a "
             "property of the server's token scheme keys.",
         RETRY_OK,
         ctx("The token is authenticated with a server-secret MAC: "
             "clients cannot modify or forge it — compliant.",
             "secret-material", True, Q[81]),
         ctx("The same bytes are an unauthenticated encoding any "
             "client could fabricate — violation.",
             "secret-material", False, Q[81])),
    PAIR(84, "Replay of address-validation tokens is prevented or "
             "limited across connections.",
         RETRY_OK,
         ctx("The deployment tracks token use; this token's first use "
             "is this connection — compliant.",
             "prior-connection", True, Q[84]),
         ctx("The same token has been accepted on many prior "
             "connections without limit — violation. This "
             "connection's datagrams are identical.",
             "prior-connection", False, Q[84])),
    PAIR(109, "The loss-detection timer is no more aggressive than "
              "QUIC-RECOVERY prescribes — timer settings live in "
              "wall-clock time, which the datagram sequence does not "
              "carry.",
         PLAIN,
         ctx("The endpoint's PTO timer matches the QUIC-RECOVERY "
             "computation — compliant.", "clock", True, Q[109]),
         ctx("The endpoint fires its timer at half the prescribed "
             "interval; the same frames would appear in the same "
             "order — violation.", "clock", False, Q[109])),
    PAIR(138, "Either one connection-ID length is used for ALL the "
              "deployment's connections, or lengths are "
              "self-describing — a property of the scheme across "
              "connections.",
         PLAIN,
         ctx("Every connection of this deployment uses 8-byte "
             "connection IDs — compliant.",
             "deployment-policy", True, Q[138]),
         ctx("Other live connections of the same deployment use mixed "
             "lengths with no self-describing encoding — violation. "
             "This connection is identical.",
             "deployment-policy", False, Q[138])),
    PAIR(23, "The same IP and port do not serve multiple concurrent "
             "zero-length-CID connections (unless the guarded features "
             "are known unused).",
         ZCID_CONN,
         ctx("This is the endpoint's only zero-length-CID connection "
             "on that address and port — compliant.",
             "prior-connection", True, Q[23]),
         ctx("A second concurrent zero-length-CID connection shares "
             "the same address and port, with migration in use — "
             "violation. This connection's datagrams are identical.",
             "prior-connection", False, Q[23])),
    PAIR(128, "A fatal error the endpoint wishes to communicate goes "
              "out as CONNECTION_CLOSE when the endpoint is able.",
         PLAIN,
         ctx("The endpoint hit no fatal error (or crashed before it "
             "could send anything): the closeless transcript is "
             "compliant.", "party-conduct", True, Q[128]),
         ctx("The endpoint detected a fatal error, wished to report "
             "it, and was able to send — but silently dropped the "
             "connection instead — violation.",
             "party-conduct", False, Q[128])),
    PAIR(190, "Upon determining PMTU < 1200 bytes on the path, the "
              "endpoint ceases sending non-probe, non-close packets.",
         PLAIN,
         ctx("The path's PMTU supports 1200 bytes; normal sending may "
             "continue — compliant.", "network-path", True, Q[190]),
         ctx("The path degraded below 1200 and the endpoint's "
             "PMTU discovery has determined it, yet the same ordinary "
             "packets keep flowing — violation.",
             "network-path", False, Q[190])),

    # ---- QC6: contested multi-rung ----
    VAL(152, "No packet number field exceeds 2^62-1 (abstract-integer "
             "model, convention 1).",
        "pkt", v152p,
        accept=[D("client", [PK("app", 5, [F("PING")])], size=100)],
        reject=[D("client", [PK("app", 2 ** 62, [F("PING")])],
                  size=100)],
        quote=Q[152]),
    VAL(152, "After a sender's packet number reaches 2^62-1, nothing "
             "further is sent by it — including no CONNECTION_CLOSE.",
        "conn", v152c, accept=[PN_OK], reject=[PN_VIOL], quote=Q[152],
        pair_fine=KPAIR(
            D("client", [PK("app", 7, [F("PING")])], size=100),
            ctx("No earlier packet of this sender reached 2^62-1: "
                "ordinary sending is compliant.",
                "other-dgrams", True, Q[152]),
            ctx("An earlier packet of this sender carried packet "
                "number 2^62-1: the same datagram violates the "
                "cease-sending duty.", "other-dgrams", False, Q[152]))),
    VAL(162, "No packet number is acknowledged before a peer datagram "
             "carrying it appears in the connection.",
        "conn", v162, accept=[ACK_OK], reject=[ACK_EARLY], quote=Q[162],
        pair_fine=KPAIR(
            D("client", [PK("app", 2, [F("ACK", space="app",
                                         acked=[3])])], size=100),
            ctx("The peer's packet 3 appears earlier in the sequence: "
                "acknowledging it is compliant.",
                "other-dgrams", True, Q[162]),
            ctx("Packet 3 has not yet appeared: the same ACK "
                "acknowledges an unreceived packet — violation.",
                "other-dgrams", False, Q[162]))),
    PAIR(162, "Acknowledgment additionally waits until every frame of "
              "the packet has been PROCESSED — internal processing "
              "state.",
         ACK_OK,
         ctx("The endpoint processed all frames of packet 5 before "
             "acknowledging it — compliant.",
             "party-conduct", True, Q[162]),
         ctx("The endpoint acknowledged packet 5 after removing "
             "protection but before processing its frames — "
             "violation. The datagram sequence is identical.",
             "party-conduct", False, Q[162])),
    VAL(144, "A conn-visible semantic violation by the peer (modeled: "
             "a flow-control breach) is followed by a CONNECTION_CLOSE "
             "from the victim.",
        "conn", v144, accept=[SEM_VIOL_SIGNALED, PLAIN],
        reject=[SEM_VIOL_SILENT], quote=Q[144],
        pair_fine=KPAIR(
            D("server", [PK("app", 2, [F("PING")])], size=100),
            ctx("No connection-unusable error has occurred elsewhere: "
                "continuing without a close is compliant.",
                "other-dgrams", True, Q[144]),
            ctx("The peer's earlier frames breached protocol "
                "semantics, leaving the connection unusable: the same "
                "continuing datagram violates the signal duty.",
                "other-dgrams", False, Q[144]))),
    PAIR(144, "Internal state corruption affecting the connection is "
              "signaled with CONNECTION_CLOSE — the corruption is not "
              "in the datagram sequence.",
         PLAIN,
         ctx("No state corruption occurred: the closeless transcript "
             "is compliant.", "party-conduct", True, Q[144]),
         ctx("The endpoint's connection state was corrupted (memory "
             "fault affecting the whole connection) and it kept "
             "running without signaling — violation.",
             "party-conduct", False, Q[144])),
]

# --- recorded construction failures (honest outcomes, per README) ---------

FAILS = [
    {"item": 58, "rung": "conn", "reading":
        "A conn-local predicate comparing the server's new transport "
        "parameters against the client's REMEMBERED values.",
     "reason": "The remembered values are the prior connection's "
               "parameters; this connection's datagram sequence never "
               "carries them, so no predicate over it can perform the "
               "comparison. Any reader who constructs a conn validator "
               "for this reading refutes the registration's strongest "
               "prediction (QC2).",
     "channel": "prior-connection"},
    {"item": 78, "rung": "conn", "reading":
        "The cannot-be-used-in-subsequent-attempts half: this "
        "connection's Initial does not carry a token obtained via "
        "Retry in ANOTHER attempt.",
     "reason": "A token's provenance (Retry of a prior attempt vs "
               "NEW_TOKEN) is not recoverable from this connection "
               "when no Retry precedes it here; the discriminating "
               "fact lives in the earlier connection.",
     "channel": "prior-connection"},
    {"item": 142, "rung": "conn", "reading":
        "The guarded reading: an endpoint maintaining loop-prevention "
        "state may send resets not smaller than the trigger.",
     "reason": "Whether the endpoint maintains such state is internal; "
               "the shipped validator is scope-conditioned to the "
               "unguarded clause (convention 4).",
     "channel": "party-conduct"},
    {"item": 54, "rung": "conn", "reading":
        "A conn-local predicate deciding whether the client USED "
        "remembered values for the seven listed parameters.",
     "reason": "Use is the client's internal interpretation (e.g., of "
               "ACK delays); the listed parameters' remembered values "
               "live in a prior connection, and behavior over this "
               "transcript is consistent with both use and non-use.",
     "channel": "prior-connection"},
    {"item": 55, "rung": "conn", "reading":
        "A conn-local predicate deciding whether the client adopted "
        "the server's new handshake values over remembered ones.",
     "reason": "Same shape as 54: interpretation is internal and the "
               "alternative values are in a prior connection.",
     "channel": "prior-connection"},
    {"item": 59, "rung": "conn", "reading":
        "A conn-local predicate for 'restored values cannot be "
        "supported'.",
     "reason": "Supportability is the server's current configuration "
               "and capacity, not connection content.",
     "channel": "deployment-policy"},
    {"item": 29, "rung": "conn", "reading":
        "A conn-local predicate deciding whether an endpoint forgot a "
        "connection ID without retiring it.",
     "reason": "Forgetting is internal memory state with no mandatory "
               "wire correlate.",
     "channel": "party-conduct"},
    {"item": 32, "rung": "pkt", "reading":
        "A pkt-local predicate for 'smaller packet with unsupported "
        "version'.",
     "reason": "Size and version are in-datum, but 'unsupported' is "
               "the server's own version set — configuration, not "
               "datagram content.",
     "channel": "deployment-policy"},
    {"item": 33, "rung": "pkt", "reading":
        "A pkt-local predicate for 'all other circumstances'.",
     "reason": "The section's enumerated circumstances include matching "
               "the server's existing connections and acceptance "
               "policy — neither is in one datagram.",
     "channel": "deployment-policy"},
    {"item": 33, "rung": "conn", "reading":
        "A conn-local predicate for 'all other circumstances'.",
     "reason": "The enumeration also turns on the server's OTHER "
               "connections (whether the packet matches an existing "
               "one) and its configuration; one connection's "
               "transcript cannot enumerate the rest.",
     "channel": "prior-connection"},
    {"item": 138, "rung": "pkt", "reading":
        "A pkt-local predicate for 'same length for all connections or "
        "self-describing encoding'.",
     "reason": "Scheme-hood is a property of the deployment across "
               "connections; a single datagram's CID exhibits a length "
               "but cannot witness the scheme.",
     "channel": "deployment-policy"},
    {"item": 23, "rung": "conn", "reading":
        "A conn-local predicate for 'no other concurrent zero-length-"
        "CID connection shares this address and port'.",
     "reason": "The other connections are, by construction, outside "
               "this connection's datagram sequence.",
     "channel": "prior-connection"},
    {"item": 128, "rung": "conn", "reading":
        "A conn-local predicate for 'a wished-for fatal error report "
        "went out as CONNECTION_CLOSE if able'.",
     "reason": "Both the wish and the ability are internal; a "
               "closeless transcript is consistent with no-error, "
               "unable, and violating endpoints alike.",
     "channel": "party-conduct"},
    {"item": 190, "rung": "conn", "reading":
        "A conn-local predicate for 'ceased sending upon determining "
        "PMTU < 1200'.",
     "reason": "The PMTU determination is a path measurement plus "
               "internal discovery state; the datagram sequence (which "
               "carries no clock and no ICMP feedback in this model) "
               "does not fix it.",
     "channel": "network-path"},
    # WITHDRAWN at the witness-pass gate — the record below was
    # REFUTED by the gate's cold reviewer, who constructed the denied
    # validator (v235p above): the TP frame's carrier packet exposes
    # the SCID choice in the same datagram, so the "different
    # datagrams" premise does not block the designated datum. This is
    # the selective-elasticity failure mode the registration's FAILS
    # discipline exists to catch, occurring on a registered exact
    # prediction (QC5 drops to 27/28). Preserved for the record:
    # {"item": 235, "rung": "pkt", "reading":
    #     "A pkt-local predicate for 'zero-length-CID server provides
    #     no preferred address'.",
    #  "reason": "The server's transport parameters and its
    #            zero-length CID choice can travel in different
    #            datagrams of the flight (large flights span
    #            datagrams); a datagram showing one half cannot decide
    #            the conjunction.",
    #  "channel": "other-dgrams"},
    {"item": 144, "rung": "pkt", "reading":
        "A pkt-local predicate for 'connection-unusable error is "
        "signaled with CONNECTION_CLOSE'.",
     "reason": "Whether an error occurred and whether a close followed "
               "are facts about the sequence, not about one datagram.",
     "channel": "other-dgrams"},
]
