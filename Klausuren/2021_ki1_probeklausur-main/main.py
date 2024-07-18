from helper_functions import generate_data, try_plot_data, experimental
from filter import filter_data
from machine_learning import learn

# Read the data file
data = generate_data()
# Try to plot the data
try_plot_data(data=data)

# TODO: apply a filter to the data
filtered = filter_data(data=data)

# TODO: apply machine learning
result = learn(data=data)


# this code is just to test something on all PCs for the actual exam
experimental()
