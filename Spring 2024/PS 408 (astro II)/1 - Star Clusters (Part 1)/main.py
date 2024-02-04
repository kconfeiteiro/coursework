import pandas as pd
from helpers import list_dir, read_data
from matplotlib import pyplot as plt

CONFIG = {
    "isochrones": {
        "paths": list_dir("DATA\\ISOCHRONES"),
        "ages": "6.5 7.5 8.5 9.5 10.1".split(),
    },
    "tracks": {
        "paths": list_dir("DATA\\EVOLUTION_TRACKS"),
        "masses": "0.8 0.9 1 1.1 1.25 1.35 1.5 3 4 7 20 25 32 85 120".split(),
    },
    "cluster8": {"path": "DATA\\cluster8.txt"},
    "read kwargs": {"delim_whitespace": True, "comment": "#", "on_bad_lines": "skip"},
    "plotted columns": ["logL", "logTe"],
    "sun vals": (3.761, 0),
}

TRACK_DATA_ZAMS = read_data(
    CONFIG["tracks"]["paths"],
    **CONFIG["read kwargs"],
)

ISOCHRONES = read_data(
    CONFIG["tracks"]["paths"],
    **CONFIG["read kwargs"],
)

CLUSTER_8 = pd.read_csv(CONFIG["cluster8"]["path"], **CONFIG["read kwargs"])
CLUSTER_8["B"] = CLUSTER_8[CLUSTER_8.columns[1]] + CLUSTER_8[CLUSTER_8.columns[2]]
DATA = (CLUSTER_8["B-V"], CLUSTER_8["B"])

FIG, AXES = plt.subplots()
AXES.scatter(*DATA, s=5, label="Cluster 8")
AXES.set_ylabel("Magnitude (B)")
AXES.set_xlabel("Color Index (B-V)")
AXES.set_title("CMD - Cluster 8")
AXES.legend()
plt.show()
