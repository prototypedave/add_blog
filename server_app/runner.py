from flask import Flask
from .models.storage import db
from .scheduler import start_scheduler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    start_scheduler(app, db)  # Only runs in this script


