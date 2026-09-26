# Input Data Structure

The source file expected by Notebook 01 is:

```text
Data/Raw/Original data.xlsx
```

The default worksheet name is `Breast`. The original registry variable names are referenced directly in the cohort-construction and cleaning notebooks because exact mappings are required for reproducibility.

At minimum, the authorized source extract must contain the diagnosis and recurrence date fields and the demographic, clinicopathological, receptor, treatment, and follow-up fields used by the notebooks. The code verifies required columns before analysis and stops with an informative error if they are missing.

The final modelling dataset produced by Notebook 02 contains the following 17 candidate predictors and one binary outcome:

| Type | Variable |
|---|---|
| Continuous | `Age_at_Diagnosis` |
| Continuous | `Tumor_Size_mm` |
| Categorical | `Marital_Status` |
| Categorical | `Nationality` |
| Categorical | `Menopause_Status` |
| Categorical | `Breast_Cancer_Family_History` |
| Categorical | `Primary_Site_Group` |
| Categorical | `Laterality` |
| Categorical | `Histology_Group` |
| Categorical | `Tumor_Grade` |
| Categorical | `Summary_Stage` |
| Categorical | `ER_Status` |
| Categorical | `PR_Status` |
| Categorical | `HER2_Status` |
| Categorical | `Surgery` |
| Categorical | `Chemotherapy` |
| Categorical | `Hormone_Therapy` |
| Outcome | `Five_Year_Recurrence` (No/Yes) |

Unknown registry values are retained as explicit categorical levels where specified in the manuscript. Missing numerical tumour size is imputed inside the corresponding model-training fold.

