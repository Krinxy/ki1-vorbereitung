import pandas as pd
import numpy as np
from helper_functions import dummy_divide


def learn(data: pd.DataFrame):
    # Divide the data into two groups
    labels = dummy_divide(data=data, threshold=0.03)
    # Fixes the seed to encounter less randomness in the results
    np.random.seed = 123
    # Extract the values as numpy array
    values = data.values

    # TODO: Have a look at the documentation provided in the subfolder ./doc
    # TODO: Choose the best algorithm from this documentation to learn to group the data
    # into the categories as set by the labels, encoded as 0 and 1
    # TODO: Train and apply the algorithm (on the same data, ignore splitting the data for this assignment)

    # TODO: Return the result as one value per data point
    return None
