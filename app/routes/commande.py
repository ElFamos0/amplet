from flask_login.utils import login_required
from db import *
from models import *
from flask_login import current_user
from flask import render_template

##############################
########## COMMANDE  #########
##############################

@app.route("/commande")
@login_required
def commande():
    inscr_id_coursier = []
    inscr_id_amp = []
    inscr_valide = []
    inscr_nom_coursier = []
    cours_id_amp = []
    inscriptions = participants_amp.Participants_amp.query.filter_by(id_user=current_user.id).all()
    for i in range(len(inscriptions)):
        temp = inscriptions[i]
        inscr_id_amp.append(temp.id_amp)
        if temp.valide==0:
            inscr_valide.append("En attente")
        if temp.valide==1:
            inscr_valide.append("Accepté")
        if temp.valide==2:
            inscr_valide.append("Refusé")
        inscr_id_coursier.append(amplet.Amplets.query.filter_by(id = inscr_id_amp[-1], navette = 0).first().id_coursier)
        inscr_nom_coursier.append(users.User.query.filter_by(id = inscr_id_coursier[-1]).first().username)
    n = len(inscriptions)


        
    



    # afficher les amplet dont user est le coursier
    # + une fois que Jules aura fait le classement, les produits des commandes navettes qui sont dispo dans les masagasins selectionnés

    
    return render_template("commande.html",moi=current_user,n=n,inscr_id_amp=inscr_id_amp, inscr_valide=inscr_valide,inscr_id_coursier=inscr_id_coursier,inscr_nom_coursier=inscr_nom_coursier)