import warnings
import matplotlib.pyplot as plt
import utils.tools as tl

warnings.filterwarnings("ignore")


# %% test 2
read_kwargs = dict(
    delim_whitespace=True,
    comment="#",
    usecols=(0, 1),
    names=["Wavelength", "Flux"]
)
spectral_atlas_file_list = tl.list_directory("data\\spectral_atlas_data")
print("spectral_atlas_file_list:\n", spectral_atlas_file_list)
spectral_atlas_spectra = tl.read_spectra(*spectral_atlas_file_list, normalize_col="Flux", **read_kwargs)
spectral_atlas_spectra["star1"]

# %% plot spectral atlas
figure_kwargs = dict(figsize=(7, 8))
fig2, axes2 = plt.subplots(**figure_kwargs)
for i, data in enumerate(spectral_atlas_spectra.values(), 1):
    data["Flux"] = data["Flux"].apply(lambda x: x + i)
    axes2.plot(*tl.split(data))
    i += 1

axes2.set_xlim((3500, 7000))
# axes2.set_ylim((0, 60))
axes2.set_title("Spectral Atlas")
axes2.set_ylabel(r"Flux, $F$ ($W$)")
axes2.set_xlabel(r"Wavelength, $\lambda$ ($\AA$)")

# text box for each spectral class
axes2.text(6700, 8.75, "07.5V")
axes2.text(6700, 7.75, "B5 V")
axes2.text(6700, 6.50, "A2.5 V")
axes2.text(6700, 5.85, "F1 V")
axes2.text(6700, 4.85, "G1 V")
axes2.text(6700, 3.10, "K0 V")
axes2.text(6700, 2.25, "K8 V")
axes2.text(6700, 1.15, "M3 V")

plt.show()

# %% plotting my spectra on the spectral atlas
mystery_star_spectra = tl.read_starfile(r"data/star1.dat", normalize_col="Flux")
data = tl.normalize_spectra(mystery_star_spectra)
data
# tl.plot_single_spectra(data["star1"], ax=axes2)

# %% read and noramlize data
plt_kwargs = dict(figsize=(14, 7), tight_layout=True)

# %% Plot Spectra for Mystery Star
tl.plot_single_spectra(data["star1"], title="Star 1 Spectra (Mystery Star)")
plt.show()
