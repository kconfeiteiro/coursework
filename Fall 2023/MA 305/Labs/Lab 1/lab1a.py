"""
Name: Krystian Confeiteiro
Professor: Dr. Sam
Course: MA-305 - Introduction to Scienfific Computing
Assignment: Lab 1 (Part A) - Problem 1
Script name: lab1b.py
Date: 09/25/2023
"""
from math import sqrt, cos, sin
import math

# problem 1
## part a
### Define function to calculate resistance in parallel
def calc_resistance_parallel(*resistances):
    return 1/sum((1/res) for res in resistances)

resistances = (100, 200, 300) # r1, r2, r3
r_eq = calc_resistance_parallel(*resistances)

## part b
def final_value(principle_amt, rate, frequency, time):
    return round(principle_amt*(1 + (rate/frequency))**(frequency*time), 2)

values = (10_000, 0.08, 4, 20) # p_amt, rate, freq, time
final_val = final_value(*values)

## part c
### Define function to calcualte triangle area (in cm)
def calc_triangle_area(a, b, c):
    s = (a + b + c)/2
    return round(sqrt(s*(s-a)*(s-b)*(s-c)), 3)

triangle_sides = (6, 8, 10) # a, b, c
triangle_area = calc_triangle_area(*triangle_sides)

## part d
### Define function to evaluate the expression
def func(r, theta):
    _exp = lambda x: math.e**x
    return round((_exp(r)*cos(theta)) + (_exp(2*r)*cos(2*theta)), 3)

vals = (-0.3, ((3*math.pi)/4))
evaluated_val = func(*vals)

print(f"""
Problem 1:
----------
part (a) - Equivalent resistance: {round(r_eq, 3)} ohms
part (b) - Final calculated value: ${final_val}
part (c) - Calculated area: {triangle_area} cm^2
part (d) - Evaluated value: {evaluated_val} units
""")

