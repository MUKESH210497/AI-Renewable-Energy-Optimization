"""Leakage-aware one-step-ahead solar power forecasting.

Input CSV must contain timestamp (ISO-8601) and power_kw (numeric).
The script is implemented, but not run on a real PVDAQ site in this repository.
No trained models or metrics are bundled.
"""
from __future__ import annotations
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

FEATURES = ["lag_1", "lag_2", "lag_24", "hour_sin", "hour_cos", "dayofyear_sin", "dayofyear_cos"]


def load_and_validate(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    required = {"timestamp", "power_kw"}
    if not required.issubset(frame.columns):
        raise ValueError(f"Required columns: {sorted(required)}")
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], utc=True, errors="raise")
    frame["power_kw"] = pd.to_numeric(frame["power_kw"], errors="raise")
    if frame[["timestamp", "power_kw"]].isna().any().any():
        raise ValueError("Null timestamps or power values must be resolved before training")
    frame = frame.sort_values("timestamp").reset_index(drop=True)
    if frame["timestamp"].duplicated().any():
        raise ValueError("Duplicate timestamps detected")
    if len(frame) < 200:
        raise ValueError("At least 200 observations required for this starter example")
    delta = frame["timestamp"].diff().dropna()
    if delta.nunique() != 1:
        raise ValueError("Expected a regularly spaced time series; handle gaps before modeling")
    if (frame["power_kw"] < 0).any():
        raise ValueError("Negative power readings found; inspect units and quality flags")
    return frame


def make_features(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.copy()
    for lag in (1, 2, 24):
        result[f"lag_{lag}"] = result["power_kw"].shift(lag)
    # Calendar features refer to the timestamp being predicted and are known in advance.
    hour = result["timestamp"].dt.hour + result["timestamp"].dt.minute / 60
    doy = result["timestamp"].dt.dayofyear
    result["hour_sin"] = np.sin(2 * np.pi * hour / 24)
    result["hour_cos"] = np.cos(2 * np.pi * hour / 24)
    result["dayofyear_sin"] = np.sin(2 * np.pi * doy / 366)
    result["dayofyear_cos"] = np.cos(2 * np.pi * doy / 366)
    return result.dropna(subset=FEATURES).reset_index(drop=True)


def metrics(y, pred):
    return {
        "mae_kw": float(mean_absolute_error(y, pred)),
        "rmse_kw": float(np.sqrt(mean_squared_error(y, pred))),
    }


def evaluate(frame: pd.DataFrame, output: Path) -> pd.DataFrame:
    data = make_features(frame)
    n = len(data)
    train_end, valid_end = int(n * 0.7), int(n * 0.85)
    if train_end < 50 or valid_end <= train_end or valid_end >= n:
        raise ValueError("Insufficient observations after feature construction")
    train = data.iloc[:train_end]
    validation = data.iloc[train_end:valid_end]
    test = data.iloc[valid_end:]
    # Validation is reserved for future model selection. No test-set tuning.
    _ = validation
    predictions = {"persistence": test["lag_1"].to_numpy()}
    models = {
        "random_forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
        "gradient_boosting": GradientBoostingRegressor(random_state=42),
    }
    for name, model in models.items():
        model.fit(train[FEATURES], train["power_kw"])
        predictions[name] = model.predict(test[FEATURES])
    rows = []
    output.mkdir(parents=True, exist_ok=True)
    forecast = pd.DataFrame({"timestamp": test["timestamp"], "actual_kw": test["power_kw"]})
    for name, values in predictions.items():
        forecast[f"pred_{name}_kw"] = values
        rows.append({"model": name, **metrics(test["power_kw"], values)})
    summary = pd.DataFrame(rows)
    summary.to_csv(output / "model_metrics.csv", index=False)
    forecast.to_csv(output / "test_predictions.csv", index=False)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path, help="Normalized real CSV")
    parser.add_argument("--output", default=Path("outputs"), type=Path)
    args = parser.parse_args()
    result = evaluate(load_and_validate(args.input), args.output)
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
