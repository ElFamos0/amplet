from db import *
from models import *
from flask_login import current_user
from flask import render_template

##############################
########### INDEX  ###########
##############################

@app.route("/")
def index():
    return render_template("index.html", user=current_user)