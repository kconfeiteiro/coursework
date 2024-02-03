"""
Antonio Cascio & Krystian Ojeda Confeiteiro
Dr. Jack
DS 440 - 01DB
Final Project
Created: 11/18/2023
Due: 12/13/2023
Last Edited: 12/08/2023
"""

import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score

import toolkit.helpers as hp
from toolkit.evaluations import TSNEeval, kcrossfoldval
from toolkit.models import (
    dtregressor,
    rfregressor,
    kmeansclassifier,
    db_scan_classifier,
)
from toolkit.optimizers import gridsearchvc_optimizer

CONFIG = {
    "paths": {
        "data": "DATA\School_Attendance_by_Student_Group_and_District__2021-2022.txt",
        "plots pth": "PLOTS",
        "visualizations": "DATAVIZ",
    },
    "test size": 0.2,
    "random forest": {"n_estimators": 100, "random_state": 1},
    "decision tree": {"max_depth": 5, "random_state": 1},
    "DTR optimization params": {
        "max_depth": 5,
        "max_features": "auto",
        "max_leaf_nodes": 40,
        "min_samples_leaf": 2,
        "min_weight_fraction_leaf": 0.1,
        "splitter": "random",
    },
    "features": [
        "District name",
        "Student group",
        "Category",
        "2021-2022 student count - year to date",
        # "2020-2021 student count",
        # "2019-2020 student count",
    ],
    "prediction options": {
        "A": "2021-2022 attendance rate - year to date",
        "B": "2020-2021 attendance rate",
        "C": "2019-2020 attendance rate",
    },
}

# read and save correlation plots for data visuzliation
dframe = pd.read_csv(CONFIG["paths"]["data"])
features = dframe[CONFIG["features"]]
to_predict = dframe[CONFIG["prediction options"]["A"]]

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

X_train, X_test, y_train, y_test = hp.prepare_data(
    X=features,
    y=to_predict,
    test_size=CONFIG["test size"],
    as_named_tuple=False,
)

# decision tree regressor
DTR = dtregressor(xtrain=X_train, ytrain=y_train, **CONFIG["decision tree"])
ypred_train_dtr = DTR.predict(X_train)
ypred_test_dtr = DTR.predict(X_test)

print("\nDecision Tree Regressor")
print("Test R^2 value (DTR): ", DTR.score(X_test, ypred_test_dtr))
print("Train R^2 value (DTR): ", DTR.score(X_train, ypred_train_dtr))

tuned_dtr = gridsearchvc_optimizer(DTR, X_train, y_train)
y_pred_train_dtr_tuned = tuned_dtr.predict(X_test)

print(f"Tuned DTR R^2: ", tuned_dtr.score(X_test, y_pred_train_dtr_tuned))

# k-fold cross-validation
avg_cv_score_dtr = kcrossfoldval(optimal_model=tuned_dtr)
print("Decision Tree Regressor avg cross-val score: ", avg_cv_score_dtr)

RFR = rfregressor(xtrain=X_train, ytrain=y_train, **CONFIG["random forest"])
ypred_train_rfr = RFR.predict(X_train)
ypred_test_rfr = RFR.predict(X_test)

print("\nRandom Forset Regressor")
print("Test R^2 value (RFR): ", RFR.score(X_test, ypred_test_rfr))
print("Train R^2 value (RFR): ", RFR.score(X_train, ypred_train_rfr))

tuned_rfr = gridsearchvc_optimizer(
    regressor=RFR,
    cfg_params={
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    },
)

ypred_test_frf_tuned = tuned_rfr.predict(X_test)
print("\nTuned FRF R^2: ", tuned_rfr.score(X_test, ypred_test_frf_tuned))


# modifying data for classification models
y_train_new = hp.regressor2classifier(y_train)
y_test_new = hp.regressor2classifier(y_test)

# k nearest regressory
KMC = kmeansclassifier(X_train)
ypred_test_KMC = KMC.predict(X_test)

# (last model)
dbscan, dbscan_labels = db_scan_classifier(X_train)
ari_score = adjusted_rand_score(y_train_new, dbscan_labels)

# print results
print("\nK-Means Regressor")
print("Test R^2 value (KMR): ", KMC.score(X_test, ypred_test_rfr))
print("Train R^2 value (KMR): ", KMC.score(X_train, ypred_train_rfr))

print("\nDBSCAN Classifier")
print("Ari-Score: ", ari_score)

exit()

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
