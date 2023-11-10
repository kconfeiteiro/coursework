from typing import Literal, Sequence, Tuple

import pandas as pd


def separate(
    dataframe: pd.DataFrame = ..., columns: Sequence[str] = None
) -> Tuple[pd.DataFrame | pd.Series]:
    cols = dataframe.columns if not columns else columns
    return tuple(dataframe[col] for col in cols)


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
