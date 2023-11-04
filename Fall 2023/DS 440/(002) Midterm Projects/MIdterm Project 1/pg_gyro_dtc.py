# -*- coding: utf-8 -*-
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

# ignore warnings
warnings.filterwarnings("ignore")

X, y = None, None  # to stop warnings

## Decision Tree Classifier
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=1
)

# Initial Prediction Model
clf = DecisionTreeClassifier(random_state=1)
clf.fit(X_train, y_train)

ypred_train = clf.predict(X_train)
ypred_test = clf.predict(X_test)
train_acc = accuracy_score(y_train, ypred_train)
test_acc = accuracy_score(y_test, ypred_test)

print("Training accuracy:", train_acc)
print("Testing accuracy:", test_acc)

# Information on DTC
print("Tree depth:", clf.get_depth())
print("Number of leaves:", clf.get_n_leaves())


t_n, f_p, f_n, t_p = confusion_matrix(y_test, ypred_test).ravel()
conf_mat = confusion_matrix(y_test, ypred_test, labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=conf_mat, display_labels=clf.classes_)
disp.plot()
plt.show()

# Confusion Matrix and Classification Report
print(
    f"""
True positive: {t_p}
False positive: {f_p}
True negative: {t_n}
False Negative: {f_n}
"""
)
