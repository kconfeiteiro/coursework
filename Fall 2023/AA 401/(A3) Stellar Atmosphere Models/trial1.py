import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from google.colab import drive

drive.mount("/content/drive", force_remount=True)

FILE1 = "/content/drive/MyDrive/006_Courses/PS_401/Portfolio/(A03) Stellar Atmosphere Models/DATA/kurucz6000logg0.txt"
FILE2 = "/content/drive/MyDrive/006_Courses/PS_401/Portfolio/(A03) Stellar Atmosphere Models/DATA/black_body_spectra.txt"
FILE3 = "/content/drive/MyDrive/006_Courses/PS_401/Portfolio/(A03) Stellar Atmosphere Models/DATA/kurucz6000logg0.txt"


def prepare_data(
    filename,
    drange=(3.8e3, 7e3),
    colnames=None,
    astype=np.float64,
    dropna=True,
    **kwargs
):
    DATA = pd.read_csv(filename, **kwargs)

    if dropna:
        DATA = DATA.dropna()

    if astype:
        DATA = DATA.astype(np.float64)

    if drange:
        DATA = DATA.loc[
            (DATA[DATA.columns[0]] > d_range[0]) & (DATA[DATA.columns[0]] < d_range[1])
        ]

    return DATA


COLNAMES = ["Wavelength", "Flux"]
_kwargs = dict(delim_whitespace=True, comment="#", names=COLNAMES, on_bad_lines="skip")
d_range = (3.8e3, 7e3)

MODEL_1 = prepare_data(FILE1, **_kwargs)
MODEL_2 = prepare_data(FILE2, **_kwargs)
MODEL_3 = prepare_data(FILE3, **_kwargs)

fig, axe = plt.subplots()
axe.plot(MODEL_1, label="Model 1")
axe.plot(MODEL_2, label="Model 2")
axe.plot(MODEL_3, label="Model 3")
axe.set_xlabel(r"Flux, $F$")
axe.set_ylabel(r"Wavelength, $\lambda$")
axe.set_title(r"Spectra between $3800\AA < \lambda < 7000\AA$ ")
axe.legend()
plt.show()
