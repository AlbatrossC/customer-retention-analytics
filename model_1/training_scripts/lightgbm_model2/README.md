# LightGBM Model 2

Stronger LightGBM training script for Model 1 churn prediction.

It uses the existing dataset only. It does not edit, regenerate, rebalance, or resample the data.

## Install Check

LightGBM is already installed in this environment.

To verify:

```powershell
python -c "import lightgbm; print(lightgbm.__version__)"
```

## Train

Run from the repository root:

```powershell
python model_1\training_scripts\lightgbm_model2\train_lightgbm.py
```

This uses the full strategy:

- customer-level split
- native categorical features
- no `scale_pos_weight`
- multiple LightGBM candidates
- early stopping on validation PR-AUC
- probability adjustment on validation only
- threshold sweep
- permutation importance on test with 10 repeats
- branch/card decoy checks

## Faster Test Run

Use this only when you want a quicker local check:

```powershell
python model_1\training_scripts\lightgbm_model2\train_lightgbm.py --permutation-repeats 3
```

## Predict

After training:

```powershell
python model_1\training_scripts\lightgbm_model2\test_prediction.py
```

## Artifacts

Training writes:

```text
model_1/training_scripts/lightgbm_model2/artifacts/
```
