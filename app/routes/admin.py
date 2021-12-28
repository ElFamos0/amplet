from db import *
from models import *
from flask_login import login_required, current_user
from flask import render_template, request

##############################
########### ADMIN  ###########
##############################

@app.route("/dashboard")
def hello_world():
    content = "<p>UTILISATEURS</p>"
    content += "<br/>"
    for user in users.User.query.all():
        content += f"{user.id} - {user.username} & {user.email}"
        content += "<br/>"
    content += "<br>"
    content += "<p>AMPLET</p>"
    content += "<br/>"
    for amplit in amplet.Amplets.query.all():
        content += f"{amplit.id} - {amplit.date_depart} - {amplit.date_arrivee} - {amplit.places_dispo} - {amplit.id_coursier}"
        content += "<br/>"
    content += "<br>"
    content += "<p>COMMANDES</p>"
    content += "<br/>"
    for produit_amp in produits_amp.Produits_amp.query.all():
        content += f"{produit_amp.id_amp} - {produit_amp.id_produit} - {produit_amp.quantite} - {produit_amp.unite}"
        content += "<br/>"
    return content

@app.route("/admin", methods=['GET','POST'])
@login_required
def adminpage():
    if current_user.username == "admin":
        if request.method=='POST':
            dateD = request.form.get("dateD")
            dateA = request.form.get("dateA")
            navamplet = amplet.Amplets(navette=True,date_depart=dateD,date_arrivee=dateA,places_dispo=5,id_coursier=87)
            db.session.add(navamplet)
            db.session.commit()
            return render_template("admin.html")
        return render_template("admin.html")
    else:
        return "404"