#!/usr/bin/env python3
"""Mechanical identifier+domain-noun obfuscation of the iCal corpus.

Deterministic: nonces generated from a fixed seed via a CV-syllable
generator, assigned in sorted-token order. Reversible: the map is a
bijection, applied longest-first at word boundaries; the round-trip
check (de-obfuscate == original, byte-identical) is asserted at build.
Retention tiers are REGISTERED, not improvised (see the map header).
"""
import re, json, random, sys

SEED = "enforceability-census-obfuscation-v1"

# --- Tier 1: REPLACED — RFC-5545-specific identifiers and scheduling-domain nouns.
UPPER_IDS = sorted({
 'DTSTART','DTEND','DUE','EXDATE','RDATE','RRULE','RECUR','TZID','TZOFFSETFROM','TZOFFSETTO',
 'PRODID','VERSION','METHOD','DURATION','FREEBUSY','FBTYPE','ATTENDEE','DESCRIPTION','SUMMARY',
 'ATTACH','ACTION','TRIGGER','REPEAT','UID','RECURRENCE-ID','UNTIL','COUNT','FREQ',
 'BYSECOND','BYMINUTE','BYHOUR','BYDAY','BYWEEKNO','BYMONTHDAY','BYYEARDAY',
 'MONTHLY','YEARLY','WEEKLY','DAILY','RSVP','ROLE','EMAIL','DISPLAY','AUDIO','URL',
 'VEVENT','VTODO','VJOURNAL','VALARM','VTIMEZONE','VFREEBUSY','STANDARD','DAYLIGHT',
 'THISANDPRIOR','UNKNOWN','BUSY','NEEDS-ACTION','PARENT','REQ-PARTICIPANT','PRIVATE',
 'ENCODING','START','END',
})
LOWER_IDS = sorted({'dur-day','dur-week','method',
 # quoted lowercase ABNF rule names (enumerated mechanically from the corpus)
 'todoprop','eventprop','standardc','daylightc','tzurl','last-mod'})
# lowercase ABNF aliases of UPPER_IDS get the same nonce, lowercased (added in build_map)
LOWER_ALIASES = sorted({'duration','repeat','due','dtend','dtstart','tzid','trigger','recur','action'})
XSTEMS = [('x-','q-'), ('iana-','zeta-'),
          ('x- ','q- '), ('iana- ','zeta- ')]      # morphology preserved, stems replaced
# the space-bearing variants catch the corpus's line-wrap artifact ("iana- token",
# item 37) byte-preservingly: the wrap space survives, the stem does not.
DOMAIN_NOUNS = sorted({'iCalendar','calendar','calendaring','event','to-do','journal','alarm','scheduling','attendee'})
# --- Tier 2: RETAINED (disclosed): MUST/SHALL/NOT/MAY/SHOULD/REQUIRED/OPTIONAL/RECOMMENDED;
# punctuation/ABNF names (COMMA SEMICOLON COLON DQUOTE BACKSLASH PLUS SIGN HYPHEN-MINUS LATIN
# SMALL CAPITAL LETTER); encoding/charset universals (BASE64 BINARY TEXT FLOAT URI MIME UTF-8
# charset); temporal universals (DATE TIME DATE-TIME UTC 'time zone' 'floating' 'leap'
# recurrence duration-as-English); structural nouns (object property parameter component value
# type grammar); numbers and section references; sibling-RFC citations (RFC2045/2368/3986).

try:
    ENGLISH = {w.strip().lower() for w in open('/usr/share/dict/words')}
except FileNotFoundError:
    ENGLISH = set()
ENGLISH |= {'fine','fines','lula','duri','dura','mira','sola','bela','dona','kola',
            'mesa','pita','sole','bone','dote','tame','mole','ride','vane','gala'}

def syllables(rng, n_syl, upper):
    C, V = 'bdfgklmnprstvz', 'aeiou'
    while True:
        w = ''.join(rng.choice(C) + rng.choice(V) for _ in range(n_syl))
        if w.lower() not in ENGLISH and (w.lower() + 's') not in ENGLISH:
            return w.upper() if upper else w

def build_map():
    rng = random.Random(SEED)
    m = {}
    used = set()
    def nonce(tok, upper, n_syl):
        while True:
            w = syllables(rng, n_syl, upper)
            if w not in used and w.lower() not in used:
                used.add(w); used.add(w.lower()); return w
    for t in UPPER_IDS:
        m[t] = nonce(t, True, 3 if len(t) > 6 else 2)
    for t in LOWER_IDS:
        m[t] = nonce(t, False, 2)
    for t in DOMAIN_NOUNS:
        m[t] = (nonce(t, False, 2).capitalize() if t[0].isupper() else nonce(t, False, 2))
    for t in LOWER_ALIASES:
        # quoted-ABNF alias: only within single quotes, same nonce as the UPPER form, lowercased
        m["'" + t + "'"] = "'" + m[t.upper().replace('_','-')].lower() + "'"
    return m

def apply_map(txt, m, reverse=False):
    pairs = [(v, k) for k, v in m.items()] if reverse else list(m.items())
    pairs += [(b, a) for a, b in XSTEMS] if reverse else XSTEMS
    # longest-first to avoid prefix shadowing
    for src, dst in sorted(pairs, key=lambda p: -len(p[0])):
        if src.startswith("'"):
            txt = txt.replace(src, dst)
        elif src.endswith('-') or src.endswith('- '):  # stem replacement (x- / iana-)
            txt = re.sub(r'\b' + re.escape(src) + r'(?=[a-z])', dst, txt)
        elif src[0].islower() or (len(src) > 1 and src[1:].islower()):
            # word-like token: match initial-cap variant and optional plural, preserve both
            def repl(mo, dst=dst):
                w = mo.group(1)
                out = dst.capitalize() if w[0].isupper() and dst[0].islower() else \
                      (dst[0].lower() + dst[1:] if w[0].islower() and dst[0].isupper() else dst)
                return out + mo.group(2)
            pat = r'\b(' + re.escape(src[0].upper() + src[1:]) + '|' + re.escape(src[0].lower() + src[1:]) + r')(s?)\b'
            txt = re.sub(pat, repl, txt)
        else:
            txt = re.sub(r'\b' + re.escape(src) + r'\b', dst, txt)
    return txt

if __name__ == '__main__':
    orig = open('census/ical/rfc5545_s3_musts.txt').read()
    m = build_map()
    obf = apply_map(orig, m)
    back = apply_map(obf, m, reverse=True)
    assert back == orig, "ROUND-TRIP FAIL: de-obfuscation is not byte-identical"
    # residual-leak scan: no tier-1 token may survive
    leak_pats = []
    for t in list(m) + ['x-param', 'iana-token', 'x-name', 'iana-comp',
                        'x- param', 'iana- token', 'x- name', 'iana- comp']:
        leak_pats.append(t)
        if t[0].isalpha() and (t[0].islower() or t[1:].islower()):
            leak_pats += [t + 's', t[0].upper() + t[1:], (t[0].upper() + t[1:]) + 's']
    leaks = sorted({p for p in leak_pats if re.search(r'\b' + re.escape(p) + r'\b', obf)})
    leaks += [s for s, _ in XSTEMS if re.search(r'\b' + re.escape(s) + r'(?=[a-z])', obf)]
    assert not leaks, f"LEAK: {leaks}"
    open(sys.argv[1], 'w').write(obf)
    json.dump(m, open(sys.argv[2], 'w'), indent=1, sort_keys=True)
    n = len(re.findall(r'(?m)^\[\d+\]', obf))
    print(f"obfuscated corpus written: {n} items; map: {len(m)} tokens + 2 stems; round-trip OK; no leaks")
