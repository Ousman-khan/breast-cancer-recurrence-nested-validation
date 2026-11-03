# Breast Cancer Recurrence Prediction: Reproducible Analysis Code

This repository contains the analysis notebooks for the manuscript **“Development and Internal Validation of Machine Learning Models for Breast Cancer Recurrence Using Real-World Clinical Data from Saudi Arabia.”**

The code constructs the five-year recurrence cohort, cleans and recodes candidate predictors, and performs the repeated nested cross-validation, model evaluation, interpretation, ablation, and sensitivity analyses reported in the manuscript.

## Repository contents

```text
notebooks/
  00_synthetic_smoke_test.ipynb
  01_construct_five_year_cohort.ipynb
  02_clean_and_recode_predictors.ipynb
  03_descriptive_analysis.ipynb
  04_model_development_and_validation.ipynb
scripts/
  generate_synthetic_data.py
docs/
  input_data_schema.md
Data/
  Synthetic/
    synthetic_model_data.csv
    README.md
  Raw/          # restricted source data; not included
  Processed/    # generated locally; not included
Results/        # generated locally; not included
```

## Data availability

Patient-level registry data are not included because they contain sensitive clinical information and are subject to institutional and ethical restrictions. Researchers with an approved data-use pathway may contact the corresponding author and the data-holding institution regarding access.

A fully synthetic dataset is provided solely to verify data loading, preprocessing, model fitting, and performance-calculation workflows. It contains no real patient records or identifiable information and cannot reproduce the manuscript results.

To protect patient confidentiality, the repository configuration excludes raw and processed clinical data, checkpoint predictions, and record-level outputs from version control.

## Software environment

The analysis was conducted with Python 3.9.7. Install the recorded package versions with:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the analysis

### Synthetic smoke test

To verify the workflow without access to restricted clinical data:

1. Use the supplied `Data/Synthetic/synthetic_model_data.csv`, or regenerate it by running `scripts/generate_synthetic_data.py`.
2. Run `notebooks/00_synthetic_smoke_test.ipynb`.

The smoke test verifies the principal computational steps but does not reproduce the manuscript results.

### Full analysis with authorized data

1. Place the authorized registry extract at `Data/Raw/Original data.xlsx` and confirm that its worksheet and variables match `docs/input_data_schema.md`.
2. Start Jupyter from the repository root or the `notebooks` directory.
3. Run the notebooks in this order:
   - `01_construct_five_year_cohort.ipynb`
   - `02_clean_and_recode_predictors.ipynb`
   - `03_descriptive_analysis.ipynb`
   - `04_model_development_and_validation.ipynb`
4. Generated intermediate data are written to `Data/Processed`; tables, figures, checkpoints, and model results are written to `Results`.

The main modelling notebook uses random seed `2026`. The full repeated nested-validation analysis is computationally intensive and supports checkpoint resumption.

## Validation design

The four candidate models were evaluated using 10 repetitions of nested five-fold stratified cross-validation with four-fold inner tuning. Preprocessing, hyperparameter selection, and threshold selection were performed within the corresponding training data. Final patient-level performance was calculated from averaged held-out predictions, with uncertainty estimated using 2,000 patient-level bootstrap samples.


## License

The analysis code is released under the MIT License. The license does not apply to the underlying clinical data.

## Citation

Please use the citation information supplied in `CITATION.cff`. The archived repository is available through Zenodo at https://doi.org/10.5281/zenodo.22982804.
