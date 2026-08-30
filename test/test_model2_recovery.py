import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend import retention_api_server as server


def sample_payload(**signals):
    complaint = signals.pop("complaint", None)
    return {
        "task": "select_recovery_schemas_and_actions",
        "risk": {
            "churn_probability_percent": 83.2,
            "risk_score": 92.0,
            "churn_prediction": "Yes",
            "risk_level": "High",
        },
        "customer": {
            "segment": "salary",
            "income_regularity": signals.pop("income_regularity", "regular"),
            "value_tier": "medium",
            "tenure_months": 24,
            "products_count": signals.pop("products_count", 3),
            "has_credit_card": False,
            "has_loan": signals.pop("has_loan", False),
        },
        "customer_signals": {
            "days_since_last_transaction": 0,
            "balance_change_30d": 0,
            "transaction_change_30d": 0,
            "card_spend_change_30d": 0,
            "app_login_change_30d": 0,
            "salary_missing_days": 0,
            "external_transfer_change_30d": 0,
            "upi_share_of_spend": 0.2,
            "fd_maturing_in_30d": 0,
            "products_dropped_90d": 0,
            "complaints_30d": 0,
            "unresolved_complaints": 0,
            "failed_transactions_30d": 0,
            "avg_resolution_time_hrs": 0,
            "emi_bounce_30d": 0,
            **signals,
        },
        "main_signals": [
            {"field": field, "value": value, "message": f"{field} triggered."}
            for field, value in signals.items()
        ],
        "trend_summary": {"overall_direction": "stable", "messages": []},
        "complaint": complaint,
        "risk_group": "unknown",
    }


@pytest.fixture()
def recovery_config():
    return server.load_model2_recovery_config(force=True)


def test_load_model2_recovery_config_validates_catalog(recovery_config):
    assert recovery_config["system_prompt"].strip()
    assert len(recovery_config["recovery_schemas"]) == 10
    assert "SERVICE_COMPLAINT" in server.recovery_schema_map(recovery_config)


def test_parse_model2_response_accepts_strict_json(recovery_config):
    payload = sample_payload(complaints_30d=2, unresolved_complaints=1)
    text = json.dumps(
        {
            "primary_schema": "SERVICE_COMPLAINT",
            "selected_schemas": ["SERVICE_COMPLAINT"],
            "actions": [
                {
                    "action_id": "complaint_follow_up",
                    "action_label": "Complaint follow-up",
                    "reason": "Customer has unresolved complaint activity.",
                    "priority": "high",
                    "evidence_fields": ["complaints_30d", "unresolved_complaints"],
                },
                {
                    "action_id": "complaint_escalation",
                    "action_label": "Complaint escalation",
                    "reason": "The complaint needs escalation because it is unresolved.",
                    "priority": "high",
                    "evidence_fields": ["unresolved_complaints"],
                },
            ],
            "summary_reason": "High churn risk is linked to unresolved service friction.",
        }
    )

    parsed = server.parse_model2_response(text, payload, recovery_config)

    assert not server.response_needs_fallback(parsed)
    assert parsed["primary_schema"] == "SERVICE_COMPLAINT"
    assert parsed["actions"][0]["action_id"] == "complaint_follow_up"


def test_parse_model2_response_rejects_markdown(recovery_config):
    parsed = server.parse_model2_response(
        "Why:\n- Complaint exists\n\nNext Actions:\n- Follow up",
        sample_payload(complaints_30d=1),
        recovery_config,
    )

    assert server.response_needs_fallback(parsed)
    assert "strict JSON" in parsed["error"]


def test_parse_model2_response_rejects_unknown_action(recovery_config):
    payload = sample_payload(complaints_30d=1)
    text = json.dumps(
        {
            "primary_schema": "SERVICE_COMPLAINT",
            "selected_schemas": ["SERVICE_COMPLAINT"],
            "actions": [
                {
                    "action_id": "unknown_action",
                    "action_label": "Unknown action",
                    "reason": "Customer has a complaint.",
                    "priority": "high",
                    "evidence_fields": ["complaints_30d"],
                },
                {
                    "action_id": "complaint_follow_up",
                    "action_label": "Complaint follow-up",
                    "reason": "Customer has a complaint.",
                    "priority": "high",
                    "evidence_fields": ["complaints_30d"],
                },
            ],
            "summary_reason": "Service friction is visible.",
        }
    )

    parsed = server.parse_model2_response(text, payload, recovery_config)

    assert server.response_needs_fallback(parsed)
    assert "selected schemas" in parsed["error"]


def test_parse_model2_response_rejects_missing_action_reason(recovery_config):
    payload = sample_payload(complaints_30d=1)
    text = json.dumps(
        {
            "primary_schema": "SERVICE_COMPLAINT",
            "selected_schemas": ["SERVICE_COMPLAINT"],
            "actions": [
                {
                    "action_id": "complaint_follow_up",
                    "action_label": "Complaint follow-up",
                    "reason": "",
                    "priority": "high",
                    "evidence_fields": ["complaints_30d"],
                },
                {
                    "action_id": "complaint_escalation",
                    "action_label": "Complaint escalation",
                    "reason": "The complaint needs escalation.",
                    "priority": "high",
                    "evidence_fields": ["complaints_30d"],
                },
            ],
            "summary_reason": "Service friction is visible.",
        }
    )

    parsed = server.parse_model2_response(text, payload, recovery_config)

    assert server.response_needs_fallback(parsed)
    assert "reason" in parsed["error"]


@pytest.mark.parametrize(
    ("signals", "expected_schema"),
    [
        ({"complaints_30d": 1}, "SERVICE_COMPLAINT"),
        ({"failed_transactions_30d": 1}, "TRANSACTION_FAILURE"),
        ({"transaction_change_30d": -20}, "ACTIVITY_DECLINE"),
        ({"balance_change_30d": -30}, "BALANCE_OUTFLOW"),
        ({"app_login_change_30d": -25}, "DIGITAL_DISENGAGEMENT"),
        ({"salary_missing_days": 5}, "SALARY_OR_INCOME_BREAK"),
        ({"fd_maturing_in_30d": 1}, "FD_MATURITY"),
        ({"products_dropped_90d": 1}, "PRODUCT_DROPOFF"),
        ({"emi_bounce_30d": 1, "has_loan": True}, "LOAN_REPAYMENT_STRESS"),
    ],
)
def test_deterministic_schema_selection_for_triggers(recovery_config, signals, expected_schema):
    selected = server.deterministic_schema_selection(sample_payload(**signals), recovery_config)

    assert selected[0] == expected_schema


def test_deterministic_schema_selection_low_risk_monitor(recovery_config):
    payload = sample_payload()
    payload["risk"]["risk_level"] = "Low"
    payload["risk"]["churn_prediction"] = "No"
    payload["risk"]["churn_probability_percent"] = 2.1

    result = server.fallback_model2_response(payload, recovery_config)

    assert result["primary_schema"] == "LOW_RISK_MONITOR"
    assert result["selected_schemas"] == ["LOW_RISK_MONITOR"]
    assert 1 <= len(result["actions"]) <= 2
    assert all(action["priority"] == "low" for action in result["actions"])
    assert all(action["reason"] for action in result["actions"])


def test_deterministic_schema_selection_low_risk_active_issue(recovery_config):
    payload = sample_payload(failed_transactions_30d=3, unresolved_complaints=1)
    payload["risk"]["risk_level"] = "Low"
    payload["risk"]["churn_prediction"] = "No"
    payload["risk"]["churn_probability_percent"] = 3.0

    result = server.fallback_model2_response(payload, recovery_config)

    assert result["primary_schema"] == "SERVICE_COMPLAINT"
    assert "LOW_RISK_MONITOR" not in result["selected_schemas"]
    assert all(action["priority"] == "low" for action in result["actions"])


def test_context_fields_do_not_trigger_income_or_product_schemas(recovery_config):
    payload = sample_payload(income_regularity="seasonal", products_count=1)

    selected = server.deterministic_schema_selection(payload, recovery_config)

    assert "SALARY_OR_INCOME_BREAK" not in selected
    assert "PRODUCT_DROPOFF" not in selected


def test_parse_model2_response_rejects_aggressive_low_risk_output(recovery_config):
    payload = sample_payload(failed_transactions_30d=2)
    payload["risk"]["risk_level"] = "Low"
    payload["risk"]["churn_prediction"] = "No"
    payload["risk"]["churn_probability_percent"] = 3.0
    text = json.dumps(
        {
            "primary_schema": "TRANSACTION_FAILURE",
            "selected_schemas": ["TRANSACTION_FAILURE"],
            "actions": [
                {
                    "action_id": "failed_transaction_review",
                    "action_label": "Failed transaction review",
                    "reason": "Customer has recent failed transactions.",
                    "priority": "high",
                    "evidence_fields": ["failed_transactions_30d"],
                }
            ],
            "summary_reason": "Payment friction is visible.",
        }
    )

    parsed = server.parse_model2_response(text, payload, recovery_config)

    assert server.response_needs_fallback(parsed)
    assert "low priority" in parsed["error"]


def test_predict_model2_retries_until_valid_json(monkeypatch, recovery_config):
    payload = sample_payload(complaints_30d=1)
    valid_text = json.dumps(
        {
            "primary_schema": "SERVICE_COMPLAINT",
            "selected_schemas": ["SERVICE_COMPLAINT"],
            "actions": [
                {
                    "action_id": "complaint_follow_up",
                    "action_label": "Complaint follow-up",
                    "reason": "Customer has a recent complaint.",
                    "priority": "high",
                    "evidence_fields": ["complaints_30d"],
                },
                {
                    "action_id": "service_recovery_call",
                    "action_label": "Service recovery call",
                    "reason": "A service recovery call can confirm resolution.",
                    "priority": "medium",
                    "evidence_fields": ["complaints_30d"],
                },
            ],
            "summary_reason": "High churn risk is linked to recent service friction.",
        }
    )
    outputs = iter(["Why:\n- bad", "{bad json", valid_text])
    calls = []

    monkeypatch.setattr(server, "model2", "retention-0.5bv2")
    monkeypatch.setattr(server, "load_model2_recovery_config", lambda force=False: recovery_config)
    monkeypatch.setattr(server, "ollama_chat", lambda messages: calls.append(messages) or next(outputs))

    result = server.predict_model2(payload)

    assert result["primary_schema"] == "SERVICE_COMPLAINT"
    assert len(calls) == 3
    assert "previous_invalid_output" in calls[1][1]["content"]


def test_predict_model2_falls_back_after_retry_limit(monkeypatch, recovery_config):
    payload = sample_payload(failed_transactions_30d=2)
    calls = []

    monkeypatch.setattr(server, "model2", "retention-0.5bv2")
    monkeypatch.setattr(server, "load_model2_recovery_config", lambda force=False: recovery_config)
    monkeypatch.setattr(server, "ollama_chat", lambda messages: calls.append(messages) or "Next Actions:\n- bad")

    result = server.predict_model2(payload)

    assert result["primary_schema"] == "TRANSACTION_FAILURE"
    assert len(calls) == server.MODEL2_MAX_RETRIES
    assert all(action["reason"] for action in result["actions"])


def test_predict_model2_falls_back_after_generation_errors(monkeypatch, recovery_config):
    payload = sample_payload(balance_change_30d=-25)
    calls = []

    def fail_generation(messages):
        calls.append(messages)
        raise RuntimeError("Ollama chat HTTP 400: context length exceeded")

    monkeypatch.setattr(server, "model2", "retention-0.5bv2")
    monkeypatch.setattr(server, "load_model2_recovery_config", lambda force=False: recovery_config)
    monkeypatch.setattr(server, "ollama_chat", fail_generation)

    result = server.predict_model2(payload)

    assert result["primary_schema"] == "BALANCE_OUTFLOW"
    assert len(calls) == server.MODEL2_MAX_RETRIES
    assert all(action["reason"] for action in result["actions"])
