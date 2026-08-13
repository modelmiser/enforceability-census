#!/usr/bin/env python3
"""
Regenerate the Wayland declared-error corpus consumed by wayland-classifier.py.

Walks protocol XML files and emits one JSON row per <entry> of every
<enum name="error"> in every <interface>:
  {file, iface, name, summary, desc}

Usage:
  extract-corpus.py OUT.json XML_OR_DIR [XML_OR_DIR ...]

Notes (censoring/provenance — read before quoting a denominator):
- The 2026-08 census corpus was 172 errors / 77 interfaces from core
  wayland.xml + 36 extension files (3 of them from misc/experimental sets).
  Running this over a full wayland-protocols checkout (stable + staging +
  unstable + experimental) yields a SUPERSET; report n for the corpus you
  actually ran.
- Only enums literally named "error" are collected — that is the protocol's
  own declaration convention for post_error codes.
"""
import json, sys, xml.etree.ElementTree as ET
from pathlib import Path


def rows_from_xml(path):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        print(f'  SKIP (parse error): {path}: {e}', file=sys.stderr)
        return
    for iface in root.iter('interface'):
        for enum in iface.findall('enum'):
            if enum.get('name') != 'error':
                continue
            for entry in enum.findall('entry'):
                desc_el = entry.find('description')
                desc = (desc_el.text or '').strip() if desc_el is not None else ''
                yield {
                    'file': Path(path).name,
                    'iface': iface.get('name'),
                    'name': entry.get('name'),
                    'summary': (entry.get('summary') or '').strip(),
                    'desc': desc,
                }


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    out, srcs = sys.argv[1], sys.argv[2:]
    xmls = []
    for s in srcs:
        p = Path(s)
        xmls += sorted(p.rglob('*.xml')) if p.is_dir() else [p]
    # tests.xml in the core repo is a test fixture, not a protocol
    xmls = [x for x in xmls if x.name != 'tests.xml']
    rows = [r for x in xmls for r in rows_from_xml(x)]
    json.dump(rows, open(out, 'w'), indent=1)
    ifaces = {r['iface'] for r in rows}
    files = {r['file'] for r in rows}
    print(f'{len(rows)} declared errors / {len(ifaces)} interfaces / '
          f'{len(files)} files (of {len(xmls)} XML files scanned) -> {out}')


main()
