#!/usr/bin/env python3
import math

"""
========================================================================
MA305 - cw 2: your name - date
Purpose: Find the sum of the convergent series.
========================================================================
"""

N = int(input("Enter a positive integers N: "))

# Geometric series 1+1/2 +1/2^2 + ... +1/2^n + ... sum=a/(1-r)=2
sum_gs = 0
print("\nGeometric series:")
print("n \t S_n")
for n in range(N):
    sum_gs += 1 / 2**n
    print(n + 1, "\t", sum_gs)

print("\n")

# Harmonic series 1+1/2 +1/3 + ... +1/n + ...
print("\nHarmonic series:")
print("n \t S_n")

sum_hs = 0
for n in range(1, N + 1):
    sum_hs += 1 / n
    print(n, "\t", sum_hs)
print("\n")

# Alternating series 1-1/2 +1/3 - ... (-1)^(n+1)/n + ...
print("\nAlternating series:")
print("n \t S_n")

sum_as = 0
for n in range(1, N + 1):
    sum_as += (-1) ** (n + 1) * (1 / n)
    print(n, "\t", sum_as)

print("\n")
print("===============================")
print(" Sum of the first", n, "terms")
print(" 1a. GS = ", sum_gs)
print(" 1b. HS = ", sum_hs)
print(" 1c. AS = ", sum_as)
print("================================")
print("\n")

print("     n              GS                     HS                     AS")
print("=============================================================================")
sum_gs = sum_hs = sum_as = 0
for n in range(N):
    sum_gs += 1 / 2**n
    sum_hs += 1 / (n + 1)
    sum_as += (-1) ** (n + 2) * (1 / (n + 1))
    print(
        "{0:6d} \t {1:20.15f} \t {2:20.15f} \t {3:20.15f}".format(
            n + 1, sum_gs, sum_hs, sum_as
        )
    )

print("\n")
print("  Error in Geometric Series:", abs(2 - sum_gs))
print("Error in Alternating Series:", abs(math.log(2) - sum_as))
print("\n")
