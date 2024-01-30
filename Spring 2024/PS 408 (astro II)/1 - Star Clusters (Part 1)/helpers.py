import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def list_dir(rel_path):
    ABS = os.path.abspath(rel_path)
    listed_paths = os.listdir(rel_path)
    prepend = lambda path: os.path.join(ABS, path)
    return list(map(prepend, listed_paths))


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


def fix_data(*dataframes):
    returns = []
    for data in dataframes:
        data.sort_values(data.columns[0], inplace=True)
        data = data.astype(np.float64)
        data = (data.iloc[:, 1], data.iloc[:, 0])
        returns.append(data)

    return tuple(returns)


def plot_cmd(figsize, xlabel="Color", ylabel="Absolute Magnitude", title=None, save_as=None, **kwargs):
    fig, axes = plt.subplots(figsize=figsize, **kwargs)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_title(title)

    if save_as:
        fig.savefig(save_as)


