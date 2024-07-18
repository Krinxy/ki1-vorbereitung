import os
import cv2
import main as src
import featureberechnung as feat
import numpy as np


# def test_execution():
#     ret = os.system('python3 main.py')
#     exitcode = os.WEXITSTATUS(ret)
#     print(exitcode)
#     assert(exitcode == 0)

def test_apfel_rot_schnitt():
    assert (abs(src.durchschnitt_apfel[0] - 170.229) < 1.0)


def test_banane_rot_schnitt():
    assert (abs(src.durchschnitt_banane[0] - 154.474) < 1.0)


def test_anzahl_features():
    assert (src.durchschnitt_apfel.shape[0] >= 2)


def test_anzahl_beispiele_apfel():
    assert (len(src.ergebnisse["apfel"]) >= 9)


def test_anzahl_beispiele_banane():
    assert (len(src.ergebnisse["banane"]) >= 4)


def test_anzahl_features2():
    image = cv2.imread("./beispieldaten/apfel/Red_Apple.jpg")
    features = feat.berechne_features(image)
    assert (isinstance(features, np.ndarray))
    assert (features.shape[0] >= 2)


def test_mittlerer_rotwert():
    image = cv2.imread("./beispieldaten/apfel/Red_Apple.jpg")
    rotwert = feat.mittlerer_rotwert(image)
    assert (abs(rotwert - 219.65) < 1.0)


def test_eiegnes_feature():
    image1 = cv2.imread("./beispieldaten/apfel/Red_Apple.jpg")
    image2 = cv2.imread("./beispieldaten/banane/130px-Bananen_Frucht.jpg")
    image3 = cv2.imread("./beispieldaten/apfel/Granny_smith_closeup.jpg")
    feature1 = feat.berechne_features(image1)[0]
    feature2 = feat.berechne_features(image2)[0]
    feature3 = feat.berechne_features(image3)[0]
    assert (feature1 != feature2)
    assert (feature2 != feature3)
    assert (feature1 != feature3)
