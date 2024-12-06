import warnings
import matplotlib.pyplot as plt
import utils.tools as tl

warnings.filterwarnings("ignore")


# %% test 2
spectral_atlas_spectra = tl.process_spectra(r"finalproject\data\spectral_atlas_data")
spectral_atlas_spectra[0]

# %% read and noramlize data
data = tl.normalize_spectra(tl.read_starfile(r"data/star1.dat", "data\\mystery_stars\\star15.dat"))
plt_kwargs = dict(figsize=(14, 7), tight_layout=True)

# %% Plot Spectra for Mystery Star
tl.plot_single_spectra(data["star1"], title="Star 1 Spectra (Mystery Star)")
plt.show()
