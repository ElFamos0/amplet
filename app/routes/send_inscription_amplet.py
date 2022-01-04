from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request,redirect
from datetime import date, datetime
from time import mktime
from utils.timestamp import now, timestamp_to_date
from utils.recherche_par import recherche_par
from utils.amplets_a_afficher import amplets_a_afficher, amplet_dict

@app.route('/send_inscription_amplet', methods=['POST'])
@login_required
def send_inscription_amplet() :

    ampl = request.form.get("amp_id")
    am = amplet_dict(ampl)
    mag = marchands.Marchands.query.add_entity(marchands_amp.Marchands_amp).join(marchands_amp.Marchands_amp).filter(marchands_amp.Marchands_amp.id_amp == ampl,marchands_amp.Marchands_amp.id_marchand==marchands.Marchands.id)
        
    liste_mag = [m[0].id for m in mag]
    listeproduits = []
    listeprix = []
    for id_mag in liste_mag :
        prod = produits.Produits.query.add_entity(marchands.Marchands).join(marchands.Marchands).filter(marchands.Marchands.id == id_mag,produits.Produits.id_marchand == marchands.Marchands.id)
        listeprix += [p[0].prix for p in prod]
        listeproduits += [p[0].nom for p in prod]

    items = []
    for i in range(0,5):
        items.append({
                "produit": request.form.get(f"produit{i}"),
                "quantite": request.form.get(f"quantite{i}"),
                "unite": request.form.get(f"unite{i}"),
                })  
        #Cette partie ci-dessous me permet de faire toute les comparaisons nécessaire au bon fonctionnement du form
    participation_valide = participants_amp.Participants_amp.query.filter_by(id_amp=ampl,id_user=current_user.id).first() is not None #afin que le form ne comptabilise qu'une seule participation à une amplet
    listeverif = []
    
    for item in items:      
        if item["produit"] != "null":
            listeverif.append(item["produit"])
    allgood = not len(set(listeverif))!=len(listeverif)
    if participation_valide or not allgood :
        return render_template('inscription_amplet.html',user=current_user,produits=listeproduits,amp = am,prix = listeprix,noproblem = allgood,ampid=ampl,dejainsc= participation_valide)

    if allgood and not participation_valide:
        for item in items:
            if item["produit"] not in listeproduits or 0 > int(item["quantite"]) > 40 or item["quantite"]=="":
                continue
            idproduit = produits.Produits.query.filter(produits.Produits.nom==item["produit"]).first()
            produit = produits_amp.Produits_amp(id_amp=ampl,id_produit=idproduit.id,quantite=int(item["quantite"]),unite=item["unite"],id_user=current_user.id)
            if participation_valide == False: #afin que le form ne comptabilise qu'une seule participation à une amplet
                participation = participants_amp.Participants_amp(id_amp=ampl,id_user=current_user.id,valide= 0)
                db.session.add(participation)
                participation_valide = True
            db.session.add(produit)
            db.session.commit()


    return redirect("/succes")