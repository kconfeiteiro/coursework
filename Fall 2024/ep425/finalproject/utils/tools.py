from astropy.io import fits
from matplotlib import pyplot as plt
import pandas as pd
import astropy as ap
import numpy as np
import os
import glob

def read_fits_directory(directory_path, file_pattern="*.fits"):
    """
    Reads all FITS files in a directory matching a given pattern and extracts the flux data from them.

    Parameters:
    directory_path (str): The path to the directory containing FITS files.
    file_pattern (str): The pattern to match FITS files. Default is "*.fits".

    Returns:
    flux_data_list (list): A list of flux data arrays extracted from each FITS file.
    """
    flux_data_list = []
    search_pattern = os.path.join(directory_path, file_pattern)
    for file_path in glob.glob(search_pattern):
        with fits.open(file_path) as hdul:
            flux_data = hdul[1].data['FLUX']  # Assuming flux data is in the second HDU and column named 'FLUX'
            flux_data_list.append(flux_data)
    return flux_data_list

def read_table(*paths, return_df=True, columns=None):
    """
    Reads a .tbl file and extracts the data from it.

    Parameters:
    file_path (str): The path to the .tbl file.

    Returns:
    data (numpy.ndarray): The data extracted from the .tbl file.
    """
    read_data = []
    for file in paths:
        data = np.genfromtxt(file, delimiter='\t', names=True)
        if return_df:
            data = pd.DataFrame(data)
            if columns:
                data = data[columns]

        read_data.append(data)
    return read_data[0] if len(paths) == 1 else tuple(read_data)


def read_fits_file(file_path):
    """
    Reads a FITS file and extracts data, flux, and time from it.

    Parameters:
    file_path (str): The path to the FITS file.

    Returns:
    data (numpy.ndarray): The data extracted from the FITS file.
    header (astropy.io.fits.header.Header): The header of the FITS file.
    flux (numpy.ndarray): The flux data extracted from the FITS file.
    time (numpy.ndarray): The time data extracted from the FITS file.
    """
    with fits.open(file_path) as hdul:
        data = hdul[0].data
        header = hdul[0].header
        return data, header, hdul


def calc_instrumental_magnitude(data, calc_col="SourceSky"):
    data[f"{calc_col}2"] = -2.5 * np.log10(data[calc_col])
    return data


def plot_fits_image(file, title=None, save_as=None):
    fig, axes = plt.subplots(tight_layout=True)
    data, _, _ = read_fits_file(file)
    axes.imshow(data)
    if not title:
        title = file.split("/")[-1]

    fig.suptitle(title)
    if save_as:
        fig.savefig(save_as)
