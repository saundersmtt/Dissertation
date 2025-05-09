import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime, timedelta

# Milestone data (label, start date)
milestones = [
    ("Start DMPC + 2024 Mg2+ sims", "2025-05-06"),
    ("Finish 1000 ns sims", "2025-05-27"),
    ("Finish POPC Mg2+ paper", "2025-05-31"),
    ("Analyze and compare with POPC", "2025-06-11"),
    ("Draft and revise POPC/DMPC paper", "2025-06-26"),
    ("Submit POPC/DMPC paper", "2025-07-05"),
    ("Incorporate final chapter into dissertation", "2025-07-15"),
    ("Revise full dissertation", "2025-07-25"),
    ("Defense preparation and edits", "2025-08-04"),
    ("Dissertation defense", "2025-08-11"),
    ("Submit final ETD", "2025-08-18"),
]

# Convert strings to datetime
milestones = [(label, datetime.strptime(date, "%Y-%m-%d")) for label, date in milestones]

# Generate end dates
bars = []
for i, (label, start) in enumerate(milestones):
    end = milestones[i + 1][1] if i + 1 < len(milestones) else start + timedelta(days=5)
    bars.append((label, start, end))

# Custom OPES-inspired palette (trimmed to remove pale yellow)
color_stops = [
    "#081d58", "#253494", "#225ea8", "#1d91c0", "#41b6c4", "#7fcdbb",
    # removed "#c7e9b4",  # <- pale yellow
    "#ffffcc", "#fed976", "#fd8d3c", "#e31a1c", "#800026"
]
trimmed_cmap = LinearSegmentedColormap.from_list("trimmed_opes", color_stops, N=256)

# Plot the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))
for i, (label, start, end) in enumerate(bars):
    ax.barh(label, (end - start).days, left=start, height=0.4, color=trimmed_cmap(i / len(bars)))

# Axis formatting
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.title("Dissertation Gantt Timeline (Adjusted OPES Palette)")
plt.tight_layout()
plt.grid(axis='x')

plt.show()

