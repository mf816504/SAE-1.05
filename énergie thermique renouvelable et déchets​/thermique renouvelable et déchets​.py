import csv
import matplotlib.pyplot as plt

annees = []
productions = []

with open("thermique renouvelable et déchets​.csv", newline='', encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier, delimiter=';')
    next(lecteur)

    for ligne in lecteur:
        if ligne and ligne[2] != '':
            annee = int(ligne[0][:4])
            valeur = float(ligne[2].replace(',', '.'))

            if annee in annees:
                index = annees.index(annee)
                productions[index] = productions[index] + valeur
            else:
                annees.append(annee)
                productions.append(valeur)

plt.bar(annees, productions)
plt.title("Évolution de la production d'électricité thermique renouvelable et déchets​")
plt.xlabel("Années")
plt.ylabel("Production annuelle en TWh")
plt.show()
