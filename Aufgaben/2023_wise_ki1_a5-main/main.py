from hilfsfunktionen import alle_bilder_in_verzeichnis, durchschnittliche_werte
from featureberechnung import features_von_bild

apfelbilder = alle_bilder_in_verzeichnis("./beispieldaten/apfel")
bananenbilder = alle_bilder_in_verzeichnis("./beispieldaten/banane")


# TODO: Berechnen der features des Bildes unter image_pfad
# TODO: Hinzufügen der features zu der Liste der Ergebnisse der Äpfel,
#       Funktionsaufruf aus featureberechnung.py
#       Hinweis: Achte auf den Datentypen von der Variable apfelbilder
# TODO: Die Featureberechnung für die Bananenbilder, analog zu den Äpfeln

# Eine leere Liste wird erstellt

aepfel_ergebnisse = []
bananen_ergebnisse = []

# Für eine Anzahl in Apfelbilder werden Features berechnet
# Dann werden sie in die Liste beigegeben

for Bilder in apfelbilder:
    apfel = features_von_bild(Bilder)
    aepfel_ergebnisse.append(apfel)

# Das selbe passiert für Bananen

for Bilder in bananenbilder:    
    bananen = features_von_bild(Bilder)
    bananen_ergebnisse.append(bananen)


ergebnisse = {'apfel': aepfel_ergebnisse,
              'banane': bananen_ergebnisse}

durchschnitt_apfel = durchschnittliche_werte(ergebnisse["apfel"])
print("Durchschnittlicher Apfel:", durchschnitt_apfel)
durchschnitt_banane = durchschnittliche_werte(ergebnisse["banane"])
print("Durchschnittliche Banane:", durchschnitt_banane)

# TODO: Kommentar, welches Feature ist besser geeignet zur Unterscheidung von Äpfeln und Bananen?
#       Schaue dir gerne die Features über einen plot mit matplotlib.pyplot an

import matplotlib.pyplot as plt

# figure = Erstellen eines 10 Zoll x 6 Zoll Abbildung
plt.figure(figsize=(10, 6))
plt.title("Featurebetrachtung von Apfel- und Bananenbildern")
plt.xlabel("Bildindex")
plt.ylabel("Feature-Wert")

# Plot Entsteht durch Eingabe des Wertes, den man sehen möchte und dann Darstellungsart)

plt.plot(aepfel_ergebnisse, label="Apfel", color="r", marker='o', linestyle=" ")
plt.plot(bananen_ergebnisse, label="Banane", color="g", marker='x', linestyle=" ")
plt.legend()
plt.grid(True)
plt.show()
