from app import db
class Navette(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dated = db.Column(db.Integer, nullable=False)
    datea = db.Column(db.Integer, nullable=False)