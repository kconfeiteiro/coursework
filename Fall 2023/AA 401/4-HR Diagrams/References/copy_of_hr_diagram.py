import numpy as np
import matplotlib.pyplot as plt


# the files above are all isochrones
fileIsochrone1 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Iso10.1]asu.tsv"
)
fileIsochrone2 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Iso6.5]asu.tsv"
)
fileIsochrone3 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Iso7.5]asu.tsv"
)
fileIsochrone4 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Iso8.5]asu.tsv"
)
fileIsochrone5 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Iso9.5]asu.tsv"
)
fileTrack1 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.25].tsv"
)
fileTrack2 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track85]asu.tsv"
)
fileTrack3 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track0.8]asu.tsv"
)
fileTrack4 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track0.9]asu.tsv"
)
fileTrack5 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1]asu.tsv"
)
fileTrack6 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.1]asu.tsv"
)
fileTrack7 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.35]asu.tsv"
)
fileTrack8 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.5]asu.tsv"
)
fileTrack9 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track3]asu.tsv"
)
fileTrack10 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track4]asu.tsv"
)
fileTrack11 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track7]asu.tsv"
)
fileTrack12 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track20]asu.tsv"
)
fileTrack13 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track25]asu.tsv"
)
fileTrack14 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track32]asu.tsv"
)
fileTrack15 = (
    "/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track120]asu.tsv"
)

Isochrone1 = np.loadtxt(fileIsochrone1, skiprows=49)
Isochrone2 = np.loadtxt(fileIsochrone2, skiprows=49)
Isochrone3 = np.loadtxt(fileIsochrone3, skiprows=49)
Isochrone4 = np.loadtxt(fileIsochrone4, skiprows=49)
Isochrone5 = np.loadtxt(fileIsochrone5, skiprows=49)
Track1 = np.loadtxt(fileTrack1, skiprows=49)
Track2 = np.loadtxt(fileTrack2, skiprows=49)
Track3 = np.loadtxt(fileTrack3, skiprows=49)
Track4 = np.loadtxt(fileTrack4, skiprows=49)
Track5 = np.loadtxt(fileTrack5, skiprows=49)
Track6 = np.loadtxt(fileTrack6, skiprows=49)
Track7 = np.loadtxt(fileTrack7, skiprows=49)
Track8 = np.loadtxt(fileTrack8, skiprows=49)
Track9 = np.loadtxt(fileTrack9, skiprows=49)
Track10 = np.loadtxt(fileTrack10, skiprows=49)
Track11 = np.loadtxt(fileTrack11, skiprows=49)
Track12 = np.loadtxt(fileTrack12, skiprows=49)
Track13 = np.loadtxt(fileTrack13, skiprows=49)
Track14 = np.loadtxt(fileTrack14, skiprows=49)
Track15 = np.loadtxt(fileTrack15, skiprows=49)


x = (
    Track3[1, 1],
    Track4[1, 1],
    Track5[1, 1],
    Track6[1, 1],
    Track1[1, 1],
    Track7[1, 1],
    Track8[1, 1],
    Track9[1, 1],
    Track10[1, 1],
    Track11[1, 1],
    Track12[1, 1],
    Track13[1, 1],
    Track14[1, 1],
    Track2[1, 1],
    Track15[1, 1],
)

y = (
    Track3[1, 0],
    Track4[1, 0],
    Track5[1, 0],
    Track6[1, 0],
    Track1[1, 0],
    Track7[1, 0],
    Track8[1, 0],
    Track9[1, 0],
    Track10[1, 0],
    Track11[1, 0],
    Track12[1, 0],
    Track13[1, 0],
    Track14[1, 0],
    Track2[1, 0],
    Track15[1, 0],
)

lum_sun, teff_sun = 0, 3.761

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(Isochrone1[:, 1], Isochrone1[:, 0], "c", label="Isochrone (6.5 yrs)")
axes.plot(Isochrone2[:, 1], Isochrone2[:, 0], "blueviolet", label="Isochrone (7.5 yrs)")
axes.plot(Isochrone3[:, 1], Isochrone3[:, 0], "pink", label="Isochrone (8.5 yrs)")
axes.plot(Isochrone4[:, 1], Isochrone4[:, 0], "g", label="Isochrone (9.5 yrs)")
axes.plot(Isochrone5[:, 1], Isochrone5[:, 0], "m", label="Isochrone (10.1 yrs)")
axes.plot(Track1[:, 1], Track1[:, 0], "b", label="Track 1.25M_Sun")
axes.plot(Track2[:, 1], Track2[:, 0], "g", label="Track 85M_Sun")
axes.plot(teff_sun, lum_sun, "y", marker=(5, 1), markersize=13, label="Sun")
plt.xlim(5, 3.5)


axes.plot(x, y, "r", label="ZAMS")
plt.title("HR Diagram")
plt.xlabel("Temperature [K]")
plt.ylabel("Luminosity [J/s]")
plt.legend()
