from db import *
from models import *
from utils.timestamp import now
from flask_socketio import emit, join_room, disconnect
from flask_login import current_user
import functools

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

@socketio.on('connect')
@authenticated_only
def handle_connection():
    print('connected')
    join_room(current_user.id)

@socketio.on('message')
@authenticated_only
def handle_message(msg):
    target = msg['target']
    content = msg['content']
    print('sent to db')
    db.session.add(chat.Chat(id_emetteur=current_user.id,id_amp=target,timestamps=now(),contenu=content))
    db.session.commit()
    data = {
        "sender": current_user.id,
        "receiver": target,
        "content": content,
        "time": "12:00",
        "date": "Today",
        "self": True,
    }
    emit('message', data, room=current_user.id)
    data["self"] = False
    emit('message', data, room=target)

@socketio.on('chats')
@authenticated_only
def handle_message(data):
    print('chats')
    if data["id"] == "all":
        for user in users.User.query.join(chat.Chat).filter(db.or_(chat.Chat.id_emetteur == users.User.id, chat.Chat.id_amp == users.User.id)).filter(db.or_(chat.Chat.id_emetteur == current_user.id, chat.Chat.id_amp == current_user.id)).all():
            pl = {
                'avatar_url' : user.avatar_url(),
                'id': user.id,
                'username': user.username,
            }
            emit('contact', pl, room=current_user.id)
        for msg in chat.Chat.query.filter(chat.Chat.id_emetteur == current_user.id).all():
            pl = {
                'sender': msg.id_emetteur,
                'receiver': msg.id_amp,
                'content' : msg.contenu,
                'time': '00',
                'date': msg.timestamps,
                'self': True,
            }
            emit('message', pl, room=current_user.id)
        for msg in chat.Chat.query.filter(chat.Chat.id_amp == current_user.id).all():
            pl = {
                'sender': msg.id_emetteur,
                'receiver': msg.id_amp,
                'content' : msg.contenu,
                'time': '00',
                'date': msg.timestamps,
                'self': False,
            }
            emit('message', pl, room=current_user.id)
    else:
        print(current_user.id, data["id"])
        for msg in chat.Chat.query.filter(chat.Chat.id_amp == data["id"]).filter(chat.Chat.id_emetteur == current_user.id).all():
            pl = {
                'sender': msg.id_emetteur,
                'receiver': msg.id_amp,
                'content' : msg.contenu,
                'time': '00',
                'date': msg.timestamps,
                'self': True,
            }
            emit('message', pl, room=current_user.id)
        for msg in chat.Chat.query.filter(chat.Chat.id_emetteur == data["id"]).filter(chat.Chat.id_amp == current_user.id).all():
            print(msg)
            pl = {
                'sender': msg.id_emetteur,
                'receiver': msg.id_amp,
                'content' : msg.contenu,
                'time': '00',
                'date': msg.timestamps,
                'self': False,
            }
            emit('message', pl, room=current_user.id)
