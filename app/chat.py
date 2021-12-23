from db import *
from models import *
from timestamp import *

def envoi_message(id_amplet:str, id_emetteur:str, contenu:str):
    msg = chat.Chat(id_amp=id_amplet, id_emetteur=id_emetteur, timestamps=now(), contenu=contenu)
    db.session.add(msg)
    db.session.commit()