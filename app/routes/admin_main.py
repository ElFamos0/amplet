from db import *
from models import *
from utils import timestamp

##############################
########### ADMIN  ###########
##############################

@app.route("/dashboard")
def hello_world():
    content = "<p>UTILISATEURS</p>"
    content += "<br/>"
    for user in users.User.query.all():
        content += f"ID USER : {user.id} - USERNAME : {user.username} - EMAIL: {user.email}"
        content += "<br/>"
    content += "<br>"
    content += "<p>AMPLET</p>"
    content += "<br/>"
    for amplit in amplet.Amplets.query.all():
        content += f"ID AMPLET : {amplit.id} - DATE DEPART : {timestamp.timestamp_to_date(amplit.date_depart,format=True)} - DATE ARRIVE : {timestamp.timestamp_to_date(amplit.date_arrivee,format=True)} - PLACES DISPO (MAX) : {amplit.places_dispo} - ID COURSIER : {amplit.id_coursier}"
        content += "<br/>"
    content += "<br>"
    content += "<p>COMMANDES</p>"
    content += "<br/>"
    for produit_amp in produits_amp.Produits_amp.query.all():
        requete1 = users.User.query.filter(users.User.id==produit_amp.id_user).first()
        requete2 = produits.Produits.query.filter(produits.Produits.id == produit_amp.id_produit).first()
        content += f"ID AMPLET : {produit_amp.id_amp} - PRODUIT : {requete2.nom} - QUANTITE : {produit_amp.quantite} - UNITE : {produit_amp.unite} - USERNAME : {requete1.username}"
        content += "<br/>"
    content += "<br>"
    content += "<p>PARTICIPANTS</p>"
    content += "<br/>"
    for participant in participants_amp.Participants_amp.query.all():
        requete1 = users.User.query.filter(users.User.id==participant.id_user).first()
        content += f"ID AMPLET : {participant.id_amp} - USERNAME : {requete1.username}"
        content += "<br/>"
    content += "<br>"
    content += "<p>MARCHANDS</p>"
    content += "<br/>"
    for marchand in marchands.Marchands.query.all():
        content += f"ID MARCHAND : {marchand.id} - NOM : {marchand.nom} - TYPE MARCHAND : {marchand.type}"
        content += "<br/>"
    #print(vote_marchand.vote("6884214503899140099"))
    return content