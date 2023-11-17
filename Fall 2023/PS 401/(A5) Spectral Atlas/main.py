import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def list_dir(rel_path):
    ABS = os.path.abspath(rel_path)
    listed_paths = os.listdir(rel_path)
    prepend = lambda path: os.path.join(ABS, path)
    return list(map(prepend, listed_paths))


def read_file(*paths, columns=None, as_type=None, **kwargs):
    read_data = []
    for file in paths:
        DATA = pd.read_csv(file, **kwargs)

        if columns:
            DATA = DATA[columns]

        if as_type:
            DATA = DATA.astype(as_type)

        read_data.append(DATA)

    return read_data if len(paths) > 1 else read_data[0]


CONFIG = {
    "columns": "lk   ukf_g8v   uks_g8v        fh       fse        fl         fd".split(),
    "files": list_dir("DATA"),
}
