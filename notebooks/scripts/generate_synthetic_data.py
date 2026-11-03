"""Generate a fully synthetic dataset for repository smoke testing.

The output follows the final modelling schema but contains no real patient
records and is not intended to reproduce the manuscript results.
"""

from pathlib import Path

import numpy as np
import pandas as pd


SEED = 2026
N_RECORDS = 300
OUTPUT_FILE = (
    Path(__file__).resolve().parents[1]
    / "Data"
    / "Synthetic"
    / "synthetic_model_data.csv"
)


def sample(rng, values, probabilities, size=N_RECORDS):
    return rng.choice(values, size=size, p=probabilities)


def main():
    rng = np.random.default_rng(SEED)

    age = np.clip(rng.normal(49, 11, N_RECORDS), 22, 84).round(0)
    tumour_size = np.clip(rng.lognormal(np.log(28), 0.55, N_RECORDS), 3, 140).round(1)
    tumour_size[rng.random(N_RECORDS) < 0.12] = np.nan

    data = pd.DataFrame(
        {
            "Age_at_Diagnosis": age,
            "Tumor_Size_mm": tumour_size,
            "Marital_Status": sample(
                rng, ["Married", "Single", "Other", "Unknown"],
                [0.61, 0.24, 0.10, 0.05]
            ),
            "Nationality": sample(
                rng, ["Saudi", "Non-Saudi", "Unknown"], [0.87, 0.11, 0.02]
            ),
            "Menopause_Status": sample(
                rng, ["Premenopausal", "Postmenopausal", "Unknown"],
                [0.46, 0.43, 0.11]
            ),
            "Breast_Cancer_Family_History": sample(
                rng, ["No", "Yes", "Unknown"], [0.78, 0.16, 0.06]
            ),
            "Primary_Site_Group": sample(
                rng,
                ["Upper outer quadrant", "Other specified breast site", "Breast NOS"],
                [0.42, 0.34, 0.24]
            ),
            "Laterality": sample(
                rng, ["Left", "Right", "Unknown"], [0.50, 0.49, 0.01]
            ),
            "Histology_Group": sample(
                rng,
                ["Ductal", "Lobular", "Other", "Unknown"],
                [0.70, 0.11, 0.17, 0.02]
            ),
            "Tumor_Grade": sample(
                rng, ["Grade 1", "Grade 2", "Grade 3", "Unknown"],
                [0.09, 0.25, 0.17, 0.49]
            ),
            "Summary_Stage": sample(
                rng, ["In Situ", "Localized", "Regional", "Distant", "Unknown"],
                [0.08, 0.30, 0.43, 0.17, 0.02]
            ),
            "ER_Status": sample(
                rng, ["Negative", "Positive", "Unknown"], [0.13, 0.31, 0.56]
            ),
            "PR_Status": sample(
                rng, ["Negative", "Positive", "Unknown"], [0.18, 0.26, 0.56]
            ),
            "HER2_Status": sample(
                rng, ["Negative", "Positive", "Unknown"], [0.28, 0.13, 0.59]
            ),
            "Surgery": sample(rng, ["No", "Yes"], [0.25, 0.75]),
            "Chemotherapy": sample(rng, ["No", "Yes"], [0.30, 0.70]),
            "Hormone_Therapy": sample(rng, ["No", "Yes"], [0.56, 0.44]),
        }
    )

    # Create a synthetic outcome with enough events for a fast smoke test.
    score = np.full(N_RECORDS, -2.55)
    score += np.where(data["Summary_Stage"].eq("Regional"), 0.55, 0.0)
    score += np.where(data["Summary_Stage"].eq("Distant"), 1.05, 0.0)
    score += np.where(data["Tumor_Grade"].eq("Grade 3"), 0.35, 0.0)
    score += np.where(data["ER_Status"].eq("Negative"), 0.30, 0.0)
    score += np.where(data["Age_at_Diagnosis"].lt(40), 0.25, 0.0)
    probability = 1.0 / (1.0 + np.exp(-score))
    outcome = rng.binomial(1, probability)

    # Guarantee both classes and at least 20 events for three-fold validation.
    if outcome.sum() < 20:
        event_indices = np.argsort(probability)[-20:]
        outcome[event_indices] = 1

    data["Five_Year_Recurrence"] = np.where(outcome == 1, "Yes", "No")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved {len(data):,} fully synthetic records to {OUTPUT_FILE}")
    print(f"Synthetic events: {(data['Five_Year_Recurrence'] == 'Yes').sum():,}")


if __name__ == "__main__":
    main()
