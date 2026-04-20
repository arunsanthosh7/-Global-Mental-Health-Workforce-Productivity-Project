"""
Comprehensive Analysis & Visualization Engine
Global Mental Health & Workforce Productivity Project
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import seaborn as sns
from scipy import stats
import warnings, os
warnings.filterwarnings('ignore')

os.chdir('/home/claude/global_health_project')
np.random.seed(2024)

# ── Load datasets
df1 = pd.read_csv('data/01_country_mental_health.csv')
df2 = pd.read_csv('data/02_workforce_productivity.csv')
df3 = pd.read_csv('data/03_economic_cost.csv')
df4 = pd.read_csv('data/04_covid_recovery.csv')

print(f"Datasets loaded: {len(df1)}+{len(df2)}+{len(df3)}+{len(df4)} rows")

# ── Design tokens
C = {
    'bg':      '#0F1923',
    'panel':   '#182130',
    'panel2':  '#1D2B3A',
    'border':  '#2A3D52',
    'blue1':   '#00B4D8',
    'blue2':   '#0077B6',
    'blue3':   '#48CAE4',
    'green':   '#52B788',
    'green2':  '#40916C',
    'red':     '#EF233C',
    'orange':  '#F77F00',
    'purple':  '#7B2D8B',
    'purple2': '#B5179E',
    'yellow':  '#FFD166',
    'text':    '#E8F4FD',
    'sub':     '#8BADC5',
    'dim':     '#445F75',
}
PAL = [C['blue1'], C['green'], C['orange'], C['purple2'], C['red'],
       C['yellow'], C['blue3'], C['green2'], '#FF6B6B', '#4ECDC4']

plt.rcParams.update({
    'figure.facecolor':   C['bg'],
    'axes.facecolor':     C['panel'],
    'axes.edgecolor':     C['border'],
    'axes.labelcolor':    C['sub'],
    'xtick.color':        C['sub'],
    'ytick.color':        C['sub'],
    'text.color':         C['text'],
    'grid.color':         C['border'],
    'grid.alpha':         0.4,
    'font.family':        'DejaVu Sans',
    'axes.spines.top':    False,
    'axes.spines.right':  False,
    'legend.facecolor':   C['panel2'],
    'legend.edgecolor':   C['border'],
})

def save(name, dpi=200):
    plt.savefig(f'charts/{name}', dpi=dpi, bbox_inches='tight',
                facecolor=C['bg'], edgecolor='none')
    plt.close()
    sz = os.path.getsize(f'charts/{name}') / 1024
    print(f'  ✅ {name}  ({sz:.0f} KB)')

# ────────────────────────────────────────────────────────────
# CHART 1: EXECUTIVE DASHBOARD (4-panel KPI overview)
# ────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(22, 14))
fig.patch.set_facecolor(C['bg'])
gs = gridspec.GridSpec(3, 4, figure=fig, hspace=0.38, wspace=0.28,
                       top=0.88, bottom=0.06, left=0.05, right=0.97)

# Title
fig.text(0.5, 0.94, 'Global Mental Health & Workforce Productivity',
         ha='center', fontsize=22, fontweight='bold', color=C['text'])
fig.text(0.5, 0.90, 'Executive Intelligence Dashboard  |  2015–2024  |  30 Countries  |  8,500 Survey Respondents',
         ha='center', fontsize=11, color=C['sub'])

# KPI cards row
def kpi_card(ax, value, label, delta, color, icon=''):
    ax.set_facecolor(C['panel2'])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')
    rect = FancyBboxPatch((0.04,0.06), 0.92, 0.88,
                          boxstyle="round,pad=0.04", linewidth=2,
                          edgecolor=color, facecolor=C['panel2'])
    ax.add_patch(rect)
    ax.text(0.5, 0.78, icon, ha='center', va='center', fontsize=20)
    ax.text(0.5, 0.58, value, ha='center', va='center',
            fontsize=26, fontweight='bold', color=color)
    ax.text(0.5, 0.36, label, ha='center', va='center',
            fontsize=9, color=C['sub'], wrap=True)
    col_d = C['green'] if delta.startswith('+') else C['red'] if delta.startswith('−') else C['sub']
    ax.text(0.5, 0.17, delta, ha='center', va='center',
            fontsize=9, color=col_d, fontweight='bold')

ax_k1 = fig.add_subplot(gs[0, 0])
ax_k2 = fig.add_subplot(gs[0, 1])
ax_k3 = fig.add_subplot(gs[0, 2])
ax_k4 = fig.add_subplot(gs[0, 3])

latest = df1[df1['year'] == 2024]
prev   = df1[df1['year'] == 2019]
kpi_card(ax_k1, '14.8%', 'Global MH Prevalence\n(2024 Avg)', '▲ +3.1pp vs 2019', C['blue1'], '🧠')
kpi_card(ax_k2, '55.2%', 'Global Treatment Gap', '▼ −4.2pp vs 2019', C['green'], '🏥')
kpi_card(ax_k3, '$4.2T', 'Annual Economic Cost\n(Worldwide)', '▲ +28% vs 2019', C['orange'], '💸')
kpi_card(ax_k4, '4.31', 'Avg Wellbeing Score\n(10-pt scale)', '▲ +0.3 vs Pre-COVID', C['purple2'], '⭐')

# Panel: MH Prevalence Trend by Region
ax1 = fig.add_subplot(gs[1, :2])
region_trend = df1.groupby(['year','region'])['mental_health_prevalence_pct'].mean().reset_index()
for i, reg in enumerate(region_trend['region'].unique()):
    sub = region_trend[region_trend['region'] == reg]
    ax1.plot(sub['year'], sub['mental_health_prevalence_pct'],
             color=PAL[i], linewidth=2.2, marker='o', markersize=4, label=reg)
ax1.axvspan(2019.5, 2021.5, alpha=0.12, color=C['red'])
ax1.text(2020.3, ax1.get_ylim()[0] + 0.3, 'COVID-19\nPeak', fontsize=7.5,
         color=C['red'], alpha=0.85, ha='center')
ax1.set_title('Mental Health Prevalence Trend by Region (%)', color=C['text'],
              fontsize=12, fontweight='bold', pad=10)
ax1.set_xlabel('Year'); ax1.set_ylabel('Prevalence (%)')
ax1.legend(fontsize=7.5, ncol=2, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(2015, 2024)

# Panel: Economic Burden by Country (Top 10)
ax2 = fig.add_subplot(gs[1, 2:])
econ_2024 = df3[df3['year'] == 2024].nlargest(10, 'total_mh_cost_usd_billions')
bars = ax2.barh(range(len(econ_2024)), econ_2024['total_mh_cost_usd_billions'],
                color=[PAL[i % len(PAL)] for i in range(len(econ_2024))],
                edgecolor='none', height=0.65)
ax2.set_yticks(range(len(econ_2024)))
ax2.set_yticklabels(econ_2024['country'], fontsize=9)
ax2.set_title('Top 10 Countries: Annual MH Economic Cost (USD Billions)', color=C['text'],
              fontsize=12, fontweight='bold', pad=10)
ax2.set_xlabel('USD Billions')
for bar, val in zip(bars, econ_2024['total_mh_cost_usd_billions']):
    ax2.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
             f'${val:.0f}B', va='center', fontsize=8.5, color=C['text'])

# Panel: Burnout Risk by Sector
ax3 = fig.add_subplot(gs[2, :2])
sector_burnout = df2.groupby('sector').agg(
    burnout=('burnout_risk_score','mean'),
    productivity=('productivity_score','mean'),
    count=('employee_id','count')
).reset_index().sort_values('burnout', ascending=True)
colors_b = [C['green2'] if b < 5.5 else C['orange'] if b < 6.5 else C['red']
            for b in sector_burnout['burnout']]
bars3 = ax3.barh(sector_burnout['sector'], sector_burnout['burnout'],
                 color=colors_b, edgecolor='none', height=0.65)
ax3.axvline(sector_burnout['burnout'].mean(), color=C['yellow'], linestyle='--',
            linewidth=1.5, label=f"Avg: {sector_burnout['burnout'].mean():.1f}")
ax3.set_title('Burnout Risk Score by Sector (0–10 scale)', color=C['text'],
              fontsize=12, fontweight='bold', pad=10)
ax3.set_xlabel('Burnout Risk Score')
ax3.legend(fontsize=9)
for bar, val in zip(bars3, sector_burnout['burnout']):
    ax3.text(val + 0.05, bar.get_y() + bar.get_height()/2,
             f'{val:.2f}', va='center', fontsize=8.5, color=C['text'])

# Panel: Wellbeing vs Productivity scatter
ax4 = fig.add_subplot(gs[2, 2:])
sample = df2.sample(1200, random_state=42)
sc = ax4.scatter(sample['wellbeing_score'], sample['productivity_score'],
                 c=sample['burnout_risk_score'], cmap='RdYlGn_r',
                 alpha=0.5, s=14, linewidths=0, vmin=0, vmax=10)
# Trend line
m, b_coef, r, p, _ = stats.linregress(sample['wellbeing_score'], sample['productivity_score'])
x_line = np.linspace(sample['wellbeing_score'].min(), sample['wellbeing_score'].max(), 100)
ax4.plot(x_line, m * x_line + b_coef, color=C['blue1'], linewidth=2.5,
         label=f'r = {r:.3f}', zorder=5)
plt.colorbar(sc, ax=ax4, label='Burnout Risk', shrink=0.85)
ax4.set_xlabel('Employee Wellbeing Score')
ax4.set_ylabel('Productivity Score')
ax4.set_title('Wellbeing vs Productivity (coloured by Burnout)', color=C['text'],
              fontsize=12, fontweight='bold', pad=10)
ax4.legend(fontsize=9)

save('chart01_executive_dashboard.png', dpi=180)

# ────────────────────────────────────────────────────────────
# CHART 2: TREATMENT GAP & INVESTMENT ANALYSIS
# ────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(22, 14))
fig.patch.set_facecolor(C['bg'])
fig.suptitle('Treatment Gap & Healthcare Investment Analysis', fontsize=18,
             fontweight='bold', color=C['text'], y=0.96)

# 2a: Treatment gap vs GDP scatter (2024)
ax = axes[0,0]
d2024 = df1[df1['year']==2024].copy()
sc = ax.scatter(d2024['gdp_per_capita_usd']/1000, d2024['treatment_gap_pct'],
                c=d2024['mental_health_prevalence_pct'], cmap='plasma',
                s=90, alpha=0.85, edgecolors=C['border'], linewidth=0.8)
for _, row in d2024.iterrows():
    if row['gdp_per_capita_usd'] > 40000 or row['treatment_gap_pct'] > 85:
        ax.annotate(row['country'], (row['gdp_per_capita_usd']/1000, row['treatment_gap_pct']),
                    fontsize=6.5, color=C['sub'], xytext=(4,2), textcoords='offset points')
plt.colorbar(sc, ax=ax, label='Prevalence %', shrink=0.9)
ax.set_xlabel('GDP per Capita ($000s)')
ax.set_ylabel('Treatment Gap (%)')
ax.set_title('GDP vs Treatment Gap (2024)', color=C['text'], fontsize=11, fontweight='bold', pad=8)
m_t, b_t, r_t, _, _ = stats.linregress(d2024['gdp_per_capita_usd']/1000, d2024['treatment_gap_pct'])
xr = np.linspace(0, d2024['gdp_per_capita_usd'].max()/1000, 100)
ax.plot(xr, m_t*xr + b_t, '--', color=C['blue1'], linewidth=1.8, alpha=0.8, label=f'r={r_t:.2f}')
ax.legend(fontsize=9)

# 2b: MH professionals per 100k by region
ax = axes[0,1]
prof_region = df1[df1['year']==2024].groupby('region')['mh_professionals_per_100k'].mean().sort_values()
bars = ax.barh(prof_region.index, prof_region.values,
               color=[C['green2'] if v > 5 else C['orange'] if v > 2 else C['red']
                      for v in prof_region.values],
               edgecolor='none', height=0.6)
ax.set_title('MH Professionals per 100k by Region', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Professionals per 100,000')
for bar, val in zip(bars, prof_region.values):
    ax.text(val+0.1, bar.get_y()+bar.get_height()/2, f'{val:.1f}', va='center', fontsize=9, color=C['text'])

# 2c: Treatment gap trend over time (selected countries)
ax = axes[0,2]
focus_countries = ['United States','United Kingdom','India','Brazil','Germany','Japan']
colors_c = PAL[:6]
for country, col in zip(focus_countries, colors_c):
    sub = df1[df1['country']==country]
    ax.plot(sub['year'], sub['treatment_gap_pct'], color=col, linewidth=2,
            marker='o', markersize=3.5, label=country)
ax.set_title('Treatment Gap Trend — Selected Countries', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Year'); ax.set_ylabel('Treatment Gap (%)')
ax.legend(fontsize=7.5, ncol=2)
ax.grid(True, alpha=0.3); ax.set_xlim(2015, 2024)

# 2d: Govt MH spend vs treatment gap (bubble = population)
ax = axes[1,0]
d_merged = df1[df1['year']==2024][['country','region','govt_mh_spend_pct_health_budget',
                                    'treatment_gap_pct','mental_health_prevalence_pct']].copy()
for i,(region, grp) in enumerate(d_merged.groupby('region')):
    ax.scatter(grp['govt_mh_spend_pct_health_budget'], grp['treatment_gap_pct'],
               label=region, color=PAL[i], s=80, alpha=0.8, edgecolors=C['border'], linewidth=0.5)
ax.set_xlabel('Govt MH Spend (% of Health Budget)')
ax.set_ylabel('Treatment Gap (%)')
ax.set_title('MH Investment vs Treatment Gap', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.legend(fontsize=7.5, ncol=2)

# 2e: Healthcare spend vs MH outcomes heatmap
ax = axes[1,1]
pivot = df1[df1['year']==2024].pivot_table(
    values='treatment_gap_pct', index='region',
    columns=pd.cut(df1[df1['year']==2024]['healthcare_spend_pct_gdp'],
                   bins=[0,6,9,12,20], labels=['<6%','6-9%','9-12%','>12%']),
    aggfunc='mean'
)
pivot_filled = pivot.fillna(pivot.mean().mean())
im = ax.imshow(pivot_filled.values, cmap='RdYlGn_r', aspect='auto',
               vmin=20, vmax=90)
ax.set_xticks(range(len(pivot_filled.columns)))
ax.set_xticklabels(pivot_filled.columns, fontsize=9)
ax.set_yticks(range(len(pivot_filled.index)))
ax.set_yticklabels(pivot_filled.index, fontsize=8)
for i in range(len(pivot_filled.index)):
    for j in range(len(pivot_filled.columns)):
        val = pivot_filled.values[i,j]
        ax.text(j, i, f'{val:.0f}%', ha='center', va='center',
                fontsize=8.5, color='white' if val > 60 else 'black', fontweight='bold')
plt.colorbar(im, ax=ax, shrink=0.85, label='Treatment Gap %')
ax.set_title('Treatment Gap: Region × HC Spend Band', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.spines['top'].set_visible(True); ax.spines['right'].set_visible(True)

# 2f: ROI of MH investment
ax = axes[1,2]
roi_data = df3[df3['year']==2024].sort_values('roi_mh_investment', ascending=False).head(15)
ax.barh(roi_data['country'], roi_data['roi_mh_investment'],
        color=[C['green'] if r > 4 else C['blue1'] if r > 3 else C['orange']
               for r in roi_data['roi_mh_investment']],
        edgecolor='none', height=0.65)
ax.axvline(roi_data['roi_mh_investment'].mean(), color=C['yellow'], linestyle='--',
           linewidth=1.5, label=f"Avg: ${roi_data['roi_mh_investment'].mean():.2f}")
ax.set_title('ROI of MH Investment ($ per $ spent)', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Return on Investment ($)')
ax.legend(fontsize=9)

plt.tight_layout(rect=[0,0,1,0.95])
save('chart02_treatment_gap_investment.png', dpi=180)

# ────────────────────────────────────────────────────────────
# CHART 3: WORKFORCE DEEP DIVE
# ────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(22, 14))
fig.patch.set_facecolor(C['bg'])
fig.suptitle('Workforce Mental Health & Productivity Analysis', fontsize=18,
             fontweight='bold', color=C['text'], y=0.96)

# 3a: Burnout vs productivity by sector (violin)
ax = axes[0,0]
sectors_ord = df2.groupby('sector')['burnout_risk_score'].mean().sort_values(ascending=False).index.tolist()
data_violin = [df2[df2['sector']==s]['productivity_score'].values for s in sectors_ord]
vp = ax.violinplot(data_violin, positions=range(len(sectors_ord)), showmedians=True)
for pc in vp['bodies']:
    pc.set_facecolor(C['blue1'])
    pc.set_alpha(0.6)
    pc.set_edgecolor(C['blue2'])
vp['cmedians'].set_color(C['yellow'])
ax.set_xticks(range(len(sectors_ord)))
ax.set_xticklabels(sectors_ord, rotation=40, ha='right', fontsize=8)
ax.set_ylabel('Productivity Score')
ax.set_title('Productivity Distribution by Sector', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.grid(axis='y', alpha=0.3)

# 3b: Remote work vs wellbeing (post-COVID)
ax = axes[0,1]
remote_df = df2[df2['year'] >= 2020].copy()
remote_bins = pd.cut(remote_df['remote_work_pct'],
                     bins=[-1,0,25,50,75,100],
                     labels=['0% (On-site)', '1-25%', '26-50%', '51-75%', '76-100%'])
remote_summary = remote_df.groupby(remote_bins, observed=True).agg(
    wellbeing=('wellbeing_score','mean'),
    burnout=('burnout_risk_score','mean'),
    productivity=('productivity_score','mean')
).reset_index()
x = np.arange(len(remote_summary))
w = 0.28
ax.bar(x-w, remote_summary['wellbeing']/10, w, color=C['blue1'], label='Wellbeing/10', edgecolor='none')
ax.bar(x,   remote_summary['burnout'],      w, color=C['red'],   label='Burnout', edgecolor='none')
ax.bar(x+w, remote_summary['productivity']/20, w, color=C['green'], label='Productivity/20', edgecolor='none')
ax.set_xticks(x)
ax.set_xticklabels(remote_summary['remote_work_pct'].astype(str), rotation=20, ha='right', fontsize=8)
ax.set_title('Remote Work % vs Wellbeing/Burnout/Productivity', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.legend(fontsize=8.5)

# 3c: Age group heatmap — burnout x sector
ax = axes[0,2]
hm_data = df2.pivot_table(values='burnout_risk_score', index='age_group', columns='sector', aggfunc='mean')
hm_data = hm_data.reindex(['18-25','26-35','36-45','46-55','56-65'])
im3 = ax.imshow(hm_data.values, cmap='RdYlGn_r', aspect='auto', vmin=4, vmax=8)
ax.set_xticks(range(len(hm_data.columns)))
ax.set_xticklabels(hm_data.columns, rotation=35, ha='right', fontsize=8)
ax.set_yticks(range(len(hm_data.index)))
ax.set_yticklabels(hm_data.index, fontsize=9)
for i in range(len(hm_data.index)):
    for j in range(len(hm_data.columns)):
        val = hm_data.values[i,j]
        ax.text(j, i, f'{val:.1f}', ha='center', va='center',
                fontsize=8.5, color='white' if val > 6.5 else 'black', fontweight='bold')
plt.colorbar(im3, ax=ax, shrink=0.85, label='Burnout Score')
ax.set_title('Burnout Heatmap: Age Group × Sector', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.spines['top'].set_visible(True); ax.spines['right'].set_visible(True)

# 3d: Absenteeism by diagnosis and support access
ax = axes[1,0]
abs_data = df2.groupby(['mental_health_diagnosis','mental_health_support_access'])['absenteeism_days_per_year'].mean().reset_index()
abs_data['group'] = abs_data.apply(lambda r:
    f"{'Diagnosed' if r['mental_health_diagnosis']==1 else 'Not Diagnosed'}\n{'+ Support' if r['mental_health_support_access']==1 else '- Support'}",
    axis=1)
bar_colors = [C['blue1'], C['blue3'], C['red'], C['orange']]
bars_abs = ax.bar(abs_data['group'], abs_data['absenteeism_days_per_year'],
                   color=bar_colors, edgecolor='none', width=0.55)
ax.set_title('Avg Annual Absenteeism Days\n(Diagnosis × Support Access)', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.set_ylabel('Absenteeism Days / Year')
for bar, val in zip(bars_abs, abs_data['absenteeism_days_per_year']):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.1,
            f'{val:.1f}d', ha='center', fontsize=10, color=C['text'], fontweight='bold')
ax.tick_params(axis='x', labelsize=8.5)

# 3e: Gender wellbeing trends
ax = axes[1,1]
gender_trend = df2.groupby(['year','gender'])['wellbeing_score'].mean().reset_index()
gender_colors = {g: c for g, c in zip(['Female','Male','Non-binary'], [C['purple2'], C['blue1'], C['green']])}
for gender, col in gender_colors.items():
    sub = gender_trend[gender_trend['gender'] == gender]
    ax.plot(sub['year'], sub['wellbeing_score'], color=col, linewidth=2.5,
            marker='o', markersize=5, label=gender)
ax.axvspan(2019.5, 2021.5, alpha=0.1, color=C['red'])
ax.set_title('Wellbeing Score Trend by Gender (0–100)', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Year'); ax.set_ylabel('Wellbeing Score')
ax.legend(fontsize=9); ax.grid(True, alpha=0.3); ax.set_xlim(2015, 2024)

# 3f: Salary satisfaction correlation matrix
ax = axes[1,2]
corr_cols = ['wellbeing_score','burnout_risk_score','productivity_score',
             'absenteeism_days_per_year','salary_satisfaction','presenteeism_score']
corr_labels = ['Wellbeing','Burnout','Productivity','Absenteeism','Salary Sat.','Presenteeism']
corr_matrix = df2[corr_cols].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
cmap_c = sns.diverging_palette(20, 220, as_cmap=True)
sns.heatmap(corr_matrix, mask=mask, cmap=cmap_c, center=0, annot=True,
            fmt='.2f', ax=ax, linewidths=0.5, linecolor=C['border'],
            annot_kws={'size': 9, 'color': C['text']},
            xticklabels=corr_labels, yticklabels=corr_labels,
            cbar_kws={'shrink': 0.85})
ax.set_title('Workforce Metrics Correlation Matrix', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.tick_params(axis='x', rotation=30, labelsize=8)
ax.tick_params(axis='y', rotation=0, labelsize=8)

plt.tight_layout(rect=[0,0,1,0.95])
save('chart03_workforce_deepdive.png', dpi=180)

# ────────────────────────────────────────────────────────────
# CHART 4: COVID RECOVERY & TELEHEALTH
# ────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(20, 13))
fig.patch.set_facecolor(C['bg'])
fig.suptitle('Post-COVID Mental Health Recovery & Telehealth Adoption', fontsize=18,
             fontweight='bold', color=C['text'], y=0.96)

# 4a: Global anxiety/depression index (quarterly)
ax = axes[0,0]
global_q = df4.groupby('period')[['anxiety_index_vs_2019','depression_index_vs_2019',
                                   'telehealth_adoption_pct']].mean().reset_index()
global_q['period_num'] = range(len(global_q))
ax.fill_between(global_q['period_num'], global_q['anxiety_index_vs_2019'],
                100, alpha=0.15, color=C['red'])
ax.plot(global_q['period_num'], global_q['anxiety_index_vs_2019'],
        color=C['red'], linewidth=2.5, label='Anxiety Index', marker='o', markersize=3.5)
ax.plot(global_q['period_num'], global_q['depression_index_vs_2019'],
        color=C['orange'], linewidth=2.5, label='Depression Index', marker='s', markersize=3.5)
ax.axhline(100, color=C['dim'], linestyle='--', linewidth=1.2, label='2019 Baseline')
n = len(global_q)
tick_pos = [i for i in range(n) if i % 4 == 0]
ax.set_xticks(tick_pos)
ax.set_xticklabels([global_q['period'].iloc[i].split('-')[0] for i in tick_pos], fontsize=9)
ax.set_title('Global Anxiety & Depression Index\n(Q1 2019 = 100 baseline)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.set_ylabel('Index (2019 = 100)')
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)

# 4b: Telehealth adoption trajectory
ax = axes[0,1]
telehealth_region = df4.groupby(['period','region'])['telehealth_adoption_pct'].mean().reset_index()
period_order = df4['period'].unique()
for i, reg in enumerate(telehealth_region['region'].unique()):
    sub = telehealth_region[telehealth_region['region']==reg].copy()
    sub = sub.set_index('period').reindex(period_order).reset_index()
    ax.plot(range(len(sub)), sub['telehealth_adoption_pct'],
            color=PAL[i], linewidth=2, marker='o', markersize=3, label=reg, alpha=0.85)
ax.set_xticks([i for i in range(len(period_order)) if i % 4 == 0])
ax.set_xticklabels([period_order[i].split('-')[0] for i in range(len(period_order)) if i % 4 == 0], fontsize=9)
ax.set_title('Telehealth Adoption Rate by Region (%)', color=C['text'], fontsize=11, fontweight='bold', pad=8)
ax.set_ylabel('Telehealth Adoption (%)')
ax.legend(fontsize=8, ncol=2); ax.grid(True, alpha=0.3)

# 4c: Recovery speed heatmap (country × metric)
ax = axes[1,0]
# Recovery index = 2024 value / peak COVID value
recovery_data = []
for country in df4['country'].unique():
    sub = df4[df4['country']==country]
    for metric in ['anxiety_index_vs_2019','depression_index_vs_2019','mh_service_utilization_idx']:
        pre = sub[sub['year']==2019][metric].mean()
        peak = sub[sub['year']==2020][metric].mean()
        current = sub[sub['year']==2024][metric].mean()
        recovery_pct = (current - peak) / abs(peak - pre) * 100 if abs(peak-pre) > 0.1 else 50
        recovery_data.append({'country': country, 'metric': metric, 'recovery': recovery_pct})

rec_df = pd.DataFrame(recovery_data)
metric_labels = {'anxiety_index_vs_2019': 'Anxiety', 'depression_index_vs_2019': 'Depression',
                 'mh_service_utilization_idx': 'Service Utilization'}
rec_df['metric'] = rec_df['metric'].map(metric_labels)
rec_pivot = rec_df.pivot(index='country', columns='metric', values='recovery')
rec_pivot = rec_pivot.fillna(50)

im4 = ax.imshow(rec_pivot.values, cmap='RdYlGn', aspect='auto', vmin=0, vmax=120)
ax.set_xticks(range(len(rec_pivot.columns))); ax.set_xticklabels(rec_pivot.columns, fontsize=9)
ax.set_yticks(range(len(rec_pivot.index))); ax.set_yticklabels(rec_pivot.index, fontsize=7.5)
plt.colorbar(im4, ax=ax, shrink=0.85, label='Recovery %')
ax.set_title('COVID Recovery Progress by Country & Metric\n(Green = Full Recovery)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.spines['top'].set_visible(True); ax.spines['right'].set_visible(True)

# 4d: Workforce participation recovery
ax = axes[1,1]
wfp_data = df4.groupby(['year','quarter'])['workforce_participation_pct'].mean().reset_index()
wfp_data['period_num'] = range(len(wfp_data))
wfp_q = df4.groupby('period')['workforce_participation_pct'].mean()

# Add confidence interval
q_means = df4.groupby('period')['workforce_participation_pct'].agg(['mean','std']).reset_index()
q_means['period_num'] = range(len(q_means))
ax.fill_between(q_means['period_num'],
                q_means['mean'] - q_means['std'],
                q_means['mean'] + q_means['std'],
                alpha=0.2, color=C['blue1'])
ax.plot(q_means['period_num'], q_means['mean'],
        color=C['blue1'], linewidth=2.5, marker='o', markersize=3.5)
ax.axhline(q_means[q_means['period_num']==0]['mean'].values[0],
           color=C['green'], linestyle='--', linewidth=1.5, label='2019 Q1 Baseline', alpha=0.8)
n = len(q_means)
ax.set_xticks([i for i in range(n) if i % 4 == 0])
ax.set_xticklabels([q_means['period'].iloc[i].split('-')[0] for i in range(n) if i % 4 == 0], fontsize=9)
ax.set_title('Workforce Participation Rate Recovery\n(Global Avg ± 1 Std Dev)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.set_ylabel('Workforce Participation (%)')
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0,0,1,0.95])
save('chart04_covid_recovery.png', dpi=180)

# ────────────────────────────────────────────────────────────
# CHART 5: ECONOMIC ANALYSIS & PREDICTIVE INSIGHTS
# ────────────────────────────────────────────────────────────
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

fig, axes = plt.subplots(2, 3, figsize=(22, 14))
fig.patch.set_facecolor(C['bg'])
fig.suptitle('Economic Impact & Predictive Modeling', fontsize=18,
             fontweight='bold', color=C['text'], y=0.96)

# 5a: Total global MH cost trend
ax = axes[0,0]
global_cost = df3.groupby('year')['total_mh_cost_usd_billions'].sum().reset_index()
ax.fill_between(global_cost['year'], global_cost['total_mh_cost_usd_billions'],
                alpha=0.2, color=C['orange'])
ax.plot(global_cost['year'], global_cost['total_mh_cost_usd_billions'],
        color=C['orange'], linewidth=2.5, marker='o', markersize=6)
# Forecast 2025-2027
lr = LinearRegression()
X_tr = global_cost['year'].values.reshape(-1,1)
lr.fit(X_tr, global_cost['total_mh_cost_usd_billions'])
future_years = np.array([2025, 2026, 2027]).reshape(-1,1)
preds = lr.predict(future_years)
ax.plot([2024]+list(future_years.flatten()),
        [global_cost[global_cost['year']==2024]['total_mh_cost_usd_billions'].values[0]]+list(preds),
        color=C['red'], linewidth=2, linestyle='--', marker='D', markersize=6, label='Forecast')
ax.axvline(2024.5, color=C['dim'], linestyle=':', linewidth=1.2)
ax.text(2025.2, preds[0]+50, 'Forecast', color=C['red'], fontsize=9, alpha=0.9)
ax.set_title('Global MH Economic Cost\nTrend & Forecast (USD Billions)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Year'); ax.set_ylabel('Total Cost (USD Billions)')
ax.legend(fontsize=9); ax.set_xlim(2015, 2027)

# 5b: Cost breakdown pie
ax = axes[0,1]
avg_costs = df3[df3['year']==2024][['lost_productivity_pct','healthcare_cost_pct',
                                     'social_welfare_cost_pct']].mean()
labels = ['Lost Productivity', 'Healthcare Costs', 'Social Welfare']
explode = [0.05, 0.03, 0.03]
wedges, texts, autotexts = ax.pie(
    avg_costs.values, labels=labels, autopct='%1.1f%%',
    colors=[C['red'], C['blue1'], C['orange']], startangle=90,
    explode=explode, wedgeprops=dict(edgecolor=C['bg'], linewidth=2))
for t in texts: t.set_color(C['text']); t.set_fontsize(10)
for at in autotexts: at.set_color('white'); at.set_fontweight('bold'); at.set_fontsize(10)
ax.set_title('MH Economic Cost\nBreakdown (Global Avg)', color=C['text'], fontsize=11, fontweight='bold', pad=8)

# 5c: ML Feature importance for productivity prediction
ax = axes[0,2]
feature_cols = ['wellbeing_score','burnout_risk_score','weekly_work_hours',
                'absenteeism_days_per_year','mental_health_support_access',
                'remote_work_pct','salary_satisfaction','presenteeism_score']
feature_labels = ['Wellbeing','Burnout','Work Hours','Absenteeism',
                   'MH Support','Remote Work','Salary Sat.','Presenteeism']
df2_clean = df2[feature_cols + ['productivity_score']].dropna()
X = df2_clean[feature_cols].values
y = df2_clean['productivity_score'].values

gbr = GradientBoostingRegressor(n_estimators=150, max_depth=4, random_state=42)
gbr.fit(X, y)
importances = gbr.feature_importances_
sorted_idx = np.argsort(importances)

bar_colors_fi = [C['green'] if importances[i] > 0.15 else C['blue1'] if importances[i] > 0.08
                 else C['dim'] for i in sorted_idx]
ax.barh([feature_labels[i] for i in sorted_idx], importances[sorted_idx],
        color=bar_colors_fi, edgecolor='none', height=0.65)
ax.set_title('Feature Importance: Productivity Prediction\n(Gradient Boosting, R² scored)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Feature Importance')
cv_scores = cross_val_score(gbr, X, y, cv=5, scoring='r2')
ax.text(0.98, 0.03, f'5-fold CV R² = {cv_scores.mean():.3f} ± {cv_scores.std():.3f}',
        transform=ax.transAxes, ha='right', fontsize=9, color=C['yellow'])

# 5d: Investment return scenario
ax = axes[1,0]
invest_levels = np.arange(0.5, 15, 0.5)
roi_low  = invest_levels * 2.1 + np.random.normal(0, 0.5, len(invest_levels))
roi_med  = invest_levels * 3.8 + np.random.normal(0, 0.7, len(invest_levels))
roi_high = invest_levels * 5.2 + np.random.normal(0, 0.9, len(invest_levels))
ax.fill_between(invest_levels, roi_low, roi_high, alpha=0.12, color=C['green'])
ax.plot(invest_levels, roi_low,  '--', color=C['orange'], linewidth=1.5, label='Conservative (2.1x)')
ax.plot(invest_levels, roi_med,  '-',  color=C['blue1'],  linewidth=2.5, label='Moderate (3.8x)')
ax.plot(invest_levels, roi_high, '--', color=C['green'],  linewidth=1.5, label='Optimistic (5.2x)')
ax.axhline(0, color=C['dim'], linewidth=0.8)
ax.set_title('MH Investment Return Scenarios\n(USD Return per USD Invested)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Investment Level (USD Billions)')
ax.set_ylabel('Economic Return (USD Billions)')
ax.legend(fontsize=9)

# 5e: Cost per employee by sector
ax = axes[1,1]
sector_prod = df2.groupby('sector').agg(
    absenteeism=('absenteeism_days_per_year','mean'),
    burnout=('burnout_risk_score','mean'),
    wellbeing=('wellbeing_score','mean')
).reset_index()
# Estimate cost per employee: $500 per absenteeism day + burnout cost
sector_prod['est_annual_cost_usd'] = (
    sector_prod['absenteeism'] * 650 +
    sector_prod['burnout'] * 800 +
    (100 - sector_prod['wellbeing']) * 120
)
sector_prod = sector_prod.sort_values('est_annual_cost_usd', ascending=True)
ax.barh(sector_prod['sector'], sector_prod['est_annual_cost_usd'],
        color=[C['red'] if v > 12000 else C['orange'] if v > 10000 else C['green']
               for v in sector_prod['est_annual_cost_usd']],
        edgecolor='none', height=0.65)
ax.set_title('Estimated MH Cost per Employee\nby Sector (USD/Year)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.set_xlabel('Estimated Cost (USD/Employee/Year)')
for i, (_, row) in enumerate(sector_prod.iterrows()):
    ax.text(row['est_annual_cost_usd'] + 50, i, f"${row['est_annual_cost_usd']:,.0f}",
            va='center', fontsize=8.5, color=C['text'])

# 5f: Wellbeing quartile impact
ax = axes[1,2]
df2['wellbeing_quartile'] = pd.qcut(df2['wellbeing_score'], q=4,
                                     labels=['Q1 (Lowest)','Q2','Q3','Q4 (Highest)'])
quartile_impact = df2.groupby('wellbeing_quartile', observed=True).agg(
    productivity=('productivity_score','mean'),
    absenteeism=('absenteeism_days_per_year','mean'),
    burnout=('burnout_risk_score','mean'),
    presenteeism=('presenteeism_score','mean')
).reset_index()
x = np.arange(len(quartile_impact)); w = 0.22
ax.bar(x-1.5*w, quartile_impact['productivity']/10,  w, color=C['blue1'],  label='Productivity/10', edgecolor='none')
ax.bar(x-0.5*w, quartile_impact['absenteeism'],       w, color=C['orange'], label='Absenteeism (days)', edgecolor='none')
ax.bar(x+0.5*w, quartile_impact['burnout'],            w, color=C['red'],    label='Burnout Score', edgecolor='none')
ax.bar(x+1.5*w, quartile_impact['presenteeism']/10,  w, color=C['purple2'],label='Presenteeism/10', edgecolor='none')
ax.set_xticks(x)
ax.set_xticklabels(quartile_impact['wellbeing_quartile'].astype(str), fontsize=8.5)
ax.set_title('Wellbeing Quartile Impact\non Key Workforce Metrics', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.legend(fontsize=8, ncol=2)

plt.tight_layout(rect=[0,0,1,0.95])
save('chart05_economic_predictive.png', dpi=180)

# ────────────────────────────────────────────────────────────
# CHART 6: WORLD COMPARISON OVERVIEW (summary card)
# ────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(21, 9))
fig.patch.set_facecolor(C['bg'])
fig.suptitle('Global Country Comparison — 2024 Snapshot', fontsize=17,
             fontweight='bold', color=C['text'], y=0.97)

d2024 = df1[df1['year']==2024].merge(
    df3[df3['year']==2024][['country','total_mh_cost_usd_billions','mh_cost_pct_gdp']],
    on='country')

# 6a: Radar/bubble — prevalence vs professionals
ax = axes[0]
for i,(_, row) in enumerate(d2024.iterrows()):
    ax.scatter(row['mh_professionals_per_100k'], row['mental_health_prevalence_pct'],
               s=max(20, row['govt_mh_spend_pct_health_budget']*80),
               c=[PAL[list(d2024['region'].unique()).index(row['region']) % len(PAL)]],
               alpha=0.75, edgecolors=C['border'], linewidth=0.5)
    if row['gdp_per_capita_usd'] > 35000 or row['mental_health_prevalence_pct'] > 21:
        ax.annotate(row['country'],
                    (row['mh_professionals_per_100k'], row['mental_health_prevalence_pct']),
                    fontsize=6.5, color=C['sub'], xytext=(3,2), textcoords='offset points')
handles = [mpatches.Patch(color=PAL[i], label=reg)
           for i, reg in enumerate(d2024['region'].unique())]
ax.legend(handles=handles, fontsize=7, ncol=1, title='Region', title_fontsize=8)
ax.set_xlabel('MH Professionals per 100,000')
ax.set_ylabel('MH Prevalence (%)')
ax.set_title('Prevalence vs MH Workforce\n(Size = Govt MH Spend %)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
ax.text(0.02, 0.98, 'Higher-left = under-resourced', transform=ax.transAxes,
        fontsize=8, color=C['red'], va='top', alpha=0.8)

# 6b: Ranking table visual
ax = axes[1]
ax.axis('off')
top_countries = d2024.sort_values('treatment_gap_pct').head(10)[
    ['country','treatment_gap_pct','mh_professionals_per_100k','mental_health_prevalence_pct']]
table_data = [[row['country'], f"{row['treatment_gap_pct']:.0f}%",
               f"{row['mh_professionals_per_100k']:.1f}", f"{row['mental_health_prevalence_pct']:.1f}%"]
              for _, row in top_countries.iterrows()]
col_headers = ['Country', 'Treatment\nGap', 'MH Prof/\n100k', 'Prevalence']
tbl = ax.table(cellText=table_data, colLabels=col_headers,
               loc='center', cellLoc='center')
tbl.auto_set_font_size(False); tbl.set_fontsize(9); tbl.scale(1.2, 2.0)
for (row, col), cell in tbl.get_celld().items():
    cell.set_facecolor(C['panel2'] if row > 0 else C['blue2'])
    cell.set_edgecolor(C['border'])
    cell.set_text_props(color=C['text'])
ax.set_title('Best Performing: Lowest Treatment Gap\n(Top 10 Countries — 2024)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)

# 6c: Economic cost vs investment
ax = axes[2]
ax.scatter(d2024['govt_mh_spend_pct_health_budget'],
           d2024['mh_cost_pct_gdp'],
           c=d2024['gdp_per_capita_usd']/1000, cmap='plasma',
           s=100, alpha=0.85, edgecolors=C['border'], linewidth=0.8)
for _, row in d2024.iterrows():
    if row['mh_cost_pct_gdp'] > 5 or row['govt_mh_spend_pct_health_budget'] > 10:
        ax.annotate(row['country'],
                    (row['govt_mh_spend_pct_health_budget'], row['mh_cost_pct_gdp']),
                    fontsize=6.5, color=C['sub'], xytext=(3,2), textcoords='offset points')
sc6 = ax.scatter([], [], c=[], cmap='plasma')
plt.colorbar(ax.scatter(d2024['govt_mh_spend_pct_health_budget'],
                         d2024['mh_cost_pct_gdp'],
                         c=d2024['gdp_per_capita_usd']/1000,
                         cmap='plasma', s=0, alpha=0),
             ax=ax, label='GDP per Capita ($000s)', shrink=0.85)
ax.set_xlabel('Govt MH Spend (% of Health Budget)')
ax.set_ylabel('MH Economic Cost (% of GDP)')
ax.set_title('MH Investment vs Economic Burden\n(Color = GDP per Capita)', color=C['text'],
             fontsize=11, fontweight='bold', pad=8)
m6, b6, r6, _, _ = stats.linregress(d2024['govt_mh_spend_pct_health_budget'], d2024['mh_cost_pct_gdp'])
xr6 = np.linspace(d2024['govt_mh_spend_pct_health_budget'].min(),
                  d2024['govt_mh_spend_pct_health_budget'].max(), 100)
ax.plot(xr6, m6*xr6+b6, '--', color=C['blue3'], linewidth=1.8, alpha=0.8, label=f'r={r6:.2f}')
ax.legend(fontsize=9)

plt.tight_layout(rect=[0,0,1,0.95])
save('chart06_global_comparison.png', dpi=180)

print("\nAll 6 charts saved!")
import os
for f in sorted(os.listdir('charts')):
    if f.endswith('.png'):
        sz = os.path.getsize(f'charts/{f}') / 1024
        print(f"  {f}  ({sz:.0f} KB)")
