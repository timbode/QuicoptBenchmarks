#!/usr/bin/env python3
"""Render the benchmark tables in README.md from data/.

Self-contained: reads only data/<type>.csv + data/meta.json (both produced upstream) and
rewrites the region of README.md between the RESULTS markers. No external dependencies, no
knowledge of how the numbers were produced — this repo holds results, not a solver.

    python3 render.py            # rewrite README.md in place
    python3 render.py --check    # exit 1 if README.md is out of date (for CI)
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
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


def summary_line(header, rows, meta):
    """One-line headline from the %_of_best column, if present."""
    if "%_of_best" not in header:
        return ""
    i = header.index("%_of_best")
    pcts = sorted(float(r[i]) for r in rows if r[i] not in ("", None))
    if not pcts:
        return ""
    mid = pcts[len(pcts) // 2]
    ref = meta.get("reference_label", "best-known")
    return (f"**{len(pcts)}/{len(rows)} instances graded vs {ref}** — "
            f"median {mid:.1f}%, range {pcts[0]:.1f}–{pcts[-1]:.1f}% of {ref}.")


def render_sections():
    meta = json.loads((DATA / "meta.json").read_text()) if (DATA / "meta.json").exists() else {}
    parts = []
    for csv_path in sorted(DATA.glob("*.csv")):
        ptype = csv_path.stem
        m = meta.get(ptype, {})
        header, rows = read_csv(csv_path)
        parts.append(f"### {m.get('title', ptype)}\n")
        if m.get("blurb"):
            parts.append(f"{m['blurb']}\n")
        s = summary_line(header, rows, m)
        if s:
            parts.append(s + "\n")
        parts.append(md_table(header, rows) + "\n")
    return "\n".join(parts).rstrip() + "\n"


def splice(readme_text, body):
    if BEGIN not in readme_text or END not in readme_text:
        raise SystemExit(f"README.md must contain the markers {BEGIN} … {END}")
    pre = readme_text.split(BEGIN)[0]
    post = readme_text.split(END, 1)[1]
    return f"{pre}{BEGIN}\n\n{body}\n{END}{post}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if README.md is stale")
    args = ap.parse_args()
    new = splice(README.read_text(), render_sections())
    if args.check:
        if README.read_text() != new:
            raise SystemExit("README.md is out of date — run `python3 render.py`")
        print("README.md is up to date")
        return
    README.write_text(new)
    print(f"rendered {len(list(DATA.glob('*.csv')))} table(s) into {README.name}")


if __name__ == "__main__":
    main()
