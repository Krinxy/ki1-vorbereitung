import os
import main as src
import numpy as np
import helper_functions as hlp
import pandas as pd

# test if executing main.py file results in errors


def test_execution():
    ret = os.system('python3 main.py')
    exitcode = os.WEXITSTATUS(ret)
    print(exitcode)
    assert (exitcode == 0)


def test_quadratic_model():
    assert (abs(src.quadratic_model(0.0, 1, 1, 3.21) - 3.21) < 0.0001)


def test_quadratic_model2():
    assert (abs(src.quadratic_model(1.0, 1, 1, 3.21) - 5.21) < 0.0001)


def test_error_lin0():
    x = [0.0, 1.0]
    y = [0.2, 1.2]
    error = hlp.compute_error_of_model(x, y, src.linear_model, np.array([1.0, 0.2]))
    assert (abs(error - 0.0) < 0.0001)


def test_error_lin2():
    x = src.x
    y = src.y
    error = hlp.compute_error_of_model(x, y, src.linear_model, np.array([1.0, 0.2]))
    assert (abs(error - 1.25) < 0.0001)


def test_error_quad0():
    data = pd.read_csv("data.csv")
    x = data["x"]
    y = data["y"]
    error = hlp.compute_error_of_model(x, y, src.quadratic_model, np.array([1.0, 0.0, 0.1]))
    assert (abs(error - 0.01) < 0.0001)


def test_error_quad2():
    data = pd.read_csv("data.csv")
    x = data["x"]
    y = data["y"]
    error = hlp.compute_error_of_model(x, y, src.quadratic_model, np.array([2.0, -1.0, -0.1]))
    assert (abs(error - 1.83) < 0.0001)
