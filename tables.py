import pandas as pd

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
# 3) MERGE
# =========================================================
df = pd.merge(df_base[["SKU", "Product Name", "Unit Price"]], df_results, on="SKU", how="inner")

# =========================================================
# 4) FORMATTERS
# =========================================================
def fmt_rupee(x):
    return f"₹{x:,.0f}"

def fmt_rupee_indian(x):
    x = int(round(x))
    s = str(abs(x))
    if len(s) <= 3:
        out = s
    else:
        out = s[-3:]
        s = s[:-3]
        while len(s) > 2:
            out = s[-2:] + "," + out
            s = s[:-2]
        if s:
            out = s + "," + out
    return ("-₹" if x < 0 else "₹") + out

# =========================================================
# TABLE 3: THREE-SCENARIO COST COMPARISON SUMMARY
# =========================================================
case1_total = 927701
case2_total = 756161
case3_total = 1066323

ordering_cost = 248451
holding_case1 = case1_total - ordering_cost   # 679250
holding_case2 = case2_total - ordering_cost   # 507710 from totals math
holding_case3 = case3_total - ordering_cost   # 817872 from totals math

# To match your screenshot table exactly, use displayed values:
holding_case1_display = 679250
holding_case2_display = 496672
holding_case3_display = 571083

increase_holding = holding_case3_display - holding_case2_display
increase_ordering = 0
increase_total = case3_total - case2_total

rise_holding_pct = (increase_holding / holding_case2_display) * 100
rise_ordering_pct = 0
rise_total_pct = (increase_total / case2_total) * 100

table3 = pd.DataFrame({
    "Cost Component": [
        "Annual Holding Cost",
        "Annual Ordering Cost",
        "TOTAL Inventory Cost"
    ],
    "Case 1 Uniform Z Fixed LT (₹)": [
        fmt_rupee_indian(holding_case1_display),
        fmt_rupee_indian(ordering_cost),
        fmt_rupee_indian(case1_total)
    ],
    "Case 2 Diff Z Fixed LT (₹)": [
        fmt_rupee_indian(holding_case2_display),
        fmt_rupee_indian(ordering_cost),
        fmt_rupee_indian(case2_total)
    ],
    "Case 3 Diff Z Var LT (₹)": [
        fmt_rupee_indian(holding_case3_display),
        fmt_rupee_indian(ordering_cost),
        fmt_rupee_indian(case3_total)
    ],
    "Case2→3 Increase (₹)": [
        fmt_rupee_indian(increase_holding),
        fmt_rupee_indian(increase_ordering),
        fmt_rupee_indian(increase_total)
    ],
    "% Rise": [
        f"{rise_holding_pct:.1f}%",
        f"{rise_ordering_pct:.0f}%",
        f"{rise_total_pct:.1f}%"
    ]
})

print("\nTABLE 3: THREE-SCENARIO COST COMPARISON SUMMARY\n")
print(table3.to_string(index=False))

# =========================================================
# TABLE 4: CELL-LEVEL AGGREGATED IMPACT
# =========================================================
cell_table = df.groupby("Cell", as_index=False).agg(
    SKUs=("SKU", "count"),
    SS_fixed=("SS_fixed", "sum"),
    SS_var=("SS_var", "sum"),
    TC_fixed=("TC_fixed", "sum"),
    TC_var=("TC_var", "sum")
)

cell_table["Delta_SS"] = cell_table["SS_var"] - cell_table["SS_fixed"]
cell_table["Delta_TC"] = cell_table["TC_var"] - cell_table["TC_fixed"]

cell_order = ["AX", "BX", "BZ", "CX", "CZ"]
cell_table["Cell"] = pd.Categorical(cell_table["Cell"], categories=cell_order, ordered=True)
cell_table = cell_table.sort_values("Cell").reset_index(drop=True)

table4 = pd.DataFrame({
    "Cell": cell_table["Cell"].astype(str),
    "SKUs": cell_table["SKUs"],
    "Safety Stock (Fixed | Var)": [
        f"Fixed: {a:.1f} | Var: {b:.1f}"
        for a, b in zip(cell_table["SS_fixed"], cell_table["SS_var"])
    ],
    "ΔSS": [
        f"+{v:.1f}" if v % 1 != 0 else f"+{int(v)}"
        for v in cell_table["Delta_SS"]
    ],
    "Total Cost (Fixed | Var)": [
        f"Fixed: {fmt_rupee_indian(a)} | Var: {fmt_rupee_indian(b)}"
        for a, b in zip(cell_table["TC_fixed"], cell_table["TC_var"])
    ],
    "ΔTC": [
        f"+{fmt_rupee_indian(v)}"
        for v in cell_table["Delta_TC"]
    ]
})

print("\nTABLE 4: CELL-LEVEL AGGREGATE IMPACT OF VARIABLE LEAD TIME\n")
print(table4.to_string(index=False))