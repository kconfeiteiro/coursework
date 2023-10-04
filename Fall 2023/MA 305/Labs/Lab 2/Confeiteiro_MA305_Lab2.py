from math import sqrt


# define function to approximate the squart root
# FIXME - fix this goddamn fucking shit it doesn't work and IDK what I am doing.
def approx_sqrt(
    start: float = None,
    precision: float = 0.5e-14,
):
    """
    Approximate the square root of a numbe using the Babylonian Algorithm.

    Args:
        n_terms (float, optional): Number of terms. Defaults to None.
        precision (float, optional): Presion you want to evaluate the algorithm with. Defaults to 1e-14.
        guess (float, optional): Initial guess of square root value. Defaults to None.
    """
    start, precision, vals = float(start), float(precision), []
    babylon = lambda x: 0.5 * (x + (start / x))
    x_0 = start / 2
    while abs(x_0**2 - start) < precision:
        x_0 = babylon(x_0)
        print(f"Next val is fukin: {x_0}")
        vals.append(x_0)

    return x_0, len(vals)


test, count = approx_sqrt(
    5.0,
)

print("Total # iterations: ", count)
print("Approximated sqrt(5): ", test)
print("Actual sqrt(5): ", round(sqrt(5), 4))
