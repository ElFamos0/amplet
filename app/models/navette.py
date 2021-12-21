from app import db
class Navette(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dated = db.Column(db.Date, nullable=False)
    datea = db.Column(db.Date, nullable=False)