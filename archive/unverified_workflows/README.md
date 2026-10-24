# Earlier computational workflows

This directory retains earlier exploratory code and related data used during development of the glycosylation modeling workflow. These files remain available for methodological reference and comparison with the final manuscript.

## Contents

- **`glyc-ml/`** — Earlier feature-processing, regression, and EFI-label classification experiments. The binary EFI-label task differs from the post-prediction EFI index reported in the manuscript. Its dataset splitting and input-schema assumptions also require separate interpretation.
- **`reverse-optimization/`** — Earlier condition-search experiments. The script includes a fallback constant yield and a separately fitted EFI approximation; these are not presented as the final validated bidirectional implementation.

For analysis of these differences, see [Implementation and data notes](../../review/AUDIT.md).

The original files remain unchanged within this directory. The previous directory layout is preserved on the `reviewer-ready-original-code` branch.
