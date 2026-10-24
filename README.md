# Decoding the Multidimensional Complexity of Glycosylation Reactions via Machine Learning

### Bidirectional prediction of glycosylation stereoselectivity and reaction yield

Glycosylation is strongly influenced by the structures and reactivities of the reacting partners, as well as the conditions under which the reaction is carried out. Even small changes in temperature, solvent, promoter, or concentration can lead to different stereochemical outcomes. Our work explores these relationships using machine learning, with the aim of making reaction prediction and condition selection more systematic.

We developed a bidirectional framework that combines chemical descriptors and experimental reaction conditions to predict **α-selectivity** and **reaction yield**. The forward model estimates the outcome of a specified glycosylating agent–alcohol combination under given conditions. In the reverse direction, the model is used to explore conditions for a fixed pair of reacting partners and identify those associated with higher or lower α-selectivity. The resulting predictions are then assessed through experimental comparisons.

An important part of this study is the **Environmental Factor Impact (EFI) index**. EFI brings together predicted reaction outcomes and environmental contributions into a condition-dependent index. It helps us compare reaction environments and examine regions in which the preferred stereochemical outcome changes. The index is intended to support chemical interpretation, not to identify a reaction intermediate or pathway on its own.

## Research workflow

The study follows a connected workflow, from reaction data to experimental evaluation:

**Reaction data and descriptors → Hybrid machine-learning models → Forward prediction → Reverse condition search → EFI analysis → Experimental validation**

The input descriptors cover structural and stereochemical properties of the glycosylating agent and alcohol, their reactivity parameters (RRV and Aka), and reaction conditions such as solvent, temperature, concentration, stoichiometry, and promoter. Random Forest and XGBoost are among the models used in the hybrid prediction framework.

The forward predictions provide estimates of stereoselectivity and yield. For reverse prediction, the reacting partners are held fixed while selected reaction conditions are varied within the investigated chemical space. EFI provides an additional way to examine how these environmental changes relate to predicted outcomes. Experimental results are used to evaluate the condition-dependent selectivity shifts.

## Data, analyses, and figures

| File or directory | Contents |
| --- | --- |
| `cleaned_glycosylation_dataset.csv` | Glycosylation reaction data |
| `filtered_feature_data/` | Feature data |
| `hybrid/` | Hybrid-model feature-importance results |
| `predicted_alpha_ratios_out_of_sample.csv` | Exported α-selectivity predictions |
| `Hybrid_train-test-2.html`, `a-ratio_ML-training-test-plots.html`, `Yield-ML-training-test-plots.html` | Model training and evaluation visualizations |
| `SHAP-2.html`, `Feature_attribution.html` | Feature-attribution analyses |
| `Reaction_condition_prediction-2.html` | Reaction-condition prediction results |
| `Features/`, `a-ratio/`, `Yield/`, and other figure folders | Figures and graphical results |
| `archive/unverified_workflows/` | Earlier exploratory code and associated data |
| `review/` | Methodological notes, source-file inventory, and structural checks |

Additional HTML reports in the repository contain the corresponding model-performance and prediction visualizations.

## Code availability and reproducibility

This repository brings together the available research data, analysis outputs, figures, and selected computational scripts. The earlier scripts in `archive/unverified_workflows/` document development-stage experiments; they are distinct from the final EFI formulation and reverse-condition procedure described in the manuscript.

Reproduction of the complete numerical workflow requires the matching fitted models, preprocessing and encoding settings, EFI calibration, and the identifiers connecting individual predictions with experimental observations. The exported results and figures are provided here, while the model-validation details, EFI equations, and experimental analyses are documented in the manuscript and Supporting Information.

Further information about the available implementations and dataset relationships is included in the [methodological notes](review/AUDIT.md).

## Manuscript

*Decoding the Multidimensional Complexity of Glycosylation Reactions via Machine Learning*  
JACS manuscript **ja-2026-034613**.
