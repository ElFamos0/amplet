from app import db
class Enregistrement_Navette(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marchants = db.Column(db.String(200), nullable=False)
