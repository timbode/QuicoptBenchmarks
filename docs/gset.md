# Gset — Maximum Cut

Max-Cut on the standard Gset graphs (Stanford). Objective = cut value.

**52/71 instances graded vs best-known** — median 99.4%, range 97.1–100.0% of best-known.

| instance | N | edges | w | cut | best-known | %_of_best | wall_time_s | hardware | solver |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G1 | 800 | 19176 | +1 | 11623 | 11624 | 99.99 | 5.76 | NVIDIA A100 80GB | Quicopt v0.1 |
| G2 | 800 | 19176 | +1 | 11617 | 11620 | 99.97 | 0.7 | NVIDIA A100 80GB | Quicopt v0.1 |
| G3 | 800 | 19176 | +1 | 11621 | 11622 | 99.99 | 0.59 | NVIDIA A100 80GB | Quicopt v0.1 |
| G4 | 800 | 19176 | +1 | 11646 |  |  | 0.61 | NVIDIA A100 80GB | Quicopt v0.1 |
| G5 | 800 | 19176 | +1 | 11624 |  |  | 0.66 | NVIDIA A100 80GB | Quicopt v0.1 |
| G6 | 800 | 19176 | ±1 | 2175 |  |  | 0.61 | NVIDIA A100 80GB | Quicopt v0.1 |
| G7 | 800 | 19176 | ±1 | 2002 |  |  | 1.44 | NVIDIA A100 80GB | Quicopt v0.1 |
| G8 | 800 | 19176 | ±1 | 2002 |  |  | 0.61 | NVIDIA A100 80GB | Quicopt v0.1 |
| G9 | 800 | 19176 | ±1 | 2047 |  |  | 0.66 | NVIDIA A100 80GB | Quicopt v0.1 |
| G10 | 800 | 19176 | ±1 | 1997 |  |  | 0.62 | NVIDIA A100 80GB | Quicopt v0.1 |
| G11 | 800 | 1600 | ±1 | 564 | 564 | 100.00 | 0.48 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G12 | 800 | 1600 | ±1 | 556 | 556 | 100.00 | 0.47 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G13 | 800 | 1600 | ±1 | 582 | 582 | 100.00 | 0.43 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G14 | 800 | 4694 | +1 | 3041 | 3064 | 99.25 | 1.26 | NVIDIA A100 80GB | Quicopt v0.1 |
| G15 | 800 | 4661 | +1 | 3032 | 3050 | 99.41 | 1.34 | NVIDIA A100 80GB | Quicopt v0.1 |
| G16 | 800 | 4672 | +1 | 3037 | 3052 | 99.51 | 1.27 | NVIDIA A100 80GB | Quicopt v0.1 |
| G17 | 800 | 4667 | +1 | 3026 |  |  | 2.12 | NVIDIA A100 80GB | Quicopt v0.1 |
| G18 | 800 | 4694 | ±1 | 980 |  |  | 1.71 | NVIDIA A100 80GB | Quicopt v0.1 |
| G19 | 800 | 4661 | ±1 | 887 |  |  | 2.0 | NVIDIA A100 80GB | Quicopt v0.1 |
| G20 | 800 | 4672 | ±1 | 935 |  |  | 1.63 | NVIDIA A100 80GB | Quicopt v0.1 |
| G21 | 800 | 4667 | ±1 | 920 |  |  | 1.9 | NVIDIA A100 80GB | Quicopt v0.1 |
| G22 | 2000 | 19990 | +1 | 13327 | 13359 | 99.76 | 1.0 | NVIDIA A100 80GB | Quicopt v0.1 |
| G23 | 2000 | 19990 | +1 | 13326 |  |  | 1.7 | NVIDIA A100 80GB | Quicopt v0.1 |
| G24 | 2000 | 19990 | +1 | 13312 |  |  | 0.83 | NVIDIA A100 80GB | Quicopt v0.1 |
| G25 | 2000 | 19990 | +1 | 13313 | 13340 | 99.8 | 0.93 | NVIDIA A100 80GB | Quicopt v0.1 |
| G26 | 2000 | 19990 | +1 | 13299 | 13328 | 99.78 | 0.93 | NVIDIA A100 80GB | Quicopt v0.1 |
| G27 | 2000 | 19990 | ±1 | 3307 | 3341 | 98.98 | 0.91 | NVIDIA A100 80GB | Quicopt v0.1 |
| G28 | 2000 | 19990 | ±1 | 3275 | 3298 | 99.3 | 0.79 | NVIDIA A100 80GB | Quicopt v0.1 |
| G29 | 2000 | 19990 | ±1 | 3374 | 3405 | 99.09 | 1.64 | NVIDIA A100 80GB | Quicopt v0.1 |
| G30 | 2000 | 19990 | ±1 | 3381 | 3413 | 99.06 | 0.81 | NVIDIA A100 80GB | Quicopt v0.1 |
| G31 | 2000 | 19990 | ±1 | 3290 | 3309 | 99.43 | 0.93 | NVIDIA A100 80GB | Quicopt v0.1 |
| G32 | 2000 | 4000 | ±1 | 1410 | 1410 | 100.00 | 1.13 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G33 | 2000 | 4000 | ±1 | 1382 | 1382 | 100.00 | 1.38 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G34 | 2000 | 4000 | ±1 | 1384 | 1384 | 100.00 | 1.25 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G35 | 2000 | 11778 | +1 | 7618 |  |  | 2.2 | NVIDIA A100 80GB | Quicopt v0.1 |
| G36 | 2000 | 11766 | +1 | 7615 | 7678 | 99.18 | 3.96 | NVIDIA A100 80GB | Quicopt v0.1 |
| G37 | 2000 | 11785 | +1 | 7621 |  |  | 2.8 | NVIDIA A100 80GB | Quicopt v0.1 |
| G38 | 2000 | 11779 | +1 | 7621 | 7687 | 99.14 | 2.53 | NVIDIA A100 80GB | Quicopt v0.1 |
| G39 | 2000 | 11778 | ±1 | 2364 | 2408 | 98.17 | 3.13 | NVIDIA A100 80GB | Quicopt v0.1 |
| G40 | 2000 | 11766 | ±1 | 2334 | 2400 | 97.25 | 5.35 | NVIDIA A100 80GB | Quicopt v0.1 |
| G41 | 2000 | 11785 | ±1 | 2335 | 2405 | 97.09 | 3.57 | NVIDIA A100 80GB | Quicopt v0.1 |
| G42 | 2000 | 11779 | ±1 | 2417 | 2481 | 97.42 | 3.52 | NVIDIA A100 80GB | Quicopt v0.1 |
| G43 | 1000 | 9990 | +1 | 6653 | 6660 | 99.89 | 0.63 | NVIDIA A100 80GB | Quicopt v0.1 |
| G44 | 1000 | 9990 | +1 | 6646 |  |  | 1.55 | NVIDIA A100 80GB | Quicopt v0.1 |
| G45 | 1000 | 9990 | +1 | 6647 |  |  | 0.63 | NVIDIA A100 80GB | Quicopt v0.1 |
| G46 | 1000 | 9990 | +1 | 6641 |  |  | 0.79 | NVIDIA A100 80GB | Quicopt v0.1 |
| G47 | 1000 | 9990 | +1 | 6651 | 6657 | 99.91 | 0.53 | NVIDIA A100 80GB | Quicopt v0.1 |
| G48 | 3000 | 6000 | +1 | 5934 | 6000 | 98.9 | 0.8 | NVIDIA A100 80GB | Quicopt v0.1 |
| G49 | 3000 | 6000 | +1 | 5960 | 6000 | 99.33 | 0.82 | NVIDIA A100 80GB | Quicopt v0.1 |
| G50 | 3000 | 6000 | +1 | 5844 | 5880 | 99.39 | 1.58 | NVIDIA A100 80GB | Quicopt v0.1 |
| G51 | 1000 | 5909 | +1 | 3821 | 3848 | 99.3 | 1.56 | NVIDIA A100 80GB | Quicopt v0.1 |
| G52 | 1000 | 5916 | +1 | 3823 | 3851 | 99.27 | 1.58 | NVIDIA A100 80GB | Quicopt v0.1 |
| G53 | 1000 | 5914 | +1 | 3825 | 3850 | 99.35 | 1.35 | NVIDIA A100 80GB | Quicopt v0.1 |
| G54 | 1000 | 5916 | +1 | 3821 | 3852 | 99.2 | 1.45 | NVIDIA A100 80GB | Quicopt v0.1 |
| G55 | 5000 | 12498 | +1 | 10195 | 10294 | 99.04 | 2.15 | NVIDIA A100 80GB | Quicopt v0.1 |
| G56 | 5000 | 12498 | ±1 | 3907 | 4012 | 97.38 | 1.51 | NVIDIA A100 80GB | Quicopt v0.1 |
| G57 | 5000 | 10000 | ±1 | 3494 | 3494 | 100.00 | 3.19 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G58 | 5000 | 29570 | +1 | 19104 | 19263 | 99.17 | 10.72 | NVIDIA A100 80GB | Quicopt v0.1 |
| G59 | 5000 | 29570 | ±1 | 5919 | 6078 | 97.38 | 14.53 | NVIDIA A100 80GB | Quicopt v0.1 |
| G60 | 7000 | 17148 | +1 | 14028 | 14176 | 98.96 | 2.65 | NVIDIA A100 80GB | Quicopt v0.1 |
| G61 | 7000 | 17148 | ±1 | 5644 | 5789 | 97.5 | 2.67 | NVIDIA A100 80GB | Quicopt v0.1 |
| G62 | 7000 | 14000 | ±1 | 4866 | 4870 | 99.92 | 9.14 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G63 | 7000 | 41459 | +1 | 26761 | 27047 | 98.94 | 15.95 | NVIDIA A100 80GB | Quicopt v0.1 |
| G64 | 7000 | 41459 | ±1 | 8513 | 8735 | 97.46 | 20.03 | NVIDIA A100 80GB | Quicopt v0.1 |
| G65 | 8000 | 16000 | ±1 | 5560 | 5562 | 99.96 | 10.09 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G66 | 9000 | 18000 | ±1 | 6354 | 6364 | 99.84 | 22.79 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G67 | 10000 | 20000 | ±1 | 6948 | 6950 | 99.97 | 30.16 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G70 | 10000 | 9999 | +1 | 9448 | 9595 | 98.47 | 2.6 | NVIDIA A100 80GB | Quicopt v0.1 |
| G72 | 10000 | 20000 | ±1 | 7002 | 7008 | 99.91 | 30.80 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G77 | 14000 | 28000 | ±1 | 9934 | 9940 | 99.94 | 38.89 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |
| G81 | 20000 | 40000 | ±1 | 14044 | 14060 | 99.89 | 56.04 | AMD EPYC (CPU) | Quicopt v0.1 + post-solve |

---

<sub>Generated from [`../data/`](../data/) by [`../render.py`](../render.py). Reference values are third-party attributions, not Quicopt output.</sub>
