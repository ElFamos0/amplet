from app import db

class Produits_amp(db.Model):
    __tablename__ = 'produits_amp'
    id_amp = db.Column(db.String(40), primary_key=True)
    id_produit = db.Column(db.String(40), db.ForeignKey('produits.id'),primary_key=True)
    id_user = db.Column(db.String(40), db.ForeignKey('users.id'))
    quantite = db.Column(db.Integer)
    unite = db.Column(db.String(10))