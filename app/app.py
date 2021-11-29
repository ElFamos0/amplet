from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *
import os

# Setup ####################################
setup = False
if not os.path.isfile("data/db.db"):
    os.open("data/db.db", os.O_CREAT)
    setup = True
############################################

app = Flask(__name__) # We define the flask application on main
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/db.db' # Declares the database path
db = SQLAlchemy(app) # Uses SQLAlchemy as ORM
        
db.create_all() # Creates the tables if necessary

# Setup ####################################
if setup:
    admin = User(username='admin', email='admin@test.com')
    guest = User(username='guest', email='guest@test.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
############################################

@app.route("/")
def hello_world():
    content = "<p>Hello, World ! Here are my users : </p>"
    content += "<br/>"
    for user in User.query.all():
        content += f"{user.id} - {user.username} & {user.email}"
        content += "<br/>"
    return content