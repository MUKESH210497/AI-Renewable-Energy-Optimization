# AI-Driven Operational Efficiency in the Renewable Energy Sector

**MBA final-year research project · AI forecasting · business analytics · renewable energy**

> **Project status:** Proposal, literature framework, executable starter code, test suite, survey-analysis utility, and dashboard specification have been committed. A real dataset has **not** been downloaded, the model has **not** been evaluated on real observations, and no survey responses, business savings, or Power BI report are claimed.

## Research aim
Investigate how AI-based predictive analytics and automation could support renewable energy operations, and what organizational factors shape adoption. Combine a solar power forecasting demonstration with an ethics-aware survey research plan.

## Explore the repository
| Workstream | Files | Status |
|---|---|---|
| MBA proposal | [Project proposal](proposal/MBA_Project_Proposal.md) | Draft |
| Literature | [Thematic review](literature/Literature_Review.md) | Working draft; academic sources to expand |
| Data | [PVDAQ acquisition guide](data/Dataset_Acquisition.md), [source manifest template](data/source_manifest.template.json) | Real public source identified; site not yet selected |
| AI forecasting | [Python implementation](src/forecast.py), [tests](tests/test_forecast.py) | Starter code committed; real-data evaluation pending |
| Analysis workflow | [Reproducibility guide](notebooks/Workflow.md) | Documented |
| Power BI | [Dashboard specification](dashboards/PowerBI_Specification.md) | Design only |
| Survey | [Questionnaire](research/Questionnaire.md), [analysis plan](survey/Analysis_Plan.md), [analysis script](survey/analyze_survey.py) | No responses collected |
| Dissertation | [Six-chapter working draft](report/MBA_Dissertation_Draft.md) | Results chapters pending |
| Portfolio | [Architecture](docs/Architecture.md), [contributing guide](CONTRIBUTING.md) | Documented |

## Verified dataset source
The Open Energy Data Initiative's [PVDAQ public dataset](https://data.openei.org/submissions/4568) provides photovoltaic performance data from public systems; data availability and schema vary by site. Review [OpenEDI PVDAQ documentation](https://github.com/openEDI/documentation/blob/main/pvdaq.md). The old PVDAQ V3 API has been decommissioned.

**No third-party dataset is redistributed in this repository.**

## Reproduce the starter forecasting workflow
Requires Python 3.10+ and a locally prepared real CSV with `timestamp,power_kw` at regular intervals.

```bash
python -m venv .venv
pip install -r requirements.txt
python -m pytest -q
python -m src.forecast --input data/processed/solar_power.csv --output outputs
```

The script performs chronological 70/15/15 partitioning, compares a lag-1 persistence baseline with Random Forest and Gradient Boosting, and exports held-out MAE/RMSE and predictions. The validation segment is reserved but not used for hyperparameter tuning in this starter version. No forecast accuracy claims are made.

## Management research
Proposed survey dimensions include AI adoption, data readiness, perceived efficiency, decision support, cost barriers and staff capabilities. Responses must be consent-based and anonymized. Cross-sectional survey associations do not prove causation.

## Responsible research
Do not upload identifiable respondents, confidential employer/client records, or unlicensed data. Cite academic sources, document all preprocessing, and distinguish predictive accuracy from actual financial or environmental outcomes. University guide approval is required before submission.

## Project roadmap
- [x] Proposal, objectives, questionnaire and research design
- [x] Verified public dataset discovery and acquisition instructions
- [x] Forecasting starter code and unit tests
- [x] Survey analysis starter utility
- [x] Power BI specification and dissertation draft
- [ ] Select, download and validate a real PVDAQ site dataset
- [ ] Execute models, validate and publish genuine evaluation
- [ ] Conduct consent-based survey and analyze real responses
- [ ] Create and validate a real Power BI report
- [ ] Finish evidence-based dissertation Chapters 4–6

## Sources
- [OEDI PVDAQ public data](https://data.openei.org/submissions/4568)
- [OpenEDI PVDAQ technical documentation](https://github.com/openEDI/documentation/blob/main/pvdaq.md)
- [scikit-learn TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
- [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
