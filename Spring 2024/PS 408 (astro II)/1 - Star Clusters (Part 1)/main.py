"""
Star Cluster assignment (Part 1) -- PS 408-02DB Spring 2024.

Module Information
------------------
Workspace: 1 - Star Clusters (Part 1)
Filename: main.py
Path: main.py
Creator: Krysitan Ojeda Confeiteiro
    - `confeitk@my.erau.edu` (work)
    - `confeitk@outlook.com` (personal)

Objectives
----------
1. Plot isochrones from the given ranges
2. Overlay your cluster"s data
3. Manually adjust the cluster"s y-axis data from (2) to match the best isochrone

Sources & References
--------------------
1. https://commons.wikimedia.org/wiki/File:Plot_of_various_initial_mass_functions.svg
    - For the functions for the IMF and the histogram
"""
import pandas as pd
from helpers import (
    calculate_distance,
    list_dir,
    prepare_data,
    read_isochrones,
    percent_error,
    salpeter55,
    kroupa01
)
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
    "dist-mod-1": 10.25, # vertical shift for best-fit isochrone
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

axes.set_title(f"Color Magnitude Diagram (CMD) - IC 1805")
axes.set_ylabel(r"$V_{mag}$")
axes.set_xlabel(r"$B-V$")

axes.scatter(*DATA, s=5, label="Reddened")
axes.scatter(*DATA_R, s=12, marker="*", label="De-reddened")
axes.plot(*ISO1, label="6.5 Myr")
axes.plot(*ISO2, label="7.5 Myr")
axes.plot(*ISO3, label="8.5 Myr")
axes.plot(*ISO4, label="9.5 Myr")
axes.plot(*ISO5, label="10.1 Myr")

axes.invert_yaxis()
axes.annotate(
    text="",
    xy=(0.0, -1.75),
    xytext=(-0.1, -4.15),
    fontsize=10,
    horizontalalignment="right",
    arrowprops=dict(facecolor="black", shrink=0.05),
    verticalalignment="top"
)
axes.legend(loc="lower right")

text_position = (0.3, -3.5)
axes.annotate(
    text="Reddening",
    xy=text_position,
    xytext=text_position,
    fontsize=10,
    horizontalalignment="right",
    verticalalignment="top"
)
axes.legend(loc="lower right")

# plot histogram of masses
fig2, axes2 = plt.subplots()
sorted_masses = C8_MASSES.Mass.dropna().sort_values()

# salpeter55 [1]
axes2.plot(
    sorted_masses,
    salpeter55(sorted_masses) / salpeter55(1),
    label="Salpeter 55",
    linewidth=2
)

# kroupa01 [1]
axes2.plot(
    sorted_masses,
    kroupa01(sorted_masses) / kroupa01(1),
    label="Kroupa 01",
    linewidth=2
)

axes2.hist(C8_MASSES.Mass, color="lightblue") # histogram
axes2.set_xlabel(r"Masses $(M/M_\odot)$")
axes2.set_title("IC 1805 - Histogram of Masses")
fig2.tight_layout()
axes2.legend()
plt.show()

# calculate percent errors
dist_mod_percent_err = percent_error(CFG["dist-mod-1"], CFG["actual-dist-mod"])
distance_percent_err = percent_error(CFG["calculated-distance"], CFG["actual-C8-dist"])
cluster_age_percent_err = percent_error(CFG["est. cluter age"], CFG["actual cluster age"])

print(f"Distance modulus percent error {dist_mod_percent_err * 100:.04f}%")
print(f"Cluster distance percent error {distance_percent_err * 100:.04f}%")
print(f"Cluster age percent error {cluster_age_percent_err * 100:.04f}%")
