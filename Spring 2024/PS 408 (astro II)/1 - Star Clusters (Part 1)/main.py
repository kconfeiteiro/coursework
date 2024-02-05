import pandas as pd
from helpers import list_dir, prepare_data, read_isochrones
from matplotlib import pyplot as plt

# assignment configuration dictionary
CFG = {
    "isochrones": {
        "paths": list_dir("DATA\\ISOCHRONES"),
        "ages": "6.5 7.5 8.5 9.5 10.1".split(),
    },
    "cluster8": {"path": "DATA\\cluster8.txt"},
    "read kwargs": {"sep": r"\s+", "comment": "#", "on_bad_lines": "skip"},
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
CLUSTER_8["B"] = CLUSTER_8["B-V"] + CLUSTER_8["V"]
DATA = (CLUSTER_8["B-V"], CLUSTER_8["B"])

# plot
FIG, AXES = plt.subplots()
AXES.scatter(*DATA, s=5, label="Cluster 8")
AXES.plot(*ISO1, label="ISO-1 (6.5)")
AXES.plot(*ISO2, label="ISO-2 (7.5)")
AXES.plot(*ISO3, label="ISO-3 (8.5)")
AXES.plot(*ISO4, label="ISO-4 (9.5)")
AXES.plot(*ISO5, label="ISO-5 (10.1)")
AXES.set_ylabel("Magnitude (B)")
AXES.set_xlabel("Color Index (B-V)")
AXES.set_title("CMD - Cluster 8")
AXES.invert_yaxis()
AXES.legend()
plt.show()
