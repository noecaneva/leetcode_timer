# leetcode_timer

Lightweight harness to compare the performance of different implementations for LeetCode-style problems.

This repo is intended for collecting multiple implementations of the same problem and running timed experiments to compare them.

## Quick overview

- Add implementations for a problem under the problem's `implementations/` folder.
- Add the corresponding input cases under `inputs/`.
- Add or update results under `results/` when you run experiments.
- Each implementation should be registered in the `SOLUTIONS` dictionary (typically in the problem's implementation module) so it can be discovered by the benchmark runner in `control/`.

## Project structure

```
leetcode_timer/
├── control/                  # runner(s) / scripts for executing experiments
├── problems/
│   ├── daily_temperatures/
│   │    ├── inputs/          # test inputs for the problem
│   │    ├── implementations/# one folder/file per implementation
│   │    └── results/         # recorded results / outputs / timings
│   └── online_stock_span/
│        ├── inputs/
│        ├── implementations/
│        └── results/
```

## Languages

This repository contains Python code only.

## How to use

1. Clone or download the repo.
2. Add your solution to the appropriate `implementations/` folder (e.g., `impl.py` or analogous). Follow the structure of the other examples.
3. Register your solution in the problem's `SOLUTIONS` dictionary so the runner sees it.
4. Add or update test inputs in `inputs/`.
5. Run the benchmark/experiment runner in `control/` to compare implementations and collect timings.

Have fun comparing implementations :)!
