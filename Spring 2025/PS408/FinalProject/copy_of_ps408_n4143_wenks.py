# -*- coding: utf-8 -*-
"""Copy of ps408_n4143_wenks.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lJ6jhZ3NE8tH45WOU0-T1FHFHpgIj6CH
"""

from astropy.io import fits
from astropy.utils.data import download_file
import numpy as np
import matplotlib.pyplot as plt


url = 'https://www.legacysurvey.org/viewer/cutout.fits?ra=182.4009&dec=42.5331&layer=ls-dr9-north'
ngc4143fits = download_file(url)
hdu = fits.open(ngc4143fits)
data = hdu[0].data
hdu.close()

"""NGC 4143 is a lenticular galaxy located in the Canes Venatici constellation. Given its visual magnitude of 12.08, it is not visible to the naked eye.


Source: https://theskylive.com/sky/deepsky/ngc4143-object

"""

from photutils.isophote import Ellipse, EllipseGeometry
from photutils.centroids import centroid_com
import numpy as np

data_2d = data[1]  # r-band
masked_data = np.nan_to_num(data_2d, nan=0.0)
masked_g = np.nan_to_num(data[0], nan=0.0)
masked_z = np.nan_to_num(data[2], nan=0.0)

y0, x0 = centroid_com(masked_data)
y0g, x0g = centroid_com(masked_g)
y0z, x0z = centroid_com(masked_z)
print(f"Estimated center: x0 = {x0:.2f}, y0 = {y0:.2f}")
print(f"Estimated center: x0 = {x0g:.2f}, y0 = {y0g:.2f}")
print(f"Estimated center: x0 = {x0z:.2f}, y0 = {y0z:.2f}")

from photutils.isophote import EllipseGeometry, Ellipse

geometry = EllipseGeometry(x0=x0, y0=y0, sma=30, eps=0.3, pa=0.0) # estimate sma = 30 (?)
ellipse = Ellipse(data_2d, geometry)
isolist = ellipse.fit_image()

#Display the results as an Astropy Table
isolist = ellipse.fit_image(sclip=2., nclip=3)
isolist.to_table()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['image.origin'] = 'lower'
# %matplotlib inline

plt.figure(figsize=(8, 4))

plt.scatter(isolist.sma**0.25, -2.5*np.log10(isolist.intens))
plt.title("N4143 profile with sigma-clip")
plt.xlabel('sma**1/4')
plt.ylabel('Magnitude')
plt.gca().invert_yaxis()

plt.figure(figsize=(10, 5))
plt.figure(1)

plt.subplot(221)
plt.errorbar(isolist.sma, isolist.eps, yerr=isolist.ellip_err, fmt='o', markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('Ellipticity')

plt.subplot(222)
plt.errorbar(isolist.sma, isolist.pa/np.pi*180., yerr=isolist.pa_err/np.pi* 80., fmt='o', markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('PA (deg)')

plt.subplot(223)
plt.errorbar(isolist.sma, isolist.x0, yerr=isolist.x0_err, fmt='o', markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('X0')

plt.subplot(224)
plt.errorbar(isolist.sma, isolist.y0, yerr=isolist.y0_err, fmt='o', markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('Y0')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(data[1], vmin=0, vmax=1000, cmap='jet')  # r-band
plt.axis([0, 255, 0, 255])

isos = []
smas = [20., 50., 90.]
for sma in smas:
    iso = isolist.get_closest(sma)
    isos.append(iso)
    x, y = iso.sampled_coordinates()
    ax.plot(x, y, color='white')

plt.figure(figsize=(10, 3))

for iso in isos:
    angles = ((iso.sample.values[0] + iso.sample.geometry.pa) / np.pi*180.) % 360.
    plt.scatter(angles, iso.sample.values[2])

plt.xlabel("Angle (deg)")
plt.ylabel("Intensity")

plt.figure(figsize=(10, 5))
plt.figure(1)
limits = [0., 100., -0.1, 0.1]

plt.subplot(221)
plt.axis(limits)
plt.errorbar(isolist.sma, isolist.a3, yerr=isolist.a3_err, fmt='o', markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('A3')

plt.subplot(222)
plt.axis(limits)
plt.errorbar(isolist.sma, isolist.b3, yerr=isolist.b3_err, fmt='o', markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('B3')

plt.subplot(223)
plt.axis(limits)
plt.errorbar(isolist.sma, isolist.a4, yerr=isolist.a4_err, fmt='o', markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('A4')

plt.subplot(224)
plt.axis(limits)
plt.errorbar(isolist.sma, isolist.b4, fmt='o', yerr=isolist.b4_err, markersize=4)
plt.xlabel('Semimajor axis length')
plt.ylabel('B4')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from photutils.isophote import build_ellipse_model
import matplotlib.pyplot as plt
# %matplotlib inline

model_image = build_ellipse_model(data[1].shape, isolist, fill=np.mean(data[1][0:10, 0:10]))

vmin = np.percentile(data[1], 1)
vmax = np.percentile(data[1], 99)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

ax1.imshow(model_image, vmin=vmin, vmax=vmax, cmap='viridis')
ax1.set_title("Model")

ax2.imshow(data[1], vmin=vmin, vmax=vmax, cmap='viridis')
ax2.set_title("Data")

print("Model (r-band):", np.min(model_image[1]), np.max(model_image[1]))
print("Any NaNs?:", np.isnan(model_image[1]).any())
print("Shape:", model_image[1].shape)

residual = data[1] - model_image

print("Residual min:", np.min(residual))
print("Residual max:", np.max(residual))
print("Residual std:", np.std(residual))

print("Data[1] min/max:", np.min(data[1]), np.max(data[1]))
print("Model min/max:", np.min(model_image), np.max(model_image))

plt.figure(figsize=(6,6))
plt.imshow(residual, cmap='viridis', vmin=-2, vmax=2)  # larger stretch to see small differences
plt.title("Residual - Enhanced Stretch")
plt.colorbar()

from astropy.stats import sigma_clip

# Apply a less aggressive sigma-clipping with sigma=2
residual2 = sigma_clip(residual, sigma=2, maxiters=5)

# Check the number of NaNs again
print("Number of NaNs after adjusted clipping:", np.isnan(residual2).sum())

# limits = [512-120, 512+150]

plt.figure(figsize=(6,6))
plt.imshow(residual, cmap='viridis')  # Let matplotlib auto-scale
plt.title("Residual - Full Dynamic Range")
plt.colorbar()

import matplotlib.pyplot as plt

r = isolist.sma  # semi-major axis
I = isolist.intens  # mean intensity
print("r:  ", r)
print("I:  ", I)

plt.figure(figsize=(6,4))
plt.plot(r, I, 'o-')
plt.xlabel("Semi-major axis (pixels)")
plt.ylabel("Mean intensity")
plt.title("Surface Brightness Profile")
#plt.gca().invert_yaxis()
print("Radius range:", r[0], "to", r[-1])
plt.figure()
plt.plot(np.log(r), np.log(I), 'o-')
plt.xlabel("log(Semi-major axis)")
plt.ylabel("log(Intensity)")
plt.title("Log-Intensity Profile")

!pip install pyimfit
#!pip install astropy
from astropy.io import fits
import pyimfit


# define a function for making a simple bulge+disk model, where both components
# share the same central coordinate (SimpleModelDescription class)
def galaxy_model(x0, y0, PA_bulge, ell_bulge, n, I_e, r_e, PA_disk, ell_disk, I_0, h):
    model = pyimfit.SimpleModelDescription()
    # define the limits on X0 and Y0 as +/-10 pixels relative to initial values
    model.x0.setValue(x0, [x0 - 10, x0 + 10])
    model.y0.setValue(y0, [y0 - 10, y0 + 10])

    bulge = pyimfit.make_imfit_function('Sersic', label='bulge')
    bulge.PA.setValue(PA_bulge, [0, 180])
    bulge.ell.setValue(ell_bulge, [0, 1])
    bulge.I_e.setValue(I_e, [0, 10*I_e])
    bulge.r_e.setValue(r_e, [0, 10*r_e])
    bulge.n.setValue(n, [0.5, 7])

    disk = pyimfit.make_imfit_function('Exponential', label='disk')
    disk.PA.setValue(PA_disk, [0, 180])
    disk.ell.setValue(ell_disk, [0, 1])
    disk.I_0.setValue(I_0, [0, 10*I_0])
    disk.h.setValue(h, [0, 10*h])

    model.addFunction(bulge)
    model.addFunction(disk)

    return model


model_desc = galaxy_model(x0, y0, PA_bulge=90.0, ell_bulge=0.2, n=1, I_e=1,
                        r_e=24, PA_disk=90.0, ell_disk=0.5, I_0=1, h=25)

imfit_fitter = pyimfit.Imfit(model_desc)
print(model_desc)
print(imfit_fitter)

g_band = data[0]
r_band = data[1]
z_band = data[2]


from photutils.centroids import centroid_com
import numpy as np

#g_masked = g_band.copy()
#r_masked = r_band.copy()
#z_masked = z_band.copy()

g_masked = np.nan_to_num(g_band, nan=0.0)
r_masked = np.nan_to_num(r_band, nan=0.0)
z_masked = np.nan_to_num(z_band, nan=0.0)

yg, xg = centroid_com(g_masked)
yr, xr = centroid_com(r_masked)
yz, xz = centroid_com(z_masked)



from photutils.isophote import Ellipse, EllipseGeometry

def fit_band(band_data, x0, y0):
    geometry = EllipseGeometry(x0=x0, y0=y0, sma=30, eps=0.3, pa=0.0)
    ellipse = Ellipse(band_data, geometry)
    isolist = ellipse.fit_image()
    return isolist



g_iso = fit_band(g_masked, xg, yg)
r_iso = fit_band(r_masked, xr, yr)
z_iso = fit_band(z_masked, xz, yz)



#def integrate_luminosity(isolist, n=10):
#    total_lum = 0
#    for iso in isolist[:n]:
#       # area = np.pi * iso.sample.sma * iso.sample.smb
#        area = np.pi * iso.sample.geometry.sma * iso.sample.geometry.smb
#        total_lum += iso.intens * area
#    return total_lum

def integrate_luminosity(isolist, n=10):
    total_lum = 0
    for iso in isolist[:n]:
        sma = iso.sample.geometry.sma
        eps = iso.sample.geometry.eps
        smb = sma * (1 - eps)
        area = np.pi * sma * smb
        total_lum += iso.intens * area
    return total_lum


L_g = integrate_luminosity(g_iso)
L_r = integrate_luminosity(r_iso)
L_z = integrate_luminosity(z_iso)

print("Bulge Luminosities:")
print(f"g-band: {L_g:.2f}, r-band: {L_r:.2f}, z-band: {L_z:.2f}")



def luminosity_to_mag(L, zero_point=22.5):
    return -2.5 * np.log10(L) + zero_point

m_g = luminosity_to_mag(L_g)
m_r = luminosity_to_mag(L_r)
m_z = luminosity_to_mag(L_z)

print(f"Bulge Apparent Magnitudes:")
print(f"g-band: {m_g:.2f}, r-band: {m_r:.2f}, z-band: {m_z:.2f}")



D_L = 14.8e6  # in parsecs

def apparent_to_absolute(m, D_pc):
    return m - 5 * np.log10(D_pc / 10)

M_g = apparent_to_absolute(m_g, D_L)
M_r = apparent_to_absolute(m_r, D_L)
M_z = apparent_to_absolute(m_z, D_L)

M_g = apparent_to_absolute(m_g, D_L)
M_r = apparent_to_absolute(m_r, D_L)
M_z = apparent_to_absolute(m_z, D_L)

print(f"Bulge Absolute Magnitudes:")
print(f"g: {M_g:.2f}, r: {M_r:.2f}, z: {M_z:.2f}")



# Example: assume M/L_r = 3 (can vary from 1–5 depending on color)
M_L_ratio = 5
solar_Mr = 4.64  # Sun's absolute r-band magnitude

L_bulge = 10**(-0.4 * (M_r - solar_Mr))  # in solar units
mass_bulge = M_L_ratio * L_bulge

print(f"Estimated Bulge Stellar Mass (r-band): {mass_bulge:.2e} Msun")

#r_masked = np.nan_to_num(r_band, nan=np.median(r_band[np.isfinite(r_band)]))
plt.figure()
plt.imshow(z_band, cmap='jet', origin='lower', vmin=0, vmax=20)
plt.title('z-band')
plt.colorbar()
plt.figure()
plt.imshow(r_band, cmap='jet', origin='lower', vmin=0, vmax=20)
plt.title('r-band')
plt.colorbar()
plt.figure()
plt.imshow(g_band, cmap='jet', origin='lower', vmin=0, vmax=20)
plt.title('g-band')
plt.colorbar()
