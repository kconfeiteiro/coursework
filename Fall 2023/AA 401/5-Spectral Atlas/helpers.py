import os

import pandas as pd
from natsort import natsorted


def list_dir(rel_path, reversed=False, return_dict=False, natsort=True):
    ABS = os.path.abspath(rel_path)
    prepend = lambda path: os.path.join(ABS, path)

    listed_paths = os.listdir(rel_path)
    read_files = list(map(prepend, listed_paths))
    if natsort:
        read_files = natsorted(read_files)

    if return_dict:
        return {f"{i}": data for i, data in enumerate(read_files)}
    else:
        return read_files[::-1] if reversed else read_files


def normalize(col, min_max_scaling=False):
    if min_max_scaling:
        return (col - col.min()) / (col.max() - col.min())
    else:
        return col / col.max()


def read_spectra(
    *paths,
    sort_col=None,
    xrange=None,
    normalize_col=None,
    min_max_scaling=False,
    **kwargs,
):
    data = [0] * len(paths)
    for i, path in enumerate(paths):
        temp = pd.read_csv(path, **kwargs)

        if xrange and sort_col:
            temp = temp.loc[
                (temp[sort_col] >= xrange[0]) & (temp[sort_col] <= xrange[1])
            ]

        if normalize_col:
            temp[normalize_col] = normalize(
                temp[normalize_col], min_max_scaling=min_max_scaling
            )

        data[i] = temp

    return data[0] if len(paths) == 1 else tuple(data)


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
