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
    ampletinscrit = []
    ampletcoursier = []
    inscriptions = participants_amp.Participants_amp.query.filter_by(id_user=current_user.id).all()
    for i in range(len(inscriptions)):
        ampletinscrit.append(inscriptions[i].id_amp)

    #faut afficher les amplet sur lesquelles l'utilisateur a été accepté
    # + une fois que Jules aura fait le classement, les produits des commandes navettes qui sont dispo dans les masagasins selectionnés

    
    return render_template("commande.html",moi=current_user,inscription=ampletinscrit,coursier=ampletcoursier)