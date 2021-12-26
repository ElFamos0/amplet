from re import M
from flask import render_template, request, url_for
from flask_login import LoginManager, login_required, current_user
from datetime import date
import os

# Setup ####################################
setup = False
if not os.path.isfile("data/db.db"):
    os.open("data/db.db", os.O_CREAT)
    setup = True
############################################

from db import *
from models import *
        
db.create_all() # Creates the tables if necessary

# Setup ####################################
if setup:
    admin = users.User(username='admin', email='admin@test.com', code_postal=57000)
    guest = users.User(username='guest', email='guest@test.com', code_postal=57000)
    third = users.User(username='third', email='third@test.com', code_postal=57000)
    amplet1 = amplet.Amplets(navette=False,date_depart="18h50-28/12/2021",date_arrivee="19h50-28/12/2021",places_dispo=5,id_coursier=2)
    amplet2 = amplet.Amplets(navette=True,date_depart="18h50-29/12/2021",date_arrivee="19h50-30/12/2021",places_dispo=5,id_coursier=5)
    amplet3 = amplet.Amplets(navette=True,date_depart="18h50-30/12/2021",date_arrivee="19h50-31/12/2021",places_dispo=5,id_coursier=5)
    produit1 = produits.Produits(id_marchand=78,nom="Tomate(s)",prix=450)
    produit2 = produits.Produits(id_marchand=78,nom="Pomme(s) de terre(s)",prix=450)
    produit3 = produits.Produits(id_marchand=78,nom="Orange(s)",prix=450)
    produit4 = produits.Produits(id_marchand=78,nom="Carotte(s)",prix=450)
    admin.set_password('oof')
    guest.set_password('oof')
    third.set_password('oof')
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(third)
    db.session.add(amplet1)
    db.session.add(amplet2)
    db.session.add(amplet3)
    db.session.add(produit1)
    db.session.add(produit2)
    db.session.add(produit3)
    db.session.add(produit4)
    db.session.commit()
############################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return users.User.query.get(int(user_id))

@app.route("/admin")
def hello_world():
    content = "<p>Hello, World ! Here are my users : </p>"
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
    return content

@app.route("/")
def index():
    return render_template("index.html", user=current_user)

@app.route("/navette", methods=['GET','POST'])
@login_required
def navette():
    L = {'username':str(current_user.username),'mail':str(current_user.email),'id':str(current_user.id)}
    listeproduits = []
    for produit in produits.Produits.query.all():
        listeproduits.append(produit.nom)
    if request.method=='POST':
        items = []
        for i in range(0,5):
            items.append({
                    "produit": request.form.get(f"produit{i}"),
                    "quantite": request.form.get(f"quantite{i}"),
                    "unite": request.form.get(f"unite{i}"),
                    })
        #for item in items:
            #produit = produits_amp.Produits_amp(id_amp=)
    return render_template("navette.html",personne=L,produits=listeproduits)

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


## IMPORT ROUTES

from routes import *

if __name__ == 'app':
    socketio.run(app, host='0.0.0.0', port=5000)