"""
Functions that we are going to numerically integrate
"""

from math import exp


def f_func(x):
    return (2 * x + 1) * (x**2 + x + 1) ** 3


def g_func(x):
    return exp(-(x**2))
