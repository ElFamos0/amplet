from db import *
from models import *
from flask_login import current_user, login_required
from flask import render_template

##############################
########### NAVETTE ##########
##############################

@app.route("/navette", methods=['GET','POST'])
@login_required
def navette():
    L = {'username':str(current_user.username),'mail':str(current_user.email),'id':str(current_user.id)}
    listeproduits = []
    listenavettes = []
    for produit in produits.Produits.query.all():
        listeproduits.append(produit.nom)
    for navette in amplet.Amplets.query.filter(amplet.Amplets.navette==True).all():
        listenavettes.append([navette.date_depart,navette.date_arrivee])
    if request.method=='POST':
        items = []
        for i in range(0,5):
            items.append({
                    "produit": request.form.get(f"produit{i}"),
                    "quantite": request.form.get(f"quantite{i}"),
                    "unite": request.form.get(f"unite{i}"),
                    })
        for item in items:
            if item["produit"] not in listeproduits or 0 >= int(item["quantite"]) > 40:
                continue
            idproduit = produits.Produits.query.filter(produits.Produits.nom==item["produit"]).first()
            produit = produits_amp.Produits_amp(id_amp=57,id_produit=idproduit.id,quantite=int(item["quantite"]),unite=item["unite"],user_id=0)
            db.session.add(produit)
            db.session.commit()
        return "Commande effectué"
    return render_template("navette.html",personne=L,produits=listeproduits,optionnavette=listenavettes)