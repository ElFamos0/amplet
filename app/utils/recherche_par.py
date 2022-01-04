from db import *
from models import *

def distance(adresse1,adresse2) :
    
    x1 = adresse1.coordx
    x2 = adresse2.coordx
    distx = x1-x2

    y1 = adresse1.coordy
    y2 = adresse2.coordy
    disty = y1-y2

    return (distx**2 + disty**2)**(0.5)



def recherche_par(liste_amplet,type,id_adresse = 0) :
    if type == "Proximité" : # A améliorer avec une API type google map

        if len(liste_amplet) <= 1 :
            return(liste_amplet)
        else :
            m = len(liste_amplet)//2

        l1 = recherche_par(liste_amplet[:m],type,id_adresse)
        l2 = recherche_par(liste_amplet[m:],type,id_adresse)
        retour = []
        adresse_user = adresses.Adresse.query.get(id_adresse)
        while len(l1) >0 and len(l2) >0 :

                id_ad1 = users.User.query.get(l1[0]['id_cours']).id_adresse
                id_ad2 = users.User.query.get(l2[0]['id_cours']).id_adresse

                adresse1 = adresses.Adresse.query.get(id_ad1)
                adresse2 = adresses.Adresse.query.get(id_ad2)

                distance1 = distance(adresse_user,adresse1)
                distance2 = distance(adresse_user,adresse2)

                if distance1 < distance2 :
                    retour.append(l1.pop(0))
                else :
                    retour.append(l2.pop(0))

        return retour + l1 + l2

    elif type =='Date de début' :

        if len(liste_amplet) <= 1 :
            return(liste_amplet)
        else :
            m = len(liste_amplet)//2

        l1 = recherche_par(liste_amplet[:m],type)
        l2 = recherche_par(liste_amplet[m:],type)
        retour = []
        while len(l1) >0 and len(l2) >0 :
                if l1[0]['date'] < l2[0]['date'] :
                    retour.append(l1.pop(0))
                else :
                    retour.append(l2.pop(0))

        return retour + l1 + l2


#l = [{'date' : 3,'cp': 54000},{'date' : 12,'cp': 54500},{'date' : 4,'cp': 57200},{'date' : 2,'cp': 54100},{'date' : 0,'cp': 54300},{'date' : 9,'cp': 54620},{'date' : 7,'cp': 54700}]
#print(recherche_par(l,'Proximité',54600))
#print(recherche_par(l,'Date de début',54600))
