import pandas as pd
import numpy as np
from helper_functions import sort_five_numbers

def filter_data(data):
    # Extract the values as numpy array
    # values = data.ravel()
    data = np.array(data)
    median= []
    for array in range(data):
        wdata = data[array].copy()

        for i in range(2, len(data) - 2):
            a = wdata[i - 2]
            b = wdata[i - 1]
            c = wdata[i]
            d = wdata[i + 1]
            e = wdata[i + 2]

            mask = np.abs(a + b + c + d + e)
            sort_five_numbers(a, b, c, d, e)

            median.append(c)
            i =+ 1

    # median = np.array(median)
    print(median)
    # TODO: Apply the required filter to the values
    # TODO: return the resulting values as numpy array
    # NOTE: Be careful not to overwrite the original data!
    return median

filter_data(np.array([2,3,4,5,6,6,7,8,9,9,4,6,4,3],
            [4,3,2,12,3,4,5,3,2,3,4,5],
            [2,3,4,2,9]))


def filter_with_edge(data: pd.DataFrame):
    # TODO: copy or extend the function filter_data to treat edges
    # The only requirement is, that the size of the data stays the same as in the inputdata "data" and
    # the values unaffected by the edge are the same as with filter_data(data)
    # You may implement each and any treatment for the values affected by the edge
    pass
