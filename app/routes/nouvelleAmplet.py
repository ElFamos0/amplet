from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request

@app.route('/nouvelleAmplet', methods=['GET','POST'])
@login_required
def nouvelleAmplet():
    mag_dispo=marchands.Marchands.query.all()
    mag_dispo_noms=[e.nom for e in mag_dispo]
    mag_choisis_id=[]
    if request.method=='POST':
        L=request.form
        for e in L:
            mag_choisis_id.append(e)
        print(L)
    return render_template('nouvelleAmplet.html', mag_dispo=mag_dispo, mag_dispo_noms=mag_dispo_noms,user=current_user)