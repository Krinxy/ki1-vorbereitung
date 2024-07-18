import numpy as np
import cv2

conf_matrix = np.array([[10, 40],
                        [10, 100]])

"""
Matrix:
TN  FP  N
FN  TP  P
NP  PP
"""

true_positive_rate = conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1])
true_negative_rate = conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1])

false_positive_rate = conf_matrix[0, 1] / (conf_matrix[0, 0] + conf_matrix[0, 1])
false_negative_rate = conf_matrix[1, 0] / (conf_matrix[1, 0] + conf_matrix[1, 1])

precision = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[0, 1])
accuracy = (conf_matrix[0, 0] + conf_matrix[1, 1]) / (conf_matrix[0,0] + conf_matrix[0, 1] + conf_matrix[1, 0] + conf_matrix[1, 1])


print(true_positive_rate)
print(true_negative_rate)

print(false_positive_rate)
print(false_negative_rate)

print(precision)
print(accuracy)
