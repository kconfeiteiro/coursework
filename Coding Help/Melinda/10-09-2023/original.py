# melinda walls
# homework 5
# problem 5.4

# imports
import math as mt
import matplotlib.pyplot as plt
import numpy as np


# this is our J function
def J(m, x):
    # here is a nested function that is our integration
    def f(theta):
        return mt.cos(m * theta - x * mt.sin(theta))

    # defining constants

    # our N value that determines our slices
    N = 1000

    # a is 0 and b is pi
    a = 0
    b = 3.14

    # calculate h
    h = (3.14 - 0) / 1000

    # the answer of our integral
    int_ans = f(a) + f(b)

    # iterates through 1 for our integral answer
    for i in range(1, N):
        # odd
        if i % 2 == 0:
            int_ans = int_ans + (4 * f(a + i * h))

        # even
        else:
            int_ans = int_ans + (2 * f(a + i * h))

    int_ans = (int_ans * h) / 3
    int_ans_final = int_ans / 3.14
    return int_ans_final


# this defines our x values as a range from 0 to 20
x = np.linspace(0, 20, 1000)


# this function iterates through each j function with each x in the linspace
def getJ(index, array, J):
    return [J(index, k) for k in x]


# J_0, J_1, and J_2
J_0 = getJ(0, x, J)
J_1 = getJ(1, x, J)
J_2 = getJ(2, x, J)


# this plots the different lines
# J0 is maroon, J1 is blue, and J2 is red
plt.plot(x, J_0, "m-")
plt.plot(x, J_1, "b-")
plt.plot(x, J_2, "r-")
plt.show()


# --------------- part b ----------------
# this next block of code is for the intensity density graph
# this is our lambda which is 500 nanometers
lambda_val = 500 * 10**-9
# k value
k = (2 * 3.14) / lambda_val
# defines r as values between 0 and 10e-6
r = np.linspace(0, 10**-6, 1000)


# density of intensity function
def densityofi(r, k):
    # if the r is less than or equal to 10e-8 it returns ((1/(2*k))**2)
    if r <= 10**-8:
        return (1 / (2 * k)) ** 2

    # otherwise it returns in the J function
    return (J(1, k * r) / (k * r)) ** 2


# calculating the density usuing x=r, y=k
def getdensityofi(index, array, densityofi):
    return [densityofi(index, k) for k in x]
