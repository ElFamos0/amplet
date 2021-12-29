from math import sqrt
import numpy as np
def pluscourtchemin(listepoint:list):
    """Suivant une liste de points (tuples) permet de calculer le plus court chemin reliant ces points le premier est l'endroit de départ, il s'agit en fait d'une instance du voyageur de commerce"""
    depart = listepoint[0]
    listepoint = listepoint[1:]

def creationgraph(listepoint:list):
    M = np.zeros((len(listepoint),len(listepoint)))
    for i in range(len(listepoint)):
        for j in range(len(listepoint)):
            if i != j:
                M[i,j] = sqrt((listepoint[j][0] - listepoint[i][0])**2 +  (listepoint[j][1] - listepoint[i][1])**2)
    return M

    
pluscourtchemin([(5,6),(3,2),(8,7),(6,9),(0,0)])
print(creationgraph([(5,6),(3,2),(8,7),(6,9),(0,0)]))
