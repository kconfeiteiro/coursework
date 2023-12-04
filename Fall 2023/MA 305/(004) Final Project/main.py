import os
from math import degrees, e, tan
from time import time

from mpmath import cot, csc, sec

from helpers import newton_raphson, plot_function, uniquefilename

CONFIG = {
    "part a": {
        "x-vals range": (-10, 10, 100),
        "plot config": {
            "figtitle": r"$f(x)$ & $f'(x)$",
            "xlabel": r"$x$",
            "ylabel": r"$y$",
            "est_height": 950,
            "display": False,
            "save_as": uniquefilename("part_a_attempt.jpg", os.getcwd()),
            "tight_layout": True,
            "grid": True,
        },
        "newton-raphson cfg": {
            "tolerance": 1e-12,
            "recursion_limit": None,
            "prints": False,
        },
    },
    "part b": {
        "x-vals range": (-10, 10, 100),
        "plot config": {
            "figtitle": "Finding Maximum Length",
            "xlabel": r"$\gamma$",
            "ylabel": r"$l(\gamma)$",
            "display": False,
            "save_as": uniquefilename("part_b_attempt.jpg", os.getcwd()),
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
            "save_as": uniquefilename("part_c_attempt.jpg", os.getcwd()),
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

# start time
START = time()

# define functions for Newton's Cubic and first derivative
cubic = lambda x: x**3 - 2 * x - 5
dcubic = lambda x: 3 * x**2 - 2

# use Newton's method to determine zero(es) of f(x) (part a)
est_ncubic_zero = newton_raphson(
    guess=0,
    function=cubic,
    dfunction=dcubic,
    **CONFIG["part a"]["newton-raphson cfg"],
)

print("\n{0} Part (a) {0}".format("=" * 20))
print(f"Estimated zero for Newton's cubic: {est_ncubic_zero}")

plot_function(
    (cubic, r"$f(x)=x^3-2x-5$"),
    (dcubic, r"$f'(x)=3x^2-2$"),
    estimated_value=est_ncubic_zero,
    **CONFIG["part a"]["plot config"],
)

# set up for part b (ladder in hallway)
w1, w2 = 9, 7
length = lambda ang: (w1 * csc(ang)) + (w2 * sec(ang))
dlength = lambda ang: (w2 * sec(ang) * tan(degrees(ang))) + (w1 * csc(ang) * cot(ang))

est_angle = newton_raphson(
    guess=12,
    function=length,
    dfunction=dlength,
    **CONFIG["part b"]["newton-raphson cfg"],
)

est_angle = degrees(est_angle)

print("\n{0} Part (b) {0}".format("=" * 20))
print(f"Maximum angle found: {est_angle} deg")
print(f"Maximum length determined l({est_angle} deg): {abs(length(est_angle))} ft")

plot_function(
    (length, r"$l(\gamma)$"),
    (dlength, r"$l'(\gamma)$"),
    **CONFIG["part b"]["plot config"],
)

# set up for part c
temp = lambda t: 68 + 22 * (e ** (-t))
dtemp = lambda t: -22 * (e ** (-t))
est_time = newton_raphson(
    guess=89.5,
    function=temp,
    dfunction=dtemp,
    **CONFIG["part c"]["newton-raphson cfg"],
)

print("\n{0} Part (c) {0}".format("=" * 20))
print(f"Estimated time of death: {est_time}")
print(f"Tempeature at time of death: {temp(est_time)} deg F")

plot_function(
    (temp, r"$T(t)=t+72+12e^{-t}$"),
    (dtemp, r"$T'(t)=1-12e^{-t}$"),
    **CONFIG["part c"]["plot config"],
)


print("\n\n------- Code executed in {} seconds".format(abs(START - time())))
