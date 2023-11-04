#!/usr/bin/env python3

"""
========================================================================
MA305 - Lab 4: Antonio Cascio - October 25, 2023
Purpose: Estimates roots for a given function.
! NOTE: this version assumes F(a)<0<F(b), needs improvement !
========================================================================
"""

# Define constant(s)
Nmax = 1000


# Define functions:
def F(x):
    value = -3.0 + x * (-3.0 + x * (1.0 + x))  # =x**3+x**2-3.0*x-3.0
    return value


def find_roots(a, b, Tol, Nmax, function=F):
    Fa = function(a)
    Fb = function(b)

    # ................ Make sure Bisection is applicable, else exit
    if Fa * Fb > 0:
        print(" F(a)*F(b) > 0, Bisection NOT applicable!")
        print(" try different a, b ? ...exiting")
        exit

    # ................ Initialization:
    print("  n               r            F(r)           error")
    n = 0  # initialize the counter
    error = abs(b - a)  # initialize the error

    # ---------------- Begin Bisection Loop ---------------
    while error > Tol:
        n += 1
        r = (a + b) / 2
        Fr = F(r)
        if Fr == 0:
            print("Got lucky! root =", r, " F(r)=", Fr)
            print(" in", n, " tries", " error <=", error / 2)
            break
        elif Fr < 0:
            a = r
            Fa = Fr
        else:
            b = r
            Fb = Fr

        error = error / 2  # or: = b-a
        print("{0: 3d} {1: 15.8g} {2: 15.8g} {3: 15.8g}".format(n, r, Fr, error))

        if n > Nmax:
            print("....NOT done, iterations exhausted:")
            print(" n=", n, " > Nmax=", Nmax)
            print("try shorter [a,b], or bigger nMAX; Exiting...")
            break

    return r


# ---------------- end of bisection loop ---------------
while True:
    print("\n=========================================================\n")
    a, b, Tol = input(" Enter the values of a, b, Tol:").split()
    a = float(a)
    b = float(b)
    Tol = float(Tol)

    r = find_roots(a, b, Tol, Nmax)

    more = input("Go again (y/n)?: ")
    if more.lower() == "n":
        break

print("\nDone! best estimate for the root:{0: 21.14g}\n".format(r))

print("\n================= Moving on to the linear function =================\n")


def f(x):
    return 1 - 2 * x


a = float(a)
b = float(b)
Tol = float(Tol)

print("\nFor the linear: ")

while True:
    print("\n=========================================================\n")
    a, b, Tol = input(" Enter the values of a, b, Tol:").split()
    a = float(a)
    b = float(b)
    Tol = float(Tol)

    r = find_roots(a, b, Tol, Nmax, function=f)

    more = input("Go again (y/n)?: ")
    if more.lower() == "n":
        break

print("\nDone! best estimate for the root:{0: 21.14g}".format(r))

print("\n=========================================================\n")
print("All done!")
