from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request
from datetime import date, datetime
from time import mktime
from utils.timestamp import now, timestamp_to_date
from utils.recherche_par import recherche_par
from utils.amplets_a_afficher import amplets_a_afficher, amplet_dict

##############################
########### AMPLETS  ###########
##############################

@app.route('/nouvelleAmplet', methods=['GET','POST'])
@login_required
def nouvelleAmplet():
    mag_dispo=['primeur du coin', 'chez Tony']
    mag_visit=[]
    # if request.method=='POST':
    #     L=request.form
    #     for e in mag_dispo:
    #         if e in L:
    #             mag_visit.append(e)
    #     return mag_visit[1]
    return render_template('nouvelleAmplet.html', magasins=mag_dispo)

@app.route('/amplets_en_cours', methods=['GET','POST'])
@login_required
def amplets_en_cours() :

    march = marchands.Marchands.query.all()
    recherche = ['Proximité','Date de début']
    d2 = date.today().strftime("%Y-%m-%d")

    liste_type = []
    liste_mag =  []
    for m in march :
        liste_mag.append(m.nom)
        if m.type not in liste_type :
            liste_type.append(m.type)
    
    if request.method == "POST" :

        debut = request.form.get('mindate',d2)
        if debut == "" :
            debut = d2
        fin = request.form.get('maxdate',d2)
        if fin == "" :
            fin = d2
        
        recherche_actuelle = request.form.get('recherche','Proximité')
        i = 0
        for j in range(len(recherche)) :
            if recherche[j] == recherche_actuelle :
                i = j
        recherche[0],recherche[i] = recherche[i],recherche[0]
        liste_typebis = []
        for i in liste_type :
            val = request.form.get(i,'off')
            if val == 'on' :
                liste_typebis.append((i,True))
            else :
                liste_typebis.append((i,False))
    else :
        debut = d2
        fin = d2
        liste_typebis = []
        for i in liste_type :
            liste_typebis.append((i,False))

    
    debut_stamp = mktime(datetime.strptime(debut,"%Y-%m-%d").timetuple()) * 1000 # On convertit en timestamp
    fin_stamp = mktime(datetime.strptime(fin,"%Y-%m-%d").timetuple()) * 1000 # On convertit en timestamp

    liste_amplet= amplets_a_afficher(debut_stamp,fin_stamp,liste_typebis)

    if recherche[0] == 'Proximité' :

        id_ad =  users.User.query.get(current_user.id).id_adresse

        cp = adresses.Adresse.query.get(id_ad).codepostal

    else :
        cp = -100000

    liste_amplet = recherche_par(liste_amplet,recherche[0],cp)



    #amplet1 = {'id_amp' : 1,'participants' : ['Rémi BACHELET','LV'],'debut' : d2, 'navette' : 54600,"places" : 3, 'coursier' : 'NULL', 'l_magasins' : liste_mag,'valide' : True, 'cp' : 54600}
    #amplet2 = {'id_amp' : 2,'participants' : ['TropFortFestor'],'debut' : d2, 'navette' : 54610,"places" : 2, 'coursier' : 'NULL', 'l_magasins' : liste_mag,'valide' : False, 'cp' : 54610}
    #amplet3 = {'id_amp' : 3,'participants' : [],'debut' : d2, 'navette' : "NULL","places" : 4, 'coursier' : 'TOMZCAK', 'l_magasins' : liste_mag,'valide' : True, 'cp' : 54510}
    #liste_amplet = [amplet1,amplet2,amplet3]

  
    return render_template('amplets_en_cours.html',user=current_user,type_magasins = liste_typebis,debut = debut,fin = fin,recherche = recherche,amplets=liste_amplet)




@app.route('/inscription_amplet', methods=['GET','POST'])
@login_required
def inscription_amplet() :
    

    if request.method=='POST':
        ampl = request.form.get("amp_id")
        am = amplet_dict(ampl)
        if request.form.get('err') is None :
            allgood = True
        else :
            allgood = request.form.get('err')

        mag = marchands.Marchands.query.add_entity(marchands_amp.Marchands_amp).join(marchands_amp.Marchands_amp).filter(marchands_amp.Marchands_amp.id_amp == ampl,marchands_amp.Marchands_amp.id_marchand==marchands.Marchands.id)
        
        liste_mag = [m[0].id for m in mag]
        listeproduits = []
        listeprix = []
        for id_mag in liste_mag :
            prod = produits.Produits.query.add_entity(marchands.Marchands).join(marchands.Marchands).filter(marchands.Marchands.id == id_mag,produits.Produits.id_marchand == marchands.Marchands.id)
            listeprix += [p[0].prix for p in prod]
            listeproduits += [p[0].nom for p in prod]
        
        participation_valide = participants_amp.Participants_amp.query.filter_by(id_amp=ampl,id_user=current_user.id).first() is not None
    if request.method == "GET" :
        return render_template("index.html")
    
    return render_template('inscription_amplet.html',user=current_user,produits=listeproduits,amp = am,prix = listeprix,noproblem = allgood,ampid = ampl,dejainsc= participation_valide)
    
@app.route('/send_inscription_amplet', methods=['POST'])
@login_required
def send_inscription_amplet() :

    ampl = request.form.get("amp_id")
    am = amplet_dict(ampl)
    mag = marchands.Marchands.query.add_entity(marchands_amp.Marchands_amp).join(marchands_amp.Marchands_amp).filter(marchands_amp.Marchands_amp.id_amp == ampl,marchands_amp.Marchands_amp.id_marchand==marchands.Marchands.id)
        
    liste_mag = [m[0].id for m in mag]
    listeproduits = []
    listeprix = []
    for id_mag in liste_mag :
        prod = produits.Produits.query.add_entity(marchands.Marchands).join(marchands.Marchands).filter(marchands.Marchands.id == id_mag,produits.Produits.id_marchand == marchands.Marchands.id)
        listeprix += [p[0].prix for p in prod]
        listeproduits += [p[0].nom for p in prod]

    items = []
    for i in range(0,5):
        items.append({
                "produit": request.form.get(f"produit{i}"),
                "quantite": request.form.get(f"quantite{i}"),
                "unite": request.form.get(f"unite{i}"),
                })  
        #Cette partie ci-dessous me permet de faire toute les comparaisons nécessaire au bon fonctionnement du form
    participation_valide = participants_amp.Participants_amp.query.filter_by(id_amp=ampl,id_user=current_user.id).first() is not None #afin que le form ne comptabilise qu'une seule participation à une amplet
    print(participation_valide)
    if participation_valide :
        print(participants_amp.Participants_amp.query.filter_by(id_amp=ampl,id_user=current_user.id).first().id_user)
    listeverif = []
    
    for item in items:      
        if item["produit"] != "null":
            listeverif.append(item["produit"])
    allgood = not len(set(listeverif))!=len(listeverif)
    if participation_valide or not allgood :
        return render_template('inscription_amplet.html',user=current_user,produits=listeproduits,amp = am,prix = listeprix,noproblem = allgood,ampid=ampl,dejainsc= participation_valide)

    if allgood and not participation_valide:
        for item in items:
            if item["produit"] not in listeproduits or 0 > int(item["quantite"]) > 40 or item["quantite"]=="":
                continue
            idproduit = produits.Produits.query.filter(produits.Produits.nom==item["produit"]).first()
            produit = produits_amp.Produits_amp(id_amp=ampl,id_produit=idproduit.id,quantite=int(item["quantite"]),unite=item["unite"],id_user=current_user.id)
            if participation_valide == False: #afin que le form ne comptabilise qu'une seule participation à une amplet
                participation = participants_amp.Participants_amp(id_amp=ampl,id_user=current_user.id,valide= 0)
                db.session.add(participation)
                participation_valide = True
            db.session.add(produit)
            db.session.commit()


    return render_template("succès.html", user=current_user, succesnavette=False)


@app.route('/succès')
@login_required
def succès() :

    return render_template('succès.html',user=current_user, succesnavette=False)



@app.route('/amptest', methods=['GET','POST'])
@login_required
def amptest() :
    #db.session.add(marchands.Marchands(nom= 'Chez Jupux',adresse="4 rue Jean Gireadoux 54600",type="Crémier",multiplicateur=1.0,coordx = 0,coordy= 0))
    #db.session.add(marchands.Marchands(nom= 'Chez Tomczak',adresse="12 rue de Mondésert 54000",type="Maître Sauceur",multiplicateur=1.0,coordx = 0,coordy= 0))
    #db.session.add(marchands.Marchands(nom= 'Chez LV',adresse="2 Avenue Paul Muller 54000",type="Primeur",multiplicateur=1.0,coordx = 0,coordy= 0))

    #db.session.add(amplet.Amplets(navette=False,date_depart=1640717400000,date_arrivee=1640721000000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666666))
    #db.session.add(amplet.Amplets(navette=False,date_depart=1640868629249, date_arrivee=1640807400000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666666))
    #db.session.add(amplet.Amplets(navette=False,date_depart=1640890200000,date_arrivee=1640893800000,places_dispo=5,id_coursier=lu_id[0],ferme = False,delai_fermeture_depart = 6666660))

    #db.session.add(participants_amp.Participants_amp(id_amp = "6882299353730387968",id_user = "6882298862820655104"))
    #db.session.add(participants_amp.Participants_amp(id_amp = "6882299353730387969",id_user = "6882298862820655105"))
    #db.session.add(participants_amp.Participants_amp(id_amp = "6882299353730387970",id_user = "6882298862820655104"))
    #db.session.add(participants_amp.Participants_amp(id_amp = "6882299353730387970",id_user = "6882298862820655106"))

    #db.session.add(marchands_amp.Marchands_amp(id_amp = "6882299353730387968",id_marchand = "6882299353730400256"))
    #db.session.add(marchands_amp.Marchands_amp(id_amp = "6882299353730387969",id_marchand = "6882299353730400256"))
    #db.session.add(marchands_amp.Marchands_amp(id_amp = "6882299353730387970",id_marchand = "6882299353730400256"))

    #db.session.add(marchands_amp.Marchands_amp(id_amp = "6882299353730387970",id_marchand = "6882299353730400257"))
    #db.session.add(marchands_amp.Marchands_amp(id_amp = "6882299353730387969",id_marchand = "6882299353730400257"))

    #db.session.add(marchands_amp.Marchands_amp(id_amp = "6882299353730387970",id_marchand = "6882299353730400258"))


    #db.session.commit()
    test = db.metadata.tables.keys()
    test2 = db.metadata.tables['amplets'].columns.keys()
    #test3 = users.User.query.add_entity(amplet.Amplets).join(amplet.Amplets).filter(amplet.Amplets.id == "6881902203561316352",amplet.Amplets.id_coursier==users.User.id)
    #test3 = amplet.Amplets.query.all()
    #test3 = marchands.Marchands.query.all()
    test3 = users.User.query.get(current_user.id)
    test4 = users.User.query.all()
    liste1 = ""
    liste2 = ""
    liste3 = ""
    liste4 = ""
    for i in test :
        liste1+= i +' '

    for i  in test2 :
        liste2 += i + " "

    #for i  in test3 :
        #liste3 += i.id_amp + "__" + i.id_user + "   "
        #liste3 += i[0].username
        #liste3 += i.username + i.id
    liste3+= test3.username + str(test3.code_postal)
    for i  in test4 :
        liste4 += i.id + "__" + i.username + "  "
    
    return(render_template("amptest.html",a=liste1,b=liste2,c=liste3,d = liste4))

