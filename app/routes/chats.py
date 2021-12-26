from db import *
from models import *
from utils.timestamp import now, timestamp_to_date
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
    timestamp = now()
    db.session.add(chat.Chat(id_emetteur=current_user.id,id_amp=target,timestamps=timestamp,contenu=content))
    db.session.commit()
    count1 = chat.Chat.query.filter(chat.Chat.id_emetteur==current_user.id,chat.Chat.id_amp==target).count()
    count2 = chat.Chat.query.filter(chat.Chat.id_amp==current_user.id,chat.Chat.id_emetteur==target).count()
    if count1+count2 == 1:
        pl = {
                'avatar_url' : current_user.avatar_url(),
                'id': current_user.id,
                'username': current_user.username,
            }
        emit('contact', pl, room=target)
        ## Client will ask for the message out of curiosity
        return
    d = timestamp_to_date(timestamp)
    pl = {
        'sender': current_user.id,
        'receiver': target,
        'content' : content,
        'time': f'{d.hour:02d}:{d.minute:02d}:{d.second:02d}',
        'date': f'{d.day}-{d.month}-{d.year}',
        'self': True,
    }
    emit('message', pl, room=current_user.id)
    pl["self"] = False
    emit('message', pl, room=target)

@socketio.on('contact')
@authenticated_only
def handle_contact(data):
    req = users.User.query.get(data['id'])
    pl = {
        'avatar_url' : req.avatar_url(),
        'id': req.id,
        'username': req.username,
    }
    emit('contact', pl, room=current_user.id)

@socketio.on('chats')
@authenticated_only
def handle_chat(data):
    print('chats')
    if data["id"] == "all":
        q1 = db.session.query(chat.Chat.id_amp.label('id')).filter_by(id_emetteur=current_user.id)
        q2 = db.session.query(chat.Chat.id_emetteur.label('id')).filter_by(id_amp=current_user.id)
        u = q1.union(q2).group_by('id').all()
        for id in u:
            user = users.User.query.get(id)
            if user:
                pl = {
                    'avatar_url' : user.avatar_url(),
                    'id': user.id,
                    'username': user.username,
                }
                emit('contact', pl, room=current_user.id)
    else:
        q1 = chat.Chat.query.filter(chat.Chat.id_amp == data["id"]).filter(chat.Chat.id_emetteur == current_user.id)
        q2 = chat.Chat.query.filter(chat.Chat.id_emetteur == data["id"]).filter(chat.Chat.id_amp == current_user.id)
        u = q1.union(q2).order_by(chat.Chat.timestamps.asc()).all()
        for msg in u:
            isSelf = False
            if msg.id_emetteur == current_user.id:
                isSelf = True
            d = timestamp_to_date(msg.timestamps)
            pl = {
                'sender': msg.id_emetteur,
                'receiver': msg.id_amp,
                'content' : msg.contenu,
                'time': f'{d.hour:02d}:{d.minute:02d}:{d.second:02d}',
                'date': f'{d.day}-{d.month}-{d.year}',
                'self': isSelf,
            }
            emit('message', pl, room=current_user.id)
            if msg.id_emetteur == msg.id_amp:
                pl['self'] = False
                emit('message', pl, room=current_user.id)
