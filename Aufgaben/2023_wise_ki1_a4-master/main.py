import cv2
from schwellwert import oberer_schwellwert, unterer_schwellwert
from histogram import histogramm_graubild, plot_histogram, get_lower_threshold_from_histogram

# Hinweis: pip install -r requirements.txt  installiert alle benötigten Pakete
# Hinweis2: Fenster über eine Taste (auf dem Keyboard) schließen: cv2.waitKey(0)

img = cv2.imread('bilder/apfel.jpg')

graubild = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Graubild', graubild)
# um sich das Bild anzeigen zu lassen, muss die folgende Zeile auskommentiert werden
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# TODO: Finde einen guten oberen Schwellwert für das Beispielbild (durch Testen verschiedener Werte)
guter_oberer_schwellwert = 123
guter_unterer_schwellwert = 35

# Anwendung beider Schwellwerte auf das Graubild
result = oberer_schwellwert(grauwert_bild=graubild, schwellwert=guter_oberer_schwellwert)
result = unterer_schwellwert(grauwert_bild=result, schwellwert=guter_unterer_schwellwert)

cv2.imshow('schwellwert ', result)


# TODO: verwende die selbstgeschriebenen Funktionen, um ein Histogramm zu erstellen und plotte es anschließend
histogramm_graubild(graubild)
histogramm_graubild(result)

print("Close the Windows by pressing any key")
# Die folgende Zeile sollte für pytests auskommentiert werden:
cv2.waitKey(0)
cv2.destroyAllWindows()
