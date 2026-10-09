# Power BI Dashboard Specification

**Status:** Design specification only; no .pbix file or observed KPIs.

## Input tables
1. `test_predictions.csv`: timestamp, actual_kw, pred_persistence_kw, pred_random_forest_kw, pred_gradient_boosting_kw
2. `model_metrics.csv`: model, mae_kw, rmse_kw

Both files are created by `python -m src.forecast` after processing a real dataset.

## Suggested report pages
### 1. Executive Overview
- Dataset provenance, site, period, units and forecast horizon.
- KPI cards: baseline MAE/RMSE and model MAE/RMSE, populated only from outputs.
- Bar chart comparing errors by model.
- Caveat: lower forecasting error does not establish cost savings.

### 2. Forecast Performance
- Time-series line chart: actual power vs each model prediction.
- Date/time slicer.
- Error by hour-of-day and month after transforming the predictions into long format.
- Table of largest absolute forecast errors with timestamps.

### 3. Managerial Interpretation
- Opportunities: scheduling, anomaly triage, staffing and monitoring.
- Barriers: data completeness, model maintenance, integration and change management.
- Implementation decision matrix: feasibility, cost, governance and potential value.

## Example DAX (after importing test_predictions)
```dax
Actual Power (kW) = SUM(test_predictions[actual_kw])
RF Absolute Error (kW) =
SUMX(test_predictions, ABS(test_predictions[actual_kw] - test_predictions[pred_random_forest_kw]))
RF MAE (kW) =
DIVIDE([RF Absolute Error (kW)], COUNTROWS(test_predictions))
```

## Data quality checks
Confirm timestamp type, time zone, units, duplicates, blank rows and whether the dataset represents power (kW) or energy (kWh). Avoid summing power values as if they were energy. Document sample interval before deriving energy estimates.

## Publication policy
Do not add screenshots or KPI values until an actual dashboard has been built from real predictions.
