# Archived, unverified historical workflows

These are the **original scripts and data**, moved here without modifying their Git blobs. This archive prevents experimental or reconstructed workflows from being mistaken for the final, validated bidirectional ML + EFI model.

- `glyc-ml/`: its README frames EFI as a **binary classifier**; its "random" split generator uses row order and the available input schema does not validate its claimed end-to-end training recipe.
- `reverse-optimization/`: substitutes **50% yield** if a trained yield model is missing and fits an EFI proxy; neither behavior is confirmed as the original final reverse-mode implementation.

The original locations and every original figure can be found on the backup branch `reviewer-ready-original-code`. Do not report these archived scripts as reproduced manuscript results. See [review/AUDIT.md](../../review/AUDIT.md).
