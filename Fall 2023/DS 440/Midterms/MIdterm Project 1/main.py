import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
)


def eval_dtc(
    X_train,
    y_train,
    X_test,
    y_test,
    feature_names,
    class_names=["0", "1"],
    criterion="entropy",
    random_state=1,
    save_as=None,
):
    # instantiate & fit model
    MODEL = DecisionTreeClassifier(random_state=random_state, criterion=criterion)
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

    # create decision tree layer outline
    fig = tree.plot_tree(
        MODEL, feature_names=feature_names, class_names=class_names, filled=True
    )

    if save_as:
        fig.savefig(save_as)

    return training_acc, testing_acc, txt_repr, fig
