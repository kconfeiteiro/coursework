import os
import re
from typing import List, Literal, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from toolkit import SplitData


def prepare_data(xcols, ycol, data, test_size=0.2, random_state=1, **kwargs):
    X, y = data[xcols], data[ycol]
    return SplitData(
        *train_test_split(
            X, y, test_size=test_size, random_state=random_state, **kwargs
        )
    )


def separate(
    dataframe: pd.DataFrame = ..., columns: Sequence[str] = None
) -> Tuple[pd.DataFrame | pd.Series]:
    cols = dataframe.columns if not columns else columns
    return tuple(dataframe[col] for col in cols)


# FIXME - this function does not work
def split_large_data(
    dataframe: pd.DataFrame = ...,
    n_bins: int = ...,
    save_as: str = None,
    file_etx: Literal[".csv", ".txt"] = ".txt",
) -> None:
    BINNED = [
        dataframe.iloc[i : i + n_bins, :] for i in range(0, dataframe.shape[0], n_bins)
    ]

    if save_as:
        for i, data in enumerate(BINNED):
            file = f"{save_as}_{i}.{file_etx}"
            data.to_csv(file)
            print(f"Saved '{file}' ({i}/{len(BINNED)})")
    else:
        return tuple(BINNED)


def to_txt(
    save_as: str = None,
    lines: str | List[str] = None,
    mode: Literal["w", "wb", "a"] = "w",
    **kwargs,
):
    """
    Writes string or list of strings to a text file.

    Args:
        save_as (str, optional): name to save file as. Defaults to None.
        lines (Union[str, List[str]], optional): string or list of strings to save to file. Defaults to None.
        mode (literal, optional): write mode for ExcelWriter. Defaults to 'w'.
    """

    with open(save_as, mode=mode, **kwargs) as file:
        if isinstance(lines, str):
            file.write(lines)
        else:
            for line in lines:
                file.write(line)
        file.close()


def strmatch(pattern, string):
    return bool(re.search(pattern, string))
