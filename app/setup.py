from db import *
from models import *

db.session.add(adresses.Adresse(numero = 12,rue = "Rue Charle III",ville = "Nancy",codepostal = 54000))
db.session.add(adresses.Adresse(numero = 193,rue = "Avenue Paul Muller",ville = "Villers-Lès-Nancy",codepostal = 54602))
db.session.add(adresses.Adresse(numero = 2,rue = "Rue Pol Chone",ville = "Laxou",codepostal = 54250))
db.session.add(adresses.Adresse(numero = 10,rue = "Rue Marie Marvingt",ville = "Heillecourt",codepostal = 54180))
db.session.add(adresses.Adresse(numero = 58,rue = "Avenue du Général Mangin",ville = "Nancy",codepostal = 54000))
db.session.add(adresses.Adresse(numero = 8,rue = "Rue des Pâquis",ville = "Messein",codepostal = 54850))
db.session.add(adresses.Adresse(numero = 15,rue = "Rude de Verdun",ville = "Champigneulles",codepostal = 54250))

db.session.add(adresses.Adresse(numero = 21,rue = "Grande Rue",ville = "Heillecourt",codepostal = 54180))
db.session.add(adresses.Adresse(numero = 7,rue = "Rue de Vannes",ville = "Heillecourt",codepostal = 54180))
db.session.add(adresses.Adresse(numero = 2,rue = "Rue Jean de la Fontaine",ville = "Laneuveville",codepostal = 54410))
db.session.add(adresses.Adresse(numero = 4,rue = "Rue Boris Vian",ville = "Laneuveville",codepostal = 54410))
db.session.add(adresses.Adresse(numero = 1,rue = "Rue Paul Verlaine",ville = "Laneuveville",codepostal = 54410))
db.session.add(adresses.Adresse(numero = 17,rue = "Rue Jeanne D'Arc",ville = "Nancy",codepostal = 54000))
db.session.add(adresses.Adresse(numero = 14,rue = "Avenue du Général Leclerc",ville = "Nancy",codepostal = 54000))
db.session.add(adresses.Adresse(numero = 22,rue = "Rue de Laxou",ville = "Nancy",codepostal = 54000))
db.session.add(adresses.Adresse(numero = 2,rue = "Rue de la Visitation",ville = "Nancy",codepostal = 54000))
db.session.add(adresses.Adresse(numero = 29,rue = "Lotissement La Croisette",ville = "Azelot",codepostal = 54210))


db.session.commit()


l_ad = adresses.Adresse.query.all()
lad_id = []
for i in l_ad :
    lad_id.append(i.id)

admin = users.User(username='admin', email='admin@test.com', id_adresse=lad_id[0], points=54, role=666)
guest = users.User(username='navette', email='guest@test.com', id_adresse=lad_id[1], points=38, role=1)
third = users.User(username='third', email='third@test.com', id_adresse=lad_id[2])
user1 = users.User(username='user1', email='user1@test.com', id_adresse=lad_id[3], points=5497)
user2 = users.User(username='user2', email='user2@test.com', id_adresse=lad_id[4], points=38)
user3 = users.User(username='user3', email='user3@test.com', id_adresse=lad_id[5])
user4 = users.User(username='user4', email='user4@test.com', id_adresse=lad_id[6])
admin.set_password('oof')
guest.set_password('oof')
third.set_password('oof')
user1.set_password('oof1')
user2.set_password('oof2')
user3.set_password('oof3')
user4.set_password('oof4')

db.session.add(admin)
db.session.add(guest)
db.session.add(third)
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)


db.session.add(marchands.Marchands(nom= 'Mâitre de la Crème',id_adresse=lad_id[7],type="Crémier",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'Apprenti de la Crème',id_adresse=lad_id[8],type="Crémier",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'Maître Sauceur',id_adresse=lad_id[9],type="Sauceur",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'Primeur aguerri',id_adresse=lad_id[10],type="Primeur",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'La floraison des Fruits',id_adresse=lad_id[11],type="Primeur",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'La patate fraîche',id_adresse=lad_id[12],type="Primeur",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'Mécanichien',id_adresse=lad_id[13],type="Mécanicien",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'Sports 200',id_adresse=lad_id[14],type="Magasin de Sport",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'Dodécathlon',id_adresse=lad_id[15],type="Magasin de Sport",multiplicateur=1.0))
db.session.add(marchands.Marchands(nom= 'Technique celle-là',id_adresse=lad_id[16],type="Technologie",multiplicateur=1.0))



db.session.commit()

l_u = users.User.query.all()
lu_id = []
for i in l_u :
    lu_id.append(i.id)


l_m = marchands.Marchands.query.all()
lm_id = []
for i in l_m :
    lm_id.append(i.id)


db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème épaisse",prix = 500)) #0
db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème liquide",prix = 500))
db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème liquide entière",prix = 300))
db.session.add(produits.Produits(id_marchand=lm_id[0],nom = "Crème épaisse suprême",prix = 1000)) 

db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Crème épaisse",prix = 500)) #4
db.session.add(produits.Produits(id_marchand=lm_id[1],nom = "Crème liquide",prix = 500))


db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Sauce Blanche",prix = 500)) #6
db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Sauce Andalouse",prix = 500))
db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Sauce Bolognaise",prix = 300))
db.session.add(produits.Produits(id_marchand=lm_id[2],nom = "Sauce Burger",prix = 200))

db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Tomate",prix=450)) #10
db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Pomme de terre",prix=450))
db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Orange",prix=450))
db.session.add(produits.Produits(id_marchand=lm_id[3],nom = "Carotte",prix=450))

db.session.add(produits.Produits(id_marchand=lm_id[4],nom = "Fraise",prix=450)) #14
db.session.add(produits.Produits(id_marchand=lm_id[4],nom = "Pas Paille",prix=50))
db.session.add(produits.Produits(id_marchand=lm_id[4],nom = "Pomme",prix=250))
db.session.add(produits.Produits(id_marchand=lm_id[4],nom = "Orange",prix=750))
db.session.add(produits.Produits(id_marchand=lm_id[4],nom = "Citron",prix=350))

db.session.add(produits.Produits(id_marchand=lm_id[5],nom = "Pomme de terre",prix=450)) #19
db.session.add(produits.Produits(id_marchand=lm_id[5],nom = "Pomme de terre de qualité",prix=650))

db.session.add(produits.Produits(id_marchand=lm_id[6],nom = "Essuie-glaces",prix=1450)) #21
db.session.add(produits.Produits(id_marchand=lm_id[6],nom = "Pneu",prix=3650))
db.session.add(produits.Produits(id_marchand=lm_id[6],nom = "Pneu hiver",prix=4650))

db.session.add(produits.Produits(id_marchand=lm_id[7],nom = "Chaussures bof",prix=4450)) #24
db.session.add(produits.Produits(id_marchand=lm_id[7],nom = "Ballon crevé",prix=350))
db.session.add(produits.Produits(id_marchand=lm_id[7],nom = "Masque percé",prix=450))

db.session.add(produits.Produits(id_marchand=lm_id[8],nom = "Chaussures bof",prix=4450)) #27
db.session.add(produits.Produits(id_marchand=lm_id[8],nom = "Chaussures bien",prix=8450))
db.session.add(produits.Produits(id_marchand=lm_id[8],nom = "Ballon",prix=950))

db.session.add(produits.Produits(id_marchand=lm_id[9],nom = "Adaptateur",prix=3499)) #30
db.session.add(produits.Produits(id_marchand=lm_id[9],nom = "Siège Gaming",prix=18350))
db.session.add(produits.Produits(id_marchand=lm_id[9],nom = "Tablette Graphique",prix=19950))


db.session.commit()

db.session.add(amplet.Amplets(navette=False,date_depart=1641312000000,date_arrivee=1641314600000,places_dispo=5,id_coursier=lu_id[3],ferme = True,delai_fermeture_depart = 6666666,dist_max = 50))
db.session.add(amplet.Amplets(navette=False,date_depart=1643040000000,date_arrivee=1643043600000,places_dispo=4,id_coursier=lu_id[6],ferme = False,delai_fermeture_depart = 6666666,dist_max = 25))
db.session.add(amplet.Amplets(navette=False,date_depart=1643130000000,date_arrivee=1643133600000,places_dispo=2,id_coursier=lu_id[4],ferme = True,delai_fermeture_depart = 6666660,dist_max = 15))
db.session.add(amplet.Amplets(navette=False,date_depart=1643184000000,date_arrivee=1643189800000,places_dispo=3,id_coursier=lu_id[6],ferme = False,delai_fermeture_depart = 6666666,dist_max = 10))
db.session.add(amplet.Amplets(navette=False,date_depart=1643205600000,date_arrivee=1643209200000,places_dispo=5,id_coursier=lu_id[5],ferme = False,delai_fermeture_depart = 6666666,dist_max = 50))
db.session.add(amplet.Amplets(navette=True,date_depart=1641312000000,date_arrivee=1641356000000,places_dispo=100,id_coursier=guest.id,ferme = True,delai_fermeture_depart = 6666660))
db.session.add(amplet.Amplets(navette=True,date_depart=1643040000000,date_arrivee=1643043600000,places_dispo=100,id_coursier=guest.id,ferme = False,delai_fermeture_depart = 6666660))
db.session.add(amplet.Amplets(navette=True,date_depart=1643040000000,date_arrivee=1643045600000,places_dispo=100,id_coursier=guest.id,ferme = False,delai_fermeture_depart = 6666660))
db.session.add(amplet.Amplets(navette=True,date_depart=1643184000000,date_arrivee=1643189800000,places_dispo=100,id_coursier=guest.id,ferme = False,delai_fermeture_depart = 6666660))
db.session.add(amplet.Amplets(navette=True,date_depart=1643205600000,date_arrivee=1643205600000,places_dispo=100,id_coursier=guest.id,ferme = False,delai_fermeture_depart = 6666660))


db.session.commit()


l_a = amplet.Amplets.query.all()
l_p = produits.Produits.query.all()
la_id = []
lp_id = []
for i in l_a :
    la_id.append(i.id)
for i in l_p :
    lp_id.append(i.id)


db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[0],id_marchand = lm_id[0]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[0],id_marchand = lm_id[3]))

db.session.add(participants_amp.Participants_amp(id_amp = la_id[0],id_user = lu_id[5],valide=1))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[0],id_user = lu_id[4],valide=1))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[0], id_user = lu_id[5], id_produit= lp_id[0],quantite = 5,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[0], id_user = lu_id[5], id_produit= lp_id[1],quantite = 3,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[0], id_user = lu_id[5], id_produit= lp_id[11],quantite = 1,unite = "kg"))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[0], id_user = lu_id[4], id_produit= lp_id[3],quantite = 3,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[0], id_user = lu_id[4], id_produit= lp_id[12],quantite = 5,unite = "kg"))



db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[1],id_marchand = lm_id[9]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[1],id_marchand = lm_id[5]))

db.session.add(participants_amp.Participants_amp(id_amp = la_id[1],id_user = lu_id[3],valide=0))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[1],id_user = lu_id[4],valide=0))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[1],id_user = lu_id[5],valide=2))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[1], id_user = lu_id[3], id_produit= lp_id[20],quantite = 5,unite = "kg"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[1], id_user = lu_id[3], id_produit= lp_id[31],quantite = 1,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[1], id_user = lu_id[3], id_produit= lp_id[32],quantite = 1,unite = "unite"))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[1], id_user = lu_id[4], id_produit= lp_id[30],quantite = 1,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[1], id_user = lu_id[4], id_produit= lp_id[19],quantite = 5,unite = "kg"))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[1], id_user = lu_id[5], id_produit= lp_id[20],quantite = 9,unite = "kg"))



db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[2],id_marchand = lm_id[5]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[2],id_marchand = lm_id[4]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[2],id_marchand = lm_id[3]))

db.session.add(participants_amp.Participants_amp(id_amp = la_id[2],id_user = lu_id[3],valide=1))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[2],id_user = lu_id[6],valide=1))


db.session.add(produits_amp.Produits_amp(id_amp = la_id[2], id_user = lu_id[3], id_produit= lp_id[15],quantite = 5,unite = "kg"))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[2], id_user = lu_id[6], id_produit= lp_id[20],quantite = 1,unite = "kg"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[2], id_user = lu_id[6], id_produit= lp_id[19],quantite = 5,unite = "kg"))



db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[9]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[8]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[3],id_marchand = lm_id[7]))

db.session.add(participants_amp.Participants_amp(id_amp = la_id[3],id_user = lu_id[4],valide=1))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[3],id_user = lu_id[5],valide=1))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[3], id_user = lu_id[4], id_produit= lp_id[24],quantite = 1,unite = "unite"))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[3], id_user = lu_id[5], id_produit= lp_id[28],quantite = 1,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[3], id_user = lu_id[5], id_produit= lp_id[29],quantite = 2,unite = "unite"))



db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[9]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[5]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[2]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[4],id_marchand = lm_id[0]))







db.session.add(participants_amp.Participants_amp(id_amp = la_id[5],id_user = lu_id[4],valide=0))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[5],id_user = lu_id[5],valide=0))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[5], id_user = lu_id[4], id_produit= lp_id[12],quantite = 1,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[5], id_user = lu_id[4], id_produit= lp_id[16],quantite = 1,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[5], id_user = lu_id[4], id_produit= lp_id[9],quantite = 1,unite = "unite"))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[5], id_user = lu_id[5], id_produit= lp_id[14],quantite = 1,unite = "unite"))
db.session.add(produits_amp.Produits_amp(id_amp = la_id[5], id_user = lu_id[5], id_produit= lp_id[13],quantite = 2,unite = "unite"))

db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[2],votes = 1))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[3],votes = 2))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[4],votes = 2))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[8]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[9]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[5],id_marchand = lm_id[0]))





db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[2]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[3]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[4]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[8]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[9]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[0]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[1]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[5]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[6]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[6],id_marchand = lm_id[7]))


db.session.add(participants_amp.Participants_amp(id_amp = la_id[6],id_user = lu_id[3],valide=0))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[6],id_user = lu_id[4],valide=0))
db.session.add(participants_amp.Participants_amp(id_amp = la_id[6],id_user = lu_id[5],valide=0))

db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[4], id_produit= lp_id[12],quantite = 4,unite = "kg"))  #Orange Primeur aguerri
db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[4], id_produit= lp_id[16],quantite = 4,unite = "kg"))  #Orange FLoraison des fruits
db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[4], id_produit= lp_id[9],quantite = 1,unite = "unite")) # Sauce burger

db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[3], id_produit= lp_id[14],quantite = 1,unite = "unite")) # Fraise floraison
db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[3], id_produit= lp_id[20],quantite = 2,unite = "kg")) # Patates de qualités 

db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[5], id_produit= lp_id[31],quantite = 1,unite = "unite")) # Siège gaming
db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[5], id_produit= lp_id[7],quantite = 1,unite = "unite")) #Sauce Andalouse
db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[5], id_produit= lp_id[24],quantite = 1,unite = "unite")) # Chaussure BOf sport 200
db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[5], id_produit= lp_id[28],quantite = 1,unite = "unite")) # Chaussure bien dodécathlon
db.session.add(produits_amp.Produits_amp(id_amp = la_id[6], id_user = lu_id[5], id_produit= lp_id[27],quantite = 1,unite = "unite")) # Chaussure BOf Dodécathlon





db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[7],id_marchand = lm_id[0]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[7],id_marchand = lm_id[1]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[7],id_marchand = lm_id[2]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[7],id_marchand = lm_id[3]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[7],id_marchand = lm_id[4]))


db.session.add(participants_amp.Participants_amp(id_amp = la_id[7],id_user = lu_id[3],valide=0))


db.session.add(produits_amp.Produits_amp(id_amp = la_id[7], id_user = lu_id[4], id_produit= lp_id[12],quantite = 4,unite = "kg")) #Orange Primeur aguerri
db.session.add(produits_amp.Produits_amp(id_amp = la_id[7], id_user = lu_id[4], id_produit= lp_id[16],quantite = 4,unite = "kg")) #Orange FLoraison des fruits
db.session.add(produits_amp.Produits_amp(id_amp = la_id[7], id_user = lu_id[4], id_produit= lp_id[0],quantite = 1,unite = "unite")) #Crème épaisse mâitre
db.session.add(produits_amp.Produits_amp(id_amp = la_id[7], id_user = lu_id[4], id_produit= lp_id[4],quantite = 1,unite = "unite")) #Crème épaisse apprenti
db.session.add(produits_amp.Produits_amp(id_amp = la_id[7], id_user = lu_id[4], id_produit= lp_id[1],quantite = 1,unite = "unite")) #Crème liquide Maître
db.session.add(produits_amp.Produits_amp(id_amp = la_id[7], id_user = lu_id[4], id_produit= lp_id[5],quantite = 1,unite = "unite")) #Crème liquide apprenti
db.session.add(produits_amp.Produits_amp(id_amp = la_id[7], id_user = lu_id[4], id_produit= lp_id[3],quantite = 2,unite = "unite")) #Crème suprème Maître


db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[8],id_marchand = lm_id[0]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[8],id_marchand = lm_id[1]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[8],id_marchand = lm_id[2]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[8],id_marchand = lm_id[3]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[8],id_marchand = lm_id[4]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[8],id_marchand = lm_id[5]))




db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[0]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[1]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[2]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[3]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[4]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[5]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[6]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[7]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[8]))
db.session.add(marchands_amp.Marchands_amp(id_amp = la_id[9],id_marchand = lm_id[9]))

db.session.commit()



""" ANCIEN SETUP DES AMPLETS
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


db.session.add(participants_amp.Participants_amp(id_amp=la_id[2], id_user=lu_id[0], valide=1))
db.session.add(participants_amp.Participants_amp(id_amp=la_id[0], id_user=lu_id[2], valide=1)) """

