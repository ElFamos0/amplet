from flask_login.utils import login_required
from utils.score_course import score_course
from db import *
from models import *
from flask_login import current_user
from flask import render_template
from routes.profil_commandes import commande

@app.route('/f/<string:id_ampl>/')
@login_required
def fermerAmplet(id_ampl):
    amp = amplet.Amplets.query.filter_by(id = id_ampl).first()
    if amp and current_user.id==amp.id_coursier:
        amp.ferme=1
        nb_marchands = len(marchands_amp.Marchands_amp.query.filter_by(id_amp=id_ampl).all())
        nb_participants = len(participants_amp.Participants_amp.query.filter_by(id_amp=id_ampl,valide=1).all())
        current_user.points+=score_course(nb_marchands,nb_participants)
        db.session.commit()
        # le commit c'est pas pris en compte quand j'arrive sur la route depuis accepter
        return commande()
    else:
        return render_template('info.html', user=current_user, msg="Vous n'avez pas l'autorisation de fermer cette Amplet ou elle n'existe pas", retour="/commande")
