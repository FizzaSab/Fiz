# Decoding the Multidimensional Complexity of Glycosylation Reactions via Machine Learning

**Bidirectional prediction of glycosylation stereoselectivity, reaction yield, and conditions**

Precise control of glycosylation stereoselectivity remains challenging because reaction outcomes are influenced by the structures and reactivities of the reacting partners and by the reaction environment. Solvent, temperature, promoter, concentration, and stoichiometry can affect the relative formation of α- and β-glycosides, often through interacting effects.

In our work, we use machine learning to study these relationships and guide reaction-condition selection. The framework combines chemical and environmental descriptors to predict **α-selectivity and reaction yield**. The hybrid modeling approach brings together Random Forest and XGBoost analyses.

The framework is **bidirectional**. In forward prediction, the glycosylating agent, alcohol, and specified reaction conditions are used to estimate the reaction outcome. In reverse prediction, we examine reaction conditions for a fixed glycosylating agent–alcohol pair to identify conditions associated with higher or lower α-selectivity. These predictions are considered alongside experimental measurements.

We also developed the **Environmental Factor Impact (EFI) index** to examine the combined influence of reaction conditions on glycosylation outcomes. EFI provides a quantitative basis for comparing reaction environments and studying regions associated with changes in stereochemical preference.

## Research approach

**Reaction data → Chemical and environmental descriptors → Hybrid machine-learning model → Forward prediction and reverse condition selection → EFI analysis → Experimental validation**

The input descriptors include structural and stereochemical characteristics of the reacting partners, relative reactivity values (RRV), acceptor reactivity (Aka), temperature, solvent, concentration, stoichiometry, and promoter. Model evaluation and feature-attribution analyses provide additional insight into the relationships captured by the models.

## Data and results

| File or directory | Contents |
| --- | --- |
| `cleaned_glycosylation_dataset.csv` | Glycosylation reaction dataset |
| `filtered_feature_data/` | Feature dataset |
| `predicted_alpha_ratios_out_of_sample.csv` | Exported α-selectivity predictions |
| `hybrid/` | Hybrid-model feature-importance results |
| `Hybrid_train-test-2.html` | Training and evaluation analysis |
| `Model_prfmnc-a-ratio.html`, `Model_prfmnc_yield.html` | Model-performance comparisons |
| `a-ratio_ML-training-test-plots.html`, `Yield-ML-training-test-plots.html` | Prediction and evaluation figures |
| `SHAP-2.html`, `Feature_attribution.html` | Feature-attribution analyses |
| `Reaction_condition_prediction-2.html` | Reaction-condition prediction analysis |
| `Features/`, `a-ratio/`, `Yield/` | Research figures |
| `code/` | Scripts for inspecting the provided reaction data and prediction exports |

The additional HTML files contain model analyses and graphical outputs.

## Code and methods

The `code/` directory contains small utilities for examining the dataset columns, reaction counts, and saved prediction values. The computational framework, EFI formulation, model evaluation, and experimental comparisons are described in the accompanying research work and Supporting Information.
