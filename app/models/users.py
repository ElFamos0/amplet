from app import db
from utils.sha import generate_password_hash, check_password_hash
from flask_login import UserMixin
from snowflake import SnowflakeGenerator
import os

gen = SnowflakeGenerator(0)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(40), primary_key=True)
    id_adresse = db.Column(db.Integer, db.ForeignKey('adresses.id'))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    role = db.Column(db.Integer, nullable=False)

    def is_Admin(self):
        return self.role == 666

    def is_Mayor(self):
        return self.role == 1

    def avatar_url(self):
        folder = f"static/avatar/{self.id}"
        if not os.path.exists(folder):
            return f"/r/a/{self.id}/0"
        L = os.listdir(folder)
        if len(L) == 0: 
            return f"/r/a/{self.id}/0"
        name = L[0].replace(".png", "")
        return f"/r/a/{self.id}/{name}"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, email, id_adresse, points=0, role=0):
        self.id = next(gen)
        self.username = username
        self.email = email
        self.id_adresse = id_adresse
        self.points = points
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username

