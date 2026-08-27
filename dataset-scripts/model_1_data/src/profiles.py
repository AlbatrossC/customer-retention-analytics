"""Stage 1 - static customer profiles.

One row per customer. Nothing here changes between snapshots.

Also holds the two things every later stage needs: the config loader and the
named random streams. Spec: dataset/model_1_plan.md sections 4.1-4.3, 4.7, 14.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from faker import Faker

# src/ -> model_1_data -> dataset-scripts -> repository root.
# PACKAGE_ROOT holds the generator; PROJECT_ROOT is what config.yaml's data
# paths are relative to. Every other module takes these two from here rather
# than counting parents itself.
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_PATH = PACKAGE_ROOT / "config.yaml"


def load_config(path: str | Path = CONFIG_PATH) -> dict:
    """Read config.yaml. Every tunable number in the generator comes from here."""
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def make_streams(config: dict) -> dict[str, np.random.Generator]:
    """One named generator per attribute, spawned from SeedSequence(master).

    Spawn order is the order of ``seed.streams`` in config.yaml. Appending a new
    name to the end of that list gives the new column its own stream and leaves
    every existing stream's draws untouched, so adding a column later does not
    shift the data already generated.
    """
    names = list(config["seed"]["streams"])
    children = np.random.SeedSequence(config["seed"]["master"]).spawn(len(names))
    return {name: np.random.default_rng(seq) for name, seq in zip(names, children)}


def customer_ids(config: dict) -> np.ndarray:
    """Sequential ids, C10000 to C19999. Not random, not UUID."""
    ds = config["dataset"]
    start = ds["customer_id_start"]
    prefix = ds["customer_id_prefix"]
    return np.array(
        [f"{prefix}{start + i}" for i in range(ds["n_customers"])], dtype=object
    )


def _draw_segments(config: dict, rng: np.random.Generator, n: int) -> np.ndarray:
    segments = config["profiles"]["segments"]
    names = list(segments)
    shares = np.array([segments[name]["share"] for name in names], dtype=float)
    shares = shares / shares.sum()
    return rng.choice(names, size=n, p=shares)


def _per_segment_param(config: dict, segment: np.ndarray, key: str) -> np.ndarray:
    """Broadcast a per-segment config value out to one value per customer."""
    segments = config["profiles"]["segments"]
    lookup = {name: params[key] for name, params in segments.items()}
    return np.array([lookup[value] for value in segment])


def _draw_names(config: dict, n: int) -> np.ndarray:
    """Faker en_IN names.

    Deliberately not ``fake.unique``: the en_IN pool is far smaller than 10,000
    and unique() would raise UniquenessException. Duplicate names are realistic.
    """
    fake = Faker(config["faker"]["locale"])
    Faker.seed(config["faker"]["seed"])
    return np.array([fake.name() for _ in range(n)], dtype=object)


def _cap_tenure(
    tenure_months: np.ndarray, age: np.ndarray, config: dict
) -> np.ndarray:
    """Hard rule from 4.2: tenure_months / 12 <= age - min_banking_age.

    Drawn first, capped after, so the tenure distribution keeps its shape for
    older customers instead of being squeezed for everyone.
    """
    profiles = config["profiles"]
    max_months = (age - profiles["min_banking_age"]) * 12
    capped = np.minimum(tenure_months, max_months)
    return np.clip(capped, profiles["tenure_min_months"], None).astype(int)


def build_profiles(config: dict, streams: dict[str, np.random.Generator]) -> pd.DataFrame:
    """Return one static row per customer."""
    n = config["dataset"]["n_customers"]
    profiles_cfg = config["profiles"]

    segment = _draw_segments(config, streams["segment"], n)

    age_min = _per_segment_param(config, segment, "age_min")
    age_max = _per_segment_param(config, segment, "age_max")
    age = streams["age"].integers(age_min, age_max + 1).astype(int)

    tenure_mean = _per_segment_param(config, segment, "tenure_mean_months")
    tenure_sd = _per_segment_param(config, segment, "tenure_sd_months")
    tenure_raw = streams["tenure"].normal(tenure_mean, tenure_sd)
    tenure_months = _cap_tenure(np.rint(tenure_raw), age, config)

    customer_name = _draw_names(config, n)

    value_mu = _per_segment_param(config, segment, "yearly_value_mu")
    value_sigma = _per_segment_param(config, segment, "yearly_value_sigma")
    customer_yearly_value = np.clip(
        streams["yearly_value"].lognormal(value_mu, value_sigma),
        profiles_cfg["yearly_value_min"],
        profiles_cfg["yearly_value_max"],
    )

    # Hidden. Enters the churn score, never becomes a model feature.
    loyalty = streams["loyalty"].normal(0.0, profiles_cfg["loyalty_sd"], size=n)

    products_rng = streams["products"]
    has_credit_card = (
        products_rng.random(n) < _per_segment_param(config, segment, "credit_card_p")
    ).astype(int)
    has_loan = (
        products_rng.random(n) < _per_segment_param(config, segment, "loan_p")
    ).astype(int)
    extra = products_rng.poisson(profiles_cfg["products"]["extra_poisson_lambda"], n)
    # 1 base account + each flag + extras, so the count can never contradict a flag.
    products_count = np.minimum(
        1 + has_credit_card + has_loan + extra, profiles_cfg["products"]["max_products"]
    ).astype(int)

    return pd.DataFrame(
        {
            "customer_id": customer_ids(config),
            "customer_name": customer_name,
            "age": age,
            "tenure_months": tenure_months,
            "customer_segment": segment,
            "income_regularity": _per_segment_param(config, segment, "income_regularity"),
            "customer_yearly_value": customer_yearly_value,
            "loyalty": loyalty,
            "products_count": products_count,
            "has_credit_card": has_credit_card,
            "has_loan": has_loan,
        }
    )
