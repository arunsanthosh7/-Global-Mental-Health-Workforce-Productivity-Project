"""
Global Mental Health & Workforce Productivity Analysis
Generates a rich, realistic multi-dimensional dataset covering:
- Country-level mental health indicators
- Workforce productivity metrics  
- Healthcare investment data
- Demographic breakdown
- Longitudinal trends (2015-2024)
"""

import pandas as pd
import numpy as np
from datetime import datetime
import random, json

np.random.seed(2024)
random.seed(2024)

# ── Country definitions with real-world inspired base values ─────────────
COUNTRIES = {
    # name: (region, gdp_per_capita_usd, hc_spend_pct_gdp, base_prevalence)
    "United States":     ("North America",   65000, 16.8, 19.1),
    "Canada":            ("North America",   51000, 10.8, 17.4),
    "United Kingdom":    ("Europe",          42000, 10.2, 18.5),
    "Germany":           ("Europe",          50000,  11.7, 14.8),
    "France":            ("Europe",          43000, 11.3, 15.9),
    "Sweden":            ("Europe",          54000, 11.0, 13.2),
    "Norway":            ("Europe",          82000, 10.5, 12.8),
    "Netherlands":       ("Europe",          58000, 10.1, 14.1),
    "Switzerland":       ("Europe",          86000, 11.9, 12.5),
    "Australia":         ("Oceania",         55000, 10.4, 18.3),
    "New Zealand":       ("Oceania",         42000,  9.7, 19.2),
    "Japan":             ("Asia",            39000, 11.1, 7.9),
    "South Korea":       ("Asia",            32000,  8.1, 11.8),
    "Singapore":         ("Asia",            65000,  4.2, 13.4),
    "India":             ("Asia",             2100,  3.5, 14.3),
    "China":             ("Asia",            12000,  5.4, 9.7),
    "Brazil":            ("South America",    8700,  9.5, 18.1),
    "Mexico":            ("South America",    9800,  5.5, 15.3),
    "Argentina":         ("South America",   10200,  9.8, 20.1),
    "South Africa":      ("Africa",           6000,  8.1, 19.8),
    "Nigeria":           ("Africa",           2100,  3.9, 12.1),
    "Kenya":             ("Africa",           1800,  4.8, 13.5),
    "Egypt":             ("Africa",           3500,  4.7, 10.9),
    "Saudi Arabia":      ("Middle East",     23000,  5.7, 15.2),
    "UAE":               ("Middle East",     43000,  4.4, 12.8),
    "Turkey":            ("Middle East",     9500,   4.2, 18.4),
    "Poland":            ("Europe",          17000,  6.5, 15.6),
    "Russia":            ("Europe",          12000,  5.3, 15.1),
    "Spain":             ("Europe",          29000,  9.1, 14.7),
    "Italy":             ("Europe",          33000,  9.0, 13.8),
}

YEARS = list(range(2015, 2025))
SECTORS = ["Technology", "Healthcare", "Finance", "Manufacturing", "Education",
           "Retail", "Government", "Construction", "Transportation", "Agriculture"]
AGE_GROUPS = ["18-25", "26-35", "36-45", "46-55", "56-65"]
GENDERS = ["Male", "Female", "Non-binary"]

# ── Dataset 1: Country-Level Mental Health Indicators ─────────────────────
print("Generating Dataset 1: Country Mental Health Indicators...")
country_records = []

for country, (region, gdp, hc_pct, base_prev) in COUNTRIES.items():
    for year in YEARS:
        year_idx = year - 2015
        
        # COVID-19 effect (2020-2021 spike, gradual recovery)
        covid_bump = 0
        if year == 2020: covid_bump = 3.2
        elif year == 2021: covid_bump = 2.8
        elif year == 2022: covid_bump = 1.5
        elif year == 2023: covid_bump = 0.7
        
        # Trend: mental health awareness increasing prevalence reported
        trend = year_idx * 0.18
        
        # GDP influence (higher GDP → better treatment access → lower untreated)
        gdp_factor = np.log(gdp / 1000) * 0.8
        
        prevalence = round(base_prev + trend + covid_bump + np.random.normal(0, 0.4), 2)
        prevalence = max(5.0, min(32.0, prevalence))
        
        # Treatment gap (% needing care who don't receive it)
        treatment_gap = round(max(10, 85 - gdp_factor * 5 + np.random.normal(0, 3)), 1)
        treatment_gap = min(92, treatment_gap)
        
        # Mental health professionals per 100k
        professionals = round(max(0.1, gdp / 3000 + np.random.normal(0, 1.2)), 2)
        
        # Govt mental health spend as % of health budget
        mh_spend_pct = round(max(0.5, gdp_factor * 0.6 - 1.2 + np.random.normal(0, 0.5)), 2)
        
        # Anxiety disorders prevalence
        anxiety_prev = round(prevalence * 0.52 + np.random.normal(0, 0.3), 2)
        
        # Depression prevalence  
        depression_prev = round(prevalence * 0.38 + np.random.normal(0, 0.25), 2)
        
        # PTSD prevalence
        ptsd_prev = round(prevalence * 0.10 + np.random.normal(0, 0.15), 2)
        ptsd_prev = max(0.1, ptsd_prev)
        
        # GDP adjusted each year (2% avg growth)
        gdp_adj = gdp * (1.02 ** year_idx) * (0.95 if year == 2020 else 1.0)
        
        # Healthcare spend adjusted
        hc_adj = hc_pct + year_idx * 0.08 + (0.3 if year >= 2020 else 0)
        
        country_records.append({
            "country": country,
            "region": region,
            "year": year,
            "gdp_per_capita_usd": round(gdp_adj, 0),
            "healthcare_spend_pct_gdp": round(hc_adj, 2),
            "mental_health_prevalence_pct": prevalence,
            "anxiety_disorders_pct": anxiety_prev,
            "depression_pct": depression_prev,
            "ptsd_pct": ptsd_prev,
            "treatment_gap_pct": treatment_gap,
            "mh_professionals_per_100k": professionals,
            "govt_mh_spend_pct_health_budget": mh_spend_pct,
            "population_millions": round(np.random.uniform(1, 1400), 1),
        })

df_country = pd.DataFrame(country_records)
df_country.to_csv("/home/claude/global_health_project/data/01_country_mental_health.csv", index=False)
print(f"  ✅ {len(df_country)} rows × {len(df_country.columns)} cols")

# ── Dataset 2: Workforce Productivity & Wellbeing Survey ──────────────────
print("Generating Dataset 2: Workforce Productivity & Wellbeing...")
workforce_records = []

for i in range(8500):
    country = random.choice(list(COUNTRIES.keys()))
    region, gdp, hc_pct, base_prev = COUNTRIES[country]
    sector = random.choice(SECTORS)
    age_group = random.choice(AGE_GROUPS)
    gender = random.choices(GENDERS, weights=[0.47, 0.50, 0.03])[0]
    year = random.choice(YEARS)
    
    # Wellbeing score (0-100)
    base_wellbeing = 55 + (gdp / 5000) + np.random.normal(0, 8)
    base_wellbeing = max(10, min(100, base_wellbeing))
    
    # Burnout risk (0-10 scale)
    sector_burnout = {"Technology": 6.2, "Healthcare": 7.1, "Finance": 6.8,
                      "Manufacturing": 5.4, "Education": 6.5, "Retail": 5.8,
                      "Government": 4.9, "Construction": 5.2,
                      "Transportation": 5.6, "Agriculture": 4.7}
    burnout = round(sector_burnout[sector] + np.random.normal(0, 1.2), 2)
    burnout = max(0, min(10, burnout))
    
    # Work hours per week
    base_hours = 40
    sector_hours = {"Technology": 3, "Healthcare": 5, "Finance": 6,
                    "Manufacturing": 2, "Education": 1, "Retail": -1,
                    "Government": -2, "Construction": 4,
                    "Transportation": 3, "Agriculture": 2}
    hours = round(base_hours + sector_hours[sector] + np.random.normal(0, 4), 1)
    hours = max(20, min(80, hours))
    
    # Productivity score (correlated with wellbeing, inversely with burnout)
    productivity = round(base_wellbeing * 0.6 - burnout * 4 + np.random.normal(0, 5) + 40, 1)
    productivity = max(10, min(100, productivity))
    
    # Absenteeism days per year
    absenteeism = round(max(0, 8 - base_wellbeing/15 + burnout*0.8 + np.random.normal(0, 2)), 1)
    
    # Mental health support access (yes/no)
    support_access = 1 if (gdp > 20000 and random.random() > 0.3) else (
                     1 if random.random() > 0.7 else 0)
    
    # Remote work %
    remote_pct = 0
    if year >= 2020:
        sector_remote = {"Technology": 75, "Finance": 55, "Education": 45,
                         "Healthcare": 15, "Manufacturing": 5, "Retail": 10,
                         "Government": 35, "Construction": 5,
                         "Transportation": 10, "Agriculture": 2}
        remote_pct = round(sector_remote[sector] + np.random.normal(0, 8))
        remote_pct = max(0, min(100, remote_pct))
    
    # Salary satisfaction (1-5)
    salary_sat = round(min(5, max(1, 2.5 + (gdp/30000) + np.random.normal(0, 0.8))), 1)
    
    # Mental health diagnosis (binary)
    diagnosis_prob = (base_prev / 100) * (1.3 if burnout > 6 else 1.0)
    has_diagnosis = 1 if random.random() < diagnosis_prob else 0
    
    # Presenteeism score (working while unwell, 0-100)
    presenteeism = round(max(0, burnout * 8 + np.random.normal(0, 5)), 1)
    presenteeism = min(100, presenteeism)
    
    workforce_records.append({
        "employee_id": f"EMP{i+10001:06d}",
        "country": country,
        "region": region,
        "sector": sector,
        "age_group": age_group,
        "gender": gender,
        "year": year,
        "wellbeing_score": round(base_wellbeing, 1),
        "burnout_risk_score": burnout,
        "weekly_work_hours": hours,
        "productivity_score": productivity,
        "absenteeism_days_per_year": absenteeism,
        "mental_health_support_access": support_access,
        "remote_work_pct": remote_pct,
        "salary_satisfaction": salary_sat,
        "mental_health_diagnosis": has_diagnosis,
        "presenteeism_score": presenteeism,
    })

df_workforce = pd.DataFrame(workforce_records)
df_workforce.to_csv("/home/claude/global_health_project/data/02_workforce_productivity.csv", index=False)
print(f"  ✅ {len(df_workforce)} rows × {len(df_workforce.columns)} cols")

# ── Dataset 3: Mental Health Economic Cost by Country ─────────────────────
print("Generating Dataset 3: Economic Cost of Mental Health...")
econ_records = []

for country, (region, gdp, hc_pct, base_prev) in COUNTRIES.items():
    pop_millions = {"United States": 331, "China": 1411, "India": 1393, "United Kingdom": 67,
                    "Germany": 83, "France": 67, "Japan": 126, "Brazil": 213,
                    "Australia": 25, "Canada": 38, "South Korea": 52, "Mexico": 130,
                    "Russia": 145, "Spain": 47, "Italy": 60, "Argentina": 45,
                    "South Africa": 60, "Nigeria": 211, "Kenya": 54, "Egypt": 102,
                    "Saudi Arabia": 35, "UAE": 10, "Turkey": 85, "Sweden": 10,
                    "Norway": 5, "Netherlands": 17, "Switzerland": 9, "Poland": 38,
                    "New Zealand": 5, "Singapore": 6}.get(country, 20)
    
    for year in YEARS:
        year_idx = year - 2015
        gdp_adj = gdp * (1.02 ** year_idx)
        covid_mult = 1.35 if year == 2020 else (1.28 if year == 2021 else 1.15 if year == 2022 else 1.0)
        
        # Economic cost of mental ill-health as % of GDP
        cost_pct_gdp = round(2.8 + (base_prev / 25) * 1.5 + np.random.normal(0, 0.2), 2)
        cost_pct_gdp *= covid_mult
        
        # Total economic cost (USD billions)
        total_gdp_bn = gdp_adj * pop_millions / 1000
        total_cost_bn = round(total_gdp_bn * cost_pct_gdp / 100, 2)
        
        # Lost productivity (% of cost)
        lost_productivity_pct = round(55 + np.random.normal(0, 3), 1)
        healthcare_cost_pct = round(30 + np.random.normal(0, 2), 1)
        social_welfare_pct = round(100 - lost_productivity_pct - healthcare_cost_pct, 1)
        
        econ_records.append({
            "country": country,
            "region": region,
            "year": year,
            "gdp_per_capita_usd": round(gdp_adj),
            "population_millions": pop_millions,
            "mh_cost_pct_gdp": cost_pct_gdp,
            "total_mh_cost_usd_billions": total_cost_bn,
            "lost_productivity_pct": lost_productivity_pct,
            "healthcare_cost_pct": healthcare_cost_pct,
            "social_welfare_cost_pct": social_welfare_pct,
            "roi_mh_investment": round(max(2, gdp / 15000 + np.random.normal(0, 0.5)), 2),
        })

df_econ = pd.DataFrame(econ_records)
df_econ.to_csv("/home/claude/global_health_project/data/03_economic_cost.csv", index=False)
print(f"  ✅ {len(df_econ)} rows × {len(df_econ.columns)} cols")

# ── Dataset 4: Post-COVID Longitudinal Recovery Tracking ──────────────────
print("Generating Dataset 4: Post-COVID Recovery Tracking...")
covid_records = []
quarters = ["Q1","Q2","Q3","Q4"]
metrics = ["anxiety_index","depression_index","workforce_participation_pct",
           "telehealth_adoption_pct","mh_service_utilization_idx"]

for country in list(COUNTRIES.keys())[:20]:  # Top 20 countries
    region, gdp, hc_pct, base_prev = COUNTRIES[country]
    for year in YEARS:
        for q in quarters:
            if year < 2019: continue  # Only 2019-2024
            period = f"{year}-{q}"
            pre_covid_base = 100
            
            # Index tracking vs 2019 baseline
            if year == 2019:
                anxiety_idx = round(100 + np.random.normal(0, 2), 1)
                depr_idx = round(100 + np.random.normal(0, 2), 1)
                wfp = round(72 + np.random.normal(0, 1.5), 1)
                telehealth = round(8 + np.random.normal(0, 1), 1)
                util_idx = round(100 + np.random.normal(0, 2), 1)
            elif year == 2020:
                shock = {"Q1": 1.1, "Q2": 1.45, "Q3": 1.35, "Q4": 1.30}[q]
                wfp_shock = {"Q1": 0.97, "Q2": 0.82, "Q3": 0.87, "Q4": 0.89}[q]
                anxiety_idx = round(100 * shock + np.random.normal(0, 3), 1)
                depr_idx = round(100 * (shock * 0.9) + np.random.normal(0, 3), 1)
                wfp = round(72 * wfp_shock + np.random.normal(0, 1.5), 1)
                telehealth = round(8 * (1 + (shock-1)*8) + np.random.normal(0, 3), 1)
                util_idx = round(100 * 0.75 + np.random.normal(0, 3), 1)
            elif year == 2021:
                shock = {"Q1": 1.38, "Q2": 1.32, "Q3": 1.28, "Q4": 1.22}[q]
                anxiety_idx = round(100 * shock + np.random.normal(0, 2.5), 1)
                depr_idx = round(100 * (shock * 0.88) + np.random.normal(0, 2), 1)
                wfp = round(72 * 0.91 + np.random.normal(0, 1.5), 1)
                telehealth = round(45 + np.random.normal(0, 5), 1)
                util_idx = round(100 * 0.88 + np.random.normal(0, 3), 1)
            elif year == 2022:
                shock = {"Q1": 1.18, "Q2": 1.14, "Q3": 1.10, "Q4": 1.08}[q]
                anxiety_idx = round(100 * shock + np.random.normal(0, 2), 1)
                depr_idx = round(100 * (shock * 0.92) + np.random.normal(0, 2), 1)
                wfp = round(72 * 0.96 + np.random.normal(0, 1.5), 1)
                telehealth = round(55 + np.random.normal(0, 4), 1)
                util_idx = round(100 * 0.95 + np.random.normal(0, 2), 1)
            elif year == 2023:
                shock = {"Q1": 1.06, "Q2": 1.04, "Q3": 1.03, "Q4": 1.02}[q]
                anxiety_idx = round(100 * shock + np.random.normal(0, 1.5), 1)
                depr_idx = round(100 * (shock * 0.96) + np.random.normal(0, 1.5), 1)
                wfp = round(72 * 0.99 + np.random.normal(0, 1.2), 1)
                telehealth = round(58 + np.random.normal(0, 3), 1)
                util_idx = round(100 * 0.98 + np.random.normal(0, 2), 1)
            else:  # 2024
                anxiety_idx = round(102 + np.random.normal(0, 1.5), 1)
                depr_idx = round(101 + np.random.normal(0, 1.5), 1)
                wfp = round(72.5 + np.random.normal(0, 1), 1)
                telehealth = round(61 + np.random.normal(0, 2), 1)
                util_idx = round(101 + np.random.normal(0, 1.5), 1)
            
            covid_records.append({
                "country": country,
                "region": region,
                "year": year,
                "quarter": q,
                "period": period,
                "anxiety_index_vs_2019": max(50, anxiety_idx),
                "depression_index_vs_2019": max(50, depr_idx),
                "workforce_participation_pct": max(40, min(85, wfp)),
                "telehealth_adoption_pct": max(0, min(100, telehealth)),
                "mh_service_utilization_idx": max(50, util_idx),
            })

df_covid = pd.DataFrame(covid_records)
df_covid.to_csv("/home/claude/global_health_project/data/04_covid_recovery.csv", index=False)
print(f"  ✅ {len(df_covid)} rows × {len(df_covid.columns)} cols")

print("\n✅ All 4 datasets generated!")
print(f"  Dataset 1: {len(df_country):,} rows — Country Mental Health Indicators")
print(f"  Dataset 2: {len(df_workforce):,} rows — Workforce Productivity & Wellbeing")
print(f"  Dataset 3: {len(df_econ):,} rows — Economic Cost of Mental Health")
print(f"  Dataset 4: {len(df_covid):,} rows — Post-COVID Recovery Tracking")
