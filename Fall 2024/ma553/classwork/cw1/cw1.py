#!/usr/bin/env python
import sys
import math
from num_int import trapezoid_rule, midpoint_rule
from num_int import simpson_rule as simp
import pi
import time

"""
========================================================================
MA453 - Classwork 1: Krystian Confeiteiro - 09/06/2024
Purpose: To compute pi using midpoint, trapezoid and simpson rules for a
         definite integral, sum of analternating series and Monte Carlo
         method (Dart Board algorithm)
Input:   Number of points as a command line argument
         e.g., run with: >>> python cw1.py 100
Output:  Approximate value of pi from different methods
========================================================================
"""

if len(sys.argv) < 2:
    print("Error: must supply a number of points as a command line argument")
else:
    n = int(sys.argv[1])

    f = lambda x: 4 / (1 + x**2)

    t_start = time.time()
    approx1 = trapezoid_rule(f, 0, 1, n)
    approx2 = midpoint_rule(f, 0, 1, n)
    approx3 = simp(f,0,1,n)
    approx4 = pi.alternating_series_pi(n)
    approx5 = pi.dart_board_pi(n)

    error1 = abs(approx1 - math.pi)
    error2 = abs(approx2 - math.pi)
    error3 = abs(approx3 - math.pi)
    error4 = abs(approx4 - math.pi)
    error5 = abs(approx5 - math.pi)

    print()
    print("Approximation to pi using n={}:".format(n))
    print("======================================================")
    print("                  Approximation         Error ")
    print("   Trapezoid:  {0:18.16f}  {1:18.16f}".format(approx1, error1))
    print("    Midpoint:  {0:18.16f}  {1:18.16f}".format(approx2, error2))
    print("     Simpson:  {0:18.16f}  {1:18.16f}".format(approx3, error3))
    print("  Series Sum:  {0:18.16f}  {1:18.16f}".format(approx4, error4))
    print(" Monte Carlo:  {0:18.16f}  {1:18.16f}".format(approx5, error5))
    print("======================================================")
    t_end = time.time()
    print("Elapsed time:", t_end - t_start)
    print()