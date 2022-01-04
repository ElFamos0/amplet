from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template

@app.route('/succes')
@login_required
def succes() :
    return render_template('succes.html',user=current_user,succesnavette = False)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('erreur.html',user=current_user,erreur= "Oops... Cette page n'existe pas !"), 404

