"""Descriptive survey analysis; requires genuine anonymized survey responses.

Input CSV column names expected:
consent, direct_sector_experience, ai_usage_frequency, efficiency_rating,
decision_rating, data_readiness_rating, cost_barrier_rating, skills_rating

No real responses or statistics are included in the repository.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

FIELDS = [
    "ai_usage_frequency", "efficiency_rating", "decision_rating",
    "data_readiness_rating", "cost_barrier_rating", "skills_rating"
]


def analyze(path: Path, output: Path) -> None:
    df = pd.read_csv(path)
    required = {"consent", "direct_sector_experience", *FIELDS}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df[df["consent"].astype(str).str.strip().str.lower().isin(["yes", "true", "1"])].copy()
    if df.empty:
        raise ValueError("No consenting responses")
    output.mkdir(parents=True, exist_ok=True)
    counts = df.groupby("direct_sector_experience", dropna=False).size().rename("count")
    counts.to_csv(output / "respondent_groups.csv")
    for field in FIELDS:
        df[field] = pd.to_numeric(df[field], errors="coerce")
    summary = df[FIELDS].agg(["count", "median", "mean"]).T
    summary.to_csv(output / "descriptive_summary.csv")
    for field in FIELDS:
        df[field].value_counts(dropna=False).sort_index().rename("count").to_csv(
            output / f"{field}_distribution.csv"
        )
    print(f"Analyzed {len(df)} consenting responses; descriptive tables saved to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", default=Path("outputs/survey"), type=Path)
    args = parser.parse_args()
    analyze(args.input, args.output)
