import pandas as pd
import pytest
from scripts.prepare_pvdaq import normalize


def test_normalize_power_units(tmp_path):
    raw = tmp_path / "raw.csv"
    pd.DataFrame({
        "utc_measured_on": pd.date_range("2024-01-01", periods=3, freq="h", tz="UTC"),
        "metric_id": [42, 42, 42],
        "value": [1000, 2000, 3000],
    }).to_csv(raw, index=False)
    result = normalize(raw, tmp_path / "processed.csv", "utc_measured_on",
                       "value", "W", "metric_id", "42")
    assert result["power_kw"].tolist() == [1, 2, 3]


def test_irregular_timestamps_rejected(tmp_path):
    raw = tmp_path / "raw.csv"
    pd.DataFrame({
        "time": ["2024-01-01T00:00:00Z", "2024-01-01T01:00:00Z",
                 "2024-01-01T03:00:00Z"],
        "power": [1, 2, 3],
    }).to_csv(raw, index=False)
    with pytest.raises(ValueError, match="Irregular"):
        normalize(raw, tmp_path / "out.csv", "time", "power", "kW")
