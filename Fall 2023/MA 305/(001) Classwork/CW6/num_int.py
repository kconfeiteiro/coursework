"""
Functions to use for numerical integration.
"""


def left_sum(func, a_lim, b_lim, n_iterations):
    """Approximates integrals by summing the area of the rectangles with height taken from the left end."""
    dx = (b_lim - a_lim) / n_iterations
    return dx * sum(func(a_lim + i * dx) for i in range(n_iterations))


def right_sum(func, a_lim, b_lim, n_iterations):
    """Approximates integrals by summing the area of rectangles with height taken from the right end."""
    dx = (b_lim - a_lim) / n_iterations
    return dx * sum(func(a_lim + i * dx) for i in range(1, n_iterations + 1))


def middle_sum(func, a_lim, b_lim, n_iterations):
    """Approximates integrals by summing the area of rectangles with height taken from the right end."""
    dx = (b_lim - a_lim) / n_iterations
    return dx * sum(func(a_lim + i * dx) for i in range(1, n_iterations - 1))
