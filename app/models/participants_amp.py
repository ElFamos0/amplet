from app import db

class Participants_amp(db.Model):
    __tablename__ = 'participants_amp'
    id_amp = db.Column(db.String(40), primary_key=True)
    id_user = db.Column(db.String(40), db.ForeignKey('users.id'))