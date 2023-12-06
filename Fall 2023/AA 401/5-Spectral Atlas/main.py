import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from helpers import list_dir, read_spectra, split, uniquefilename

# project configurations
CONFIG = {
    "files": list_dir("DATA"),
    "figure config": {
        "figsize": (7, 8),
    },
    "xrange": (3500, 7000),
    "read kwargs": {
        "delim_whitespace": True,
        "comment": "#",
        "usecols": (0, 1),
        "names": ["Wavelength", "Flux"],
    },
    "title": "A Sequence of Stellar Flux Profiles",
    "save as": uniquefilename("spectral_atlas.jpg", "PLOTS")[0],
    "spectral atlas key": {
        "File 1": "F2V",
        "File 2": "G8V",
        "File 3": "G2V",
        "File 4": "M0V",
        "File 5": "B3V",
        "File 6": "O9V",
        "File 7": "K5V",
        "File 8": "F8V",
        "File 9": "M6V",
        "File 10": "B9V",
        "File 11": "A0V",
        "File 12": "O5V",
        "File 13": "A5V",
        "File 14": "WN",
        "File 15": "L5",
    },
    "spectral classes annotations": [
        (6700, 8.75, "07.5V"),
        (6700, 7.75, "B5 V"),
        (6700, 6.50, "A2.5 V"),
        (6700, 5.85, "F1 V"),
        (6700, 4.85, "G1 V"),
        (6700, 3.10, "K0 V"),
        (6700, 2.25, "K8 V"),
        (6700, 1.15, "M3 V"),
    ],
    "plot annotations": {
        "H-alpha": {
            "text": r"$H_\alpha$",
            "xy": (6550, 8.35),
            "xytext": (6350, 7.75),
        },
        "H-beta": {
            "text": r"$H_\beta$",
            "xy": (4900, 6.35),
            "xytext": (5100, 6.25),
        },
        "He I": {
            "text": "He I",
            "xy": (4471, 4.5),
            "xytext": (4201, 4.85),
        },
        "He II": {
            "text": "He II",
            "xy": (4542, 4.25),
            "xytext": (4642, 3.75),
        },
        "Na D": {
            "text": "Na D",
            "xy": (5875, 4.35),
            "xytext": (5500, 3.75),
        },
        "Ca I": {
            "text": "Ca I",
            "xy": (4227, 5.90),
            "xytext": (4350, 6.20),
        },
        "TiO": {
            "text": "Ti O",
            "xy": (5448, 5.75),
            "xytext": (5548, 5.15),
        },
        "H-delta": {
            "text": r"$H_\delta$",
            "xy": (4125, 8.65),
            "xytext": (4300, 8.0),
        },
        "H-gamma": {
            "text": r"$H_\gamma$",
            "xy": (4350, 8.65),
            "xytext": (4550, 8.35),
        },
        "Ca K": {
            "text": "Ca K",
            "xy": (4000, 2.65),
            "xytext": (4200, 2.35),
        },
        "Balmer Jump": {
            "text": "Balmer Jump",
            "xy": (3750, 7.30),
            "xytext": (4200, 7.1),
        },
    },
}

# read spectral data
spectral_data = read_spectra(
    *CONFIG["files"],
    normalize_col="Flux",
    **CONFIG["read kwargs"],
)

for data in spectral_data:
    print("max: ", data.describe().iloc[-1, -1])

# create spectrum plot
fig, axes = plt.subplots(**CONFIG["figure config"])
for i, (data, spectype) in enumerate(
    zip(spectral_data, CONFIG["spectral atlas key"].values())
):
    axes.plot(*split(data), label=spectype)
    data["Flux"] = data["Flux"].apply(lambda x: x + i)

# add blue shade to plot
axes.set_xlim(*CONFIG["xrange"])
axes.set_title(CONFIG["title"])
axes.set_ylabel(r"Flux, $F$ ($W$) (w/ linear shift)")
axes.set_xlabel(r"Wavelength, $\lambda$ ($\AA$)")
axes.add_patch(Rectangle((3750, 0), 1250, 10, fc="lightblue", alpha=0.33))

# add annotations to plot
# for key in CONFIG["plot annotations"].keys():
#     axes.annotate(
#         **CONFIG["plot annotations"][key],
#         arrowprops={
#             "facecolor": "black",
#             "width": 0.75,
#             "headwidth": 6,
#         },
#     )

# add spectral class name annotations
# for spectral_class in CONFIG["spectral classes annotations"]:
#     axes.text(*spectral_class)

# save figure
fig.tight_layout()
axes.legend()
# fig.savefig(CONFIG["save as"])
plt.show()
