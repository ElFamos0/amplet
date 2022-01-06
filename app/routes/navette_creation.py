from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request, flash, abort
from datetime import date, datetime
from time import mktime
from utils.timestamp import now
from utils.cast import conversion
from utils.creation_navette import lance_vote_automatique

@app.route('/nouvelleNavette', methods=['GET','POST'])
@login_required
def nouvelleNavette():
    if not current_user.is_Mayor():
        abort(404)
    mag_dispo=marchands.Marchands.query.all()
    d2 = date.today().strftime("%Y-%m-%d")
    if request.method=='POST':
        rayon = 40100
        marchands_choisis = request.form.getlist('marchands[]')
        datedebut = request.form.get("startdate", d2) or d2
        heuredebut = request.form.get("starthour")+1
        datefin = request.form.get("enddate", d2) or d2
        heurefin = request.form.get("endhour")+1
        delai = conversion(request.form.get("delai"), int, 2)
        places = 100

        debut_stamp = mktime(datetime.strptime(datedebut,"%Y-%m-%d").timetuple()) * 1000 + conversion(heuredebut, int, 0)*60*60*1000
        fin_stamp = mktime(datetime.strptime(datefin,"%Y-%m-%d").timetuple()) * 1000 + conversion(heurefin, int, 0)*60*60*1000

        print(debut_stamp, now(), fin_stamp)

        error = False
        if debut_stamp < now():
            error = True
            flash("L'amplet ne peut pas débuter avant maintenant.")

        if fin_stamp < now():
            error = True
            flash("L'amplet ne peut pas se terminer avant maintenant.")

        if fin_stamp <= debut_stamp+3*60*60*1000: # Minimum 3h
            error = True
            flash("Les votes pour la navette doivent se terminer au moins 3h après le début d'une Amplet.")

        if fin_stamp > debut_stamp+7*24*60*60*1000:
            error = True
            flash("La navette ne doit pas durer plus d'une semaine.")

        if not heuredebut or not heurefin:
            error = True
            flash("Veuillez renseigner l'heure de début et/ou l'heure de fin.")

        if not delai or fin_stamp-delai*60*60*1000 < debut_stamp or delai < 1:
            error = True
            flash("Veuillez renseigner le délai d'avant départ.")

        if len(marchands_choisis) == 0:
            error = True
            flash("Veuillez sélectionner au moins un marchand.")

        if not error:
            nouvelle_navette = amplet.Amplets(id_coursier=current_user.id\
            ,navette=True
            ,date_depart=debut_stamp\
            ,date_arrivee=fin_stamp\
            ,places_dispo=places\
            ,delai_fermeture_depart=delai\
            ,ferme=0\
            ,dist_max=rayon)
            db.session.add(nouvelle_navette)
            for e in marchands_choisis:
                db.session.add(marchands_amp.Marchands_amp(id_marchand=str(e),id_amp=nouvelle_navette.id))
            db.session.commit()
            #lance_vote_automatique(nouvelle_navette.id)
            return render_template('info.html', user=current_user, msg="Vous avez créé votre nouvelle Navette !", retour="/")

    return render_template('navette/nouvelleNavette.html', mag_dispo=mag_dispo, user=current_user)