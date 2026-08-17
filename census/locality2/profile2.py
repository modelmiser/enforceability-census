#!/usr/bin/env python3
"""Per-item agreement profile across every archived label map for the
RFC 5545 SS3 corpus (iCalendar, n=225, ten raters) and the RFC 9000
SS2-19 corpus (QUIC, n=281, twelve raters).

Selection input for the census/locality2 registration: parses the
archived full label maps from their reports' verbatim raw-label blocks,
normalizes label spellings, strips torn flags, and verifies the parse
against published agreement numbers as known-answer tests (KATs) with a
perturbation self-test.

Usage: python3 profile2.py <ical|quic> [--profile | --summary |
                                        --eligibility | --stable]
"""
import hashlib
import os
import pathlib
import re
import sys

if not __debug__:
    raise SystemExit("this tool's KATs use assert — do not run with -O")

REPO = pathlib.Path(os.environ.get(
    "CENSUS_REPO", pathlib.Path(__file__).resolve().parents[2]))

VALID = {"DOMAIN", "TYPESTATE", "PROCESS", "THRESHOLD", "REVOCABLE", "CV",
         "NEG", "POLICY", "META", "U"}
ALIASES = {"NEGOTIATION": "NEG", "CRYPTO-VERIFY": "CV", "UNCLASSIFIED": "U",
           "CRYPTOVERIFY": "CV"}
ELIMINABLE = {"DOMAIN", "TYPESTATE"}

# (rater, file, heading substring, nth fenced block after heading, instrument)
CORPORA = {
    "ical": {
        "n": 225,
        "corpus_file": "census/ical/rfc5545_s3_musts.txt",
        "sources": [
            ("Ai",   "census/ical/rfc5545-census.md",              "Raw labels (rater Ai",            0, "v3p4"),
            ("Xi",   "census/ical/rfc5545-census.md",              "Raw labels (rater Xi",            0, "v3p4"),
            ("Av4i", "census/v4-ical/rfc5545-v4pass.md",           "Raw labels (rater Av4i",          0, "v4"),
            ("Xv4i", "census/v4-ical/rfc5545-v4pass.md",           "Raw labels (rater Xv4i",          0, "v4"),
            ("Av5i", "census/v5-completion/rfc-v5-completion.md",  "Raw labels (iCalendar: rater Av5", 0, "v5"),
            ("Xv5i", "census/v5-completion/rfc-v5-completion.md",  "Raw labels (iCalendar: rater Av5", 1, "v5"),
            ("Av6i", "census/v6-pass/rfc-v6-pass.md",              "Raw labels (iCalendar: rater Av6", 0, "v6"),
            ("Xv6i", "census/v6-pass/rfc-v6-pass.md",              "Raw labels (iCalendar: rater Av6", 1, "v6"),
            ("Av7i", "census/v7-pass/rfc-v7-pass.md",              "Raw labels (iCalendar Av7",       0, "v7"),
            ("Xv7i", "census/v7-pass/rfc-v7-pass.md",              "Raw labels (iCalendar Xv7",       0, "v7"),
        ],
        # Published pairwise raw-agreement counts (of 225).
        # Sources: census report (219), v4 report (219), v5-completion
        # table (218), v6 report (98.7% -> 222, uniquely implied),
        # v7 report (220).
        "kat_pairs": {
            ("Ai", "Xi"): 219, ("Av4i", "Xv4i"): 219, ("Av5i", "Xv5i"): 218,
            ("Av6i", "Xv6i"): 222, ("Av7i", "Xv7i"): 220,
        },
        # Published per-rater eliminable (DOMAIN+TYPESTATE) counts.
        # v6 counts 200/200 uniquely implied by the report's 88.9/88.9.
        "kat_elim": {
            "Ai": 198, "Xi": 199, "Av4i": 200, "Xv4i": 198,
            "Av5i": 211, "Xv5i": 205, "Av6i": 200, "Xv6i": 200,
            "Av7i": 199, "Xv7i": 197,
        },
    },
    "quic": {
        "n": 281,
        "corpus_file": "census/quic/rfc9000_s2-19_musts.txt",
        "sources": [
            ("Aq3",  "census/quic/rfc9000-census.md",              "Raw labels (archived verbatim",  0, "v3p4"),
            ("Bq3",  "census/quic/rfc9000-census.md",              "Raw labels (archived verbatim",  1, "v3p4"),
            ("Aq",   "census/quic-replication/rfc9000-replication.md", "Raw labels (rater Aq",       0, "v3p4"),
            ("Xq",   "census/quic-replication/rfc9000-replication.md", "Raw labels (rater Xq",       0, "v3p4"),
            ("Av4q", "census/v4-completion/rfc-v4-completion.md",  "Raw labels (QUIC: rater Av4",    0, "v4"),
            ("Xv4q", "census/v4-completion/rfc-v4-completion.md",  "Raw labels (QUIC: rater Av4",    1, "v4"),
            ("Aq5",  "census/v5-quic/rfc9000-v5pass.md",           "Raw labels (rater Aq5",          0, "v5"),
            ("Xq5",  "census/v5-quic/rfc9000-v5pass.md",           "Raw labels (rater Xq5",          0, "v5"),
            ("Av6q", "census/v6-pass/rfc-v6-pass.md",              "Raw labels (QUIC: rater Av6",    0, "v6"),
            ("Xv6q", "census/v6-pass/rfc-v6-pass.md",              "Raw labels (QUIC: rater Av6",    1, "v6"),
            ("Av7q", "census/v7-pass/rfc-v7-pass.md",              "Raw labels (QUIC Av7",           0, "v7"),
            ("Xv7q", "census/v7-pass/rfc-v7-pass.md",              "Raw labels (QUIC Xv7",           0, "v7"),
        ],
        # Published pairwise raw-agreement counts (of 281).
        # Era pairs: census (239), replication (230), v4-completion
        # (84.0% -> 236, uniquely implied), v5-quic (252), v6 (89.3% ->
        # 251, uniquely implied), v7 (243). Cross-era: replication
        # role-matched (Aq-Aq3 231, Xq-Bq3 235), v5-quic finding
        # (Aq5-Av4q 256, Xq5-Xv4q 221).
        "kat_pairs": {
            ("Aq3", "Bq3"): 239, ("Aq", "Xq"): 230, ("Av4q", "Xv4q"): 236,
            ("Aq5", "Xq5"): 252, ("Av6q", "Xv6q"): 251, ("Av7q", "Xv7q"): 243,
            ("Aq", "Aq3"): 231, ("Xq", "Bq3"): 235,
            ("Aq5", "Av4q"): 256, ("Xq5", "Xv4q"): 221,
        },
        # Published per-rater eliminable (DOMAIN+TYPESTATE) counts.
        # v6 counts 183/183 uniquely implied by the report's 65.1/65.1.
        "kat_elim": {
            "Aq3": 188, "Bq3": 194, "Aq": 190, "Xq": 196,
            "Av4q": 179, "Xv4q": 193, "Aq5": 189, "Xq5": 187,
            "Av6q": 183, "Xv6q": 183, "Av7q": 177, "Xv7q": 178,
        },
    },
}


def block_after(text, heading_substr, nth):
    idx = text.find(heading_substr)
    assert idx >= 0, "heading not found: %s" % heading_substr
    rest = text[idx:]
    end = rest.find("\n## ", 1)
    section = rest if end == -1 else rest[:end]
    blocks = re.findall(r"```\n(.*?)```", section, re.S)
    assert len(blocks) > nth, (heading_substr, len(blocks))
    return blocks[nth]


def parse_map(block, who, all_items):
    labels, torn = {}, set()
    for tok in block.split():
        m = re.fullmatch(r"(\d+):([A-Za-z?-]+)", tok)
        assert m, "%s: bad token %r" % (who, tok)
        n, lab = int(m.group(1)), m.group(2)
        assert n not in labels, "%s: duplicate item %d" % (who, n)
        if lab.endswith("?"):
            torn.add(n)
            lab = lab[:-1]
        lab = ALIASES.get(lab, lab)
        assert lab in VALID, "%s: unknown label %r at %d" % (who, lab, n)
        labels[n] = lab
    assert set(labels) == all_items, \
        "%s: items %s" % (who, sorted(all_items ^ set(labels)))
    return labels, torn


def agree(m1, m2, all_items):
    return sum(1 for i in all_items if m1[i] == m2[i])


def load_all(corpus):
    cfg = CORPORA[corpus]
    all_items = set(range(1, cfg["n"] + 1))
    maps, torn_sites = {}, {}
    for who, relpath, heading, nth, _gen in cfg["sources"]:
        text = (REPO / relpath).read_text()
        maps[who], torn_sites[who] = parse_map(
            block_after(text, heading, nth), who, all_items)
    # Known-answer tests: the parse must reproduce every published number.
    for (r1, r2), expect in cfg["kat_pairs"].items():
        got = agree(maps[r1], maps[r2], all_items)
        assert got == expect, "KAT %s-%s: got %d, expect %d" % (
            r1, r2, got, expect)
    for who, expect in cfg["kat_elim"].items():
        got = sum(1 for i in all_items if maps[who][i] in ELIMINABLE)
        assert got == expect, "KAT elim %s: got %d, expect %d" % (
            who, got, expect)
    # Self-test: a perturbed copy must FAIL a KAT.
    first = cfg["sources"][0][0]
    bad = dict(maps[first])
    bad[1] = "DOMAIN" if bad[1] != "DOMAIN" else "PROCESS"
    (k1, k2), expect = next(iter(cfg["kat_pairs"].items()))
    probe = {k1: bad if k1 == first else maps[k1],
             k2: bad if k2 == first else maps[k2]}
    assert first in (k1, k2) and \
        agree(probe[k1], probe[k2], all_items) != expect, \
        "mutant KAT did not fire"
    return maps, torn_sites, all_items


def profile(maps, cfg, all_items):
    out = {}
    order = [s[0] for s in cfg["sources"]]
    for i in sorted(all_items):
        counts = {}
        for who in order:
            lab = maps[who][i]
            counts[lab] = counts.get(lab, 0) + 1
        modal = max(counts.values())
        out[i] = (counts, modal, len(counts))
    return out, order


def contested_items(prof, n_raters, corpus):
    """Registered per-corpus departure thresholds (README.md §Item set):
    iCal takes its ENTIRE >=2-departure dissent mass (14 items — the
    corpus is crisp enough to witness the whole boundary); QUIC's
    >=2-departure mass is 99 items (nearly twice the TLS archive's 53
    under the same rule), so the witness set takes the most contested
    tiers, >=5 of 12 departures, with the dropped tiers enumerated in
    the registration (no silent caps)."""
    thresh = {"ical": 2, "quic": 5}[corpus]
    return sorted(i for i in prof if n_raters - prof[i][1] >= thresh)


def sentences(cfg):
    text = (REPO / cfg["corpus_file"]).read_text()
    out = {}
    for line in text.splitlines():
        m = re.match(r"\[(\d+)\] (.*)", line.strip())
        if m:
            out[int(m.group(1))] = m.group(2)
    assert set(out) == set(range(1, cfg["n"] + 1))
    return out


def stable_sample(prof, n_raters, cfg):
    """Per unanimous class, first 3 items ranked by md5 of sentence text
    (the census self-audit's ordering, as in census/locality)."""
    sents = sentences(cfg)
    byclass = {}
    for i in prof:
        if prof[i][1] == n_raters:
            byclass.setdefault(next(iter(prof[i][0])), []).append(i)
    out = {}
    for lab, items in byclass.items():
        ranked = sorted(items, key=lambda i: hashlib.md5(
            sents[i].encode()).hexdigest())
        out[lab] = ranked[:3]
    return out


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in CORPORA:
        raise SystemExit("usage: profile2.py <ical|quic> [--profile | "
                         "--summary | --eligibility | --stable]")
    corpus = sys.argv[1]
    cfg = CORPORA[corpus]
    maps, torn_sites, all_items = load_all(corpus)
    prof, order = profile(maps, cfg, all_items)
    n_raters = len(order)
    mode = sys.argv[2] if len(sys.argv) > 2 else "--profile"
    if mode not in ("--profile", "--summary", "--eligibility", "--stable"):
        raise SystemExit("unknown mode %s" % mode)
    unanimous = [i for i in sorted(prof) if prof[i][1] == n_raters]
    if mode == "--stable":
        for lab, items in sorted(stable_sample(prof, n_raters, cfg).items()):
            print("%-10s %s" % (lab, items))
        return
    if mode == "--eligibility":
        elig = eligibility(prof, corpus, n_raters)
        for i in contested_items(prof, n_raters, corpus):
            if i in META_EXCLUDED[corpus]:
                print("%3d  (META-excluded)" % i)
                continue
            print("%3d  %s" % (i, ",".join(sorted(elig[i]))))
        return
    print("raters (%d): %s" % (n_raters, " ".join(order)))
    print("unanimous: %d/%d" % (len(unanimous), cfg["n"]))
    for depart in range(1, n_raters):
        n = sum(1 for i in prof if n_raters - prof[i][1] == depart)
        if n:
            print("  departures=%d: %d items" % (depart, n))
    print("contested (registered threshold): %s" %
          contested_items(prof, n_raters, corpus))
    if mode == "--profile":
        for i in sorted(prof):
            counts, modal, _ = prof[i]
            cell = " ".join("%s:%d" % (l, c) for l, c in
                            sorted(counts.items(), key=lambda kv: -kv[1]))
            torn = "".join(" torn:%s" % w for w in order
                           if i in torn_sites[w])
            print("%3d  %s%s" % (i, cell, torn))


# Registered vote->rung maps (README.md §Eligibility). Per-item overrides
# follow the registered assignment rules: an iCal DOMAIN vote claims
# locality at prop unless the compliance criterion references content
# outside one content line (another property, an occurrence count over the
# object) -> object; an iCal TYPESTATE vote targets in-object cross-property
# state (-> object) except where the referenced state is cross-artifact
# (185's inheritance across the scheduling transaction -> nonlocal); a QUIC
# THRESHOLD vote's rung follows rule 16's branches on where the quantity
# and bound live: conn-carried -> conn, clock- or path-valued -> nonlocal.
VOTE_RUNG = {
    "ical": {"DOMAIN": "prop", "TYPESTATE": "object", "PROCESS": "nonlocal",
             "U": "nonlocal", "POLICY": "nonlocal", "NEG": "nonlocal",
             "CV": "nonlocal", "REVOCABLE": "nonlocal"},
    "quic": {"DOMAIN": "pkt", "TYPESTATE": "conn", "PROCESS": "nonlocal",
             "U": "nonlocal", "POLICY": "nonlocal", "NEG": "nonlocal",
             "CV": "nonlocal", "REVOCABLE": "nonlocal"},
}
PER_ITEM_RUNG = {
    "ical": {
        "DOMAIN": {116: "object", 143: "object", 185: "object",
                   192: "object", 193: "object", 194: "object"},
        "TYPESTATE": {185: "nonlocal"},
        "THRESHOLD": {},
    },
    "quic": {
        "DOMAIN": {},
        "TYPESTATE": {},
        "THRESHOLD": {4: "conn", 9: "conn", 10: "conn", 17: "conn",
                      18: "conn", 26: "conn", 27: "conn", 62: "conn",
                      83: "conn", 94: "conn", 142: "conn", 254: "conn",
                      255: "conn", 258: "conn", 259: "conn", 262: "conn",
                      263: "conn", 109: "nonlocal", 190: "nonlocal"},
    },
}
# META obliges specification/extension authors — no runtime party, neither
# witness form applies (the TLS study's item-117 exclusion, applied by the
# same criterion): QUIC 53, 280 (unanimous META) and 281 (modal META).
META_EXCLUDED = {"ical": set(), "quic": {53, 280, 281}}


def eligibility(prof, corpus, n_raters):
    """Eligible rungs per witness-set item (contested set plus md5 stable
    sample): classes with >=2 votes, mapped through the registered
    vote->rung tables."""
    out = {}
    contested = [i for i in contested_items(prof, n_raters, corpus)
                 if i not in META_EXCLUDED[corpus]]
    sample = [i for items in
              stable_sample(prof, n_raters, CORPORA[corpus]).values()
              for i in items if i not in META_EXCLUDED[corpus]]
    for i in contested + sample:
        rungs = set()
        for lab, c in prof[i][0].items():
            if c < 2 or lab == "META":
                continue
            over = PER_ITEM_RUNG[corpus].get(lab, {})
            if lab == "THRESHOLD":
                rungs.add(over[i])
            else:
                rungs.add(over.get(i, VOTE_RUNG[corpus][lab]))
        out[i] = rungs
    return out


if __name__ == "__main__":
    main()
