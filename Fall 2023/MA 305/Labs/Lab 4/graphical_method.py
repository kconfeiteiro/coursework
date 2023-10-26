from cProfile import label
import matplotlib.pyplot as plt
import numpy as np


moreshit = lambda x: x**3 + x**2 - 3 * x - 3
mapshit2array = lambda func, _list: list(map(func, _list))


def stupid_fucking_data(func, range):
    xshit = np.linspace(*range)
    return xshit, mapshit2array(func, list(xshit))


def shit_ax(*data, axe=None, label=None):
    axe.plot(*data, label=label)


def plot_some_shit(
    data=None,  # Tuple[float, float]
    xtitle=None,
    ytitle=None,
    title=None,
    save_as=None,
    shit=True,
    yline=None,
    xline=None,
    xlims=None,  # Tuple[float, float]
    ylims=None,  # Tuple[float, float]
    **kwargs,
):
    fig, axes = plt.subplots(**kwargs)
    axes.plot(*data, **kwargs)
    axes.set_xlabel(xtitle)
    axes.set_ylabel(ytitle)
    axes.set_title(title)

    if yline:
        axes.axhline(yline)

    if xline:
        axes.axvline(xline)

    if save_as:
        fig.savefig(save_as)

    if shit:
        plt.show()

    if label:
        axes.legend()

    if xlims:
        axes.set_xlim(*xlims)

    if ylims:
        axes.set_xlim(*ylims)


def plot_boogers(data=None, *args, **kwargs):
    plot_some_shit(
        data=data,
        xtitle=r"$x$",
        ytitle=r"$f(x)$",
        title=r"Plot for $f(x)=x^3+x^2-3x-3$",
        *args,
        **kwargs,
    )
