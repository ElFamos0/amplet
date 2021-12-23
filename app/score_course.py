# calcule le score rapporté par une course en fonction de
# nb_mag : le nombre de magasins visités par le coursier
# nb_clients : le nombre de clients qui ont bénéficié de la course
def score_course(nb_mag, nb_clients):
    if nb_mag<0:
        raise ValueError("nombre de magasins visités négatif")
    if nb_clients<0:
        raise ValueError("nombre de clients négatif")
    return nb_clients*nb_mag