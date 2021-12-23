from app import db
class Marchands(db.Model):
    id_marchand = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    adresse = db.Column(db.String(400))
    type = db.Column(db.String(50))
    multiplicateur = db.Column(db.Float)