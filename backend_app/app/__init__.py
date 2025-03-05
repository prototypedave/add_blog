from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from .routes import register_routes 
from .storage.database import db
from .models import register_models
from .scraping.scrape import flashscore

import redis

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    lock_name = "scheduler_lock"
    lock_timeout = 60

    db.init_app(app)

    register_models(app)

    register_routes(app)

    # Ensure only one instance runs when more than one worker is provided
    scheduler = BackgroundScheduler()
    if redis_client.set(lock_name, "locked", ex=lock_timeout, nx=True):
        scheduler.add_job(func=flashscore, trigger="interval", hours=6, args=[app, db])
        scheduler.start()

    return app
