from app.models.football.accumulator import AccumulatorPrediction
from app.models.football.best import BestPicksPrediction
from app.models.football.general import GeneralPrediction
from app.models.football.sure import SurePrediction
from app.models.basketball import BasketPrediction
from app.models.hockey import HockeyPrediction


def calculate_win_percentage(db, table):
    """Calculate the percentage of winning predictions."""
    total_records = db.session.query(table).count()
    if total_records == 0:
        return 0.0  

    won_count = db.session.query(table).filter_by(won=True).count()
    win_percentage = (won_count / total_records) * 100
    return round(win_percentage, 2)

def win_percentage(db):
    accumulator = calculate_win_percentage(db, AccumulatorPrediction)
    best = calculate_win_percentage(db, BestPicksPrediction)
    general = calculate_win_percentage(db, GeneralPrediction)
    sure = calculate_win_percentage(db, SurePrediction)
    basket = calculate_win_percentage(db, BasketPrediction)
    hockey = calculate_win_percentage(db, HockeyPrediction)

    return {
        "accumulator": accumulator,
        "best": best,
        "general": general,
        "sure": sure,
        "basket": basket,
        "hockey": hockey
    }