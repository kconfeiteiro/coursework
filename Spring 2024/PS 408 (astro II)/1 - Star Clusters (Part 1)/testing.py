import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE = os.path.join("DATA", "asu1.tsv")

DATA = pd.read_csv(FILE, delim_whitespace=True, comment="#", skip_blank_lines=True)
DATA = DATA.iloc[2:, :]
DATA = DATA.reset_index()
DATA.drop(columns=["index"])
toplot = (DATA["Vmag"], DATA["B-V"])

fig, axes = plt.subplots()
axes.scatter(*toplot[::-1], s=5)
axes.set_xlabel('SHIT - X')
axes.set_ylabel("SHIT - Y")
axes.set_title('SHIT TITLE')
plt.show()
