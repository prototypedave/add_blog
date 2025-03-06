from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from app.scraping.events import get_events
from app.scraping.match_details import match_details, is_record_existing, update_score
from app.models.basketball import BasketPrediction
from datetime import datetime
from .h2h import get_h2h
from app.scraping.odds import odds_over_under


"""
    Gets flashscore data for basketball
"""
def scrape_basketball(page: Page, db):
    events = get_events(page=page, href="https://www.flashscore.co.ke/basketball/")

    for link in events:
        match = match_details(page, link)
        home, away, time, score = match['home'], match['away'], match['time'], match['score']

        if is_record_existing(db=db, table=BasketPrediction, home=home, away=away, time=time):
            update_score(db=db, table=BasketPrediction, home=home, away=away, time=time, score=score)
            continue  

        if datetime.strptime(time, "%d.%m.%Y %H:%M") <= datetime.now():
            continue
        
        prediction = get_h2h(page, link[:link.rfind('#')] + "#/h2h", home, away)
        if not prediction:
            continue

        for obj in prediction:
            if 'total' in obj:
                odds = odds_over_under(page, link[:link.rfind('#')] + "#/odds-comparison")
                if odds and int(odds[0]['over']) < obj['total']:
                    create_and_save_prediction(db, match, home, away, score, time, prediction)
                    break  
            else:
                create_and_save_prediction(db, match, home, away, score, time, prediction)
                break  

        print(f"Home team: {home}, Prediction: {prediction}")

    
def create_and_save_prediction(db, match, home, away, score, time, prediction):
    """Helper function to create and save a new prediction."""
    new_pred = BasketPrediction(
        league=match['country'],
        home_team=home,
        away_team=away,
        result=score,
        time=time
    )
    new_pred.set_prediction(prediction)
    db.session.add(new_pred)
    db.session.commit()