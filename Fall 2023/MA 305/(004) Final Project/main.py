import matplotlib.pyplot as plt
import numpy as np

from helpers import newton_raphson, plot_function

# configurations for project
CONFIG = {
    "x-vals range": (-10, 10, 100),
    "tolereance": 1e-12,
    "initial guess": 0,
}

# define functions for Newton's Cubic and first derivative
ncubic = lambda x: x**3 - 2 * x - 5
ncubic_prime = lambda x: 3 * x**2 - 2

# use Newton's method to determine zero(es) of f(x)
guess1 = newton_raphson(
    CONFIG["initial guess"],
    function=ncubic,
    first_deriv=ncubic_prime,
    tolerance=CONFIG["tolereance"],
    prints=True,
)
print("Guess 1: ", guess1)

# plot function(s) for visualization
plot_function(
    (ncubic, r"$f(x)=x^3-2x-5$"),
    (ncubic_prime, r"$f'(x)=3x^2-2$"),
    estimated_value=guess1,
    figtitle=r"$f(x)$ & $f'(x)$",
    xlabel=r"$y$",
    ylabel=r"$x$",
    est_height=950,
    grid=True,
)
