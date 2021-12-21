from app import db
class Navette(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dated = db.Column(db.Date, nullable=False)
    datea = db.Column(db.Date, nullable=False)
    marchant1 = db.Column(db.String(120), nullable=False)
    marchant2 = db.Column(db.String(120))
    marchant3 = db.Column(db.String(120))
    marchant4 = db.Column(db.String(120))
    marchant5 = db.Column(db.String(120))