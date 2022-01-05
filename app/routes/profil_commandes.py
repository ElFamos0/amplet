from flask_login.utils import login_required
from db import *
from models import *
from flask_login import current_user
from flask import render_template
from utils.vote_marchand import *
from utils.timestamp import *

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
    inscr_list_len = []
    inscr_id_produits = []
    inscr_nom_produits = []
    inscr_quantite_produits = []
    inscr_unite_produits = []
    inscr_prix_produits = []
    inscr_totaux = []
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
            inscr_produits = produits_amp.Produits_amp\
            .query.add_entity(produits.Produits)\
            .join(produits.Produits, produits_amp.Produits_amp.id_produit==produits.Produits.id)\
            .filter(produits_amp.Produits_amp.id_user==current_user.id,produits_amp.Produits_amp.id_amp==inscr_id_amp[i]).all()
            inscr_id_produits.append([e[0].id_produit for e in inscr_produits])
            inscr_nom_produits.append([e[1].nom for e in inscr_produits])
            inscr_quantite_produits.append([e[0].quantite for e in inscr_produits])
            inscr_unite_produits.append([e[0].unite for e in inscr_produits])
            inscr_prix_produits.append([e[1].prix for e in inscr_produits])
        inscr_list_len = [len(e) for e in inscr_id_produits]
        n = len(inscriptions)
        inscr_totaux = [sum([inscr_prix_produits[i][j]*inscr_quantite_produits[i][j]/100 for j in range(inscr_list_len[i])]) for i in range (n)]
    cours_id_amp = []
    cours_strstatut_amp = []
    cours_list_len=[]
    cours_id_participants = []
    cours_valide_participants = []
    cours_nom_participants = []
    cours_places_amp_tot = []
    cours_valide_participants_acceptes = []
    cours_places_amp_occ = []
    cours_id_produits_participants = []
    cours_quantite_produits_participants = []
    cours_unite_produits_participants = []
    cours_nom_produits_participants = []
    cours_list_len2 = []
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
        cours_strstatut_amp = ["Fermée" if (amplet.Amplets.query.filter_by(id=idd).first().ferme) else "Ouverte" for idd in cours_id_amp ]
        cours_list_len = [len(e) for e in cours_id_participants]
        cours_places_amp_occ = [len(e) for e in cours_valide_participants_acceptes]
        for i in range(len(coursier)):
            cours_produits_participants = [produits_amp.Produits_amp\
                                        .query.add_entity(produits.Produits)\
                                        .join(produits.Produits,produits_amp.Produits_amp.id_produit==produits.Produits.id)\
                                        .filter(produits_amp.Produits_amp.id_amp==cours_id_amp[i],produits_amp.Produits_amp.id_user==id).all() for id in cours_id_participants[i]]
            # print('\n\n\n')
            # print(cours_produits_participants)
            # print('\n\n\n')
            cours_id_produits_participants.append([[f[0].id_produit for f in e] for e in cours_produits_participants])
            cours_nom_produits_participants.append([[f[1].nom for f in e] for e in cours_produits_participants])
            cours_quantite_produits_participants.append([[f[0].quantite for f in e] for e in cours_produits_participants])
            cours_unite_produits_participants.append([[f[0].unite for f in e] for e in cours_produits_participants])
        cours_list_len2 = [[len(f) for f in e] for e in cours_id_produits_participants]
    # nav_id_marchands_choisis = ['6884198245245927426','6884198245245927426'] 
    nav_id_marchands_choisis = []
    """A RECUP A PARTIR DU VOTE"""
    nav_voeux = produits_amp.Produits_amp.query.filter_by(id_user=current_user.id)
    nav_id = nav_voeux.group_by(produits_amp.Produits_amp.id_amp).all()
    nav_id = [e.id_amp for e in nav_id]
    nav_ferme = []
    nav_id_produits_choisis = []
    nav_prix_produits_choisis = []
    nav_nom_produits_choisis = []
    nav_quantite_produits_choisis = []
    nav_unite_produits_choisis = []
    nav_date = []
    nav_list_len = []
    nav_totaux = []

    nav_list_len2 = []
    nav_id_produits_pas_choisis = []
    nav_nom_produits_pas_choisis = []
    nav_quantite_produits_pas_choisis = []
    nav_unite_produits_pas_choisis = []
    p = len(nav_id)
    for i in range(p):
        # print('\n\n')
        # print(vote(nav_id[i]))
        # print('\n\n')
        nav_id_marchands_choisis.append(vote(nav_id[i])[0])
        # print('\n\n')
        # print(nav_id_marchands_choisis)
        # print('\n\n')
        prod_choisis = produits_amp.Produits_amp\
            .query.add_entity(produits.Produits)\
            .join(produits.Produits, produits_amp.Produits_amp.id_produit==produits.Produits.id)\
            .filter(produits_amp.Produits_amp.id_user==current_user.id,produits_amp.Produits_amp.id_amp==nav_id[i]).all()
        # print('\n\n\n')
        # print(prod_choisis)
        # print('\n\n\n')
        nav_id_produits_choisis.append([e[0].id_produit for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        nav_id_produits_pas_choisis.append([e[0].id_produit for e in prod_choisis if e[1].id_marchand not in nav_id_marchands_choisis[i]])
        nav_prix_produits_choisis.append([e[1].prix for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        temp_nom = [e[1].nom for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]]
        nav_nom_produits_choisis.append(temp_nom)
        nav_nom_produits_pas_choisis.append(list(set([e for e in [e[1].nom for e in prod_choisis] if e not in temp_nom])))
        # print('\n\n\n')
        # print(nav_nom_produits_pas_choisis)
        # print('\n\n\n')
        nav_quantite_produits_choisis.append([e[0].quantite for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        nav_quantite_produits_pas_choisis.append([e[0].quantite for e in prod_choisis if e[1].id_marchand not in nav_id_marchands_choisis[i]])
        # print('\n\n\n')
        # print(nav_quantite_produits_choisis)
        # print('\n\n\n')
        nav_unite_produits_choisis.append([e[0].unite for e in prod_choisis if e[1].id_marchand in nav_id_marchands_choisis[i]])
        nav_unite_produits_pas_choisis.append([e[0].unite for e in prod_choisis if e[1].id_marchand not in nav_id_marchands_choisis[i]])
        nav_date.append(timestamp_to_date(amplet.Amplets.query.filter_by(id=nav_id[i]).first().date_depart,format='True'))
        nav_ferme.append(amplet.Amplets.query.filter_by(id=nav_id[i]).first().ferme)
    nav_list_len = [len(e) for e in nav_id_produits_choisis]
    nav_list_len2 = [len(e) for e in nav_nom_produits_pas_choisis]
    nav_totaux = [sum([nav_prix_produits_choisis[i][j]*nav_quantite_produits_choisis[i][j]/100 for j in range(nav_list_len[i])]) for i in range (p)]
    # print('\n\n\n')
    # print('\n\n\n')
    return render_template("profil/commande.html",user=current_user,n=n,m=m,p=p,inscr_id_amp=inscr_id_amp, inscr_valide=inscr_valide,inscr_id_coursier=inscr_id_coursier,inscr_nom_coursier=inscr_nom_coursier, 
    inscr_totaux=inscr_totaux,inscr_list_len=inscr_list_len,inscr_id_produits=inscr_id_produits,inscr_nom_produits=inscr_nom_produits,inscr_quantite_produits=inscr_quantite_produits,inscr_unite_produits=inscr_unite_produits,inscr_prix_produits=inscr_prix_produits,
    cours_id_amp=cours_id_amp,cours_strstatut_amp=cours_strstatut_amp,cours_places_amp_occ=cours_places_amp_occ, cours_places_amp_tot=cours_places_amp_tot,cours_id_participants=cours_id_participants, cours_nom_participants=cours_nom_participants,cours_valide_participants=cours_valide_participants,cours_list_len=cours_list_len,
    cours_list_len2=cours_list_len2,cours_nom_produits_participants=cours_nom_produits_participants,cours_quantite_produits_participants=cours_quantite_produits_participants,cours_unite_produits_participants=cours_unite_produits_participants,
    nav_id=nav_id,nav_ferme=nav_ferme,nav_list_len=nav_list_len,nav_totaux=nav_totaux,nav_id_produits_choisis=nav_id_produits_choisis,nav_prix_produits_choisis=nav_prix_produits_choisis,nav_nom_produits_choisis=nav_nom_produits_choisis,nav_quantite_produits_choisis=nav_quantite_produits_choisis,nav_unite_produits_choisis=nav_unite_produits_choisis,nav_date=nav_date,
    nav_list_len2=nav_list_len2,nav_id_produits_pas_choisis=nav_id_produits_pas_choisis,nav_nom_produits_pas_choisis=nav_nom_produits_pas_choisis,nav_quantite_produits_pas_choisis=nav_quantite_produits_pas_choisis,nav_unite_produits_pas_choisis=nav_unite_produits_pas_choisis)

@app.route('/a/<string:id_ampl>/<string:id_part>')
@login_required
def accepter_participation(id_ampl,id_part):
    curr_amp = participants_amp.Participants_amp.query.filter_by(id_user = id_part, id_amp=id_ampl).first()
    curr_amp_id = curr_amp.id_amp
    amp = amplet.Amplets.query.filter_by(id = curr_amp_id).first()
    cours_id = amp.id_coursier
    if curr_amp and current_user.id==cours_id:
        curr_amp.valide=1
        db.session.commit()
        return commande()
    else:
        return render_template('info.html', user=current_user, msg="Vous n'avez pas l'autorisation de modifier le statut de cette Amplet ou elle n'existe pas", retour="/commande")

@app.route('/r/<string:id_ampl>/<string:id_part>')
@login_required
def refuser_participation(id_ampl,id_part):
    curr_amp = participants_amp.Participants_amp.query.filter_by(id_user = id_part, id_amp=id_ampl).first()
    curr_amp_id = curr_amp.id_amp
    amp = amplet.Amplets.query.filter_by(id = curr_amp_id).first()
    cours_id = amp.id_coursier
    if curr_amp and current_user.id==cours_id:
        curr_amp.valide=2
        db.session.commit()
        return commande()
    else:        
        return render_template('info.html', user=current_user, msg="Vous n'avez pas l'autorisation de modifier le statut de cette Amplet ou elle n'existe pas", retour="/commande")