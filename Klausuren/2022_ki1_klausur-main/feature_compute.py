import numpy as np


def compute_feature(example: np.ndarray):
    # TODO: IN THE FIRST LINE OF THIS FUNCTION ABOVE THIS:
    # Write a comment to explain your idea for a feature that
    # gives different results for examples of the "I" class and of the "O" class

    size_y = example.shape[0]  # from top to bottom
    size_x = example.shape[1]  # from left to right
    # NOTE: use here as example[y_index][x_index]
    # NOTE: example[y_size - 1][0] is the datapoint bottom left

    # TODO: Implement your feature

    return 0


def good_threshold():
    # TODO: set the threshold such that it differentiates between "I"s and "O"s
    return 99999999999
