#!/usr/bin/env python3
"""Per-item agreement profile across every archived TLS-204 label map.

Selection input for the census/locality registration: parses all fourteen
archived full label maps for the RFC 8446 §4 corpus (rater A from the census
class table; C, D, Av4, Xv4, Av6, Xv6, Av7, Xv7, G, X, M, K, Z from their
reports' verbatim raw-label blocks), verifies the parse against nineteen
pairwise agreement numbers (eighteen published counts plus the Av6-Xv6
count uniquely implied by the v6 report's 93.1%) as known-answer tests,
and emits the per-item label distribution.

Rater B is EXCLUDED: its full map was never archived (provenance note in
census/tls13/rfc8446-s4-census.md); only 16 recorded labels exist.

Torn flags (trailing `?`) are stripped for the profile and for agreement
counts, matching the convention of every shipped scorer in this repository;
torn sites are reported separately.

Usage: python3 profile_tls.py [--profile | --summary | --eligibility |
                               --stable]
"""
import os
import pathlib
import re
import sys

REPO = pathlib.Path(os.environ.get(
    "CENSUS_REPO", pathlib.Path(__file__).resolve().parents[2]))

ALL_ITEMS = set(range(1, 205))

# (rater, file, heading substring, nth fenced block after heading, instrument)
# Instrument identities from the reports themselves: C rated under the v2
# paraphrase whose pass the pass-3 report declares INVALID as a
# codebook-v2 test (diagnostic as an instrument test); D rated under the
# SAME frozen blob a08febba as the five foreign raters (v3p4).
SOURCES = [
    ("C",   "census/tls13/rfc8446-s4-pass3.md",     "Raw labels (rater C",        0, "v2"),
    ("D",   "census/tls13/rfc8446-s4-pass4.md",     "Raw labels (rater D",        0, "v3p4"),
    ("Av4", "census/v4-tls/rfc8446-s4-v4pass.md",   "Raw labels (rater Av4",      0, "v4"),
    ("Xv4", "census/v4-tls/rfc8446-s4-v4pass.md",   "Raw labels (rater Xv4",      0, "v4"),
    ("Av6", "census/v6-pass/rfc-v6-pass.md",        "Raw labels (TLS: rater Av6", 0, "v6"),
    ("Xv6", "census/v6-pass/rfc-v6-pass.md",        "Raw labels (TLS: rater Av6", 1, "v6"),
    ("Av7", "census/v7-pass/rfc-v7-pass.md",        "Raw labels (TLS Av7",        0, "v7"),
    ("Xv7", "census/v7-pass/rfc-v7-pass.md",        "Raw labels (TLS Xv7",        0, "v7"),
    ("G",   "census/foreign/rfc8446-s4-foreign.md", "Raw labels (rater G",        0, "v3p4"),
    ("X",   "census/foreign/rfc8446-s4-foreign.md", "Raw labels (rater X",        0, "v3p4"),
    ("M",   "census/foreign2/rfc8446-s4-foreign2.md", "Raw labels (rater M",      0, "v3p4"),
    ("K",   "census/foreign2/rfc8446-s4-foreign2.md", "Raw labels (rater K",      0, "v3p4"),
    ("Z",   "census/foreign2/rfc8446-s4-foreign2.md", "Raw labels (rater Z",      0, "v3p4"),
]

# Published pairwise raw agreements (of 204) — known-answer tests.
# Sources: pass3 §comparison table (C-A 162), pass4 (D-A 171), v4 report
# (Av4-Xv4 188), v6 report (pair 93.1% -> 190), v7 report (Av7-Xv7 188),
# foreign report (G-A 164, X-A 178, G-D 166, X-D 187, G-X 176), foreign2
# pairwise table (M/K/Z vs each other and vs G/X).
KAT_PAIRS = {
    ("C", "A"): 162, ("D", "A"): 171,
    ("Av4", "Xv4"): 188, ("Av6", "Xv6"): 190, ("Av7", "Xv7"): 188,
    ("G", "A"): 164, ("X", "A"): 178,
    ("G", "D"): 166, ("X", "D"): 187, ("G", "X"): 176,
    ("M", "K"): 168, ("M", "Z"): 163, ("M", "G"): 171, ("M", "X"): 180,
    ("K", "Z"): 163, ("K", "G"): 164, ("K", "X"): 175,
    ("Z", "G"): 164, ("Z", "X"): 180,
}

# Rater A's per-class counts, asserted against the census table parse.
A_COUNTS = {"TYPESTATE": 94, "DOMAIN": 73, "PROCESS": 15, "CV": 6, "U": 6,
            "NEG": 3, "REVOCABLE": 2, "THRESHOLD": 2, "POLICY": 2, "META": 1}

A_CLASS_MAP = {
    "TYPESTATE (3)": "TYPESTATE", "DOMAIN (0)": "DOMAIN", "PROCESS": "PROCESS",
    "CRYPTO-VERIFY (prov.)": "CV", "UNCLASSIFIED-unverifiable": "U",
    "NEGOTIATION (prov.)": "NEG", "REVOCABLE (2)": "REVOCABLE",
    "THRESHOLD (1)": "THRESHOLD", "POLICY": "POLICY", "META": "META",
}

VALID = set(A_COUNTS)

# Alias normalization: the v6/v7 archives spell some labels in full.
ALIASES = {"NEGOTIATION": "NEG", "CRYPTO-VERIFY": "CV", "UNCLASSIFIED": "U",
           "CRYPTOVERIFY": "CV"}


def block_after(text, heading_substr, nth):
    idx = text.find(heading_substr)
    assert idx >= 0, "heading not found: %s" % heading_substr
    rest = text[idx:]
    end = rest.find("\n## ", 1)
    section = rest if end == -1 else rest[:end]
    blocks = re.findall(r"```\n(.*?)```", section, re.S)
    assert len(blocks) > nth, (heading_substr, len(blocks))
    return blocks[nth]


def parse_map(block, who):
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
    assert set(labels) == ALL_ITEMS, \
        "%s: items %s" % (who, sorted(ALL_ITEMS ^ set(labels)))
    return labels, torn


def parse_a():
    text = (REPO / "census/tls13/rfc8446-s4-census.md").read_text()
    labels = {}
    for row in re.findall(r"^\| (.+?) \| (\d+) \| [\d.]+% \| (.+?) \|?$",
                          text, re.M):
        cls, n, items_cell = row[0].strip(), int(row[1]), row[2]
        if cls not in A_CLASS_MAP:
            continue
        lab = A_CLASS_MAP[cls]
        cell = re.sub(r"\([^)]*\)", "", items_cell)
        items = [int(x) for x in re.findall(r"\d+", cell)]
        assert len(items) == n == A_COUNTS[lab], (cls, len(items), n)
        for i in items:
            assert i not in labels, "A: duplicate item %d" % i
            labels[i] = lab
    assert set(labels) == ALL_ITEMS, sorted(ALL_ITEMS ^ set(labels))
    return labels


def agree(m1, m2):
    return sum(1 for i in ALL_ITEMS if m1[i] == m2[i])


def load_all():
    maps = {"A": parse_a()}
    torn_sites = {"A": set()}
    for who, relpath, heading, nth, _gen in SOURCES:
        text = (REPO / relpath).read_text()
        maps[who], torn_sites[who] = parse_map(
            block_after(text, heading, nth), who)
    # Known-answer tests: the parse must reproduce every published number.
    for (r1, r2), expect in KAT_PAIRS.items():
        got = agree(maps[r1], maps[r2])
        assert got == expect, "KAT %s-%s: got %d, expect %d" % (
            r1, r2, got, expect)
    # Self-test: a perturbed copy must FAIL a KAT.
    bad = dict(maps["C"])
    bad[1] = "DOMAIN" if bad[1] != "DOMAIN" else "PROCESS"
    assert agree(bad, maps["A"]) != KAT_PAIRS[("C", "A")], \
        "mutant KAT did not fire"
    return maps, torn_sites


def profile(maps):
    out = {}
    order = ["A"] + [s[0] for s in SOURCES]
    for i in sorted(ALL_ITEMS):
        counts = {}
        for who in order:
            lab = maps[who][i]
            counts[lab] = counts.get(lab, 0) + 1
        modal = max(counts.values())
        out[i] = (counts, modal, len(counts))
    return out, order


# Registered vote->rung map (see README.md §Eligibility). THRESHOLD is
# per-item by rule 16's two branches: 188's quantity is in-datum, 189's is
# clock-valued.
VOTE_RUNG = {"DOMAIN": "msg", "TYPESTATE": "transcript", "NEG": "nonlocal",
             "PROCESS": "nonlocal", "CV": "nonlocal", "REVOCABLE": "nonlocal",
             "POLICY": "nonlocal", "U": "nonlocal"}
THRESHOLD_RUNG = {188: "msg", 189: "nonlocal"}
META_ITEM = 117


def contested_items(prof, n_raters):
    return sorted(i for i in prof if n_raters - prof[i][1] >= 4)


def eligibility(prof):
    """Eligible rungs per witness-set item: classes with >=2 of 14 votes."""
    out = {}
    n_raters = 14
    contested = contested_items(prof, n_raters)
    stable = [i for i in prof
              if prof[i][1] == n_raters and i != META_ITEM]
    # Stable sample is md5-selected in the registration; eligibility is
    # computable for any item — the checker cross-checks only its own set.
    for i in contested + stable:
        rungs = set()
        for lab, c in prof[i][0].items():
            if c < 2:
                continue
            if lab == "THRESHOLD":
                rungs.add(THRESHOLD_RUNG[i])
            elif lab in VOTE_RUNG:
                rungs.add(VOTE_RUNG[lab])
        out[i] = rungs
    return out


def sentences():
    text = (REPO / "census/tls13/rfc8446_s4_musts.txt").read_text()
    out = {}
    for line in text.splitlines():
        m = re.match(r"\[(\d+)\] (.*)", line.strip())
        if m:
            out[int(m.group(1))] = m.group(2)
    assert set(out) == ALL_ITEMS
    return out


def stable_sample(prof, n_raters):
    """Registration's stable sample: per unanimous class, first 3 items
    ranked by md5 of sentence text (the census self-audit's ordering)."""
    import hashlib
    sents = sentences()
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
    maps, torn_sites = load_all()
    prof, order = profile(maps)
    n_raters = len(order)
    mode = sys.argv[1] if len(sys.argv) > 1 else "--profile"
    if mode not in ("--profile", "--summary", "--eligibility", "--stable"):
        raise SystemExit("unknown mode %s (use --profile | --summary | "
                         "--eligibility | --stable)" % mode)
    unanimous = [i for i in sorted(prof) if prof[i][1] == n_raters]
    if mode == "--stable":
        for lab, items in sorted(stable_sample(prof, n_raters).items()):
            print("%-10s %s" % (lab, items))
        return
    if mode == "--eligibility":
        elig = eligibility(prof)
        for i in contested_items(prof, n_raters):
            print("%3d  %s" % (i, ",".join(sorted(elig[i]))))
        return
    print("raters (%d): %s" % (n_raters, " ".join(order)))
    print("unanimous: %d/204" % len(unanimous))
    for depart in range(1, n_raters):
        n = sum(1 for i in prof if n_raters - prof[i][1] == depart)
        if n:
            print("  departures=%d: %d items" % (depart, n))
    print("contested (>=4 departures): %s" %
          contested_items(prof, n_raters))
    if mode == "--profile":
        for i in sorted(prof):
            counts, modal, _ = prof[i]
            cell = " ".join("%s:%d" % (l, c) for l, c in
                            sorted(counts.items(), key=lambda kv: -kv[1]))
            torn = "".join(" torn:%s" % w for w in order
                           if i in torn_sites[w])
            print("%3d  %s%s" % (i, cell, torn))


if __name__ == "__main__":
    main()
