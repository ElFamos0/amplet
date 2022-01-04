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
        listeproduits += [{"nom":p[0].nom, "prix:": p[0].prix} for p in prod]
    
    if participants_amp.Participants_amp.query.filter_by(id_amp=ampl,id_user=current_user.id).first() is not None:
        flash("Vous vous êtes déjà inscrit à cet amplet !")
    if not request.form.get('err') is None:
        flash("Merci de ne pas mettre plus d'une fois le même article.")
    return render_template('inscription_amplet.html', user=current_user, produits=listeproduits, amp = am)
 