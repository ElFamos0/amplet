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

@app.route('/succes')
@login_required
def succes() :

    return render_template('succes.html',user=current_user)

