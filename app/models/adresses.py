from app import db
from snowflake import SnowflakeGenerator
import requests

gen = SnowflakeGenerator(12)
api_url = "http://api-adresse.data.gouv.fr/search/"

class Adresse(db.Model):
    __tablename__ = 'adresses'
    id = db.Column(db.String(40), primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    rue = db.Column(db.String(200), nullable=False)
    ville = db.Column(db.String(200), nullable=False)
    codepostal = db.Column(db.Integer, nullable=False)
    coordx = db.Column(db.Integer)
    coordy = db.Column(db.Integer)

    def __init__(self, numero, rue, ville, codepostal):
        self.id = next(gen)
        self.numero = numero
        self.rue = rue
        self.ville = ville
        self.codepostal = codepostal

        # Récupération des coordonnées
        resp = requests.get(api_url, params={'q': f'{self.numero}, {self.rue}, {self.codepostal} {self.ville}', 'limit': 1})
        parsed = resp.json()
        if len(parsed['features']) > 0:
            self.coordx = int(parsed['features'][0]['properties']['x'])
            self.coordy = int(parsed['features'][0]['properties']['y'])