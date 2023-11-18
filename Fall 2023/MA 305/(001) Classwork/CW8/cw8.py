"""
Krystian Ojeda Confeiteiro
Dr. Sam
MA 305 - 06DB
Classwork 8
11/17/2023
"""

import matplotlib.pyplot as plt
import numpy as np

import helpers as hp

# configurations for this assignment
CONFIG = {
    "datapth": "DATA\\cw8_data.txt",
    "read kwargs": {"delim_whitespace": True, "comment": "#"},
    "x-range": (-10, 10, 100),
}


# prepare data for first plot
DATA = hp.read_data(CONFIG.get("datapth"), **CONFIG.get("read kwargs"))
YEAR, MEN, WOMEN = hp.split_df(DATA)

# plot second plot
fig, axes = plt.subplots()
axes.plot(YEAR, MEN, "o-", label="Men")
axes.plot(YEAR, WOMEN, "d-", label="Women")
axes.set_title("Median Age At First Marrige In U.S. (1890 - 2020)")
axes.set_xlabel("Year")
axes.set_ylabel("Age")
axes.legend()
fig.savefig("fig1.pdf")

# prepare data for second plot using gaussian function
X_VALS = np.linspace(*CONFIG.get("x-range"))
Y_VALS0_5 = hp.gaussian(X_VALS, mean=0, stdev=0.5)
Y_VALS1_0 = hp.gaussian(X_VALS, mean=0, stdev=0.5)
Y_VALS1_5 = hp.gaussian(X_VALS, mean=0, stdev=1.5)

# plot second plot
fig2, axes2 = plt.subplots()
axes2.plot(X_VALS, Y_VALS0_5, "-", label=r"$\sigma=0.5$")
axes2.plot(X_VALS, Y_VALS1_0, "d-", label=r"$\sigma=1.0$")
axes2.plot(X_VALS, Y_VALS1_5, label=r"$\sigma=1.5$")
axes2.set_title(r"Gaussian Function - $g(x)$")
axes2.set_xlabel(r"$x$")
axes2.set_ylabel(r"$g(x)$")
fig2.savefig("fig2.pdf")

# calculate area for part (3)
AREA = hp.calc_area()
print("Area: ", AREA)

# prepare the values of the approximated first derivative (and normalize)
APPROX = hp.normalize(hp.deriv_approx(X_VALS, step=0.1, mean=0, stdev=1))

# plot third plot
axes2.plot(X_VALS, APPROX, label=r"$g'(x)$")
axes2.legend()
fig2.savefig("fig3.pdf")
plt.show()
