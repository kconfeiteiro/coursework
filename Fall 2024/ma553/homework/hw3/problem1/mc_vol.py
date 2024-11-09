#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 13:02:27 2022

@author: Khanal
"""
import random


def mc_volume(n):
    """Approximates volume of the solid
    below x^2+y^2+(z-1)^2=1 and above z^2=x^2+y^2
    using Monte Carlo integration with n random points."""
    count = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(0, 2)
        if x**2 + y**2 < z**2 and x**2 + y**2 < z * (2 - z):
            count += 1
    return 8 * count / n

if __name__ == '__main__':
    n = 1000000
    print("With n=", n)
    print('approx vol of the "Ice-Cream Cone" =', mc_volume(n))

