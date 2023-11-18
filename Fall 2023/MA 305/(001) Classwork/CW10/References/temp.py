import numpy as np
import matplotlib.pyplot as plt

M = np.loadtxt("DATA\\data10.txt", skiprows=3)
x1 = M[:, 0]
y1 = M[:, 1]
x2 = M[:, 2]
y2 = M[:, 3]
x3 = M[:, 4]
y3 = M[:, 5]

p1 = np.polyfit(x1, y1, 1)
p2 = np.polyfit(x2, y2, 1)
p3 = np.polyfit(x3, y3, 1)

xx1 = np.linspace(min(x1), max(x1), 50)
xx2 = np.linspace(min(x2), max(x2), 50)
xx3 = np.linspace(min(x3), max(x3), 50)

z1 = np.polyval(p1, xx1)
z2 = np.polyval(p2, xx2)
z3 = np.polyval(p3, xx3)


fig = plt.figure()
plt.plot(x1, y1, "o", xx1, z1, "-")
plt.legend(["Data", "Line of Best Fit"], loc="best")
plt.title("Least Square Fit of a Straight Line for Data Set A")
plt.xlabel("$X_1$")
plt.ylabel("$Y_1$")

fig.savefig("figure1.png")
fig = plt.figure()
plt.plot(x2, y2, "o", xx2, z2, "-")
plt.legend(["Data", "Line of Best Fit"], loc="best")
plt.title("Least Square Fit of a Straight Line for Data Set B")
plt.xlabel("$X_2$")
plt.ylabel("$Y_2$")

fig.savefig("figure2.png")
fig = plt.figure()
plt.plot(x3, y3, "o", xx3, z3, "-")
plt.legend(["Data", "Line of Best Fit"], loc="best")
plt.title("Least Square Fit of a Straight Line for Data Set C")
plt.xlabel("$X_3$")
plt.ylabel("$Y_3$")
fig.savefig("figure3.png")

plt.show()

