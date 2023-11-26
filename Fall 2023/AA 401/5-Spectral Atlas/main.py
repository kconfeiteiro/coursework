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
}

RDATA = read_spectra(
    *CONFIG["files"],
    normalize_col="Flux",
    **CONFIG["read kwargs"],
)

fig, axes = plt.subplots(figsize=(7, 12))
for i, data in enumerate(RDATA, 1):
    data["Flux"] = data["Flux"].apply(lambda x: x + i)
    axes.plot(*split(data), label=f"Spectra {i}")
    i += 1

axes.set_xlim(*CONFIG["xrange"])
axes.set_title(CONFIG["title"])
axes.set_ylabel(r"Flux, $F$ ($W$) (w/ linear shift)")
axes.set_xlabel(r"Wavelength, $\lambda$ ($\AA$)")
axes.legend(loc="upper right", bbox_to_anchor=(1.3, 1.00))
fig.tight_layout()
fig.savefig(CONFIG["save as"])
plt.show()
