import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import helpers as hp

CONFIG = {
    "datapth": "DATA\\cw8_data.txt",
    "read kwargs": {"delim_whitespace": True, "comment": "#"},
}


DATA = hp.read_data(CONFIG.get("datapth"), **CONFIG.get("read kwargs"))
YEAR, MEN, WOMEN = hp.split_df(DATA)

fig, axes = plt.subplots()
axes.plot(YEAR, MEN, "o-", label="Men")
axes.plot(YEAR, WOMEN, "d-", label="Women")
axes.set_title("Median Age At First Marrige In U.S. (1890 - 2020)")
axes.set_xlabel("Year")
axes.set_ylabel("Age")
axes.legend()
fig.savefig("fig1.pdf")
plt.show()
