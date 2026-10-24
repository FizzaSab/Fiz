# Decoding the Multidimensional Complexity of Glycosylation Reactions via Machine Learning

**Bidirectional prediction and reaction-condition optimization**

**Related manuscript:** *Decoding the Multidimensional Complexity of Glycosylation Reactions via Machine Learning* (JACS manuscript ja-2026-034613).

## Overview

This repository contains the glycosylation reaction datasets, model-analysis exports, figures, and supporting code associated with our study of reaction stereoselectivity and yield. The approach combines structural and reactivity descriptors with reaction-environment information to study how experimental conditions influence glycosylation outcomes.

The bidirectional framework has two complementary functions:

- **Forward prediction:** Given a glycosylating agent, alcohol, and reaction conditions, the model estimates α-selectivity and reaction yield.
- **Reverse condition optimization:** For a specified glycosylating agent/alcohol pair, candidate conditions are evaluated to identify high- and low-α-selectivity regions for subsequent experimental testing.

We also introduce the **Environmental Factor Impact (EFI) index**, a model-derived measure calculated from predicted reaction outcomes and environmental factors. EFI is used to compare condition-dependent behavior and identify regions associated with changes in selectivity. These associations are considered together with experimental evidence; EFI is not treated as direct identification of reaction intermediates.

## Workflow

1. **Data and descriptors.** Curate reaction records and describe the glycosylating agent, alcohol, RRV, Aka, stereochemical features, solvent, temperature, concentration, stoichiometry, and promoter.
2. **Model development.** Train and evaluate regression models for α-selectivity and reaction yield, including the hybrid random-forest/XGBoost approach.
3. **Forward prediction.** Predict outcomes from specified substrates and reaction conditions.
4. **Reverse prediction.** Fix the glycosylating agent/alcohol pair and evaluate candidate conditions to find predicted selectivity extrema.
5. **EFI analysis.** Calculate and interpret the EFI index alongside the predicted outcomes and environmental settings.
6. **Experimental comparison.** Compare selected predicted conditions with measured stereoselectivity and yield, distinguishing model fitting from independent evaluation.

The relevant model results, validation details, and EFI formulation are described in the manuscript and Supporting Information.

## Repository contents

| Path | Contents |
| --- | --- |
| `cleaned_glycosylation_dataset.csv` | Glycosylation reaction data |
| `filtered_feature_data/` | Feature-data export |
| `hybrid/` | Hybrid-model feature-importance results |
| `predicted_alpha_ratios_out_of_sample.csv` | Exported α-selectivity predictions |
| Root-level `*.html` files | Interactive model analyses, performance plots, SHAP, and reaction-condition results |
| Figure folders (`Features/`, `Yield/`, `a-ratio/`, etc.) | Original plots and graphical outputs |
| `archive/unverified_workflows/` | Earlier exploratory implementations, retained separately from the manuscript workflow |
| `review/` | Implementation notes, file inventory, and data-structure checks |

The original figures, analysis exports, and reaction records are retained without modification.

## Code and reproducibility

The repository includes original analysis artifacts and selected source files. Some files document exploratory implementations rather than the final models used for the manuscript. These earlier scripts are retained under `archive/unverified_workflows/` and should not be used as substitutes for the reported final EFI calculation or reverse-optimization procedure.

A simple consistency check can be run with:

```bash
python review/verify_repository.py
```

This check examines file availability, CSV row counts, and Python syntax. It does not retrain the models or reproduce the manuscript's numerical results.

For the reported model performance, dataset definitions, EFI formulation, and experimental validation, refer to the main manuscript and Supporting Information. The complete published workflow should only be rerun with its corresponding original preprocessing settings, trained models, and record-level validation mappings.

Further implementation notes are available in [review/AUDIT.md](review/AUDIT.md).

## Scope

The repository is intended to make the available data, plots, and computational analyses accessible to researchers interested in carbohydrate synthesis and machine-learning-assisted reaction optimization. Reported experimental findings and mechanistic interpretations should be read in the context of the manuscript and its Supporting Information.
