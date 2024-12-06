import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_starfile(*filepaths, col_names=None, read_kwargs=dict(skiprows=3)):
    file = filepaths[0]
    data = np.loadtxt(file, **read_kwargs)
    return pd.DataFrame(data, columns=col_names)


def min_max_scaling(col):
    return (col - col.min()) / (col.max() - col.min())


def read_spectra(*paths, normalize_col=None, **kwargs):
    data = []
    for i, path in enumerate(paths):
        print(f"Reading path ({i + 1}): {path}")
        dataframe = pd.read_csv(path, **kwargs)

        if normalize_col is not None:
            dataframe[normalize_col] = min_max_scaling(dataframe[normalize_col])
        data.append(dataframe)

    print(f"Read data files: {len(paths)}")
    return data[0] if len(paths) == 1 else data


def list_directory(path):
    return [os.path.join(path, x) for x in os.listdir(path)]


def plot_single_spectra(
    data,
    title,
    xtitle="Wavelength",
    ytitle="Flux",
    plt_kwargs=dict(tight_layout=True),
    save_as=None,
):
    fig, axes = plt.subplots(**plt_kwargs)
    axes.plot(data["Wavelength"], data["Flux"])
    axes.set_xlabel(xtitle)
    axes.set_ylabel(ytitle)
    axes.set_title(title)

    if save_as:
        print(f"Saved figure as: `{save_as}`")
        fig.savefig(save_as)


def normalize_spectra(dataframes_dict):
    processed_data = {}
    for key, spectrum_data in dataframes_dict.items():
        max_flux = spectrum_data["Flux"].max()
        normalized_flux = spectrum_data["Flux"] / max_flux
        sorted_spectrum = pd.DataFrame(
            {"Wavelength": spectrum_data["Wavelength"], "Flux": normalized_flux}
        ).sort_values(by="Wavelength")
        processed_data[key] = sorted_spectrum
    return processed_data


def process_spectra(file_paths): # TODO - rewrite this function. 
    all_spectra = []
    read_spectra_data = read_spectra(*file_paths, comment="#")
    for spectra_data in read_spectra_data:
        spectra_data = spectra_data[[spectra_data.columns[-1]]]
        spectra_data.columns = [f"col_{i}" for i in range(len(spectra_data.columns))]
        split_cols = spectra_data["col_0"].str.split(expand=True)
        split_cols.columns = [f"col_{i}" for i in range(len(split_cols.columns))]
        all_spectra.append(split_cols)
    return all_spectra
