"""
Visualizing `RegrTree` in `DTreeViz`.
"""

import dtreeviz
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import *

dataset_url = "https://raw.githubusercontent.com/parrt/dtreeviz/master/data/cars.csv"
df_cars = pd.read_csv(dataset_url)
df_cars.head()

X = df_cars.drop("MPG", axis=1)
y = df_cars["MPG"]
features = list(X.columns)

# 80% training and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# call DTR
dtr_cars = DecisionTreeRegressor(max_depth=4, criterion="absolute_error")
dtr_cars.fit(X_train, y_train)
print(dtr_cars.score(X_test, y_test))

sklearn.metrics.r2_score(dtr_cars.predict(X), y)

viz_rmodel = dtreeviz.model(dtr_cars, X, y, feature_names=features, target_name="MPG")
viz_rmodel.view(scale=1.0, fontname="monospace")
