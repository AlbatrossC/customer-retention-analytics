# Model 2 Fine-Tuning Dataset

The model-training details, LoRA configuration, persisted training metrics, and evaluation methodology are documented in [README.md](README.md).

> **At a glance**
> 
> **1,000** synthetic records | **80/20** individual-to-cohort mix | **5** allowed actions | **802/99/99** train-validation-test split

This dataset is designed for fine-tuning a banking customer-retention assistant that explains churn risk and recommends retention actions based on structured customer and cohort context.

## Dataset overview

The dataset contains 1,000 synthetic examples built from a retained source corpus and a balanced synthetic extension. It is intended for a hackathon-style fine-tuning task and should not be treated as real banking data.

## Files

- `model2_finetune_1000.jsonl` — complete 1,000-example master dataset
- `model2_train.jsonl` — 802-example training split
- `model2_validation.jsonl` — 99-example validation split
- `model2_test.jsonl` — 99-example held-out test split

The split sizes sum to the full corpus: $802 + 99 + 99 = 1{,}000$ records.

## Composition

- Total records: 1,000
- Individual records: 800 (80%)
- Cohort records: 200 (20%)

The final corpus preserves the original type-specific risk-group proportions while extending the dataset with synthetic examples that vary feature combinations, risk groups, trends, complaints, and retention actions.

### Overall risk groups

- `behaviour_problem`: 380
- `service_problem`: 224
- `both`: 172
- `neither`: 224

All five permitted action prefixes occur in the master dataset. Across the records, there are 1,658 recommended actions and an average of 4.33 explanation items per record. These counts describe the synthetic labels, not model predictions.

### Individual and cohort statistics

The dataset deliberately combines two decision contexts. Individual records describe one customer, while cohort records summarize a group with shared characteristics. Risk-group counts are record counts, not the number of customers inside each cohort.

| Record type | Records | Share | Size range | Average size | Main purpose |
| --- | ---: | ---: | ---: | ---: | --- |
| Individual | 800 | 80% | 1 | 1 | Customer-level retention decision |
| Cohort | 200 | 20% | 8–299 | 40.14 | Segment-level pattern and intervention |

| Record type | `behaviour_problem` | `service_problem` | `both` | `neither` |
| --- | ---: | ---: | ---: | ---: |
| Individual | 320 | 200 | 160 | 120 |
| Cohort | 60 | 24 | 12 | 104 |

**Individual records** are dominated by behavior-related risk: 320 records, or 40%, are labeled `behaviour_problem`; 200 (25%) are `service_problem`; 160 (20%) combine both; and 120 (15%) are `neither`.

**Cohort records** are mostly low-risk or neutral: 104 records (52%) are `neither`, 60 (30%) are `behaviour_problem`, 24 (12%) are `service_problem`, and 12 (6%) contain both risk types. Cohort sizes range from 8 to 299 members, with an average of 40.14 members.

These proportions mean the model must learn both fine-grained customer reasoning and aggregate reasoning. A cohort response should describe a shared pattern and recommend a group-level action; it should not invent a customer-specific explanation.

## Complete record representation

Each JSONL row contains a conversation-style record with a system prompt, a user payload, and an assistant response.

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "<structured Model 1 + customer/cohort context>"},
    {"role": "assistant", "content": "<JSON why + next_actions>"}
  ]
}
```

The `content` values are strings. The user and assistant strings contain serialized JSON, so a loader must parse the outer JSONL row first and then parse the `content` of the user and assistant messages.

### Shared fields

Every user payload contains:

| Field | Type | Meaning |
| --- | --- | --- |
| `type` | string | Either `individual` or `cohort` |
| `model1_output` | object | Upstream churn prediction and risk signals |
| `risk_group` | string | Training label: `behaviour_problem`, `service_problem`, `both`, or `neither` |

`model1_output` contains different values by record type:

| Record type | Parameters |
| --- | --- |
| Individual | `churn_probability`, `risk_tier`, `top_risk_drivers[]` |
| Cohort | `avg_churn_probability`, `shared_risk_drivers[]` |

For an individual, each `top_risk_drivers` item contains `feature`, `badness_score`, and `direction`. The direction indicates whether the feature increases or decreases risk.

### Individual payload parameters

| Object | Parameters | Meaning |
| --- | --- | --- |
| `customer_profile` | `segment`, `income_regularity`, `tenure_months`, `age`, `products_count`, `has_credit_card`, `has_loan`, `value_tier` | Static customer and relationship characteristics |
| `current_snapshot` | `days_since_last_transaction`, `balance_change_30d`, `transaction_change_30d`, `card_spend_change_30d`, `app_login_change_30d`, `salary_missing_days`, `external_transfer_change_30d`, `upi_share_of_spend`, `fd_maturing_in_30d`, `products_dropped_90d`, `complaints_30d`, `unresolved_complaints`, `failed_transactions_30d`, `avg_resolution_time_hrs`, `emi_bounce_30d` | Current activity, product, service, and risk signals |
| `trend_last_3_months` | `days_since_last_transaction[]`, `balance_change_30d[]`, `external_transfer_change_30d[]`, `complaints_30d[]`, `overall_direction` | Three monthly observations and overall direction |
| `recent_complaint_text` | string or `null` | Recent complaint narrative when available |

Example individual user payload:

```json
{
  "type": "individual",
  "model1_output": {
    "churn_probability": 0.274,
    "risk_tier": "medium",
    "top_risk_drivers": [
      {"feature": "fd_maturing_in_30d", "badness_score": 1.0, "direction": "increases_risk"}
    ]
  },
  "customer_profile": {"segment": "farmer", "tenure_months": 116, "value_tier": "medium"},
  "current_snapshot": {"days_since_last_transaction": 7, "complaints_30d": 0, "fd_maturing_in_30d": 1},
  "trend_last_3_months": {"overall_direction": "declining"},
  "recent_complaint_text": null,
  "risk_group": "behaviour_problem"
}
```

The example is abbreviated for readability; the complete files retain every parameter listed in the table.

### Cohort payload parameters

| Object | Parameters | Meaning |
| --- | --- | --- |
| `cohort_size` | integer | Number of customers represented by the cohort |
| `segment_profile` | `customer_segment`, `tenure_band`, `value_tier`, `products_band` | Shared segment and relationship bands |
| `aggregate_behaviour` | `avg_days_since_last_transaction`, `avg_balance_change_30d`, `avg_external_transfer_change_30d`, `pct_with_complaints`, `pct_fd_maturing_30d`, `pct_unresolved_complaints` | Group-level averages and proportions |
| `dominant_trend` | string | Overall cohort direction, such as `improving` or `declining` |
| `model1_output` | `avg_churn_probability`, `shared_risk_drivers[]` | Aggregated upstream risk signal |

Example cohort user payload:

```json
{
  "type": "cohort",
  "cohort_size": 31,
  "model1_output": {"avg_churn_probability": 0.141, "shared_risk_drivers": ["complaints_30d"]},
  "segment_profile": {"customer_segment": "business", "tenure_band": "3-7 years", "value_tier": "medium", "products_band": "2-3"},
  "aggregate_behaviour": {"avg_days_since_last_transaction": 2.1, "pct_with_complaints": 0.23, "pct_unresolved_complaints": 0.0},
  "dominant_trend": "improving",
  "risk_group": "neither"
}
```

The system prompt instructs the model to:

- act as a banking customer-retention decision assistant
- explain the strongest evidence behind churn risk
- recommend practical retention actions
- use only information provided in the input
- preserve numeric facts exactly
- avoid inventing unsupported customer or product details
- return JSON only

The assistant `content` is serialized JSON with two fields:

| Field | Type | Expected content |
| --- | --- | --- |
| `why` | array of strings | Evidence-based explanation, normally 3–5 concise items |
| `next_actions` | array of strings | 1–3 actions formatted as `prefix: instruction` |

## Removed metadata

The following metadata fields were removed from the source records:

- `customer_id`
- `cohort_id`
- `snapshot_date`
- `_paraphrased`
- `_paraphrase_failure_reason`

## Allowed action prefixes

The assistant output should use only these action prefixes:

- `rm_call`
- `rate_offer`
- `fee_waiver`
- `complaint_escalation`
- `do_nothing`

## Output expectations

For individual records, the model is expected to return JSON with:

- `why`: 3–5 concise reasons explaining the churn risk
- `next_actions`: 1–3 actions using the allowed prefixes

For cohort records, the model is expected to:

- explain the shared pattern affecting the cohort
- provide 1–3 cohort-level actions using the same action prefixes

## Recommended usage

1. Train using `model2_train.jsonl`
2. Validate during fine-tuning using `model2_validation.jsonl`
3. Keep `model2_test.jsonl` untouched until final evaluation

## Suggested evaluation

Compare the base model and the fine-tuned model on the 99 held-out test examples across these criteria:

1. JSON validity
2. Correct use of supplied numbers and facts
3. Relevance of the `why` explanations
4. Appropriateness of retention actions
5. Reduction of hallucination and unsupported claims
6. Correct handling of individual vs. cohort scenarios

## Important note

This is synthetic data created for a project and hackathon demonstration. It should not be used as real banking data or as the basis for real customer decisions.
