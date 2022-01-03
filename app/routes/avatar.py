from db import app
from flask_login import login_required, current_user
from flask import render_template, request, send_from_directory
import os

default_path = "photos/chien.jpeg"

##############################
########### AVATAR ###########
##############################

@app.route('/change_avatar', methods = ['GET', 'POST'])
@login_required
def upload_pp():
    if request.method == 'POST':
        f = request.files['file']
        folder = f"static/avatar/{current_user.id}"
        if not os.path.exists(folder):
            os.mkdir(folder)
        f.save(f"{folder}/avatar.png")
        return 'avatar reçu !'
    else:
        return render_template('upload.html', personne=current_user)

if __name__=="__main__":
    app.run(debug=True)

@app.route('/r/a/<string:id>')
def get_pp(id):
    folder = f"static/avatar/{id}"
    file = f"avatar/{id}/avatar.png"
    if not os.path.exists(folder):
        return send_from_directory('static', default_path)
    return send_from_directory('static', file)