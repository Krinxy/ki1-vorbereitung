import os
import machine_learning as ml
import auswertung as aw

labels_tests = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
ergebnisse_tests = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]


def test_confusion_matrix():
    conf_matrix = aw.confusion_matrix(truth=labels_tests, results=ergebnisse_tests)
    print(conf_matrix)
    assert(conf_matrix.shape[0] == 2)
    assert(conf_matrix.shape[1] == 2)


def test_confusion_matrix_values():
    conf_matrix = aw.confusion_matrix(truth=labels_tests, results=ergebnisse_tests)
    print(conf_matrix)
    assert(conf_matrix[0, 0] == 10)
    assert(conf_matrix[0, 1] == 1)
    assert(conf_matrix[1, 0] == 2)
    assert(conf_matrix[1, 1] == 2)


def test_fnr():
    assert(abs(aw.false_negative_rate(labels_tests, ergebnisse_tests) - 0.5) < 0.001)


def test_fpr():
    assert(abs(aw.false_positive_rate(labels_tests, ergebnisse_tests) - 0.0909) < 0.001)


def test_tnr():
    assert(abs(aw.true_negative_rate(labels_tests, ergebnisse_tests) - 0.909) < 0.001)


def test_prec():
    assert(abs(aw.precision(labels_tests, ergebnisse_tests) - 0.6666) < 0.001)


labels_tests2 = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1]
ergebnisse_tests2 = [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]


def test_confusion_matrix2():
    conf_matrix = aw.confusion_matrix(truth=labels_tests2, results=ergebnisse_tests2)
    print(conf_matrix)
    assert(conf_matrix.shape[0] == 2)
    assert(conf_matrix.shape[1] == 2)


def test_confusion_matrix_values2():
    conf_matrix = aw.confusion_matrix(truth=labels_tests2, results=ergebnisse_tests2)
    print(conf_matrix)
    assert(conf_matrix[0, 0] == 8)
    assert(conf_matrix[0, 1] == 1)
    assert(conf_matrix[1, 0] == 4)
    assert(conf_matrix[1, 1] == 9)


def test_fnr2():
    assert(abs(aw.false_negative_rate(labels_tests2, ergebnisse_tests2) - 0.3077) < 0.001)


def test_fpr2():
    assert(abs(aw.false_positive_rate(labels_tests2, ergebnisse_tests2) - 0.11111111) < 0.001)


def test_tnr2():
    assert(abs(aw.true_negative_rate(labels_tests2, ergebnisse_tests2) - 0.88888888) < 0.001)


def test_prec2():
    assert(abs(aw.precision(labels_tests2, ergebnisse_tests2) - 0.9) < 0.001)
