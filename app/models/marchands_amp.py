from app import db
class Marchands_amp(db.Model):
    id_marchand = db.Column(db.Integer, primary_key=True)
    id_amp = db.Column(db.Integer)