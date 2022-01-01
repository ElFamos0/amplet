from db import *
from models import *
from flask_login import current_user
from flask import render_template

@app.route("/amplets_en_cours")
def amplets_en_cours():
    return render_template('amplets_en_cours.html')