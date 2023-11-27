import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def list_dir(rel_path):
    ABS = os.path.abspath(rel_path)
    listed_paths = os.listdir(rel_path)
    prepend = lambda path: os.path.join(ABS, path)
    return list(map(prepend, listed_paths))


def min_max_scaling(col):
    return (col - col.min()) / (col.max() - col.min())


def read_spectra(*paths, sort_col=None, xrange=None, normalize_col=None, **kwargs):
    data = [0] * len(paths)
    for i, path in enumerate(paths):
        temp = pd.read_csv(path, **kwargs)

        if xrange and sort_col:
            temp = temp.loc[
                (temp[sort_col] >= xrange[0]) & (temp[sort_col] <= xrange[1])
            ]

        if normalize_col:
            temp[normalize_col] = min_max_scaling(temp[normalize_col])

        data[i] = temp

    if len(paths) == 1:
        return data[0]
    else:
        return tuple(data)


def split(dataframe):
    return tuple(dataframe[[col]] for col in dataframe.columns)


def uniquefilename(
    filename,
    savepath=None,
):
    base_name, ext = os.path.splitext(filename)
    unique_name, counter = filename, 1
    while os.path.exists(os.path.join(savepath, unique_name)):
        counter += 1
        unique_name = f"{base_name}({counter}){ext}"

    return (os.path.join(savepath, unique_name), counter)