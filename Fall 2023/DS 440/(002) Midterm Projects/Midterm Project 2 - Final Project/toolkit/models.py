from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor


def rfregressor(xtrain, ytrain, n_esitmators=100, random_state=1, **kwargs):
    MODEL = RandomForestRegressor(
        n_estimators=n_esitmators, random_state=random_state, **kwargs
    )
    MODEL.fit(xtrain, ytrain)
    return MODEL


def dtregressor(xtrain, ytrain, max_depth=5, **kwargs):
    MODEL = DecisionTreeRegressor(max_depth=max_depth, **kwargs)
    MODEL.fit(xtrain, ytrain)
    return MODEL
