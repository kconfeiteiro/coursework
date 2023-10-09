# melinda walls
# homework 5
# problem 5.4

# imports
import math as mt
import matplotlib.pyplot as plt
import numpy as np


# this is our J function
def J_bessel(m, x):
    # here is a nested function that is our integration
    def f(theta):
        return mt.cos(m * theta - x * mt.sin(theta))

    # defining constants
    # our N value that determines our slices
    N = 1000

    # a is 0 and b is pi
    a = 0
    b = 3.14

    # calculate h = a-b/N
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
J_0 = getJ(0, x, J_bessel)
J_1 = getJ(1, x, J_bessel)
J_2 = getJ(2, x, J_bessel)


# this plots the different lines
# J0 is maroon/pink?, J1 is blue, and J2 is red
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
def densityofi(I, k):  # Intensity
    return ((J_bessel(1, k * r)) / (k * r)) ** 2


# for this i couldnt get it to be over 50 without it taking a very long time
num_points = 50

# this is for graphing purposes
linewidth = 0.5


# creating an empty set for the intensity denisty so that it can get filled
# by our intensity values
intensity_density = np.empty([50, 50], np.float64)


# this iterates through our points to get the x and y values
for a in range(num_points):
    # y values using our number of points and the linewidth that we chose
    y_val = (a - ((0.5) * num_points)) * linewidth

    for b in range(num_points):
        # x values
        x_val = (b - ((0.5) * num_points)) * linewidth
        # the distance in the line or the magnitude is r = sqrt(a^2 + b^2)
        r = np.sqrt(((a) ** 2) + ((b) ** 2))

        # the intensity density vector is filled in the for loop
        intensity_density[a, b] = densityofi(lambda_val, r)


# from textbook
plt.imshow(intensity_density, vmax=0.01, cmap="hot")
plt.gray()
plt.show()
