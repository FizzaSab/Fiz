import argparse, os, joblib, glob
import numpy as np, pandas as pd
from utils import load_data, load_json, bootstrap_ci
from config import *
from metrics import regression_metrics, classification_metrics
from category_encoders.one_hot import OneHotEncoder
from sklearn.preprocessing import StandardScaler

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/processed/gly_dataset.cleaned.csv")
    ap.add_argument("--split", required=True)
    ap.add_argument("--tasks", nargs="+", default=["alpha","yield","efi"])
    ap.add_argument("--with-ci", dest="with_ci", action="store_true")
    ap.add_argument("--models_dir", default="models")
    args = ap.parse_args()

    df = load_data(args.data)
    split = load_json(f"data/splits/{args.split}.json")["folds"][0]
    te_ids = set(split["test_ids"])
    te_mask = df["row_id"].isin(te_ids)

    artifacts = joblib.load(f"{args.models_dir}/artifacts.pkl")

    # Rebuild features for test set using saved encoder/scaler:
    X_cat_raw = df[CATEGORICAL_COLS]
    enc: OneHotEncoder = artifacts["encoder"]
    X_cat = enc.transform(X_cat_raw).drop(columns=CATEGORICAL_COLS)

    X_num_raw = df[NUMERIC_COLS]
    scaler: StandardScaler = artifacts["scaler"]
    X_num = pd.DataFrame(scaler.transform(X_num_raw), columns=NUMERIC_COLS, index=df.index)

    X = pd.concat([X_num, X_cat], axis=1)
    Xte = X[te_mask]

    # Truth
    yte_alpha = df.loc[te_mask, "alpha_ratio_pct"]
    yte_yield = df.loc[te_mask, "yield_pct"]
    yte_efi   = df.loc[te_mask, CLASSIFICATION_TARGET] if "efi" in args.tasks else None

    model_files = glob.glob(f"{args.models_dir}/*.pkl")
    for fname in model_files:
        if fname.endswith("artifacts.pkl"):
            continue
        model = joblib.load(fname)
        if fname.endswith("_alpha.pkl") and "alpha" in args.tasks:
            yp = model.predict(Xte)
            m = regression_metrics(yte_alpha, yp)
            print(os.path.basename(fname), m)
            if args.with_ci:
                # Report CI on R2 via bootstrap of residual means (simple proxy)
                # Here we just CI the RMSE for illustration
                _, low, high = bootstrap_ci((yte_alpha - yp)**2, alpha=0.05)
                print("  RMSE^2 95% CI:", (low, high))
        if fname.endswith("_yield.pkl") and "yield" in args.tasks:
            yp = model.predict(Xte)
            m = regression_metrics(yte_yield, yp)
            print(os.path.basename(fname), m)
            if args.with_ci:
                _, low, high = bootstrap_ci((yte_yield - yp)**2, alpha=0.05)
                print("  RMSE^2 95% CI:", (low, high))
        if fname.endswith("_efi.pkl") and "efi" in args.tasks:
            yp = model.predict(Xte)
            m = classification_metrics(yte_efi, yp)
            print(os.path.basename(fname), m)

if __name__ == "__main__":
    main()
