import csv #Import du module
import matplotlib.pyplot as plt #Import du module

annees = []  #creation de la liste qui va servir à stocker les années
productions = [] #creation de la liste qui va servir à stocker la production total

with open("thermique.csv", newline='', encoding="utf-8") as fichier:  # Ouverture du fichier csv pour pouvoir le lire 
    lecteur = csv.reader(fichier, delimiter=';') # Déclaration du délimiteur
    next(lecteur) # Saute la première ligne pour la bonne lecture des données

    for ligne in lecteur: #Parcour le fichier
        
        if ligne and ligne[2] != '': #Vérifie si la ligne est vide
            annee = int(ligne[0][:4])  # Extrait l'année du fichier
            valeur = float(ligne[2].replace(',', '.')) # La valeur de production est récupérée, convertie en nombre réel et la virgule est remplacée par un point

            if annee in annees:  #Parcour le fichier
                index = annees.index(annee) # Récupèrer l'index de l'année
                productions[index] +=valeur
            else:
                annees.append(annee) #Complète la liste avec les valeurs
                productions.append(valeur) #Complète la liste avec les valeurs

plt.bar(annees, productions) # Produit un diagramme en bar
plt.title("Évolution de la production d'électricité thermique fossile") # Ajoute un titre
plt.xlabel("Années") #Nom des axes
plt.ylabel("Production annuelle en TWh") #Nom des axes
plt.show() # Affiche le graphique 

