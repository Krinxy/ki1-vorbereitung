import cv2
import numpy as np


def featureberechnung_alle_bilder(apfelbilder: list, bananenbilder: list):
    # Features und Labels für alle Bilder berechnen
    # Label encoding: 0 = Apfel, 1 = Banane
    # TODO: berechne features und labels für alle Bilder und füge sie den Listen hinzu
    
    alle_features = []
    alle_labels = []

    for bilder in apfelbilder:
        alle_features.append(features_von_bild(bilder))
        alle_labels.append(0)

    for bilder in bananenbilder:
        alle_features.append(features_von_bild(bilder))
        alle_labels.append(1)
    return alle_features, alle_labels


def get_pixel_color_by_colorindex(image, x: int, y: int, color_index: int):
    if color_index > 2 or color_index < 0:
        return None

    x_size = image.shape[0]
    y_size = image.shape[1]
    if x > x_size or x < 0:
        return None
    if y > y_size or y < 0:
        return None
    # For the pixel at location x and y, you have a list/array of three values.
    # return the value of the requested color for the pixel
    return image[x][y][color_index]


def get_pixel_color_by_colorname(image, x: int, y: int, color: str = "r"):
    color = color.lower()
    if color == "b":
        color_index = 0
    elif color == "g":
        color_index = 1
    elif color == "r":
        color_index = 2
    else:
        return None
    # For the pixel at location x and y, you have a list/array of three values.
    # return the value of the requested color for the pixel
    return get_pixel_color_by_colorindex(image=image, x=x, y=y, color_index=color_index)


def durchschnitt(werte: list):
    durchschnittswert = sum(werte / len(werte))
    return durchschnittswert


def abweichung_zu_gelb(pixelwerte: np.array):
    max_gelb = np.array([0, 255, 255])
    abweichung = np.sum(np.abs(pixelwerte - max_gelb))
    return abweichung


def anteil_gelber_pixel(bild):
    # Berechnen des Anteils gelb "genuger" Pixel
    # NOTE: ANTEIL, NICHT ANZAHL! Sonst würden große und kleine Bilder unterschiedlich behandelt!
    maximale_abweichung = 100.0
    anzahl_gelber_pixel = 0
    for i in range(bild.shape[0]):
        for j in range(bild.shape[1]):
            if abweichung_zu_gelb(bild[i, j]) < maximale_abweichung:
                anzahl_gelber_pixel += 1

    anteil = anzahl_gelber_pixel / (bild.shape[0] * bild.shape[1])
    return anteil


def mittlere_abweichung_zu_gelb(bild):
    # Berechnen der Abweichung jedes Pixels zum maximalen Gelbwert
    gesamte_abweichung = 0.0
    for i in range(bild.shape[0]):
        for j in range(bild.shape[1]):
            gesamte_abweichung += abweichung_zu_gelb(bild[i, j])

    durchschnittliche_abweichung = gesamte_abweichung / (bild.shape[0] * bild.shape[1])
    return durchschnittliche_abweichung


def rotwert_bildmitte(bild):
    # Berechnen des mittleren Rotwertes der Pixel in der Bildmitte
    gesamt_rotwert = 0.0
    start_bildmitte_dim0 = int(0.25*bild.shape[0])
    ende_bildmitte_dim0 = int(0.75*bild.shape[0])
    start_bildmitte_dim1 = int(0.25*bild.shape[1])
    ende_bildmitte_dim1 = int(0.75*bild.shape[1])
    for i in range(start_bildmitte_dim0, ende_bildmitte_dim0):
        for j in range(start_bildmitte_dim1, ende_bildmitte_dim1):
            gesamt_rotwert += get_pixel_color_by_colorname(image=bild, x=i, y=j, color="r")

    durchschnittlicher_rotwert = gesamt_rotwert / (0.5*bild.shape[0] * 0.5*bild.shape[1])
    return durchschnittlicher_rotwert


def durchschnittlicher_rotwert(bild):
    # Berechnen des mittleren Rotwertes aller Pixel im Bild
    gesamt_rotwert = 0.0
    for i in range(bild.shape[0]):
        for j in range(bild.shape[1]):
            gesamt_rotwert += get_pixel_color_by_colorname(image=bild, x=i, y=j, color="r")

    durchschnittlicher_rotwert = gesamt_rotwert / (bild.shape[0] * bild.shape[1])
    return durchschnittlicher_rotwert


def eigenes_feature(bild):
    # TODO: optional eigenes Feature implementieren, kann von letzter Übung übernommen werden falls nicht bereits vorhanden
    return 0


def berechne_features(bild):
    return np.array([durchschnittlicher_rotwert(bild), rotwert_bildmitte(bild),
                     mittlere_abweichung_zu_gelb(bild), anteil_gelber_pixel(bild), eigenes_feature(bild)])


def features_von_bild(bild_pfad: str):
    print("Berechne Features für folgendes Bild " + str(bild_pfad))
    bild = cv2.imread(bild_pfad)
    features = berechne_features(bild)
    print("Ergebnis: ", features)
    return features
