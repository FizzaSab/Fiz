# Methodological notes

The computational files accompanying our glycosylation study include datasets, prediction exports, figures, and scripts from different stages of model development. The final research framework focuses on forward prediction of α-selectivity and yield, reverse exploration of reaction conditions, and interpretation using the Environmental Factor Impact (EFI) index.

## EFI and reverse prediction

In the manuscript, EFI is a model-derived index calculated from predicted outcomes and reaction-environment information. An earlier exploratory implementation under `archive/unverified_workflows/glyc-ml/` instead uses a binary `EFI_label` classification task. This is a separate modeling exercise and does not represent the EFI calculation used in the manuscript.

The earlier `archive/unverified_workflows/reverse-optimization/src/inverse_optimize.py` script uses a constant yield of 50% if a fitted yield predictor is unavailable and estimates a separate EFI approximation. These fallback calculations are not experimental measurements and are not used as evidence of the final reverse-prediction results.

## Dataset and model correspondence

The archived `glyc-ml/src/prepare_features.py` script partitions observations in row order, despite using the filename `random` for its split output. Its data encoding and expected feature names also differ from some of the available datasets. Consequently, that script alone does not establish the train/test partitions or exact preprocessing applied in the manuscript.

The external dataset kept with the exploratory scripts contains 190 rows, while the root-level `predicted_alpha_ratios_out_of_sample.csv` contains 169 records. These files cannot be matched by row position without corresponding reaction identifiers.

A separate combined hybrid-model script from the development materials specifies an assumed 50:50 Random Forest/XGBoost weighting and includes an incomplete placeholder class. That assumption is not sufficient to determine the weighting or prediction method of the fitted model used for the reported results.

## Reproducibility

Complete reproduction of the final analysis depends on the corresponding trained model objects, feature encoding and ordering, validation splits, EFI coefficients, reverse-search settings, and observation-level links between predictions and experiments.

The files in this repository allow inspection of the available data and outputs, but do not by themselves establish all of those elements. The `verify_repository.py` utility checks file structure, CSV record counts, and Python syntax; it is not a model-validation or performance-reproduction script.

The manuscript and Supporting Information provide the scientific definitions, reported model performance, EFI formulation, and experimental-validation results. Earlier exploratory scripts are kept separately to avoid conflating development-stage calculations with the reported study.
