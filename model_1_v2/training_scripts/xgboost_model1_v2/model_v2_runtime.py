"""Shared loading and scoring for the Model 1 v2 model.

Training seed-bags the winning XGBoost config: the same configuration is fitted
under several random seeds and their probabilities are averaged. Averaging away
the per-seed variance is worth a few thousandths of ROC-AUC and, more usefully,
stops the reported number from moving when the seed changes.

The first member is always saved as ``xgboost_model_v2.json``, so any caller
written against the old single-file layout still loads a working model. Callers
that go through ``load_v2`` get every member and reproduce the exact
probabilities the metrics were measured on.
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier

PRIMARY_MODEL_FILE = "xgboost_model_v2.json"
CALIBRATOR_FILE = "calibrator_v2.joblib"
METADATA_FILE = "model_metadata_v2.json"


def model_member_files(metadata):
    """Model filenames for this artifact set, primary member first."""
    members = list(metadata.get("ensemble_members") or [])
    return members or [PRIMARY_MODEL_FILE]


def load_v2(artifact_dir, metadata):
    """Load every ensemble member. Missing members are skipped, not fatal."""
    artifact_dir = Path(artifact_dir)
    models = []
    for filename in model_member_files(metadata):
        path = artifact_dir / filename
        if not path.exists():
            continue
        model = XGBClassifier()
        model.load_model(path)
        models.append(model)
    if not models:
        raise FileNotFoundError(f"No Model 1 v2 model files found in {artifact_dir}")
    return models


def load_calibrators(artifact_dir):
    return joblib.load(Path(artifact_dir) / CALIBRATOR_FILE)


def prepare_x(df, metadata):
    """Build the feature frame in the exact column order the model was fitted on."""
    x_data = df[metadata["features"]].copy()
    for feature in metadata.get("numerical_features", []):
        x_data[feature] = pd.to_numeric(x_data[feature], errors="raise")
    for feature in metadata["categorical_features"]:
        x_data[feature] = x_data[feature].astype("category")
    return x_data


def predict_raw_proba(models, x_data):
    """Ensemble-averaged raw churn probability."""
    stacked = np.column_stack([model.predict_proba(x_data)[:, 1] for model in models])
    return stacked.mean(axis=1)


def mean_shap_contributions(models, x_data):
    """SHAP contributions averaged over the ensemble, bias column removed.

    The explanation has to be averaged over the same members as the probability,
    otherwise the reasons Model 2 receives describe a model that never produced
    the score shown next to them.
    """
    dmatrix = xgb.DMatrix(x_data, enable_categorical=True)
    stacked = np.stack(
        [np.asarray(model.get_booster().predict(dmatrix, pred_contribs=True))[:, :-1] for model in models]
    )
    return stacked.mean(axis=0)


def apply_probability_mode(raw_probabilities, calibrators, mode):
    """Map raw probabilities through the calibrator chosen at training time."""
    raw_probabilities = np.asarray(raw_probabilities, dtype="float64").reshape(-1)
    if mode == "sigmoid":
        return calibrators["sigmoid"].predict_proba(raw_probabilities.reshape(-1, 1))[:, 1]
    if mode == "isotonic":
        return calibrators["isotonic"].predict(raw_probabilities)
    return raw_probabilities
