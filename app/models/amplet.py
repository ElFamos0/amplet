from app import db
from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(1)

class Amplets(db.Model):
    __tablename__ = 'amplets'
    id = db.Column(db.String(40), primary_key=True)
    id_coursier = db.Column(db.String(40), db.ForeignKey('users.id'), nullable=False)
    navette = db.Column(db.Boolean, nullable=False)
    date_depart = db.Column(db.Integer, nullable=False)
    date_arrivee = db.Column(db.Integer, nullable=False)
    delai_fermeture_depart = db.Column(db.Integer, nullable=False)
    places_dispo = db.Column(db.Integer, nullable=False)
    ferme = db.Column(db.Bool, nullable=False)

    def __init__(self, navette, date_depart, date_arrivee, places_dispo, id_coursier, delai_fermeture_depart, ferme):
        self.id = next(gen)
        self.navette = navette
        self.date_depart = date_depart
        self.date_arrivee = date_arrivee
        self.places_dispo = places_dispo
        self.id_coursier = id_coursier
        self.delai_fermeture_depart = delai_fermeture_depart
        self.ferme = ferme