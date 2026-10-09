# Project Architecture and Reproducibility

## Workstreams
1. **Research:** proposal, literature review, methodology, questionnaire, survey plan.
2. **Data:** public PVDAQ site selection, source manifest, quality checks, normalized CSV.
3. **Forecasting:** `src/forecast.py` consumes normalized CSV, produces held-out predictions and error metrics.
4. **Dashboard:** Power BI imports model output files.
5. **Dissertation:** research evidence feeds Chapters 4–6; do not fill before analysis.

## Data flow
```text
OEDI PVDAQ source (site selection pending)
    -> documented download / local cleaning
    -> normalized timestamp,power_kw CSV
    -> chronological train/validation/test split
    -> persistence / Random Forest / Gradient Boosting
    -> real prediction and metric CSV files
    -> Power BI dashboard
    -> dissertation interpretation

Voluntary survey (not yet distributed)
    -> consent and de-identification
    -> private survey CSV
    -> descriptive analysis
    -> aggregate results only
    -> dissertation interpretation
```

## Local quick start
```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
python -m src.forecast --input data/processed/solar_power.csv --output outputs
```

## Limitations
Code is a starter implementation; not yet executed on a real selected PVDAQ site. The model is one-step-ahead, assumes regular intervals and uses past power values plus calendar features. No operational deployment, measured savings, survey outcomes or published dashboard exists.
