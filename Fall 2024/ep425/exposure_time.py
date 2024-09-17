import numpy as np

def exposure_time_calculator(
    target_snr,
    source_mag,
    sky_background,
    telescope_diameter,
    pixel_scale,
    read_noise,
    dark_current,
    quantum_efficiency,
):
    """
    Calculate the required exposure time to achieve a target signal-to-noise ratio.

    Parameters:
    - target_snr: Desired signal-to-noise ratio
    - source_mag: Magnitude of the target object
    - sky_background: Sky background in mag/arcsec^2
    - telescope_diameter: Telescope diameter in meters
    - pixel_scale: Pixel scale in arcsec/pixel
    - read_noise: Read noise in electrons/pixel
    - dark_current: Dark current in electrons/pixel/second
    - quantum_efficiency: Quantum efficiency of the detector (0-1)

    Returns:
    - Exposure time in seconds
    """

    # Convert magnitudes to flux
    source_flux = 10 ** (-0.4 * source_mag)
    sky_flux = 10 ** (-0.4 * sky_background) * pixel_scale**2

    # Calculate signal and noise components
    signal = source_flux * quantum_efficiency * np.pi * (telescope_diameter / 2) ** 2
    noise_sky = np.sqrt(sky_flux * quantum_efficiency * np.pi * (telescope_diameter / 2) ** 2)
    noise_dark = np.sqrt(dark_current)
    noise_read = read_noise

    # Calculate exposure time
    return target_snr**2 * (noise_sky**2 + noise_dark**2 + noise_read**2) / signal**2


# Example usage
target_snr = 10
source_mag = 20
sky_background = 21.5  # mag/arcsec^2
telescope_diameter = 2.0  # meters
pixel_scale = 0.2  # arcsec/pixel
read_noise = 5  # electrons/pixel
dark_current = 0.1  # electrons/pixel/second
quantum_efficiency = 0.8

exposure_time = exposure_time_calculator(
    target_snr,
    source_mag,
    sky_background,
    telescope_diameter,
    pixel_scale,
    read_noise,
    dark_current,
    quantum_efficiency,
)

print(f"Required exposure time: {exposure_time:.2f} seconds")
