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
    adresse1 = adresses.Adresse(numero = 34,rue = "Rue des Tilleuls",ville = "Metz",codepostal = 57070)
    adresse2 = adresses.Adresse(numero = 1,rue = "Rue Emile Knoepfler",ville = "Mey",codepostal = 57070)
    db.session.add(adresse1)
    db.session.add(adresse2)
    db.session.add(adresses.Adresse(numero = 37,rue = "Rue Alfred Krieger",ville = "Metz",codepostal = 57070))
    db.session.add(adresses.Adresse(numero = 3,rue = "Rue Delattre de Tassigny",ville = "Laquenexy",codepostal = 57530))
    db.session.add(adresses.Adresse(numero = 1,rue = "Rue du Chapitre",ville = "Woippy",codepostal = 57140))
    db.session.add(adresses.Adresse(numero = 8,rue = "Rue de Metz",ville = "Gravelotte",codepostal = 57130))
    db.session.add(adresses.Adresse(numero = 59,rue = "Avenue du Général Mangin",ville = "Nancy",codepostal = 54000))

    db.session.commit()


    l_ad = adresses.Adresse.query.all()
    lad_id = []
    for i in l_ad :
        lad_id.append(i.id)

    admin = users.User(username='admin', email='admin@test.com', id_adresse=lad_id[0], points=54, role=666)
    guest = users.User(username='guest', email='guest@test.com', id_adresse=lad_id[1], points=38, role=38)
    third = users.User(username='third', email='third@test.com', id_adresse=lad_id[2])
    JeSuisLaNavette = users.User(username='navette', email='navette@test.com', id_adresse=lad_id[0], points=0, role=666)
    admin.set_password('oof')
    guest.set_password('oof')
    third.set_password('oof')
    JeSuisLaNavette.set_password('oof')
    db.session.add(marchands.Marchands(nom= 'Chez Jupux',id_adresse=lad_id[3],type="Crémier",multiplicateur=1.0))
    db.session.add(marchands.Marchands(nom= 'Chez Tomczak',id_adresse=lad_id[4],type="Maître Sauceur",multiplicateur=1.0))
    db.session.add(marchands.Marchands(nom= 'Chez LV',id_adresse=lad_id[5],type="Primeur",multiplicateur=1.0))
    db.session.add(marchands.Marchands(nom= 'Chez Malo',id_adresse=lad_id[6],type="Primeur",multiplicateur=1.0))
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(third)
    db.session.add(JeSuisLaNavette)
    db.session.commit()

    l_u = users.User.query.all()
    lu_id = []
    for i in l_u :
        lu_id.append(i.id)
    
    db.session.add(amplet.Amplets(navette=False,date_depart=1640717400000,date_arrivee=1640721000000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666666,dist_max = 50))
    db.session.add(amplet.Amplets(navette=False,date_depart=1640868629249, date_arrivee=1640807400000,places_dispo=5,id_coursier=lu_id[1],ferme = False,delai_fermeture_depart = 6666666,dist_max = 50))
    db.session.add(amplet.Amplets(navette=False,date_depart=1640890200000,date_arrivee=1640893800000,places_dispo=5,id_coursier=lu_id[2],ferme = False,delai_fermeture_depart = 6666660,dist_max = 50))
    db.session.add(amplet.Amplets(navette=True,date_depart=1640940200000,date_arrivee=1640806800000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666660))
    db.session.add(amplet.Amplets(navette=True,date_depart=1640990200000,date_arrivee=1640893800000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666660))
    db.session.add(amplet.Amplets(navette=True,date_depart=1650990200000,date_arrivee=1650893800000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666660))
    db.session.add(amplet.Amplets(navette=True,date_depart=1660990200000,date_arrivee=1660893800000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666660))

    db.session.commit()


    l_m = marchands.Marchands.query.all()
    l_a = amplet.Amplets.query.all()
    lm_id = []
    la_id = []
    
    for i in l_a :
        la_id.append(i.id)
    
    for i in l_m :
        lm_id.append(i.id)

    db.session.add(participants_amp.Participants_amp(id_amp = la_id[0],id_user = lu_id[1],valide=0))
    db.session.add(participants_amp.Participants_amp(id_amp = la_id[1],id_user = lu_id[2],valide=1))
    db.session.add(participants_amp.Participants_amp(id_amp = la_id[2],id_user = lu_id[1],valide=1))
    db.session.add(participants_amp.Participants_amp(id_amp = la_id[2],id_user = lu_id[2],valide=1))

    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[0],id_marchand = lm_id[0]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[1],id_marchand = lm_id[0]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[2],id_marchand = lm_id[0]))

    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[2],id_marchand = lm_id[1]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[1],id_marchand = lm_id[1]))

    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[2],id_marchand = lm_id[2]))


    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[0]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[1]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[2]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[3]))

    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[1]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[2]))
    db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[3]))

    db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème épaisse 50 cL",prix = 500))
    db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème liquide 50 cL",prix = 500))
    db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème liquide 25 cL",prix = 300))

    db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Sauce Blanche 50 cL",prix = 500))
    db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Sauce Andalouse 50 cL",prix = 500))
    db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Sauce Bolognaise 25 cL",prix = 300))

    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Tomate",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Pomme de terre",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Orange",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Carotte",prix=450))

    db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Tomate",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Pomme de terre",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Orange",prix=450))
    db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Carotte",prix=450))

    db.session.add(participants_amp.Participants_amp(id_amp=la_id[2], id_user=lu_id[0], valide=1))
    db.session.add(participants_amp.Participants_amp(id_amp=la_id[0], id_user=lu_id[2], valide=1))

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