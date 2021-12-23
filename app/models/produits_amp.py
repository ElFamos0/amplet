from app import db
class Produits_amp(db.Model):
    id_amp = db.Column(db.Integer, primary_key=True)
    id_produit = db.Column(db.Integer)