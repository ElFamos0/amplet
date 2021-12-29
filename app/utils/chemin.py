from math import sqrt
import numpy as np



def creationgraph(listepoint:list):
    M = np.zeros((len(listepoint),len(listepoint)))
    for i in range(len(listepoint)):
        for j in range(len(listepoint)): #cette partie peut être simplifié car la matrice sera forcement symétrique car le graphe est symétrique (arrête qui ont le même poids que l'on parcourt dans un sens ou dans l'autre)
            if i != j:
                # Formule de calcul de la distance entre deux points dans un repère orthonormé 
                M[i,j] = sqrt((listepoint[j][0] - listepoint[i][0])**2 +  (listepoint[j][1] - listepoint[i][1])**2)
    return M

def pluscourtchemin(listepoint:list):
    """Suivant une liste de points (tuples) permet de calculer le plus court chemin reliant ces points le premier est l'endroit de départ, il s'agit en fait d'une instance du voyageur de commerce
    https://www.youtube.com/watch?v=xcDeWt2w6LM"""
    M = creationgraph(listepoint)
    listepassage = []
    listedejavisite = [0]
    while len(listedejavisite)!=len(listepoint):
        i = listedejavisite[-1]
        min = 10000
        for j in range(len(M[i])):
            if M[i][j]<=min and i!=j and j not in listedejavisite:
                min = M[i][j]
                visite = j
                passage = listepoint[j]
        listedejavisite.append(visite)
        listepassage.append(passage)
    listepassage.append(listepoint[0])
    return listepassage





    
    

print(creationgraph([(5,6),(3,2),(8,7),(6,9),(0,0)]))  
print(pluscourtchemin([(5,6),(3,2),(8,7),(6,9),(0,0)]))
print(pluscourtchemin([(20,13),(21,4),(45,9),(20,28),(8,7)]))
