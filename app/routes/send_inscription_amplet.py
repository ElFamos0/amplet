from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request, redirect, flash
from utils.amplets_a_afficher import amplet_dict
from utils.cast import conversion

@app.route('/si/<string:id>', methods=['POST'])
@login_required
def send_inscription_amplet(id) :

    ampl = id
    am = amplet_dict(ampl)
    mag = marchands.Marchands.query.add_entity(marchands_amp.Marchands_amp).join(marchands_amp.Marchands_amp).filter(marchands_amp.Marchands_amp.id_amp == ampl,marchands_amp.Marchands_amp.id_marchand==marchands.Marchands.id)
        
    liste_mag = [m[0].id for m in mag]
    listeproduits = []
    for id_mag in liste_mag :
        prod = produits.Produits.query.add_entity(marchands.Marchands).join(marchands.Marchands).filter(marchands.Marchands.id == id_mag,produits.Produits.id_marchand == marchands.Marchands.id)
        listeproduits += [{"nom":p[0].nom, "marchand": p[1].nom} for p in prod]

    items = []
    for i in range(0,5):
        items.append({
                "produit": request.form.get(f"produit{i}"),
                "quantite": request.form.get(f"quantite{i}"),
                "unite": request.form.get(f"unite{i}"),
                })  
        #Cette partie ci-dessous me permet de faire toute les comparaisons nécessaire au bon fonctionnement du form
    participation_valide = participants_amp.Participants_amp.query.filter(participants_amp.Participants_amp.id_amp==ampl,participants_amp.Participants_amp.id_user==current_user.id).first() is None #afin que le form ne comptabilise qu'une seule participation à une amplet
    listeverif = []
    print(current_user)
    mon_amplet = amplet.Amplets.query.filter(amplet.Amplets.id==ampl).first().id_coursier == current_user.id
    
    for item in items:      
        if item["produit"] != "null":
            if item["quantite"].isdigit() and int(item["quantite"]) > 0 :
                listeverif.append(item["produit"])
    allgood1 = len(set(listeverif)) == len(listeverif)
    allgood2 = len(listeverif) > 0
    allgood = allgood1 and allgood2

    if mon_amplet :
        flash("Vous ne pouvez pas vous inscrire sur votre amplet !")
        return render_template('inscription_amplet.html', user=current_user, produits=listeproduits, amp = am)
    if not participation_valide:
        flash("Vous vous êtes déjà inscrit à cet amplet !")
        return render_template('inscription_amplet.html', user=current_user, produits=listeproduits, amp = am)
    if not allgood1:
        flash("Merci de ne pas mettre plus d'une fois le même article.")
        return render_template('inscription_amplet.html', user=current_user, produits=listeproduits, amp = am)
    if not allgood2:
        flash("Merci de mettre au moins un article.")
        return render_template('inscription_amplet.html', user=current_user, produits=listeproduits, amp = am)
    
    if allgood and participation_valide:
        for item in items:
            produit, qte, unite = item["produit"], conversion(item["quantite"], int, 0), item["unite"]
            skip = True
            for p in listeproduits:
                if produit == p["nom"]:
                    skip = False
                    break
            if skip:
                continue

            if unite == "kg" and (0 >= qte or qte > 10):
                continue
            if unite == "g" and (0 >= qte or qte > 10000):
                continue
            if unite == "unite" and qte <= 0:
                continue
            
            print(conversion(item["quantite"], int, 0))
            idproduit = produits.Produits.query.filter(produits.Produits.nom==produit).first()
            produit = produits_amp.Produits_amp(id_amp=ampl, id_produit=idproduit.id, quantite=qte, unite=unite, id_user=current_user.id)
            if participation_valide: #afin que le form ne comptabilise qu'une seule participation à une amplet
                participation = participants_amp.Participants_amp(id_amp=ampl,id_user=current_user.id,valide= 0)
                db.session.add(participation)
                participation_valide = False
            db.session.add(produit)
        db.session.commit()

    return render_template('info.html', user=current_user, msg="Vous avez bien été inscris !", retour="/amplets_en_cours")