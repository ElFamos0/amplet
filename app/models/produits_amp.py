from app import db

class Produits_amp(db.Model):
    __tablename__ = 'produits_amp'
    id_amp = db.Column(db.String(40), primary_key=True)
    id_produit = db.Column(db.String(40), db.ForeignKey('produits.id'))