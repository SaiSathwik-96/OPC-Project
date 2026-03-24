import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

# =========================================================
# 1) ORIGINAL DATASET
# =========================================================
demand_data = {
    "SKU": [
        "SP-001","SP-002","SP-003","SP-004","SP-005","SP-006","SP-007","SP-008","SP-009","SP-010",
        "SP-011","SP-012","SP-013","SP-014","SP-015","SP-016","SP-017","SP-018","SP-019","SP-020"
    ],
    "Product Name": [
        "Engine Control Unit","Alloy Wheel Rim","LED Headlight Assembly","ABS Actuator","Radiator Core",
        "Fuel Injector Nozzle","Brake Disc Rotor","Shock Absorber","Alternator Belt","Air Filter Element",
        "Oil Filter","Spark Plug (Platinum)","Brake Pads (Front Set)","Wiper Blade Set","Coolant Reservoir Cap",
        "Battery Terminal","Fuses (Assorted)","Plastic Trim Clips","Rubber O-Rings","Copper Washer"
    ],
    "Unit Price": [
        15000,12000,8500,9800,4200,3500,2800,2200,1200,850,
        450,350,1100,650,250,150,80,10,5,8
    ],
    "Jan": [45,10,120,20,150,80,200,50,400,600,1000,200,350,50,100,500,1200,500,2000,100],
    "Feb": [42,55,115,22,140,85,210,250,390,580,980,800,340,500,95,480,1150,4500,1950,1500],
    "Mar": [48,5,125,19,160,78,195,30,410,620,1020,150,360,30,105,520,1250,200,2050,50],
    "Apr": [44,80,118,21,145,82,205,180,395,590,990,950,345,450,98,490,1180,6000,1980,1800],
    "May": [46,12,122,20,155,81,200,40,405,610,1010,100,355,40,102,510,1220,100,2020,80],
    "Jun": [43,60,119,23,142,84,208,220,398,595,995,700,342,480,99,495,1190,4800,1990,1600],
    "Jul": [47,8,121,18,158,79,198,60,402,605,1005,250,358,60,101,505,1210,400,2010,120],
    "Aug": [45,45,117,21,148,83,202,190,400,600,1000,850,348,420,97,500,1170,5500,1970,1700],
    "Sep": [44,15,123,20,152,80,205,35,395,590,990,120,352,35,103,490,1230,300,2030,90],
    "Oct": [46,70,120,22,150,82,200,210,408,615,1015,900,350,470,100,515,1200,5200,2000,1550],
    "Nov": [45,10,118,19,145,81,197,45,397,598,998,180,345,45,98,498,1180,150,1980,110],
    "Dec": [44,50,122,21,155,83,203,200,405,605,1005,750,355,440,102,505,1220,4900,2020,1650]
}

df_base = pd.DataFrame(demand_data)

# =========================================================
# 2) FINAL RESULTS DATASET PROVIDED BY YOU
# =========================================================
results_data = {
    "SKU": [
        "SP-001","SP-002","SP-003","SP-004","SP-005","SP-006","SP-007","SP-008","SP-009","SP-010",
        "SP-011","SP-012","SP-013","SP-014","SP-015","SP-016","SP-017","SP-018","SP-019","SP-020"
    ],
    "Cell": [
        "AX","BZ","AX","CX","AX","BX","AX","BZ","AX","AX",
        "AX","CZ","BX","CZ","CX","CX","CX","CZ","CX","CZ"
    ],
    "mu_LT": [
        1.0,1.5,1.0,1.3,1.0,1.2,1.0,1.5,1.0,1.0,
        1.0,1.8,1.2,1.8,1.3,1.3,1.3,1.8,1.3,1.8
    ],
    "sigma_LT": [
        0.10,0.40,0.10,0.25,0.10,0.20,0.10,0.40,0.10,0.10,
        0.10,0.55,0.20,0.55,0.25,0.25,0.25,0.55,0.25,0.55
    ],
    "SS_fixed": [
        3.9,35.4,6.5,2.4,14.7,4.1,10.4,112.7,13.7,26.3,
        26.3,365.6,12.3,227.3,4.6,18.6,46.1,2676.8,46.1,840.9
    ],
    "SS_var": [
        11.2,46.9,28.7,8.9,37.9,32.3,48.2,152.4,94.3,142.4,
        234.6,566.6,137.9,337.3,41.6,207.6,497.8,3912.1,826.7,1231.4
    ],
    "Delta_SS": [
        7.3,11.5,22.2,6.5,23.2,28.2,37.7,39.6,80.6,116.1,
        208.4,201.0,125.5,109.9,37.0,189.0,451.7,1235.3,780.5,390.4
    ],
    "ROP_fixed": [
        48.8,70.4,126.5,22.9,164.7,85.6,212.4,238.6,414.1,626.9,
        1026.9,861.4,362.3,479.0,104.6,519.3,1246.1,5389.3,2046.1,1703.4
    ],
    "ROP_var": [
        56.1,99.4,148.7,35.5,187.9,130.1,250.1,341.1,494.7,743.1,
        1235.3,1459.1,557.9,790.3,171.6,858.5,2057.8,8794.6,3426.7,2783.9
    ],
    "TC_fixed": [
        51931,116681,60553,26635,51206,29001,42683,75383,37241,39472,
        35239,45998,33112,49368,7977,13984,15917,13422,4945,5415
    ],
    "TC_var": [
        73724,144309,98283,39369,70723,48743,63823,92820,56589,59213,
        53991,60067,60728,63659,9825,19654,23144,15893,5726,6040
    ]
}

df_results = pd.DataFrame(results_data)

# =========================================================
# 3) MERGE BOTH DATASETS
# =========================================================
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

df_base["Annual Demand"] = df_base[months].sum(axis=1)
df_base["Mean Monthly Demand"] = df_base[months].mean(axis=1)
df_base["Std Monthly Demand"] = df_base[months].std(axis=1, ddof=1)
df_base["Annual Consumption Value"] = df_base["Annual Demand"] * df_base["Unit Price"]

df = pd.merge(df_base, df_results, on="SKU", how="inner")
df["ABC"] = df["Cell"].str[0]
df["XYZ"] = df["Cell"].str[1]

# This fixes Figure 6 to match your report-style output
df["Additional_Holding_Cost"] = df["TC_var"] - df["TC_fixed"]

# =========================================================
# 4) COLORS
# =========================================================
cell_colors = {
    "AX": "#1f77b4",
    "BX": "#3aa657",
    "BZ": "#e28b47",
    "CX": "#a56cc1",
    "CZ": "#d04f3b"
}
df["Color"] = df["Cell"].map(cell_colors)

def lakh_fmt(x, pos):
    return f"₹{x/100000:.1f}L"

df = df.sort_values("SKU").reset_index(drop=True)
x = np.arange(len(df))
w = 0.34

# =========================================================
# FIGURE 1: Safety Stock Comparison
# =========================================================
fig, ax = plt.subplots(figsize=(16, 7))
ax.bar(x - w/2, df["SS_fixed"], width=w, color="#5aa1c2", label="Fixed LT")
ax.bar(x + w/2, df["SS_var"], width=w, color="#e96b75", label="Variable LT")

ax.set_xticks(x)
ax.set_xticklabels(df["SKU"], rotation=45, ha="right")
for tick, color in zip(ax.get_xticklabels(), df["Color"]):
    tick.set_color(color)

for i, d in enumerate(df["Delta_SS"]):
    if d > 50:
        y = max(df.loc[i, "SS_fixed"], df.loc[i, "SS_var"])
        ax.text(i + w/2, y + df["SS_var"].max()*0.02, f"+{int(round(d))}",
                ha="center", va="bottom", fontsize=8, color="#d94841", fontweight="bold")

legend_items = [
    Patch(facecolor="#5aa1c2", label="Fixed LT"),
    Patch(facecolor="#e96b75", label="Variable LT"),
    Patch(facecolor=cell_colors["AX"], label="AX"),
    Patch(facecolor=cell_colors["BX"], label="BX"),
    Patch(facecolor=cell_colors["BZ"], label="BZ"),
    Patch(facecolor=cell_colors["CX"], label="CX"),
    Patch(facecolor=cell_colors["CZ"], label="CZ"),
]
ax.legend(handles=legend_items, ncol=7, loc="upper right", fontsize=9)
ax.set_title("Safety Stock Comparison: Fixed LT vs Variable LT\n(by SKU, colored by ABC-XYZ Cell)", fontweight="bold")
ax.set_ylabel("Safety Stock (Units)")
ax.grid(True, linestyle="--", alpha=0.25)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()

# =========================================================
# FIGURE 2: Incremental Safety Stock
# =========================================================
fig, ax = plt.subplots(figsize=(16, 6))
ax.bar(df["SKU"], df["Delta_SS"], color=df["Color"], width=0.72)

for i, v in enumerate(df["Delta_SS"]):
    ax.text(i, v + df["Delta_SS"].max()*0.01, f"{int(round(v))}",
            ha="center", va="bottom", fontsize=8)

ax.legend(
    handles=[
        Patch(facecolor=cell_colors["AX"], label="AX"),
        Patch(facecolor=cell_colors["BX"], label="BX"),
        Patch(facecolor=cell_colors["BZ"], label="BZ"),
        Patch(facecolor=cell_colors["CX"], label="CX"),
        Patch(facecolor=cell_colors["CZ"], label="CZ"),
    ],
    title="ABC-XYZ Cell", ncol=5, loc="upper left", fontsize=9
)

ax.set_title("Incremental Safety Stock from Variable Lead Time (ΔSS = SS_var − SS_fixed)", fontweight="bold")
ax.set_ylabel("Additional Safety Stock (Units)")
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df["SKU"], rotation=45, ha="right", fontsize=9)
ax.grid(True, linestyle="--", alpha=0.25)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()

# =========================================================
# FIGURE 3: Three-Scenario Cost Comparison
# =========================================================
case1_total = 927701
case2_total = 756161
case3_total = 1066323
ordering_total = 248451
holding_case2 = case2_total - ordering_total
holding_case3 = case3_total - ordering_total

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Inventory Cost Impact of Variable Lead Time", fontsize=15, fontweight="bold")

scenario_labels = [
    "Case 1\n(Uniform Z,\nFixed LT)",
    "Case 2\n(Diff Z,\nFixed LT)",
    "Case 3\n(Diff Z,\nVariable LT)"
]
total_costs = [case1_total, case2_total, case3_total]

ax1 = axes[0]
ax1.bar(np.arange(3), total_costs, color=["#9aa7a9", "#2e86ab", "#ef4b57"], width=0.5)
ax1.set_title("Total Annual Cost — 3 Scenarios", fontsize=11, fontweight="bold")
ax1.set_ylabel("Total Annual Inventory Cost (₹)")
ax1.set_xticks(np.arange(3))
ax1.set_xticklabels(scenario_labels, fontsize=9)
ax1.yaxis.set_major_formatter(FuncFormatter(lakh_fmt))
ax1.grid(axis="y", linestyle="--", alpha=0.3)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
for i, v in enumerate(total_costs):
    ax1.text(i, v + max(total_costs)*0.02, f"₹{v:,.0f}", ha="center", va="bottom", fontsize=8, fontweight="bold")

ax2 = axes[1]
x2 = np.arange(2)
holding_vals = [holding_case2, holding_case3]
ordering_vals = [ordering_total, ordering_total]
totals = [case2_total, case3_total]

ax2.bar(x2, holding_vals, color="#e9636f", label="Holding Cost")
ax2.bar(x2, ordering_vals, bottom=holding_vals, color="#5aa1d6", label="Ordering Cost")
ax2.set_title("Cost Breakdown: Fixed vs Variable LT", fontsize=11, fontweight="bold")
ax2.set_ylabel("Annual Cost (₹)")
ax2.set_xticks(x2)
ax2.set_xticklabels(["Case 2\n(Fixed LT)", "Case 3\n(Variable LT)"], fontsize=9)
ax2.yaxis.set_major_formatter(FuncFormatter(lakh_fmt))
ax2.grid(axis="y", linestyle="--", alpha=0.3)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.legend(loc="upper left", fontsize=8)

for i in range(2):
    ax2.text(x2[i], holding_vals[i] / 2, f"₹{holding_vals[i]:,.0f}",
             ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    ax2.text(x2[i], totals[i] + max(total_costs)*0.02, f"₹{totals[i]:,.0f}",
             ha="center", va="bottom", fontsize=8, fontweight="bold")

plt.tight_layout()
plt.show()

# =========================================================
# FIGURE 4: Reorder Point Comparison
# =========================================================
fig, ax = plt.subplots(figsize=(16, 7))
ax.bar(x - w/2, df["ROP_fixed"], width=w, color="#56b870", label="ROP Fixed LT")
ax.bar(x + w/2, df["ROP_var"], width=w, color="#e69138", label="ROP Variable LT")

ax.set_xticks(x)
ax.set_xticklabels(df["SKU"], rotation=45, ha="right")
for tick, color in zip(ax.get_xticklabels(), df["Color"]):
    tick.set_color(color)

ax.legend(handles=[
    Patch(facecolor="#56b870", label="ROP Fixed LT"),
    Patch(facecolor="#e69138", label="ROP Variable LT"),
    Patch(facecolor=cell_colors["AX"], label="AX"),
    Patch(facecolor=cell_colors["BX"], label="BX"),
    Patch(facecolor=cell_colors["BZ"], label="BZ"),
    Patch(facecolor=cell_colors["CX"], label="CX"),
    Patch(facecolor=cell_colors["CZ"], label="CZ"),
], ncol=7, loc="upper right", fontsize=9)

ax.set_title("Reorder Point Comparison: Fixed LT vs Variable LT\n(higher ROP with Variable LT = earlier trigger)", fontweight="bold")
ax.set_ylabel("Reorder Point (units)")
ax.grid(True, linestyle="--", alpha=0.25)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()

# =========================================================
# FIGURE 5: sigma_LT vs Delta_SS Scatter
# =========================================================
fig, ax = plt.subplots(figsize=(10, 7))
for _, row in df.iterrows():
    ax.scatter(
        row["sigma_LT"], row["Delta_SS"],
        s=row["Annual Consumption Value"] / 5000,
        color=row["Color"],
        alpha=0.85,
        edgecolors="white",
        linewidth=0.7
    )
    ax.text(row["sigma_LT"] + 0.003, row["Delta_SS"] + 10, row["SKU"], fontsize=7)

ax.legend(handles=[
    Patch(color=cell_colors["AX"], label="AX"),
    Patch(color=cell_colors["BX"], label="BX"),
    Patch(color=cell_colors["BZ"], label="BZ"),
    Patch(color=cell_colors["CX"], label="CX"),
    Patch(color=cell_colors["CZ"], label="CZ")
], title="ABC-XYZ Cell", loc="upper left", fontsize=8, title_fontsize=9)

ax.set_title("σ_LT vs Incremental Safety Stock\n(bubble size ∝ Annual Consumption Value)", fontweight="bold")
ax.set_xlabel("Lead Time Std Dev (σ_LT, months)")
ax.set_ylabel("Additional Safety Stock from Variable LT (units)")
ax.grid(True, linestyle="--", alpha=0.25)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()

# =========================================================
# FIGURE 6: Additional Annual Holding Cost per SKU
# fixed to use report totals difference
# =========================================================
plot_df = df.sort_values("Additional_Holding_Cost", ascending=False).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(15, 6))
ax.bar(plot_df["SKU"], plot_df["Additional_Holding_Cost"], color=plot_df["Color"], width=0.8)

for i, v in enumerate(plot_df["Additional_Holding_Cost"]):
    ax.text(
        i,
        v + plot_df["Additional_Holding_Cost"].max() * 0.01,
        f"₹{v:,.0f}",
        ha="center",
        va="bottom",
        fontsize=8,
        rotation=55,
        color="dimgray"
    )

ax.legend(handles=[
    Patch(facecolor=cell_colors["AX"], label="AX"),
    Patch(facecolor=cell_colors["BX"], label="BX"),
    Patch(facecolor=cell_colors["BZ"], label="BZ"),
    Patch(facecolor=cell_colors["CX"], label="CX"),
    Patch(facecolor=cell_colors["CZ"], label="CZ"),
], title="ABC-XYZ Cell", ncol=5, loc="upper right", fontsize=8, title_fontsize=9, frameon=True)

ax.set_title("Additional Annual Holding Cost per SKU due to Variable Lead Time", fontsize=12, fontweight="bold")
ax.set_ylabel("Additional Annual Holding Cost (₹)")
ax.set_xticks(np.arange(len(plot_df)))
ax.set_xticklabels(plot_df["SKU"], rotation=45, ha="right", fontsize=9)
ax.grid(True, linestyle="--", alpha=0.25)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()

# =========================================================
# FIGURE 7: Safety Stock sensitivity heatmaps (Top 4 by SS impact)
# =========================================================
top4 = df.sort_values("Delta_SS", ascending=False).head(4).copy()

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
axes = axes.flatten()

for ax, (_, row) in zip(axes, top4.iterrows()):
    mu_lt_grid = np.linspace(0.5, 3.0, 80)
    sigma_lt_grid = np.linspace(0.0, 0.8, 80)
    MU_LT, SIGMA_LT = np.meshgrid(mu_lt_grid, sigma_lt_grid)

    z_val = row["SS_fixed"] / (row["Std Monthly Demand"] * np.sqrt(row["mu_LT"]))
    ss_grid = z_val * np.sqrt(
        MU_LT * (row["Std Monthly Demand"] ** 2) +
        (row["Mean Monthly Demand"] ** 2) * (SIGMA_LT ** 2)
    )

    contour = ax.contourf(MU_LT, SIGMA_LT, ss_grid, levels=25, cmap="YlOrRd")
    ax.scatter(row["mu_LT"], row["sigma_LT"], color="white", marker="*", s=40, label="Current")
    ax.set_title(
        f"{row['SKU']} — {row['Product Name']}\n"
        f"(z={z_val:.2f}, μ_D={row['Mean Monthly Demand']:.1f}, σ_D={row['Std Monthly Demand']:.1f})",
        fontsize=8
    )
    ax.set_xlabel("Mean Lead Time μ_LT (months)", fontsize=8)
    ax.set_ylabel("Lead Time Std Dev σ_LT (months)", fontsize=8)
    ax.tick_params(labelsize=7)
    ax.legend(fontsize=6, loc="upper right")
    cbar = fig.colorbar(contour, ax=ax, shrink=0.82)
    cbar.ax.tick_params(labelsize=6)

fig.suptitle("Safety Stock Sensitivity Heatmap\n(μ_LT vs σ_LT — Top 4 items by SS impact)", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()

# =========================================================
# FIGURE 8: Cell-Level Aggregate Analysis
# =========================================================
agg_df = df.groupby("Cell", as_index=False).agg({
    "SS_fixed": "sum",
    "SS_var": "sum",
    "TC_fixed": "sum",
    "TC_var": "sum"
})

cell_order = ["AX", "BX", "BZ", "CX", "CZ"]
agg_df["Cell"] = pd.Categorical(agg_df["Cell"], categories=cell_order, ordered=True)
agg_df = agg_df.sort_values("Cell")

x3 = np.arange(len(agg_df))
w2 = 0.35

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Cell-Level Impact of Variable Lead Time", fontsize=15, fontweight="bold")

# Left: Aggregate Safety Stock
ax1 = axes[0]
ax1.bar(x3 - w2/2, agg_df["SS_fixed"], width=w2, color="#5aa1c2", label="Fixed LT")
ax1.bar(x3 + w2/2, agg_df["SS_var"], width=w2, color="#e96b75", label="Variable LT")
ax1.set_title("Aggregate Safety Stock by ABC-XYZ Cell", fontsize=11, fontweight="bold")
ax1.set_ylabel("Total Safety Stock (units)")
ax1.set_xticks(x3)
ax1.set_xticklabels(agg_df["Cell"])
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.25)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# Right: Aggregate Cost
ax2 = axes[1]
ax2.bar(x3 - w2/2, agg_df["TC_fixed"], width=w2, color="#5aa1c2", label="Fixed LT")
ax2.bar(x3 + w2/2, agg_df["TC_var"], width=w2, color="#e96b75", label="Variable LT")
ax2.set_title("Aggregate Inventory Cost by ABC-XYZ Cell", fontsize=11, fontweight="bold")
ax2.set_ylabel("Total Annual Inventory Cost (₹)")
ax2.set_xticks(x3)
ax2.set_xticklabels(agg_df["Cell"])
ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"₹{int(x/1000)}K"))
ax2.legend()
ax2.grid(True, linestyle="--", alpha=0.25)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()

# =========================================================
# OPTIONAL TABLE OUTPUT
# =========================================================
print(df[[
    "SKU", "Cell", "mu_LT", "sigma_LT", "SS_fixed", "SS_var", "Delta_SS",
    "ROP_fixed", "ROP_var", "TC_fixed", "TC_var", "Additional_Holding_Cost"
]].to_string(index=False))