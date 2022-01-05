from flask_login.utils import login_required
from db import *
from models import *
from flask_login import current_user
from flask import render_template
from utils.vote_marchand import *
from utils import *

##############################
########## COMMANDE  #########
##############################

@app.route("/commande")
@login_required
def commande():
    n=0
    m=0
    inscr_id_coursier = []
    inscr_id_amp = []
    inscr_valide = []
    inscr_nom_coursier = []
    inscriptions = participants_amp.Participants_amp\
        .query.filter_by(id_user=current_user.id)\
        .join(amplet.Amplets,participants_amp.Participants_amp\
        .id_amp==amplet.Amplets.id)\
        .filter_by(navette=0).all()
    # print(inscriptions)
    if inscriptions:
        for i in range(len(inscriptions)):
            temp = inscriptions[i]
            inscr_id_amp.append(temp.id_amp)
            if temp.valide==0:
                inscr_valide.append("En attente")
            if temp.valide==1:
                inscr_valide.append("Accepté")
            if temp.valide==2:
                inscr_valide.append("Refusé")
            inscr_id_coursier.append(amplet.Amplets.query.filter_by(id = inscr_id_amp[-1], navette = 0).first().id_coursier)
            inscr_nom_coursier.append(users.User.query.filter_by(id = inscr_id_coursier[-1]).first().username)
        n = len(inscriptions)
    cours_id_amp = []
    cours_list_len=[]
    cours_id_participants = []
    cours_valide_participants = []
    cours_nom_participants = []
    cours_places_amp_tot = []
    cours_valide_participants_acceptes = []
    coursier = amplet.Amplets\
        .query.filter_by(id_coursier = current_user.id).all()
    if coursier:
        for i in range(len(coursier)):
            cours_id_amp.append(coursier[i].id)
            cours_places_amp_tot.append(coursier[i].places_dispo)
            cours_id_participants.append([e.id_user for e in participants_amp.Participants_amp.query.filter_by(id_amp = cours_id_amp[-1]) if e.valide!=2])
            cours_valide_participants.append([e.valide for e in participants_amp.Participants_amp.query.filter_by(id_amp = cours_id_amp[-1]) if e.valide!=2])
            cours_valide_participants_acceptes.append([e.valide for e in participants_amp.Participants_amp.query.filter_by(id_amp = cours_id_amp[-1]) if e.valide==1])
            cours_nom_participants.append([users.User.query.filter_by(id = e).first().username for e in cours_id_participants[-1]])
        m = len(coursier)
        cours_list_len = [len(e) for e in cours_id_participants]
        cours_places_amp_occ = [len(e) for e in cours_valide_participants_acceptes]
    # nav_id_marchands_choisis = ['6884198245245927426','6884198245245927426'] 
    nav_id_marchands_choisis = []
    """A RECUP A PARTIR DU VOTE"""
    nav_voeux = produits_amp.Produits_amp.query.filter_by(id_user=current_user.id)
    nav_id = nav_voeux.group_by(produits_amp.Produits_amp.id_amp).all()
    nav_id = [e.id_amp for e in nav_id]
    nav_id_produits_choisis = []
    nav_prix_produits_choisis = []
    nav_nom_produits_choisis = []
    nav_quantite_produits_choisis = []
    nav_unite_produits_choisis = []
    nav_date = []
    nav_list_len = []
    p = len(nav_id)
    for i in range(p):
        nav_id_marchands_choisis.append(vote(nav_id[i])[0])
        print('\n\n\n')
        print(nav_id_marchands_choisis)
        print('\n\n\n')
        prod_choisis = produits_amp.Produits_amp\
            .query.add_entity(produits.Produits)\
            .join(produits.Produits, produits_amp.Produits_amp.id_produit==produits.Produits.id)\
            .filter(produits_amp.Produits_amp.id_user==current_user.id,produits_amp.Produits_amp.id_amp==nav_id[i]).all()
        # print('\n\n\n')
        # print(prod_choisis)
        # print('\n\n\n')
        nav_id_produits_choisis.append([e[0].id_produit for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        nav_prix_produits_choisis.append([e[1].prix for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        nav_nom_produits_choisis.append([e[1].nom for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        nav_quantite_produits_choisis.append([e[0].quantite for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        # print('\n\n\n')
        # print(nav_quantite_produits_choisis)
        # print('\n\n\n')
        nav_unite_produits_choisis.append([e[0].unite for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        nav_date.append(timestamp.timestamp_to_date(amplet.Amplets.query.filter_by(id=nav_id[i]).first().date_depart,format='True'))
    nav_list_len = [len(e) for e in nav_id_produits_choisis]
    # print('\n\n\n')
    # print(nav_id)
    # print('\n\n\n')
    return render_template("commande.html",user=current_user,n=n,m=m,p=p,inscr_id_amp=inscr_id_amp, inscr_valide=inscr_valide,inscr_id_coursier=inscr_id_coursier,inscr_nom_coursier=inscr_nom_coursier, 
    cours_id_amp=cours_id_amp,cours_places_amp_occ=cours_places_amp_occ, cours_places_amp_tot=cours_places_amp_tot,cours_id_participants=cours_id_participants, cours_nom_participants=cours_nom_participants,cours_valide_participants=cours_valide_participants,cours_list_len=cours_list_len,
    nav_id=nav_id,nav_list_len=nav_list_len,nav_id_produits_choisis=nav_id_produits_choisis,nav_prix_produits_choisis=nav_prix_produits_choisis,nav_nom_produits_choisis=nav_nom_produits_choisis,nav_quantite_produits_choisis=nav_quantite_produits_choisis,nav_unite_produits_choisis=nav_unite_produits_choisis,nav_date=nav_date)