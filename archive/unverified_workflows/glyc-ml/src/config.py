SEED = 42
N_OUTER_FOLDS = 5
N_INNER_FOLDS = 5

REGRESSION_TARGETS = ["alpha_ratio_pct", "yield_pct"]
CLASSIFICATION_TARGET = "EFI_label"  # 'high' or 'low'

CATEGORICAL_COLS = [
    "donor_id","acceptor_id","solvent","promoter"
    # add donor/acceptor structural categorical columns here:
    # "donor_C2_func","donor_C6_func","acceptor_site","acceptor_type", ...
]

NUMERIC_COLS = [
    "RRV","Aka","temperature_C","concentration_M","stoichiometry_ratio","polarity_index"
    # add any other numeric structural descriptors here
]

# Hyperparam grids (inner CV randomized search) -- placeholders for future extension
RF_GRID = {
    "n_estimators": (200, 1000),
    "max_depth": (3, None),
    "max_features": ["sqrt", "log2"]
}

XGB_GRID = {
    "n_estimators": (400, 2000),
    "learning_rate": (1e-3, 0.3),
    "max_depth": (3, 10),
    "subsample": (0.6, 1.0),
    "colsample_bytree": (0.6, 1.0),
    "reg_alpha": (0.0, 5.0),
    "reg_lambda": (0.0, 5.0)
}
