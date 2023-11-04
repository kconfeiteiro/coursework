#!/usr/bin/env python3
"""
Krystian Confeiteiro
Dr. Sam
MA 305 - 06DB
Lab 4 (Part b)
10/25/2023
"""

to_float = lambda *inputs: (float(item) for item in inputs)


def func(x):
    value = -3.0 + x * (-3.0 + x * (1.0 + x))
    return value


def estimate_roots(a, b, Tol, func, n_max=1000):
    a, b, Tol = float(a), float(b), float(Tol)
    _prompt1 = f"\n Searching for root in range [{a: 5.2f}, {b: 5.2f}], with tolerance of {Tol:0.8g}"
    print(_prompt1, "\n", "-" * len(_prompt1))

    f_a, f_b = func(a), func(b)
    if f_a * f_b > 0:
        print(" Product of a and b, the Bisection method is not applicable.")
        print(" try different a and/or b.")
        exit()

    n, error = 0, abs(b - a)
    _header = "n\t\tr\t\tfunc(r)\t\terror"
    print(_header, "\n", "-" * len(_prompt1))

    # bisection loop
    while error > Tol:
        n += 1
        estiamte = (a + b) / 2
        f_r = func(estiamte)
        if f_r == 0:
            print(
                f"Got lucky! Estimated root is {estiamte} and function evaluation, f(r), is: {f_r}"
            )
            print(f"For n = {n} tries error <= {error / 2}")
            break
        elif f_r < 0:
            a, f_a = estiamte, f_r
        else:
            b, f_b = estiamte, f_r

        error = error / 2  # or: = b - a
        print(f"{n: 3d} {estiamte: 15.8g} {f_r: 15.8g} {error: 15.8g}")

        if n > n_max:
            print("\nIterations exhausted:")
            print(f"\tFor n = {n} > n_max = {n_max},")
            print("\ttry shorter range or bigger maximum n value.\n")
            break

    return estiamte


print("\n========== SHOWING INPUTS ==========\n")

while True:
    vals = input(" Enter the values of a, b, Tol: ").split()
    vals = to_float(*vals)
    estimate = estimate_roots(*vals, func=func)

    print("-" * 50)
    _bestimates = f"Bestimate: {estimate: 21.14g}"
    print("-" * len(_bestimates), "\n", _bestimates, "\n", "-" * len(_bestimates))

    go_again = input("\nDo you want to go again (y/n): ")
    if go_again.lower() in ["no", "n", "0"]:
        break


print("\n========== REST OF THE VALUES (automated) ==========\n")

_tolerance = 0.5e-8
other_vals = [
    (-1.8, -1.6, _tolerance),
    (-1.3, -0.5, _tolerance),
    (-1.0, 2.0, _tolerance),
]

estimates = []
for _set in other_vals:
    estimate = estimate_roots(*_set, func=func)
    _bestimates = f"Bestimate: {estimate: 21.14g}"
    print("-" * len(_bestimates), "\n", _bestimates, "\n", "-" * len(_bestimates))
    estimates.append(_bestimates)

print("-" * 50)
_finalprompt = "FINAL ESTIAMTES"
print(_finalprompt, "\n", "-" * len(_finalprompt))
for i, (_values, _estimate) in enumerate(zip(other_vals, estimates), 1):
    print(f"{i}. For values `", *_values, f". Estimate: {_estimate}")


print("\n========== LINEAR FUNCTION ==========\n")


def linear_func(x):
    return 1 - 2 * x


_tolerance = 1e-6
other_vals = [
    (-1.8, 1.6, _tolerance),
    (-1.3, 0.5, _tolerance),
    (1.0, 2.0, _tolerance),
]

for i, vals in enumerate(other_vals):
    estimate = estimate_roots(*vals, func=linear_func)
    _bestimates = f"Bestimate: {estimate: 21.14g}"
    print("-" * len(_bestimates), "\n", _bestimates, "\n", "-" * len(_bestimates))
    print(f"{i}. For values `", *vals, f". {_bestimates}")
