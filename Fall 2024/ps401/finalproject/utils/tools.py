import os

import matplotlib.pyplot as plt
from natsort import natsorted
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter


def read_starfile(*filepaths, col_names=None, read_kwargs=dict(skiprows=3)):
    file = filepaths[0]
    data = np.loadtxt(file, **read_kwargs)
    dataframe = pd.DataFrame(data, columns=col_names)
    return dataframe


def min_max_scaling(col):
    return (col - col.min()) / (col.max() - col.min())


def read_spectra(*paths, normalize_col=None, **kwargs):
    data = {}
    for i, path in enumerate(paths):
        dataframe = pd.read_csv(path, **kwargs)
        if normalize_col:
            dataframe[normalize_col] = min_max_scaling(dataframe[normalize_col])

        new_key = f"spectra{i + 1}"
        data[new_key] = dataframe
        print(f"Reading path ({i + 1}) for key '{new_key}': '{path}'")
    print(f"Read data files: {len(paths)}")
    return data


def list_dir(rel_path, reversed=False):
    ABS = os.path.abspath(rel_path)
    read_files = natsorted(list(map(lambda path: os.path.join(ABS, path), os.listdir(rel_path))))
    return read_files[::-1] if reversed else read_files


def plot_single_spectra(
    data,
    title=None,
    xtitle=None,
    ytitle=None,
    plt_kwargs=dict(tight_layout=True),
    ax=None,
    save_as=None,
    label=None,
    **plot_cfg
):
    if ax is None:
        fig, ax = plt.subplots(**plt_kwargs)
    else:
        fig = ax.get_figure()

    ax.plot(data["Wavelength"], data["Flux"], label=label, **plot_cfg)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)
    ax.set_title(title)

    if label:
        ax.legend()

    if save_as:
        print(f"Saved figure as: `{save_as}`")
        fig.savefig(save_as)


def normalize_spectra(*spectrum_data):
    normalized_data = []
    for data in spectrum_data:
        if isinstance(data, pd.DataFrame):
            normalized_flux = data["Flux"] / data["Flux"].max()
            sorted_spectrum = pd.DataFrame(
                {"Wavelength": data["Wavelength"], "Flux": normalized_flux}
            ).sort_values(by="Wavelength")
            normalized_data.append(sorted_spectrum)
        else:
            raise TypeError("Expected a DataFrame, got {}".format(type(data).__name__))
    return normalized_data if len(normalized_data) > 1 else normalized_data[0]


def split(dataframe):
    return tuple(dataframe[[col]] for col in dataframe.columns)


def chi_squared_analysis(mystery_star_df, known_star_df):
    """
    Compares the spectrum of a mystery star to a known stellar spectrum
    using interpolation and Chi-Squared analysis.

    Args:
        mystery_star_df: A Pandas DataFrame with columns "Wavelength" and "Flux"
                         containing the mystery star's spectral data.
        known_star_df: A Pandas DataFrame with columns "Wavelength" and "Flux"
                        containing the known stellar spectrum data.

    Returns:
        A tuple containing the interpolated data, Chi-Squared value, and the reduced Chi-Squared value.
    """

    # Interpolation
    x_old = mystery_star_df["Wavelength"].values
    x_grid = known_star_df["Wavelength"].values
    y_grid = known_star_df["Flux"].values
    y_new = np.interp(x_old, x_grid, y_grid)

    # Normalization and Variance Calculation
    wopt = np.where((x_old > 3500) & (x_old < 7500))
    y_old = mystery_star_df["Flux"].values
    x_list = x_old[wopt]
    y_list = y_old[wopt]
    slope, intercept = np.polyfit(x_list, y_list, 1)
    ynorm = y_list / (slope * x_list + intercept)
    variance = np.std(ynorm)

    # Chi-Squared Calculation
    obs = y_old / np.max(y_old)  # Observed normalized flux
    exp = y_new                # Expected flux
    vals = []
    for i in range(len(exp)):
        val = ((obs[i] - exp[i])**2 / variance)
        vals.append(val)
    chi2 = sum(vals)
    red_chi2 = chi2 / (len(y_old) - 1)

    interpolated_data = pd.DataFrame({"Wavelength": x_old, "Flux": y_new})

    return interpolated_data, chi2, red_chi2


def remove_nans(mat):
    x, y = mat[0], mat[1]
    x = x[~np.isnan(x)]
    y = x[~np.isnan(y)]
    return np.matrix(x, y)


def read_data(
    *filenames,
    filetype=".tsv",
    columns=None,
    labels=None,
    as_type=None,
    skip_rows=2,
    sort=True,
    sample=None,
    read_kwargs=...,
    **kwargs,
):
    read_data = {}
    for i, file in enumerate(filenames):
        if file.endswith(filetype):
            DATA = pd.read_csv(file, **read_kwargs, **kwargs)

            if skip_rows:
                DATA = DATA.iloc[skip_rows:, :]
                DATA = DATA.reset_index()

            if columns:
                DATA = DATA[columns]

            if sort and columns and len(columns) > 0:
                DATA.sort_values(columns[0], inplace=True)

            if as_type:
                DATA = DATA.astype(as_type)

            if sample:
                DATA = DATA.sample(sample)

            if labels:
                DATA["Sort"] = labels[i]

            read_data[f"file{i + 1}"] = DATA
        else:
            print(f"Skipping file {file} as it is not a {filetype} file.")

    return read_data


def fix_data(*dataframes, sample=None, sort=False, astype=np.float64, dropna=False):
    returns = []
    for data in dataframes:
        data = data.astype(astype)

        if dropna:
            data = data.dropna()

        if sample:
            data = data.sample(sample)

        if sort:
            data = data.sort_values(data.columns[0])

        data = (data.iloc[:, 1], data.iloc[:, 0])
        returns.append(data)
    return tuple(returns)


def reset_index(data):
    data = data.reset_index(drop=True)
    return data


def smooth_signal(dataframe, col_to_smooth, window_size=5, polyorder=2):
    """
    Smooths out signal data using Savitzky-Golay filter.

    Args:
        dataframe: A Pandas DataFrame with columns "Wavelength" and "Flux".
        window_size: The length of the filter window (i.e., the number of coefficients). Must be a positive odd integer.
        polyorder: The order of the polynomial used to fit the samples. Must be less than window_size.

    Returns:
        A Pandas DataFrame with smoothed "Flux" values.
    """


    smoothed_flux = savgol_filter(dataframe[col_to_smooth], window_size, polyorder)
    smoothed_data = dataframe.copy()
    smoothed_data[col_to_smooth] = smoothed_flux

    return smoothed_data
