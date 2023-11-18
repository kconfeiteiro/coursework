#!/usr/bin/env/python3
"""
=========================================================
MA305 - Classwork 10: Antonio Cascio - 17 November 2023
Purpose:
=========================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# Reading the data file into matrix M
M = np.loadtxt("week7/data10.txt", skiprows=3)

#########################################################################
# Extracting the first two columns of M to arrays x and y
x1 = M[:, 0]
y1 = M[:, 1]

# Plotting datasets
# plt.plot(x1,y1,'o')
# plt.show()

# Using polyfit to fit (x,y) to a straight line
p1 = np.polyfit(x1, y1, 1)
print(
    "Slope and y-intercept value of Data Set A:", p1
)  # Printing p1 to get slope of line and y-intercept

# Defining 50 equally spaced points in the range of x values, then use polyval to evaluate the fit at these points
xx1 = np.linspace(min(x1), max(x1), 50)
z1 = np.polyval(p1, xx1)

# Plot the points and the line on the same window
fig = plt.figure()
plt.plot(x1, y1, "o", x1, z1, "-")
plt.legend(["Data", "Line of Best Fit"], loc="best")
plt.title("Least Square Fit of a Straight Line for Data Set A")
plt.xlabel("$X_1$")
plt.ylabel("$Y_1$")
plt.show()
fig.savefig("figure1.png")
#########################################################################
# Extracting the second two columns of M to arrays x and y
x2 = M[:, 2]
y2 = M[:, 3]

# Plotting datasets
plt.plot(x2, y2, "o")
plt.show()

# Using polyfit to fit (x,y) to a straight line
p2 = np.polyfit(x2, y2, 1)
print(
    "Slope and y-intercept value of Data Set B:", p2
)  # Printing p2 to get slope of line and y-intercept

# Defining 50 equally spaced points in the range of x values, then use polyval to evaluate the fit at these points
xx2 = np.linspace(min(x2), max(x2), 50)
z2 = np.polyval(p1, xx2)

# Plot the points and the line on the same window
fig = plt.figure()
plt.plot(x2, y2, "o", x2, z2, "-")
plt.legend(["Data", "Line of Best Fit"], loc="best")
plt.title("Least Square Fit of a Straight Line for Data Set B")
plt.xlabel("$X_2$")
plt.ylabel("$Y_2$")
plt.show()
fig.savefig("figure2.png")
#########################################################################
# Extracting the third two columns of M to arrays x and y
x3 = M[:, 4]
y3 = M[:, 5]

# Plotting datasets
plt.plot(x3, y3, "o")
plt.show()

# Using polyfit to fit (x,y) to a straight line
p3 = np.polyfit(x3, y3, 1)
print(
    "Slope and y-intercept value of Data Set C:", p3
)  # Printing p3 to get slope of line and y-intercept

# Defining 50 equally spaced points in the range of x values, then use polyval to evaluate the fit at these points
xx3 = np.linspace(min(x3), max(x3), 50)
z3 = np.polyval(p1, xx3)

# Plot the points and the line on the same window
fig = plt.figure()
plt.plot(x3, y3, "o", x3, z3, "-")
plt.legend(["Data", "Line of Best Fit"], loc="best")
plt.title("Least Square Fit of a Straight Line for Data Set C")
plt.xlabel("$X_3$")
plt.ylabel("$Y_3$")
plt.show()
fig.savefig("figure3.png")
