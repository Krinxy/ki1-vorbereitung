import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from models import linear_model, quadratic_model
from helper_functions import evaluate_fits


data = pd.read_csv("data.csv")
x = data["x"]
y = data["y"]
plt.plot(x, y, 'bo', label='data')
# NOTE: You can usually close a matplotlib plot by pressing "q"
# For more information, see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# Fit linear model:
linear_model_parameters, _ = curve_fit(linear_model, x, y)
# NOTE: curve_fit returns two values, but we only need the first one here.

# TODO: You have to write the quadratic model function first in models.py!

# TODO: then fit quadratic model here:
quadratic_model_parameters, _ = curve_fit(quadratic_model, x, y)

x_fine, y_fine_linear, y_fine_quad = evaluate_fits(x, y, linear_model, linear_model_parameters,
                                                   quadratic_model, quadratic_model_parameters)

# Plotting the results
plt.plot(x_fine, y_fine_linear, 'r-', label="Linear fit")
plt.plot(x_fine, y_fine_quad, 'b-', label="quadratic fit")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
