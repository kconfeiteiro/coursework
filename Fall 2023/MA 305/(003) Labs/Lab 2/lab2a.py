# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
================================
| Student: Krystian Confeiteiro
| Professor: Dr. Sam
| Assignment: Lab 2a
| Course: MA 305 - 06DB
| Date: 10/04/2023
================================


"""


from math import sqrt


# define function to calculate percent error
def percent_error(approx=None, actual=None):
    return round((abs(approx - actual) / actual) * 100, 5)


# define function to approximate the squart root
def approx_sqrt(start=None, precision=1e-7, return_list=False):
    start, precision, vals = float(start), float(precision), []
    babylon = lambda x: 0.5 * (x + (start / x))
    x_0 = float(start) / 2
    while abs(x_0**2 - start) > float(precision):
        x_0 = babylon(x_0)
        vals.append(x_0)
        print(f"{len(vals)}th term: {x_0}")

    return (x_0, len(vals), vals) if return_list else (x_0, len(vals))


# read user input (w/ validation loop)
while True:
    try:
        input_val = float(input("(1.) Enter number for square root approximation: "))
        break
    except:
        print("Invalid Input.\n")

# calculate approximate and actual square roots of inputted value
test, count = approx_sqrt(input_val)
act_sqrt = sqrt(input_val)

print("\nUser Input Value: ", input_val)
print("Total Iterations: ", count)
print(f"Approximated sqrt({input_val}): ", test)
print(f"Actual sqrt({input_val}): ", act_sqrt)
print(f"Percent error: {percent_error(test, act_sqrt)}%")
print('\nAll terms of ')
