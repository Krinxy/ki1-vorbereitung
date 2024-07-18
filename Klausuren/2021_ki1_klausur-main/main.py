from helper_functions import read_data, try_plot_data, dummy_divide
from filter import filter_data
from machine_learning import learn

# Read the data file
data = read_data()
# Try to plot the data
try_plot_data(data=data)

# applies a filter
filtered = filter_data(data=data)

# divide the data into two groups with a simple threshold
# TODO: Find a better threshold according to the assignment description
division_threshold = 0.0
labels = dummy_divide(data=data, threshold=division_threshold)

# applies machine learning
result = learn(data=data)
