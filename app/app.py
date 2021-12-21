from flask import Flask, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

# Setup ####################################
setup = False
if not os.path.isfile("data/db.db"):
    os.open("data/db.db", os.O_CREAT)
    setup = True
############################################

from db import *
from models import *
        
db.create_all() # Creates the tables if necessary

# Setup ####################################
if setup:
    admin = users.User(username='admin', email='admin@test.com',points=20, marchand=True)
    guest = users.User(username='guest', email='guest@test.com',points=0, marchand=False)
    admin.set_password('oof')
    guest.set_password('oof')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
############################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return users.User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=50)], render_kw={"placeholder": "Pseudo"})
    password = PasswordField("Password", validators=[InputRequired(), Length(max=50)], render_kw={"placeholder":  "Mot de passe"})
    submit = SubmitField("Se connecter")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Invalid Email"), Length(max=100)], render_kw={"placeholder": "exemple@gmail.com"})
    username = StringField("Username", validators=[InputRequired(), Length(max=50)], render_kw={"placeholder": "Pseudo"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Mot de passe"})
    submit = SubmitField("S'inscrire")

    def validate_username(self, username):
        existing_user_username = users.User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("Ce nom d'utilisateur existe déjà merci d'en choisir un autre")

    def validate_email(self, email):
        existing_user_email = users.User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError("Cette addresse email est déjà utilisé par un autre utilisateur merci d'en choisir une autre")

@app.route("/admin")
def hello_world():
    content = "<p>Hello, World ! Here are my users : </p>"
    content += "<br/>"
    for user in users.User.query.all():
        content += f"{user.id} - {user.username} & {user.email}"
        content += "<br/>"
    return content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/navette")
@login_required
def navette():
    L = {'username':str(current_user.username),'mail':str(current_user.email),'id':str(current_user.id)}
    return render_template("navette.html",personne=L)
@app.route("/particulier")
@login_required
def particulier():
    return f"particulier"

@app.route("/profil")
@login_required
def profil():
    L = {'username':str(current_user.username),'mail':str(current_user.email),'points':str(current_user.points)}
    return render_template("profil.html",data=L)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = users.User(username=form.username.data, email=form.email.data, points=0, marchand=False)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form,login=False)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.User.query.filter_by(username=form.username.data).first()
        print(user.password_hash)
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for("index"))
        flash("Cet utilisateur n'existe pas")
    return render_template('register.html', title="Login", form=form, login=True)

@app.route('/logout', methods=["GET","POST"])
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('login'))

@app.route('/nouvelleAmplet')
def nouvelleAmplet():
    return render_template('nouvelleAmplet.html')

if __name__=="__main__":
    app.run(debug=True)