from app import db

class Chat(db.Model):
    __tablename__ = 'chat'
    id_amp = db.Column(db.String(40), primary_key=True)
    id_emetteur = db.Column(db.String(40), db.ForeignKey('users.id'), primary_key=True)
    timestamps = db.Column(db.Integer, primary_key=True)
    contenu = db.Column(db.String(500))