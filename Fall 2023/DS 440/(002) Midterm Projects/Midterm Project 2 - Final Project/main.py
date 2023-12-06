"""
Antonio Cascio & Krystian Ojeda Confeiteiro
Dr. Jack
DS 440 - 01DB
Final Project
Created: 11/18/2023
Due: 12/13/2023
Last Edited: 12/05/2023
"""

import numpy as np
import pandas as pd

import toolkit.helpers as hp
from toolkit.evaluations import TSNEeval
from toolkit.models import dtregressor, rfregressor

CONFIG = {
    "paths": {
        "data": "DATA\School_Attendance_by_Student_Group_and_District__2021-2022.txt",
        "plots pth": "PLOTS",
        "visualizations": "DATAVIZ",
    },
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

# read and save correlation plots for data visuzliation
DATA = pd.read_csv(CONFIG["paths"]["data"])
features = DATA[CONFIG["features"]]
to_predict = DATA[CONFIG["prediction options"]["A"]]
to_predict_2 = DATA[CONFIG["prediction options"]["B"]]

# replace all alphanumerical values
features = features.replace(
    {
        "Category": hp.replacements(features["Category"].unique()),
        "District name": hp.replacements(features["District name"].unique()),
        "Student group": hp.replacements(features["Student group"].unique()),
    }
)
features = features.fillna(0.0)
features = features.astype(np.float64)

to_predict = to_predict.apply(lambda x: x.strip("%"))
to_predict = to_predict.astype(np.float64)

SDATA = hp.prepare_data(X=features, y=to_predict, test_size=CONFIG["test size"])

# decision tree regressor
DTR = dtregressor(xtrain=SDATA.X_train, ytrain=SDATA.y_train, **CONFIG["decision tree"])
y_pred_train_DTR = DTR.predict(SDATA.X_train)
y_pred_test_DTR = DTR.predict(SDATA.X_test)

# DTR visualiztion
hp.regression_tree_viz(
    model=DTR,
    feature_names=CONFIG["features"],
    figtitle="Decision Tree Visualization",
)

RFR = rfregressor(xtrain=SDATA.X_train, ytrain=SDATA.y_train, **CONFIG["random forest"])
y_pred_train_RFR = RFR.predict(SDATA.X_train)
y_pred_test_RFR = RFR.predict(SDATA.X_test)

print("Test R^2 value (DTR): ", DTR.score(SDATA.X_test, y_pred_test_DTR))
print("Train R^2 value (DTR): ", DTR.score(SDATA.X_train, y_pred_train_DTR))
print("Test R^2 value (RFR): ", RFR.score(SDATA.X_test, y_pred_test_RFR))
print("Train R^2 value (RFR): ", RFR.score(SDATA.X_train, y_pred_train_RFR))

X_test, X_train = SDATA.X_test, SDATA.X_train
y_test, y_train = SDATA.y_test, SDATA.y_train

# t-sne configurations
TSNE_CFG = {
    "tsne": {
        "n_components": 2,
        "lrate": "auto",
        "init": "random",
        "perplexity": 5,
        "X_data": features,
    },
    "scatter_cfg": {"c": list(to_predict.values), "s": 8},
    "plt_cfg": {"nrows": 1, "ncols": 1},
    "img_cfg": {"cmap": "jet", "interpolation": "none"},
}

TSNE = TSNEeval(**TSNE_CFG["tsne"])
TSNE.initialize(fit_transform=True)
TSNE.visualize(
    figtitle="t-SNE Evaluations (w/ 'fit transform')",
    plt_cfg=TSNE_CFG["plt_cfg"],
    scatter_cfg=TSNE_CFG["scatter_cfg"],
)
