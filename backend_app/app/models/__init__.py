from app.storage.database import db
from .basketball import BasketPrediction
from .hockey import HockeyPrediction
from .football.accumulator import AccumulatorPrediction
from .football.best import BestPicksPrediction
from .football.general import GeneralPrediction
from .football.sure import SurePrediction

def register_models(app):
    """Import all models to ensure they are registered with SQLAlchemy."""
    with app.app_context():
        db.create_all()