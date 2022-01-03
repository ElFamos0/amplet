from app import db
from utils.sha import generate_password_hash, check_password_hash
from flask_login import UserMixin
from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(0)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(40), primary_key=True)
    id_adresse = db.Column(db.Integer, db.ForeignKey('adresses.id'))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    
    def avatar_url(self):
        return f"/r/a/{self.id}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, email, id_adresse,points):
        self.id = next(gen)
        self.username = username
        self.email = email
        self.id_adresse = id_adresse
        self.points = points

    def __repr__(self):
        return '<User %r>' % self.username

