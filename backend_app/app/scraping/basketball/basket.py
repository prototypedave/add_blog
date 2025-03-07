from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from app.scraping.events import get_events
from app.scraping.match_details import match_details, is_record_existing, update_score
from app.models.basketball import BasketPrediction
from datetime import datetime
from .h2h import get_h2h
from app.scraping.odds import get_odds


"""
    Gets flashscore data for basketball
"""
def scrape_basketball(page: Page, db):
    events = get_events(page=page, href="https://www.flashscore.co.ke/basketball/")

    for link in events:
        try:
            match = match_details(page, link)
        except Exception:
            continue
        
        home, away, time, score = match['home'], match['away'], match['time'], match['score']

        """if is_record_existing(db=db, table=BasketPrediction, home=home, away=away, time=time):
            update_score(db=db, table=BasketPrediction, home=home, away=away, time=time, score=score)
            continue"""  

        if datetime.strptime(time, "%d.%m.%Y %H:%M") <= datetime.now():
            continue
        
        prediction = get_h2h(page, link[:link.rfind('#')] + "#/h2h", home, away)
        if not prediction:
            continue

        for obj in prediction:
            if 'total' in obj:
                odds = get_odds(page, link[:link.rfind('#')] + "#/odds-comparison", prediction, 'over_under')
                print(odds)
                #create_and_save_prediction(db, match, home, away, score, time, prediction, odds, link)
                break  
            elif 'handicap' in obj:
                odds = get_odds(page, link[:link.rfind('#')] + "#/odds-comparison", prediction, 'handicap')
                print(odds)
                #create_and_save_prediction(db, match, home, away, score, time, prediction, odds, link)
                break
            elif 'win' in obj:
                odds = get_odds(page, link[:link.rfind('#')] + "#/odds-comparison", prediction, 'fulltime')
                print(odds)
                #create_and_save_prediction(db, match, home, away, score, time, prediction, odds, link)
                break  

        print(f"Home team: {home}, Prediction: {prediction}")

    
def create_and_save_prediction(db, match, home, away, score, time, prediction, odds, link):
    """Helper function to create and save a new prediction."""
    new_pred = BasketPrediction(
        league=match['country'],
        home_team=home,
        away_team=away,
        result=score,
        time=time,
        odds=odds,
        href=link,
    )
    new_pred.set_prediction(prediction)
    db.session.add(new_pred)
    db.session.commit()