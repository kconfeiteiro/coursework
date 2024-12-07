# %%
import utils.tools as tl
import matplotlib.pyplot as plt

# %%
test_files = "data/spectral_atlas_data/spectra3.dat"
read_kwargs = dict(
    delim_whitespace=True,
    comment="#",
    usecols=(0, 1),
    names=["Wavelength", "Flux"]
)
data = tl.read_spectra(test_files, **read_kwargs)["spectra1"]
data = tl.normalize_spectra(data)

# %% read spectra data
star1 = tl.read_starfile("data/star1.dat", col_names="Wavelength Flux".split())
star1 = tl.normalize_spectra(star1)

# %%
fig, axes = plt.subplots()
axes.plot(data["Wavelength"], data["Flux"], label=test_files.split("/")[-1])
axes.plot(star1["Wavelength"], star1["Flux"], label="Mystery Star 1")
axes.set_xlim((3500, 7000))
axes.legend()
plt.show()
