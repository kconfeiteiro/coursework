import numpy as np
import matplotlib.pyplot as plt
import math

start = 0.0
end = 1.0
rad_star = np.arange(start, end, 0.01)  # r / r_\star
mass = 4 * (rad_star / end) ** 3 - 3 * (rad_star / end) ** 4
grav = 4 * (rad_star / 1) - 3 * (rad_star / 1) ** 2

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax1.plot(rad_star, mass, "b-")
ax2.plot(rad_star, grav, "r-")

ax1.set_title("Stellar Interior of Star with constant density")
ax1.set_ylabel("Mass ($M/M_{*}$)", color="blue")
ax2.set_ylabel("Gravity ($g/g_{surface}$)", color="red")
ax1.set_xlabel("Radius ($r/R_{*}$)")

r_start_dec, r_end_dec, r_star = 1, 10, 10
rho_0 = 1  # initial density
rad_star_dec = np.arange(r_start_dec, r_end_dec, 0.01)

mass_dec = 4 ** (rad_star_dec / r_star) ** 3 - 3 * (rad_star_dec / r_star) ** 4
grav_dec = 4 * (rad_star_dec / r_star) - 3 * (rad_star_dec / r_star) ** 2
rho_dec = rho_0 * (1 - (rad_star_dec / r_star))
press_dec = (
    ((-24 / 5) * (rad_star_dec / r_star) ** 2)
    + ((25 / 8) * (rad_star_dec / r_star) ** 3)
    - ((9 / 5) * (rad_star_dec / r_star) ** 4)
    + 1
)
potential_dec = (210 / 13) * (
    ((4 / 5) * (rad_star_dec / r_star) ** 5)
    - ((7 / 6) * (rad_star_dec / r_star) ** 6)
    + ((3 / 7) * (rad_star_dec / r_star) ** 7)
)

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(rad_star_dec, rho_dec, "r", label="Density")
axes.plot(rad_star_dec, mass_dec, "b", label="Mass")
axes.plot(rad_star_dec, grav_dec, "g", label="Gravity")
axes.plot(rad_star_dec, press_dec, "m", label="Pressure")
axes.set_title("Variable Density Star")
axes.set_xlabel(r"Radius ($r$)")
axes.legend(loc="best")
plt.show()
