# Glycosylation reaction prediction and condition optimization

**Related manuscript:** *Decoding the Multidimensional Complexity of Glycosylation Reactions via Machine Learning* (JACS manuscript ja-2026-034613).

This repository provides the original uploaded research data, prediction exports, visualizations, and a provenance review for the bidirectional glycosylation machine-learning study. **Its present contents do not constitute an independently verified, end-to-end reproduction of all manuscript results.** No additional measurements, predicted values, model scores, or EFI calibration coefficients have been invented during repository cleanup.

## Scientific workflow in the revised manuscript

1. **Descriptors:** glycosylating agent, alcohol, RRV, Aka, stereochemical and structural variables, and environmental conditions such as temperature, solvent, concentration, stoichiometry, and promoter.
2. **Forward ML prediction:** predict α/β stereoselectivity and yield for specified molecular and reaction conditions.
3. **Reverse condition selection:** hold the glycosylating agent/alcohol pair fixed and evaluate conditions to identify high- and low-α-selectivity options, which are then tested experimentally.
4. **Environmental Factor Impact (EFI):** a post-prediction, model-derived index for describing and ranking condition-dependent behavior. **It is not the same as a supervised binary EFI label classifier.**
5. **Validation:** keep training/fitting, held-out, external and prospective experimental evaluations separate. Do not present fitted-data predictions as unseen test performance.

This summary follows the revised manuscript and reviewer responses; it is **not** a claim that the exact model implementations have all been recovered in this repository.

## Repository map

| Location | What is actually present |
| --- | --- |
| `cleaned_glycosylation_dataset.csv` | Original uploaded glycosylation dataset (801 CSV data rows); retained unmodified |
| `filtered_feature_data/` | Original feature export |
| `predicted_alpha_ratios_out_of_sample.csv` | Original 169-row alpha-prediction export; record-level matching to other data has not been verified |
| `hybrid/` | Original hybrid feature-importance export; not a complete trained-model release |
| `*.html`, image directories | Original exported plots and analysis artifacts, **not modified or regenerated** |
| `archive/unverified_workflows/glyc-ml/` | Byte-identical original experimental scripts and data, archived due to incompatible EFI-classifier descriptions and unresolved preprocessing/split issues |
| `archive/unverified_workflows/reverse-optimization/` | Byte-identical original scripts, archived because the fallback yield and EFI refitting cannot be established as the final published reverse-mode method |
| `review/` | Specific discrepancies, original Git-blob inventory, and a read-only structural/syntax check |

The previous README referred to three executable notebooks (`01_feature_importance.ipynb`, `02_modeling_y1_y2.ipynb`, `03_inverse_design.ipynb`) that **are not in this repository snapshot**. These instructions have been removed rather than inventing notebooks.

## Start here

```bash
python review/verify_repository.py
```

This check uses only the Python standard library. It reports file presence, CSV row counts, and Python syntax, **not predictive accuracy or manuscript reproducibility**.

## Source provenance and limitations

- Original research artifacts and all figures have been left unchanged. Archived source/data use exactly their pre-cleanup Git blobs; their previous locations are preserved in the backup branch `reviewer-ready-original-code`.
- In the archived `glyc-ml/` scripts, the so-called random split is a contiguous row-order split. Do not describe it as the verified publication split.
- The archived reverse optimization substitutes a yield of 50% if no fitted yield predictor is found. **This is not a measured yield or a verified prediction and must not be used as such.**
- The archived EFI classifier is distinct from the manuscript's calibrated post-prediction EFI index.
- The 190 rows in the archived external dataset must **not** be automatically paired with the 169 rows in the alpha-prediction CSV.
- The authoritative original model object, final model weights/encoders, exact EFI coefficients and reverse-mode implementation, and full experimental row-ID mappings must be verified before releasing an executable reproduction of the published analyses.
- No accuracy metrics were recomputed during the cleanup. Refer to the manuscript and Supporting Information for the reported numerical results.

See [review/AUDIT.md](review/AUDIT.md) for code-specific findings and [review/ORIGINAL_BLOB_INVENTORY.csv](review/ORIGINAL_BLOB_INVENTORY.csv) for the original source blob IDs.

**Reproducibility policy:** never fill missing parts with placeholder models, default yield values, synthetic observations, silently changed encodings or fitted values selected merely to match reported numbers.
