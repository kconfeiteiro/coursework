#!/usr/bin/env python3
"""
========================================================================
MA305 - CW 6: your name - date
Purpose: To implement Left Sum, Right Sum, and Middle Sum  rules
         approximations for integrals creating some user defined modules.
========================================================================
"""
from math import sqrt, pi, erf


def f(x):
    y = (2 * x + 1) * (x**2 + x + 1) ** 3
    return y


def left_sum(f, a, b, n):
    """Approximates integrals by summing the area of the rectangles with height taken from the left end."""
    dx = (b - a) / n
    lsum = 0
    for i in range(n):
        xi = a + i * dx
        lsum += f(xi)
    return dx * lsum


def right_sum(f, a, b, n):
    """Approximates integrals by summing the area of rectangles with height taken from the right end."""
    dx = (b - a) / n
    rsum = 0
    for i in range(1, n + 1):
        xi = a + i * dx
        rsum += f(xi)
    return dx * rsum


def middle_sum(f, a, b, n):
    """Approximates integrals by summing the area of rectangles with height taken from the midpoint, not completed yet."""
    dx = (b - a) / n
    msum = 0
    return dx * msum


#########################################################################
if __name__ == "__main__":
    # Limits of integration
    a = 0
    b = 1

    # Exact value of the integral
    exact = 20  # exact integral of f(x)
    # exact=sqrt(pi)*erf(b)/2 # exact integral of g(x)

    n = int(input("Enter the number of rectangles n:"))

    # Evaluate the approximate value of the integral using different methods
    approx1 = left_sum(f, a, b, n)
    approx2 = right_sum(f, a, b, n)
    approx3 = middle_sum(f, a, b, n)

    # Compute the absolute errors
    error1 = abs(approx1 - exact)
    error2 = abs(approx2 - exact)
    error3 = abs(approx3 - exact)

    # Print the results in a nice formatted output
    print()
    print("Results using {} rectangles:".format(n))
    print("=============================================")
    print("                 Approximation       Error")
    print("  Left-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx1, error1))
    print(" Right-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx2, error2))
    print("   Mid-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx3, error3))
    print("=============================================")
    print()
