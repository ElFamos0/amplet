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

##############################
########### AMPLETS  ###########
##############################

@app.route('/amplets_en_cours', methods=['GET','POST'])
@login_required
def amplets_en_cours() :

    march = marchands.Marchands.query.all()
    recherche = ['Proximité','Date de début']
    d2 = date.today().strftime("%Y-%m-%d")

    liste_type = []
    liste_mag =  []
    for m in march :
        liste_mag.append(m.nom)
        if m.type not in liste_type :
            liste_type.append(m.type)
    
    if request.method == "POST" :

        debut = request.form.get('mindate',d2)
        if debut == "" :
            debut = d2
        fin = request.form.get('maxdate',d2)
        if fin == "" :
            fin = d2
        
        recherche_actuelle = request.form.get('recherche','Proximité')
        i = 0
        for j in range(len(recherche)) :
            if recherche[j] == recherche_actuelle :
                i = j
        recherche[0],recherche[i] = recherche[i],recherche[0]
        liste_typebis = []
        for i in liste_type :
            val = request.form.get(i,'off')
            if val == 'on' :
                liste_typebis.append((i,True))
            else :
                liste_typebis.append((i,False))
    else :
        debut = d2
        fin = d2
        liste_typebis = []
        for i in liste_type :
            liste_typebis.append((i,False))

    
    debut_stamp = mktime(datetime.strptime(debut,"%Y-%m-%d").timetuple()) * 1000 # On convertit en timestamp
    fin_stamp = mktime(datetime.strptime(fin,"%Y-%m-%d").timetuple()) * 1000 # On convertit en timestamp

    liste_amplet= amplets_a_afficher(debut_stamp,fin_stamp,liste_typebis)

    if recherche[0] == 'Proximité' :

        id_adresse =  users.User.query.get(current_user.id).id_adresse

    else :
        id_adresse = 0

    liste_amplet = recherche_par(liste_amplet,recherche[0],id_adresse)
  
    return render_template('amplets_en_cours.html',user=current_user,type_magasins = liste_typebis,debut = debut,fin = fin,recherche = recherche,amplets=liste_amplet)