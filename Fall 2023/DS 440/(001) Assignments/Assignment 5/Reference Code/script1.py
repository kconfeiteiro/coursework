"""
Visualizing DTree in Scikit Learn.
"""

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics, tree
from sklearn.model_selection import train_test_split
from sklearn.tree import *
from sklearn.tree import DecisionTreeClassifier

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

feature_cols = ["pregnant", "insulin", "bmi", "age", "glucose", "bp", "pedigree"]

# load dataset
pima = pd.read_csv("diabetes.csv", header=0, names=col_names)
X = pima[feature_cols]  # Features
y = pima.label  # Target variable
print(pima.head())

#  70% training and 30% test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Visualizing decision tree using scikit-learn
text_representation = tree.export_text(clf)
print(text_representation)

# plotting
fig = plt.figure(figsize=(25, 20))
_ = tree.plot_tree(clf, feature_names=feature_cols, class_names=["0", "1"], filled=True)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# plotting
fig = plt.figure(figsize=(25, 20))
_ = tree.plot_tree(clf, feature_names=feature_cols, class_names=["0", "1"], filled=True)
