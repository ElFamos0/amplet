from math import sqrt
import numpy as np
import itertools



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
    taillechemin = 0
    while len(listedejavisite)!=len(listepoint):
        i = listedejavisite[-1]
        min = float("inf") #valeur hypothétique qui ne sera jamais atteinte
        for j in range(len(M[i])):
            if M[i][j]<=min and i!=j and j not in listedejavisite:
                min = M[i][j]
                taillechemin += min
                visite = j
                passage = listepoint[j]
        listedejavisite.append(visite)
        listepassage.append(passage)
    taillechemin += M[listedejavisite[-1]][0]
    listepassage.append(listepoint[0])
    return listepassage


def pluscourtcheminexhaustif(listepoint:list):
    """Sachant qu'au maximum on passe par 6 points (une seule fois) on aura donc 1/2*(n-1)! chemins à tester pour voir lequel est le meilleur on liste donc toute les
    substitution avec un algorithme de Heap"""
    listepossible = []
    depart = listepoint[0]
    min = float("inf")

    def heap(listepoint:list,n):

        if n == 1:
            listepossible.append(listepoint)    
    
        for i in range(n):
            heap(listepoint, n-1)
    
            if n & 1:
                listepoint[0], listepoint[n-1] = listepoint[n-1], listepoint[0]
            else:
                listepoint[i], listepoint[n-1] = listepoint[n-1], listepoint[i] 
    heap(listepoint[1:],len(listepoint[1:]))
    for liste in listepossible:
        trajet = 0
        precedent = depart
        for elm in liste:
            trajet += sqrt(((elm[0] - precedent[0])**2) +  ((elm[1] - precedent[1])**2))
            precedent = elm
        trajet += sqrt(((depart[0] - precedent[0])**2) +  ((depart[1] - precedent[1])**2))
        if trajet < min:
            min = trajet
            listeretenu = liste
            listeretenu.append(depart)
    return listeretenu, trajet


            
def calcultrajet(listepoint):
    liste = listepoint[1:]
    depart = listepoint[0]
    trajet = 0
    precedent = depart
    for elm in liste:
            trajet += sqrt(((elm[0] - precedent[0])**2)+ ((elm[1] - precedent[1])**2))
            precedent = elm
    trajet += sqrt(((depart[0] - precedent[0])**2) + ((depart[1] - precedent[1])**2))
    return trajet


def pluscourtcheminexhaustifb(listepoint:list):
    """Sachant qu'au maximum on passe par 6 points (une seule fois) on aura donc 1/2*(n-1)! chemins à tester pour voir lequel est le meilleur on liste donc toute les
    substitution avec un algorithme de Heap"""
    listepossible = []
    depart = listepoint[0]
    min = float("inf")

    def heap(listepoint:list,n):

        if n == 1:
            listepossible.append(listepoint)    
    
        for i in range(n):
            heap(listepoint, n-1)
    
            if n & 1:
                listepoint[0], listepoint[n-1] = listepoint[n-1], listepoint[0]
            else:
                listepoint[i], listepoint[n-1] = listepoint[n-1], listepoint[i] 
    heap(listepoint[1:],len(listepoint[1:]))
    for liste in listepossible:
        trajet = 0
        precedent = depart
        for elm in liste:
            trajet += sqrt(((elm[0] - precedent[0])**2) +  ((elm[1] - precedent[1])**2))
            precedent = elm
        trajet += sqrt(((depart[0] - precedent[0])**2) +  ((depart[1] - precedent[1])**2))
        if trajet < min:
            min = trajet
            listeretenu = liste
            listeretenu.append(depart)
    return listeretenu, trajet

#print(pluscourtcheminexhaustif([(20,13),(21,4),(45,9),(20,28),(8,7)]))
#print(pluscourtcheminexhaustifb([(20,13,"maison"),(21,4,"point 1"),(45,9,"point 2"),(20,28,"point 3"),(8,7,"point 4")]))
#print(creationgraph([(5,6),(3,2),(8,7),(6,9),(0,0)]))  
#print(pluscourtchemin([(5,6),(3,2),(8,7),(6,9),(0,0)]))
#print(pluscourtchemin([(20,13),(21,4),(45,9),(20,28),(8,7)]))
#print(pluscourtcheminexhaustif([(20,13),(21,4),(45,9),(20,28),(8,7)]))
#print(pluscourtcheminexhaustif([(5,6),(3,2),(8,7),(6,9),(0,0)]))
#print(calcultrajet([(5, 6),(6, 9), (8, 7), (3, 2), (0, 0)]))
#print(calcultrajet([(5, 6),(0, 0), (3, 2), (8, 7), (6, 9)]))
#print(calcultrajet([(20,13), (21, 4), (8, 7), (20, 28), (45, 9)]))