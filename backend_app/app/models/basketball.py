from datetime import datetime
from app.storage.database import db
from datetime import datetime, timedelta
from sqlalchemy.sql import func
import json

class BasketPrediction(db.Model):
    __tablename__ = 'basket_predictions'

    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(100), nullable=False)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    prediction = db.Column(db.Text, nullable=False)  
    result = db.Column(db.String(50), default="-")
    time = db.Column(db.String(20), nullable=False)
    href = db.Column(db.String(50), nullable=False)
    odds = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())  

    def to_dict(self):
        return {
            "id": self.id,
            "league": self.league,
            "homeTeam": self.home_team,
            "awayTeam": self.away_team,
            "prediction": self.get_prediction(),  
            "result": self.result,
            "odds": self.odds,
            "time": self.time,
        }
    
    def set_prediction(self, prediction_dict):
        """Convert dictionary to JSON string for storage"""
        if isinstance(prediction_dict, dict):  
            self.prediction = json.dumps(prediction_dict)
        else:
            raise ValueError("Prediction must be a dictionary")

    def get_prediction(self):
        """Convert JSON string back to a formatted list of 'key - value' strings"""
        try:
            prediction_dict = json.loads(self.prediction)
            return [f"{key} - {value}" for key, value in prediction_dict.items()]
        except (TypeError, json.JSONDecodeError):
            return []
    
    def get_link(self):
        return self.href
    

def delete_basket_predictions(db):
    expiry_date = datetime.now() - timedelta(days=3)
    BasketPrediction.query.filter(BasketPrediction.created_at < expiry_date).delete()
    db.session.commit()
