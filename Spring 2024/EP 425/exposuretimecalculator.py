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
CALC_A = lambda N_STAR_DOT, SNR: (N_STAR_DOT / SNR) ** 2
CALC_B = lambda N_STAR_DOT, N_PIX, A_B, b_dot, d_dot: -(N_STAR_DOT + (N_PIX * A_B(b_dot + d_dot)))
CALC_C = lambda N_PIX, A_B, RHO: -(N_PIX * A_B * (RHO**2))
CALC_NSTAR = ...


def calc_exposure_time(star_mag: float = ..., snr: float = ...):
    pass

SNR = ...
N_STAR_DOT = ...
N_PIX = ...
N_PIX = ...
A_B = ...
RHO = ...
