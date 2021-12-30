from app import db

class Marchands_amp(db.Model):
    __tablename__ = 'marchands_amp'
    id_marchand = db.Column(db.String(40), db.ForeignKey('marchands.id'), primary_key=True)
    id_amp = db.Column(db.String(40), db.ForeignKey('amplets.id'), primary_key=True)