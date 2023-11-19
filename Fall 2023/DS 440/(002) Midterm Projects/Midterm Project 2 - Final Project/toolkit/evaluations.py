from typing import Literal, Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from helpers import strmatch, to_txt
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    auc,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
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
