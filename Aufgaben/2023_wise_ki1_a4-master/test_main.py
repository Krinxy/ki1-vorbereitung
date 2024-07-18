import os
import cv2
import numpy as np
from histogram import graubild_zu_liste, histogramm_aus_liste, histogramm_graubild, get_lower_threshold_from_histogram
import schwellwert as sw
from main import guter_oberer_schwellwert, guter_unterer_schwellwert


def _farbbild_zu_liste(image, cchannel: int):
    data = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            data.append(image[i][j][cchannel])
    return data


def _summe_farbe(image, cchannel: int):
    liste = _farbbild_zu_liste(image=image, cchannel=cchannel)
    summe = sum(liste)
    return summe


def test_execution():
    ret = os.system('python3 main.py')
    exitcode = os.WEXITSTATUS(ret)
    print(exitcode)
    assert (exitcode == 0)


def test_main_guter_oberer_schwellwert():
    assert (guter_oberer_schwellwert is not None)
    assert (guter_oberer_schwellwert > 110)
    assert (guter_oberer_schwellwert < 200)


def test_main_guter_unterer_schwellwert():
    assert (guter_unterer_schwellwert is not None)
    assert (guter_unterer_schwellwert > 10)
    assert (guter_unterer_schwellwert < 50)


def test_lower_threshold1():
    img = cv2.imread('bilder/a_bar_somewhere.jpg')
    graubild = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = sw.unterer_schwellwert(grauwert_bild=graubild, schwellwert=150)
    assert (sum(graubild_zu_liste(image=image)) == 11152389)


def test_lower_threshold2():
    img = cv2.imread('bilder/a_bar_somewhere.jpg')
    graubild = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = sw.unterer_schwellwert(grauwert_bild=graubild, schwellwert=105)
    assert (sum(graubild_zu_liste(image=image)) == 18023200)


def test_upper_threshold1():
    img = cv2.imread('bilder/a_bar_somewhere.jpg')
    graubild = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = sw.oberer_schwellwert(grauwert_bild=graubild, schwellwert=150)
    assert (sum(graubild_zu_liste(image=image)) == 28285082)


def test_upper_threshold2():
    img = cv2.imread('bilder/a_bar_somewhere.jpg')
    graubild = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = sw.oberer_schwellwert(grauwert_bild=graubild, schwellwert=105)
    assert (sum(graubild_zu_liste(image=image)) == 35182846)


def test_graubild_zu_liste():
    img = cv2.imread('bilder/a_bar_somewhere.jpg')
    graubild = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    assert (sum(graubild_zu_liste(image=graubild)) == 25782731)


def test_histogramm_aus_liste_random():
    test_liste = list(np.random.randint(low=0, high=255, size=4000))
    hist = histogramm_aus_liste(test_liste)
    for i in hist:
        matches = 0
        for j in test_liste:
            if i == j:
                matches += 1
        assert (hist[i] == matches)


def test_histogramm_aus_graubild_merkel():
    img = cv2.imread('bilder/merkel-blazer.jpg')
    graubild = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = histogramm_graubild(graubild)
    assert (hist[17] == 2469)
    assert (hist[120] == 5887)
    assert (hist[67] == 8854)


def test_get_lower_threshold_from_histogram():
    assert (get_lower_threshold_from_histogram({3: 1}) is not None)


def test_histogramm_aus_liste():
    assert (histogramm_aus_liste([3]) is not None)


def test_graubild_zu_liste1():
    # Test case 1: single pixel image
    image = np.array([[128]])
    expected_output = [128]
    assert graubild_zu_liste(image) == expected_output


def test_graubild_zu_liste2():
    # Test case 2: 3x3 image with random pixel values
    image = np.array([[255, 0, 128], [64, 192, 32], [96, 224, 160]])
    expected_output = [0, 32, 64, 96, 128, 160, 192, 224, 255]
    assert graubild_zu_liste(image) == expected_output


def test_get_lower_threshold_from_histogram2():
    # Test case 2: Histogram with only one bin
    histogram = {0: 10}
    assert get_lower_threshold_from_histogram(histogram) == 0


def test_get_lower_threshold_from_histogram3():
    # Test case 3: Histogram with multiple bins
    histogram = {0: 10, 1: 20, 2: 5, 3: 15}
    assert get_lower_threshold_from_histogram(histogram) <= 2


def test_get_lower_threshold_from_histogram4():
    # Test case 4: Histogram with all bins having the same count
    histogram = {0: 10, 1: 10, 2: 10, 3: 10}
    assert get_lower_threshold_from_histogram(histogram) <= 2


def test_get_lower_threshold_from_histogram5():
    # Test case 5: Histogram with only one bin having count greater than 0
    histogram = {0: 0, 1: 0, 2: 0, 3: 10}
    assert get_lower_threshold_from_histogram(histogram) == 3
