import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import utils.tools as tl
import glob

# read data table
files = [
    "data/Observed data/20241116/HD 237190/HD237190_r30s_20241116_DataTable.tbl",
    "data/Observed data/20241107/HD 213306/HD213306_r30s_20241107_table.tbl",
    "data/Observed data/20241116/HD 213306/red-filter/HD213306_20241116_r30s_Table.tbl"
]

for file in files:
    print(f"Processing file: `{file}`")
    data = tl.read_table(file)
    data = tl.calc_instrumental_magnitude(data, calc_col="SourceSky_T1")
    data = data.dropna(axis=1)

    target, obs_date = file.split("/")[3], file.split("/")[2]
    time, flux, mags = "BJD_TDB", "rel_flux_T1", "SourceSky_T12"

    # read data table
    fig2, axes2 = plt.subplots(3, 1, figsize=(10, 8), tight_layout=True)

    axes2[1].plot(data["AIRMASS"], data[mags])
    axes2[0].plot(data[time], data[mags])
    axes2[2].plot(data[time], data["rel_flux_T1"])

    axes2[0].set_ylabel("Instrumental Magnitudes")
    axes2[0].set_xlabel(f"Time ({time})")

    axes2[1].set_ylabel("Instrumental Magnitudes")
    axes2[1].set_xlabel("Airmass")

    axes2[2].set_ylabel("Relative Flux")
    axes2[2].set_xlabel(f"Time ({time})")

    axes2[0].set_title("Light Curve")
    axes2[1].set_title("Airmass vs. Instrumental Magnitude")
    axes2[2].set_title(f"{target} Light Curve")

    fig2.suptitle(f"{target} (cepheid) Light Curve & Airmass [red filter] - {tl.format_date(obs_date)}")
    fig2.savefig(f"figures/for_paper/{target}_{obs_date}_lightcurve_magnitudeplot_airmassplot.jpg")

    # calculate periodogram
    periods, power, frequency = tl.generate_periodogram(data)

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), tight_layout=True)
    axes[0].plot(periods, power)
    axes[1].plot(frequency, power)

    axes[0].set_xlabel("Periods")
    axes[0].set_ylabel("Power")
    axes[0].set_title("Period vs. Power")

    axes[1].set_xlabel("Frequency")
    axes[1].set_ylabel("Power")
    axes[1].set_title("Frequency vs Power")

    fig.suptitle(f"Periodogram and Frequency Analysis of {target} ({tl.format_date(obs_date)})")
    fig.savefig(f"figures/for_paper/{target}_{obs_date}_periodogram_frequency_analysis.jpg")
