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
    affichage = []
    navettedisp = amplet.Amplets.query.filter_by(navette=True,ferme=True).order_by(amplet.Amplets.id).all()
    if not navettedisp:
        return render_template("info.html", msg="Il n'y a pas de navette")
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
        resultat = chemin.pluscourtcheminexhaustifb(calcultrajet)
        trajet = resultat[1]
        passage = []
        for elm in resultat[0][:-1]:
            requete3 = marchands.Marchands.query.filter(marchands.Marchands.id==elm[2]).first()
            print(elm[2])
            passage.append(requete3.nom)
        affichage.append((p.id,passage,trajet))
        

    return render_template("trajet.html", user=current_user.id, affichage=affichage)
