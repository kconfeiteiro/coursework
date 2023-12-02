from typing import Callable, Dict, NamedTuple, Tuple

import matplotlib.pyplot as plt
import numpy as np


def newton_raphson(
    guess=None, function=None, first_deriv=None, tolerance=None, prints=False
):
    h = function(guess) / first_deriv(guess)
    count = 0
    while abs(h) >= tolerance:
        h = function(guess) / first_deriv(guess)
        guess -= h

        if prints:
            print("{}. F(x_n) = {}; x_n = {}".format(count, round(function(guess), 4), round(guess, 4)))

        count += 1

    return guess


def set_plot_range(function, setrange=(-10, 10, 100)):
    fmap = lambda func, lst: list(map(func, lst))
    actual = np.linspace(*setrange)
    return (actual, fmap(function, actual))


def plot_function(
    *items,
    plt_cfg={"nrows": 1, "ncols": 1},
    xrange=(-10, 10, 100),
    estimated_value=None,
    figtitle=None,
    xlabel=None,
    ylabel=None,
    est_height=None,
    grid=True,
    save_as=None,
    setlabels=True,
    display=True
):
    fig, axes = plt.subplots(**plt_cfg)

    for func, label in items:
        axes.plot(*set_plot_range(func, setrange=xrange), label=label)

    if grid:
        axes.grid()

    if estimated_value:
        axes.axvline(estimated_value)
        axes.text(
            estimated_value + 0.5,
            est_height,
            s="Estimation: {}".format(round(estimated_value, 3)),
        )

    if figtitle:
        axes.set_title(figtitle)

    if xlabel:
        axes.set_xlabel(xlabel)

    if ylabel:
        axes.set_ylabel(ylabel)

    if save_as:
        fig.savefig(save_as)

    if setlabels:
        axes.legend()

    if display:
        plt.show()
