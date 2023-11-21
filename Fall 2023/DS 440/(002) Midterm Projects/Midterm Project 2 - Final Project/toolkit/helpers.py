import re
from typing import List, Literal, Sequence, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from toolkit import SplitData


def prepare_data(
    X=None,
    y=None,
    xcols=None,
    ycol=None,
    data=None,
    test_size=0.2,
    random_state=1,
    **kwargs,
):
    if all(val for val in [xcols, ycol, data]):
        X, y = data[xcols], data[ycol]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, **kwargs
    )

    return SplitData(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)


def separate(
    dataframe: pd.DataFrame = ..., columns: Sequence[str] = None
) -> Tuple[pd.DataFrame | pd.Series]:
    cols = dataframe.columns if not columns else columns
    return tuple(dataframe[col] for col in cols)


def replacements(data):
    return {f"{key}": i for i, key in enumerate(data)}


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
