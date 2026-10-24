# Glycosylation ML (RRV/Aka + environment → α/β, yield, EFI)

This repository contains code to reproduce the results and figures for our manuscript on predicting stereoselective glycosylations with mechanistically informed features.

## What's here
- **Regression**: predict α-ratio (%) and yield (%) from pre-experimental descriptors (RRV, Aka, donor/acceptor structure, solvent class/polarity, temperature, concentration, stoichiometry, promoter).
- **Classification**: predict **EFI** as **high vs low efficiency**. EFI is an **outcome label only** (not a feature).
- **Generalization tests**: random, donor-holdout, acceptor-holdout, scaffold, temporal.
- **Reproducibility**: seeded splits stored in `data/splits/*.json`.

## Quickstart

```bash
conda env create -f environment.yml
conda activate glyc-ml

# 1) Prepare features and splits
python src/prepare_features.py --data data/processed/gly_dataset.csv --out data/processed/ --make-splits

# 2) Train models (α, yield regressors + EFI classifier) on donor-holdout (replace with desired split)
python src/train.py --split random --models rf xgb --tasks alpha yield efi

# 3) Evaluate with 95% CIs and save figures
python src/evaluate.py --split random --tasks alpha yield efi --with-ci

# 4) Simple inverse search example
python src/optimize_conditions.py --donor_id D123 --acceptor_id A456
```

## Data format

`data/processed/gly_dataset.csv` must contain:

- **Inputs (pre-experimental)**:  
  - `RRV`, `Aka` (numeric)  
  - `donor_id`, `acceptor_id` (categorical)  
  - `donor_features_*`, `acceptor_features_*` (categorical/numeric; e.g., positions, PGs)  
  - `solvent`, `promoter` (categorical); `polarity_index` (numeric if available)  
  - `temperature_C`, `concentration_M`, `stoichiometry_ratio` (numeric)
- **Targets**:  
  - `alpha_ratio_pct`, `yield_pct` (numeric)  
  - `EFI_label` in {`high`, `low`}  (**binary label; not used as feature**)

## Reproducibility
- All splits are precomputed and stored under `data/splits/*.json`.
- Seeds are fixed within each outer CV fold; inner CV tunes hyperparameters.

## Why EFI is a **label** (not a feature)
To avoid leakage flagged by reviewers, EFI summarises overall reaction efficiency and is predicted in a **separate classification task**. α and yield regressions never use EFI as input.

## License
MIT
