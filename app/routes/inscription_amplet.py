from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request, flash
from utils.amplets_a_afficher import amplet_dict

@app.route('/i/<string:id>', methods=['GET'])
@login_required
def inscription_amplet(id) :
    ampl = id
    am = amplet_dict(ampl)

    mag = marchands.Marchands.query.add_entity(marchands_amp.Marchands_amp).join(marchands_amp.Marchands_amp).filter(marchands_amp.Marchands_amp.id_amp == ampl,marchands_amp.Marchands_amp.id_marchand==marchands.Marchands.id)
    
    liste_mag = [m[0].id for m in mag]
    listeproduits = []
    for id_mag in liste_mag :
        prod = produits.Produits.query.add_entity(marchands.Marchands).join(marchands.Marchands).filter(marchands.Marchands.id == id_mag,produits.Produits.id_marchand == marchands.Marchands.id)
        listeproduits += [{"nom":p[0].nom,"marchand": p[1].nom} for p in prod]
    

    mon_amplet = amplet.Amplets.query.filter(amplet.Amplets.id==ampl).first().id_coursier == current_user.id

    if participants_amp.Participants_amp.query.filter_by(id_amp=ampl,id_user=current_user.id).first() is not None:
        flash("Vous vous êtes déjà inscrit à cette amplet !")
    if request.form.get('err') is not None:
        flash("Merci de ne pas mettre plus d'une fois le même article.")
    if mon_amplet :
        flash("Vous ne pouvez pas vous inscrire sur votre amplet !")
    return render_template('inscription_amplet.html', user=current_user, produits=listeproduits, amp = am)
 