from sqlalchemy.sql.expression import and_
from utils.cast import conversion
from db import *
from models import *
from flask_login import current_user, login_required
from flask import render_template, redirect, flash

##############################
########### NAVETTE ##########
##############################

@app.route("/navette", methods=['GET'])
@login_required
def navette_main():
    listenavettes = amplet.Amplets.query.filter_by(navette=True, ferme=False).all()
    for i in range(len(listenavettes)-1,-1,-1):# on gère l'affichage des amplets de type navette disponibles pour chaque utilisateurs
        navette = listenavettes[i]
        count = produits_amp.Produits_amp.query.filter_by(id_amp=navette.id, id_user=current_user.id).count()
        if count > 0: #on vérifie que il y a au moins une navette disponible
            listenavettes.pop(i)
    if listenavettes == []:
        return render_template("info.html",user=current_user, msg = "Il n'y a pas de navette disponible pour le moment !", retour="/")
    return redirect(f"/navette/{listenavettes[0].id}")

@app.route("/navette/<string:navid>", methods=['GET','POST'])
@login_required
def navette(navid):
    listenavettes = amplet.Amplets.query.filter_by(navette=True, ferme=False).all()
    for i in range(len(listenavettes)-1,-1,-1):# on gère l'affichage des amplets de type navette disponibles pour chaque utilisateurs
        navette = listenavettes[i]
        count = produits_amp.Produits_amp.query.filter_by(id_amp=navette.id, id_user=current_user.id).count()
        if count > 0: #on vérifie que il y a au moins une navette disponible
            listenavettes.pop(i)
    if listenavettes == []:
        return render_template("erreur.html", user=current_user, erreur = "Il n'y a pas de navette disponible pour le moment !")
    if navid not in [n.id for n in listenavettes]:
        return redirect(f"/navette/{listenavettes[0].id}")

    listeproduits = marchands_amp\
        .Marchands_amp\
        .query\
        .filter_by(id_amp=navid)\
        .add_entity(produits.Produits)\
        .join(produits.Produits, produits.Produits.id_marchand==marchands_amp.Marchands_amp.id_marchand)\
        .group_by(produits.Produits.nom)\
        .order_by(produits.Produits.nom)\
        .all()
    allgood = True
    if request.method=='POST':
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
        participation_valide = not participants_amp.Participants_amp.query.filter_by(id_amp=navette.id,id_user=current_user.id).first() is not None #afin que le form ne comptabilise qu'une seule participation à une amplet
        allgood = True
        listeverif = []
        
        for item in items:      
            if item["produit"] != "null":
                listeverif.append(item["produit"])
        allgood = len(set(listeverif)) == len(listeverif) and len(listeverif) > 0
        if allgood: #si il n'y pas d'erreur on ajoute item après item 
            for item in items: #vérifie si les valeurs entrés ne dépassent pas certaines valeurs
                produit, qte, unite = item["produit"], conversion(item["quantite"], int, 0), item["unite"]
                skip = True
                for p in listeproduits:
                    if produit == p[1].id:
                        skip = False
                        produit = p[1].nom
                        break
                if skip:
                    continue

                if unite == "kg" and 0 > qte > 10:
                    continue
                if unite == "g" and 0 > qte > 10000:
                    continue
                if unite == "unite" and qte > 0:
                    continue
                
                Lproduits = produits.Produits.query.filter(produits.Produits.nom==produit).all()
                for produit in Lproduits:
                    produit_amp = produits_amp.Produits_amp(id_amp=navette.id,id_produit=produit.id,quantite=qte,unite=unite,id_user=current_user.id)
                    db.session.add(produit_amp)
                if participation_valide: # afin que le form ne comptabilise qu'une seule participation à une amplet
                    participation = participants_amp.Participants_amp(id_amp=navette.id,id_user=current_user.id,valide=0)
                    db.session.add(participation)
                    participation_valide = False
            db.session.commit()
            return render_template("info.html", user=current_user,msg="Votre vote pour la navette a été pris en compte merci de regarder le statut de votre commande dans Mes Amplets", retour="/")
        else:
            if len(listeverif) > 0:
                flash("Merci de ne pas mettre plus d'une fois le même article.")
            else:
                flash("Merci de renseigner au moins un article.")

    return render_template("navette.html",user=current_user, produits=listeproduits, navettes=listenavettes, navid=navid) #chargement de la page