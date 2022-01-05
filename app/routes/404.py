from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('info.html', user=current_user, msg= "Oops... Cette page n'existe pas !", retour="/"), 404

