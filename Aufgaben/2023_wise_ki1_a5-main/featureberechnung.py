import cv2
from image_functions import get_pixel_color_by_colorname
import numpy as np

# Irgendwelche Features spucken eine Zahl aus

def eigenes_feature(image: np.ndarray):
    # TODO: überlege dir ein sinnvolles Feature, das du berechnen kannst
        # Bild in Graustufen umwandeln
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gauss'schen Weichzeichners, um das Bild zu glätten und das Rauschen zu reduzieren
    verwischung = cv2.GaussianBlur(gray, (5, 5), 0)

    # Canny-Kantenerkennungsalgorithmus
    kanten = cv2.Canny(verwischung, 30, 150)

    # Finde Konturen im Bild
    konturen, _ = cv2.findContours(kanten.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    groesste_kontur = max(konturen, key=cv2.contourArea)

    umfang = cv2.arcLength(groesste_kontur, True)
    bereich = cv2.contourArea(groesste_kontur)
    rundheit = 4 * np.pi * bereich / (umfang ** 2)

    # Definiere Schwellenwert für Rundheit
    rundheit_schwellwert = 0.7

    # Wenn Rundheit größer als Schwellwert, dann vermutlich rund
    if rundheit > rundheit_schwellwert:
        # Zeichne Clickbait-Rechteck um das erkannte Objekt
        x, y, w, h = cv2.boundingRect(groesste_kontur)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return rundheit


def mittlerer_rotwert(image: np.ndarray):
    # TODO: Berechnen des mittleren Rotwertes aller Pixel im Bild
    # Hinweise: Verwende get_pixel_color_by_colorname
    red = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            red.append(get_pixel_color_by_colorname(image=image, x=i, y=j, color="r"))
    # Hinweis: Der Durchschnitt ist die Summe aller Werte geteilt durch die Anzahl der Werte
    avg_red = (sum(red) / len(red))
    return avg_red


def oberflaechentextur(image: np.ndarray):
    # Bild grau machen und Haralick-Texturen berechnen
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texturen = cv2.HuMoments(cv2.moments(gray_image)).flatten()

    combined_moments = np.mean(texturen)

    return combined_moments


def stielansatz(image: np.ndarray):
    hsvbild = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_braun = np.array([10, 50, 50])
    upper_braun = np.array([20, 255, 255])

    mask_brown = cv2.inRange(hsvbild, lower_braun, upper_braun)
    konturen, _ = cv2.findContours(mask_brown, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return len(konturen)


def krümmungsgrad(image: np.ndarray):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    konturen, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    größte_kontur = max(konturen, key=cv2.contourArea)

    epsilon = 0.1 * cv2.arcLength(größte_kontur, True)
    approx = cv2.approxPolyDP(größte_kontur, epsilon, True)

    krümmung = cv2.arcLength(approx, True)

    return krümmung


def gelbton_vergleich(image: np.ndarray):
    # Zufälligen Gelbton generieren

    import random

    random_gelb = (
        200 + random.randint(0, 56),
        200 + random.randint(0, 56),
        random.randint(0, 20)
    )

    # Durchschnittsfarben des Bildes berechnen
    avg_color = np.mean(image, axis=(0, 1)).astype(int)

    # Berechnung der euklidischen Distanz zwischen den Farben
    distanz = np.linalg.norm(np.array(avg_color) - np.array(random_gelb))
    max_distanz = np.linalg.norm(np.array([255, 255, 255]))

    # Bestimme die Ähnlichkeit als Prozentsatz der Distanz
    gelbton_ähnlichkeit = 1 - (distanz / max_distanz)

    return gelbton_ähnlichkeit


def lichtreflexion_kontrast(image: np.ndarray):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Berechne das Histogramm des Graustufenbildes
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Berechne Unterschied zwischen den hellsten und dunkelsten Pixeln im Histogramm
    contrast = (hist.max() - hist.min()) / hist.sum()

    return contrast


def berechne_features(image: np.ndarray):
    # ruft alle features auf und gibt sie als array zurück
    return np.array([mittlerer_rotwert(image), eigenes_feature(image)])


def features_von_bild(image_pfad: str):
    print("Berechne Features für folgendes Bild " + str(image_pfad))
    image = cv2.imread(image_pfad)
    features = berechne_features(image)
    print("Ergebnis: ", features)
    return features
