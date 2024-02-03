from datetime import datetime
from typing import Callable, Literal, Sequence

import numpy as np
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV, KFold, cross_val_score

from toolkit import DTROptimizierParams


# decision tree regressor optimzier
def cross_validation_score(dt, X_train, y_train):
    cv_scores = cross_val_score(dt, X_train, y_train, cv=5)
    mean_cv_score = np.mean(cv_scores)
    return mean_cv_score


def adabooster(
    decisiontree, Xvals, yvals, n_estimators: int = 300, random_state: int = 1, **kwargs
):
    MODEL = AdaBoostRegressor(
        decisiontree, n_estimators=n_estimators, random_state=random_state, **kwargs
    )
    MODEL.fit(Xvals, yvals)
    return


def gridsearchvc_optimizer(
    regressor: Callable = ...,
    xvals: Sequence[int | float] = ...,
    yvals: Sequence[int | float] = ...,
    cfg_params: DTROptimizierParams = {
        "splitter": ["best", "random"],
        "max_depth": [1, 3, 5, 7, 9, 11, 12],
        "min_samples_leaf": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "min_weight_fraction_leaf": np.linspace(0.0, 0.5, 9),
        "max_features": [25, "log2", "sqrt", 10],
        "max_leaf_nodes": [None, 10, 20, 30, 40, 50, 60, 70, 80, 90],
    },
    scoring: Literal["neg_mean_squared_error"] = "neg_mean_squared_error",
    cv: int = 3,
    verbose: int = 3,
    time_execution: bool = False,
    **kwargs
):
    if time_execution:
        start = datetime.now()

    tuning_model = GridSearchCV(
        estimator=regressor,
        param_grid=cfg_params,
        scoring=scoring,
        cv=cv,
        verbose=verbose,
        **kwargs,
    )

    tuning_model.fit(xvals, yvals)

    if time_execution:
        end = start - datetime.now()
        return tuning_model, end
    else:
        return tuning_model


# random forest regressor optimzier



# k-means classifier optmizier


# dbscan classifier optimizier
