import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from photutils.isophote import Ellipse, EllipseGeometry, build_ellipse_model
from photutils.background import Background2D, MedianBackground

# Load FITS data
image_path = "data/cutout_216.0328_34.8589.fits"
with fits.open(image_path) as hdul:
    image_data = hdul[0].data
    g_band, r_band, z_band = image_data[0], image_data[1], image_data[2]

# Process each filter: g_band, r_band, z_band
bands = {'g_band': g_band, 'r_band': r_band, 'z_band': z_band}
for band_name, band_data in bands.items():
    print(f"Analyzing `{band_name}`")

    # Estimate background and subtract
    bkg_estimator = MedianBackground()
    bkg = Background2D(band_data, (64, 64), filter_size=(3, 3), bkg_estimator=bkg_estimator)
    image = band_data - bkg.background

    # Estimate galaxy center
    y_center, x_center = np.unravel_index(np.argmax(image), image.shape)

    # Set initial geometry
    geometry = EllipseGeometry(x0=x_center, y0=y_center, sma=5.0, eps=0.1, pa=0.0)

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

    plt.figure()
    plt.errorbar(sma, intens, yerr=intens_err, fmt='o', markersize=3, label=f'{band_name} Surface Brightness')
    plt.xlabel("Semi-major Axis (pixels)")
    plt.ylabel("Mean Intensity")
    plt.title(f"{band_name.capitalize()} Surface Brightness Profile")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"{band_name}_Surface_Brightness_Profile.png")

    # Create smooth galaxy model
    if isolist:
        smooth_model = build_ellipse_model(image.shape, isolist)
    else:
        print(f"Skipping `{band_name}` due to empty isolist.")
        continue

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


    # Plot additional isophote properties
    plt.figure(figsize=(10, 5))
    plt.suptitle(f"{band_name.capitalize()} Isophote Properties")

    plt.subplot(221)
    plt.errorbar(sma, [iso.eps for iso in isolist], yerr=[iso.ellip_err for iso in isolist], fmt='o', markersize=4)
    plt.xlabel('Semimajor axis length')
    plt.ylabel('Ellipticity')

    plt.subplot(222)
    plt.errorbar(sma, [iso.pa / np.pi * 180. for iso in isolist], yerr=[iso.pa_err / np.pi * 180. for iso in isolist], fmt='o', markersize=4)
    plt.xlabel('Semimajor axis length')
    plt.ylabel('PA (deg)')

    plt.subplot(223)
    plt.errorbar(sma, [iso.x0 for iso in isolist], yerr=[iso.x0_err for iso in isolist], fmt='o', markersize=4)
    plt.xlabel('Semimajor axis length')
    plt.ylabel('X0')

    plt.subplot(224)
    plt.errorbar(sma, [iso.y0 for iso in isolist], yerr=[iso.y0_err for iso in isolist], fmt='o', markersize=4)
    plt.xlabel('Semimajor axis length')
    plt.ylabel('Y0')

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)
    plt.savefig(f"{band_name}_Isophote_Properties.png")
