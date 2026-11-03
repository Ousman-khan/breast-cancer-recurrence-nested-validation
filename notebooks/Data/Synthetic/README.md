# Synthetic demonstration data

`synthetic_model_data.csv` contains 300 fully artificial records generated with
random seed 2026. It follows the final modelling schema so that the public smoke
test can exercise data loading, preprocessing, model fitting, held-out
prediction, and metric calculation.

No row is derived from, matched to, or intended to represent a real patient.
The synthetic event rate and model-performance estimates have no clinical
interpretation and do not reproduce the manuscript results.

Regenerate the file from the repository root with:

```bash
python scripts/generate_synthetic_data.py
```
