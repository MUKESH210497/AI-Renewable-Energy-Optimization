# Literature Review — Working Draft

## Scope and evidence standard
This is a thematic review framework, not a completed systematic literature review. It discusses established methods and documented data resources, identifies research gaps, and provides verifiable starting references. Add peer-reviewed, full-text sources with complete bibliographic information before academic submission.

## 1. Renewable energy operations
Photovoltaic and wind generation are influenced by weather, asset condition and grid conditions. Operators require generation estimates for scheduling, planning, and exception management. Forecast quality alone is not evidence of financial savings.

## 2. Forecasting and AI
Forecasting methods range from persistence and seasonal-naive baselines to tree-based machine learning. Predictive features must be known at the moment the forecast is issued. A model that uses measured irradiance from the target time when those measurements were unavailable in advance is not a valid operational forecast.

## 3. Maintenance and anomaly detection
Potential use cases include detecting unusual power-output patterns, identifying equipment degradation, and prioritizing inspections. Their operational value requires evidence of detection quality, response costs, and avoided downtime; this repository has not evaluated those effects.

## 4. Business and organizational adoption
Possible factors to investigate include data readiness, staff capabilities, system integration, investment costs, management sponsorship and governance. Survey statements about benefits represent respondents' perceptions rather than verified causal impacts.

## 5. Sustainability and managerial implications
Potential benefits include more reliable planning and better asset utilization. Any claim about emissions avoided or energy saved requires a transparent counterfactual and data; no such impacts are claimed here.

## 6. Research gaps and contribution
The proposed project combines (a) a documented, held-out forecasting comparison and (b) a management survey on adoption and barriers. The integration is intended to connect technical performance with implementation feasibility without equating predictive accuracy with business outcomes.

## Research synthesis matrix (to complete)
| Theme | Source | Design/data | Findings | Limitations | Relevance |
|---|---|---|---|---|---|
| PV operational data | OEDI PVDAQ documentation | Public PV system time series | Data resource, not a causal impact study | Varying sensors and schemas | Candidate forecasting data |
| Time-series evaluation | scikit-learn TimeSeriesSplit documentation | Methodological guidance | Time-ordered splitting | Equal spacing considerations | Leakage-resistant evaluation |
| AI implementation barriers | Peer-reviewed sources to be identified | Pending | Not yet synthesized | Pending | Survey constructs |

## Verified starting sources
1. Open Energy Data Initiative. *Photovoltaic Data Acquisition (PVDAQ) Public Datasets*. https://data.openei.org/submissions/4568
2. OpenEDI. *PVDAQ Documentation*. https://github.com/openEDI/documentation/blob/main/pvdaq.md
3. scikit-learn developers. *TimeSeriesSplit*. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
4. scikit-learn developers. *Common pitfalls: Data leakage*. https://scikit-learn.org/stable/common_pitfalls.html

## Literature-review completion checklist
Search Google Scholar and academic databases for peer-reviewed forecasting, predictive maintenance, renewable energy operations and technology-adoption research. Record author, year, DOI, study design, population, sample, measures, findings and limitations. Verify every reference before including it in the final dissertation.
