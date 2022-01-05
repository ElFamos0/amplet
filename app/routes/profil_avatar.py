from db import app
from flask_login import login_required, current_user
from flask import render_template, request, send_from_directory, flash
import os
from snowflake import SnowflakeGenerator

default_path = "photos/chien.jpeg"
gen = SnowflakeGenerator(666)

##############################
########### AVATAR ###########
##############################

@app.route('/pa', methods = ['GET', 'POST'])
@login_required
def upload_pp():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            folder = f"static/avatar/{current_user.id}"
            if not os.path.exists(folder):
                os.mkdir(folder)
            else:
                L = os.listdir(folder)
                for file in L:
                    os.remove(f"{folder}/{file}")
            f.save(f"{folder}/{next(gen)}.png")
        else:
            flash("Veuillez envoyer un fichier.")
    return render_template('profil/upload.html', user=current_user)

if __name__=="__main__":
    app.run(debug=True)

@app.route('/r/a/<string:id>/<string:aid>')
def get_pp(id,aid):
    folder = f"static/avatar/{id}/{aid}.png"
    file = f"avatar/{id}/{aid}.png"
    if not os.path.exists(folder):
        return send_from_directory('static', default_path)
    return send_from_directory('static', file)