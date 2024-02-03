from typing import Any, Dict, NamedTuple, Sequence, TypedDict


class Evaluations(NamedTuple):
    accuracy: Any = None
    cm: Any = None
    f1: Any = None
    false_positives_rate: Any = None
    mae: Any = None
    mse: Any = None
    precision: Any = None
    r2: Any = None
    recall: Any = None
    rmse: Any = None
    roc_auc: Any = None
    roc_thresohold: Any = None
    true_positives_rate: Any = None
    dictionary: Dict[str, Any] = None
    true_negatives: float = None
    false_positives: float = None
    false_negatives: float = None
    true_positives: float = None


class SplitData(NamedTuple):
    X_train: Sequence[int | float] = None
    X_test: Sequence[int | float] = None
    y_train: Sequence[int | float] = None
    y_test: Sequence[int | float] = None
    X: Sequence[int | float] = None
    y: Sequence[int | float] = None


class DTROptimizierParams(TypedDict):
    splitter: Sequence[str]
    max_depth: Sequence[int]
    min_samples_leaf: Sequence[int]
    min_weight_fraction_leaf: Sequence[int]
    max_features: Sequence[str]
    max_leaf_nodes: Sequence[int | None]
