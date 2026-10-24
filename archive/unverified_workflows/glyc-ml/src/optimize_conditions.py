import argparse, joblib, pandas as pd, numpy as np
from config import *
from utils import load_data
from category_encoders.one_hot import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# NOTE: Simple discrete search over candidate conditions for a fixed donor/acceptor.
# Describe as a heuristic inverse design in the paper.

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/processed/gly_dataset.cleaned.csv")
    ap.add_argument("--donor_id", required=True)
    ap.add_argument("--acceptor_id", required=True)
    ap.add_argument("--models_dir", default="models")
    args = ap.parse_args()

    df = load_data(args.data)
    artifacts = joblib.load(f"{args.models_dir}/artifacts.pkl")
    model_alpha = joblib.load(f"{args.models_dir}/rf_alpha.pkl")  # or xgb
    model_yield = joblib.load(f"{args.models_dir}/rf_yield.pkl")

    # Candidate grids (clip to values seen in data when possible)
    temps = sorted(df["temperature_C"].dropna().unique().tolist())[:6] or [-40, -20, 0, 25]
    concs = sorted(df["concentration_M"].dropna().unique().tolist())[:6] or [0.02, 0.05, 0.10, 0.30]
    solvents = df["solvent"].dropna().unique().tolist()
    promoters = df["promoter"].dropna().unique().tolist()
    stoichs = sorted(df["stoichiometry_ratio"].dropna().unique().tolist())[:5] or [0.66, 1.0, 1.5]

    base = df[(df["donor_id"] == args.donor_id) & (df["acceptor_id"] == args.acceptor_id)].head(1)
    if base.empty:
        base = df.iloc[[0]].copy()
        base["donor_id"]=args.donor_id
        base["acceptor_id"]=args.acceptor_id

    rows = []
    for t in temps:
        for c in concs:
            for s in solvents:
                for p in promoters:
                    for st in stoichs:
                        row = base.copy()
                        row["temperature_C"]=t
                        row["concentration_M"]=c
                        row["solvent"]=s
                        row["promoter"]=p
                        row["stoichiometry_ratio"]=st
                        rows.append(row)

    grid = pd.concat(rows, ignore_index=True)

    # Encode with saved encoder/scaler
    enc: OneHotEncoder = artifacts["encoder"]
    scaler: StandardScaler = artifacts["scaler"]
    X_cat = enc.transform(grid[CATEGORICAL_COLS]).drop(columns=CATEGORICAL_COLS)
    X_num = pd.DataFrame(scaler.transform(grid[NUMERIC_COLS]), columns=NUMERIC_COLS, index=grid.index)
    Xg = pd.concat([X_num, X_cat], axis=1)

    grid["pred_alpha"] = model_alpha.predict(Xg)
    grid["pred_yield"] = model_yield.predict(Xg)

    # Example scoring: target high beta (i.e., low alpha) and decent yield weight
    grid["score"] = (100 - grid["pred_alpha"]) + 0.2 * grid["pred_yield"]

    best = grid.sort_values("score", ascending=False).head(10)
    print(best[["donor_id","acceptor_id","solvent","promoter","temperature_C","concentration_M","stoichiometry_ratio","pred_alpha","pred_yield","score"]])

if __name__ == "__main__":
    main()
