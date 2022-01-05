from vote_marchand import *
#cette fonction ne marche pas dans la configuration actuelle
#je fais ce test sans utiliser pytest car il ne semble pas accepter l'import de la database

def test_trifusion():
    assert trifusion([("lol",1),("bonjour",3),("bonsoir",2)]) == [("lol",1),("bonsoir",2),("bonjour",3)]
    assert trifusion([("a",9.0),("b",7.5),("b",7.5),("b",94.8),("b",54.180),("b",110.17),("b",7.5),("b",7.5),("b",7.5),("b",64.52),("b",2.0001),("b",128.128),("b",7.89),("b",27.12)]) == [('b', 2.0001), ('b', 7.5), ('b', 7.5), ('b', 7.5), ('b', 7.5), ('b', 7.5), ('b', 7.89), ('a', 9.0), ('b', 27.12), ('b', 54.18), ('b', 64.52), ('b', 94.8), ('b', 110.17), ('b', 128.128)]
print(test_trifusion)