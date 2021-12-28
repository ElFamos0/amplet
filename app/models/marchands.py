from app import db
from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(4)

class Marchands(db.Model):
    __tablename__ = 'marchands'
    id = db.Column(db.String(40), primary_key=True)
    nom = db.Column(db.String(100))
    adresse = db.Column(db.String(400))
    coordx = db.Column(db.Integer)
    coordy = db.Column(db.Integer)
    type = db.Column(db.String(50))
    multiplicateur = db.Column(db.Float)

    def __init__(self, nom, adresse, coordx, coordy, type):
        self.id = next(gen)
        self.nom = nom
        self.prix = adresse
        self.multiplicateur = type
        self.coordx = coordx
        self.coordy = coordy