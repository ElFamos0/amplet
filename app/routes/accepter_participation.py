from flask_login.utils import login_required
from db import *
from models import *
from flask_login import current_user
from flask import render_template
from routes.commande import commande

@app.route('/a/<string:id_ampl>/<string:id_part>')
@login_required
def accepter_participation(id_ampl,id_part):
    curr_amp = participants_amp.Participants_amp.query.filter_by(id_user = id_part, id_amp=id_ampl).first()
    curr_amp_id = curr_amp.id_amp
    amp = amplet.Amplets.query.filter_by(id = curr_amp_id).first()
    cours_id = amp.id_coursier
    if curr_amp and current_user.id==cours_id:
        curr_amp.valide=1
        db.session.commit()
        return commande()
    else:
        return render_template('info.html', user=current_user, msg="Vous n'avez pas l'autorisation de modifier le statut de cette Amplet ou elle n'existe pas", retour="/commande")
