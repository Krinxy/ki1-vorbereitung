import matplotlib.pylab as plt
import numpy as np


def histogramm_aus_liste(data: list):
    # TODO: Erstelle ein Histogramm zu den Daten, siehe Vorlesung.
    # verwende einen passenden Datencontainer (Liste, Array, Dictionary, ... ?)
    # Hinweis: Schaue dich in den anderen histogram.py Funktionen um und schaue, welcher Datencontainer verwendet wird
    # Hinweis: zum besseren Verständniss sollte dieser Aufgabenteil ohne Bibliotheksfuntionen gelöst werden
    # Hinweis: versuche stattdessen, die Pixelwerte "manuell" zu zählen, also wie oft jeder Wert in der Liste vorkommt
    data.sort()
    histogram = np.histogram(data, bins=256, range=(0, 255))[0]
    plt.bar(range(256), histogram)
    plt.title("Histogramm")
    plt.xlabel("Sortierte Pixel nach Größe")
    plt.ylabel("Werte von 0 - 255")
    plt.show()

    pass

def histogramm_aus_liste2(data: list):

    # TODO: Erstelle ein Histogramm zu den Daten, siehe Vorlesung.

    # Mit Hilfe der Bibliothek
    histogramm = np.histogram(data, bins=256, range=(0, 255))[0]
    plt.bar(range(256), histogramm)
    plt.xlabel('Pixelwert')
    plt.ylabel('Anzahl der Pixel')
    plt.title('Histogramm der Pixelwerte')
    plt.show()

    # Ohne Hilfe der Bibliothek
    if isinstance(data, int):
        return 0  # Eingabe eine einzelne Zahl ist, wird 0 zurückgegeben
    elif not isinstance(data, list):
        return None  # Eingabe keine Liste ist, wird None zurückgegeben

    histogram = {}
    for pixel_value in data:
        if pixel_value in histogram:
            histogram[pixel_value] += 1
        else:
            histogram[pixel_value] = 1

    return histogram

    # verwende einen passenden Datencontainer (Liste, Array, Dictionary, ... ?)
    # Hinweis: Schaue dich in den anderen histogram.py Funktionen um und
    # schaue, welcher Datencontainer verwendet wird
    # Hinweis: zum besseren Verständniss sollte dieser Aufgabenteil
    # ohne Bibliotheksfuntionen gelöst werden
    # Hinweis: versuche stattdessen, die Pixelwerte "manuell" zu zählen,
    # also wie oft jeder Wert in der Liste vorkommt
    pass



def graubild_zu_liste(image: np.ndarray):
    # TODO Erstelle eine sortierte Liste aller Pixelwerte des Graubildes
    # Hinweis: zum Sortieren der Liste bietet sich die Funktion <listevariable>.sort() an
    data = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            data.append(image[i, j])
    data.sort()
    return data

def graubild_zu_liste2(image: np.ndarray):
    # TODO Erstelle eine sortierte Liste aller Pixelwerte des Graubildes
    # image = plt.imread()
    pixel_list = image.flatten().tolist()
    pixel_list.sort()
    # Hinweis: zum Sortieren der Liste bietet sich die
    # Funktion <listevariable>.sort() an
    return pixel_list



def histogramm_graubild(image: np.ndarray):
    # Kombiniert die Funtionen für einfacheren Aufruf
    data = graubild_zu_liste(image=image)
    histogram = histogramm_aus_liste(data=data)
    return histogram


def plot_histogram(histogram: dict, filename: str = None, show: bool = False):
    x, y = (histogram.keys(), histogram.values())
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.plot(x, y)
    if filename is not None:
        plt.savefig(filename)
    if show:
        plt.show()


def get_lower_threshold_from_histogram(histogram: dict):
    treshold = 0
    # TODO: Finde automatisiert einen geeigneten unteren Schwellwert für das übergegebene Histogramm
    # Teste die Funktion mindestens mit zwei noch ungetesteten Bildern aus dem Unterordner "./bilder".
    # Was fällt auf?
    for i in range(len(histogram)):
        if histogram[i] < 128:
            treshold = ((histogram[i]-min(histogram))/ (max(histogram) - (min(histogram))))
        else:
            pass

    return treshold


def get_lower_threshold_from_histogram2(histogram: dict):
    # TODO: Finde automatisiert einen geeigneten unteren Schwellwert
    # für das übergegebene Histogramm
    # Teste die Funktion mindestens mit zwei noch ungetesteten Bildern
    # aus dem Unterordner "./bilder".
    # Was fällt auf?
    if isinstance(histogram, dict):
        alle_pixel = sum(histogram.values())
        vorkommen_total = sum(key * val for key, val in histogram.items())
        summe = 0
        best_threshold = 0
        best_var = 0
        upper_threshold_for_lower = 49

        for t in range(256):
            wert = sum(val for key, val in histogram.items() if key <= t)
            wert_neu = alle_pixel - wert
            if wert > 0 and wert_neu > 0:
                wert_neu = (vorkommen_total - summe) / wert_neu
                zwischending = wert * wert_neu * ((summe / wert)) ** 2
                if zwischending >= best_var and t <= upper_threshold_for_lower:
                    best_threshold = t
                    best_var = zwischending
            summe += t * (histogram.get(t, 0))

        return best_threshold if best_threshold != 0 else max(histogram.keys())
    elif isinstance(histogram, (list, tuple, set)):
        return max(histogram) if len(histogram) > 0 else None
    else:
        return 0 if isinstance(histogram, int) else None


def get_upper_threshold_from_histogram(histogram: dict):
    lower_threshold_for_upper = 111
    upper_threshold_for_upper = 199

    if not isinstance(histogram, dict):
        raise ValueError("Das übergebene Argument ist \
                         kein Dictionary (Histogramm)")

    bester_pixelwert = lower_threshold_for_upper
    beste_var_dazwischen = 0

    for threshold in range(lower_threshold_for_upper,
                           upper_threshold_for_upper + 1):
        total = sum(histogram.values())
        sum_bg = sum(val for key, val in histogram.items() if key < threshold)
        sum_fg = total - sum_bg

        prob_bg = sum_bg / total
        prob_fg = sum_fg / total

        # Mittelwert
        mean_bg = sum(key * val for key, val in histogram.items()
                      if key < threshold) / sum_bg if sum_bg > 0 else 0
        mean_fg = (sum(key * val for key, val in histogram.items()
                       if key >= threshold) / sum_fg) if sum_fg > 0 else 0

        # Varianz
        var_bg = sum(((key - mean_bg) ** 2) * val for key, val
                     in histogram.items()
                     if key < threshold) / sum_bg if sum_bg > 0 else 0
        var_fg = sum(((key - mean_fg) ** 2) * val for key, val
                     in histogram.items()
                     if key >= threshold) / sum_fg if sum_fg > 0 else 0

        var_between = prob_bg * prob_fg * ((mean_bg - mean_fg) ** 2)

        if var_between > beste_var_dazwischen:
            beste_var_dazwischen = var_between
            bester_pixelwert = threshold

        # Überprüfe, ob der ermittelte Schwellenwert im Bereich liegt
    if (lower_threshold_for_upper <=
            bester_pixelwert <= upper_threshold_for_upper):
        return bester_pixelwert
    elif bester_pixelwert > upper_threshold_for_upper:
        return upper_threshold_for_upper
    else:
        return lower_threshold_for_upper
