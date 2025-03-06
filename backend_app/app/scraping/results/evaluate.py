from playwright.sync_api import sync_playwright, Page
from app.models.football.accumulator import AccumulatorPrediction
from app.models.football.best import BestPicksPrediction
from app.models.football.general import GeneralPrediction
from app.models.football.sure import SurePrediction
from app.models.basketball import BasketPrediction
from app.models.hockey import HockeyPrediction
from datetime import datetime, timedelta
from app.scraping.h2h import format_score

time_threshold = datetime.now() - timedelta(hours=24)

def update_results(db, page: Page):
    get_results(db, AccumulatorPrediction, page, get_football)
    get_results(db, BestPicksPrediction, page, get_football)
    get_results(db, GeneralPrediction, page, get_football)
    get_results(db, SurePrediction, page, get_football)
    get_results(db, BasketPrediction, page, get_basket)
    get_results(db, HockeyPrediction, page, get_hockey)
    

def get_results(db, table, page: Page, func):
    # Calculate the time threshold (last 24 hours)
    time_threshold = datetime.now() - timedelta(days=1)

    # Fetch records created in the last 24 hours
    records = db.query(table).filter(table.created_at >= time_threshold).all()

    if not records:
        print("No records found in the last 24 hours.")
        return

    for record in records:
        try:
            page.goto(record.href)
            score = page.locator(".detailScore__wrapper").inner_text().strip()
            score = format_score(score)
            win = func(score, record.prediction)
            record.result = score
            record.won = win

        except Exception as e:
            print(f"Error processing {record.href}: {e}")

    db.commit()


def get_football(score, prediction):
    prediction = prediction.lower()

    if not score or '-' not in score:
        return False

    try:
        a, b = map(int, score.split('-'))

        conditions = {
            'home win': a > b,
            'away win': b > a,
            'over 2.5': (a + b) > 2.5,
            'under 2.5': (a + b) < 2.5,
            'over 3.5': (a + b) > 3.5,
            'under 3.5': (a + b) < 3.5,
            'btts yes': a > 0 and b > 0,
            'btts no': a == 0 or b == 0
        }

        return conditions.get(prediction, False)

    except ValueError:
        return False
    

def get_hockey(score, prediction):
    prediction = prediction.lower()

    if not score or '-' not in score:
        return False

    try:
        a, b = map(int, score.split('-'))

        conditions = {
            'home win': a > b,
            'away win': b > a,
            'over 3.5': (a + b) > 2.5,
            'over 4.5': (a + b) > 3.5,
            'btts yes': a > 1 and b > 1,
        }

        return conditions.get(prediction, False)

    except ValueError:
        return False
    
def get_basket(score, prediction):
    prediction = prediction.lower()

    if not score or '-' not in score:
        return False

    try:
        a, b = map(int, score.split('-'))
        for obj in prediction:
            if 'home win' in obj and a > b:
                return True
            if 'away win' in obj and b > a:
                return True
            if 'total' in obj:
                if prediction['total'] > (a + b):
                    return True
            return False

    except ValueError:
        return False