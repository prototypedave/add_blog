from datetime import datetime
from storage.database import db
from datetime import datetime, timedelta
import json

class BasketPrediction(db.Model):
    __tablename__ = 'basket_predictions'

    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(100), nullable=False)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    prediction = db.Column(db.String(500), nullable=False)
    result = db.Column(db.String(50), default="-")
    time = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now) 

    def to_dict(self):
        return {
            "id": self.id,
            "league": self.league,
            "homeTeam": self.home_team,
            "awayTeam": self.away_team,
            "prediction": self.prediction,
            "result": self.result,
            "time": self.time,
        }
    
    def set_prediction(self, predictions_list):
        self.prediction = json.dumps(list(predictions_list))

    def get_prediction(self):
        """Convert JSON string back to list when retrieving"""
        return json.loads(self.prediction)
    

def delete_basket_predictions(db):
    expiry_date = datetime.now() - timedelta(days=3)
    BasketPrediction.query.filter(BasketPrediction.created_at < expiry_date).delete()
    db.session.commit()
