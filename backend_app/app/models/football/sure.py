from datetime import datetime
from app.storage.database import db
from datetime import datetime, timedelta

class SurePrediction(db.Model):
    __tablename__ = 'sure_pred'

    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(100), nullable=False)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    prediction = db.Column(db.String(50), nullable=False)
    odds = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(50), default="-")
    form = db.Column(db.Text, nullable=False)
    h2h = db.Column(db.Text, nullable=False)
    missing = db.Column(db.Text, nullable=False)
    home_away = db.Column(db.Text, nullable=False)
    matchup = db.Column(db.Text, nullable=False)
    insights = db.Column(db.Text, nullable=False)
    chance = db.Column(db.Double(10))
    time = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now) 

    def to_dict(self):
        return {
            "id": self.id,
            "league": self.league,
            "homeTeam": self.home_team,
            "awayTeam": self.away_team,
            "prediction": self.prediction,
            "form": self.form,
            "h2h": self.h2h,
            "missing": self.missing,
            "home_away": self.home_away,
            "matchup": self.matchup,
            "insights": self.insights,
            "odds": self.odds,
            "result": self.result,
            "chance": self.chance,
            "time": self.time,
        }
    

def delete_sure_predictions(db):
    expiry_date = datetime.now() - timedelta(days=3)
    SurePrediction.query.filter(SurePrediction.created_at < expiry_date).delete()
    db.session.commit()
