from db import *
from models import *
from flask_login import login_required, current_user
from flask import render_template, request, abort, flash, redirect
from utils.cast import conversion

##############################
########### ADMIN  ###########
##############################

@app.route("/admin/creer_marchand", methods=['GET', 'POST'])
@login_required
def creer_marchand():
    if not current_user.is_Mayor() and not current_user.is_Admin():
        abort(404)

    if request.method=='POST':
        nom = request.form.get("nom")
        numero = conversion(request.form.get("numero"), int)
        rue = request.form.get("rue")
        ville = request.form.get("ville")
        codepostal = conversion(request.form.get("codepostal"), int)
        mtype = request.form.get("type")

        erreur = False

        if not nom:
            erreur = True
            flash("Veuillez remplir le champs nom.")

        if not numero:
            erreur = True
            flash("Veuillez remplir le champs numéro.")

        if not rue:
            erreur = True
            flash("Veuillez remplir le champs rue.")

        if not ville:
            erreur = True
            flash("Veuillez remplir le champs ville.")

        if not codepostal:
            erreur = True
            flash("Veuillez remplir le champs code postal.")

        if not mtype:
            erreur = True
            flash("Veuillez remplir le champs type.")

        if not marchands.Marchands.query.filter_by(nom=nom).first() and not erreur:
            adr = adresses.Adresse(numero, rue, ville, codepostal)
            marchand = marchands.Marchands(nom, adr.id, mtype)
            db.session.add(adr)
            db.session.add(marchand)
            db.session.commit()
            return render_template("infos.html", user=current_user, msg="Vous avez créé ce marchand !", retour="admin/creer_marchand")

    return render_template("admin/creermarchand.html", user=current_user)


@app.route("/admin/ajout_produit_marchand", methods=['GET'])
@login_required
def ajout_produit_marchand_main():
    if not current_user.is_Mayor() and not current_user.is_Admin():
        abort(404)
    lmarchand = marchands.Marchands.query.all()

    if len(lmarchand) == 0:
        return render_template("info.html",user=current_user, msg = "Il n'y a pas de marchands disponible pour le moment !", retour="/")
    return redirect(f"/admin/ajout_produit_marchand/{lmarchand[0].id}")


@app.route("/admin/ajout_produit_marchand/<string:mid>", methods=['GET','POST'])
@login_required
def ajout_produit_marchand(mid):
    if not current_user.is_Mayor() and not current_user.is_Admin():
        abort(404)
    lmarchand = marchands.Marchands.query.all()

    if len(lmarchand) == 0:
        return render_template("info.html",user=current_user, msg = "Il n'y a pas de marchands disponible pour le moment !", retour="/")
    if mid not in [n.id for n in lmarchand]:
        return redirect(f"/admin/ajout_produit_marchand/{lmarchand[0].id}")


    if request.method=='POST':
        nom = request.form.get("nom")
        prix = conversion(request.form.get("prix"), int)
        erreur = False

        if not nom:
            erreur = True
            flash("Veuillez remplir le champs nom.")

        if not prix or prix < 0:
            erreur = True
            flash("Veuillez remplir le champs prix.")

        if not erreur:
            produit = produits.Produits(mid, nom, prix)
            db.session.add(produit)
            db.session.commit()
            render_template(f"info.html", user=current_user, msg="Vous avez créer un nouveau produit !", retour=f"/admin/ajout_produit_marchand/{mid}")

    return render_template(f"/admin/ajoutproduit.html", user=current_user, marchands=lmarchand, mid=mid)
