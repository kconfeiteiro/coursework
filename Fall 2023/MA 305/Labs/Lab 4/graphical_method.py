from cProfile import label
import matplotlib.pyplot as plt
import numpy as np


moreshit = lambda x: x**3 + x**2 - 3 * x - 3
mapshit2array = lambda func, _list: np.array(list(map(func, _list)))


def get_shit_data(func, range):
    xshit = np.linspace(*range)
    return xshit, mapshit2array(func, list(xshit))


def shit_ax(*data, axe=None, label=None):
    axe.plot(*data, label=label)


def plot_some_shit(
    func=moreshit,
    range_of_shit=None,
    xtitle=None,
    ytitle=None,
    title=None,
    save_as=None,
    shit=True,
    xlims=None,  # Tuple[float, float]
    ylims=None,  # Tuple[float, float]
    **kwargs,
):
    fig, axes = plt.subplots()
    axes.plot(*get_shit_data(func, range_of_shit), **kwargs)
    axes.set_xlabel(xtitle)
    axes.set_ylabel(ytitle)
    axes.set_title(title)

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

    return (fig, axes)


shit, othershit = plot_some_shit(
    range_of_shit=(0, 20, 100),
    xtitle=r"$x$",
    ytitle=r"$f(x)$",
    title=r"Plot for $f(x)=x^3+x^2-3x-3$",
    xlims=(2.5, 17.5), # not working
)
