from db import *
from models import *

def update_multiplicateur(liste_id_marchand,dic_marchand) :

    l_marchand = marchands.Marchands.query.all()
    l_non_select = []
    vote_tot = 0
    
    for march in l_marchand :
        if march.id in liste_id_marchand :
            march.multiplicateur = 1
        else :
            l_non_select.append(march)
            if march.id in dic_marchand:
                vote_tot += dic_marchand[march.id]
        
    for march in l_non_select :
        if march.id in dic_marchand:
            march.multiplicateur *= (1 + dic_marchand[march.id]/vote_tot)
    
    db.session.commit()

