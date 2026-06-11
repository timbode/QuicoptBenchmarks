#!/usr/bin/env python3
"""Render the benchmark results from data/ into a summary landing + per-problem pages.

Self-contained: reads only data/<type>.csv + data/meta.json (both produced upstream) and writes
  - README.md  : a one-row-per-family summary table (between the RESULTS markers)
  - docs/<type>.md : the full per-instance table for each family
No external dependencies, no knowledge of how the numbers were produced — this repo holds
results, not a solver.

    python3 render.py            # rewrite README.md + docs/ pages in place
    python3 render.py --check    # exit 1 if any generated file is out of date (for CI)
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
README = ROOT / "README.md"
BEGIN, END = "<!-- BEGIN RESULTS -->", "<!-- END RESULTS -->"


def read_csv(path):
    with open(path) as fh:
        r = csv.reader(fh)
        return next(r), list(r)  # header, rows


def md_table(header, rows):
    line = lambda cells: "| " + " | ".join(str(c) for c in cells) + " |"
    out = [line(header), line(["---"] * len(header))]
    out += [line(r) for r in rows]
    return "\n".join(out)


def _pcts(header, rows):
    """Sorted %_of_best values, or None if the family has no such column."""
    if "%_of_best" not in header:
        return None
    i = header.index("%_of_best")
    return sorted(float(r[i]) for r in rows if r[i] not in ("", None))


def page_summary(header, rows, meta):
    """Full headline line for a problem page — only families with a %_of_best column have one."""
    pcts = _pcts(header, rows)
    if not pcts:
        return ""
    ref = meta.get("reference_label", "best-known")
    return (f"**{len(pcts)}/{len(rows)} instances graded vs {ref}** — "
            f"median {pcts[len(pcts) // 2]:.1f}%, range {pcts[0]:.1f}–{pcts[-1]:.1f}% of {ref}.")


def landing_headline(header, rows, meta):
    """Compact headline for the landing summary table cell."""
    pcts = _pcts(header, rows)
    if pcts:
        ref = meta.get("reference_label", "best-known")
        return f"{len(pcts)}/{len(rows)} graded — median {pcts[len(pcts) // 2]:.1f}% of {ref}"
    return meta.get("headline", "")


def families():
    meta = json.loads((DATA / "meta.json").read_text()) if (DATA / "meta.json").exists() else {}
    out = []
    for csv_path in sorted(DATA.glob("*.csv")):
        ptype = csv_path.stem
        header, rows = read_csv(csv_path)
        out.append((ptype, meta.get(ptype, {}), header, rows))
    return out


def page_text(ptype, m, header, rows):
    parts = [f"# {m.get('title', ptype)}\n"]
    if m.get("blurb"):
        parts.append(m["blurb"] + "\n")
    s = page_summary(header, rows, m)
    if s:
        parts.append(s + "\n")
    parts.append(md_table(header, rows) + "\n")
    parts.append("---\n\n<sub>Generated from [`../data/`](../data/) by [`../render.py`](../render.py). "
                 "Reference values are third-party attributions, not Quicopt output.</sub>\n")
    return "\n".join(parts)


def landing_body(fams):
    header = ["problem", "instances", "objective", "Quicopt result"]
    rows = []
    for ptype, m, h, r in fams:
        obj = m.get("objective_label", "")
        if m.get("objective_sense"):
            obj = f"{obj} ({m['objective_sense']})"
        rows.append([f"[{m.get('title', ptype)}](docs/{ptype}.md)", len(r), obj,
                     landing_headline(h, r, m)])
    return ("### Results by problem family\n\n"
            + md_table(header, rows)
            + "\n\nFull per-instance tables are in [`docs/`](docs/).")


def splice(readme_text, body):
    if BEGIN not in readme_text or END not in readme_text:
        raise SystemExit(f"README.md must contain the markers {BEGIN} … {END}")
    pre = readme_text.split(BEGIN)[0]
    post = readme_text.split(END, 1)[1]
    return f"{pre}{BEGIN}\n\n{body}\n{END}{post}"


def build():
    """Return {path: desired_text} for the landing README and every per-problem page."""
    fams = families()
    out = {DOCS / f"{ptype}.md": page_text(ptype, m, h, r) for ptype, m, h, r in fams}
    out[README] = splice(README.read_text(), landing_body(fams))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if any generated file is stale")
    args = ap.parse_args()
    out = build()
    if args.check:
        stale = [p for p, t in out.items() if not p.exists() or p.read_text() != t]
        if stale:
            names = ", ".join(str(p.relative_to(ROOT)) for p in stale)
            raise SystemExit(f"out of date: {names} — run `python3 render.py`")
        print("README.md + docs/ pages are up to date")
        return
    DOCS.mkdir(exist_ok=True)
    for p, t in out.items():
        p.write_text(t)
    print(f"rendered landing + {len(out) - 1} per-problem page(s)")


if __name__ == "__main__":
    main()
