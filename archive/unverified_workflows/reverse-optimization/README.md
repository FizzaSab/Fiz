# Reverse (Inverse) Optimization of Glycosylation Conditions

This module implements **reverse prediction (inverse screening)** for glycosylation reactions.

Given:
- a trained machine-learning model (external `.pkl`)
- a fixed donor–acceptor pair
- fixed environmental descriptors (RRV, Aka)

the algorithm samples chemically reasonable reaction conditions
(solvent, promoter, temperature, concentration, stoichiometry)
and ranks them to identify:

- **Maximum α-selectivity**
- **Minimum α-selectivity**
- **Maximum Environmental Factor Impact (EFI)**

## Scientific motivation

Unlike forward prediction, reverse optimization removes the need for
extensive experimental screening by directly proposing conditions
that optimize stereoselectivity and yield under realistic constraints.

This workflow supports the methodology described in the accompanying
manuscript on bidirectional machine-learning–assisted glycosylation.

## Usage

```bash
python src/inverse_optimize.py \
  --bundle path/to/trained_model.pkl \
  --data path/to/experimental_data.csv \
  --rrv 5000 \
  --aka 5.76 \
  --n-candidates 20000 \
  --topk 5
```

## Notes

- Trained models (`.pkl`) and experimental datasets are **not included**
  in this repository and must be supplied externally.
- This design ensures reproducibility while protecting unpublished data.
