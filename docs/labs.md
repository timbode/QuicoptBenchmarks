# LABS — Low-Autocorrelation Binary Sequences

Low-Autocorrelation Binary Sequences: find a ±1 sequence of length N minimizing the off-peak autocorrelation energy E = sum_k C_k^2. Quality is read as the merit factor F = N^2 / (2E) (higher is better). At these sizes the proven optimum exists only for N ≤ 66 and the whole field sits well above it, so no reference/gap column is shown here — the head-to-head against Gurobi and ABS2 lives on the website. Per row: `energy` is the best over 100 seeds; `wall_time_s` is the mean single-seed solve time.

| instance | N | energy | merit_factor | wall_time_s | hardware | solver |
| --- | --- | --- | --- | --- | --- | --- |
| LABS-4 | 4 | 2 | 4.0 | 0.01 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-5 | 5 | 2 | 6.25 | 0.01 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-6 | 6 | 7 | 2.57 | 0.01 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-7 | 7 | 3 | 8.17 | 0.01 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-8 | 8 | 8 | 4.0 | 0.02 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-9 | 9 | 12 | 3.38 | 0.02 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-10 | 10 | 13 | 3.85 | 0.02 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-11 | 11 | 5 | 12.1 | 0.02 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-12 | 12 | 10 | 7.2 | 0.02 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-13 | 13 | 6 | 14.08 | 0.03 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-14 | 14 | 19 | 5.16 | 0.03 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-15 | 15 | 23 | 4.89 | 0.03 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-16 | 16 | 24 | 5.33 | 0.03 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-17 | 17 | 32 | 4.52 | 0.04 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-18 | 18 | 25 | 6.48 | 0.04 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-19 | 19 | 37 | 4.88 | 0.05 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-20 | 20 | 34 | 5.88 | 0.05 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-21 | 21 | 34 | 6.49 | 0.06 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-22 | 22 | 39 | 6.21 | 0.07 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-23 | 23 | 51 | 5.19 | 0.07 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-24 | 24 | 52 | 5.54 | 0.08 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-25 | 25 | 56 | 5.58 | 0.09 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-26 | 26 | 61 | 5.54 | 0.1 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-27 | 27 | 37 | 9.85 | 0.11 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-28 | 28 | 74 | 5.3 | 0.12 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-29 | 29 | 78 | 5.39 | 0.13 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-30 | 30 | 83 | 5.42 | 0.14 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-31 | 31 | 83 | 5.79 | 0.16 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-32 | 32 | 80 | 6.4 | 0.18 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-33 | 33 | 104 | 5.24 | 0.19 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-34 | 34 | 97 | 5.96 | 0.21 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-35 | 35 | 109 | 5.62 | 0.24 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-36 | 36 | 114 | 5.68 | 0.26 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-37 | 37 | 106 | 6.46 | 0.28 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-38 | 38 | 135 | 5.35 | 0.31 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-39 | 39 | 139 | 5.47 | 0.34 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-40 | 40 | 144 | 5.56 | 0.37 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-41 | 41 | 140 | 6.0 | 0.4 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-42 | 42 | 157 | 5.62 | 0.44 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-43 | 43 | 161 | 5.74 | 0.47 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-44 | 44 | 186 | 5.2 | 0.52 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-45 | 45 | 170 | 5.96 | 0.55 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-46 | 46 | 155 | 6.83 | 0.6 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-47 | 47 | 219 | 5.04 | 0.65 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-48 | 48 | 208 | 5.54 | 0.72 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-49 | 49 | 224 | 5.36 | 0.77 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-50 | 50 | 257 | 4.86 | 0.84 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-51 | 51 | 221 | 5.88 | 0.89 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-52 | 52 | 242 | 5.59 | 0.95 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-53 | 53 | 238 | 5.9 | 1.07 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-54 | 54 | 263 | 5.54 | 1.13 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-55 | 55 | 299 | 5.06 | 1.22 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-56 | 56 | 304 | 5.16 | 1.26 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-57 | 57 | 316 | 5.14 | 1.39 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-58 | 58 | 301 | 5.59 | 1.46 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-59 | 59 | 313 | 5.56 | 1.57 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-60 | 60 | 346 | 5.2 | 1.68 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-61 | 61 | 358 | 5.2 | 1.81 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-62 | 62 | 371 | 5.18 | 1.92 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-63 | 63 | 351 | 5.65 | 2.04 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-64 | 64 | 396 | 5.17 | 2.21 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-65 | 65 | 400 | 5.28 | 2.3 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-66 | 66 | 417 | 5.22 | 2.46 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-67 | 67 | 357 | 6.29 | 2.63 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-68 | 68 | 442 | 5.23 | 2.8 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-69 | 69 | 470 | 5.06 | 2.27 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-70 | 70 | 479 | 5.11 | 3.4 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-71 | 71 | 519 | 4.86 | 3.61 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-72 | 72 | 508 | 5.1 | 3.7 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-73 | 73 | 544 | 4.9 | 3.99 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-74 | 74 | 565 | 4.85 | 4.25 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-75 | 75 | 569 | 4.94 | 4.38 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-76 | 76 | 586 | 4.93 | 4.57 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-77 | 77 | 646 | 4.59 | 5.0 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-78 | 78 | 667 | 4.56 | 5.27 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-79 | 79 | 647 | 4.82 | 5.51 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-80 | 80 | 632 | 5.06 | 5.88 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-81 | 81 | 672 | 4.88 | 6.24 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-82 | 82 | 681 | 4.94 | 6.62 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-83 | 83 | 733 | 4.7 | 6.97 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-84 | 84 | 730 | 4.83 | 7.37 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-85 | 85 | 742 | 4.87 | 7.92 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-86 | 86 | 767 | 4.82 | 8.33 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-87 | 87 | 763 | 4.96 | 8.76 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-88 | 88 | 740 | 5.23 | 9.3 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-89 | 89 | 828 | 4.78 | 9.78 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-90 | 90 | 845 | 4.79 | 10.69 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-91 | 91 | 857 | 4.83 | 11.33 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-92 | 92 | 738 | 5.73 | 11.81 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-93 | 93 | 854 | 5.06 | 13.06 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-94 | 94 | 915 | 4.83 | 13.54 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-95 | 95 | 867 | 5.2 | 14.13 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-96 | 96 | 984 | 4.68 | 14.48 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-97 | 97 | 1000 | 4.7 | 14.99 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-98 | 98 | 897 | 5.35 | 16.24 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-99 | 99 | 985 | 4.98 | 15.1 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |
| LABS-100 | 100 | 1022 | 4.89 | 10.81 | AMD EPYC-Rome (1 core) | Quicopt v0.1 |

---

<sub>Generated from [`../data/`](../data/) by [`../render.py`](../render.py). Reference values are third-party attributions, not Quicopt output.</sub>
