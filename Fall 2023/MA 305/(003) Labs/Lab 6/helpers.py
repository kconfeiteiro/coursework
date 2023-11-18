from math import sqrt
from typing import Any, NamedTuple

import numpy as np
import pandas as pd


class Stats(NamedTuple):
    avg: int | float = None
    min: int | float = None
    max: int | float = None
    product: int | float = None
    stdev: int | float = None
    variance: int | float = None
    median: int | float = None


class Norms(NamedTuple):
    transpose: Any = None
    innerprod: Any = None
    mcolsum: int | float = None
    mrowsum: int | float = None
    sqrtsum: int | float = None


def find_indx(col, condition):
    return col.index(condition)


def stats(*datasets):
    """
    Returns statistical information about an array.

    Parameters
    ----------
    data : List or NumPy array
        List or array that you want to describe.

    Returns
    -------
    _type_
        _description_
    """
    _stats = tuple(
        Stats(
            avg=sum(data) / len(data),
            min=np.argmin(data),
            max=np.argmax(data),
            product=np.prod(data),
            stdev=np.std(data),
            variance=np.std(data) ** 2,
            median=np.median(data),
        )
        for data in datasets
    )
    return _stats[0] if len(datasets) == 1 else _stats


def display_table(data):
    """
    Displays data in a formatted table

    Parameters
    ----------
    data : ArrayLike
        Data you want to print.
    """
    for i, point in enumerate(data):
        print("{0:2d} \t {1:5.2f}".format(i, point))


def read_data(*paths, **kwargs):
    """
    Reads files of similar data.

    Returns
    -------
    Tuple
        Returns tuple of `pd.DataFrame` objects
    """
    return (pd.read_csv(path, **kwargs) for path in paths)


def create_matrix(cols, rows):
    matrix = np.zeros((rows, cols))
    for j in range(cols):
        for i in range(rows):
            matrix[i, j] = ((-1) ** (i + j)) * (2 * i + j)

    return matrix


def solve_tridiag(matrix, f):
    """
    Solves a tridiagonal matrix system [a c b][x] = [f]

    a (Sequence[int]):
        [0, a1, a2, ...,an-1] sub-diagonal
    b (Sequence[int]):
        [b0, b1, b2, ...,bn-2,0] super-diagonal
    c (Sequence[int]):
        [c0, c1, c2, ...,cn-1] leading-diagonal
    x (Sequence[int]):
        [x0,x1,...,xn-1] unknown vector
    f (Sequence[int]):
        [f0,f1,...,fn-1] right hand side vector
    """
    # a, b, c
    a = np.diagonal(matrix, -1)
    b = np.diagonal(matrix, +1)
    c = np.diagonal(matrix, 0)

    n = len(a)
    y, alpha, beta = np.zeros(n), np.zeros(n), np.zeros(n)

    alpha[1] = -b[0] / c[0]
    beta[1] = f[0] / c[0]

    for i in range(1, n - 1):
        alpha[i + 1] = -b[i] / (a[i] * alpha[i] + c[i])
        beta[i + 1] = (f[i] - a[i] * beta[i]) / (a[i] * alpha[i] + c[i])

    y[n - 1] = (f[n - 1] - a[n - 1] * beta[n - 1]) / (
        c[n - 1] + a[n - 1] * alpha[n - 1]
    )

    for i in reversed(range(n - 1)):
        y[i] = alpha[i + 1] * y[i + 1] + beta[i + 1]

    return y


def matrix_ops(matrix):
    B = matrix.transpose()
    return Norms(
        transpose=B,
        innerprod=np.dot(matrix, B),
        mcolsum=max(sum(col) for col in list(matrix)),
        mrowsum=max(sum(col) for col in list(B)),
        sqrtsum=sqrt(sum(i**2 for i in matrix.flatten())),
    )


def read_n_prep(*paths, **kwargs):
    READ_DATA = [np.loadtxt(path).flatten() for path in paths]
    return pd.DataFrame(READ_DATA, **kwargs).transpose()


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


def separate(*cols, dataframe):
    if len(cols) > 1:
        return tuple(dataframe[col] for col in cols)
    else:
        return dataframe[cols]
