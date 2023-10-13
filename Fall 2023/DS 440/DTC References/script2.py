"""
Visualizing `DTree` in `dtreeviz`.
"""

import os
import sys

import dtreeviz
import matplotlib as plt
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import *

# col names
col_names = [
    "pregnant",
    "glucose",
    "bp",
    "skin",
    "insulin",
    "bmi",
    "pedigree",
    "age",
    "label",
]


# load dataset
feature_cols = ["pregnant", "insulin", "bmi", "age", "glucose", "bp", "pedigree"]
pima = pd.read_csv("diabetes.csv", header=0, names=col_names)
X = pima[feature_cols]  # Features
y = pima.label  # Target variable
print(pima.head())

# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", sklearn.metrics.accuracy_score(y_test, y_pred))

cm = sklearn.metrics.confusion_matrix(y_test, y_pred, labels=clf.classes_)
disp = sklearn.metrics.ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=clf.classes_
)
disp.plot()

fig = sklearn.metrics.ConfusionMatrixDisplay.from_estimator(
    clf, X_test, y_test, display_labels=clf.classes_, cmap=plt.cm.Blues, normalize="all"
)
fig.ax_.set_title("Normalized over all samples")

fig = sklearn.metrics.ConfusionMatrixDisplay.from_estimator(
    clf,
    X_test,
    y_test,
    display_labels=clf.classes_,
    cmap=plt.cm.Blues,
    normalize="true",
)
fig.ax_.set_title("Normalized over true samples")


viz_model = dtreeviz.model(
    clf, X_train, y_train, feature_names=feature_cols, target_name="label"
)
viz_model.view(scale=1.0, fontname="monospace")
viz_model.view(fancy=False, scale=1.0, fontname="monospace")
x = pima.iloc[10][feature_cols]  # Features
y = pima.label.iloc[10]  # Target variable

viz_model.view(x=x, fontname="monospace")
viz_model.view(x=x, fancy=False, fontname="monospace")
print(viz_model.explain_prediction_path(x))

viz_model.instance_feature_importance(x, fontname="monospace", figsize=(3.5, 2))
viz_model.node_stats(node_id=0)
viz_model.ctree_leaf_distributions(figsize=(3.5, 2), fontname="monospace")
