from db import *
from models import *


def vote(id_amplet:int):
    lol = produits_amp.Produits_amp\
        .query.add_entity(produits.Produits,marchands.Marchands)\
        .join(produits.Produits)\
        .filter(produits_amp.Produits_amp.id_produit == produits.Produits.id, produits_amp.Produits_amp.id_amp == id_amplet)\
        .join(marchands.Marchands)\
        .filter(marchands.Marchands)
    for p in lol:
        print(f"{p[0].id_amp} et {p[1].nom}")
