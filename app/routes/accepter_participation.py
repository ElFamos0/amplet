from flask_login.utils import login_required
from models.users import User
from db import *
from models import *
from flask_login import current_user
from flask import render_template
from routes.commande import commande

@app.route('/a/<string:id_ampl>/<string:id_part>')
@login_required
def accepter_participation(id_ampl,id_part):
    curr_amp = participants_amp.Participants_amp.query.filter_by(id_user = id_part, id_amp=id_ampl).first()
    if curr_amp:
        curr_amp.valide=1
        db.session.commit()
        return commande()
    else:
        return render_template('erreur.html', erreur="Vous n'avez pas l'autorisation de modifier le status de cette Amplet ou elle n'existe pas",user=current_user)