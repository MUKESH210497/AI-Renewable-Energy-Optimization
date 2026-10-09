# Research Methodology (Proposed)

## Design
Mixed-methods exploratory and descriptive research: survey, optional interviews, literature review, and solar generation forecasting demonstration.

## Sampling
Target approximately 60–100 voluntary respondents with relevant energy, operations, engineering, analytics, or consulting experience if feasible. Use purposive/convenience sampling and report actual recruitment. Distinguish respondents with direct renewable-sector experience.

## Primary data
Collect structured responses using a consent-based questionnaire. Avoid personal identifiers and confidential business metrics. Analyze descriptive statistics and, where appropriate, scale reliability and exploratory associations. Cross-sectional correlations do not establish causation. Code optional open-ended answers thematically.

## Secondary data
Identify a publicly accessible and appropriately licensed dataset containing timestamps and measured solar generation, ideally with weather features. Record source, license, units, timezone, temporal resolution, missingness and exclusions.

## Forecasting protocol
1. Define prediction target and horizon.
2. Create chronological training, validation and held-out test splits.
3. Engineer only features known at prediction time.
4. Establish persistence or seasonal-naive baseline.
5. Compare Random Forest and Gradient Boosting.
6. Evaluate with MAE and RMSE, including units.
7. Inspect errors and possible data leakage.
8. Visualize actual and predicted generation only after models have been run.

## Tools
Python, pandas, NumPy, scikit-learn, Excel, Power BI, Google Forms/Microsoft Forms.

## Ethics and limitations
Secure informed consent, anonymize responses, and do not commit private survey records or employer/client data. A public forecasting demonstration cannot itself substantiate operational cost savings. Findings depend on actual collected data and analysis.
