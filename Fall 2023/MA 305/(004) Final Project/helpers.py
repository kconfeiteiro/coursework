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
    """
    Applies the Newton-Raphson method for a mathematical function.

    Parameters
    ----------
    guess : int or float, optional
        Your initial guess for Newton's method, by default None
    function : Callable, optional
        The inital function you want to use Newton's method for, by default None
    dfunction : Callable, optional
        The first derivative of `function`, by default None
    tolerance : Float, optional
        The tolerance (precision) you want to estimate by, by default None
    prints : bool, optional
        Option to bring each iteration of the `while` loop, by default False
    recursion_limit : Int, optional
        The maximum iteration limit (optional), by default None

    Returns
    -------
    Int or float
        The final estimation for the Newton-Raphson method.
    """
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
    """
    Sets the plot range for a given function (for plotting).

    Parameters
    ----------
    function : Callable
        The mathematical function that you want to plot
    setrange : tuple, optional
        The range that you want to plot (for `np.linspace`), by default (-10, 10, 100)

    Returns
    -------
    Tuple[Sequence[float], Sequence[float]]
        Returns a tuple of X and Y values for you to plot for a given mathematical function.
    """
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
    """
    Standard function for plotting a mathematical function.

    Parameters
    ----------
    plt_cfg : dict, optional
        Configruation dictionary for the `plt.subplots()` line, by default {"nrows": 1, "ncols": 1}
    setxrange : tuple, optional
        x-range you want to plot (for `np.linspace`), by default (-10, 10, 100)
    estimated_value : float or int, optional
        The estiamted value from Newton's method (will place a vertical bar where that estimation is), by default None
    figtitle : str, optional
        The figure title, by default None
    xlabel : str, optional
        Figure's x-axis label, by default None
    ylabel : str, optional
        Figure's y-axis label, by default None
    xlim : Tuple, optional
        Limits for the x-axis, by default None
    ylim : Tuple, optional
        Limits for y-axis, by default None
    tight_layout : bool, optional
        Option for a tight-layout plot, by default False
    est_height : Float, optional
        Option to change the height of the annotation for the `estimated_value` value, by default None
    grid : bool, optional
        Option to turn on the plot's grid, by default True
    save_as : str, optional
        What you want to save the plot as, by default None
    setlabels : bool, optional
        Option to turn the legend on (and off), by default True
    display : bool, optional
        Option to display the plot via `matplotlib` GUI, by default True
    return_figure : bool, optional
        Option to return the `fig` and `axes` for further manipulation, by default False

    Returns
    -------
    matplotlib.pyplot.figure
        Returns `fig` and `axes` (if user desires)
    """
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
    """
    Creates a unique file name (i.e., when you copy a file in any OS)

    Parameters
    ----------
    filename : str
        Initial file name
    savepath : str, optional
        Path you want to save the file, by default None
    return_count : bool, optional
        Option to return the current file count, by default False

    Returns
    -------
    str (and an optional counter)
        Returns a unique file name
    """    
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
