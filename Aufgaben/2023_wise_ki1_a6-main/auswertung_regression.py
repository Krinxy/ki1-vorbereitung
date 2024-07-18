import numpy as np


def mean_absolute_error(truth, results):
    error = abs(truth - results)
    return sum(error) / error.shape[0]


def mean_squared_error(truth, results):
    error = abs(truth - results)
    return sum(np.square(error)) / error.shape[0]


def maximum_error(truth, results):
    error = abs(truth - results)
    return np.max(error)


def auswerten_regression(truth, results):
    mae = mean_absolute_error(truth, results)
    print("Mean absolut error", mae)
    mse = mean_squared_error(truth, results)
    print("Mean squared error", mse)
    maxe = maximum_error(truth, results)
    print("Maximum error", maxe)
