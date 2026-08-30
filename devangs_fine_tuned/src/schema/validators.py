"""
Schema validation for Model 2 input and output.

Enforces the exact contracts from the project specification (Sections 5 and 6).
All approved value lists are imported from src.config.settings so there is
a single source of truth.
"""

from typing import Any, Dict, List, Optional, Tuple

from src.config.settings import (
    APPROVED_ACTIONS_SET,
    APPROVED_REASONS_SET,
    APPROVED_URGENCY_SET,
    VALID_CHURN_PREDICTIONS,
    VALID_CUSTOMER_SEGMENTS,
    VALID_INCOME_REGULARITY,
    VALID_RISK_LEVELS,
)


class ValidationError(Exception):
    """Raised when a schema validation check fails."""


# ── helpers ──────────────────────────────────────────────────────────────────

def _check_type(value: Any, expected_type: type, field: str) -> None:
    if not isinstance(value, expected_type):
        raise ValidationError(
            f"{field}: expected {expected_type.__name__}, got {type(value).__name__}"
        )


def _check_in(value: Any, allowed: set, field: str) -> None:
    if value not in allowed:
        raise ValidationError(f"{field}: '{value}' not in {sorted(allowed)}")


def _check_int_or_null(value: Any, field: str) -> None:
    if value is not None and not isinstance(value, int):
        raise ValidationError(f"{field}: expected int or null, got {type(value).__name__}")


def _check_number(value: Any, field: str) -> None:
    if not isinstance(value, (int, float)):
        raise ValidationError(f"{field}: expected number, got {type(value).__name__}")


# ── input validator ──────────────────────────────────────────────────────────

_REQUIRED_INPUT_SECTIONS = {
    "customer_context",
    "behavior",
    "service_evidence",
    "model1",
    "eligible_actions",
}

_CUSTOMER_CONTEXT_FIELDS = {
    "age": int,
    "tenure_months": int,
    "customer_segment": str,
    "income_regularity": str,
    "customer_yearly_value": (int, float),
    "products_count": int,
    "has_credit_card": int,
    "has_loan": int,
}

_BEHAVIOR_FIELDS = {
    "days_since_last_transaction": int,
    "balance_change_30d": (int, float),
    "transaction_change_30d": (int, float),
    "card_spend_change_30d": (int, float),
    "app_login_change_30d": (int, float),
    "external_transfer_change_30d": (int, float),
    "upi_share_of_spend": (int, float),
    "fd_maturing_in_30d": int,
    "products_dropped_90d": int,
    "emi_bounce_30d": int,
    # salary_missing_days: int or null — handled separately
}

_SERVICE_EVIDENCE_FIELDS = {
    "complaints_30d": int,
    "unresolved_complaints": int,
    "failed_transactions_30d": int,
    "avg_resolution_time_hrs": (int, float),
    # complaint_text: str or null — handled separately
}


def validate_model2_input(data: Dict[str, Any]) -> List[str]:
    """
    Validate a Model 2 input record against the exact schema (Section 5).

    Returns a list of error strings. An empty list means the input is valid.
    """
    errors: List[str] = []

    # Top-level keys
    missing = _REQUIRED_INPUT_SECTIONS - set(data.keys())
    if missing:
        errors.append(f"Missing top-level keys: {sorted(missing)}")
        return errors  # cannot continue without top-level structure

    # ── customer_context ─────────────────────────────────────────────────
    cc = data["customer_context"]
    if not isinstance(cc, dict):
        errors.append("customer_context: expected dict")
    else:
        for field, ftype in _CUSTOMER_CONTEXT_FIELDS.items():
            if field not in cc:
                errors.append(f"customer_context.{field}: missing")
            elif not isinstance(cc[field], ftype if isinstance(ftype, tuple) else (ftype,)):
                errors.append(
                    f"customer_context.{field}: expected {ftype}, got {type(cc[field]).__name__}"
                )
        if "customer_segment" in cc and cc["customer_segment"] not in VALID_CUSTOMER_SEGMENTS:
            errors.append(
                f"customer_context.customer_segment: '{cc['customer_segment']}' "
                f"not in {sorted(VALID_CUSTOMER_SEGMENTS)}"
            )
        if "income_regularity" in cc and cc["income_regularity"] not in VALID_INCOME_REGULARITY:
            errors.append(
                f"customer_context.income_regularity: '{cc['income_regularity']}' "
                f"not in {sorted(VALID_INCOME_REGULARITY)}"
            )
        if "has_credit_card" in cc and cc["has_credit_card"] not in (0, 1):
            errors.append("customer_context.has_credit_card: must be 0 or 1")
        if "has_loan" in cc and cc["has_loan"] not in (0, 1):
            errors.append("customer_context.has_loan: must be 0 or 1")

    # ── behavior ─────────────────────────────────────────────────────────
    beh = data["behavior"]
    if not isinstance(beh, dict):
        errors.append("behavior: expected dict")
    else:
        for field, ftype in _BEHAVIOR_FIELDS.items():
            if field not in beh:
                errors.append(f"behavior.{field}: missing")
            elif not isinstance(beh[field], ftype if isinstance(ftype, tuple) else (ftype,)):
                errors.append(
                    f"behavior.{field}: expected {ftype}, got {type(beh[field]).__name__}"
                )
        # salary_missing_days: int or null
        if "salary_missing_days" not in beh:
            errors.append("behavior.salary_missing_days: missing")
        elif beh["salary_missing_days"] is not None and not isinstance(
            beh["salary_missing_days"], (int, float)
        ):
            errors.append("behavior.salary_missing_days: expected int or null")

    # ── service_evidence ─────────────────────────────────────────────────
    se = data["service_evidence"]
    if not isinstance(se, dict):
        errors.append("service_evidence: expected dict")
    else:
        for field, ftype in _SERVICE_EVIDENCE_FIELDS.items():
            if field not in se:
                errors.append(f"service_evidence.{field}: missing")
            elif not isinstance(se[field], ftype if isinstance(ftype, tuple) else (ftype,)):
                errors.append(
                    f"service_evidence.{field}: expected {ftype}, got {type(se[field]).__name__}"
                )
        # complaint_text: str or null
        if "complaint_text" not in se:
            errors.append("service_evidence.complaint_text: missing")
        elif se["complaint_text"] is not None and not isinstance(se["complaint_text"], str):
            errors.append("service_evidence.complaint_text: expected str or null")

    # ── model1 ───────────────────────────────────────────────────────────
    m1 = data["model1"]
    if not isinstance(m1, dict):
        errors.append("model1: expected dict")
    else:
        if "churn_probability" not in m1:
            errors.append("model1.churn_probability: missing")
        elif not isinstance(m1["churn_probability"], (int, float)):
            errors.append("model1.churn_probability: expected float")

        if "churn_prediction" not in m1:
            errors.append("model1.churn_prediction: missing")
        elif m1["churn_prediction"] not in VALID_CHURN_PREDICTIONS:
            errors.append(
                f"model1.churn_prediction: '{m1['churn_prediction']}' not in {sorted(VALID_CHURN_PREDICTIONS)}"
            )

        if "risk_level" not in m1:
            errors.append("model1.risk_level: missing")
        elif m1["risk_level"] not in VALID_RISK_LEVELS:
            errors.append(
                f"model1.risk_level: '{m1['risk_level']}' not in {sorted(VALID_RISK_LEVELS)}"
            )

        if "top_risk_factors" not in m1:
            errors.append("model1.top_risk_factors: missing")
        elif not isinstance(m1["top_risk_factors"], list):
            errors.append("model1.top_risk_factors: expected list")
        else:
            for i, rf in enumerate(m1["top_risk_factors"]):
                if not isinstance(rf, dict):
                    errors.append(f"model1.top_risk_factors[{i}]: expected dict")
                elif "factor" not in rf or "value" not in rf:
                    errors.append(f"model1.top_risk_factors[{i}]: must have 'factor' and 'value'")

    # ── eligible_actions ─────────────────────────────────────────────────
    ea = data["eligible_actions"]
    if not isinstance(ea, list) or len(ea) == 0:
        errors.append("eligible_actions: expected non-empty list")
    else:
        for action in ea:
            if action not in APPROVED_ACTIONS_SET:
                errors.append(f"eligible_actions: '{action}' not in approved actions")

    return errors


# ── output validator ─────────────────────────────────────────────────────────

_REQUIRED_OUTPUT_KEYS = {
    "primary_reason",
    "secondary_reasons",
    "evidence",
    "urgency",
    "recommended_action",
    "reasoning_summary",
}


def validate_model2_output(
    output: Dict[str, Any],
    eligible_actions: Optional[List[str]] = None,
) -> List[str]:
    """
    Validate a Model 2 output record against the exact schema (Section 6).

    If ``eligible_actions`` is provided, also checks that
    ``recommended_action ∈ eligible_actions``.

    Returns a list of error strings. An empty list means the output is valid.
    """
    errors: List[str] = []

    if not isinstance(output, dict):
        errors.append("Output is not a dict")
        return errors

    missing = _REQUIRED_OUTPUT_KEYS - set(output.keys())
    if missing:
        errors.append(f"Missing output keys: {sorted(missing)}")
        return errors

    # primary_reason
    if output["primary_reason"] not in APPROVED_REASONS_SET:
        errors.append(f"primary_reason: '{output['primary_reason']}' not in approved reasons")

    # secondary_reasons
    if not isinstance(output["secondary_reasons"], list):
        errors.append("secondary_reasons: expected list")
    else:
        for i, sr in enumerate(output["secondary_reasons"]):
            if sr not in APPROVED_REASONS_SET:
                errors.append(f"secondary_reasons[{i}]: '{sr}' not in approved reasons")
            if sr == output.get("primary_reason"):
                errors.append(
                    f"secondary_reasons[{i}]: '{sr}' duplicates primary_reason"
                )

    # evidence
    if not isinstance(output["evidence"], list):
        errors.append("evidence: expected list")

    # urgency
    if output["urgency"] not in APPROVED_URGENCY_SET:
        errors.append(f"urgency: '{output['urgency']}' not in approved urgency levels")

    # recommended_action
    if output["recommended_action"] not in APPROVED_ACTIONS_SET:
        errors.append(
            f"recommended_action: '{output['recommended_action']}' not in approved actions"
        )
    if eligible_actions is not None and output["recommended_action"] not in eligible_actions:
        errors.append(
            f"recommended_action: '{output['recommended_action']}' not in eligible_actions "
            f"{eligible_actions}"
        )

    # reasoning_summary
    if not isinstance(output["reasoning_summary"], str) or not output["reasoning_summary"].strip():
        errors.append("reasoning_summary: must be a non-empty string")

    return errors
