from app import db
from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(4)

class Marchands(db.Model):
    __tablename__ = 'marchands'
    id = db.Column(db.String(40), primary_key=True)
    id_adresse = db.Column(db.Integer, db.ForeignKey('adresses.id'))
    nom = db.Column(db.String(100))
    type = db.Column(db.String(50))
    multiplicateur = db.Column(db.Float)

    def __init__(self, nom, id_adresse, type, multiplicateur=1):
        self.id = next(gen)
        self.nom = nom
        self.id_adresse = id_adresse
        self.type = type
        self.multiplicateur = multiplicateur
