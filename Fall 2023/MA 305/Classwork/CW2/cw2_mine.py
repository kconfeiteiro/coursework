# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
========================================================================
Krystian Confeiteiro
Dr. Sam
Classwork 2
MA305-06DB
10/03/2023
========================================================================
"""

# Sum of a geometric series
def geometric_sum(a, r):
    return (a / (1 - r))


# Problem 1
def geo_series(n):
    return sum((1 / (2**i)) for i in range(n))


# Problem 2
def harm_series(n):
    return sum((1 / i) for i in range(n))


# Problem 3
def alt_series(n):
    return sum((-(1 ** (i + 1)) / i) for i in range(n))


N = int(input("Enter a positive integer, N: "))
print("\nGeometric series: ", geo_series(N))
print("\nHarmonic series: ", harm_series(N))
print("\nAlternating series: ", alt_series(N))


n = 100_1000_100000
sum_gs = geo_series(n)
sum_hs = harm_series(n)
sum_as = alt_series(n)

print("\n")
print("===============================")
print(" Sum of the first", n, "terms")
print(" 1a. GS = ", sum_gs)
print(" 1b. HS = ", sum_hs)
print(" 1c. AS = ", sum_as)
print("================================")
print("\n")

print("     n              GS                     HS                     AS")
