from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # We define the flask application on main
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/db.db' # Declares the database path
db = SQLAlchemy(app) # Uses SQLAlchemy as ORM
