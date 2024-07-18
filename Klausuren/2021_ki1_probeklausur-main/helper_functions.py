import numpy as np
import pandas as pd
import zipfile
import matplotlib.pyplot as plt


def generate_data():
    # see https://www.netzfrequenz.info/allgemein/die-waschmaschine-und-der-stromverbrauch.html/attachment/emoncms
    # for power cycle of washing machine
    np.random.seed = 123
    data = []

    for i in range(80):
        number = 0.01 + (np.random.random() - 0.5) * 0.02
        data.append(number)

    for i in range(140):
        number = 0.01 + 0.07 + (np.random.random() - 0.5) * 0.1
        data.append(number)

    for i in range(110):
        number = 0.01 + 0.89 + (np.random.random() - 0.5) * 0.2
        data.append(number)

    for i in range(240):
        number = 0.01 + 0.07 + (np.random.random() - 0.5) * 0.1
        data.append(number)

    for i in range(40):
        number = 0.01 + (np.random.random() - 0.5) * 0.02
        data.append(number)

    times = np.arange('2022-01-17T05:30:00', '2022-01-17T10:30:00', dtype='datetime64[10s]')
    return pd.DataFrame(2100.0 * np.array(data), index=times[:len(data)], columns=["Y in Watt"])


def try_plot_data(data: pd.DataFrame):
    try:
        data.plot(kind='line')
        plt.show()
    except Exception:
        pass


def experimental():
    try:
        filename = "beispielabgabe.zip"
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(".")
    except Exception as e:
        print("Failed to unzip")
        print(e)
