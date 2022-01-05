from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request, flash
from utils import vote_marchand
from utils import chemin


@app.route('/trajet', methods=['GET','POST'])
@login_required
def trajet():
    navettedisp = amplet.Amplets.query.filter_by(navette=True,ferme=True).order_by(amplet.Amplets.id).all()
    ifnull = "Il n'y a pas de navette à optimiser"
    for p in navettedisp:
        fonctionvote = vote_marchand.vote(p.id)
        listechoisie = fonctionvote[0]
        calcultrajet = []
        requete1 = adresses.Adresse.query.join(users.User, users.User.id_adresse==adresses.Adresse.id).filter(users.User.username=="navette").first()
        requete2 = users.User.query.filter(users.User.username=="navette").first()
        calcultrajet.append((requete1.coordx,requete1.coordy,requete2.id))
        print(calcultrajet)
        for elm in listechoisie:
            requete = adresses.Adresse.query.join(marchands.Marchands, marchands.Marchands.id_adresse==adresses.Adresse.id).filter(marchands.Marchands.id==elm).first()
            coordx = requete.coordx
            coordy = requete.coordy
            calcultrajet.append((coordx,coordy,elm))
        print(calcultrajet)
        chemin.pluscourtcheminexhaustifb(calcultrajet)
        


    return render_template("trajet.html", user=current_user.id)
