import pandas as pd
import numpy as np


def learn(data: pd.DataFrame):
    # Fixes the seed to encounter less randomness in the results
    np.random.seed = 123
    # Extract the values as numpy array
    values = data.values

    # TODO: Have a look at the documentation provided in the subfolder ./doc
    # TODO: Choose the best algorithm to group the data into three unknown categories encoded as 0, 1 and 2
    # TODO: return the result as one value per data point
    return None
