# Implementation and data notes

These notes document the organization and interpretation of computational files associated with *Decoding the Multidimensional Complexity of Glycosylation Reactions via Machine Learning*.

## Repository organization

The main repository contains the original reaction datasets, exported predictions, figures, and model-analysis files. Earlier exploratory scripts are retained in `archive/unverified_workflows/` to distinguish them from the final bidirectional model described in the manuscript. A copy of the previous repository structure is available on the `reviewer-ready-original-code` branch.

Original plotted figures, HTML visualizations, reaction observations, and exported prediction values have not been changed in this reorganization. The original file identifiers are listed in [ORIGINAL_BLOB_INVENTORY.csv](ORIGINAL_BLOB_INVENTORY.csv).

## Interpretation of individual scripts

**EFI formulation.** The EFI index discussed in the manuscript is calculated using model-predicted outcomes and environmental information. The earlier `glyc-ml/` workflow includes a supervised binary `EFI_label` classification formulation, which is a different task. It is therefore kept as an exploratory implementation rather than used to reproduce the reported EFI index.

**Reverse condition optimization.** The earlier `reverse-optimization/src/inverse_optimize.py` implementation can substitute a fixed 50% yield when a fitted yield predictor is unavailable and includes an independently fitted EFI approximation. This behavior does not establish the final reverse-prediction method reported in the manuscript, so the script is retained for reference only.

**Dataset splitting.** The split generator in `glyc-ml/src/prepare_features.py` uses row order for its 90:10 partition even though the output is named `random`. This partition should not be interpreted as evidence of the held-out partition used for the manuscript.

**Data schema.** The archived training scripts and source datasets contain differences in expected column names and encoding. The final model's preprocessing settings and feature order are needed to reproduce its predictions.

**External-prediction matching.** The archived external dataset has 190 records, whereas `predicted_alpha_ratios_out_of_sample.csv` contains 169 prediction records. These files represent differently sized sets and should be matched only through verified reaction identifiers, not row position.

**Hybrid-model weighting.** A separate combined script includes an assumed 0.50 RF/XGBoost weight and a placeholder `HybridRF_XGB` class. These values are not sufficient to establish the original fitted hybrid model. The original trained model and prediction method take precedence.

## Reproduction requirements

Full numerical reproduction of the manuscript requires the corresponding original trained model objects, feature encoders, partition assignments, EFI coefficients/calibration, reverse-search settings, and record identifiers linking experimental outcomes to predictions.

The files currently supplied here support inspection of the datasets, exported analyses, and source-code history. The `verify_repository.py` utility checks structure and syntax only; it does not estimate R² or RMSE, validate EFI numerically, or rerun the experimental analysis.

Model-performance and experimental-validation results should be cited from the manuscript and Supporting Information rather than inferred from exploratory scripts or unmatched datasets.
