import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from category_encoders.one_hot import OneHotEncoder

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def make_feature_target_tables(df, numeric_cols, categorical_cols, regression_targets, class_target):
    # Encode categoricals safely
    enc = OneHotEncoder(cols=categorical_cols, use_cat_names=True, handle_unknown="value", handle_missing="value")
    X_cat = enc.fit_transform(df[categorical_cols]).drop(columns=categorical_cols)
    X_num = df[numeric_cols].copy()

    # Simple scaling for numeric features
    scaler = StandardScaler()
    X_num_scaled = pd.DataFrame(scaler.fit_transform(X_num), columns=numeric_cols, index=df.index)

    X = pd.concat([X_num_scaled, X_cat], axis=1)

    y_reg = df[regression_targets].copy()
    y_cls = df[class_target].copy() if class_target in df.columns else None

    artifacts = {"encoder": enc, "scaler": scaler, "feature_names": X.columns.tolist()}
    return X, y_reg, y_cls, artifacts

def save_json(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def bootstrap_ci(values, alpha=0.05, nboot=2000, seed=42):
    rng = np.random.default_rng(seed)
    arr = np.array(values)
    boots = []
    for _ in range(nboot):
        sample = rng.choice(arr, size=len(arr), replace=True)
        boots.append(np.mean(sample))
    low = np.percentile(boots, 100 * (alpha/2))
    high = np.percentile(boots, 100 * (1 - alpha/2))
    return float(np.mean(arr)), float(low), float(high)
