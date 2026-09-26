# Breast Cancer Recurrence Prediction: Reproducible Analysis Code

This repository contains the analysis notebooks for the manuscript **“Development and Internal Validation of Machine Learning Models for Breast Cancer Recurrence Using Real-World Clinical Data from Saudi Arabia.”**

The code constructs the five-year recurrence cohort, cleans and recodes candidate predictors, and performs the repeated nested cross-validation, model evaluation, interpretation, ablation, and sensitivity analyses reported in the manuscript.

## Repository contents

```text
notebooks/
  01_construct_five_year_cohort.ipynb
  02_clean_and_recode_predictors.ipynb
  03_descriptive_analysis.ipynb
  04_model_development_and_validation.ipynb
docs/
  input_data_schema.md
Data/
  Raw/          # restricted source data; not included
  Processed/    # generated locally; not included
Results/        # generated locally; not included
```

## Data availability

Patient-level registry data are not included because they contain sensitive clinical information and are subject to institutional and ethical restrictions. Researchers with an approved data-use pathway may contact the corresponding author and the data-holding institution regarding access. The repository provides the complete analysis code, expected input structure, model configurations, random seed, and software environment needed to reproduce the workflow when an authorized dataset is available.

## Software environment

The analysis was conducted with Python 3.9.7. Install the recorded package versions with:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the analysis

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

## Privacy note

Do not commit raw or processed patient-level data, checkpoint predictions, spreadsheets, or generated results containing record-level information. The supplied `.gitignore` excludes these directories by default.

## License

The analysis code is released under the MIT License. The license does not apply to the underlying clinical data.

## Citation

Please use the citation information supplied in `CITATION.cff`. A version-specific DOI will be added after the GitHub release is archived in Zenodo.
