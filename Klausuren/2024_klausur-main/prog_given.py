# You do not need to modify this file!
# Diese Datei muss und darf nicht geändert werden!

from sklearn import datasets, metrics
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np


def load_data():
    """Load data from mnist dataset."""
    digits = datasets.load_digits()

    # set images and labels
    images = digits.images
    labels = digits.target

    return images, labels


def train_test_splitting(images, labels):
    """Split data into train and test data."""
    images_train, images_test, labels_train, labels_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    return images_train, images_test, labels_train, labels_test


def plot_images(images, labels):
    """Plot the first 10 images and their labels from the given data."""
    _, axes = plt.subplots(nrows=1, ncols=10, figsize=(10, 3))
    for ax, image, label in zip(axes, images, labels):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
        ax.set_title("Train: %i" % label)
    plt.show()


def evaluation(labels_predicted, labels_test):
    """Evaluate the predicted labels with the test labels."""
    if type(labels_predicted) == int:
        print("No input data! You have to solve the tasks first!")
    else:
        # calculate confusion matrix
        confusion_matrix = metrics.confusion_matrix(labels_test, labels_predicted)

        print(confusion_matrix)

        # calculate accuracy
        accuracy = metrics.accuracy_score(labels_test, labels_predicted)

        print(f"Accuracy: {accuracy}")

        return confusion_matrix


def additional_preprocessing(images):
    """Additional preprocessing for the given images."""

    # flatten the images
    images = images.reshape((images.shape[0], -1))

    return images
