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
from helpers import distance_modulus, list_dir, prepare_data, read_isochrones
from matplotlib import pyplot as plt

# assignment configuration dictionary
CFG = {
    "isochrones": {
        "paths": list_dir("DATA\\ISOCHRONES"),
        "ages": "6.5 7.5 8.5 9.5 10.1".split(),
    },
    "cluster8": {"path": "DATA\\cluster8.txt"},
    "read kwargs": {"sep": r"\s+", "comment": "#", "on_bad_lines": "skip"},
    "columns": "B B-V".split(),
    "sun vals": (3.761, 0),
    "y-shift": 10.5,
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
if CFG["y-shift"]:
    CLUSTER_8["V"] = CLUSTER_8["V"] - CFG["y-shift"]

DATA = (CLUSTER_8["B-V"], CLUSTER_8["V"])

# estimate distance using distance modulus (w/ extinction)
CLUSTER_DISTANCE = distance_modulus(CFG["y-shift"])

# plot
FIG, AXES = plt.subplots()
AXES.scatter(*DATA, s=5, label="Cluster 8")
AXES.plot(*ISO1, label="6.5 Myr")
AXES.plot(*ISO2, label="7.5 Myr")
AXES.plot(*ISO3, label="8.5 Myr")
AXES.plot(*ISO4, label="9.5 Myr")
AXES.plot(*ISO5, label="10.1 Myr")
AXES.set_title(f"Color Magnitude Diagram (CMD) - Cluster #8 ({CLUSTER_DISTANCE:.03f} pc)")
AXES.set_ylabel(r"$B_{mag}$")
AXES.set_xlabel(r"$B-V$")
AXES.invert_yaxis()
AXES.legend()
plt.show()
