import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import list_dir, read_data


CONFIG = {
    "isochrones": {
        "paths": list_dir("DATA\\ISOCHRONES"),
        "ages": "6.5 7.5 8.5 9.5 10.1".split(),
    },
    "tracks": {
        "paths": list_dir("DATA\\EVOLUTION_TRACKS"),
        "masses": "0.8 0.9 1 1.1 1.25 1.35 1.5 3 4 7 20 25 32 85 120".split(),
    },
    "read kwargs": {"delim_whitespace": True, "comment": "#", "on_bad_lines": "skip"},
    "plotted columns": ["logL", "logTe"],
    "sun vals": (3.761, 0),

}

track_data_ZAMS = pd.concat(
    read_data(
        CONFIG["tracks"]["paths"],
        columns=CONFIG["plotted columns"],
        **CONFIG["read kwargs"],
    ),
)

isochrones = read_data(
    CONFIG["tracks"]["paths"],
    columns=CONFIG["plotted columns"],
    **CONFIG["read kwargs"],
)

print(isochrones[0])
