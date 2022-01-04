import threading
from time import sleep
from models.amplet import Amplets
from timestamp import until

def attend_vote_automatique(id):
    amp = Amplets.query.get(id)
    sleep(until(amp.date_arrivee-amp.delai_fermeture_depart))
    ### Il faut appeler le vote ici
    print("voila")

def lance_vote_automatique(id):
    x = threading.Thread(target=attend_vote_automatique, args=(id,))
    x.start()