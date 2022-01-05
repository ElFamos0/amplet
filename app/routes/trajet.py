from db import *
from models import *
from flask_login import login_required
from flask_login import current_user
from flask import render_template, request, flash
from utils import vote_marchand


@app.route('/trajet', methods=['GET','POST'])
@login_required
def trajet():
    navettedisp = amplet.Amplets.query.filter_by(navette=True,ferme=True).order_by(amplet.Amplets.id).all()
    phrase = "Il n'y a pas de navette à optimiser"
    for p in navettedisp:
        a = vote_marchand.vote(p.id)
        print(f"{p.id} et {a}")
        phrase = f"{p.id} et {a}"
    return render_template("trajet.html", user=current_user.id,phrase=phrase)
