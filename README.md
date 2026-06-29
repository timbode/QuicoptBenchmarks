# Quicopt Benchmarks

Public benchmark results for **Quicopt**, an optimization solver suite, on standard problem sets.
The summary below has one row per problem family; the full per-instance results live in
[`docs/`](docs/).

- **What this is:** benchmark results across standard problem sets, with the solver identified
  by version (`Quicopt vX.Y`).
- **Data:** machine-readable in [`data/`](data/) — [`results.json`](data/results.json) (all
  problem types) and one `<type>.csv` per family. The summary and the per-problem pages are
  generated from those files by [`render.py`](render.py); edit the data, not the prose tables.
- **Per-instance columns** vary by family: typically the instance and its size, the objective
  Quicopt achieved, our-hardware wall-time, and — where a confident literature value exists — the
  best-known / optimum, its source, and `%_of_best` (100 = matched). A family with no published
  reference at these sizes (e.g. LABS) reports the field's native quality metric instead.

<!-- BEGIN RESULTS -->

### Results by problem family

| problem | instances | objective | Quicopt result |
| --- | --- | --- | --- |
| [Gset — Maximum Cut](docs/gset.md) | 71 | cut (max) | 52/71 graded — median 100.0% of best-known |
| [LABS — Low-Autocorrelation Binary Sequences](docs/labs.md) | 97 | sidelobe energy (min) | median merit factor F ≈ 5 across N=4–100 |
| [Maximum Independent Set](docs/mis.md) | 50 | set size (max) | 50/50 graded — median 100.0% of best-known |

Full per-instance tables are in [`docs/`](docs/).
<!-- END RESULTS -->

---

<sub>Summary and per-problem pages auto-generated from `data/` by `render.py` (run in CI on every
data change). Where a family carries reference values, they are sourced per row and drift as new
records are published (see that family's `data/<type>.csv`). Reference values are attributions to
third-party results, not Quicopt output.</sub>
