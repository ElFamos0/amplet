from app import db
from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(5)

class Produits(db.Model):
    __tablename__ = 'produits'
    id_produit = db.Column(db.String(40), primary_key=True)
    id_marchand = db.Column(db.String(40), db.ForeignKey('marchands.id'))
    nom = db.Column(db.String(100))
    prix = db.Column(db.Integer)

    def __init__(self, id_marchand, nom, prix):
        self.id = next(gen)
        self.id_marchand = id_marchand
        self.nom = nom
        self.prix = prix