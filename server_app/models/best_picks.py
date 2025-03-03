from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .storage import db
from datetime import datetime, timedelta

class BestPicksPrediction(db.Model):
    __tablename__ = 'sure_pred'

    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(100), nullable=False)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    prediction = db.Column(db.String(50), nullable=False)
    odds = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(50), default="-")
    reason = db.Column(db.Text, nullable=False)
    chance = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now) 

    def to_dict(self):
        return {
            "id": self.id,
            "league": self.league,
            "homeTeam": self.home_team,
            "awayTeam": self.away_team,
            "prediction": self.prediction,
            "odds": self.odds,
            "result": self.result,
            "reason": self.reason,
            "chance": self.chance,
            "time": self.time,
        }
    

def delete_best_predictions(db):
    expiry_date = datetime.now() - timedelta(days=3)
    BestPicksPrediction.query.filter(BestPicksPrediction.created_at < expiry_date).delete()
    db.session.commit()
