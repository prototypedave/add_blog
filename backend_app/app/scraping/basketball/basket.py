from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from app.scraping.events import get_events
from app.scraping.match_details import match_details, is_record_existing, update_score
from app.models.basketball import BasketPrediction
from datetime import datetime
from .h2h import get_h2h

"""
    Gets flashscore data for basketball
"""
def scrape_basketball(page: Page, db):
    events = get_events(page=page, href="https://www.flashscore.co.ke/basketball/")
    for link in events:
        match = match_details(page, link)

        home = match['home']
        away = match['away']
        time = match['time']
        score = match['score']

        if not is_record_existing(db=db, table=BasketPrediction, home=home, away=away, time=time):
            # Check if a match is viable for prediction
            if datetime.strptime(time, "%I:%M %p, %B %d, %Y") > datetime.now():
                prediction = get_h2h(page, link[:link.rfind('#')] + "#/h2h", home, away)
                if prediction:
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
                    print(f"Home team: {home}, Prediction: {prediction}")
        # Update score
        update_score(db=db, table=BasketPrediction, home=home, away=away, time=time, score=score)