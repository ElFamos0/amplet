def score_course(nb_mag:int, nb_clients:int):
    '''
        Calcule le score rapporté par une course en fonction du nombre de magasins et de clients.
        nb_mag : le nombre de magasins visités par le coursier
        nb_clients : le nombre de clients qui ont bénéficié de la course
    '''
    if nb_mag<0:
        raise ValueError("nombre de magasins visités négatif")
    if nb_clients<0:
        raise ValueError("nombre de clients négatif")
    return nb_clients*nb_mag