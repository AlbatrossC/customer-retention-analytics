"""
Model 2 configuration — single source of truth for all constants.

All approved value lists, model identifiers, paths, and the system prompt
are defined here. Import from this module rather than hard-coding values
elsewhere.
"""

from pathlib import Path
from typing import List, Set

# ---------------------------------------------------------------------------
# Paths (relative to repo root)
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[2]

# V2 LoRA adapter location.
# Option A: local directory under model/ (if using Git LFS or after download).
# Option B: Hugging Face Hub repo id (preferred for lightweight Git).
# Update ADAPTER_PATH to match your chosen strategy — see README §12.
ADAPTER_PATH: str = str(REPO_ROOT / "model" / "model2_v2_finetuned")

# ---------------------------------------------------------------------------
# Base model
# ---------------------------------------------------------------------------
BASE_MODEL_ID: str = "Qwen/Qwen2.5-3B-Instruct"

# ---------------------------------------------------------------------------
# System prompt — used verbatim in training; must match exactly at inference
# ---------------------------------------------------------------------------
SYSTEM_PROMPT: str = (
    "You are a banking retention analyst. Given a customer retention case, "
    "identify the most supported reason for risk, cite evidence, assign urgency, "
    "and select exactly one eligible retention action."
)

# ---------------------------------------------------------------------------
# Approved value lists
# ---------------------------------------------------------------------------
APPROVED_REASONS: List[str] = [
    "SERVICE_DISSATISFACTION",
    "COMPETITOR_MIGRATION",
    "FEE_DISSATISFACTION",
    "LOW_ENGAGEMENT",
    "PRODUCT_MISMATCH",
    "DIGITAL_FRICTION",
    "FINANCIAL_STRESS",
    "LIFE_STAGE_CHANGE",
    "TEMPORARY_SEASONAL_CHANGE",
    "UNKNOWN",
]
APPROVED_REASONS_SET: Set[str] = set(APPROVED_REASONS)

APPROVED_ACTIONS: List[str] = [
    "MONITOR",
    "SERVICE_RECOVERY",
    "COMPLAINT_ESCALATION",
    "FEE_WAIVER_REVIEW",
    "RM_CALLBACK",
    "PRODUCT_REVIEW",
    "CARD_REVIEW",
    "LOAN_REVIEW",
    "RE_ENGAGEMENT",
    "FINANCIAL_GUIDANCE",
]
APPROVED_ACTIONS_SET: Set[str] = set(APPROVED_ACTIONS)

APPROVED_URGENCY: List[str] = ["LOW", "MEDIUM", "HIGH"]
APPROVED_URGENCY_SET: Set[str] = set(APPROVED_URGENCY)

# Low-confidence fallback triple — the model falls back to this when it
# cannot determine a clear reason.  The notebook tracks its rate explicitly.
FALLBACK_TRIPLE = ("UNKNOWN", "MEDIUM", "MONITOR")

# ---------------------------------------------------------------------------
# Inference defaults
# ---------------------------------------------------------------------------
DEFAULT_MAX_NEW_TOKENS: int = 256
DEFAULT_MAX_LENGTH: int = 640

# ---------------------------------------------------------------------------
# V2 LoRA adapter metadata (from adapter_config.json — do not alter)
# ---------------------------------------------------------------------------
V2_LORA_CONFIG = {
    "base_model_name_or_path": BASE_MODEL_ID,
    "peft_type": "LORA",
    "r": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.05,
    "bias": "none",
    "target_modules": [
        "down_proj",
        "q_proj",
        "k_proj",
        "up_proj",
        "o_proj",
        "v_proj",
        "gate_proj",
    ],
    "task_type": "CAUSAL_LM",
}

# ---------------------------------------------------------------------------
# Customer segment and risk level enums (for input validation)
# ---------------------------------------------------------------------------
VALID_CUSTOMER_SEGMENTS = {"salary", "pension", "farmer", "vendor", "business"}
VALID_INCOME_REGULARITY = {"regular", "irregular", "seasonal"}
VALID_RISK_LEVELS = {"Low", "Medium", "High"}
VALID_CHURN_PREDICTIONS = {"Yes", "No"}
