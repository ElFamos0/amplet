from math import sqrt
import numpy as np



def creationgraph(listepoint:list):
    M = np.zeros((len(listepoint),len(listepoint)))
    for i in range(len(listepoint)):
        for j in range(len(listepoint)):
            if i != j:
                # Formule de calcul de la distance entre deux points dans un repère orthonormé
                M[i,j] = sqrt((listepoint[j][0] - listepoint[i][0])**2 +  (listepoint[j][1] - listepoint[i][1])**2)
    return M

def pluscourtchemin(listepoint:list):
    """Suivant une liste de points (tuples) permet de calculer le plus court chemin reliant ces points le premier est l'endroit de départ, il s'agit en fait d'une instance du voyageur de commerce
    https://www.youtube.com/watch?v=xcDeWt2w6LM"""
    M = creationgraph(listepoint)
    """
    deparr = listepoint[0] #un mélange de départ et arrivée
    listemagasin = listepoint[1:] #les magasins qu'il faut visiter
    """
    listepassage = []
    listedejavisite = [0]
    while len(listedejavisite)!=len(listepoint):
        i = listedejavisite[-1]
        print(f"je vais sur la ligne {i}")
        min = 10000
        for j in range(len(M[i])):
            if M[i][j]<=min and i!=j and j not in listedejavisite:
                min = M[i][j]
                visite = j
                print(f"la valeur {j} est la plus petite pour le moment")
                passage = listepoint[j]
        listedejavisite.append(visite)
        listepassage.append(passage)
    listepassage.append(listepoint[0])
    return listepassage





    
    

    
pluscourtchemin([(5,6),(3,2),(8,7),(6,9),(0,0)])
