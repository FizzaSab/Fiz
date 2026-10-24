#!/usr/bin/env python3
"""Summarize the existing alpha-ratio prediction export without fitting a model."""
import csv
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
PREDICTIONS = ROOT / "predicted_alpha_ratios_out_of_sample.csv"

def main():
    with PREDICTIONS.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        column = "Predicted Alpha Ratio"
        if reader.fieldnames is None or column not in reader.fieldnames:
            raise ValueError(f"Expected column: {column}")
        values = [float(row[column]) for row in reader if row[column].strip()]
    if not values:
        raise ValueError("No numeric prediction values were found.")
    print(f"Source: {PREDICTIONS.name}")
    print(f"Saved predictions: {len(values)}")
    print(f"Minimum predicted alpha-ratio: {min(values):.4f}%")
    print(f"Mean predicted alpha-ratio: {mean(values):.4f}%")
    print(f"Maximum predicted alpha-ratio: {max(values):.4f}%")

if __name__ == "__main__":
    main()
