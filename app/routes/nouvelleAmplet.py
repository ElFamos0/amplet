from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request
from datetime import date, datetime
from time import mktime
from utils.timestamp import now, timestamp_to_date
from utils.recherche_par import recherche_par
from utils.amplets_a_afficher import amplets_a_afficher, amplet_dict

@app.route('/nouvelleAmplet', methods=['GET','POST'])
@login_required
def nouvelleAmplet():
    mag_dispo=['primeur du coin', 'chez Tony']
    mag_visit=[]
    if request.method=='POST':
        L=request.form
        for e in mag_dispo:
            if e in L:
                mag_visit.append(e)
        return mag_visit[1]
    return render_template('nouvelleAmplet.html', magasins=mag_dispo)