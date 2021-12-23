from app import db
class Produits(db.Model):
    id_produit = db.Column(db.Integer, primary_key=True)
    id_marchand = db.Column(db.Integer)
    nom = db.Column(db.String(100))
    prix = db.Column(db.Integer)