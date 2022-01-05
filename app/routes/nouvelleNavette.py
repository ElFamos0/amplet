from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request
from datetime import date, datetime
from time import mktime
from utils.timestamp import now

@app.route('/nouvelleNavette', methods=['GET','POST'])
@login_required
def nouvelleNavette():
    mag_dispo=marchands.Marchands.query.all()
    mag_dispo_noms=[e.nom for e in mag_dispo]
    mag_choisis_id=[]
    date_now = now()
    if request.method=='POST':
        L=request.form
        for e in L:
            if e=="dist_max":
                break
            mag_choisis_id.append(e)
        print("\n\n\n")
        print(L)
        print("\n\n\n")
        dist_max = L['dist_max']
        date_dep = L['date_depart']
        heure_dep = L['heure_depart']
        if date_dep=="":
            date_dep=now()
            date_dep_ts=date_dep + (int(heure_dep)*60*60*1000)
        else:
            date_dep_ts = int(mktime(datetime.strptime(date_dep,"%Y-%m-%d").timetuple()) * 1000) + ((int(heure_dep)+1)*60*60*1000)
        delai_ferm = int(L['delai_ferm'])*60*60*1000
        places_dispo = L['places_dispo']
        newAmp = amplet.Amplets(id_coursier=current_user.id, navette=0, date_depart=date_dep_ts, date_arrivee=date_dep_ts+1, places_dispo=places_dispo, delai_fermeture_depart=delai_ferm, ferme=0)
        db.session.add(newAmp)
        for e in mag_choisis_id:
            db.session.add(marchands_amp.Marchands_amp(id_marchand=str(e),id_amp=newAmp.id))
        db.session.commit()
    return render_template('nouvelleNavette.html', mag_dispo=mag_dispo, mag_dispo_noms=mag_dispo_noms,user=current_user)
