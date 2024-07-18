import numpy as np


def generateI():
    size_x = 11
    size_y = 11
    x_start = np.random.rand() * 0.85
    x_end = x_start + 0.05 + np.random.rand() * 0.1
    y_start = np.random.rand() * 0.2
    y_end = y_start + 0.5 + np.random.rand() * 0.3

    x_start_bin = int(np.round(x_start * size_x))
    x_end_bin = int(np.round(x_end * size_x))
    y_start_bin = int(np.round(y_start * size_y))
    y_end_bin = int(np.round(y_end * size_y))

    assert(x_end_bin - x_start_bin) <= 2

    data = np.zeros((size_x, size_y))
    for i in range(size_x):
        if i >= x_start_bin and i <= x_end_bin:
            for j in range(size_y):
                if j >= y_start_bin and j <= y_end_bin:
                    data[i][j] = 255

    return data.T.astype(int)


def generateO():
    size_x = 11
    size_y = 11
    x_start = 0.05 + np.random.rand() * 0.6
    x_end = x_start + 0.2 + np.random.rand() * 0.2
    y_start = 0.05 + np.random.rand() * 0.35
    y_end = y_start + 0.3 + np.random.rand() * 0.4

    x_start_bin = int(np.round(x_start * size_x))
    x_end_bin = int(np.round(x_end * size_x))
    y_start_bin = int(np.round(y_start * size_y))
    y_end_bin = int(np.round(y_end * size_y))

    assert(x_end_bin - x_start_bin) >= 2

    data = np.zeros((size_x, size_y))
    for i in range(size_x):
        if i == x_start_bin or i == x_end_bin:
            for j in range(size_y):
                if j >= y_start_bin and j <= y_end_bin:
                    data[i][j] = 255
        if i > x_start_bin and i < x_end_bin:
            for j in range(size_y):
                if j == y_start_bin or j == y_end_bin:
                    data[i][j] = 255

    return data.T.astype(int)


# def generate_random(number_examples: int = 100):
#     examples = []
#     for i in range(number_examples):
#         if np.random.rand() > 0.5:
#             examples.append(generateI())
#         else:
#             examples.append(generateO())

#     return examples


def generate_in_order(number_I: int = 50, number_O: int = 50, show: bool = False):
    examples = []
    for i in range(number_I):
        examples.append(generateI())
    for i in range(number_O):
        examples.append(generateO())

    if show:
        for ex in examples:
            print(ex)
            print("")

    return examples
