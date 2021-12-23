from db import app, db
from models import *
from flask import render_template, redirect, url_for, session, flash
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, ValidationError
import os

##############################
########### LOGIN  ###########
##############################


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