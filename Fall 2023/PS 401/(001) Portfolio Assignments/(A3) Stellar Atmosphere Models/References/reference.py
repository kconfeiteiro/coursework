import matplotlib.pyplot as plt
import numpy as np

file = "kurucz6000logg0.txt"

# read in file into star1 array, skip first 11 rows
star1 = np.loadtxt(file, skiprows=11)

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(star1[:, 0], star1[:, 1])
