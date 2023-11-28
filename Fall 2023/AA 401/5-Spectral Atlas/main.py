import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


from helpers import list_dir, read_spectra, split, uniquefilename

CONFIG = {
    "files": list_dir("DATA", reversed=True),
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
    "spectral classes": [
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

RDATA = read_spectra(
    *CONFIG["files"],
    normalize_col="Flux",
    **CONFIG["read kwargs"],
)

fig, axes = plt.subplots(**CONFIG["figure config"])
for i, (data, smag) in enumerate(zip(RDATA, CONFIG["spectral classes"][::-1]), 1):
    data["Flux"] = data["Flux"].apply(lambda x: x + i)
    axes.plot(*split(data), label=smag)
    i += 1

rectangle = Rectangle((3750, 0), 1250, 10, fc="lightblue", alpha=0.33)
axes.set_xlim(*CONFIG["xrange"])
axes.set_title(CONFIG["title"])
axes.set_ylabel(r"Flux, $F$ ($W$) (w/ linear shift)")
axes.set_xlabel(r"Wavelength, $\lambda$ ($\AA$)")
axes.add_patch(rectangle)

for key in CONFIG["plot annotations"].keys():
    axes.annotate(
        **CONFIG["plot annotations"][key],
        arrowprops={
            "facecolor": "black",
            "width": 0.75,
            "headwidth": 6,
        },
    )

for sclass in CONFIG["spectral classes"]:
    axes.text(*sclass)


fig.tight_layout()
fig.savefig(CONFIG["save as"])
plt.show()
