import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from photutils.isophote import Ellipse, EllipseGeometry
from photutils.background import Background2D, MedianBackground


# load FITS data
image_path = "data/cutout_216.0328_34.8589.fits"
with fits.open(image_path) as hdul:
    image_data = hdul[0].data
    # if image_data.ndim > 2:
    g_band = image_data[0]
    r_band = image_data[1]
    z_band = image_data[2]
    # else:
        # raise ValueError("Expected a 3D array for g, r, and z filters.")
    header = hdul[0].header

# Process each filter: g_band, r_band, z_band
bands = {'g_band': g_band, 'r_band': r_band, 'z_band': z_band}
for band_name, band_data in bands.items():
    print(f"Analyzing `{band_name}`")
    # Estimate background and subtract
    bkg_estimator = MedianBackground()
    bkg = Background2D(band_data, (64, 64), filter_size=(3, 3), bkg_estimator=bkg_estimator)
    image = band_data - bkg.background

    # Estimate galaxy center (you can use WCS or centroid manually)
    y_center, x_center = np.unravel_index(np.argmax(image), image.shape)

    # Set initial geometry: semi-major axis, ellipticity, PA (deg)
    geometry = EllipseGeometry(
        x0=x_center,
        y0=y_center,
        sma=5.0,
        eps=0.1,
        pa=0.0
    )

    # Fit isophotes
    ellipse = Ellipse(image, geometry)
    isolist = ellipse.fit_image()

    # Plot surface brightness profile
    sma = [iso.sma for iso in isolist]
    try:
        isolist = ellipse.fit_image()
    except Exception as e:
        print(f"Skipping `{band_name}` due to fitting error: {e}")

    intens = [iso.intens for iso in isolist]
    intens_err = [iso.int_err for iso in isolist]

    fig, axe = plt.subplots()
    axe.errorbar(sma, intens, yerr=intens_err, fmt='o', markersize=3, label=f'{band_name} Surface Brightness')
    axe.set_xlabel("Semi-major Axis (pixels)")
    axe.set_ylabel("Mean Intensity")
    axe.set_title(f"{band_name.capitalize()} Surface Brightness Profile")
    axe.grid(True)
    axe.legend()
    fig.savefig(f"{band_name}_Surface_Brightness_Profile.png")


# Process each filter: g_band, r_band, z_band
bands = {'g_band': g_band, 'r_band': r_band, 'z_band': z_band}
for band_name, band_data in bands.items():
    print(f"Analyzing `{band_name}`")
    # Estimate background and subtract
    bkg_estimator = MedianBackground()
    bkg = Background2D(band_data, (64, 64), filter_size=(3, 3), bkg_estimator=bkg_estimator)
    image = band_data - bkg.background

    # Estimate galaxy center (you can use WCS or centroid manually)
    y_center, x_center = np.unravel_index(np.argmax(image), image.shape)

    # Set initial geometry: semi-major axis, ellipticity, PA (deg)
    geometry = EllipseGeometry(
        x0=x_center,
        y0=y_center,
        sma=5.0,
        eps=0.1,
        pa=0.0
    )

    # Fit isophotes
    ellipse = Ellipse(image, geometry)
    try:
        isolist = ellipse.fit_image()
    except Exception as e:
        print(f"Skipping `{band_name}` due to fitting error: {e}")
        continue

    # Plot surface brightness profile
    sma = [iso.sma for iso in isolist]
    intens = [iso.intens for iso in isolist]
    intens_err = [iso.int_err for iso in isolist]

    # Create smooth galaxy model using BModel
    bmodel = BModel(isolist)
    smooth_model = bmodel(image.shape)

    # Generate residual image
    residual_image = image - smooth_model

    # Save the smooth model and residual image
    plt.figure()
    plt.imshow(smooth_model, origin='lower', cmap='viridis')
    plt.colorbar()
    plt.title(f"{band_name.capitalize()} Smooth Galaxy Model")
    plt.savefig(f"{band_name}_Smooth_Model.png")

    plt.figure()
    plt.imshow(residual_image, origin='lower', cmap='viridis')
    plt.colorbar()
    plt.title(f"{band_name.capitalize()} Residual Image")
    plt.savefig(f"{band_name}_Residual_Image.png")
