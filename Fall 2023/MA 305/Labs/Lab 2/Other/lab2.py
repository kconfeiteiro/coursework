# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Antonio Cascio
Dr. Sam - MA305, Section 06
Lab 2
10/04/2023
"""

import math

# calculate inner value of babylonian algorithm
def babylon(x, y):
    return (1 / 2) * (x + (y / x))

# eval entire babylonian algorithm
def babylonian_algorithm(main, epsilon):
    x_nplus1 = main / 2
    print("\nAlgorithm terms")
    print("---------------\n")

    count = 0
    print("0. ", x_nplus1)
    while abs(x_nplus1**2 - main) > float(epsilon):
        x_nplus1 = babylon(x_nplus1, main)
        count += 1
        print(f"{count}. ", x_nplus1)
    return x_nplus1

# read user input
user_val = input("Enter number: ")
user_val = float(user_val)

# approximate & actual square roots
approx = babylonian_algorithm(user_val, 1e-7)
actual = math.sqrt(user_val)

# final print statements
print("\n---------------")
print("User input: ", user_val)
print("Approximate square root: ", approx)
print("Actual value: ", actual)

print("\n---------------")
print("THE END. Thank you for coming to my TED Talk xD")
