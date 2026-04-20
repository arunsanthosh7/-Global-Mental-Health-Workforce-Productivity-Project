# 🧠 Global Mental Health & Workforce Productivity Analysis

> **End-to-end data analysis project by [Arunsanthosh](https://github.com/arunsanthosh)** — Data Analyst  
> Covering 30 countries, 10 years of longitudinal data, and 8,500 workforce survey records.

---

## What This Project Is About

Mental health is the largest unaddressed productivity crisis in the global economy. We know this intuitively. But the numbers — when you actually run them — are harder to sit with than most people expect.

This project started with a simple question: *how much does untreated mental ill-health actually cost, and what predicts whether an employee is productive or not?* Four datasets, six visualizations, and one machine learning model later, some of the answers are clear. Others raise more questions than they close.

The analysis covers 30 countries from 2015 through 2024, tracks quarterly COVID-19 impact and recovery, models the workforce productivity of 8,500 employees across 10 industry sectors, and estimates the economic burden country by country. It uses Python, Pandas, Scikit-learn, Matplotlib, and Seaborn throughout.

---

## Project Stats at a Glance

| Metric | Value |
|--------|-------|
| **Countries analyzed** | 30 |
| **Years of data** | 10 (2015–2024) |
| **Workforce survey records** | 8,500 |
| **Datasets** | 4 integrated datasets |
| **Visualizations produced** | 6 high-resolution charts |
| **ML model CV R²** | 0.642 (Gradient Boosting, 5-fold) |
| **Global economic burden (2024)** | USD 6.4 trillion/year |
| **Treatment gap range** | 18% (Europe) → 88% (Sub-Saharan Africa) |
| **COVID anxiety spike (2020)** | +32.5 index points above 2019 baseline |
| **Recovery by 2024** | 94.5% of COVID spike resolved |
| **Telehealth growth** | 8.2% → 61.4% (7.5× in five years) |
| **Top predictor of productivity** | Wellbeing score (32.4% feature importance) |
| **Code files** | 3 Python files + 1 Jupyter notebook |

---

## The Analyst

**Arunsanthosh** — Data Analyst

This project was designed, built, and documented by Arunsanthosh, a data analyst focused on turning large, messy, multi-source datasets into decisions people can act on. The analysis draws on WHO and OECD mental health benchmarks, Lancet Psychiatry burden-of-disease estimates, McKinsey workforce research, and Harvard Business Review burnout cost modeling — all synthesized into a reproducible Python pipeline.

- 📧 Connect on [LinkedIn](https://linkedin.com/in/arunsanthosh)
- 💻 More projects on [GitHub](https://github.com/arunsanthosh)
- 📊 Portfolio on [Naukri](https://naukri.com)

---

## Key Findings

**On the global crisis:**

Mental health prevalence rose from 13.3% in 2015 to 16.1% in 2024 — a 21% increase. COVID-19 accelerated this sharply, pushing the global anxiety index to 32.5 points above baseline in Q2 2020. By 2024, about 94.5% of that spike has unwound, but the trend line never returned to its pre-2019 trajectory. We're at a structurally higher level than we were before the pandemic.

**On treatment equity:**

GDP per capita and treatment gap correlate at r = −0.82 (p < 0.001). That's the strongest statistical relationship in the entire dataset. High-income countries in Northern Europe have treatment gaps around 18–25%. Sub-Saharan Africa is at 85–88%. The prevalence rates are not that different. The resources are.

**On the workforce:**

Wellbeing score is the single strongest predictor of employee productivity (feature importance: 32.4%), followed by burnout risk (26.1%) and presenteeism (15.3%). Absenteeism — which is what most HR departments actually track — ranks fourth at 10.2%. The implication is uncomfortable: the visible metric companies measure is less than a third as predictive as wellbeing, which most companies don't systematically measure at all.

**On burnout by sector:**

Healthcare workers average a burnout score of 7.08/10. Finance comes in at 6.82. Technology at 6.21. Agriculture and Government are at the other end — 4.70 and 4.90. These aren't marginal differences. They're structural, and they've been consistent across every year in the dataset.

**On remote work:**

The data suggests 26–50% remote work is the sweet spot. Fully on-site and fully remote both underperform on wellbeing, burnout, and productivity. The optimal isn't a philosophical statement about flexibility — it's a measurable outcome sitting in the middle of the distribution.

**On economic cost:**

The global mental health economic burden reached USD 6.4 trillion in 2024 — up 32.4% from 2015. Lost productivity accounts for 55% of that figure. Healthcare costs are 30%. Social welfare costs make up the remaining 15%. WHO evidence puts the return on evidence-based treatment at $4 per $1 invested. The countries achieving the highest ROI (Switzerland, Norway, Netherlands) are also the ones with the lowest treatment gaps.

---

## Datasets

All four datasets are included in this repository as CSV files.

### DS1 — Country Mental Health Indicators
**`DS1_Country_Mental_Health.csv`** · 300 rows × 13 columns

Country-level mental health statistics from 2015–2024. Variables include MH prevalence %, anxiety disorders %, depression %, PTSD %, treatment gap %, mental health professionals per 100,000 population, government MH spend as % of health budget, and GDP per capita.

Built with base prevalence values sourced from WHO Mental Health Atlas (2020) and OECD Health at a Glance (2023), with COVID-19 period effects modeled from Lancet Psychiatry (Santomauro et al., 2021).

### DS2 — Workforce Productivity & Wellbeing Survey
**`DS2_Workforce_Productivity.csv`** · 8,500 rows × 17 columns

Employee-level survey data across 10 sectors, 30 countries, and 5 age cohorts. Variables include wellbeing score (0–100), burnout risk score (0–10), productivity score (0–100), absenteeism days per year, presenteeism score, remote work %, salary satisfaction, mental health support access, and mental health diagnosis flag.

Scoring frameworks aligned with WHO-5 Wellbeing Index and Maslach Burnout Inventory (MBI) conventions.

### DS3 — Economic Cost of Mental Ill-Health
**`DS3_Economic_Cost.csv`** · 300 rows × 11 columns

Country-level economic burden estimates from 2015–2024. Variables include MH cost as % of GDP, total MH cost in USD billions, lost productivity %, healthcare cost %, social welfare cost %, and estimated ROI of MH investment.

Base cost modeling derived from McKinsey Global Institute (2022) and OECD Working Paper on the Economics of Mental Health.

### DS4 — Post-COVID Recovery Tracking
**`DS4_COVID_Recovery.csv`** · 480 rows × 10 columns

Quarterly tracking across 20 countries from Q1 2019 through Q4 2024. Variables include anxiety index vs. 2019 baseline, depression index vs. 2019 baseline, workforce participation %, telehealth adoption %, and MH service utilization index. Pre-COVID quarterly data is included as the baseline reference period.

---

## Visualizations

Six analysis charts are included, all produced at 200 DPI with a dark professional theme.

**Chart 01 — Executive Intelligence Dashboard** (`Chart01_Executive_Dashboard.png`)  
Four-panel dashboard: KPI cards (global prevalence, treatment gap, economic burden, wellbeing score), regional prevalence trend by year, top-10 countries by economic burden, burnout risk by sector, and wellbeing vs. productivity scatter with regression line.

**Chart 02 — Treatment Gap & Investment Analysis** (`Chart02_Treatment_Gap.png`)  
Six-panel deep dive: GDP vs. treatment gap scatter annotated by country, MH professionals per 100k by region, treatment gap trend for six selected countries, government MH spend vs. treatment gap, region × healthcare spend heatmap, and ROI ranking by country.

**Chart 03 — Workforce Deep Dive** (`Chart03_Workforce_Deepdive.png`)  
Six panels: productivity distribution by sector (violin plots), remote work level vs. wellbeing/burnout/productivity, age group × sector burnout heatmap, absenteeism by diagnosis and support access, gender wellbeing trends 2015–2024, and a 6-metric correlation matrix.

**Chart 04 — COVID Recovery & Telehealth** (`Chart04_COVID_Recovery.png`)  
Four panels: global anxiety and depression quarterly index (filled area chart), telehealth adoption by region from 2019–2024, country-level COVID recovery heatmap across three metrics, and workforce participation recovery with confidence bands.

**Chart 05 — Economic Impact & Predictive Modeling** (`Chart05_Economic_Predictive.png`)  
Six panels: global MH cost trend with 2025–2027 linear forecast, cost breakdown pie, Gradient Boosting feature importance for productivity prediction, three-scenario investment ROI simulation, estimated annual MH cost per employee by sector, and wellbeing quartile impact on workforce metrics.

**Chart 06 — Global Country Comparison** (`Chart06_Global_Comparison.png`)  
Three panels: bubble chart of MH professionals vs. prevalence, top-10 countries ranked by treatment gap, and government MH investment vs. economic burden scatter.

---

## Code Files

### `01_generate_dataset.py`
Builds all four datasets from scratch. Each dataset is constructed with calibrated statistical distributions matching published WHO, OECD, and Lancet benchmarks. COVID-19 period effects, GDP-correlated treatment gaps, sector-specific burnout distributions, and telehealth adoption curves are all built from real-world reference parameters. Random seed is fixed at 2024 for reproducibility.

### `02_analysis_and_charts.py`
The full analysis and visualization pipeline. Runs Pearson correlations, time-series decomposition, sector/age heatmaps, Gradient Boosting feature importance with cross-validation, economic cost forecasting, and ROI scenario modeling. Produces all six charts. Runtime on a standard laptop is around 45–90 seconds.

### `Global_MH_Analysis.ipynb`
The Jupyter Notebook version of the analysis — 22 cells, 8 sections, narrative text throughout. Designed to be run top-to-bottom as a reproducible analysis document. Covers the same ground as the Python scripts but with explanatory markdown between code blocks.

---

## Machine Learning Model

The productivity prediction model uses three algorithms on the 8,500-record workforce dataset:

| Model | Train R² | Test R² | CV R² (5-fold) | MAE |
|-------|----------|---------|----------------|-----|
| Linear Regression | 0.412 | 0.409 | 0.408 | 11.23 |
| Random Forest | 0.924 | 0.632 | 0.624 | 8.71 |
| **Gradient Boosting** | **0.883** | **0.649** | **0.642** | **8.49** |

Gradient Boosting was selected as the best model. The gap between train and test R² (0.883 vs. 0.649) indicates some overfitting, which is typical with tree ensembles at this dataset size. The 5-fold CV R² of 0.642 is the honest performance estimate.

**Feature importance (Gradient Boosting):**

```
Wellbeing Score       ████████████████████  32.4%
Burnout Risk          ████████████████      26.1%
Presenteeism          ██████████            15.3%
Absenteeism           ██████                10.2%
Work Hours            ████                   6.1%
Salary Satisfaction   ███                    5.2%
MH Support Access     ██                     3.1%
Remote Work %         █                      1.4%
```

Two variables that most organizations don't systematically track — wellbeing and presenteeism — account for nearly 48% of productivity variance combined. The variables that HR systems typically do track (absenteeism, work hours) explain less than 17% between them.

---

## How to Run It

**Requirements:**

```
python >= 3.10
pandas >= 2.1.0
numpy >= 1.26.0
matplotlib >= 3.8.0
seaborn >= 0.13.0
scikit-learn >= 1.3.2
scipy >= 1.11.3
```

**Install dependencies:**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

**Generate datasets:**

```bash
python 01_generate_dataset.py
```

This creates the four CSV files in a `data/` subdirectory. Takes around 10–15 seconds.

**Run the full analysis:**

```bash
python 02_analysis_and_charts.py
```

Saves all six chart PNGs to a `charts/` subdirectory. Takes 45–90 seconds depending on hardware.

**Open the notebook:**

```bash
jupyter notebook Global_MH_Analysis.ipynb
```

Run cells top-to-bottom. The notebook expects the CSV files to exist in `data/` — run the generation script first if they don't.

---

## Project Structure

```
global-mh-productivity/
│
├── data/
│   ├── DS1_Country_Mental_Health.csv      # 300 rows — country health indicators
│   ├── DS2_Workforce_Productivity.csv     # 8,500 rows — workforce survey
│   ├── DS3_Economic_Cost.csv             # 300 rows — economic burden estimates
│   └── DS4_COVID_Recovery.csv            # 480 rows — quarterly recovery tracking
│
├── charts/
│   ├── Chart01_Executive_Dashboard.png
│   ├── Chart02_Treatment_Gap.png
│   ├── Chart03_Workforce_Deepdive.png
│   ├── Chart04_COVID_Recovery.png
│   ├── Chart05_Economic_Predictive.png
│   └── Chart06_Global_Comparison.png
│
├── 01_generate_dataset.py                 # Dataset generation script
├── 02_analysis_and_charts.py             # Analysis + visualization pipeline
├── Global_MH_Analysis.ipynb             # Jupyter notebook (narrative + code)
├── Global_MH_Workforce_Report.docx       # Full senior analyst report (3MB)
└── README.md                             # This file
```

---

## Data Sources & References

The synthetic datasets are calibrated against the following published sources:

- **WHO World Mental Health Report (2022)** — global prevalence and treatment gap baselines
- **OECD Mental Health Systems (2023)** — government expenditure and workforce data
- **Lancet Psychiatry** — Santomauro et al. (2021), "Global prevalence and burden of depressive and anxiety disorders in 2020 and 2019"
- **McKinsey Global Institute (2022)** — "Addressing employee burnout: Are companies making the right investments?"
- **Harvard Business Review (2022)** — Wigert & Agrawal, "The cost of employee burnout"
- **Our World in Data** — mental health statistics compilation (ourworldindata.org/mental-health)
- **National Institute of Mental Health (NIMH)** — US-specific workforce and prevalence data
- **Global Burden of Disease Study 2019** — YLD estimates for mental disorders

---

## Limitations

A few things worth knowing before drawing conclusions from this data:

The datasets are synthetic — built from real-world distributions and calibrated against published benchmarks, but not collected from actual respondents or country reporting agencies. The patterns are statistically plausible rather than empirically verified. Use the analysis as a methodology and framework demonstration, not as a source of production statistics.

The productivity model explains about 65% of variance. That's reasonable for survey-based behavioral data, but 35% is unexplained. There are almost certainly important variables missing — job autonomy, manager quality, team dynamics, organizational culture — that a real survey would capture.

Treatment gap estimates for low-income countries are particularly uncertain. Published data for Sub-Saharan Africa and South Asia is sparse and inconsistently collected. The correlations hold, but the absolute numbers should be treated with more caution for those regions.

---

## License

MIT License. Use freely, modify as needed, attribution appreciated.

---

## Contact

**Arunsanthosh** · Data Analyst  
Questions about the methodology, the datasets, or the analysis: open an issue or reach out directly via LinkedIn.

If you're building something in the mental health analytics or HR tech space and want to talk through the approach, I'm interested.

---

*Built with Python · Pandas · Matplotlib · Seaborn · Scikit-learn · SciPy*  
*Data calibrated against WHO, OECD, Lancet Psychiatry, and McKinsey sources*  
*Analyst: Arunsanthosh*
