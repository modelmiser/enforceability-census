#!/usr/bin/env python3
"""Mechanical checker + grader for the second locality passes (README.md).

Shipped at registration time, BEFORE any witness exists: the grading is
fixed first. When a corpus's witness file is absent, runs that corpus's
self-tests and exits without grading it.

Witness schema (witnesses_ical.py / witnesses_quic.py each expose
WITNESSES: list, FAILS: list; rung names are per-corpus — iCal
prop/object/nonlocal, QUIC pkt/conn/nonlocal):

Validator entry (asserts locality of a reading at a rung):
  {"item": int, "reading": str, "rung": <fine>|<coarse>,
   "eligible": bool, "kind": "validator",
   "fn": callable-of-one-parameter, "accept": [datum, ...],
   "reject": [datum, ...], "quote": str,
   # coarse rung only — the fine-granularity distinguishing pair against
   # the best-candidate fine designation (README §Definitions):
   "pair_fine": <pair structure> }

Pair entry (asserts NON-locality of a reading; rung is always "nonlocal"
and datum_kind is the coarse granularity — the lemma then denies both
local rungs):
  {"item": int, "reading": str, "rung": "nonlocal", "eligible": bool,
   "kind": "pair", "pair": {"datum_kind": <coarse>, "datum": obj,
   "contexts": [{"desc": str, "channel": str, "verdict": bool,
                 "quote": str}, <same, opposite verdict>]}}

FAILS entry (an attempted construction that did not succeed — an honest
outcome, not evidence of impossibility):
  {"item": int, "rung": str, "reading": str, "reason": str,
   "channel": str}

Item outcome = set of rungs of eligible entries that pass all mechanical
checks. Contradiction flag: a validator and a pair sharing an item and an
identical reading string (the lemma forbids both).
"""
import inspect
import pathlib
import sys

if not __debug__:
    raise SystemExit("this checker's guards use assert — do not run with -O")

HERE = pathlib.Path(__file__).resolve().parent


def _pred(mapping):
    out = {}
    for items, rungs in mapping:
        for i in items:
            assert i not in out, "duplicate PRED for %d" % i
            out[i] = set(rungs)
    return out


CFG = {
    "ical": {
        "fine": "prop", "coarse": "object",
        "witness_module": "witnesses_ical",
        "channels": {"other-props", "other-artifacts", "party-conduct",
                     "deployment-policy", "private-intent",
                     "generation-process", "world-fact", "clock"},
        # Eligible rungs per item (README §Eligibility; re-derivable via
        # `profile2.py ical --eligibility`, cross-checked in self-tests).
        "eligible": {
            13: {"prop", "nonlocal"}, 43: {"prop", "nonlocal"},
            62: {"prop", "nonlocal"}, 77: {"prop", "nonlocal"},
            79: {"prop", "nonlocal"}, 91: {"prop", "nonlocal"},
            116: {"object", "nonlocal"}, 146: {"prop", "nonlocal"},
            150: {"prop", "nonlocal"}, 185: {"object", "nonlocal"},
            192: {"object"}, 193: {"object"}, 194: {"object"},
            210: {"prop", "nonlocal"},
            # stable sample
            63: {"prop"}, 84: {"prop"}, 143: {"object"},
            69: {"nonlocal"}, 118: {"nonlocal"}, 1: {"nonlocal"},
            201: {"nonlocal"}, 200: {"nonlocal"}, 7: {"nonlocal"},
        },
        # Predicted item outcomes (README §Predictions).
        "pred": _pred([
            ((63, 84), {"prop"}),
            ((143, 192, 193, 194), {"object"}),
            ((69, 118, 1, 201, 200, 7), {"nonlocal"}),
            ((13, 43, 62, 77, 79, 91, 146, 150, 210), {"nonlocal"}),
            ((116, 185), {"object", "nonlocal"}),
        ]),
        # E(i): DOMAIN+TYPESTATE strict majority (>=6 of 10 votes);
        # derivation in profile2.py, cross-checked in self-tests.
        "e_maj": {62, 63, 77, 79, 84, 116, 143, 185, 192, 193, 194},
        "named_exceptions": {62, 77, 79},
        "clauses": {
            "IC1": {"items": [63, 84, 143], "mode": "exact", "floor": 3},
            "IC2": {"items": [69, 118, 1, 201, 200, 7], "mode": "exact",
                    "floor": 6},
            "IC3": {"items": [13, 43, 62, 77, 79, 91, 146, 150, 210,
                              192, 193, 194], "mode": "exact", "floor": 10},
            "IC4": {"items": [116, 185], "mode": "multi", "floor": 2},
        },
        "corr_clause": "IC6",
        "corr_families": (({62, 77, 79}, 2),),
        "dup_pair": (43, 79),  # IC5: byte-identical corpus sentences
    },
    "quic": {
        "fine": "pkt", "coarse": "conn",
        "witness_module": "witnesses_quic",
        "channels": {"other-dgrams", "prior-connection", "secret-material",
                     "clock", "party-conduct", "counterparty-config",
                     "deployment-policy", "private-intent",
                     "generation-process", "network-path"},
        "eligible": {
            4: {"conn"}, 9: {"conn"}, 10: {"conn"}, 17: {"conn"},
            18: {"conn"}, 26: {"conn"}, 27: {"conn"}, 254: {"conn"},
            255: {"conn"}, 258: {"conn"}, 259: {"conn"}, 262: {"conn"},
            263: {"conn"}, 142: {"conn"},
            23: {"conn", "nonlocal"}, 29: {"conn", "nonlocal"},
            32: {"pkt", "nonlocal"}, 33: {"pkt", "conn", "nonlocal"},
            54: {"conn", "nonlocal"}, 55: {"conn", "nonlocal"},
            59: {"conn", "nonlocal"}, 81: {"nonlocal"}, 84: {"nonlocal"},
            109: {"nonlocal"}, 128: {"conn", "nonlocal"},
            138: {"pkt", "nonlocal"}, 144: {"pkt", "conn", "nonlocal"},
            152: {"pkt", "conn"}, 162: {"conn", "nonlocal"},
            190: {"conn", "nonlocal"}, 235: {"pkt", "conn"},
            # stable sample
            236: {"pkt"}, 249: {"pkt"}, 49: {"pkt"},
            171: {"conn"}, 78: {"conn"}, 58: {"conn"},
            94: {"conn"}, 83: {"conn"}, 62: {"conn"},
            40: {"nonlocal"}, 230: {"nonlocal"}, 34: {"nonlocal"},
            207: {"nonlocal"}, 107: {"nonlocal"}, 92: {"nonlocal"},
            80: {"nonlocal"}, 119: {"nonlocal"}, 75: {"nonlocal"},
        },
        "pred": _pred([
            ((236, 249, 49), {"pkt"}),
            ((171, 78), {"conn"}),
            ((58,), set()),  # eliminable-voted 12/12, predicted UNWITNESSABLE
            ((40, 230, 34, 207, 107, 92, 80, 119, 75), {"nonlocal"}),
            ((94, 83, 62), {"conn"}),
            ((4, 9, 10, 17, 18, 26, 27, 254, 255, 258, 259, 262, 263,
              235, 142), {"conn"}),
            ((54, 55, 59, 29, 32, 33, 81, 84, 109, 138, 23, 128, 190),
             {"nonlocal"}),
            ((152,), {"pkt", "conn"}),
            ((162, 144), {"conn", "nonlocal"}),
        ]),
        # E(i): DOMAIN+TYPESTATE strict majority (>=7 of 12 votes).
        "e_maj": {32, 49, 58, 59, 78, 142, 144, 152, 162, 171, 235,
                  236, 249},
        "named_exceptions": {4, 9, 10, 17, 18, 26, 27, 254, 255, 258, 259,
                             262, 263, 94, 83, 62, 32, 58, 59},
        "clauses": {
            "QC1": {"items": [236, 249, 49], "mode": "exact", "floor": 3},
            "QC2": {"items": [171, 78, 58], "mode": "exact", "floor": 3},
            "QC3": {"items": [40, 230, 34, 207, 107, 92, 80, 119, 75],
                    "mode": "exact", "floor": 9},
            "QC4": {"items": [94, 83, 62], "mode": "exact", "floor": 3},
            "QC5": {"items": [4, 9, 10, 17, 18, 26, 27, 254, 255, 258,
                              259, 262, 263, 235, 142,
                              54, 55, 59, 29, 32, 33, 81, 84, 109, 138,
                              23, 128, 190], "mode": "exact", "floor": 24},
            "QC6": {"items": [152, 162, 144], "mode": "multi", "floor": 2},
        },
        "corr_clause": "QC7",
        "corr_families": (
            ({4, 9, 10, 17, 18, 26, 27, 254, 255, 258, 259, 262, 263,
              94, 83, 62}, 13),   # (a) L-and-not-E, floor 13/16
            ({32, 58, 59}, 2),    # (b) not-L-and-E, floor 2/3
        ),
        "dup_pair": None,
    },
}

for _c in CFG.values():
    assert set(_c["pred"]) == set(_c["eligible"])
    _fams = [f for f, _fl in _c["corr_families"]]
    assert set().union(*_fams) == _c["named_exceptions"]
    assert sum(len(f) for f in _fams) == len(_c["named_exceptions"])
assert len(CFG["ical"]["eligible"]) == 23
assert len(CFG["quic"]["eligible"]) == 49


class WitnessError(Exception):
    pass


def check_pair(pair, where, cfg):
    if pair.get("datum_kind") not in (cfg["fine"], cfg["coarse"]):
        raise WitnessError("%s: bad datum_kind" % where)
    if "datum" not in pair:
        raise WitnessError("%s: pair missing datum" % where)
    ctxs = pair.get("contexts")
    if not isinstance(ctxs, list) or len(ctxs) != 2:
        raise WitnessError("%s: pair needs exactly 2 contexts" % where)
    verdicts = []
    for c in ctxs:
        if c.get("channel") not in cfg["channels"]:
            raise WitnessError("%s: unknown channel %r" % (where,
                                                           c.get("channel")))
        if not isinstance(c.get("verdict"), bool):
            raise WitnessError("%s: verdict must be bool" % where)
        for k in ("desc", "quote"):
            if not (isinstance(c.get(k), str) and c[k].strip()):
                raise WitnessError("%s: empty %s" % (where, k))
        verdicts.append(c["verdict"])
    if verdicts[0] == verdicts[1]:
        raise WitnessError("%s: verdicts do not differ — not a "
                           "distinguishing pair" % where)


def check_validator(w, where):
    fn = w.get("fn")
    if not callable(fn):
        raise WitnessError("%s: fn not callable" % where)
    params = inspect.signature(fn).parameters
    if len(params) != 1:
        raise WitnessError("%s: validator must take exactly one parameter "
                           "(the datum) — it takes %d" % (where, len(params)))
    acc, rej = w.get("accept"), w.get("reject")
    if not acc or not rej:
        raise WitnessError("%s: needs >=1 accept AND >=1 reject vector "
                           "(a predicate with no reject vector is vacuous)"
                           % where)
    for v in acc:
        if fn(v) is not True:
            raise WitnessError("%s: accept vector not accepted" % where)
    for v in rej:
        if fn(v) is not False:
            raise WitnessError("%s: reject vector not rejected" % where)
    if not (isinstance(w.get("quote"), str) and w["quote"].strip()):
        raise WitnessError("%s: empty quote" % where)


def check_entry(w, cfg):
    item = w.get("item")
    where = "item %s (%s)" % (item, w.get("rung"))
    if item not in cfg["eligible"]:
        raise WitnessError("%s: not in the registered item set" % where)
    if w.get("rung") not in (cfg["fine"], cfg["coarse"], "nonlocal"):
        raise WitnessError("%s: bad rung" % where)
    if not (isinstance(w.get("reading"), str) and w["reading"].strip()):
        raise WitnessError("%s: empty reading" % where)
    if not isinstance(w.get("eligible"), bool):
        raise WitnessError("%s: eligible must be bool" % where)
    if w["eligible"] and w["rung"] not in cfg["eligible"][item]:
        raise WitnessError("%s: marked eligible but rung not in the "
                           "registered eligibility table" % where)
    if w.get("kind") == "validator":
        if w["rung"] == "nonlocal":
            raise WitnessError("%s: a validator cannot have rung nonlocal"
                               % where)
        check_validator(w, where)
        if w["rung"] == cfg["coarse"]:
            if "pair_fine" not in w:
                raise WitnessError("%s: coarse rung requires pair_fine"
                                   % where)
            check_pair(w["pair_fine"], where + " pair_fine", cfg)
            if w["pair_fine"]["datum_kind"] != cfg["fine"]:
                raise WitnessError("%s: pair_fine must have datum_kind %s"
                                   % (where, cfg["fine"]))
    elif w.get("kind") == "pair":
        if w["rung"] != "nonlocal":
            raise WitnessError("%s: pair entries assert rung nonlocal"
                               % where)
        check_pair(w.get("pair", {}), where, cfg)
        if w["pair"]["datum_kind"] != cfg["coarse"]:
            raise WitnessError("%s: nonlocal pair must be at %s granularity"
                               % (where, cfg["coarse"]))
    else:
        raise WitnessError("%s: bad kind" % where)


def outcomes(witnesses, cfg):
    out = {i: set() for i in cfg["eligible"]}
    for w in witnesses:
        check_entry(w, cfg)
        if w["eligible"]:
            out[w["item"]].add(w["rung"])
    for w in witnesses:
        if w["kind"] != "validator":
            continue
        for v in witnesses:
            if (v["kind"] == "pair" and v["item"] == w["item"]
                    and v["reading"] == w["reading"]):
                raise WitnessError(
                    "item %d: validator and pair share reading %r — the "
                    "lemma forbids both; resolve in the report"
                    % (w["item"], w["reading"]))
    return out


def check_fails(fails, cfg):
    for f in fails:
        for k in ("item", "rung", "reading", "reason", "channel"):
            assert isinstance(f.get(k), (int, str)) and str(f[k]).strip(), \
                "FAILS entry missing/empty %s: %r" % (k, f)
        assert f["item"] in cfg["eligible"], \
            "FAILS item %r not registered" % f["item"]
        assert f["rung"] in (cfg["fine"], cfg["coarse"], "nonlocal"), \
            "FAILS rung %r unknown" % f["rung"]
        assert f["channel"] in cfg["channels"], \
            "FAILS channel %r not in vocabulary" % f["channel"]


def check_coverage(out, fails, cfg):
    """FAILS coverage (README §Non-circularity): every registered eligible
    rung is either witnessed or carries a FAILS record for that item+rung.
    An unwitnessed rung cannot be silently dropped."""
    covered = {(f["item"], f["rung"]) for f in fails}
    missing = sorted(
        (i, r) for i in cfg["eligible"] for r in cfg["eligible"][i]
        if r not in out[i] and (i, r) not in covered)
    if missing:
        raise WitnessError(
            "eligible rungs neither witnessed nor FAILS-recorded: %s"
            % missing)


def grade(out, cfg):
    results = []
    pred, local = cfg["pred"], {cfg["fine"], cfg["coarse"]}

    def clause(name, ok, detail):
        results.append((name, ok, detail))

    for name in sorted(cfg["clauses"]):
        c = cfg["clauses"][name]
        n = len(c["items"])
        if c["mode"] == "exact":
            got = sum(1 for i in c["items"] if out[i] == pred[i])
            clause("%s exact >=%d/%d" % (name, c["floor"], n),
                   got >= c["floor"], "%d/%d" % (got, n))
        else:
            got = sum(1 for i in c["items"] if len(out[i]) >= 2)
            gotx = sum(1 for i in c["items"] if out[i] == pred[i])
            clause("%s multi-rung >=%d/%d" % (name, c["floor"], n),
                   got >= c["floor"],
                   "%d/%d multi (exact-set %d/%d)" % (got, n, gotx, n))
    mism = {i for i in cfg["eligible"]
            if bool(out[i] & local) != (i in cfg["e_maj"])}
    unnamed = sorted(mism - cfg["named_exceptions"])
    fam_ok, fam_detail = True, []
    for fam, floor in cfg["corr_families"]:
        got = len(mism & fam)
        fam_ok = fam_ok and got >= floor
        fam_detail.append("%d/%d (floor %d)" % (got, len(fam), floor))
    clause("%s correspondence: 0 unnamed AND per-family floors"
           % cfg["corr_clause"],
           not unnamed and fam_ok,
           "unnamed=%s families %s" % (unnamed, "; ".join(fam_detail)))
    if cfg["dup_pair"]:
        a, b = cfg["dup_pair"]
        ok = (out[a] == out[b]) and (b in mism) and (a not in mism)
        clause("IC5 duplicate-text control (%d,%d)" % (a, b), ok,
               "outcomes %s/%s; mismatch has %d:%s %d:%s"
               % (sorted(out[a]), sorted(out[b]), b, b in mism,
                  a, a in mism))
    return results, mism


def self_test(corpus):
    cfg = CFG[corpus]
    fine, coarse = cfg["fine"], cfg["coarse"]
    ch = sorted(cfg["channels"])[0]
    nl_item = next(i for i in sorted(cfg["eligible"])
                   if cfg["eligible"][i] == {"nonlocal"})
    fine_item = next(i for i in sorted(cfg["eligible"])
                     if cfg["eligible"][i] == {fine})
    ok_pair = {"datum_kind": coarse, "datum": {"x": 1}, "contexts": [
        {"desc": "a", "channel": ch, "verdict": True, "quote": "q"},
        {"desc": "b", "channel": ch, "verdict": False, "quote": "q"}]}
    base = {"item": nl_item, "reading": "r", "rung": "nonlocal",
            "eligible": True, "kind": "pair", "pair": ok_pair}
    check_entry(dict(base), cfg)  # the fixture itself must pass

    def must_fail(entry, why):
        try:
            check_entry(entry, cfg)
        except WitnessError:
            return
        raise AssertionError("mutant not rejected: %s" % why)

    v = {"item": fine_item, "reading": "r", "rung": fine, "eligible": True,
         "kind": "validator", "fn": lambda d: bool(d.get("ok")),
         "accept": [{"ok": 1}], "reject": [{}], "quote": "q"}
    check_entry(dict(v), cfg)
    must_fail({**v, "fn": lambda a, b: True}, "arity-2 validator")
    must_fail({**v, "reject": []}, "no reject vectors")
    must_fail({**v, "fn": lambda d: True}, "reject vector accepted")
    bad = {**base, "pair": {**ok_pair, "contexts": [
        dict(ok_pair["contexts"][0]), dict(ok_pair["contexts"][0])]}}
    must_fail(bad, "same-verdict pair")
    bad = {**base, "pair": {**ok_pair, "contexts": [
        {**ok_pair["contexts"][0], "channel": "vibes"},
        ok_pair["contexts"][1]]}}
    must_fail(bad, "unknown channel")
    must_fail({**base, "rung": fine}, "pair at fine rung")
    must_fail({**v, "item": nl_item}, "eligible validator outside table")
    must_fail({**v, "rung": coarse}, "coarse validator without pair_fine")
    # FAILS-validation mutants.
    ok_fail = {"item": fine_item, "rung": fine, "reading": "r",
               "reason": "why", "channel": ch}
    check_fails([dict(ok_fail)], cfg)
    for bad in ({**ok_fail, "channel": "vibes"},
                {**ok_fail, "rung": "wire"},
                {**ok_fail, "item": -1},
                {**ok_fail, "reason": " "}):
        try:
            check_fails([bad], cfg)
            raise SystemExit("FAILS mutant not rejected: %r" % bad)
        except AssertionError:
            pass
    # Contradiction mutant: a validator and pair sharing item+reading.
    try:
        outcomes([dict(v), {"item": fine_item, "reading": "r",
                            "rung": "nonlocal", "eligible": False,
                            "kind": "pair", "pair": dict(ok_pair)}], cfg)
        raise SystemExit("contradiction mutant not rejected")
    except WitnessError:
        pass
    # Further structural mutants.
    must_fail({**base, "pair": {**ok_pair, "contexts":
                                [ok_pair["contexts"][0]]}}, "1-context pair")
    must_fail({**base, "pair": {k: vv for k, vv in ok_pair.items()
                                if k != "datum"}}, "missing datum")
    must_fail({**v, "reading": "  "}, "empty reading")
    must_fail({**v, "accept": [{}]}, "accept vector rejected by fn")
    must_fail({**v, "rung": coarse, "pair_fine":
               {**ok_pair, "datum_kind": coarse}},
              "pair_fine at coarse datum_kind")
    # FAILS-coverage mutants: an uncovered eligible rung must raise; the
    # same rung FAILS-recorded must pass.
    empty_out = {i: set() for i in cfg["eligible"]}
    try:
        check_coverage(empty_out, [], cfg)
        raise SystemExit("coverage mutant not rejected")
    except WitnessError:
        pass
    all_fails = [{"item": i, "rung": r, "reading": "r", "reason": "x",
                  "channel": ch} for i in cfg["eligible"]
                 for r in cfg["eligible"][i]]
    check_coverage(empty_out, all_fails, cfg)
    full_out = {i: set(cfg["eligible"][i]) for i in cfg["eligible"]}
    check_coverage(full_out, [], cfg)
    # Grading mutants: perfect-prediction outcomes pass every clause;
    # per-clause flips must break exactly their clause.
    perfect = {i: set(cfg["pred"][i]) for i in cfg["eligible"]}
    res, _ = grade(perfect, cfg)
    for name, ok, _d in res:
        assert ok is not False, "perfect outcomes fail %s" % name

    def broken_grade(changes, prefix):
        broken = {i: set(cfg["pred"][i]) for i in cfg["eligible"]}
        broken.update({k: set(vv) for k, vv in changes.items()})
        res_b, _m = grade(broken, cfg)
        ok_b = [ok for name, ok, _d in res_b if name.startswith(prefix)][0]
        assert ok_b is False, "grading mutant %s did not fire" % prefix

    all_r = {fine, coarse, "nonlocal"}
    for name in sorted(cfg["clauses"]):
        c = cfg["clauses"][name]
        n_break = len(c["items"]) - c["floor"] + 1
        broken_grade({i: (all_r - cfg["pred"][i] or {fine})
                      if c["mode"] == "exact" else
                      (set(list(cfg["pred"][i])[:1]) or {fine})
                      for i in c["items"][:n_break]}, name)
    # Correspondence mutant: strip a local rung from a match-predicted
    # local item -> one unnamed mismatch.
    local_match = next(i for i in sorted(cfg["eligible"])
                       if i in cfg["e_maj"]
                       and i not in cfg["named_exceptions"]
                       and cfg["pred"][i] & {fine, coarse})
    broken_grade({local_match: {"nonlocal"}}, cfg["corr_clause"])
    # Per-family floor mutant: un-realize one whole family (its items
    # fall back to E-matching outcomes) while the others stay realized —
    # the correspondence clause must fail on the sub-floor alone.
    for fam, _floor in cfg["corr_families"]:
        broken_grade({i: ({coarse} if i in cfg["e_maj"] else {"nonlocal"})
                      for i in fam}, cfg["corr_clause"])
    if cfg["dup_pair"]:
        a, b = cfg["dup_pair"]
        broken_grade({a: {fine}}, "IC5")
    # Cross-check embedded tables against the derivation tool.
    # Unconditional: the archive reports ship in this repository, so a
    # missing file is a failure, not a skip.
    sys.path.insert(0, str(HERE))
    import profile2
    maps, _torn, all_items = profile2.load_all(corpus)
    prof, order = profile2.profile(maps, profile2.CORPORA[corpus], all_items)
    n_raters = len(order)
    derived = profile2.eligibility(prof, corpus, n_raters)
    assert set(derived) == set(cfg["eligible"]), (
        "item-set drift: derived-only %s, embedded-only %s"
        % (sorted(set(derived) - set(cfg["eligible"])),
           sorted(set(cfg["eligible"]) - set(derived))))
    for i in cfg["eligible"]:
        assert derived[i] == cfg["eligible"][i], (
            "eligibility drift at %d: derived %s, embedded %s"
            % (i, sorted(derived[i]), sorted(cfg["eligible"][i])))
    maj = n_raters // 2 + 1
    derived_emaj = {i for i in cfg["eligible"]
                    if sum(c for l, c in prof[i][0].items()
                           if l in ("DOMAIN", "TYPESTATE")) >= maj}
    assert derived_emaj == cfg["e_maj"], (
        "E_MAJ drift: derived-only %s, embedded-only %s"
        % (sorted(derived_emaj - cfg["e_maj"]),
           sorted(cfg["e_maj"] - derived_emaj)))
    if cfg["dup_pair"]:
        a, b = cfg["dup_pair"]
        sents = profile2.sentences(profile2.CORPORA[corpus])
        assert sents[a] == sents[b], "dup-pair texts differ"
    print("%s self-tests: rejection paths fire; FAILS validation and "
          "FAILS-coverage enforcement fire; grading mutants fire for "
          "every clause including per-family correspondence floors; "
          "eligibility and E_MAJ match the archive derivation" % corpus)


def main():
    for corpus in ("ical", "quic"):
        cfg = CFG[corpus]
        self_test(corpus)
        wpath = HERE / (cfg["witness_module"] + ".py")
        if not wpath.exists():
            print("no %s.py yet — registration-time run, nothing to grade"
                  % cfg["witness_module"])
            continue
        sys.path.insert(0, str(HERE))
        mod = __import__(cfg["witness_module"])
        out = outcomes(mod.WITNESSES, cfg)
        check_fails(mod.FAILS, cfg)
        check_coverage(out, mod.FAILS, cfg)
        print("%s witness entries: %d (+%d recorded construction failures)"
              % (corpus, len(mod.WITNESSES), len(mod.FAILS)))
        for i in sorted(cfg["eligible"]):
            marker = "" if out[i] == cfg["pred"][i] else \
                "   <- predicted %s" % (sorted(cfg["pred"][i]),)
            print("%3d  %-25s%s" % (i, ",".join(sorted(out[i])) or "-",
                                    marker))
        res, mism = grade(out, cfg)
        print()
        for name, ok, detail in res:
            print("%-6s %s — %s" % ("PASS" if ok else "FAIL", name, detail))
        print("%s mismatch set: %s" % (corpus, sorted(mism)))
        print()


if __name__ == "__main__":
    main()
