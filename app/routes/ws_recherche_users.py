from db import *
from models.users import User
from flask_socketio import emit, disconnect
from flask_login import current_user
import functools

#################################################
########### RECHERCHE D'UTILISATEUR  ############
#################################################

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

@socketio.on('search_users')
@authenticated_only
def handle_search(msg):
    q1 = User.query.filter(User.username.contains(msg["query"]))
    q2 = User.query.filter(User.email.contains(msg["query"]))
    u = q1.union(q2).group_by(User.id).all()
    users = []
    for user in u:
        users.append({
            "id":user.id,
            "username":user.username,
            "avatar":user.avatar_url(),
        })
    emit('users', users, room=current_user.id)