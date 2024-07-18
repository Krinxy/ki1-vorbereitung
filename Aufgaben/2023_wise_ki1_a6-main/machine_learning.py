from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import os
import pickle
from featureberechnung import features_von_bild, featureberechnung_alle_bilder


def alle_bilder_in_verzeichnis(pfad: str):
    bilder_mit_pfad = []
    bilder = os.listdir(pfad)
    for file in bilder:
        bilder_mit_pfad.append(pfad + "/" + str(file))
    return bilder_mit_pfad


def neuronales_netz_trainieren(features: np.array, labels: np.array, hidden_layers=(10,), epochen=100):
    verbose = True
    tolerance = 0.00001
    model = MLPClassifier(verbose=verbose, tol=tolerance, hidden_layer_sizes=hidden_layers, max_iter=epochen)
    model.fit(features, labels)
    return model


def ergebnisse_und_labels_speichern(ergebnisse, labels):
    with open('ergebnisse.pkl', 'wb') as f:
        pickle.dump(ergebnisse, f)
    with open('labels.pkl', 'wb') as f:
        pickle.dump(labels, f)


def ergebnisse_und_labels_laden():
    with open('ergebnisse.pkl', 'rb') as f:
        ergebnisse = pickle.load(f)
    with open('labels.pkl', 'rb') as f:
        labels = pickle.load(f)
    return ergebnisse, labels


def model_anwenden(model, features):
    # TODO: Anwenden des Models auf Features um Klasse zu erhalten

    # Ganz wichtig; Funktion von .predict
    # gewähltes Modell mit ihren features werden predicted
    return model.predict(features)


def ki_pipeline():
    np.random.seed = 123
    apfelbilder = alle_bilder_in_verzeichnis("./beispieldaten/nicht_banane")
    bananenbilder = alle_bilder_in_verzeichnis("./beispieldaten/banane")
    alle_bilder = apfelbilder + bananenbilder
    # Berechnen der features
    alle_features, alle_labels = featureberechnung_alle_bilder(apfelbilder, bananenbilder)
    # normalisierte Features
    normalisierte_features = StandardScaler().fit_transform(alle_features)
    # Trainieren des ML Modells
    model = neuronales_netz_trainieren(features=normalisierte_features, labels=alle_labels, epochen=1000)
    # Anwenden des Models auf Features um Klasse zu erhalten
    ergebnisse = model_anwenden(model, normalisierte_features)

    ergebnisse_und_labels_speichern(ergebnisse, alle_labels)
    return ergebnisse, alle_labels
