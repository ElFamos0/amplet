from flask_login.utils import login_required
from models.users import User
from db import *
from models import *
from flask_login import current_user
from flask import render_template

##############################
########## COMMANDE  #########
##############################

@app.route("/commande")
@login_required
def commande():
    n=0
    m=0
    list_len=[]
    inscr_id_coursier = []
    inscr_id_amp = []
    inscr_valide = []
    inscr_nom_coursier = []
    inscriptions = participants_amp.Participants_amp.query.filter_by(id_user=current_user.id).all()
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
    cours_id_participants = []
    cours_valide_participants = []
    cours_nom_participants = []
    coursier = amplet.Amplets.query.filter_by(id_coursier = current_user.id).all()
    if coursier:
        for i in range(len(coursier)):
            cours_id_amp.append(coursier[i].id)
            cours_id_participants.append([e.id_user for e in participants_amp.Participants_amp.query.filter_by(id_amp = cours_id_amp[-1])])
            cours_valide_participants.append([e.valide for e in participants_amp.Participants_amp.query.filter_by(id_amp = cours_id_amp[-1])])
            cours_nom_participants.append([users.User.query.filter_by(id = e).first().username for e in cours_id_participants[-1]])
        m = len(coursier)
        for i in range(len(cours_valide_participants)):
            for j in range(len(cours_valide_participants[i])):
                if cours_valide_participants[i][j]==0:
                    cours_valide_participants[i][j]="En attente"
                if cours_valide_participants[i][j]==1:
                    cours_valide_participants[i][j]="Accepté"
                if cours_valide_participants[i][j]==2:
                    cours_valide_participants[i][j]="Refusé"
        list_len = [len(e) for e in cours_id_participants]


        
    



    # afficher les amplet dont user est le coursier
    # + une fois que Jules aura fait le classement, les produits des commandes navettes qui sont dispo dans les masagasins selectionnés

    
    return render_template("commande.html",user=current_user,n=n,m=m,inscr_id_amp=inscr_id_amp, inscr_valide=inscr_valide,inscr_id_coursier=inscr_id_coursier,inscr_nom_coursier=inscr_nom_coursier, 
    cours_id_amp=cours_id_amp, cours_id_participants=cours_id_participants, cours_nom_participants=cours_nom_participants,cours_valide_participants=cours_valide_participants,list_len=list_len)