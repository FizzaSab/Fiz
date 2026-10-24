# Review of original repository files — 24 October 2026

**Scope:** Research integrity/documentation cleanup, **not** a reproduction of the final manuscript calculations.

## Changes to the manuscript-linked default branch

- Updated the front-page README to describe only files and methods supported by the supplied repository and revised JACS manuscript.
- Relocated the two unsupported/misleading workflows into `archive/unverified_workflows/`, preserving their exact original Git blob SHA values.
- Kept every historical HTML figure, PNG image, experimental dataset, prediction export and top-level results file unchanged.
- Added a read-only verification utility and original-file Git SHA inventory.
- Created backup branch `reviewer-ready-original-code` at the exact pre-cleanup commit for rollback and provenance.

## Findings requiring scientific reconciliation

1. **EFI category mistake:** the original `glyc-ml/README.md` describes supervised classification of a binary `EFI_label`, whereas the revised manuscript defines an EFI index calculated *after* forward predictions and used for condition ranking. The classifier is not presented as the final EFI method.
2. **Unverified reverse optimization:** `reverse-optimization/src/inverse_optimize.py` supplies a constant **50% yield** if the yield predictor is missing and re-fits a RidgeCV-based EFI proxy; neither is established as the final experimental or manuscript workflow.
3. **Split mislabeling:** `glyc-ml/src/prepare_features.py` writes a sequential 90:10 row split while labeling it random. Do not claim this reproduces the original split.
4. **Schema mismatch:** the `glyc-ml/` training instructions and actual source-data columns do not form a verified executable pipeline.
5. **Unmatched cohorts:** the original external CSV has 190 rows and the root prediction file contains 169 records; there is no verified row-level key for matching these by position.
6. **Earlier reconstructed code is not authoritative:** a previously uploaded combined hybrid script explicitly assumed a 0.50 RF/XGBoost weight and supplied a placeholder `HybridRF_XGB` class; do not substitute it for the original trained implementation.
7. **Missing executable provenance:** no final fitted model package, confirmed exact EFI coefficient files, or complete experimental-validation join keys are established by the GitHub snapshot.

## What remains unverified

- Published R², RMSE and external/generalization metrics have **not** been recalculated.
- The originally reported train/test split, categorical encoding and any grouping rules have **not** been proven by code execution.
- Original reverse optimization and calibrated EFI figures cannot be regenerated without their authoritative code/models.
- Historical plots are retained but are not individually certified as regenerated.

## Reviewer interpretation

This repo provides authentic uploaded artifacts, a file inventory and openly documented limitations. For method-level reproduction, locate and verify the original fitted model, full preprocessing and validation metadata, EFI scripts and experimental data mapping first. Do not fabricate or extrapolate missing items.

The archived scripts are intentionally *not* advertised as reproducing the JACS figures. They are retained byte-for-byte for traceability.
