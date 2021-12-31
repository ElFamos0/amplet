from sqlalchemy.sql.expression import and_
from db import *
from models import *
from flask_login import current_user, login_required
from flask import render_template,flash,redirect,url_for
from utils import timestamp
from sqlalchemy import and_

##############################
########### NAVETTE ##########
##############################

@app.route("/navette", methods=['GET','POST'])
@login_required
def navette():
    listeproduits = [p.nom for p in produits.Produits.query.with_entities(produits.Produits.nom).all()]
    allgood = True
    if request.method=='POST':
        navid = request.form.get("navette")
        navette = amplet.Amplets.query.filter_by(id=navid,navette=True, ferme=False).first()
        if navette == None:
            return "Il n'y a pas de navette"
        items = []
        for i in range(0,5):
            items.append({
                    "produit": request.form.get(f"produit{i}"),
                    "quantite": request.form.get(f"quantite{i}"),
                    "unite": request.form.get(f"unite{i}"),
                    })  
        #Cette partie ci-dessous me permet de faire toute les comparaisons nécessaire au bon fonctionnement du form
        participation_valide = False
        listeverif = []
        allgood = True
        for item in items:      
            if item["produit"] != "":
                listeverif.append(item["produit"])
        if len(set(listeverif))!=len(listeverif):
            allgood = False
        if allgood:
            for item in items:
                if item["produit"] not in listeproduits or 0 >= int(item["quantite"]) > 40 or item["quantite"]=="":
                    continue
                idproduit = produits.Produits.query.filter(produits.Produits.nom==item["produit"]).first()
                produit = produits_amp.Produits_amp(id_amp=navette.id,id_produit=idproduit.id,quantite=int(item["quantite"]),unite=item["unite"],id_user=current_user.id)
                if participation_valide == False: #afin que le form ne comptabilise qu'une seule participation à une amplet
                    participation = participants_amp.Participants_amp(id_amp=navette.id,id_user=current_user.id)
                    db.session.add(participation)
                    participation_valide = True
                db.session.add(produit)
                db.session.commit()

    listenavettes = amplet.Amplets.query.filter_by(navette=True, ferme=False).all()
    for i in range(len(listenavettes)-1,-1,-1):
        navette = listenavettes[i]
        count = produits_amp.Produits_amp.query.filter_by(id_amp=navette.id, id_user=current_user.id).count()
        if count > 0: 
            listenavettes.pop(i)
    if listenavettes == []:
        return "Il n'y a pas de navettes disponible merci de revenir ultérieurement"
    
    return render_template("navette.html",user=current_user,produits=listeproduits,navettes=listenavettes,noproblem=allgood)