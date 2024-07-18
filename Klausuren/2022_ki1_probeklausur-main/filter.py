import pandas as pd
import numpy as np
from helper_functions import sort_five_numbers


def filter_data(data: pd.DataFrame):
    # Extract the values as numpy array
    values = data.values.ravel()
    wdata = values.copy()
    median = np.zeros_like(wdata)

    for i in range(2, len(values) - 2):
        a = values[i - 2]
        b = values[i - 1]
        c = values[i]
        d = values[i + 1]
        e = values[i + 2]

        print(a, b, c, d, e)

        sort_five_numbers(a, b, c, d, e)
        print(c)
        
        print(median)
    # TODO: Apply the required filter to the values
    # TODO: return the resulting values as numpy array
    # NOTE: Be careful not to overwrite the original data!
    return median

kleineliste = pd.DataFrame([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(filter_data(kleineliste))



def filter_with_edge(data: pd.DataFrame):
    # TODO: copy or extend the function filter_data to treat edges
    # The only requirement is, that the size of the data stays the same as in the inputdata "data" and
    # the values unaffected by the edge are the same as with filter_data(data)
    # You may implement each and any treatment for the values affected by the edge
    pass

liste = [2,321,3,14,235,3,5,3,23,54,5,24,23,52,4,12,5,23,423,5,24,4,23,8,6,57,435,8,8]
print(len(liste))
