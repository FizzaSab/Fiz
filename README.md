**Decoding the Multi-Dimensional Complexity of Glycosylation Reaction via Machine Learning**

GlycoEnv

Machine-learning analysis and inverse design of glycosylation stereoselectivity

**What this project does**

This repository contains the Python code and Jupyter notebooks used to analyze glycosylation reactions using machine learning.
The models predict α-selectivity (α-ratio) and reaction yield from glycosylating agent/alcohol structure and reaction conditions, and are further used for inverse design to identify reaction conditions that maximize or minimize α-selectivity for a fixed glycosylating agent-alcohol pair.

The goal is to quantitatively understand how environmental parameters (solvent, temperature, promoter, concentration, stoichiometry, RRV, Aka) influence glycosylation outcomes and to enable data-driven condition optimization.

Repository structure

01_feature_importance.ipynb-
Calculates feature-importance scores to identify which structural and environmental variables most strongly affect α-ratio and yield.

02_modeling_y1_y2.ipynb-
Trains and evaluates multiple machine-learning models (Random Forest, Gradient Boosting, XGBoost, CatBoost, SVR, AdaBoost, Linear, Ridge, Lasso, Decision Tree) for:

y1: α-ratio

y2: reaction yield

Performance is assessed using RMSE, MAE, R², Spearman correlation, and normalized metrics.

03_inverse_design.ipynb
Uses trained surrogate models to recommend experimentally realistic reaction conditions that maximize or minimize α-selectivity while keeping reactivity descriptors (RRV, Aka) fixed.

**Environmental Factor Impact (EFI)**

The Environmental Factor Impact (EFI) index integrates predicted α-ratio and yield with environmental parameters into a single quantitative descriptor.
EFI is used to compare reaction efficiency across different conditions and to connect small changes in reaction environment with shifts in stereoselectivity.

Data and preprocessing

Categorical variables are one-hot encoded.

α-ratio and yield are treated as continuous targets.

Failed reactions are handled consistently during preprocessing (see notebooks for details).

All preprocessing steps are explicitly implemented in the notebooks for transparency.

Installation and reproducibility

Python 3.10

Core packages: numpy, pandas, scipy, scikit-learn, matplotlib, seaborn

Optional: xgboost, catboost

A fixed random seed (random_state = 42) is used throughout.
Package versions can be exported via pip freeze for exact reproducibility.

**Inverse design philosophy**

Inverse design does not extrapolate beyond chemistry represented in the dataset.
Candidate reaction conditions are sampled from experimentally observed ranges and combinations, ensuring that suggested conditions remain chemically plausible.

**Code availability**

Analyses were performed in Python.

Source code: https://github.com/FizzaSab/Fiz

Step-by-step tutorials: https://github.com/FizzaSab/Fizza_tutorial

Intended audience

This repository is written for organic chemists and reviewers.
No prior machine-learning expertise is required to run the notebooks or interpret the results.
