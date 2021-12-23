from app import db
class Chat(db.Model):
    id_amp = db.Column(db.Integer, primary_key=True)
    id_emetteur = db.Column(db.Integer)
    timestamps = db.Column(db.Integer)
    contenu = db.Column(db.String(500))