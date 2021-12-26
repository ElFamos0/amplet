from db import app
from models import *
from flask import render_template
from flask_login import login_required, current_user

##############################
######### PROFILE  ###########
##############################

@app.route("/p")
@login_required
def other_profiles():
    return render_template("profil.html", user=current_user, chat=False)


@app.route("/p/<string:id>")
@login_required
def profil(id):
    usr = users.User.query.get(id)
    if usr == None:
        return '404'
    chat = True
    if id == current_user.id:
        chat = False
    print(chat)
    return render_template("profil.html", user=usr, chat=chat)

@app.route("/pe")
@login_required
def profilmodif():
    return render_template("profilmodif.html",user=current_user)