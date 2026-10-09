"""Tests using generated fixture values; these are not research results."""
import numpy as np
import pandas as pd
import pytest

from src.forecast import evaluate, load_and_validate, make_features


def test_feature_lags_are_past_only():
    timestamps = pd.date_range("2024-01-01", periods=250, freq="h", tz="UTC")
    data = pd.DataFrame({"timestamp": timestamps, "power_kw": np.arange(250, dtype=float)})
    features = make_features(data)
    assert features.iloc[0]["lag_1"] == 23.0
    assert features.iloc[0]["lag_24"] == 0.0
    assert features.iloc[0]["power_kw"] == 24.0


def test_evaluate_writes_expected_files(tmp_path):
    timestamps = pd.date_range("2024-01-01", periods=250, freq="h", tz="UTC")
    frame = pd.DataFrame({"timestamp": timestamps, "power_kw": np.abs(np.sin(np.arange(250) / 8)) * 10})
    result = evaluate(frame, tmp_path)
    assert set(result["model"]) == {"persistence", "random_forest", "gradient_boosting"}
    assert (tmp_path / "test_predictions.csv").exists()
    assert (result["mae_kw"] >= 0).all()


def test_missing_time_step_rejected(tmp_path):
    timestamps = pd.date_range("2024-01-01", periods=250, freq="h", tz="UTC").delete(4)
    path = tmp_path / "gap.csv"
    pd.DataFrame({"timestamp": timestamps, "power_kw": np.ones(len(timestamps))}).to_csv(path, index=False)
    with pytest.raises(ValueError, match="regularly spaced"):
        load_and_validate(path)
