"""Normalize an inspected PVDAQ CSV to timestamp,power_kw.

Requires explicit raw column names and a VERIFIED power unit conversion.
The script will not guess which metric_id represents power.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd


def normalize(source: Path, destination: Path, timestamp_col: str,
              power_col: str, unit: str, metric_col: str | None = None,
              metric_id: str | None = None) -> pd.DataFrame:
    frame = pd.read_csv(source)
    for col in [timestamp_col, power_col]:
        if col not in frame:
            raise ValueError(f"Missing source column: {col}")
    if (metric_col is None) != (metric_id is None):
        raise ValueError("Specify both --metric-column and --metric-id, or neither")
    if metric_col:
        if metric_col not in frame:
            raise ValueError(f"Missing metric column: {metric_col}")
        frame = frame[frame[metric_col].astype(str) == metric_id].copy()
    if frame.empty:
        raise ValueError("No records after metric filtering")
    times = pd.to_datetime(frame[timestamp_col], utc=True, errors="raise")
    values = pd.to_numeric(frame[power_col], errors="raise")
    factor = {"W": 0.001, "kW": 1.0, "MW": 1000.0}[unit]
    output = pd.DataFrame({"timestamp": times, "power_kw": values * factor})
    if output.isna().any().any():
        raise ValueError("Missing values require explicit quality handling")
    if output["timestamp"].duplicated().any():
        raise ValueError("Duplicate timestamps: inspect source and DST")
    output = output.sort_values("timestamp").reset_index(drop=True)
    if (output["power_kw"] < 0).any():
        raise ValueError("Negative readings: investigate before use")
    if output["timestamp"].diff().dropna().nunique() != 1:
        raise ValueError("Irregular sampling/gaps: resolve explicitly before forecasting")
    destination.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(destination, index=False)
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", default=Path("data/processed/solar_power.csv"), type=Path)
    parser.add_argument("--timestamp-column", required=True)
    parser.add_argument("--power-column", required=True)
    parser.add_argument("--power-unit", required=True, choices=["W", "kW", "MW"])
    parser.add_argument("--metric-column")
    parser.add_argument("--metric-id")
    args = parser.parse_args()
    data = normalize(args.input, args.output, args.timestamp_column, args.power_column,
                     args.power_unit, args.metric_column, args.metric_id)
    print(f"Saved {len(data)} validated observations to {args.output}")


if __name__ == "__main__":
    main()
