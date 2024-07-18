import numpy as np
# https://en.wikipedia.org/wiki/Confusion_matrix
# https://de.wikipedia.org/wiki/Beurteilung_eines_bin%C3%A4ren_Klassifikators#Wahrheitsmatrix:_Richtige_und_falsche_Klassifikationen


def confusion_matrix(truth, results, number_classes: int = 2):
    # TODO: Erstelle die Confusion Matrix als 2x2 numpy array
    # HINWEIS: np.zeros könnte nützlich sein
    # der Eintrag [0, 0] entspricht der Zahl der Beispiele,
    # die keine Bananen sind und auch als Nicht-Banane erkannt wurden
    # der Eintrag [0, 1] entspricht der Zahl der Beispiele,
    # die keine Bananen sind, aber als Banane erkannt wurden
    # der Eintrag [1, 1] entspricht der Zahl der Beispiele,
    # die wirklich Bananen sind und auch als Banane erkannt wurden
    # der Eintrag [1, 0] entspricht der Zahl der Beispiele,
    # die wirklich Bananen sind, aber als Nicht-Banane erkannt wurden
    # NOTE: Confusion Matrices werden nicht in allen Quellen einheitlich definiert.
    # Sie unterscheiden sich dadurch, ob der erste Index die Wahrheit oder das Ergebnis darstellt.
    conf_matrix = np.zeros((number_classes, number_classes))
    
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    # Truth = Wahrheit; Result = Prediction

    for bild in range(len(truth)):
        if truth[bild] == 1 and results[bild] == 1:
            tp += 1
        
        elif truth[bild] == 0 and results[bild] == 0:
            tn += 1
        
        elif truth[bild] == 0 and results[bild] == 1:
            fp += 1
        
        elif truth[bild] == 1 and results[bild] == 0:
            fn += 1
        
        else:
            pass

    conf_matrix[1, 1] = tp
    conf_matrix[0, 0] = tn
    conf_matrix[0, 1] = fp
    conf_matrix[1, 0] = fn

    """
    TN [0, 0]   FP [0, 1]   N
    FN [1, 0]   TP [1, 1]   P

    NP          PP          SUMME: P + N

    True Positive Rate  = TP        /   TP  +   FP        // oder einfach P
    True Negative Rate  = TN        /   TN  +   FN        // oder einfach N
    False Positive Rate = FP        /   FP  +   TN        // oder einfach N
    False Negative Rate = FN        /   FN  +   TP        // oder einfach P
    Accuracy            = TP + TN   /   P   +   N         // also einmal durch alles
    Precsion            = TP        /   FP  +   TP        // oder einfach PP
    """
    
    return conf_matrix


def true_positive_rate(truth, results):
    # NOTE: Die True Positive Rate berechnet, wie viele der Bananenbilder auch als Banane erkannt wurden
    # Sie wird auch Sensitivity / Sensitivität genannt
    conf_matrix = confusion_matrix(truth, results)
    tpr = conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1])
    return tpr


def false_positive_rate(truth, results):
    # TODO: Die False Positive Rate berechnet, wie viele der "Nicht-Bananen" als Bananen klassifiziert wurden
    conf_matrix = confusion_matrix(truth, results)
    fpr = conf_matrix[0, 1] / (conf_matrix[0, 0] + conf_matrix[0, 1])
    return fpr


def true_negative_rate(truth, results):
    # TODO: Die True Negative Rate berechnet, wie viele der Nicht-Bananen korrekt klassifiziert wurden
    # Sie wird auch Specificity / Spezifität genannt
    conf_matrix = confusion_matrix(truth, results)
    tnr = conf_matrix[0, 0] / (conf_matrix[0, 1] + conf_matrix[0, 0])
    return tnr


def false_negative_rate(truth, results):
    # TODO: Die False Negative Rate berechnet, wie viele der Bananen fälschlicherweise nicht als solche erkannt wurden
    conf_matrix = confusion_matrix(truth, results)
    fnr = conf_matrix[1, 0] / (conf_matrix[1, 1] + conf_matrix[1, 0])
    return fnr


def precision(truth, results):
    # TODO: Die Precision oder Präzision berechnet, wie viele der als Bananen erkannten Beispiele wirklich Bananen waren
    conf_matrix = confusion_matrix(truth, results)
    prec = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[0, 1])
    return prec


def auswerten(truth, results):
    truth = np.array(truth)
    results = np.array(results)
    assert(truth.shape[0] == results.shape[0])

    conf_matrix = confusion_matrix(truth, results)
    print("Confusion Matrix:")
    print(conf_matrix)

    try:
        tpr = true_positive_rate(truth, results)
        print("True positive rate ", tpr)
    except TypeError:
        print("true_positive_rate() fehlgeschlagen. Ist confusion_matrix noch nicht richtig implementiert?")
    fpr = false_positive_rate(truth, results)
    print("False positive rate ", fpr)
    tnr = true_negative_rate(truth, results)
    print("True negative rate ", tnr)
    fnr = false_negative_rate(truth, results)
    print("False negative rate ", fnr)
    prec = precision(truth, results)
    print("Precision ", prec)
