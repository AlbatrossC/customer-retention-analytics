# Model 2 — Evaluation Results

All numbers in this document are sourced directly from the refinement notebook
(`notebooks/model2_refinement_fresh_runtime_final.ipynb`). Each section clearly
states whether the evaluation was **executed** in the notebook or **reused**
from a prior run, and whether the result covers the full evaluation set or a
subset.

---

## 1. V1 (checkpoint-145) — 499-Case Test Set

**Source**: Reused from a prior evaluation run. These metrics were loaded as
hard-coded values in Cell 6 of the notebook (not re-executed).

| Metric | Value |
|---|---|
| num_test_cases | 499 |
| json_valid_rate | 0.9920 |
| primary_reason_exact_match | 0.8557 |
| recommended_action_exact_match | 0.8918 |
| urgency_exact_match | 0.8697 |
| invalid_unapproved_action_rate | 0.0000 |
| mean_latency_s | 17.71 |
| median_latency_s | 18.17 |
| p95_latency_s | 20.22 |

---

## 2. V1 (checkpoint-145) — Full 466-Case Validation Set

**Source**: Loaded from a pre-computed results file
(`model2_validation_466_results.jsonl`), not re-executed in the notebook.

### Overall

| Metric | Value |
|---|---|
| schema_valid_rate | 0.9957 |
| reason accuracy | 0.8562 |
| action accuracy | 0.8884 |
| urgency accuracy | 0.8970 |

### By Risk Level

| Risk Level | n | Reason Accuracy | Action Accuracy | Urgency Accuracy |
|---|---|---|---|---|
| Low | 247 | 0.7814 | 0.8259 | 0.8826 |
| Medium | 87 | 0.9310 | 0.9310 | 0.9195 |
| High | 132 | 0.9470 | 0.9773 | 0.9091 |

---

## 3. V1 vs V2 — 100-Case Stratified Validation Screening

**Source**: Fresh V2 inference was executed on 100 of the 466 validation cases
(stratified sample). V1 results for the same 100 cases were reused from the
pre-computed results file.

**Important**: This is a 100-case screening subset, NOT the full 466-case
validation. The remaining 366 validation cases were never run against V2.

| Metric | V1 (checkpoint-145) | V2 (model2_v2_finetuned) |
|---|---|---|
| Reason accuracy | 0.82 | 0.84 |
| Action accuracy | 0.85 | 0.85 |
| Urgency accuracy | 0.78 | 0.81 |
| JSON valid rate | 0.98 | 1.00 |
| Invalid action rate | 0.02 | 0.00 |

**Case-level changes**: 25 of 100 cases changed between V1 and V2:
- 12 improvements
- 8 regressions
- 5 neutral changes

---

## 4. Full 466-Case V2 Validation

Not evaluated in the current run.

---

## 5. 499-Case V2 Test Evaluation

Not evaluated in the current run.

---

## Notes

- The 100-case V1-vs-V2 screening is a preliminary directional signal, not a
  full validation. Drawing strong conclusions from n=100 is not appropriate.
- Complete V2 validation (full 466-case set) and V2 test evaluation (499-case
  set) remain to be executed before V2 can be considered fully benchmarked.
- All V1 metrics above come from checkpoint-145 (the V1 LoRA adapter on
  Qwen2.5-3B-Instruct), not from the raw base model.
