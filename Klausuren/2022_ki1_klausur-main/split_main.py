import numpy as np
from split_train_test import split_data


def get_data():
    # create random data
    number_examples = 1000
    data = np.random.random(number_examples).tolist()
    return data, number_examples


data, number_examples = get_data()

# split the data
ratio = 0.8
train, test = split_data(data, ratio)

print("Anzahl an Beispielen vor split_data", number_examples)
print("Sollanzahl nach split_data", int(np.round(ratio * number_examples)), int(np.round((1.0 - ratio) * number_examples)))
print("Anzahl an Beispielen nach split_data", len(train), "+", len(test), "=", len(train) + len(test))
