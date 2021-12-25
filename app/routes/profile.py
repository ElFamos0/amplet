from db import app
from models import *
from flask import render_template
from flask_login import login_required, current_user

##############################
######### PROFILE  ###########
##############################

@app.route("/profil")
@login_required
def profil():
    return render_template("profil.html",personne=current_user)

@app.route("/profilmodif")
@login_required
def profilmodif():
    return render_template("profilmodif.html",personne=current_user)