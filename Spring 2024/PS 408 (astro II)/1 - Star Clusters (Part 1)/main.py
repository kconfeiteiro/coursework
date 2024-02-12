"""
Star Cluster assignment (Part 1) -- PS 408-02DB Spring 2024

Module Information
------------------
Workspace: 1 - Star Clusters (Part 1)
FIlename: main.py
Path: main.py
Date: February, 06 2024

Objectives
------
1. Plot isochrones from the given ranges
2. Overlay your cluster's data
3. Manually adjust the cluster's y-axis data from (2) to match the best isochrone
"""
import pandas as pd
from helpers import calculate_distance, list_dir, prepare_data, read_isochrones, percent_error
from matplotlib import pyplot as plt

# assignment configuration dictionary
CFG = {
    "isochrones": {
        "paths": list_dir("DATA/ISOCHRONES"),
        "ages": "6.5 7.5 8.5 9.5 10.1".split(),
    },
    "cluster8": {"path": "DATA/cluster8.txt", "masses": "DATA/c8_w_masses.txt"},
    "read kwargs": {"sep": r"\s+", "comment": "#", "on_bad_lines": "skip"},
    "columns": "B B-V".split(),
    "dist-mod-1": 10.5,
    "actual-dist-mod": 13.93,
    "reddening-C8": 2.5482,
    "actual-C8-dist": 1886,
    "calculated-distance": 1258.93,
    "R_V": 3.1,
    "actual cluster age": 6.822,
    "est. cluter age": 7.5,
}

# read data
(
    ISO1,
    ISO2,
    ISO3,
    ISO4,
    ISO5,
) = read_isochrones(
    *CFG["isochrones"]["paths"],
    **CFG["read kwargs"],
)

# setting up isochrones for plotting
ISO1, ISO2, ISO3, ISO4, ISO5 = prepare_data(ISO1, ISO2, ISO3, ISO4, ISO5)

# my cluster (cluster #8)
CLUSTER_8 = pd.read_csv(CFG["cluster8"]["path"], **CFG["read kwargs"])
C8_MASSES = pd.read_csv(CFG["cluster8"]["masses"], **CFG["read kwargs"])
if CFG["dist-mod-1"]:
    CLUSTER_8["V-part1"] = CLUSTER_8["V"] - CFG["dist-mod-1"]

if CFG["reddening-C8"]:
    CLUSTER_8["reddened"] = CLUSTER_8["V"] + CFG["reddening-C8"]

DATA = (CLUSTER_8["B-V"], CLUSTER_8["V-part1"])
DATA_R = (CLUSTER_8["B-V"], CLUSTER_8["reddened"])

# estimate distance using distance modulus (w/ extinction)
c8_distance = calculate_distance(CFG["dist-mod-1"])

# calculate the reddening for cluster 8
c8_av = CFG["reddening-C8"] * CFG["R_V"]
print("\nCalculated Av value for cluster #8: ", c8_av)

# plot cluster & isochrones
fig, axes = plt.subplots()
fig.tight_layout()

axes.set_title(f"Color Magnitude Diagram (CMD)")
axes.set_ylabel(r"$V_{mag}$")
axes.set_xlabel(r"$B-V$")

axes.scatter(*DATA, s=5, label=r"Cluster 8")
axes.scatter(*DATA_R, s=12, marker="*", label=r"Corrected")
axes.plot(*ISO1, label="6.5 Myr")
axes.plot(*ISO2, label="7.5 Myr")
axes.plot(*ISO3, label="8.5 Myr")
axes.plot(*ISO4, label="9.5 Myr")
axes.plot(*ISO5, label="10.1 Myr")

axes.invert_yaxis()
axes.arrow(
    x=0,
    y=10,
    dx=0,
    dy=-5,
    linestyle="-",
    capstyle="projecting",
    width=0.075,
    head_width=0.2,
    head_length=1,
)
axes.legend(loc="lower right")

# plot histogram of masses
fig2, axes2 = plt.subplots()
axes2.hist(C8_MASSES.Mass)
axes2.set_xlabel(r"Masses $(M/M_\odot)$")
axes2.set_title(r"IC 1805 Histogram of Masses $(M/M_\odot)$")
fig2.tight_layout()
plt.show()

# calculate percent errors
dist_mod_percent_err = percent_error(CFG["dist-mod-1"], CFG["actual-dist-mod"])
distance_percent_err = percent_error(CFG["calculated-distance"], CFG["actual-C8-dist"])
cluster_age_percent_err = percent_error(CFG["est. cluter age"], CFG["actual cluster age"])

print(f"Distance modulus percent error {dist_mod_percent_err * 100:.04f}%")
print(f"Cluster distance percent error {distance_percent_err * 100:.04f}%")
print(f"Cluster age percent error {cluster_age_percent_err * 100:.04f}%")
