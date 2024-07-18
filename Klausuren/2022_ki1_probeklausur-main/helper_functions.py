import numpy as np
import pandas as pd
import zipfile
import matplotlib.pyplot as plt


def read_data():
    filename = "data.zip"
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(".")

    data = pd.read_csv("data.csv", header=None)
    times = np.array([i * 1.0/44100 for i in range(len(data.values[:, 0]))]).astype(np.float32)
    data.index = times
    return data


def try_plot_data(data: pd.DataFrame):
    try:
        data.plot(kind='line', legend=None)
        plt.xlabel("Time in s")
        plt.ylabel("Amplitude in arbitrary units")
        plt.show()
    except Exception:
        pass


def sort_five_numbers(a: float, b: float, c: float, d: float, e: float):
    return sort_five_numbers_list([a, b, c, d, e])


def sort_five_numbers_list(numbers: list):
    return sorted(numbers)


def dummy_divide(data: pd.DataFrame, threshold: float):
    values = data.values.ravel()
    labels = np.zeros(values.shape)
    for i in range(len(values)):
        if abs(values[i]) > threshold:
            labels[i] = 1.0
    return labels
