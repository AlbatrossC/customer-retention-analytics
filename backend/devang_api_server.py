import json
import re
import sys
import time
import urllib.error
import urllib.request
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
from typing import Any

from fastapi import Body, FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


ROOT = Path(__file__).resolve().parents[1]
DEVANG_ROOT = ROOT / "devangs_fine_tuned"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(DEVANG_ROOT) not in sys.path:
    sys.path.insert(0, str(DEVANG_ROOT))

from backend import retention_api_server as model1_server
from src.config.settings import APPROVED_ACTIONS, APPROVED_REASONS, APPROVED_URGENCY, SYSTEM_PROMPT
from src.schema.validators import validate_model2_input, validate_model2_output


HOST = "127.0.0.1"
PORT = 8001
OLLAMA_HOST = "http://127.0.0.1:11434"
OLLAMA_MODEL = "devang-model2-q4"
MODEL_TIMEOUT_SECONDS = 180
MAX_RETRIES = 3
MIN_ELIGIBLE_ACTIONS = 3
MAX_ELIGIBLE_ACTIONS = 5
MAX_TOP_RISK_FACTORS = 3

# Model 1 emits a calibrated (sigmoid) probability that runs roughly 0.015-0.43.
# Model 2 was fine-tuned on churn_probability in the 0.18-0.78 range, which matches
# model1.raw_churn_probability far better. Flip to True to run the raw arm of that
# A/B; risk_level always stays the calibrated business threshold either way.
USE_RAW_CHURN_PROBABILITY = False

DECISION_RULES = """Evidence rules:
- Every evidence item must be `field=value` copied verbatim from customer_case.
  Never flip a sign, never round toward a worse value, never invent a field.
- Cite only NON-ZERO, non-null signals. A field equal to 0 or null is the ABSENCE
  of evidence and must never be cited as support for a reason.
- Never cite your own output fields (primary_reason, secondary_reasons, urgency,
  recommended_action) as evidence.
- model1.top_risk_factors is an index into this same case: the features that
  INCREASED churn risk, ordered strongest first. Look each one up in behavior or
  service_evidence and cite the value shown there. Treat factor #1 as the leading
  driver.

Urgency - check HIGH first, then LOW, then fall through to MEDIUM:
- HIGH   - model1.risk_level is High, OR unresolved_complaints > 0 together with
           avg_resolution_time_hrs >= 48, OR emi_bounce_30d > 0 together with
           salary_missing_days > 0.
- LOW    - model1.risk_level is Low AND every service_evidence field is 0 or null
           AND no behavior field moved worse than -20%.
- MEDIUM - everything else.
Do not default to MEDIUM without ruling out HIGH and LOW.

Action:
- When model1.risk_level is High, or churn_prediction is "Yes", MONITOR is NOT an
  acceptable answer unless every service_evidence field is 0 and no behavior field
  moved worse than -20%. Pick the eligible action that matches primary_reason.
- When model1.risk_level is Low and the evidence is genuinely mixed or weak,
  staying conservative with UNKNOWN and MONITOR is correct.
- eligible_actions is the final authority. If the best action is absent, choose the
  closest lower-severity eligible action; MONITOR only as the last resort.

Reason selection - route complaint_text and the strongest behavior signal:
- fees, charges or penalties levied wrongly       -> FEE_DISSATISFACTION
- repeat complaints, no callback, slow resolution -> SERVICE_DISSATISFACTION
- app/UPI/login failures, failed transactions     -> DIGITAL_FRICTION
- EMI vs salary timing, bounces, missed salary    -> FINANCIAL_STRESS
- funds leaving, which REQUIRES external_transfer_change_30d
  > 0 together with balance_change_30d < 0        -> COMPETITOR_MIGRATION
- inactivity: days_since_last_transaction high with
  transaction_change_30d < 0 and
  app_login_change_30d < 0                        -> LOW_ENGAGEMENT
- product does not fit the customer's cashflow    -> PRODUCT_MISMATCH
- seasonal or one-off dip that is already
  recovering                                      -> TEMPORARY_SEASONAL_CHANGE
- UNKNOWN only when NO reason above is supported by a single non-zero signal.
Check the sign before choosing: a reason whose rule needs a value to fall cannot be
supported by that value rising.

Coherence:
- UNKNOWN must never appear in secondary_reasons.
- If primary_reason is UNKNOWN, secondary_reasons must be empty.
- secondary_reasons must never repeat primary_reason.
- reasoning_summary must name the recommended_action you actually chose and quote
  the specific cited values that justify it. Do not open with a fixed phrase, and
  do not describe an action you did not choose.

Final check - apply these to your draft before you answer:
1. Delete every evidence item whose value is 0, 0.0, null or None. They prove
   nothing. If that empties the list, cite the largest non-zero behavior values
   instead.
2. If complaints_30d, unresolved_complaints and avg_resolution_time_hrs are all 0
   and complaint_text is null, then primary_reason MUST NOT be
   SERVICE_DISSATISFACTION - there is no service evidence in this case. Pick the
   reason that matches the behavior signals instead.
3. reasoning_summary must contain the recommended_action you chose and must not
   name any other action. Do not write "complaint escalation" unless
   recommended_action is COMPLAINT_ESCALATION.
4. Never write a reason name in place of an action name."""


class Model2Request(BaseModel):
    payload: dict[str, Any]


class BatchModel2Request(BaseModel):
    payloads: list[dict[str, Any]]


Model1Request = model1_server.Model1Request
BothRequest = model1_server.BothRequest


def canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def output_json_schema(eligible_actions: list[str] | None = None) -> dict[str, Any]:
    action_enum = eligible_actions or APPROVED_ACTIONS
    return {
        "type": "object",
        "properties": {
            "primary_reason": {"type": "string", "enum": APPROVED_REASONS},
            "secondary_reasons": {
                "type": "array",
                "items": {"type": "string", "enum": APPROVED_REASONS},
            },
            "evidence": {
                "type": "array",
                "items": {"type": "string"},
            },
            "urgency": {"type": "string", "enum": APPROVED_URGENCY},
            "recommended_action": {"type": "string", "enum": action_enum},
            "reasoning_summary": {"type": "string"},
        },
        "required": [
            "primary_reason",
            "secondary_reasons",
            "evidence",
            "urgency",
            "recommended_action",
            "reasoning_summary",
        ],
        "additionalProperties": False,
    }


def devang_system_prompt() -> str:
    return (
        SYSTEM_PROMPT
        + "\n\n"
        + DECISION_RULES
        + "\n\nUse only these approved primary_reason and secondary_reasons values: "
        + canonical_json(APPROVED_REASONS)
        + "\nUse only these approved recommended_action values, and select recommended_action only from the input's eligible_actions: "
        + canonical_json(APPROVED_ACTIONS)
        + "\n\nReturn only valid JSON with exactly these keys: "
        "primary_reason, secondary_reasons, evidence, urgency, recommended_action, reasoning_summary. "
        "Do not include markdown or text outside JSON."
    )


def build_user_payload(case_input: dict[str, Any], last_error: str | None = None) -> dict[str, Any]:
    allowed_actions = case_input["eligible_actions"]
    instruction = (
        "Use this customer_case as the only input. recommended_action MUST be exactly one of "
        f"allowed_recommended_actions={canonical_json(allowed_actions)}. "
        "Use primary_reason and secondary_reasons only from the approved Devang reasons in the system prompt. "
        "Apply the urgency, action, reason-selection and coherence rules from the system prompt to this case."
    )
    if last_error is not None:
        instruction += (
            " The previous response failed validation. Fix only the invalid fields, especially "
            "recommended_action, and return the same JSON object shape."
        )
    return {
        "customer_case": case_input,
        "allowed_recommended_actions": allowed_actions,
        "instruction": instruction,
        **({"previous_error": last_error} if last_error is not None else {}),
    }


def ollama_get(route: str, timeout: int = 10) -> dict[str, Any]:
    with urllib.request.urlopen(f"{OLLAMA_HOST}{route}", timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def ollama_post(route: str, payload: dict[str, Any], timeout: int = MODEL_TIMEOUT_SECONDS) -> dict[str, Any]:
    request = urllib.request.Request(
        f"{OLLAMA_HOST}{route}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Ollama is not reachable at {OLLAMA_HOST}: {exc}") from exc


def require_ollama_model() -> None:
    tags = ollama_get("/api/tags")
    names = {item.get("name") for item in tags.get("models", [])}
    if OLLAMA_MODEL not in names and f"{OLLAMA_MODEL}:latest" not in names:
        raise RuntimeError(
            f"Ollama model '{OLLAMA_MODEL}' was not found. "
            f"Run: ollama create {OLLAMA_MODEL} -f devangs_fine_tuned\\Modelfile.q4"
        )


def model1_loaded() -> bool:
    return model1_server.model1 is not None and model1_server.calibrator is not None


def load_model1() -> None:
    if not model1_loaded():
        model1_server.load_model1()


def extract_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"```$", "", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(text[start : end + 1])


def strip_case_id(record: dict[str, Any], id_column: str = "case_id") -> tuple[dict[str, Any], Any]:
    if id_column in record:
        return {key: value for key, value in record.items() if key != id_column}, record[id_column]
    return record, None


def number_or_default(value: Any, default: float | int) -> Any:
    if value is None:
        return default
    try:
        return value.item()
    except AttributeError:
        return value


def churn_probability_for_model2(model1_output: dict[str, Any]) -> Any:
    if USE_RAW_CHURN_PROBABILITY:
        raw = model1_output.get("raw_churn_probability")
        if raw is not None:
            return raw
    return model1_output["churn_probability"]


def probability_0_to_1(value: Any) -> float:
    probability = float(value)
    if probability > 1:
        probability = probability / 100.0
    return round(min(max(probability, 0.0), 1.0), 4)


_FACTOR_PREFIX = re.compile(r"^(latest|avg|sum|max|min|std|vs_avg)_")
_FACTOR_SUFFIX = re.compile(r"_(trend|available_history|1m|3m|6m|12m)$")

# Behavior fields whose magnitude ranks a fallback factor when nothing resolves.
_FALLBACK_BEHAVIOR_FIELDS = (
    "days_since_last_transaction",
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "external_transfer_change_30d",
)


def base_feature_name(factor: str) -> str:
    """Reduce a Model 1 engineered feature name to the raw field it derives from.

    Model 2 was fine-tuned on top_risk_factors whose names and values both appear
    verbatim elsewhere in the case, so aggregates like
    ``latest_vs_avg_external_transfer_change_30d_available_history`` have to collapse
    back to ``external_transfer_change_30d`` before they are forwarded.
    """
    name = factor
    for _ in range(4):
        previous = name
        name = _FACTOR_SUFFIX.sub("", _FACTOR_PREFIX.sub("", name))
        if name == previous:
            break
    return name


def devang_top_risk_factors(
    model1_output: dict[str, Any],
    case_fields: dict[str, Any],
) -> list[dict[str, Any]]:
    factors: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in model1_output.get("top_risk_factors", []):
        name = base_feature_name(str(item.get("factor", "")))
        # Drop aggregates with no counterpart in the case: forwarding them breaks the
        # index property and leaves the model reconciling two values for one field.
        if name in seen or case_fields.get(name) is None:
            continue
        seen.add(name)
        factors.append({"factor": name, "value": case_fields[name]})
        if len(factors) == MAX_TOP_RISK_FACTORS:
            break

    # Training always showed exactly MAX_TOP_RISK_FACTORS entries, so top up from the
    # largest behaviour movers rather than handing the model a short or empty list.
    if len(factors) < MAX_TOP_RISK_FACTORS:
        ranked = sorted(
            (
                field
                for field in _FALLBACK_BEHAVIOR_FIELDS
                if field not in seen and case_fields.get(field) is not None
            ),
            key=lambda field: abs(float(case_fields[field])),
            reverse=True,
        )
        for field in ranked[: MAX_TOP_RISK_FACTORS - len(factors)]:
            factors.append({"factor": field, "value": case_fields[field]})

    return factors


_FEE_KEYWORDS = ("charge", "fee", "penalty", "levied", "bounce charge", "deduct", "refund")
_CARD_KEYWORDS = ("card", "cloned", "atm", "swipe", "pos ", "debit card", "credit card")
_LOAN_KEYWORDS = ("emi", "loan", "instal", "repayment", "tenure")
_DIGITAL_KEYWORDS = ("app", "upi", "login", "otp", "netbanking", "online", "pending", "stuck")


def default_eligible_actions(
    customer: dict[str, Any],
    model1_output: dict[str, Any],
    complaint_text: str | None = None,
) -> list[str]:
    """Build a short, evidence-driven candidate list.

    Model 2 was fine-tuned on 3-4 curated actions per case. Handing it all ten
    (the previous behaviour for Medium/High risk) is out of distribution and biases
    it toward the head of the list, which is MONITOR.
    """
    risk_level = model1_output.get("risk_level")
    complaints = int(number_or_default(customer.get("complaints_30d"), 0))
    unresolved = int(number_or_default(customer.get("unresolved_complaints"), 0))
    failed_transactions = int(number_or_default(customer.get("failed_transactions_30d"), 0))
    avg_resolution = float(number_or_default(customer.get("avg_resolution_time_hrs"), 0.0))
    emi_bounce = int(number_or_default(customer.get("emi_bounce_30d"), 0))
    salary_missing = int(number_or_default(customer.get("salary_missing_days"), 0))
    fd_maturing = int(number_or_default(customer.get("fd_maturing_in_30d"), 0))
    products_dropped = int(number_or_default(customer.get("products_dropped_90d"), 0))
    days_idle = int(number_or_default(customer.get("days_since_last_transaction"), 0))
    app_login_change = float(number_or_default(customer.get("app_login_change_30d"), 0.0))
    external_transfer = float(number_or_default(customer.get("external_transfer_change_30d"), 0.0))
    balance_change = float(number_or_default(customer.get("balance_change_30d"), 0.0))
    has_loan = int(number_or_default(customer.get("has_loan"), 0))
    has_card = int(number_or_default(customer.get("has_credit_card"), 0))

    if complaint_text is None:
        complaint_text = customer.get("complaint_text")
    text = str(complaint_text or "").lower()

    def mentions(keywords: tuple[str, ...]) -> bool:
        return any(keyword in text for keyword in keywords)

    # Ordered strongest-evidence first so truncation keeps the best candidates.
    candidates: list[tuple[bool, str]] = [
        (unresolved > 0 or avg_resolution >= 48, "COMPLAINT_ESCALATION"),
        (mentions(_FEE_KEYWORDS), "FEE_WAIVER_REVIEW"),
        (has_card > 0 and mentions(_CARD_KEYWORDS), "CARD_REVIEW"),
        (emi_bounce > 0 or (has_loan > 0 and mentions(_LOAN_KEYWORDS)), "LOAN_REVIEW"),
        (emi_bounce > 0 or salary_missing > 0, "FINANCIAL_GUIDANCE"),
        (complaints > 0 or failed_transactions > 0 or mentions(_DIGITAL_KEYWORDS) or bool(text), "SERVICE_RECOVERY"),
        (fd_maturing > 0 or products_dropped > 0 or external_transfer >= 25.0, "PRODUCT_REVIEW"),
        (days_idle >= 14 or app_login_change <= -25.0, "RE_ENGAGEMENT"),
        (risk_level in {"Medium", "High"} or balance_change <= -25.0, "RM_CALLBACK"),
    ]

    actions = [action for supported, action in candidates if supported and action in APPROVED_ACTIONS]
    actions = list(dict.fromkeys(actions))[: MAX_ELIGIBLE_ACTIONS - 1]

    # Training never showed fewer than MIN_ELIGIBLE_ACTIONS, so pad with low-severity
    # options before falling through to MONITOR.
    for action in ("RE_ENGAGEMENT", "PRODUCT_REVIEW", "RM_CALLBACK"):
        if len(actions) >= MIN_ELIGIBLE_ACTIONS - 1:
            break
        if action not in actions:
            actions.append(action)

    # MONITOR always present and always last, so it is the deliberate fallback
    # rather than the first item a hesitant model reaches for.
    return actions + ["MONITOR"]


def build_devang_model2_input(
    customer: dict[str, Any],
    model1_output: dict[str, Any],
    extra_context: dict[str, Any] | None = None,
    case_id: str | None = None,
) -> dict[str, Any]:
    extra_context = extra_context or {}
    profile = extra_context.get("customer_profile") or {}

    # Resolved before action gating: the complaint text lives in extra_context, so
    # gating on customer["complaint_text"] alone meant text-driven actions
    # (FEE_WAIVER_REVIEW, CARD_REVIEW, LOAN_REVIEW) could never become eligible.
    complaint_text = extra_context.get("recent_complaint_text")
    if complaint_text is None:
        complaint_text = customer.get("complaint_text")

    eligible_actions = extra_context.get("eligible_actions") or default_eligible_actions(
        customer, model1_output, complaint_text=complaint_text
    )

    record = {
        "customer_context": {
            "age": int(number_or_default(profile.get("age", customer.get("age")), 0)),
            "tenure_months": int(number_or_default(profile.get("tenure_months", customer.get("tenure_months")), 0)),
            "customer_segment": str(profile.get("segment") or customer.get("customer_segment")),
            "income_regularity": str(profile.get("income_regularity") or customer.get("income_regularity")),
            "customer_yearly_value": float(
                number_or_default(profile.get("customer_yearly_value", customer.get("customer_yearly_value")), 0.0)
            ),
            "products_count": int(number_or_default(profile.get("products_count", customer.get("products_count")), 0)),
            "has_credit_card": int(number_or_default(profile.get("has_credit_card", customer.get("has_credit_card")), 0)),
            "has_loan": int(number_or_default(profile.get("has_loan", customer.get("has_loan")), 0)),
        },
        "behavior": {
            "days_since_last_transaction": int(number_or_default(customer.get("days_since_last_transaction"), 0)),
            "balance_change_30d": float(number_or_default(customer.get("balance_change_30d"), 0.0)),
            "transaction_change_30d": float(number_or_default(customer.get("transaction_change_30d"), 0.0)),
            "card_spend_change_30d": float(number_or_default(customer.get("card_spend_change_30d"), 0.0)),
            "app_login_change_30d": float(number_or_default(customer.get("app_login_change_30d"), 0.0)),
            "salary_missing_days": customer.get("salary_missing_days"),
            "external_transfer_change_30d": float(number_or_default(customer.get("external_transfer_change_30d"), 0.0)),
            "upi_share_of_spend": float(number_or_default(customer.get("upi_share_of_spend"), 0.0)),
            "fd_maturing_in_30d": int(number_or_default(customer.get("fd_maturing_in_30d"), 0)),
            "products_dropped_90d": int(number_or_default(customer.get("products_dropped_90d"), 0)),
            "emi_bounce_30d": int(number_or_default(customer.get("emi_bounce_30d"), 0)),
        },
        "service_evidence": {
            "complaints_30d": int(number_or_default(customer.get("complaints_30d"), 0)),
            "unresolved_complaints": int(number_or_default(customer.get("unresolved_complaints"), 0)),
            "failed_transactions_30d": int(number_or_default(customer.get("failed_transactions_30d"), 0)),
            "avg_resolution_time_hrs": float(number_or_default(customer.get("avg_resolution_time_hrs"), 0.0)),
            "complaint_text": complaint_text,
        },
        "model1": {
            "churn_probability": probability_0_to_1(churn_probability_for_model2(model1_output)),
            "churn_prediction": model1_output["churn_prediction"],
            "risk_level": model1_output["risk_level"],
            "top_risk_factors": [],
        },
        "eligible_actions": eligible_actions,
    }
    if record["behavior"]["salary_missing_days"] is not None:
        record["behavior"]["salary_missing_days"] = int(record["behavior"]["salary_missing_days"])

    # top_risk_factors indexes into the case, so it is resolved against the blocks
    # above rather than carrying Model 1's own engineered values.
    case_fields = {
        **record["customer_context"],
        **record["behavior"],
        **record["service_evidence"],
    }
    record["model1"]["top_risk_factors"] = devang_top_risk_factors(model1_output, case_fields)

    if case_id is not None:
        record["case_id"] = case_id

    errors = validate_model2_input(strip_case_id(record)[0])
    if errors:
        raise ValueError("Built invalid Devang Model 2 input: " + "; ".join(errors))
    return record


_EVIDENCE_ITEM = re.compile(r"^([a-z_0-9]+)\s*=\s*(.+)$")
_NULL_EVIDENCE_VALUES = {"0", "0.0", "0.00", "none", "null", "nan", ""}
_ACTION_PHRASES = {
    "COMPLAINT_ESCALATION": ("complaint escalation", "escalation", "escalate"),
    "SERVICE_RECOVERY": ("service recovery",),
    "FEE_WAIVER_REVIEW": ("fee waiver", "waiver"),
    "CARD_REVIEW": ("card review",),
    "LOAN_REVIEW": ("loan review",),
    "FINANCIAL_GUIDANCE": ("financial guidance",),
    "RM_CALLBACK": ("rm callback", "relationship manager call"),
    "PRODUCT_REVIEW": ("product review",),
    "RE_ENGAGEMENT": ("re-engagement", "reengagement"),
    "MONITOR": ("monitor",),
}


def coherence_errors(prediction: dict[str, Any], case_input: dict[str, Any]) -> list[str]:
    """Server-side checks for the prompt rules the fine-tune tends to slot-fill past.

    These feed the existing retry loop rather than the shared output validator, so
    the approved-value contract in src/schema stays the single source of truth.
    """
    errors: list[str] = []
    service = case_input.get("service_evidence") or {}
    fields = {
        **(case_input.get("customer_context") or {}),
        **(case_input.get("behavior") or {}),
        **service,
    }

    for item in prediction.get("evidence") or []:
        match = _EVIDENCE_ITEM.match(str(item).strip())
        if not match:
            continue
        field, value = match.group(1), match.group(2).strip().lower()
        if value in _NULL_EVIDENCE_VALUES:
            errors.append(f"evidence: '{item}' cites a zero/null value, which is not evidence; remove it")
        elif field in fields and fields[field] is None:
            errors.append(f"evidence: '{item}' cites a null field; remove it")

    has_service_evidence = (
        float(number_or_default(service.get("complaints_30d"), 0)) > 0
        or float(number_or_default(service.get("unresolved_complaints"), 0)) > 0
        or float(number_or_default(service.get("avg_resolution_time_hrs"), 0.0)) > 0
        or bool(service.get("complaint_text"))
    )
    if prediction.get("primary_reason") == "SERVICE_DISSATISFACTION" and not has_service_evidence:
        errors.append(
            "primary_reason: SERVICE_DISSATISFACTION requires a non-zero complaint signal, "
            "but complaints_30d, unresolved_complaints and avg_resolution_time_hrs are all 0 "
            "and complaint_text is null; choose the reason matching the behavior signals"
        )

    # NOTE: "risk_level High => urgency HIGH" is deliberately NOT enforced here. The
    # fine-tune has a strong prior against HIGH and simply re-emits MEDIUM, so guarding
    # it burned every retry and roughly doubled latency without changing an answer.
    # Left to the prompt; see the urgency-distribution note in the README.

    action = prediction.get("recommended_action")
    summary = str(prediction.get("reasoning_summary") or "").lower()
    named_others = [
        other
        for other, phrases in _ACTION_PHRASES.items()
        if other != action and any(phrase in summary for phrase in phrases)
    ]
    if named_others and not any(phrase in summary for phrase in _ACTION_PHRASES.get(action, ())):
        errors.append(
            f"reasoning_summary: describes {named_others[0]} but recommended_action is {action}; "
            "rewrite the summary around the action you chose"
        )

    return errors


def simple_output(result: dict[str, Any]) -> str:
    if not result["ok"] or not result.get("prediction"):
        return f"Prediction failed: {result.get('error')}"
    prediction = result["prediction"]
    return (
        f"Reason: {prediction['primary_reason']} | "
        f"Urgency: {prediction['urgency']} | "
        f"Action: {prediction['recommended_action']} | "
        f"Why: {prediction['reasoning_summary']}"
    )


def predict_one(record: dict[str, Any]) -> dict[str, Any]:
    started_at = time.perf_counter()
    case_input, case_id = strip_case_id(record)

    input_errors = validate_model2_input(case_input)
    if input_errors:
        raise ValueError("; ".join(input_errors))

    last_error = None
    raw_text = None
    parsed = None
    # Best schema-valid parse seen so far, kept so that a case which only ever trips
    # the softer coherence rules degrades to a flagged answer instead of no answer.
    fallback_parsed: dict[str, Any] | None = None
    fallback_warnings: list[str] = []
    for attempt in range(1, MAX_RETRIES + 1):
        user_payload = build_user_payload(case_input, last_error=last_error)

        response = ollama_post(
            "/api/chat",
            {
                "model": OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": devang_system_prompt()},
                    {"role": "user", "content": canonical_json(user_payload)},
                ],
                "format": output_json_schema(case_input["eligible_actions"]),
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "top_p": 0.9,
                    "repeat_penalty": 1.08,
                    "num_predict": 256,
                },
            },
        )
        raw_text = response.get("message", {}).get("content", "")
        try:
            parsed = extract_json_object(raw_text)
            schema_errors = validate_model2_output(parsed, eligible_actions=case_input["eligible_actions"])
            soft_errors = coherence_errors(parsed, case_input) if not schema_errors else []
            if not schema_errors and fallback_parsed is None:
                fallback_parsed, fallback_warnings = parsed, soft_errors
            if schema_errors or soft_errors:
                raise ValueError("; ".join(schema_errors + soft_errors))
            last_error = None
            break
        except Exception as exc:
            parsed = None
            last_error = str(exc)

    warnings: list[str] = []
    if last_error is not None and fallback_parsed is not None:
        # Schema-valid but never fully coherent: serve it, flagged.
        parsed = fallback_parsed
        warnings = fallback_warnings
        last_error = None

    output = {
        "case_id": case_id,
        "ok": last_error is None,
        "prediction": parsed,
        "warnings": warnings,
        "raw_text": raw_text,
        "error": last_error,
        "latency_s": round(time.perf_counter() - started_at, 4),
    }
    output["simple_output"] = simple_output(output)
    print(output["simple_output"])
    return output


def predict_payload(payload: Any) -> Any:
    if isinstance(payload, list):
        return [predict_one(record) for record in payload]
    if isinstance(payload, dict):
        return predict_one(payload)
    raise ValueError("Payload must be a JSON object or a JSON list of objects.")


async def read_upload_json(file: UploadFile) -> Any:
    content = await file.read()
    try:
        return json.loads(content.decode("utf-8"))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid JSON in {file.filename}: {exc}") from exc


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model1()
    require_ollama_model()
    print(f"Devang API ready. Model 1 v2 loaded. Ollama model: {OLLAMA_MODEL}")
    yield


app = FastAPI(title="Devang Model 2 API", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {
        "ok": True,
        "served_at": datetime.now().isoformat(timespec="seconds"),
        "ollama_host": OLLAMA_HOST,
        "ollama_model": OLLAMA_MODEL,
        "model1_loaded": model1_loaded(),
        "system_prompt": "Devang native prompt plus evidence, urgency, action and coherence rules",
        "native_system_prompt": SYSTEM_PROMPT,
        "decision_rules": DECISION_RULES,
        "max_eligible_actions": MAX_ELIGIBLE_ACTIONS,
        "max_top_risk_factors": MAX_TOP_RISK_FACTORS,
        "use_raw_churn_probability": USE_RAW_CHURN_PROBABILITY,
        "output_schema_keys": output_json_schema()["required"],
    }


@app.post("/predict/model1")
def api_predict_model1(request: Model1Request):
    try:
        return {"model1": model1_server.predict_model1(request)}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict/model2")
def api_predict_model2(request: Model2Request):
    try:
        return {"model2": predict_one(request.payload)}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict/both")
def api_predict_both(request: BothRequest):
    started_at = time.perf_counter()
    try:
        model1_started = time.perf_counter()
        model1_output = model1_server.predict_model1(request)
        model1_ms = round((time.perf_counter() - model1_started) * 1000, 2)

        customer = model1_server.latest_customer_from_request(request)
        case_id = request.customer_id
        model2_input = build_devang_model2_input(
            customer=customer,
            model1_output=model1_output,
            extra_context=request.extra_context,
            case_id=case_id,
        )

        model2_started = time.perf_counter()
        model2_output = predict_one(model2_input)
        model2_ms = round((time.perf_counter() - model2_started) * 1000, 2)

        return {
            "meta": {
                "endpoint": "/predict/both",
                "served_at": datetime.now().isoformat(timespec="seconds"),
                "elapsed_ms": round((time.perf_counter() - started_at) * 1000, 2),
                "timings_ms": {"model1": model1_ms, "model2": model2_ms},
                "customer_id": request.customer_id,
                "customer_name": request.customer_name,
                "snapshot_date": request.snapshot_date or request.prediction_date,
            },
            "model1": model1_output,
            "model2_input": model2_input,
            "model2": model2_output,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict/batch")
def api_predict_batch(request: BatchModel2Request):
    try:
        return {"model2": [predict_one(payload) for payload in request.payloads]}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict-json")
def api_predict_json(payload: Any = Body(...)):
    try:
        return predict_payload(payload)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict-file")
async def api_predict_file(file: UploadFile = File(...)):
    payload = await read_upload_json(file)
    try:
        return {"file_name": file.filename, "result": predict_payload(payload)}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict-files")
async def api_predict_files(files: list[UploadFile] = File(...)):
    results = []
    for file in files:
        payload = await read_upload_json(file)
        try:
            results.append({"file_name": file.filename, "result": predict_payload(payload)})
        except Exception as exc:
            results.append({"file_name": file.filename, "error": str(exc)})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
