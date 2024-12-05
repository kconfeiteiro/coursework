import pandas as pd

data = pd.read_csv("DDO Cepheids - Physical Data.1.txt", sep=r"\s{2,}", engine="python")
data
