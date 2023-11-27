import os

import matplotlib.pyplot as plt
import pandas as pd

from helpers import list_dir, read_spectra, split, uniquefilename

CONFIG = {
    "files": list_dir("DATA"),
    "spectral types": [
        "O5V",
        "O9V",
        "B3V",
        "B9V",
        "A0V",
        "A5V",
        "F2V",
        "F8V",
        "G2V",
        "G8V",
        "K5V",
        "M0V",
        "M6V",
    ],
    "xrange": (3500, 7000),
    "read kwargs": {
        "delim_whitespace": True,
        "comment": "#",
        "usecols": (0, 1),
        "names": ["Wavelength", "Flux"],
    },
    "title": "A Sequence of Stellar Flux Profiles",
    "save as": uniquefilename("spectral_atlas.jpg", "PLOTS")[0],
    "spectra to keep": "7.5V B5V A2.5V F1V G1V K0V K8V M3V".split(),
}

RDATA = read_spectra(
    *CONFIG["files"],
    normalize_col="Flux",
    **CONFIG["read kwargs"],
)

fig, axes = plt.subplots(figsize=(7, 12))
for i, (data, smag) in enumerate(zip(RDATA, CONFIG["spectra to keep"]), 1):
    data["Flux"] = data["Flux"].apply(lambda x: x + i)
    axes.plot(*split(data), label=smag)
    i += 1

axes.set_xlim(*CONFIG["xrange"])
axes.set_title(CONFIG["title"])
axes.set_ylabel(r"Flux, $F$ ($W$) (w/ linear shift)")
axes.set_xlabel(r"Wavelength, $\lambda$ ($\AA$)")
axes.legend(loc="upper right", bbox_to_anchor=(1.3, 1.00))
axes.axvline(6563)
axes.text(6563, 8.25, r"$H_\alpha$")
axes.axvline(4861)
axes.text(4861, 6.25, r"$H_\beta$")
axes.axvline(4250)  # TODO - check if correct
axes.text(5750, 1, "Paschen Continuum")  # TODO - check if correct
axes.axvline(4226.7)  # TODO - check if correct
axes.text(4226.7, 3, "Ca I")  # TODO - check if correct
axes.axvline(3570)  # TODO - check if correct
axes.text(3570, 2.25, "Balmer Jump")
fig.tight_layout()
fig.savefig(CONFIG["save as"])
plt.show()
