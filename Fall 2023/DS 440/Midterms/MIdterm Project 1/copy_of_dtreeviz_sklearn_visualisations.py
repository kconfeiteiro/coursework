import os
import sys

import dtreeviz
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

random_state = 1234  # get reproducible trees
dataset_url = (
    "https://raw.githubusercontent.com/parrt/dtreeviz/master/data/titanic/titanic.csv"
)

dataset = pd.read_csv(dataset_url)
dataset.fillna({"Age": dataset.Age.mean()}, inplace=True)

# Encode categorical variables
dataset["Sex_label"] = dataset.Sex.astype("category").cat.codes
dataset["Cabin_label"] = dataset.Cabin.astype("category").cat.codes
dataset["Embarked_label"] = dataset.Embarked.astype("category").cat.codes

features = ["Pclass", "Age", "Fare", "Sex_label", "Cabin_label", "Embarked_label"]
target = "Survived"

tree_classifier = DecisionTreeClassifier(max_depth=3, random_state=random_state)
tree_classifier.fit(dataset[features].values, dataset[target].values)

viz_model = dtreeviz.model(
    tree_classifier,
    X_train=dataset[features],
    y_train=dataset[target],
    feature_names=features,
    target_name=target,
    class_names=["perish", "survive"],
)

viz_model.view(scale=0.8)
viz_model.view(orientation="LR")
viz_model.view(fancy=False)

"""Another way to reduce the visualization size is to specify the tree depths of interest:"""
viz_model.view(depth_range_to_display=(1, 2))  # root is level 0
x = dataset[features].iloc[10]

"""and then display the path through the tree structure:"""
viz_model.view(x=x)
viz_model.view(x=x, show_just_path=True)
viz_model.instance_feature_importance(x, figsize=(3.5, 2))
print(viz_model.explain_prediction_path(x))

# Leaf info - There are a number of functions to get information about the leaves of the tree.

viz_model.leaf_sizes(figsize=(3.5, 2))
viz_model.ctree_leaf_distributions(figsize=(3.5, 2))
viz_model.node_stats(node_id=6)
viz_model.leaf_purity(figsize=(3.5, 2))

"""## Classification

To visualize how it decision tree partitions a single feature, let's train a shallow decision tree classifier using the toy Iris data.
"""

from sklearn.datasets import load_iris

iris = load_iris()
features = list(iris.feature_names)
class_names = iris.target_names
X = iris.data
y = iris.target

dtc_iris = DecisionTreeClassifier(max_depth=2, min_samples_leaf=1, random_state=666)
dtc_iris.fit(X, y)

viz_model = dtreeviz.model(
    dtc_iris,
    X_train=X,
    y_train=y,
    feature_names=features,
    target_name="iris",
    class_names=class_names,
)

"""The following diagram indicates that the decision tree splits the petal width feature into three mostly-pure regions (using `random_state` above to get the same tree each time):"""

viz_model.ctree_feature_space(
    show={"splits", "title"}, features=["petal width (cm)"], figsize=(5, 1)
)

viz_model.ctree_feature_space(
    nbins=40,
    gtype="barstacked",
    show={"splits", "title"},
    features=["petal width (cm)"],
    figsize=(5, 1.5),
)

"""A deeper tree gives this finer grand partitioning of the single feature space:"""

viz_model.ctree_feature_space(
    show={"splits", "title"}, features=["petal width (cm)"], figsize=(5, 1)
)

"""Let's look at how a decision tree partitions two-dimensional feature space."""

viz_model.ctree_feature_space(
    show={"splits", "title"}, features=["petal length (cm)", "petal width (cm)"]
)
