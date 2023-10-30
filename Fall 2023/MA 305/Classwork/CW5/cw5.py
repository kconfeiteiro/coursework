#!/usr/bin/env python3

"""
========================================================================
MA305 - CW 5: Antonio Cascio - 10/30/2023
Purpose: Reading and arrays from a datafile and calculate the average
========================================================================
"""


def calc_average(x):
    """calculates average of the values in the list x"""
    n = len(x)
    s = 0
    for i in range(n):
        s += x[i]
    return s / n


def calc_max(x):
    """calculates maximum value and its location in the list x"""
    n = len(x)
    maxval = x[0]
    maxloc = 0
    for i in range(1, n):
        if x[i] > maxval:
            maxval = x[i]
            maxloc = i
    return maxval, maxloc


#######################################################################
# ======================================================================
if __name__ == "__main__":
    f = open("dat5.txt", "r")

    # Read the data from a file and store the values in appropriate lists
    line = f.readline()
    print(line, end="")
    n = 0
    x, y = [], []
    while True:
        line = f.readline()
        Line = line.split()
        if int(Line[0]) == 0:
            break
        print(Line)
        x.append(float(Line[2]))
        y.append(float(Line[3]))
        n += 1
    f.close()
    print()

    print(n, "lines from 'dat5.txt' are read for calculations!")
    print("           x       y")
    for i in range(n):
        print("\t {0:-5.2f} \t {1:-5.2f}".format(x[i], y[i]))
    print("=======================")

    # Compute and print the average of x and y
    xave = calc_average(x)
    yave = calc_average(y)
    print("Average: {0:-5.2f} \t {1:-5.2f}".format(xave, yave))

    # Evaluate the maximum values in x and y
    xmax, xi = calc_max(x)
    ymax, yi = calc_max(y)
    # print('x[', xi, ']=',xmax)
    # print('y[', yi, ']=',ymax)
    print("Max: x[{0:1d}]={1:0.2f}   y[{2:1d}]={3:0.2f}".format(xi, xmax, yi, ymax))
    print()
