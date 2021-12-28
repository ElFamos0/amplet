from re import M
from flask_login import LoginManager
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
    amplet1 = amplet.Amplets(navette=False,date_depart=1640717400000,date_arrivee=1640721000000,places_dispo=5,id_coursier=2)
    amplet2 = amplet.Amplets(navette=True,date_depart=1640803800000, date_arrivee=1640807400000,places_dispo=5,id_coursier=5)
    amplet3 = amplet.Amplets(navette=True,date_depart=1640890200000,date_arrivee=1640893800000,places_dispo=5,id_coursier=5)
    produit1 = produits.Produits(id_marchand=78,nom="Tomate(s)",prix=450)
    produit2 = produits.Produits(id_marchand=78,nom="Pomme(s) de terre",prix=450)
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

## IMPORT ROUTES

from routes import *

if __name__ == 'app':
    socketio.run(app, host='0.0.0.0', port=5000)