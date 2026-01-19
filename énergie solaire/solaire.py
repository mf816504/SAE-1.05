import csv #Import du module
import matplotlib.pyplot as plt #Import du module

annees = [] #creation de la liste qui va servir à stocker les années
productions = [] #creation de la liste qui va servir à stocker la production total

with open("solaire.csv", newline='', encoding="utf-8") as fichier: # Ouverture du fichier csv pour pouvoir le lire 
    lecteur = csv.reader(fichier, delimiter=';') # Déclaration du délimiteur
    next(lecteur) # Saute la première ligne pour la bonne lecture des données

    for ligne in lecteur: #Parcour le fichier ligne par ligne
        annee = int(ligne[0][:4]) # Extrait l'année du fichier 
        
        if ligne[2] == "":  # Pour cette ligne j'ai du me faire aider car mon programme ne marchais pas sans. Il y à sans doute une meilleur façon de faire mais cette ligne regarde si la valeur est vide et si oui ignore les lignes suivantes
            continue

        valeur = float(ligne[2].replace(',', '.'))  # La valeur de production est récupérée, convertie en nombre réel et la virgule est remplacée par un point

        if annee in annees: #Parcour le fichier
            index = annees.index(annee) # Récupèrer l'index de l'année
            productions[index] += valeur
        else:
            annees.append(annee)
            productions.append(valeur)
    

plt.bar(annees, productions)# Produit un diagramme en bar
plt.title("Évolution de la production d'électricité solaire")  # Ajoute un titre
plt.xlabel("Années")#Nom des axes
plt.ylabel("Production annuelle en TWh")#Nom des axes
plt.xticks(annees, rotation=45) #Effectue une rotation de 45 degrés des années pour une meilleur visibilité 
plt.show() # Affiche le graphique


