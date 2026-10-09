# Reproducible Forecasting Workflow

The executable starter implementation lives in `src/forecast.py`. This avoids committing a notebook containing unverified output.

## Setup
```bash
python -m venv .venv
# Activate .venv for your operating system
pip install -r requirements.txt
pytest -q
```

## Data preparation
Download a real, licensed PVDAQ site dataset. Inspect timestamps, measurement units, data frequency, missing values and site metadata. Normalize the CSV to columns `timestamp,power_kw` with a regularly spaced UTC timestamp.

## Execute
```bash
python -m src.forecast --input data/processed/solar_power.csv --output outputs
```

## Output
- `outputs/model_metrics.csv`: model, MAE in kW, RMSE in kW
- `outputs/test_predictions.csv`: timestamp, actual kW, predictions from each model

These files are generated only after running on real data; none are supplied as results.

## Methodological cautions
The starter script assumes one-step-ahead forecasts and regular intervals. `lag_24` means 24 *observations*, not necessarily 24 hours. For 15-minute measurements it represents six hours. The fixed 70/15/15 chronological partitions are a demonstration; validation data is currently held out but not used for tuning. Test performance should not guide hyperparameter changes. Avoid leakage from target-time weather measurements.
