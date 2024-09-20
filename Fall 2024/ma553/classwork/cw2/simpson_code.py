#!/usr/bin/env python
from math import sqrt

import numpy as np


def f(x):
    return 4 * sqrt(1 - x**2)

def f_np(x):  # NumPy version
    return 4 * np.sqrt(1 - x**2)

def simpson_rule(f, a, b, n):
    """Approximates integral using the Simpson's 1/3rd rule."""
    if n % 2 == 1:
        n += 1
    dx = (b - a) / n
    odd_sum = 0
    even_sum = 0
    for i in range(1, n, 2):
        xi = a + i * dx
        odd_sum += f(xi)
    for i in range(2, n - 1, 2):
        xi = a + i * dx
        even_sum += f(xi)
    return dx * (f(a) + 4 * odd_sum + 2 * even_sum + f(b)) / 3

def simpson_rule_np(f_np, a, b, n):  # NumPy version
    """Approximates integral using the Simpson's 1/3rd rule."""
    if n % 2 == 1:
        n += 1
    [x, dx] = np.linspace(a, b, n + 1, retstep=True)
    fx = f_np(x)
    odd_indx = np.arange(1, n, 2)  # .reshape(-1)
    even_indx = odd_indx + 1
    odd_sum = np.sum(fx[odd_indx])
    even_sum = np.sum(fx[even_indx])
    return dx * (fx[0] + 4 * odd_sum + 2 * even_sum + fx[-1]) / 3

if __name__ == '__main__':
    a = 0
    b = 1
    n = int(input('Enter the number n: '))
    print('===========================')
    print('     Simpson_approx: pi = ', simpson_rule(f, a, b, n))
    print('Simpson_approx_numpy pi = ', simpson_rule_np(f_np, a, b, n))
