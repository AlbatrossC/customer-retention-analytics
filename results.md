# Model Results

The dataset was not changed.

Tested four models:

- XGBoost old
- XGBoost calibrated
- LightGBM model 1
- LightGBM model 2

## Simple Answer

The old XGBoost model is not good for probability display. It is too confident.

The three calibrated models are healthier.

Best practical choices:

1. XGBoost calibrated
2. LightGBM model 2

## Fit Check

| Model | Status | Why | Train ROC | Val ROC | Test ROC | Train PR | Val PR | Test PR |
|---|---|---|---:|---:|---:|---:|---:|---:|
| XGBoost old | Healthy | Train and test are close enough. | 0.8611 | 0.8305 | 0.8379 | 0.5043 | 0.4911 | 0.4633 |
| XGBoost calibrated | Healthy | Train and test are close enough. | 0.8593 | 0.8370 | 0.8332 | 0.5134 | 0.4885 | 0.4473 |
| LightGBM model 1 | Healthy | Train and test are close enough. | 0.8681 | 0.8380 | 0.8289 | 0.5361 | 0.4880 | 0.4426 |
| LightGBM model 2 | Healthy | Train and test are close enough. | 0.8540 | 0.8398 | 0.8301 | 0.5134 | 0.4887 | 0.4426 |

## Test Set Results

| Model | Precision | Recall | Flagged Rows | Mean Probability | Confusion Matrix |
|---|---:|---:|---:|---:|---|
| XGBoost old | 0.3398 | 0.6205 | 871 | 0.3229 | [[6869, 575], [181, 296]] |
| XGBoost calibrated | 0.3843 | 0.5954 | 739 | 0.0570 | [[6989, 455], [193, 284]] |
| LightGBM model 1 | 0.3961 | 0.5996 | 722 | 0.0571 | [[7008, 436], [191, 286]] |
| LightGBM model 2 | 0.4102 | 0.5891 | 685 | 0.0571 | [[7040, 404], [196, 281]] |

## Example Tests

| Example | Expected | XGBoost old | XGBoost calibrated | LightGBM 1 | LightGBM 2 |
|---|---|---:|---:|---:|---:|
| Healthy salary customer | Very low risk | 14.31% | 1.96% | 1.89% | 1.91% |
| Salary customer going quiet | Medium risk | 83.81% | 18.06% | 16.67% | 21.97% |
| Complaint-heavy customer | Medium to high risk | 85.51% | 20.69% | 19.13% | 21.97% |
| Everything going wrong | Highest risk | 99.13% | 100.00% | 100.00% | 100.00% |
| Farmer with no salary field | Should not crash; NaN salary is valid | 43.57% | 4.11% | 4.23% | 3.58% |
| Pension FD maturity | Moderate risk | 27.86% | 2.39% | 1.98% | 1.91% |
| Vendor with failed payments | Service risk | 62.81% | 8.16% | 9.15% | 8.26% |
| Improving after complaint | Low risk | 16.51% | 1.96% | 1.89% | 1.91% |

## Example Predictions

| Example | XGBoost old | XGBoost calibrated | LightGBM 1 | LightGBM 2 |
|---|---|---|---|---|
| Healthy salary customer | No / Medium | No / Low | No / Low | No / Low |
| Salary customer going quiet | Yes / High | Yes / Medium | Yes / Medium | Yes / High |
| Complaint-heavy customer | Yes / High | Yes / High | Yes / Medium | Yes / High |
| Everything going wrong | Yes / High | Yes / High | Yes / High | Yes / High |
| Farmer with no salary field | No / High | No / Low | No / Low | No / Low |
| Pension FD maturity | No / High | No / Low | No / Low | No / Low |
| Vendor with failed payments | No / High | No / Low | No / Low | No / Low |
| Improving after complaint | No / Medium | No / Low | No / Low | No / Low |

## Plain Meaning

Overfitting means train score is much higher than test score.

Underfitting means both train and test scores are weak.

Healthy means train, validation, and test are close, and test ROC/PR are in the expected range.

In these results, the calibrated models look healthy. The old XGBoost model ranks customers fairly well, but its probabilities are too high.
