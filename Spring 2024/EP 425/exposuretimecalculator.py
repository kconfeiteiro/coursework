"""
Calculations of exposure times for observational astronomy.

Module Information
------------------
Workspace: EP 425
FIlename: exposuretimecalculator.py
Path: exposuretimecalculator.py
Created: February, 01 2024
"""
from math import sqrt

QUADRATICFORM = lambda a, b, c: (-b + sqrt(b**2 - (4 * a * c))) / (2 * a)
CALC_A = lambda n_star_dot, snr: (n_star_dot / snr) ** 2
CALC_B = lambda n_star_dot, n_pix, a_b, b_dot, d_dot: -(n_star_dot + (n_pix * a_b(b_dot + d_dot)))
CALC_C = lambda n_pix, a_b, rho: -(n_pix * a_b * (rho**2))
CALC_NSTAR = ...


def calc_exposure_time(star_mag: float = ..., snr: float = ...):
    pass



KWARGS = {
    "n_star_dot": ...,
    "": ...
}
