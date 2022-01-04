from sqlalchemy.sql.expression import and_
from utils.cast import conversion
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
        for i in range(0,5):#on rempli une liste de dictionnaire avec chaque produits choisis
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
            if item["produit"] != "null":
                listeverif.append(item["produit"])
        if len(set(listeverif))!=len(listeverif):
            allgood = False
        if allgood: #si il n'y pas d'erreur on ajoute item après item 
            for item in items: #vérifie si les valeurs entrés ne dépassent pas certaines valeurs
                produit, qte, unite = item["produit"], conversion(item["quantite"], int, 0), item["unite"]

                if produit not in listeproduits:
                    print("1")
                    continue
                if 0 > qte > 40 :
                    print("2")
                    continue
                
                idproduit = produits.Produits.query.filter(produits.Produits.nom==produit).first()
                produit = produits_amp.Produits_amp(id_amp=navette.id,id_produit=idproduit.id,quantite=qte,unite=unite,id_user=current_user.id)
                if participation_valide == False: # afin que le form ne comptabilise qu'une seule participation à une amplet
                    participation = participants_amp.Participants_amp(id_amp=navette.id,id_user=current_user.id,valide=1)
                    db.session.add(participation)
                    participation_valide = True
                db.session.add(produit)
            db.session.commit()
            print("comited")
            return render_template("succes.html", user=current_user,succesnavette=True)

    listenavettes = amplet.Amplets.query.filter_by(navette=True, ferme=False).all()
    for i in range(len(listenavettes)-1,-1,-1):# on gère l'affichage des amplets de type navette disponibles pour chaque utilisateurs
        navette = listenavettes[i]
        count = produits_amp.Produits_amp.query.filter_by(id_amp=navette.id, id_user=current_user.id).count()
        if count > 0: #on vérifie que il y a au moins une navette disponible
            listenavettes.pop(i)
    if listenavettes == []:
        return render_template("erreur.html",user=current_user,erreur = "Il n'y a pas de navette disponible pour le moment !")
    return render_template("navette.html",user=current_user,produits=listeproduits,navettes=listenavettes,noproblem=allgood) #chargement de la page