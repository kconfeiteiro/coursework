from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor


def rfregressor(xtrain, ytrain, **kwargs):
    MODEL = RandomForestRegressor(**kwargs)
    MODEL.fit(xtrain, ytrain)
    return MODEL


def dtregressor(xtrain, ytrain, **kwargs):
    MODEL = DecisionTreeRegressor(**kwargs)
    MODEL.fit(xtrain, ytrain)
    return MODEL
