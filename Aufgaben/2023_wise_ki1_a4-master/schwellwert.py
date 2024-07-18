from copy import copy


def oberer_schwellwert(grauwert_bild, schwellwert: float):
    neu = copy(grauwert_bild)
    # TODO: Diese Funktion setzt alle Anteile im Schwarz-Weiß-Bild über dem oberen Schwellwert auf 255
    # Achte darauf nicht das Originalbild (grauwert_bild) zu verändern, sondern die Variable neu
    for i in range(neu.shape[0]):
        for j in range(neu.shape[1]):
            scale = neu[i, j]

            if scale > schwellwert:
                neu[i, j] = 255


    return neu


# TODO: Schreibe die Funktion für den unteren Schwellwert
def unterer_schwellwert(grauwert_bild, schwellwert: float):
    neu = copy(grauwert_bild)
    # TODO: Diese Funktion setzt alle Anteile im Schwarz-Weiß-Bild unter dem unteren Schwellwert auf 0
    # Achte darauf nicht das Originalbild (grauwert_bild) zu verändern, sondern die Variable neu
    for i in range(neu.shape[0]):
        for j in range(neu.shape[1]):
            scale = neu[i, j]

            if scale < schwellwert:
                neu[i, j] = 0
    return neu
