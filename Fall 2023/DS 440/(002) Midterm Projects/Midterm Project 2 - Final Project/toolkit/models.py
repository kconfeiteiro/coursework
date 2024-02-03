from typing import Sequence

from sklearn.cluster import DBSCAN, KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor


# supervised models
def rfregressor(
    xtrain: Sequence[float | int] = ..., ytrain: Sequence[float | int] = ..., **kwargs
):
    MODEL = RandomForestRegressor(**kwargs)
    MODEL.fit(xtrain, ytrain)
    return MODEL


def dtregressor(
    xtrain: Sequence[float | int] = ..., ytrain: Sequence[float | int] = ..., **kwargs
):
    MODEL = DecisionTreeRegressor(**kwargs)
    MODEL.fit(xtrain, ytrain)
    return MODEL


# unsupervised models
def kmeansclassifier(
    xtrain: Sequence[float | int] = ...,
    n_clusters: int = 3,
    random_state: int = 1,
    **kwargs
):
    MODEL = KMeans(n_clusters=n_clusters, random_state=random_state, **kwargs)
    MODEL.fit(xtrain)
    return MODEL


def db_scan_classifier(
    xtrain: Sequence[float | int] = ..., eps: int = 0.5, min_samples: int = 5, **kwargs
):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples, **kwargs)
    dbscan_labels = dbscan.fit_predict(xtrain)
    return dbscan, dbscan_labels
