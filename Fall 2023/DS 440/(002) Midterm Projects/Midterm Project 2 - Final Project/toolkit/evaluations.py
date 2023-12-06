from typing import Any, Dict, Literal, Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .helpers import strmatch, to_txt
from sklearn.manifold import TSNE
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    auc,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    pairwise_distances,
    precision_score,
    r2_score,
    recall_score,
    roc_curve,
)

from toolkit import Evaluations


class EvaluateModel:
    """
    Returns all evaluation metrics for a given `y_true`, and `y_pred` input set.

    Parameters
    ----------
    y_true : Sequence[int], optional
        True values of predictions, by default None
    y_pred : Sequence[int], optional
        Predicted values from model, by default None

    Returns
    -------
    NamedTuple
        NamedTuple of evelation metrics (see Notes)

    Notes
    ------
    This function returns a NamedTuple with these properties:
        - `accuracy`
        - `cm`
        - `f1`
        - `false_positives_rate`
        - `mae`
        - `mse`
        - `precision`
        - `r2`
        - `recall`
        - `rmse`
        - `roc_auc`
        - `roc_thresohold`
        - `true_positives_rate`

    Example
    -------
    >>> import numpy as np
    >>> from . import evaluate_model
    >>> y_true = np.array([1, 0, 1, 1, 0, 0, 1])
    >>> y_pred = np.array([1, 0, 0, 1, 0, 1, 1])
    >>> MODEL1_evals = EvaluateModel(y_true, y_pred)
    >>> m1_evals = MODEL1_evals.evaluate()
    >>> m1_evals.accuracy
    >>> 87.425
    """

    def __init__(
        self,
        y_true: Sequence[int] = None,
        y_pred: Sequence[int] = None,
    ) -> None:
        self.y_true = y_true
        self.y_pred = y_pred

        self._evals = None
        self._evals_list = None
        self._evals_tuple = None
        self._data = None

    # def __getattribute__(self, __name: str = None) -> Any:
    #     return self._evals[__name]

    def evaluate(
        self,
        average: Literal["micro", "macro", "weighted", "binary"] | None = None,
        zero_division: Literal["warn"] | np.nan = np.nan,
    ) -> Evaluations:
        """
        Method to evaluate the model.

        Parameters
        ----------
        average : Literal, optional
            What you want to scale the averages with, by default None
        zero_division : Literal, optional
            What you want to do with the `ZeroDivisionError`, by default np.nan

        Returns
        -------
        Evaluations
            A `NamedTuple` object of all the model's evaluations.
        """
        roc_vals = lambda y_true, y_pred, pos_label=1: roc_curve(
            y_true, y_pred, pos_label=pos_label
        )
        fpr, tpr, thresholds = roc_vals(self.y_true, self.y_pred)
        self._evals = {
            "accuracy": accuracy_score(self.y_true, self.y_pred),
            "cm": confusion_matrix(self.y_true, self.y_pred),
            "f1": f1_score(self.y_true, self.y_pred, average=average),
            "false_positives_rate": fpr,
            "mae": mean_absolute_error(self.y_true, self.y_pred),
            "mse": mean_squared_error(self.y_true, self.y_pred),
            "precision": precision_score(
                self.y_true, self.y_pred, average=average, zero_division=zero_division
            ),
            "r2": r2_score(self.y_true, self.y_pred),
            "recall": recall_score(
                self.y_true, self.y_pred, average=average, zero_division=zero_division
            ),
            "rmse": np.sqrt(mean_squared_error(self.y_true, self.y_pred)),
            "roc_auc": auc(fpr, tpr),
            "roc_thresohold": thresholds,
            "true_positives_rate": tpr,
        }

        combine = lambda x, y: f"{x}: {y}"
        self._evals_list = list(map(combine, self._evals.keys(), self._evals.values()))
        self._evals_tuple = Evaluations(*self._evals.values(), dictionary=self._evals)

    def cofusion_matrix_eval(self, classes: Sequence[int] = None, save_as: str = None):
        """
        Creates (and saves) a confusion matrix plot.

        Parameters
        ----------
        classes : Sequence[int], optional
            The classes of the model you are evaluating, by default None
        save_as : str, optional
            What you want to save the confusion matrix by, by default None
        """
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()

        with plt.ioff():
            conf_mat = confusion_matrix(self.y_true, self.y_pred, labels=classes)
            disp = ConfusionMatrixDisplay(
                confusion_matrix=conf_mat, display_labels=classes
            )

            disp.plot()
            if save_as:
                disp.figure_.savefig(save_as)

        self._evals.update(
            {
                "true_negatives": tn,
                "false_positives": fp,
                "false_negatives": fn,
                "true_positives": tp,
            }
        )

    def save_evals(
        self,
        save_as: str = None,
        filetype: Literal["CSV", "TEXT", "JSON"] = None,
        **kwargs,
    ) -> None:
        """
        Save evaluations to text file, commma-separated values file, Excel file, or JSON file.

        Parameters
        ----------
        save_as : str, optional
            Name to save file as (must be consistent with `filetype` argument), by default None
        filetype : CSV, TEXT, or JSON, optional
            Desired file type to save evaluations as, by default None

        Raises
        ------
        ValueError
            If file type does not match file extension in `save_as` argument.
        """
        self._data = pd.DataFrame(self._evals, columns=["Metric", "Value"], **kwargs)
        match filetype:
            case "CSV":
                if strmatch(r"\.csv", save_as):
                    self._data.to_csv(save_as)
                elif strmatch(r"\.xls|\.xlsx"):
                    self._data.to_excel(save_as)
                else:
                    _msg = f"Saved file name does not fit availabel options. Received: {save_as}"
                    raise ValueError(_msg)
            case "JSON":
                self._data.to_json(save_as, **kwargs)
            case "TEXT":
                to_txt(save_as, self._evals_list, **kwargs)

    @property
    def evaluations_dict(self):
        return self._evals

    @property
    def data(self):
        return self._data


class TSNEeval:
    def __init__(
        self,
        n_components: int = 2,
        lrate: str = "auto",
        init: str = "random",
        perplexity: int = 5,
        X_data: Sequence[float | int] = None,
        y_data: Sequence[float | int] = None,
    ) -> None:
        self.n_components = n_components
        self.lrate = lrate
        self.init = init
        self.perplexity = perplexity
        self.X_data = X_data
        self.y_data = y_data

        self.tsne = None

    def initialize(
        self,
        fit_transform: bool = False,
        return_data: bool = False,
        **kwargs,
    ) -> None:
        if fit_transform:
            self.tsne = TSNE(
                n_components=self.n_components,
                learning_rate=self.lrate,
                init=self.init,
                perplexity=self.perplexity,
                **kwargs,
            ).fit_transform(self.X_data)
        else:
            self.tsne = TSNE(
                n_components=self.n_components,
                learning_rate=self.lrate,
                init=self.init,
                perplexity=self.perplexity,
                **kwargs,
            )

        self.pathcollection = (self.tsne[:, 0], self.tsne[:, 1])
        if return_data:
            return self.pathcollection

    def visualize(
        self,
        figtitle: str = None,
        xlabel: str = None,
        ylabel: str = None,
        save_as: str = None,
        display: bool = True,
        plt_cfg: Dict = None,
        scatter_cfg: Dict = None,
        return_figure: bool = False,
    ) -> plt.subplots:
        fig, axes = plt.subplots(**plt_cfg)
        axes.scatter(*self.pathcollection, **scatter_cfg)

        if figtitle:
            axes.set_title(figtitle)

        if xlabel:
            axes.set_xlabel(xlabel)

        if ylabel:
            axes.set_ylabel(ylabel)

        if save_as:
            fig.savefig(save_as)

        if display:
            plt.show()

        if return_figure:
            return fig, axes

    def heatplot(
        self,
        model: Any = None,
        plt_cfg: Dict = None,
        img_cfg: Dict = None,
        save_as: str = None,
        display: bool = True,
    ):
        pairwisedist = pairwise_distances(self.X_values, metric="cosine")
        # sorting by labels
        sorted_pairwisedist = pairwisedist[np.argsort(model.labels_)][
            :, np.argsort(model.labels_)
        ]
        labels = model.labels_[np.argsort(model.labels_)]

        # keeping the distance values between 0 and 1
        sorted_pairwisedist = sorted_pairwisedist / np.max(sorted_pairwisedist)
        sorted_similarity = 1 - sorted_pairwisedist / np.max(sorted_pairwisedist)

        fig, axes = plt.subplots(**plt_cfg)
        axes.imshow(sorted_similarity, **img_cfg)

        if save_as:
            fig.savefig(save_as)

        if display:
            plt.show()
