from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

####SETUP####
#############
setup = False
if not os.path.isfile("data/db.db"):
    os.open("data/db.db", os.O_CREAT)
    setup = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/db.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
        
db.create_all()

if setup:
    admin = User(username='admin', email='admin@test.com')
    guest = User(username='guest', email='guest@test.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

@app.route("/")
def hello_world():
    content = "<p>Hello, World ! Here are my users : </p>"
    content += "<br/>"
    for user in User.query.all():
        content += f"{user.id} - {user.username} & {user.email}"
        content += "<br/>"
    return content