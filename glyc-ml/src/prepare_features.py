import argparse
import os
import pandas as pd
from utils import load_data, save_json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="data/processed")
    ap.add_argument("--make-splits", action="store_true")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)

    df = load_data(args.data)

    # Basic sanity checks (no EFI as feature—EFI_label only)
    assert "EFI_label" in df.columns, "EFI_label column missing"
    for col in ["alpha_ratio_pct","yield_pct","RRV","Aka","temperature_C","concentration_M","stoichiometry_ratio","solvent","promoter","donor_id","acceptor_id"]:
        if col not in df.columns:
            raise AssertionError(f"Missing column: {col}")

    # Save a simple ID column if not present
    if "row_id" not in df.columns:
        df.insert(0, "row_id", range(1, len(df)+1))

    out_path = os.path.join(args.out, "gly_dataset.cleaned.csv")
    df.to_csv(out_path, index=False)

    # Optional: create placeholder random split JSON
    if args.make_splits:
        n = len(df)
        fold = {
            "train_ids": df.loc[: int(0.9*n), "row_id"].tolist(),
            "test_ids":  df.loc[int(0.9*n)+1 :, "row_id"].tolist()
        }
        os.makedirs("data/splits", exist_ok=True)
        save_json({"folds": [fold]}, "data/splits/random.json")

if __name__ == "__main__":
    main()
