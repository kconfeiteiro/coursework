import pandas as pd
from helpers import list_dir, prepare_data, read_isochrones
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
    "read kwargs": {"sep": r"\s+", "comment": "#", "on_bad_lines": "skip"},
    "columns": "B B-V".split(),
    "sun vals": (3.761, 0),
}

(
    ISO1,
    ISO2,
    ISO3,
    ISO4,
    ISO5,
) = read_isochrones(
    *CONFIG["isochrones"]["paths"],
    **CONFIG["read kwargs"],
)


# setting up isochrones for plotting
ISO1, ISO2, ISO3, ISO4, ISO5 = prepare_data(ISO1, ISO2, ISO3, ISO4, ISO5)

# my cluster (cluster #8)
CLUSTER_8 = pd.read_csv(CONFIG["cluster8"]["path"], **CONFIG["read kwargs"])
CLUSTER_8["B"] = CLUSTER_8["B-V"] + CLUSTER_8["V"]
DATA = (CLUSTER_8["B-V"], CLUSTER_8["B"])

# plot
FIG, AXES = plt.subplots()
AXES.scatter(*DATA, s=5, label="Cluster 8")
AXES.scatter(*ISO1, label="ISO 1", s=1)
AXES.scatter(*ISO2, label="ISO 2", s=1)
AXES.scatter(*ISO3, label="ISO 3", s=1)
AXES.scatter(*ISO4, label="ISO 4", s=1)
AXES.scatter(*ISO5, label="ISO 5", s=1)
AXES.set_ylabel("Magnitude (B)")
AXES.set_xlabel("Color Index (B-V)")
AXES.set_title("CMD - Cluster 8")
AXES.invert_yaxis()
AXES.legend()
plt.show()
