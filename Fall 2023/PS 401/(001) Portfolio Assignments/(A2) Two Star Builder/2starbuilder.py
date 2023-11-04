import numpy as np
import matplotlib.pyplot as plt
from math import pi

G = 6.67e-11

def plot_star(
    *data,
    title,
    xlabel,
    ylabel,
    save_as = None
):
    fig, axes = plt.subplots()
    axes.plot(*data)
    axes.set_title(title)
    axes.set_ylabel(ylabel)
    axes.set_xlabel(xlabel)

    if save_as:
        fig.savefig(save_as)

# start, stop, and range
start = 0
end = 1
rad_star = np.arange(start, end, 0.01)

## mass and gravity equation
mass = lambda r: 4*pi*r**2
grav = lambda r: (G*M_r)

# decreasing density stat
start_dec = 1
end_dec = 10
rad_star_dec = np.arange(start_dec, end_dec, 0.01)

# functions for decreasing density
mass_dec =
grav_dec =
rho_dec =
press_dec =
epot_dec =

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax2 = ax1.twinx()
# ax1.plot(rad_star,mass, 'b-')
# ax2.plot(rad_star,grav, 'r-')

# ax1.set_title("Stellar Interior of Star with constant density")
# ax1.set_ylabel('Mass ($M/M_{*}$)', color='blue')
# ax2.set_ylabel('Gravity ($g/g_{surface}$)', color='red')
# ax1.set_xlabel('Radius ($r/R_{*}$)')

# plt.show()

fig = plt.figure()
axes = fig.add_subplot(111)


axes.plot(rad_star_dec, rho_dec, 'r', label='Density')
axes.plot(rad_star_dec, mass_dec, 'b', label='Mass')
axes.plot(rad_star_dec, grav_dec, 'g', label='Gravity')
axes.plot(rad_star_dec, press_dec, 'm', label='Pressure')

axes.set_title("")#<--Enter appropriate plot title in the quotations
axes.set_xlabel('')#<--Enter appropriate x-axis title in the quotations
axes.set_ylabel('')#<--Enter appropriate y-axis title in the quotations

axes.legend(loc='best')
plt.show()


