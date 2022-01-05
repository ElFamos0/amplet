import threading
from time import sleep
from utils.vote_marchand import vote
from utils.update_multiplicateur import update_multiplicateur
from models.amplet import Amplets
from timestamp import until
from db import *

def attend_vote_automatique(id):
    amp = Amplets.query.get(id)
    sleep(until(amp.date_arrivee-amp.delai_fermeture_depart))
    amp = Amplets.query.get(id)
    if not amp:
        return
    liste_marchand, dic_marchand = vote(id)
    update_multiplicateur(liste_marchand, dic_marchand)
    amp.ferme = True
    db.session.commit()


def lance_vote_automatique(id):
    x = threading.Thread(target=attend_vote_automatique, args=(id,))
    x.start()