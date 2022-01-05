from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, abort
from utils.timestamp import now
from utils.vote_marchand import vote
from utils.update_multiplicateur import update_multiplicateur

##############################
######## VOTE ADMIN  #########
##############################


@app.route('/admin/navettes', methods=['GET'])
@login_required
def admin_votes():
    if not current_user.is_Mayor():
        abort(404)
    navettes = amplet.Amplets.query.filter_by(id_coursier=current_user.id, ferme=False, navette=True)
    return render_template('admin/navettes.html', user=current_user, navettes=navettes)

@app.route('/admin/navettes/<string:id>/lance', methods=['GET'])
@login_required
def lance_navette(id):
    if not current_user.is_Mayor():
        abort(404)
    navette = amplet.Amplets.query.get(id)
    if navette.ferme:
        return render_template('info.html', user=current_user, msg="Cette navette est déjà fermé.", retour="/admin/navettes")
    if navette.date_arrivee < now():
        return render_template('info.html', user=current_user, msg="Cette navette est déjà arrivé.", retour="/admin/navettes")

    liste_marchand, dic_marchand = vote(id)
    print(liste_marchand, dic_marchand)
    update_multiplicateur(liste_marchand, dic_marchand)
    navette.ferme = True
    db.session.commit()
    return render_template('info.html', user=current_user, msg="Le vote à été lancé !", retour="/admin/navettes")