import csv #Import du module
import matplotlib.pyplot as plt #Import du module

annees = [] #creation de la liste qui va servir à stocker les années
productions = [] #creation de la liste qui va servir à stocker la production total

def ajouter_donnees(nom_fichier, donnees_trier):  #déclaration d'une fonction qui permet de rajouter des fichier de manière plus pratique
    with open(nom_fichier, newline='', encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier, delimiter=';') # Ouverture du fichier
        next(lecteur)
         
        for ligne in lecteur: #Parcour le fichier 
            if len(ligne) < 3 or ligne[2] == "":  #Vérification du nombre de colonne (car j'ai eu plusieur problème avec des colonnes vides ou un nombre différent de colonnes)
                continue #Passe à la ligne suivante
                
            donnée = ligne[1].strip() #Récupère la donnée et enleve les espaces génannt 
            if donnée != donnees_trier:  #Si la donnée rechercher ne correspond pas à celle voulue 
                continue #Passe à la ligne suivante
                
            annee = int(ligne[0][:4])  # Extrait l'année du fichier 
            valeur = float(ligne[2].replace(',', '.'))  # La valeur de production est récupérée, convertie en nombre réel et la virgule est remplacée par un point
            
            if annee in annees: # Evite les doublons
                index = annees.index(annee)  # Récupèrer l'index de l'année
                productions[index] += valeur
            else:
                annees.append(annee)  #Complète la liste avec les valeurs
                productions.append(valeur)  #Complète la liste avec les valeurs

ajouter_donnees("hydraulique.csv", "Production hydraulique") # Ajout du fichier dans la fonction créer plus tôt
ajouter_donnees("eolien.csv", "Production éolienne") # Ajout du fichier dans la fonction créer plus tôt
ajouter_donnees("solaire.csv", "Production solaire") # Ajout du fichier dans la fonction créer plus tôt
ajouter_donnees("thermique renouvelable et déchets_.csv", "Production thermique renouvelable et déchets") # Ajout du fichier dans la fonction créer plus tôt

annees, productions = zip(*sorted(zip(annees, productions))) # Trie pour pouvoir mettre en forme la courbe

plt.plot(annees, productions, marker='o')  # Affiche un point sur chaque année
plt.title("Évolution de la production d'énergie renouvelable en France")  # Ajoute un titre
plt.xlabel("Années")  #Nom des axes
plt.ylabel("Production annuelle en TWh") #Nom des axes
plt.xticks(annees, rotation=45)
plt.grid(True)  # Ajoute une grille 
plt.show()   # Affiche le graphique 