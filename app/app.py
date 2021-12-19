from flask import Flask, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
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
    admin = users.User(username='admin', email='admin@test.com')
    guest = users.User(username='guest', email='guest@test.com')
    admin.set_password('oof')
    guest.set_password('oof')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
############################################

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return users.User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=15)], render_kw={"placeholder": "Username"})
    password = PasswordField("Password", validators=[InputRequired(), Length(max=50)], render_kw={"placeholder":  "Password"})
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Invalid Email"), Length(max=50)], render_kw={"placeholder": "example@gmail.com"})
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "Username"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "********"})
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("Ce nom d'utilisateur existe déjà merci d'en choisir un autre")

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
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

@app.route("/register")
def register():
    return render_template("register.html",login=False)

@app.route("/register",methods=['POST'])
def createaccount():    
    username = request.form['username']
    motdepasse = request.form['register']
    mail = request.form['emailAddress']
    return f"{mail},{username},{motdepasse}"

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    print(form.username.data)
    if form.validate_on_submit():
        user = users.User.query.filter_by(username=form.username.data).first()
        if user:
            if users.User.check_password(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for("hello_world"))
    
        flash("Cet utilisateur n'existe pas")
    return render_template('register.html', title="Login", form=form, login=True)



if __name__=="__main__":
    app.run(debug=True)