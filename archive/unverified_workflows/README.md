# Exploratory modeling scripts

This directory contains early computational experiments from the development of the glycosylation prediction framework.

The `glyc-ml/` directory covers feature processing, model fitting, and an EFI-label classification experiment. The binary classification formulation is separate from the continuous, post-prediction EFI index presented in the manuscript.

The `reverse-optimization/` directory contains an earlier condition-search implementation. It includes a fallback yield value when a yield predictor is unavailable and a separately fitted EFI approximation. These calculations are not equivalent to the final experimentally evaluated reverse-prediction method.

The files are retained as development-stage material. Their relationship to the manuscript workflow and available data is described in the [methodological notes](../../review/AUDIT.md).
