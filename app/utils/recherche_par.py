def recherche_par(liste_amplet,type,cp = 0) :
    if type == "Proximité" : # A améliorer avec une API type google map

        if len(liste_amplet) <= 1 :
            return(liste_amplet)
        else :
            m = len(liste_amplet)//2

        l1 = recherche_par(liste_amplet[:m],type,cp)
        l2 = recherche_par(liste_amplet[m:],type,cp)
        retour = []
        while len(l1) >0 and len(l2) >0 :

                cp1 = abs(l1[0]['cp']-cp)
                cp2 = abs(l2[0]['cp'] -cp)

                if cp1 < cp2 :
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
