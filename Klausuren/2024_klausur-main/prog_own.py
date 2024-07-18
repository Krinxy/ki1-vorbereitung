import numpy as np


def normalize_images(images: np.ndarray):
    """Normalize the given images to values between 0 and 1."""
    # TODO: YOUR CODE for task 26
    images_min = np.min(images)
    images_max = np.max(images)
    images = (images - images_min) / (images_max - images_min)
    return images


def conf_matrix2accuracy(confusion_matrix: np.ndarray):
    """Calculate the accuracy from the given confusion matrix."""
    # TODO: YOUR CODE for task 25
    gesamt = 0
    richtig = 0

    for i in range(confusion_matrix.shape[0]):
        for j in range(confusion_matrix.shape[1]):
            wert = confusion_matrix[i][j]
            gesamt += wert
            if i == j:
                richtig =+ wert

    accuracy = richtig / gesamt

    return accuracy
