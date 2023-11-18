import pandas as pd


def mapfunc(data, func):
    return data, list(map(func, data))


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


def separate(*cols, dataframe):
    if len(cols) > 1:
        return tuple(dataframe[col] for col in cols)
    else:
        return dataframe[cols]
