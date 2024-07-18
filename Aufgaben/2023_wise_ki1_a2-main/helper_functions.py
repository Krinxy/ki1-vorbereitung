import numpy as np


def evaluate_fits(x, y, linear_model, linear_model_parameters, quadratic_model, quadratic_model_parameters):
    more_x_values = np.arange(0.0, 1.0, 0.01)
    print("Beste Fit-Parameter für lineare Funktion: a (Steigung) = ",
          linear_model_parameters[0], " und b (y-Achsenabschnitt) = ", linear_model_parameters[1])
    absolute_error_linear = compute_error_of_model(x_values=x, y_values=y,
                                                   model_function=linear_model,
                                                   function_parameters=linear_model_parameters)
    print("Fehler des linearen Modells ", absolute_error_linear)
    y_fine_linear = linear_model(more_x_values, *linear_model_parameters)

    print("Beste Fit-Parameter für Parabel: a = ", quadratic_model_parameters[0],
          " b = ", quadratic_model_parameters[1], " c = ", quadratic_model_parameters[2])
    absolute_error_quadratic = compute_error_of_model(x_values=x, y_values=y,
                                                      model_function=quadratic_model,
                                                      function_parameters=quadratic_model_parameters)
    print("Fehler des quadratischen Modells ", absolute_error_quadratic)
    y_fine_quad = quadratic_model(more_x_values, *quadratic_model_parameters)

    return more_x_values, y_fine_linear, y_fine_quad


def compute_error_of_model(x_values: list, y_values: list, model_function: "function", function_parameters: np.ndarray):
    error = 0.0
    for x, y in zip(x_values, y_values):
        error += abs(y - model_function(x, *function_parameters))
    return error


def compute_absolut_error_of_estimate(y_values: list, y_estimates: list):
    error = 0.0
    for y, y_est in zip(y_values, y_estimates):
        error += abs(y - y_est)
    return error
