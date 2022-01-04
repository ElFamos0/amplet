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

@app.route('/inscription_amplet', methods=['GET','POST'])
@login_required
def inscription_amplet() :
    

    if request.method=='POST':
        ampl = request.form.get("amp_id")
        am = amplet_dict(ampl)
        if request.form.get('err') is None :
            allgood = True
        else :
            allgood = request.form.get('err')

        mag = marchands.Marchands.query.add_entity(marchands_amp.Marchands_amp).join(marchands_amp.Marchands_amp).filter(marchands_amp.Marchands_amp.id_amp == ampl,marchands_amp.Marchands_amp.id_marchand==marchands.Marchands.id)
        
        liste_mag = [m[0].id for m in mag]
        listeproduits = []
        listeprix = []
        for id_mag in liste_mag :
            prod = produits.Produits.query.add_entity(marchands.Marchands).join(marchands.Marchands).filter(marchands.Marchands.id == id_mag,produits.Produits.id_marchand == marchands.Marchands.id)
            listeprix += [p[0].prix for p in prod]
            listeproduits += [p[0].nom for p in prod]
        
        participation_valide = participants_amp.Participants_amp.query.filter_by(id_amp=ampl,id_user=current_user.id).first() is not None
    if request.method == "GET" :
        return render_template("index.html")
    
    return render_template('inscription_amplet.html',user=current_user,produits=listeproduits,amp = am,prix = listeprix,noproblem = allgood,ampid = ampl,dejainsc= participation_valide)
 