from app import db
class Amplet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    navette = db.Column(db.Boolean, nullable=False)
    date_depart = db.Column(db.Integer, nullable=False)
    date_arrivee = db.Column(db.Integer, nullable=False)
    places_dispo = db.Column(db.Integer,nullable=False)
    coursier = db.Column(db.String(120),nullable=False)