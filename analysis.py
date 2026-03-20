import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.gridspec import GridSpec

# -----------------------------
# Load Data
# -----------------------------
data = pd.read_csv("data/weather_data.csv")

data.columns = data.columns.str.strip()
data.columns = ["Date", "Temperature", "WindSpeed", "WaveHeight"]

data["Date"] = pd.to_datetime(data["Date"])

# -----------------------------
# Feature Engineering
# -----------------------------
data["Risk"] = data["WindSpeed"] * data["WaveHeight"]

def check_safety(risk):
    if risk < 20:
        return "Safe"
    elif risk < 40:
        return "Moderate"
    else:
        return "Danger"

data["Safety"] = data["Risk"].apply(check_safety)

# Rolling averages
data["Wave_Rolling"] = data["WaveHeight"].rolling(3).mean()
data["Wind_Rolling"] = data["WindSpeed"].rolling(3).mean()

# Correlation
corr = data["WindSpeed"].corr(data["WaveHeight"])
print("Correlation (Wind vs Wave):", round(corr, 2))

# -----------------------------
# Dashboard Layout (GridSpec)
# -----------------------------
plt.style.use("default")

fig = plt.figure(figsize=(18, 11), facecolor='#f8f9fa')

gs = GridSpec(3, 2, height_ratios=[1, 1, 1.2], figure=fig)

fig.suptitle(
    "Ship Route Weather Analysis Dashboard",
    fontsize=22, fontweight='bold', y=0.96
)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[2, :])

# -----------------------------
# Color Mapping
# -----------------------------
colors = data["Safety"].map({
    "Safe": "green",
    "Moderate": "orange",
    "Danger": "red"
})

# -----------------------------
# Panel 1: Wave Height
# -----------------------------
ax1.bar(data["Date"], data["WaveHeight"], color=colors, alpha=0.85)
ax1.plot(data["Date"], data["Wave_Rolling"], color="#0066cc", linestyle="--", linewidth=2)

ax1.axhline(y=2.0, color="#FFA500", linestyle=":", linewidth=2)
ax1.axhline(y=3.5, color="#CC0000", linestyle=":", linewidth=2)

ax1.set_title("Wave Height Over Time", fontweight='bold')
ax1.set_ylabel("Wave Height (m)")
ax1.grid(True, linestyle='--', alpha=0.3)

# -----------------------------
# Panel 2: Wind Speed
# -----------------------------
ax2.plot(data["Date"], data["WindSpeed"], color="#0099ff", marker='o', linewidth=2)
ax2.plot(data["Date"], data["Wind_Rolling"], color="#0066cc", linestyle="--", linewidth=2)

ax2.axhline(y=30, color="#CC0000", linestyle=":", linewidth=2)

ax2.set_title("Wind Speed Over Time", fontweight='bold')
ax2.set_ylabel("Wind Speed (km/h)")
ax2.grid(True, linestyle='--', alpha=0.3)

# -----------------------------
# Panel 3: Scatter
# -----------------------------
ax3.scatter(data["WindSpeed"], data["WaveHeight"], c=colors, s=80, edgecolors='black')
ax3.set_title("Wind Speed vs Wave Height", fontweight='bold')
ax3.set_xlabel("Wind Speed (km/h)")
ax3.set_ylabel("Wave Height (m)")
ax3.grid(True, linestyle='--', alpha=0.3)

# -----------------------------
# Panel 4: Pie Chart
# -----------------------------
counts = data["Safety"].value_counts()

ax4.pie(
    counts,
    labels=counts.index,
    autopct='%1.1f%%',
    colors=["#00AA00", "#FFA500", "#CC0000"],
    startangle=90
)

ax4.set_title("Risk Distribution", fontweight='bold')

# -----------------------------
# Panel 5: Risk Timeline
# -----------------------------
ax5.bar(data["Date"], data["WaveHeight"], color=colors)

# Value labels
for i, v in enumerate(data["WaveHeight"]):
    ax5.text(data["Date"].iloc[i], v + 0.1, f"{v:.1f}", ha='center', fontsize=7)

ax5.set_title("Daily Risk Level (Green=Safe | Orange=Moderate | Red=Danger)", fontweight='bold')
ax5.set_ylabel("Wave Height")
ax5.grid(True, axis='y', linestyle='--', alpha=0.3)

# -----------------------------
# Date Formatting (CLEAN FIX)
# -----------------------------
for ax in [ax1, ax2, ax5]:
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.tick_params(axis='x', rotation=45)

# -----------------------------
# Uniform Style
# -----------------------------
for ax in [ax1, ax2, ax3, ax4, ax5]:
    ax.set_facecolor('#ffffff')
    for spine in ax.spines.values():
        spine.set_color('#cccccc')

# -----------------------------
# Footer
# -----------------------------
fig.text(0.5, 0.01, "Marine Risk Intelligence System | Built by Malavika",
         ha='center', fontsize=10, color='gray')

# -----------------------------
# Layout Fix
# -----------------------------
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.subplots_adjust(hspace=0.4, wspace=0.25)

# Save
plt.savefig("dashboard.png", dpi=300)

plt.show()