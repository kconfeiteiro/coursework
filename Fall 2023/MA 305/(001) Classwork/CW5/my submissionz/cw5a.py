#!/usr/bin/env python3
"""
========================================================================
MA305 - CW 5a: Krystian Confeiteiro - 10/30/2023
Purpose: Reading and arrays from a datafile and calculate the average
========================================================================
"""
import sys


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


def save_as_txt(filename, lines, mode="w"):
    with open(filename, mode) as file:
        file.writelines(lines)


#######################################################################
# ======================================================================
if __name__ == "__main__":
    datafile = input("Enter the name of the file to read data from: ")
    # datafile = "dat5a.txt"
    f = open(datafile, "r")
    # f = sys.stdin

    # Read data from a file and store the values in lists
    line = f.readline()
    print(line, end="")
    data = f.readlines()
    print(data)

    x, y = [], []
    for line in data:
        Line = line.split()
        print(Line)
        x.append(float(Line[2]))
        y.append(float(Line[3]))

    f.close()
    n = len(x)

    print(f"\n{n} lines from 'dat5.txt' are read for calculations!")
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
    print(f"x[{xi}]= {xmax}")
    print(f"y[{yi}]= {ymax}")
    print("Max: x[{0:1d}]={1:0.2f}   y[{2:1d}]={3:0.2f}\n".format(xi, xmax, yi, ymax))

    save_as_txt("out.txt", data)
