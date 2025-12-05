import os
import time
import csv
import importlib
from typing import List
import matplotlib.pyplot as plt
from pathlib import Path
import sys
from typing import List, Dict, Callable

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def time_function(func, arg, repeats: int = 10) -> float:
    """Return average runtime in seconds for func(arg)."""
    runtimes: List[float] = []
    try:
        for _ in range(repeats):
            start = time.perf_counter()
            func(arg)
            end = time.perf_counter()
            runtimes.append(end - start)
    except Exception as e:
        print(f"    Exception during timing: {e}")
        runtimes.append(float(100))  # large penalty
    return sum(runtimes) / len(runtimes)


def load_test_input(problem_name: str):
    """Import problems.<problem>.inputs.test_inputs and read TEST_INPUTi."""
    module_path = f"problems.{problem_name}.inputs.test_inputs"
    print(module_path)
    mod = importlib.import_module(module_path)
    inputs = {
        name: getattr(mod, name)
        for name in dir(mod)
        if name.startswith("TEST_INPUT")
    }

    return inputs

def get_solutions(problem_name: str) -> Dict[str, Callable]:
    """
    Import problems.<problem>.impl and read SOLUTIONS dict.

    SOLUTIONS must be a dict: name -> callable(input_data).
    """
    module_path = f"problems.{problem_name}.impl"
    try:
        mod = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("  No impl.py found, skipping.")
        return {}

    if not hasattr(mod, "SOLUTIONS"):
        print("  impl.py has no SOLUTIONS dict, skipping.")
        return {}

    solutions = getattr(mod, "SOLUTIONS")
    if not isinstance(solutions, dict):
        print("  SOLUTIONS is not a dict, skipping.")
        return {}

    # Optionally filter out non callables
    clean_solutions: Dict[str, Callable] = {}
    for name, func in solutions.items():
        if callable(func):
            clean_solutions[name] = func
        else:
            print(f"  skip {name} in SOLUTIONS, not callable")

    return clean_solutions

# the csv should have 2 rows: implementation, runtime, runs
# the path is to the csv of the results
def load_existing_impls(csv_path: str) -> List[str]:
    if not os.path.exists(csv_path):
        return []
    seen = set()
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            seen.add(row["implementation"])
    return list(seen)


# a mode in open() is the append mode, nothing that exists already
# will be overwritten
def append_results(csv_path: str, records: List[dict]):
    file_exists = os.path.exists(csv_path)
    fieldnames = ["implementation", "avg_runtime_s", "runs"]

    with open(csv_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for rec in records:
            writer.writerow(rec)


def update_plot(csv_path: str, plot_path: str):
    if not os.path.exists(csv_path):
        return

    names: List[str] = []
    values: List[float] = []

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            names.append(row["implementation"])
            values.append(float(row["avg_runtime_s"]))

    if not names:
        return

    plt.figure()
    plt.bar(names, values)
    plt.yscale("log")
    plt.ylabel("average runtime (s)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()


def run_for_problem(problem_name: str):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    problem_dir = os.path.join(base_dir, "problems", problem_name)
    results_dir = os.path.join(problem_dir, "results")
    os.makedirs(results_dir, exist_ok=True)

    timings_csv = os.path.join(results_dir, "timings.csv")
    plot_png = os.path.join(results_dir, "plot.png")

    print(f"\nProblem: {problem_name}")

    try:
        test_input = load_test_input(problem_name)
    except ModuleNotFoundError:
        print("  No test_input found, skipping.")
        return

    solutions = get_solutions(problem_name)
    if not solutions:
        print("  No implementation files, skipping.")
        return

    already_done = set(load_existing_impls(timings_csv))

    new_records: List[dict] = []
    for impl_name, impl_func in solutions.items():
        if impl_name in already_done:
            print(f"  skip {impl_name}, already in csv")
            continue

        print(f"  run  {impl_name}")
        nr_runs = 10
        avg = 0
        count = 0
        for test_input_name, test_input_val in test_input.items():
            avg += time_function(impl_func, test_input_val, repeats=nr_runs)
            count += 1
        avg /= count
        new_records.append(
            {
                "implementation": impl_name,
                "avg_runtime_s": f"{avg:.8f}",
                "runs": f"{nr_runs}",
            }
        )

    if new_records:
        append_results(timings_csv, new_records)
        update_plot(timings_csv, plot_png)
    else:
        print("  nothing new to run")


def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    problems_dir = os.path.join(base_dir, "problems")

    for name in os.listdir(problems_dir):
        if name == "__pycache__":
            continue
        path = os.path.join(problems_dir, name)
        if os.path.isdir(path):
            run_for_problem(name)


if __name__ == "__main__":
    main()

