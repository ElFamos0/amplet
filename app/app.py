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
    amplet1 = amplet.Amplets(navette=False,date_depart=1640717400000,date_arrivee=1640721000000,places_dispo=5,id_coursier=2,delai_fermeture_depart=6666666,ferme=False)
    amplet2 = amplet.Amplets(navette=True,date_depart=1640803800000, date_arrivee=1640807400000,places_dispo=5,id_coursier=5,delai_fermeture_depart=6666666,ferme=False)
    amplet3 = amplet.Amplets(navette=True,date_depart=1640890200000,date_arrivee=1640893800000,places_dispo=5,id_coursier=5,delai_fermeture_depart=6666666,ferme=False)
    admin.set_password('oof')
    guest.set_password('oof')
    third.set_password('oof')
    db.session.add(marchands.Marchands(nom= 'Chez Jupux',adresse="4 rue Jean Gireadoux 54600",type="Crémier",multiplicateur=1.0,coordx = 0,coordy= 0))
    db.session.add(marchands.Marchands(nom= 'Chez Tomczak',adresse="12 rue de Mondésert 54000",type="Maître Sauceur",multiplicateur=1.0,coordx = 0,coordy= 0))
    db.session.add(marchands.Marchands(nom= 'Chez LV',adresse="2 Avenue Paul Muller 54000",type="Primeur",multiplicateur=1.0,coordx = 0,coordy= 0))
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(third)
    db.session.add(amplet1)
    db.session.add(amplet2)
    db.session.add(amplet3)
    db.session.commit()

    l_u = users.User.query.all()
    lu_id = []
    for i in l_u :
        lu_id.append(i.id)
    
    db.session.add(amplet.Amplets(navette=False,date_depart=1640717400000,date_arrivee=1640721000000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666666))
    db.session.add(amplet.Amplets(navette=False,date_depart=1640868629249, date_arrivee=1640807400000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666666))
    db.session.add(amplet.Amplets(navette=False,date_depart=1640890200000,date_arrivee=1640893800000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666660))
    db.session.commit()


    l_m = marchands.Marchands.query.all()
    l_a = amplet.Amplets.query.all()
    lm_id = []
    la_id = []
    
    for i in l_a :
        la_id.append(i.id)
    
    for i in l_m :
        lm_id.append(i.id)

    db.session.add(participants_amp.Participants_amp(id_amp = la_id[3],id_user = lu_id[1],valide=1))
    db.session.add(participants_amp.Participants_amp(id_amp = la_id[4],id_user = lu_id[2],valide=1))
    db.session.add(participants_amp.Participants_amp(id_amp = la_id[5],id_user = lu_id[1],valide=1))
    db.session.add(participants_amp.Participants_amp(id_amp = la_id[5],id_user = lu_id[2],valide=1))

    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[0]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[0]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[0]))

    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[1]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[1]))

    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[2]))

    db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème épaisse 50 cL",prix = "500"))
    db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème liquide 50 cL",prix = "500"))
    db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème liquide 25 cL",prix = "300"))

    db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Sauce Blanche 50 cL",prix = "500"))
    db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Sauce Andalouse 50 cL",prix = "500"))
    db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Sauce Bolognaise 25 cL",prix = "300"))

    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Tomate",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Pomme de terre",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Orange",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Carotte",prix=450))


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