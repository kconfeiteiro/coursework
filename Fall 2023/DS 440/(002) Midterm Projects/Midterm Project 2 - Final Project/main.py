"""
Antonio Cascio & Krystian Ojeda Confeiteiro
Dr. Jack
DS 440 - 01DB
Final Project
Created:
Due:
Last Edited: 11/21/2023
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import toolkit.helpers as hp
from toolkit.models import dtregressor, rfregressor

CONFIG = {
    "data": "DATA\\School_Attendance_by_Student_Group_and_District__2021-2022.txt",
    "plots pth": "PLOTS",
    "test size": 0.2,
    "random forest": {"n_estimators": 100, "random_state": 1},
    "decision tree": {"max_depth": 5, "random_state": 1},
    "features": [
        "District name",
        "Student group",
        "Category",
        "2021-2022 student count - year to date",
        "2020-2021 student count",
        "2019-2020 student count",
    ],
    "prediction options": {
        "A": "2021-2022 attendance rate - year to date",
        "B": "2020-2021 attendance rate",
        "C": "2019-2020 attendance rate",
    },
}


DATA = pd.read_csv(CONFIG["data"])
features = DATA[CONFIG["features"]]
to_predict = DATA[CONFIG["prediction options"]["A"]]


features = features.replace(
    {  # TODO - automate this (in a function)
        "Category": hp.replacements(features["Category"].unique()),
        "District name": hp.replacements(features["District name"].unique()),
        "Student group": hp.replacements(features["Student group"].unique()),
    }
)
features = features.fillna(0.0)
features = features.astype(np.float64)

to_predict = to_predict.apply(lambda x: x.strip("%"))
to_predict = to_predict.astype(np.float64)

pdata = hp.prepare_data(X=features, y=to_predict, test_size=CONFIG["test size"])

DTR = dtregressor(xtrain=pdata.X_train, ytrain=pdata.y_train, **CONFIG["decision tree"])
y_pred_train_DTR = DTR.predict(pdata.X_train)
y_pred_test_DTR = DTR.predict(pdata.X_test)
print("Test R^2 value (DTR): ", DTR.score(pdata.X_test, y_pred_test_DTR))
print("Train R^2 value (DTR): ", DTR.score(pdata.X_train, y_pred_train_DTR))

RFR = rfregressor(xtrain=pdata.X_train, ytrain=pdata.y_train, **CONFIG["random forest"])
y_pred_train_RFR = RFR.predict(pdata.X_train)
y_pred_test_RFR = RFR.predict(pdata.X_test)
print("Test R^2 value (RFR): ", RFR.score(pdata.X_test, y_pred_test_RFR))
print("Train R^2 value (RFR): ", RFR.score(pdata.X_train, y_pred_train_RFR))
