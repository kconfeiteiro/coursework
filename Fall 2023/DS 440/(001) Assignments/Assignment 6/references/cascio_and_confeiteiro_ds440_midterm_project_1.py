import os
import warnings

import dtreeviz
import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

# ignore warnings & mount Google Drive
warnings.filterwarnings("ignore")
ROOT = os.getcwd()
PLOTS = ROOT + "/figures/"


def fix_data(*data_arr, reshape_size=(1, -1)):
    return (np.array(data).reshape(*reshape_size) for data in data_arr)


def as_np_arr(*data_arrs):
    return (np.array(data) for data in data_arrs)


def replace_vals(
    data,
    column,
    to_replace,
    replace_with,
    cfg={"na": False, "case": False, "regex": True},
):
    data.loc[
        data[column].str.contains(to_replace, **cfg) == True, column
    ] = replace_with


def get_uniques(DATA, columns=None):
    _columns = columns if columns else list(DATA.columns)
    return [DATA[col].unique() for col in _columns]


def decision_tree(
    X_train,
    X_test,
    y_train,
    y_test,
    criterion="entropy",
    random_state=1,
    **kwargs,
):
    # instantiate & fit model
    MODEL = DecisionTreeClassifier(
        random_state=random_state, criterion=criterion, **kwargs
    )
    MODEL.fit(X_train, y_train)

    # get train and test prediction values & their accuracies
    pred_train_y = MODEL.predict(X_train)
    pred_test_y = MODEL.predict(X_test)

    training_acc = accuracy_score(y_train, pred_train_y)
    testing_acc = accuracy_score(y_test, pred_test_y)

    print(f"Training accuracy: {training_acc}")
    print(f"Testing accuracy: {testing_acc}")

    # text representation of decision tree
    txt_repr = tree.export_text(MODEL)

    return training_acc, testing_acc, txt_repr, MODEL, pred_train_y, pred_test_y


# just to stop the red lines
X, y = None, None
X_vals, y_vals, pred_test_y = None, None, None

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# read data
DATA = pd.read_csv(ROOT + "fitness_class_2212.csv")
print("X shape: ", X_vals.shape)
print("y shape: ", y_vals.shape, "\n")

TARGET_1 = DATA, "day_of_week"
REPLACE_1 = {
    "Sun": 0.0,
    "Moneday|Mon": 1.0,
    "Tue": 2.0,
    "Wednesday|Wed": 3.0,
    "Thu": 4.0,
    "Fri|Fri.": 5.0,
    "Sat": 6.0,
}

for key_w, repl in REPLACE_1.items():
    replace_vals(*TARGET_1, key_w, repl)


TARGET_2 = DATA, "category"
REPLACE_2 = {
    "-": 0.0,
    "cycling": 1.0,
    "aqua": 2.0,
    "strength": 3.0,
    "hiit": 4.0,
    "yoga": 5.0,
}

for key_w, repl in REPLACE_2.items():
    replace_vals(*TARGET_2, key_w, repl)

DATA.days_before = DATA.days_before.apply(lambda x: x.replace(" days", ""))
DATA.days_before = DATA.days_before.apply(lambda x: x.strip())
DATA.days_before = DATA.days_before.astype(int)
SHIT = DATA.days_before

TARGET_3 = DATA, "time"
replace_vals(*TARGET_3, "AM", 0)
replace_vals(*TARGET_3, "PM", 1)

FEATURES = DATA.columns.drop("attended")
X_vals, y_vals = DATA[[*FEATURES]], DATA["attended"]
X_vals = X_vals.fillna(0)

DATASETS = train_test_split(
    X_vals, y_vals, test_size=0.2, stratify=y_vals, random_state=1
)
X_train, X_test, y_train, y_test = DATASETS

MODEL_1 = decision_tree(
    *DATASETS,
    FEATURES,
    max_depth=3,
)

training_acc1, testing_acc1, txt_repr1, model1, pred_train_y1, pred_test_y1 = MODEL_1

print(classification_report(y_test, pred_test_y))

viz_1 = dtreeviz.model(
    model1, X_train, y_train, feature_names=FEATURES, target_name="attended"
)

viz_1.view(scale=1.0, fontname="monospace")
viz_1.ctree_leaf_distributions(fontname="monospace")
print(txt_repr1)

model1_viz = tree.export_graphviz(
    model1,
    out_file=None,
    feature_names=X_train.columns,
    class_names=y_train.astype(str),
    filled=True,
    rounded=True,
    special_characters=True,
)
model1_viz_graph = graphviz.Source(model1_viz)
model1_viz_graph

t_n, f_p, f_n, t_p = confusion_matrix(y_test, pred_test_y1).ravel()
conf_mat = confusion_matrix(y_test, pred_test_y1, labels=model1.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=conf_mat, display_labels=model1.classes_)
disp.plot()
plt.show()
