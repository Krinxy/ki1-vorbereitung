from machine_learning import ki_pipeline
from auswertung import auswerten

print("")
print("Wir versuchen Bananen zu identifizieren!")
print("")


ergebnisse, labels = ki_pipeline()


# Ergebnisse ansehen
print("Label encoding: 0 = Nicht Banane, 1 = Banane")
for i in range(len(labels)):
    print("Ergebnis:", ergebnisse[i], " Wahr:", labels[i])

# Ergebnisse auswerten
auswerten(truth=labels, results=ergebnisse)
