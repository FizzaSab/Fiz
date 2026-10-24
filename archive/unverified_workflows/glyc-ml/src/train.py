import argparse, os, joblib
import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from xgboost import XGBRegressor, XGBClassifier
from utils import load_data, load_json, make_feature_target_tables
from config import *
from metrics import regression_metrics, classification_metrics

def get_model(kind, task):
    if kind == "rf":
        if task == "reg":
            return RandomForestRegressor(random_state=SEED)
        else:
            return RandomForestClassifier(random_state=SEED)
    elif kind == "xgb":
        if task == "reg":
            return XGBRegressor(random_state=SEED, tree_method="hist")
        else:
            return XGBClassifier(random_state=SEED, tree_method="hist", eval_metric="logloss")
    else:
        raise ValueError("Unknown model kind")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data/processed/gly_dataset.cleaned.csv")
    ap.add_argument("--split", required=True, choices=["random","donor_holdout","acceptor_holdout","scaffold","temporal"])
    ap.add_argument("--models", nargs="+", default=["rf","xgb"])
    ap.add_argument("--tasks", nargs="+", default=["alpha","yield","efi"], help="alpha,yield,efi")
    ap.add_argument("--outdir", default="models")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    df = load_data(args.data)

    # Features/targets
    X, y_reg, y_cls, artifacts = make_feature_target_tables(
        df, NUMERIC_COLS, CATEGORICAL_COLS, REGRESSION_TARGETS, CLASSIFICATION_TARGET
    )

    # Load splits (single-fold JSON for simplicity)
    from utils import load_json as _load_json
    split = _load_json(f"data/splits/{args.split}.json")["folds"][0]
    tr_ids = set(split["train_ids"]); te_ids = set(split["test_ids"])

    tr_mask = df["row_id"].isin(tr_ids)
    te_mask = df["row_id"].isin(te_ids)

    Xtr, Xte = X[tr_mask], X[te_mask]
    ytr_reg, yte_reg = y_reg[tr_mask], y_reg[te_mask]
    ytr_cls, yte_cls = (None, None)
    if "efi" in args.tasks:
        ytr_cls = df.loc[tr_mask, CLASSIFICATION_TARGET]
        yte_cls = df.loc[te_mask, CLASSIFICATION_TARGET]

    # Train per task
    results = {}
    for m in args.models:
        if "alpha" in args.tasks:
            model = get_model(m, "reg")
            model.fit(Xtr, ytr_reg["alpha_ratio_pct"])
            yp = model.predict(Xte)
            results[(m,"alpha")] = yp
            joblib.dump(model, f"{args.outdir}/{m}_alpha.pkl")
        if "yield" in args.tasks:
            model = get_model(m, "reg")
            model.fit(Xtr, ytr_reg["yield_pct"])
            yp = model.predict(Xte)
            results[(m,"yield")] = yp
            joblib.dump(model, f"{args.outdir}/{m}_yield.pkl")
        if "efi" in args.tasks:
            model = get_model(m, "cls")
            model.fit(Xtr, ytr_cls)
            yp = model.predict(Xte)
            results[(m,"efi")] = yp
            joblib.dump(model, f"{args.outdir}/{m}_efi.pkl")

    # Save artifacts (encoder/scaler/feature names)
    joblib.dump(artifacts, f"{args.outdir}/artifacts.pkl")

    # Dump quick metrics to console
    for key, preds in results.items():
        mname, task = key
        if task in ("alpha","yield"):
            ytrue = yte_reg["alpha_ratio_pct"] if task == "alpha" else yte_reg["yield_pct"]
            print(mname, task, regression_metrics(ytrue, preds))
        else:
            print(mname, task, classification_metrics(yte_cls, preds))

if __name__ == "__main__":
    main()
