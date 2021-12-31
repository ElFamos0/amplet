from flask_login.utils import login_required
from db import *
from models import *
from flask_login import current_user
from flask import render_template

##############################
########### COMMANDE  ###########
##############################

@app.route("/commande")
@login_required
def commande():
    
    return render_template("commande.html",moi=current_user,)