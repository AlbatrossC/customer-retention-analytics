import argparse
import json
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from model_v2_runtime import load_calibrators, load_v2, predict_raw_proba, prepare_x


SCRIPT_DIR = Path(__file__).resolve().parent
ARTIFACT_DIR = SCRIPT_DIR / "artifacts"
DATA_PATH = SCRIPT_DIR.parents[1] / "data" / "customers_model_1_v2.csv"
RANDOM_SEED = 42


def split_test(df):
    customer_labels = df.groupby("customer_id")["next_month_churn"].max().reset_index()
    _, holdout_customers = train_test_split(
        customer_labels,
        train_size=0.70,
        random_state=RANDOM_SEED,
        stratify=customer_labels["next_month_churn"],
    )
    _, test_customers = train_test_split(
        holdout_customers,
        train_size=0.50,
        random_state=RANDOM_SEED,
        stratify=holdout_customers["next_month_churn"],
    )
    return df[df["customer_id"].isin(set(test_customers["customer_id"]))].copy()


def summarize(name, probabilities):
    rounded = np.round(probabilities * 100, 2)
    counts = Counter(rounded)
    percentiles = np.percentile(rounded, [0, 10, 25, 50, 75, 90, 95, 99, 100])
    print(f"\n{name}")
    print(f"rows: {len(probabilities)}")
    print(f"unique rounded %: {len(counts)}")
    print(f"most common rounded %: {counts.most_common(10)}")
    print(f"percentiles %: {[round(float(value), 2) for value in percentiles]}")


def main():
    parser = argparse.ArgumentParser(description="Diagnose Model 1 v2 raw vs calibrated probabilities.")
    parser.add_argument("--data", default=str(DATA_PATH), help="V2 training CSV.")
    args = parser.parse_args()

    metadata = json.loads((ARTIFACT_DIR / "model_metadata_v2.json").read_text(encoding="utf-8"))
    calibrators = load_calibrators(ARTIFACT_DIR)
    models = load_v2(ARTIFACT_DIR, metadata)
    print(f"Loaded {len(models)} ensemble member(s)")

    df = pd.read_csv(args.data)
    test_df = split_test(df)
    x_test = prepare_x(test_df, metadata)
    raw = predict_raw_proba(models, x_test)
    sigmoid = calibrators["sigmoid"].predict_proba(raw.reshape(-1, 1))[:, 1]
    isotonic = calibrators["isotonic"].predict(raw)

    summarize("raw", raw)
    summarize("sigmoid", sigmoid)
    summarize("isotonic", isotonic)
    print(f"\nselected probability mode: {metadata['probability_mode']}")


if __name__ == "__main__":
    main()

