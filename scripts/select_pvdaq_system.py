"""Download and inspect the official OEDI PVDAQ systems catalog.

This script does NOT claim any particular system is suitable; it exposes
the real catalog for informed manual selection.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

CATALOG_URL = "https://oedi-data-lake.s3.amazonaws.com/pvdaq/csv/systems_20250729.csv"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--download-catalog", action="store_true")
    parser.add_argument("--catalog", type=Path, default=Path("data/raw/pvdaq_systems.csv"))
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()
    if args.download_catalog:
        args.catalog.parent.mkdir(parents=True, exist_ok=True)
        frame = pd.read_csv(CATALOG_URL)
        frame.to_csv(args.catalog, index=False)
    else:
        frame = pd.read_csv(args.catalog)
    print(f"Catalog records: {len(frame)}")
    print("Available columns:", ", ".join(map(str, frame.columns)))
    print(frame.head(args.limit).to_string(index=False))
    print("\nInspect source data and metric units before selecting a system ID.")


if __name__ == "__main__":
    main()
