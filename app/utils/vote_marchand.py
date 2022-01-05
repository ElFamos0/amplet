from db import *
from models import *


def trifusion(listetri):
    if len(listetri) <= 1:
        return listetri
    else:
        m = len(listetri)//2
    liste1 = trifusion(listetri[:m])
    liste2 = trifusion(listetri[m:])
    retour = []
    while len(liste1) > 0 and len(liste2) > 0:
        if liste1[0][1] < liste2[0][1]:
            retour.append(liste1.pop(0))
        else:
            retour.append(liste2.pop(0))
    return retour + liste1 + liste2

#print(trifusion([("a",9.0),("b",7.5),("b",7.5),("b",94.8),("b",54.180),("b",110.17),("b",7.5),("b",7.5),("b",7.5),("b",64.52),("b",2.0001),("b",128.128),("b",7.89),("b",27.12)]))


def vote(id_amplet:str):
    dicomarchand = {}
    liste_marchand = []
    listedejavu = []
    dicttype = {}
    listetype = []
    infovote = produits_amp.Produits_amp\
        .query.add_entity(produits.Produits)\
        .join(produits.Produits, produits_amp.Produits_amp.id_produit == produits.Produits.id)\
        .filter(produits_amp.Produits_amp.id_amp == id_amplet)\
        .add_entity(marchands.Marchands)\
        .join(marchands.Marchands, produits.Produits.id_marchand == marchands.Marchands.id)
    for p in infovote:
        # print(f"{p[0].id_amp} commande {p[1].nom} chez {p[2].nom} de type {p[2].type}")
        idm = p[2].id 
        if idm not in listedejavu:
            dicttype[idm] = p[2].type
            listedejavu.append(idm)
            mamp = marchands_amp.Marchands_amp.query.filter_by(id_amp=id_amplet, id_marchand=idm).first()
            if not mamp.votes is None:
                dicomarchand[idm] = mamp.votes
            else:
                dicomarchand[idm] = p[2].multiplicateur
        else:
            if mamp.votes is None:
                dicomarchand[idm] += p[2].multiplicateur
    vue = dicomarchand.items()
    liste = list(vue)
    listetrie = trifusion(liste)
    for i in range(len(listetrie)-1,-1,-1):
        if len(liste_marchand) == 5:
            break
        if not dicttype[listetrie[i][0]] in listetype:
            liste_marchand.append(listetrie[i][0])
            listetype.append(dicttype[listetrie[i][0]])
        print(liste_marchand,dicomarchand)
    return (liste_marchand,dicomarchand)