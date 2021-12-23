from app import db
class Participants_amp(db.Model):
    id_amp = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)