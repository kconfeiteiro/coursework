import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle


# define function for min-max
def minmax_scaling(col):
    return (col - col.min()) / (col.max() - col.min())


def list_dir(rel_path):
    ABS = os.path.abspath(rel_path)
    prepend = lambda path: os.path.join(ABS, path)
    listed_paths = os.listdir(rel_path)
    read_files = list(map(prepend, listed_paths))
    return read_files


# read data
data_paths = list_dir("../DATA")
read_data = [0] * len(data_paths)
for i, path in enumerate(data_paths[::-1]):
    # read data into Pandas DataFrame
    data = pd.read_csv(
        path,
        delim_whitespace=True,
        comment="#",
        usecols=(0, 1),
        names=["Wavelength", "Flux"],
    )

    # normalize the flux with min-max scaling
    data["Flux"] = minmax_scaling(data["Flux"])

    # append data list
    read_data[i] = data

fig, axes = plt.subplots(figsize=(7, 8))
for i, data in enumerate(read_data, 1):
    # shift the next spectra upwards
    data["Flux"] = data["Flux"].apply(lambda x: x + i)
    axes.plot(data.Wavelength, data.Flux)
    i += 1

rectangle = Rectangle((3750, 0), 1250, 10, fc="lightblue", alpha=0.33)
axes.set_xlim((3500, 7000))
axes.set_ylabel(r"Flux")
axes.set_xlabel(r"Wavelength")
axes.set_title("A Sequence of Stellar Flux Profiles")
axes.add_patch(rectangle)

# set each text box for each spectral class
axes.text(6700, 8.75, "07.5V")
axes.text(6700, 7.75, "B5 V")
axes.text(6700, 6.50, "A2.5 V")
axes.text(6700, 5.85, "F1 V")
axes.text(6700, 4.85, "G1 V")
axes.text(6700, 3.10, "K0 V")
axes.text(6700, 2.25, "K8 V")
axes.text(6700, 1.15, "M3 V")

# H-alpha
axes.annotate(
    text=r"$H_\alpha$",
    xy=(6550, 8.35),
    xytext=(6350, 7.75),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# H-beta
axes.annotate(
    text=r"$H_\beta$",
    xy=(4900, 6.35),
    xytext=(5100, 6.25),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# He I
axes.annotate(
    text="He I",
    xy=(4471, 4.5),
    xytext=(4201, 4.85),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# He II
axes.annotate(
    text="He II",
    xy=(4542, 4.25),
    xytext=(4642, 3.75),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# Na D
axes.annotate(
    text="Na D",
    xy=(5875, 4.35),
    xytext=(5500, 3.75),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# Ca I
axes.annotate(
    text="Ca I",
    xy=(4227, 5.90),
    xytext=(4350, 6.20),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# TiO
axes.annotate(
    text="Ti O",
    xy=(5448, 5.75),
    xytext=(5548, 5.15),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# H-delta
axes.annotate(
    text=r"$H_\delta$",
    xy=(4125, 8.65),
    xytext=(4300, 8.0),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# H-gamma
axes.annotate(
    text=r"$H_\gamma$",
    xy=(4350, 8.65),
    xytext=(4550, 8.35),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# Ca K
axes.annotate(
    text="Ca K",
    xy=(4000, 2.65),
    xytext=(4200, 2.35),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

# Balmer Jump
axes.annotate(
    text="Balmer Jump",
    xy=(3750, 7.30),
    xytext=(4200, 7.1),
    arrowprops={
        "facecolor": "black",
        "width": 0.75,
        "headwidth": 6,
    },
)

fig.tight_layout()
# fig.savefig("<what you wannt to save your plot as>")
