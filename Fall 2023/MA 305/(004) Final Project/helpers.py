import os

import matplotlib.pyplot as plt
import numpy as np


def newton_raphson(
    guess=None,
    function=None,
    dfunction=None,
    tolerance=None,
    prints=False,
    recursion_limit=None,
):
    h, count = function(guess) / dfunction(guess), 0
    while abs(h) >= tolerance:
        try:
            h = function(guess) / dfunction(guess)
        except ZeroDivisionError:
            h = function(guess) / 1e-10

        guess -= h

        if prints:
            print(
                "{}. F(x_n) = {:>22};\t\t x_n = {:>12}".format(
                    count, round(function(guess), 4), round(guess, 4)
                )
            )

        if count and (count == recursion_limit):
            break

        count += 1

    guess = float(guess)
    if prints:
        print(f"\nFinal estimated answer (in {count} tries): {guess}")

    return guess


def set_plot_range(function, setrange=(-10, 10, 100)):
    fmap = lambda func, lst: list(map(func, lst))
    actual = np.linspace(*setrange)
    return (actual, fmap(function, actual))


def plot_function(
    *items,
    plt_cfg={"nrows": 1, "ncols": 1},
    setxrange=(-10, 10, 100),
    estimated_value=None,
    figtitle=None,
    xlabel=None,
    ylabel=None,
    xlim=None,
    ylim=None,
    tight_layout=False,
    est_height=None,
    grid=True,
    save_as=None,
    setlabels=True,
    display=True,
    return_figure=False,
):
    fig, axes = plt.subplots(**plt_cfg)

    for func, label in items:
        axes.plot(*set_plot_range(func, setrange=setxrange), label=label)

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

    if xlim:
        axes.set_xlim(*xlim)

    if ylim:
        axes.set_ylim(*ylim)

    if tight_layout:
        fig.tight_layout()

    if setlabels:
        axes.legend()

    if save_as:
        path, _ = os.path.split(save_as)
        if not os.path.exists(path):
            os.makedirs(path)

        fig.savefig(save_as)

    if display:
        plt.show()

    if return_figure:
        return fig, axes


def uniquefilename(
    filename,
    savepath=None,
    return_count=False,
):
    base_name, ext = os.path.splitext(filename)
    unique_name, counter = filename, 1
    while os.path.exists(os.path.join(savepath, unique_name)):
        counter += 1
        unique_name = f"{base_name}({counter}){ext}"

    new_name = os.path.join(savepath, unique_name)

    if return_count:
        return new_name, counter
    else:
        return new_name
