# Renewable Energy Dataset Acquisition

## Recommended verified source
**PVDAQ (Photovoltaic Data Acquisition) Public Datasets** — Open Energy Data Initiative:
https://data.openei.org/submissions/4568

Data documentation:
https://github.com/openEDI/documentation/blob/main/pvdaq.md

The PVDAQ public data lake contains photovoltaic performance time series and system metadata. Sensor coverage and resolution vary across systems. The OpenEDI documentation describes CSV and Parquet resources and an AWS-hosted data lake.

**Important:** The legacy PVDAQ V3 API is decommissioned. Do not use old V3 endpoint tutorials: https://developer.nlr.gov/docs/solar/pvdaq-v3/

## Selection procedure
1. Browse the OEDI PVDAQ catalog and choose a site with a suitable measured generation/power variable and timestamps.
2. Inspect metadata for units, timezone, data frequency and sensor definitions.
3. Download only the subset needed for reproducible research; record exact source URL, site ID, retrieval date and usage conditions.
4. Confirm the license and any restrictions before redistribution.
5. Export a locally normalized CSV with columns `timestamp` and `power_kw`. Optional ex-ante features must be documented.
6. Do not fill missing periods without marking them; inspect duplicate timestamps, DST transitions, outages, clipping and negative readings.

## Expected normalized CSV
```csv
timestamp,power_kw
```
This header is a **schema illustration**, not a data observation.

## Recommended project storage
Store the real source files locally under `data/raw/` (ignored by Git). Store the normalized data under `data/processed/` locally unless licensing and size permit publishing. Save source metadata in `data/source_manifest.json` once selected.

## Forecasting interpretation
The supplied starter model forecasts the next observation using prior measured power and calendar features. It does not require target-time weather readings, avoiding a common source of leakage. Evaluate whether the site is regularly sampled before use.

## Status
A real, verified dataset **source has been identified**, but no PVDAQ site has been selected or data downloaded into this repository. No dataset measurements or accuracy statistics are claimed.
