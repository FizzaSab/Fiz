#!/usr/bin/env python3
"""Summarize the original glycosylation CSV files without changing their values."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "cleaned_glycosylation_dataset.csv",
    "filtered_feature_data/filtered_feature_data.csv",
)

def describe(relative_path):
    path = ROOT / relative_path
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        count = sum(1 for _ in reader)
    print(f"File: {relative_path}")
    print(f"Rows after header: {count}")
    print(f"Columns ({len(header)}): {', '.join(header)}")
    print()

def main():
    for name in FILES:
        describe(name)

if __name__ == "__main__":
    main()
