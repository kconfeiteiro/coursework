import re
from typing import Any, Callable, Dict, List, Literal, Sequence, Tuple

import dtreeviz
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree

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

    return SplitData(
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        X=X,
        y=y,
    )


def separate(
    dataframe: pd.DataFrame = ..., columns: Sequence[str] = None
) -> Tuple[pd.DataFrame | pd.Series]:
    cols = dataframe.columns if not columns else columns
    return tuple(dataframe[col] for col in cols)


def replacements(data):
    """
    Creates a dictionary of keys with enumerated values (for replacement for ML models).

    Parameters
    ----------
    data : pd.DataFrame
        Data in a Pandas DataFrame object

    Returns
    -------
    Dict[str, int]
        Dictionary of all the keys and integer values.
    """
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


def correlation_plot(
    data: pd.DataFrame = ..., save_as: str = None, display: bool = False
):
    corr_mat = data.corr()
    corr_heatmap = sns.heatmap(corr_mat, annot=True)
    figure = corr_heatmap.get_figure()

    if save_as:
        figure.savefig(save_as)

    if display:
        plt.show()


def tree_viz(
    model: Callable = ...,
    filled: bool = True,
    feature_names: Sequence[str] = ...,
    fontsize: int = 10,
    save_as: str = None,
    tight_layout: bool = True,
    figtitle: str = None,
    plt_cfg: Dict = dict(figsize=(48, 16)),
    display: bool = False,
):
    fig, axes = plt.subplots(**plt_cfg)
    plot_tree(
        model, filled=filled, feature_names=feature_names, ax=axes, fontsize=fontsize
    )

    if figtitle:
        axes.set_title(figtitle)

    if tight_layout:
        fig.tight_layout()

    if save_as:
        fig.savefig(save_as)

    if display:
        plt.show()
