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
    #faut afficher les amplet sur lesquelles l'utilisateur a été accepté
    # + une fois que Jules aura fait le classement, les produits des commandes navettes qui sont dispo dans les masagasins selectionnés

    #je le fais en  rentrant de la salle, faut que je trouve comment faire des join mdr
    
    return render_template("commande.html",moi=current_user)