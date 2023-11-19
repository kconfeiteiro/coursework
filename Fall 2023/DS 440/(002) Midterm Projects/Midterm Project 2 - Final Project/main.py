"""
Antonio Cascio & Krystian Ojeda Confeiteiro
Dr. Jack
DS 440 - 01DB
Final Project
Created:
Due:
Last Edited: 11/18/2023
"""

import pandas as pd

import toolkit.helpers as hp
from toolkit.models import dtregressor, rfregressor

CONFIG = {
    "data": "DATA\\gaia-dr2-allwise-2mass-ppmxl.csv",
    "binned pth": "DATA\\BINNED_DATA",
    "plots pth": "PLOTS",
    "random forest": {"n_estimators": 100, "random_state": 1},
    "decision tree": {"max_depth": 5, "random_state": 1},
    "features": ["parallax", "phot_g_mean_mag", "phot_rp_mean_mag"],
    "predict": "distance",
}


DATA = pd.read_csv(CONFIG["data"])
DATA1 = DATA[CONFIG["features"]]
# PDATA = hp.prepare_data()
