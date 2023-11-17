from math import sqrt
from typing import Any, NamedTuple

import numpy as np
import pandas as pd


def gaussian(x, mean, stdev):
    return np.exp(-(((x - mean) / stdev) ** 2) / 2) / (stdev * np.sqrt(2 * np.pi))


def calc_area(srange=(-10, 10, 100), **kwargs):
    """
    Calculates the 'area' of a given set of data over a finite range.

    Parameters
    ----------
    srange : tuple, optional
        The range of your x-values, by default (-10, 10, 100)

    Returns
    -------
    Float or int
        The sum of your dataset.
    """
    _x, _dx = np.linspace(srange, retstep=True, **kwargs)
    return sum(gaussian(_x)) * _dx


def deriv_approx(data, func, step):
    """
    Approximates a first-order derivative for a given function.

    Parameters
    ----------
    data : Sequence
        That data that you will use to approximate the derivative of
    func : Callable
        The mathematical function that you are approximating the derivative of
    step : int or float
        The step or "dx" that you will use to approximate

    Returns
    -------
    Sequence
        A numerical sequence of the estimated first-order derivative values
    """
    approx = lambda x: ((func(x + step) - step)) / step
    return list(map(approx, data))


def find_indx(col, condition):
    """
    Finds the index of a value or condition of a given list.

    Parameters
    ----------
    col : Sequence
        The numerical sequence that you want to search the value for
    condition :
        The conditional statement you use to find said value

    Returns
    -------
    int
        The index of the value based on your conditional statement
    """
    return col.index(condition)


def read_data(*paths, **kwargs):
    """
    Reads files of similar data.

    Returns
    -------
    Tuple
        Returns tuple of `pd.DataFrame` objects
    """
    DATA = tuple(pd.read_csv(path, **kwargs) for path in paths)
    return DATA[0] if len(paths) == 1 else DATA


def split_df(dataframe: pd.DataFrame = None):
    """
    Splits your dataframe into separate columns based on their columns.

    Parameters
    ----------
    dataframe : pd.DataFrame, optional
        The dataframe that you want to split, by default None

    Returns
    -------
    Tuple of `pd.DataFrame` objects
        Returns a Tuple of `pd.DataFrame` objects
    """
    return tuple([dataframe[col] for col in dataframe.columns])
