#!/usr/bin/env python3
"""Read-only structural and syntax checks. NOT a scientific reproduction."""
from pathlib import Path
import ast
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ROWS = {
    "cleaned_glycosylation_dataset.csv": 801,
    "predicted_alpha_ratios_out_of_sample.csv": 169,
    "archive/unverified_workflows/glyc-ml/data/processed/gly_dataset.csv": 268,
    "archive/unverified_workflows/glyc-ml/data/Out-of-sample data.csv": 190,
}

def count_data_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return max(0, sum(1 for _ in csv.reader(handle)) - 1)

def main():
    passed = True
    for relative, expected in EXPECTED_ROWS.items():
        path = ROOT / relative
        try:
            actual = count_data_rows(path)
            is_ok = actual == expected
            print(f"{'PASS' if is_ok else 'FAIL'}: {relative}: {actual} rows (expected {expected})")
            passed = passed and is_ok
        except (OSError, UnicodeError, csv.Error) as exc:
            print(f"FAIL: cannot inspect {relative}: {exc}")
            passed = False

    scripts = sorted(ROOT.rglob("*.py"))
    for script in scripts:
        try:
            ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
        except (OSError, UnicodeError, SyntaxError) as exc:
            print(f"FAIL: Python syntax/read: {script.relative_to(ROOT)}: {exc}")
            passed = False

    print(f"Checked syntax of {len(scripts)} Python files (no model execution).")
    print("NOTE: The external 190 rows and prediction 169 rows cannot be automatically joined.")
    print("NOTE: This does NOT verify predictions, EFI coefficients, splits or manuscript metrics.")
    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(main())
