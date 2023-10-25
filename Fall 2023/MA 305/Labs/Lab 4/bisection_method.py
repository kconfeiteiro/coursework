#!/usr/bin/env python3
"""
Krystian Confeiteiro
Dr. Sam
MA 305 - 06DB
Lab 4
10/25/2023
"""


def func(x):
    value = -3.0 + x * (-3.0 + x * (1.0 + x))
    return value


to_float = lambda *inputs: (float(item) for item in inputs)

N_MAX = 1000
values = input(" Enter the values of a, b, Tol:").split()
a, b, Tol = to_float(*values)

_prompt1 = f"\n Searching for root in [{a: 5.2f}, {b: 5.2f}], with TOL={Tol:0.8g}"
print(_prompt1, "\n", "-" * len(_prompt1))

# find endpoint values
f_a, f_b = func(a), func(b)

#  make sure Bisection is applicable, else exit
if f_a * f_b > 0:
    print(" func(a) * func(b) > 0, Bisection method is not applicable.")
    print(" try different `a` and/or `b`.")
    exit()

#  initialization:
_header = "  n\t\tr\t\tfunc(r)\t\terror"
print(_header, "\n", "-" * len(_header))

# initialize counter and error
n, error = 0, abs(b - a)

# bisection loop
while error > Tol:
    n += 1
    r = (a + b) / 2
    f_r = func(r)
    if f_r == 0:
        print(f"Got lucky! root = {r} and func({r}) = {f_r}")
        print(f"For n = {n} tries error <= {error/2}")
        break
    elif f_r < 0:
        a, f_a = r, f_r
    else:
        b, f_b = r, f_r

    error = error / 2  # or: = b - a
    print(f"{n: 3d} {r: 15.8g} {f_r: 15.8g} {error: 15.8g}")

    # print this iterate
    if n > N_MAX:
        print("\nIterations exhausted:")
        print(f"\tFor n = {n} > n_max = {N_MAX},")
        print("\ttry shorter range or bigger maximum `n` value.\n")
        break

# print final root estimate
print("-" * 50)
print(f"Best estimate:{r: 21.14g}")
