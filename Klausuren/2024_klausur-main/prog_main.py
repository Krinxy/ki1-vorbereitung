from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

import numpy as np

from prog_given import load_data, train_test_splitting, plot_images, evaluation, additional_preprocessing
from prog_own import normalize_images, conf_matrix2accuracy


# load data mnist dataset
images, labels = load_data()

# plot data if you want
you_want_to_plot = True  # change to False if you don't want to plot

if you_want_to_plot:
    plot_images(images, labels)

# task 27: you have to write the function normalize_images in prog_own.py!
images_normalized = normalize_images(images)

# flatten the images
images_normalized = additional_preprocessing(images_normalized)

# split data into train and test data
images_train, images_test, labels_train, labels_test = train_test_splitting(images_normalized, labels)

# vorschläge für classifier: random forest, mlp, k-means, PCA, decision tree regressor

# create classifier 1
# TODO: YOUR CODE for task 23 - name your classifier classifier1 - fit your classifier with the train data
classifier1 = MLPClassifier().fit(images_train, labels_train) # change here

# TODO: YOUR CODE for task 24 - predict the labels for the test images
labels_pred_clf1 = classifier1.predict(images_test)  # change here

# create classifier 2
# TODO: YOUR CODE for task 23 - name your classifier classifier2 - fit your classifier with the train data
classifier2 = RandomForestClassifier().fit(images_train, labels_train)  # change here

# TODO: YOUR CODE for task 24 - predict the labels for the test images
labels_pred_clf2 = classifier2.predict(images_test)  # change here

print('Auswertung classifier 1:')
confusion_matrix1 = evaluation(labels_pred_clf1, labels_test)
# task 29: you have to write the function conf_matrix2accuracy in prog_own.py!
accuracy1 = conf_matrix2accuracy(confusion_matrix1)
print(f'Selbstberechnete Accuracy: {accuracy1}\n')

print('Auswertung classifier 2:')
confusion_matrix2 = evaluation(labels_pred_clf2, labels_test)
# task 29: you have to write the function conf_matrix2accuracy in prog_own.py!
accuracy2 = conf_matrix2accuracy(confusion_matrix2)
print(f'Selbstberechnete Accuracy: {accuracy2}\n')
