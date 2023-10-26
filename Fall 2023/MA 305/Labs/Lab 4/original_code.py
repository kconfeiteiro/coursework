#!/usr/bin/env python3

"""
========================================================================
MA305 - Lab 4: your name - date
Purpose: ... briefly describe what it does ...
! NOTE: this version assumes F(a)<0<F(b), needs improvement !
========================================================================
"""


# Define function here:
def F(x):
    value = -3.0 + x * (-3.0 + x * (1.0 + x))  # =x**3+x**2-3.0*x-3.0
    return value


# Get input from user and change the string input into number types:
a, b, Tol = input(" Enter the values of a, b, Tol:").split()

a = float(a)
b = float(b)
Tol = float(Tol)

Nmax = 1000

# Print on screen:
print(
    "\n Searching for root in [{0: 5.2f}, {1: 5.2f}], with TOL={2:0.8g}".format(
        a, b, Tol
    )
)
print("-------------------------------------------------------")

# ................ Find values at endpoints:
Fa = F(a)
Fb = F(b)

# ................ Make sure Bisection is applicable, else exit
if Fa * Fb > 0:
    print(" F(a)*F(b) > 0, Bisection NOT applicable !")
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
    # print this iterate
    if n > Nmax:
        print("....NOT done, iterations exhausted:")
        print(" n=", n, " > Nmax=", Nmax)
        print("try shorter [a,b], or bigger nMAX; Exiting...")
        break
# ---------------- end of bisection loop ---------------
print("-------------------------------------------------------")
