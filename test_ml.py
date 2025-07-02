import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import (
    train_model,
    inference,
    compute_model_metrics
)
# TODO: implement the first test. Change the function name and input as needed
def test_train_model_type():
    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_inference_output_length():
    X = np.array([[1, 0], [0, 1], [1, 1]])
    y = np.array([0, 1, 0])
    model = train_model(X, y)
    preds = inference(model, X)
    assert preds.shape == y.shape

# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_perfect():
    y_true = np.array([1, 0, 1, 0])
    y_pred = np.array([1, 0, 1, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert precision == 1.0
    assert recall == 1.0
    assert fbeta == 1.0
