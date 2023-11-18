import numpy as np
import matplotlib.pyplot as plt
import helpers as hp

CONFIG = {
    "data pth": "DATA\\data10.txt",
    "read kwargs": {
        "delim_whitespace": True,
        "comment": "#",
        "names": "x1 y1 x2 y2 x3 y3	".split(),
    },
}


DATA = hp.read_data(CONFIG["data pth"], **CONFIG["read kwargs"])
x1, y1 = hp.separate("x1", "x2", dataframe=DATA)

p1 = np.polyfit(x1, y1, 1)
xx1 = np.linspace(min(x1), max(x1), 50)
z1 = np.polyval(p1, xx1)
print("p1: ", p1)

fig1, axes1 = plt.subplots()
axes1.plot(x1, y1, label="Data")
axes1.plot(x1, z1[: len(x1)], label="Best Fit Line")
axes1.set_xlabel(r"$x_1$")
axes1.set_ylabel(r"$y_1$")
axes1.set_title("Line of Best Fit for $f(x) = x$")
axes1.legend()
fig1.savefig("fig1.pdf")
plt.show()

# fig = plt.figure()
# plt.plot(x1, y1, "o", x1, z1, "-")
# plt.legend(["Data", "Line of Best Fit"], loc="best")
# plt.title("Least Square Fit of a Straight Line for Data Set A")
# plt.xlabel(r"$x_1$")
# plt.ylabel(r"$y_1$")
# plt.show()
# fig.savefig("figure1.png")

# x2, y2 = hp.separate("x2", "y2", dataframe=DATA)

# # Plotting datasets
# plt.plot(x2, y2, "o")
# plt.show()

# p2 = np.polyfit(x2, y2, 1)
# print("Slope and y-intercept value of Data Set B:", p2)

# xx2 = np.linspace(min(x2), max(x2), 50)
# z2 = np.polyval(p1, xx2)

# fig = plt.figure()
# plt.plot(x2, y2, "o", x2, z2, "-")
# plt.legend(["Data", "Line of Best Fit"], loc="best")
# plt.title("Least Square Fit of a Straight Line for Data Set B")
# plt.xlabel(r"$x_2$")
# plt.ylabel(r"$y_2$")
# plt.show()
# fig.savefig("figure2.png")

# x3, y3 = hp.separate("x2", "y2", dataframe=DATA)

# # Plotting datasets
# plt.plot(x3, y3, "o")
# plt.show()

# p3 = np.polyfit(x3, y3, 1)
# print("Slope and y-intercept value of Data Set C:", p3)

# xx3 = np.linspace(min(x3), max(x3), 50)
# z3 = np.polyval(p1, xx3)

# fig = plt.figure()
# plt.plot(x3, y3, "o", x3, z3, "-")
# plt.legend(["Data", "Line of Best Fit"], loc="best")
# plt.title("Least Square Fit of a Straight Line for Data Set C")
# plt.xlabel("$X_3$")
# plt.ylabel("$Y_3$")
# plt.show()
# fig.savefig("figure3.png")
