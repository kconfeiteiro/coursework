import os
import pandas as pd
import helpers as hp


DATA = pd.read_csv("DATA\\gaia-dr2-allwise-2mass-ppmxl.csv")
os.mkdir("DATA\\BINNED_DATA")
hp.split_large_data(DATA, 8, "DATA\\BINNED_DATA\\gaiaDR2")
