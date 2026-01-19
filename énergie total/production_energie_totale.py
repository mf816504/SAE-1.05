import csv #Import du module 
import matplotlib.pyplot as plt #Import du module 

annees = []  #creation de la liste qui va servir à stocker les années
productions = [] #creation de la liste qui va servir à stocker la production total

def ajouter_donnees(nom_fichier):  #déclaration d'une fonction qui permet de rajouter des fichier de manière plus pratique (un peu inutile pour un fichier, mais j'ai repris la même structure que mes programme qui en contiennes d'avantages)
    with open(nom_fichier, newline='', encoding="utf-8") as fichier: # Ouverture du fichier
        lecteur = csv.reader(fichier, delimiter=';')
        next(lecteur)
        
        for ligne in lecteur: #Parcour le fichier
            if len(ligne) < 3 or ligne[2].strip() == "":  #Vérification du nombre de colonne et supression des èspaces génant (car j'ai eu plusieur problème avec des colonnes vides ou un nombre différent de colonnes)
                continue #Passe à la ligne suivante
                
            donnee = ligne[1].strip() #Récupère la donnée et enleve les espaces génannt 
            if donnee != "Production totale": #Si la donnée rechercher ne correspond pas à celle voulue 
                continue #Passe à la ligne suivante
                
      
            annee = int(ligne[0][:4]) # Extrait l'année du fichier 
            valeur = float(ligne[2].replace(',', '.'))  # La valeur de production est récupérée, convertie en nombre réel et la virgule est remplacée par un point
            
            if annee in annees: # Evite les doublons
                index = annees.index(annee) # Récupèrer l'index de l'année
                productions[index] += valeur
            else:
                annees.append(annee) #Complète la liste avec les valeurs
                productions.append(valeur) #Complète la liste avec les valeurs



ajouter_donnees("production total.csv") # Ajout du fichier dans la fonction créer plus tôt


annees, productions = zip(*sorted(zip(annees, productions))) # Trie pour pouvoir mettre en forme la courbe

plt.plot(annees, productions, marker='o') # Affiche un point sur chaque année
plt.title("Production électrique totale en France") # Ajoute un titre
plt.xlabel("Année") #Nom des axes
plt.ylabel("Production (TWh)") #Nom des axes
plt.xticks(annees, rotation=45)  #Effectue une rotation de 45 degrés des années pour une meilleur visibilité 
plt.grid(True) # Ajoute une grille 
plt.show() # Affiche le graphique 