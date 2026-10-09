# NREL PVDAQ — Reproducible System Selection

## Official sources
- Dataset and citation: https://data.openei.org/submissions/4568
- Public systems catalog (CSV): https://oedi-data-lake.s3.amazonaws.com/pvdaq/csv/systems_20250729.csv
- Technical schema: https://github.com/openEDI/documentation/blob/main/pvdaq.md
- Maintained download utility: https://github.com/NatLabRockies/pvdaq_access

The OEDI catalog links the above systems CSV, which can be downloaded without credentials. The data lake includes time series and metadata. Do not use the retired PVDAQ V3 API.

## Selection criteria
Choose a system with (1) public time-series measurements, (2) an identifiable power metric and confirmed units, (3) ideally at least 12 months of observations, (4) adequate completeness and stable sampling frequency, and (5) documentation of the timestamp timezone. Irradiance and temperature are optional; they are not required by the starter forecasting model.

## Selection workflow
1. Download the systems CSV with `python scripts/select_pvdaq_system.py --download-catalog`.
2. Review the actual column names and shortlisted records printed by the script.
3. Choose a system ID only after verifying data availability and the power metric in the OEDI browser or downloaded files.
4. Record the ID, source URL, date, units, sampling interval and license in `data/source_manifest.template.json` (copy to your local manifest).
5. Download that system's data with the maintained `pvdaq_access` utility following its documentation, or from the OEDI public S3 paths.
6. Inspect raw CSV headers and metadata before running `scripts/prepare_pvdaq.py`. Supply the actual timestamp, value and optional metric column names.
7. Run the forecasting pipeline on the normalized CSV.

## Current verification boundary
The official catalog URL and data schemas have been verified from published OEDI documentation. The full CSV contents could not be read in this environment, so **no specific system ID has been selected or claimed to meet the criteria**. The selection script makes the shortlist reproducible on a networked machine; it does not invent a site.

## Correct interpretation
PVDAQ's long-form `pvdaq_pvdata` schema includes `system_id`, `measured_on`, `utc_measured_on`, `metric_id`, and `value`. Metric definitions are held separately; do not treat arbitrary `value` as kW until its `metric_id` and units are verified. A timestamp may have daylight-saving ambiguities, so prefer verified UTC measurements.
