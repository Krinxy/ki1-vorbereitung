import os


def alle_bilder_in_verzeichnis(pfad: str):
    print("Alle Bilder in " + str(pfad))
    bilder_mit_pfad = []
    bilder = os.listdir(pfad)
    for file in bilder:
        print(file)
        bilder_mit_pfad.append(pfad + "/" + str(file))
    print("")
    return bilder_mit_pfad


def durchschnittliche_werte(feature_liste: list):
    # Berechnen der durchschnittlichen Features
    # assert len(feature_liste) >= 1
    if len(feature_liste) == 0:
        return 0.0
    # Aufsummieren aller berechneten Features
    durchschnitt = feature_liste[0]
    for features in feature_liste[1:]:
        durchschnitt += features
    # Teilen durch die Anzahl an Beispielen
    durchschnitt = durchschnitt / float(len(feature_liste))
    return durchschnitt
