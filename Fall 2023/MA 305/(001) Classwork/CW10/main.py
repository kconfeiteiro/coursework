import numpy as np
import matplotlib.pyplot as plt
import helpers as hp

# configurations for assignment
CONFIG = {
    "data pth": "DATA\\data10.txt",
    "read kwargs": {
        "delim_whitespace": True,
        "comment": "#",
        "names": "x1 y1 x2 y2 x3 y3	".split(),
    },
}

# read and separate data
DATA = hp.read_data(CONFIG["data pth"], **CONFIG["read kwargs"])
x1, y1, x2, y2, x3, y3 = hp.separate(*CONFIG["read kwargs"]["names"], dataframe=DATA)

# create poly fits for all three sets
p1 = np.polyfit(x1, y1, 1)
p2 = np.polyfit(x2, y2, 1)
p3 = np.polyfit(x3, y3, 1)

xx1 = np.linspace(min(x1), max(x1), 50)
xx2 = np.linspace(min(x2), max(x2), 50)
xx3 = np.linspace(min(x3), max(x3), 50)

z1 = np.polyval(p1, xx1)
z2 = np.polyval(p2, xx2)
z3 = np.polyval(p3, xx3)

# plot everything
fig1, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 7))
ax1.plot(x1, y1, "o", label="Data")
ax1.plot(xx1, z1, "-", label="Best Fit Line")
ax1.set_xlabel(r"$x_1$")
ax1.set_ylabel(r"$y_1$")
ax1.legend()

ax2.plot(x2, y2, "o", label="Data")
ax2.plot(xx2, z2, "-", label="Best Fit Line")
ax2.set_xlabel(r"$x_2$")
ax2.set_ylabel(r"$y_2$")
ax2.legend()

ax3.plot(x3, y3, "o", label="Data")
ax3.plot(xx3, z3, "-", label="Best Fit Line")
ax3.set_xlabel(r"$x_3$")
ax3.set_ylabel(r"$y_3$")
ax3.legend()

fig1.suptitle("Lines Of Best Fit")
fig1.savefig("lab6_fig1.pdf")
plt.show()

print("\n", "-" * 30)
print("Slope and y-intercept value of Data Set A:", p1)
print("Slope and y-intercept value of Data Set B:", p2)
print("Slope and y-intercept value of Data Set C:", p3)
