import csv
import matplotlib.pyplot as plt

annees = []
productions = []

def ajouter_donnees(nom_fichier, donnees_trier):
    with open(nom_fichier, newline='', encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier, delimiter=';')
        next(lecteur)
        
        for ligne in lecteur:
            if len(ligne) < 3 or ligne[2] == "":
                continue
                
            donnee = ligne[1].strip()
            if donnee != donnees_trier:
                continue
                
            annee = int(ligne[0][:4])
            valeur = float(ligne[2].replace(',', '.'))
            
            if annee in annees:
                index = annees.index(annee)
                productions[index] += valeur
            else:
                annees.append(annee)
                productions.append(valeur)

ajouter_donnees("nucleaire.csv", "Production nucléaire")
ajouter_donnees("thermique.csv", "Production thermique fossile")

annees, productions = zip(*sorted(zip(annees, productions)))

plt.plot(annees, productions, marker='o')
plt.title("Évolution de la production nucléaire + thermique fossile en France")
plt.xlabel("Années")
plt.ylabel("Production annuelle en TWh")
plt.xticks(annees, rotation=45)
plt.grid(True)

plt.show()