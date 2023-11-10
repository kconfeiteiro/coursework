import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_data(
    filenames,
    columns=None,
    labels=None,
    as_type=None,
    skip_rows=2,
    **kwargs,
):
    read_data = []
    for i, file in enumerate(filenames):
        DATA = pd.read_csv(file, **kwargs)

        if skip_rows:
            DATA = DATA.iloc[skip_rows:, :]
            DATA = DATA.reset_index()

        if columns:
            DATA = DATA[columns]

        if as_type:
            DATA = DATA.astype(as_type)

        if labels:
            DATA["Sort"] = labels[i]

        read_data.append(DATA)

    return read_data if len(filenames) > 1 else read_data[0]


def list_dir(rel_path):
    ABS = os.path.abspath(rel_path)
    listed_paths = os.listdir(rel_path)
    prepend = lambda path: os.path.join(ABS, path)
    return list(map(prepend, listed_paths))


def separate(dataframe):
    return tuple(dataframe[col] for col in dataframe.columns)


def add_track(axis, data, label):
    axis.plot(data, label=label)


def fix_data(*dataframes):
    returns = []
    for data in dataframes:
        data.sort_values(data.columns[0], inplace=True)
        data = data.astype(np.float64)
        data = (data.iloc[:, 1], data.iloc[:, 0])
        returns.append(data)

    return tuple(returns)


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

track0, track1, track2, track3, track4 = fix_data(
    *tuple(
        read_data(
            CONFIG["isochrones"]["paths"],
            columns=CONFIG["plotted columns"],
            **CONFIG["read kwargs"],
        )
    )
)

star1_path = "DATA\\EVOLUTION_TRACKS\\m00-8.tsv"
star2_path = "DATA\\EVOLUTION_TRACKS\\m1-00.tsv"

star1, star2 = tuple(
    read_data(
        [star1_path, star2_path],
        columns=CONFIG["plotted columns"],
        **CONFIG["read kwargs"],
    )
)

star1, star2 = fix_data(star1, star2)
star1, star2 = star1.iloc[2:800], star2.iloc[2:800]


fig, axes = plt.subplots()
axes.plot(*track0, label=r"$6.5$ yrs")
axes.plot(*track1, label=r"$7.5$ yrs")
axes.plot(*track2, label=r"$8.5$ yrs")
axes.plot(*track3, label=r"$9.5$ yrs")
axes.plot(*track4, label=r"$10.1$ yrs")
axes.plot(*star1, label=r"star1")
axes.plot(*star2, label=r"star2")
axes.plot(*CONFIG["sun vals"], "y", marker="o", markersize=8, label="Sun")
# axes.plot(*ZAMS, label="ZAMS")

axes.set_title("Hertzsprung-Russell (HR) Diagram")
axes.set_ylabel(r"Luminosity - $L$ [W]")
axes.set_xlabel(r"$T_{eff}$ [K]")
axes.invert_xaxis()
axes.legend()
