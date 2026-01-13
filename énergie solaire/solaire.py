import csv
import matplotlib.pyplot as plt

annees = []
productions = []

with open("solaire.csv", newline='', encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier, delimiter=';')
    next(lecteur)

    for ligne in lecteur:
        annee = int(ligne[0][:4])
        
        if ligne[2] == "":
            continue

        valeur = float(ligne[2].replace(',', '.'))

        if annee in annees:
            index = annees.index(annee)
            productions[index] += valeur
        else:
            annees.append(annee)
            productions.append(valeur)

plt.bar(annees, productions)
plt.title("Évolution de la production d'électricité solaire")
plt.xlabel("Années")
plt.ylabel("Production annuelle en TWh")
plt.xticks(annees, rotation=45)
plt.show()

