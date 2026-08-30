"""
Preprocessing — construct Model 2 input JSONL from Model 1 output + customer data.

This module combines per-customer data with Model 1 (XGBoost) output into the
exact Model 2 input schema defined in Section 5 of the specification.

Design notes:
- A stable identifier (``case_id`` by convention in the notebook's training/eval
  data) must travel through every stage: Model 1 → Model 2 → clustering →
  dashboard, so results always trace back to the correct customer.
- The ``id_column`` parameter lets you adapt to whatever column name Model 1's
  raw output uses.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.config.settings import APPROVED_ACTIONS, APPROVED_ACTIONS_SET
from src.schema.validators import validate_model2_input


def build_model2_input(
    customer_data: Dict[str, Any],
    model1_output: Dict[str, Any],
    eligible_actions: Optional[List[str]] = None,
    case_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Combine customer data and Model 1 output into a single Model 2 input record.

    Parameters
    ----------
    customer_data : dict
        Raw customer fields — must contain sub-dicts or flat keys that map
        to the ``customer_context``, ``behavior``, and ``service_evidence``
        sections of the Model 2 input schema.  When the data is already
        pre-structured (i.e. has those three keys as nested dicts), they
        are used directly.
    model1_output : dict
        The output from Model 1 / XGBoost.  Must contain at least:
        ``churn_probability``, ``churn_prediction``, ``risk_level``,
        ``top_risk_factors``.
    eligible_actions : list[str] or None
        Subset of APPROVED_ACTIONS eligible for this customer.  Defaults
        to the full approved actions list.
    case_id : str or None
        Stable identifier for this customer/case.  Preserved in the output
        for downstream tracing.

    Returns
    -------
    dict
        A Model 2 input record matching the Section 5 schema.
    """
    if eligible_actions is None:
        eligible_actions = list(APPROVED_ACTIONS)
    else:
        invalid = [a for a in eligible_actions if a not in APPROVED_ACTIONS_SET]
        if invalid:
            raise ValueError(f"Invalid eligible action(s): {invalid}")

    # If customer_data is already pre-structured, use it directly.
    if all(k in customer_data for k in ("customer_context", "behavior", "service_evidence")):
        record = {
            "customer_context": customer_data["customer_context"],
            "behavior": customer_data["behavior"],
            "service_evidence": customer_data["service_evidence"],
        }
    else:
        # Flat-key mapping — adapt column names as needed for your dataset.
        record = {
            "customer_context": {
                "age": customer_data.get("age"),
                "tenure_months": customer_data.get("tenure_months"),
                "customer_segment": customer_data.get("customer_segment"),
                "income_regularity": customer_data.get("income_regularity"),
                "customer_yearly_value": customer_data.get("customer_yearly_value"),
                "products_count": customer_data.get("products_count"),
                "has_credit_card": customer_data.get("has_credit_card"),
                "has_loan": customer_data.get("has_loan"),
            },
            "behavior": {
                "days_since_last_transaction": customer_data.get("days_since_last_transaction"),
                "balance_change_30d": customer_data.get("balance_change_30d"),
                "transaction_change_30d": customer_data.get("transaction_change_30d"),
                "card_spend_change_30d": customer_data.get("card_spend_change_30d"),
                "app_login_change_30d": customer_data.get("app_login_change_30d"),
                "salary_missing_days": customer_data.get("salary_missing_days"),
                "external_transfer_change_30d": customer_data.get("external_transfer_change_30d"),
                "upi_share_of_spend": customer_data.get("upi_share_of_spend"),
                "fd_maturing_in_30d": customer_data.get("fd_maturing_in_30d"),
                "products_dropped_90d": customer_data.get("products_dropped_90d"),
                "emi_bounce_30d": customer_data.get("emi_bounce_30d"),
            },
            "service_evidence": {
                "complaints_30d": customer_data.get("complaints_30d"),
                "unresolved_complaints": customer_data.get("unresolved_complaints"),
                "failed_transactions_30d": customer_data.get("failed_transactions_30d"),
                "avg_resolution_time_hrs": customer_data.get("avg_resolution_time_hrs"),
                "complaint_text": customer_data.get("complaint_text"),
            },
        }

    record["model1"] = {
        "churn_probability": model1_output["churn_probability"],
        "churn_prediction": model1_output["churn_prediction"],
        "risk_level": model1_output["risk_level"],
        "top_risk_factors": model1_output["top_risk_factors"],
    }
    record["eligible_actions"] = eligible_actions

    return record


def build_model2_input_jsonl(
    customer_records: List[Dict[str, Any]],
    model1_outputs: List[Dict[str, Any]],
    output_path: str,
    id_column: str = "case_id",
    eligible_actions: Optional[List[str]] = None,
) -> int:
    """
    Build a JSONL file of Model 2 inputs from parallel customer data and
    Model 1 output lists.

    Parameters
    ----------
    customer_records : list[dict]
        One dict per customer with raw fields or pre-structured sub-dicts.
    model1_outputs : list[dict]
        Corresponding Model 1 outputs, in the same order.
    output_path : str
        Path to write the output JSONL file.
    id_column : str
        Column name used as the stable identifier.
    eligible_actions : list[str] or None
        Default eligible actions for all records.

    Returns
    -------
    int
        Number of records written.
    """
    if len(customer_records) != len(model1_outputs):
        raise ValueError(
            f"customer_records ({len(customer_records)}) and model1_outputs "
            f"({len(model1_outputs)}) must have the same length"
        )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    count = 0

    with open(output_path, "w", encoding="utf-8") as f:
        for cust, m1 in zip(customer_records, model1_outputs):
            case_id = cust.get(id_column) or m1.get(id_column)
            record = build_model2_input(
                customer_data=cust,
                model1_output=m1,
                eligible_actions=eligible_actions,
                case_id=case_id,
            )
            # Preserve the stable identifier at the top level for tracing.
            if case_id is not None:
                record[id_column] = case_id

            line = json.dumps(record, ensure_ascii=False, sort_keys=True)
            f.write(line + "\n")
            count += 1

    return count
