#!/usr/bin/env python3
"""
Inverse (Reverse) Optimization of Glycosylation Conditions

Samples chemically reasonable reaction environments and ranks
conditions that maximize or minimize α-selectivity or maximize EFI.
"""

import argparse
import numpy as np
import pandas as pd
import joblib

from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import RidgeCV

EPS = 1e-9

ALLOWED_SOLVENTS = {
    "DCM","DCM/ACN","DCM/DMF","DCM/p-Dioxane","THF","Toluene","ACN"
}
ALLOWED_PROMOTERS = {
    "NIS_TfOH","TMSOTf","TfOH","Tf2O","IDCP"
}

def promoter_from_c1(c1):
    c1 = (c1 or "").lower()
    if "imidate" in c1:
        return "TMSOTf"
    return "NIS_TfOH"

def env_design(df, ohe):
    X_num = np.column_stack([
        np.log1p(df["RRV"]),
        np.log1p(df["Aka"]),
        df["temperature_C"],
        df["temperature_C"]**2,
        np.log1p(df["concentration_M"]),
        df["stoichiometry_ratio"],
    ])
    X_cat = ohe.transform(df[["solvent","promoter"]].fillna("NaN"))
    return np.hstack([X_num, X_cat])

def main(args):
    rng = np.random.default_rng(args.seed)

    bundle = joblib.load(args.bundle)
    alpha_model = bundle["alpha"]
    yield_model = bundle.get("yield")

    raw = pd.read_csv(args.data)
    raw = raw[
        raw["solvent"].isin(ALLOWED_SOLVENTS) &
        raw["promoter"].isin(ALLOWED_PROMOTERS)
    ]

    ohe = OneHotEncoder(handle_unknown="ignore", sparse=False)
    ohe.fit(raw[["solvent","promoter"]])

    def pred_alpha(df):
        return np.clip(alpha_model.predict(df), 0, 100)

    def pred_yield(df):
        if yield_model is None:
            return np.full(len(df), 50.0)
        return np.clip(yield_model.predict(df), 0, 100)

    base = (pred_alpha(raw)/100)*(pred_yield(raw)/100) + EPS
    ridge = RidgeCV(alphas=np.logspace(-4,2,10)).fit(
        env_design(raw, ohe),
        np.log(base)
    )

    k = args.efi_target / np.median(
        base / np.exp(ridge.predict(env_design(raw, ohe)))
    )

    def EFI(df, a, y):
        h = ridge.predict(env_design(df, ohe))
        return k*((a/100)*(y/100)+EPS)/np.exp(h)

    prom = promoter_from_c1(args.c1_mod)
    solvents = raw["solvent"].unique()

    rows = []
    for _ in range(args.n_candidates):
        rows.append({
            "solvent": rng.choice(solvents),
            "promoter": prom,
            "temperature_C": rng.uniform(-40, 0),
            "concentration_M": rng.uniform(0.05, 0.30),
            "stoichiometry_ratio": rng.uniform(0.8, 1.2),
            "RRV": args.rrv,
            "Aka": args.aka,
        })

    df = pd.DataFrame(rows)
    df["alpha_pred"] = pred_alpha(df)
    df["yield_pred"] = pred_yield(df)
    df["EFI"] = EFI(df, df["alpha_pred"], df["yield_pred"])

    df.sort_values("alpha_pred", ascending=False).head(args.topk) \
      .to_csv(args.out, index=False)

    print(f"[OK] Results written to {args.out}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--rrv", type=float, default=5000)
    ap.add_argument("--aka", type=float, default=5.76)
    ap.add_argument("--c1-mod", default="STol")
    ap.add_argument("--efi-target", type=float, default=0.015)
    ap.add_argument("--n-candidates", type=int, default=20000)
    ap.add_argument("--topk", type=int, default=5)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="inverse_results.csv")
    main(ap.parse_args())
