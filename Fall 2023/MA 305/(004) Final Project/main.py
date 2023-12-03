from math import e

from helpers import newton_raphson, plot_function, uniquefilename

# configurations for project
CONFIG = {
    "part a": {
        "x-vals range": (-10, 10, 100),
        "plot config": {
            "figtitle": r"$f(x)$ & $f'(x)$",
            "xlabel": r"$y$",
            "ylabel": r"$x$",
            "est_height": 950,
            "display": False,
            "save_as": uniquefilename("part_a_attempt.jpg", "PLOTS\\part a"),
            "tight_layout": True,
            "grid": True,
        },
        "newton-raphson cfg": {
            "tolerance": 1e-12,
            "recursion_limit": None,
            "prints": False,
        },
    },
    "part c": {
        "x-vals range": (-10, 10, 100),
        "plot config": {
            "figtitle": f"Who Killed Commissioner Gordon?",
            "xlabel": r"Time $(t)$",
            "ylabel": r"$T(t)$",
            "tight_layout": True,
            "save_as": uniquefilename("part_c_attempt.jpg", "PLOTS\\part c"),
            "grid": True,
            "display": False,
        },
        "newton-raphson cfg": {
            "tolerance": 1e-12,
            "recursion_limit": 10_000,
            "prints": False,
        },
    },
}

# define functions for Newton's Cubic and first derivative
ncubic = lambda x: x**3 - 2 * x - 5
ncubic_prime = lambda x: 3 * x**2 - 2

# use Newton's method to determine zero(es) of f(x) (part a)
guess1 = newton_raphson(
    guess=0,
    function=ncubic,
    first_deriv=ncubic_prime,
    **CONFIG["part a"]["newton-raphson cfg"],
)

plot_function(
    (ncubic, r"$f(x)=x^3-2x-5$"),
    (ncubic_prime, r"$f'(x)=3x^2-2$"),
    estimated_value=guess1,
    **CONFIG["part a"]["plot config"],
)

# set up for part c
tempfunc = lambda x: x + 72 + 12 * (e ** (-x))
tempfunc_prime = lambda x: 1 - 12 * (e ** (-x))
guess2 = newton_raphson(
    guess=89.5,
    function=tempfunc,
    first_deriv=tempfunc_prime,
    **CONFIG["part c"]["newton-raphson cfg"],
)

plot_function(
    (tempfunc, r"$T(t)=t+72+12e^{-t}$"),
    (tempfunc_prime, r"$T'(t)=1-12e^{-t}$"),
    **CONFIG["part c"]["plot config"],
)
