from app import db



class Participants_amp(db.Model):
    __tablename__ = 'participants_amp'
    id_amp = db.Column(db.String(40), db.ForeignKey('amplets.id'), primary_key=True)
    id_user = db.Column(db.String(40), db.ForeignKey('users.id'), primary_key=True)
    valide = db.Column(db.Integer)

    def est_valide(self):
        return self.valide==1

    def est_refuse(self) :
        return self.valide==2

    def en_attente(self) :
        return self.valide==0

    def rend_valide(self) :
        self.valide = 1
    
    def rend_refuse(self) :
        self.valide = 2