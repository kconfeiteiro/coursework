from math import cos, pi, sin

import matplotlib.pyplot as plt
import numpy as np


# define function to plot diffraction gratings
def plot_diffractions(
    theta,
    intensity,
    color="blue",
    lw=2,
    figsize=(8, 8),
    figtitle=None,
    save_as=None,
    ylim=None,
    grid=False,
    show=False,
    **kwargs,
):
    fig, axe = plt.subplots(
        subplot_kw={"projection": "polar"}, figsize=figsize, **kwargs
    )
    axe.plot(theta, intensity, color=color, lw=lw)

    if figtitle:
        axe.set_title(figtitle)

    if ylim:
        axe.set_ylim(ylim)

    if grid:
        axe.grid(True)

    if show:
        plt.show()

    if save_as:
        fig.savefig(save_as)


# define function for J_m Bessel Function
def bessel_Jm(m, x, a=0, b=pi, N=1000, h=((pi - 0) / 1000)):
    func = lambda theta, x: cos(m * theta - x * sin(theta))

    # the answer of our integral
    int_ans = func(a, x) + func(b, x)

    # iterates through 1 for our integral answer
    for i in range(1, N):
        const = 4 if (i % 2 == 0) else 2
        int_ans += const * func(a + i * h, x)
        print(f"{i}. Thing: {int_ans}")

    int_ans = (int_ans * h) / 3

    int_ans_final = int_ans / pi
    return int_ans_final


# define function to iterate through function
def map_bessel_fns(index, array, func=bessel_Jm):
    print("\n\n===========================================")
    print(f"Mapping bessel shit for: {func.__name__}")
    return [func(index, k) for k in array]


# define functioun for intensity density
def calc_intensity(r, k, func=bessel_Jm):
    if r <= 1e-8:
        return (1 / (2 * k)) ** 2
    else:
        return (func(1, k * r) / (k * r)) ** 2


def map_intensities(index, array, func=calc_intensity):
    return [func(index, k) for k in array]


# x values as a range from 0 to 20
x1 = np.linspace(0, 20, 1000)

# J_0, J_1, and J_2
J_0 = map_bessel_fns(0, x1, bessel_Jm)
J_1 = map_bessel_fns(1, x1, bessel_Jm)
J_2 = map_bessel_fns(2, x1, bessel_Jm)

# this plots the different lines
plt.plot(x1, J_0, "m-")  # maroon
plt.plot(x1, J_1, "b-")  # blue
plt.plot(x1, J_2, "r-")  # red

# intensity density graph
_lambda = 500e-9  # 500 nm
_k = (2 * pi) / _lambda
_r = np.linspace(0, 1e-6, 1000)


# plot diffraction gratings
def final_intensity(calc_intensity, wavelength, i_0, n_points, separation):
    intensity = np.empty([n_points, n_points], np.float64)
    for i in range(n_points):
        y = separation * i

        for j in range(n_points):
            x2 = separation * j
            r2 = np.sqrt(x2**2 + y**2)

            # this is the lim as r  -> 0, I -> 0.5
            intensity[i, j] = (
                0.5 if r2 < 1e-12 else i_0 * calc_intensity(wavelength, r2)
            )
    return intensity


wavelength, i_0, n_points, separation = 0.5, 1, 500, 0.2
final_intensity = final_intensity(calc_intensity, wavelength, i_0, n_points, separation)

# from textbook
plt.imshow(final_intensity, vmax=0.01, cmap="hot")
plt.gray()
plt.show()
