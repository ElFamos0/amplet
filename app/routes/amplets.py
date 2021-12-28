from db import *
from models import *
from flask_login import login_required
from flask import render_template, request
from datetime import date, datetime
from time import mktime

##############################
########### AMPLETS  ###########
##############################

@app.route('/nouvelleAmplet', methods=['GET','POST'])
@login_required
def nouvelleAmplet():
    mag_dispo=['primeur du coin', 'chez Tony', 'vendeur de foutre']
    mag_visit=[]
    # if request.method=='POST':
    #     L=request.form
    #     for e in mag_dispo:
    #         if e in L:
    #             mag_visit.append(e)
    #     return mag_visit[1]
    return render_template('nouvelleAmplet.html', magasins=mag_dispo)

@app.route('/amplets_en_cours', methods=['GET','POST'])

def amplets_en_cours() :
    liste_mag =  ['Primeur','Garagiste','Boucher']
    #A refaire avec une requete sql

    recherche = ['Proximité','Date de début','Date de fin','Type de magasins']
    d2 = date.today().strftime("%Y-%m-%d")
    if request.method == "POST" :
        debut = request.form.get('mindate',d2)
        fin = request.form.get('maxdate',d2)
        debut = mktime(datetime.strptime(debut,"%Y-%m-%d").timetuple()) * 1000 # On convertis en timestamp
        fin = mktime(datetime.strptime(fin,"%Y-%m-%d").timetuple()) * 1000 # On convertis en timestamp
        recherche_actuelle = request.form.get('recherche','Proximité')
        i = 0
        for j in range(4) :
            if recherche[j] == recherche_actuelle :
                i = j
        recherche[0],recherche[i] = recherche[i],recherche[0]
        liste_magbis = []
        for i in liste_mag :
            val = request.form.get(i,'off')
            if val == 'on' :
                liste_magbis.append((i,True))
            else :
                liste_magbis.append((i,False))
    else :
        debut = d2
        fin = d2
        liste_magbis = []
        for i in liste_mag :
            liste_magbis.append((i,True))
    return render_template('amplets_en_cours.html',magasins = liste_magbis,debut = debut,fin = fin,recherche = recherche)