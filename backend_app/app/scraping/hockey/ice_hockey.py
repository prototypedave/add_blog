from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from app.scraping.events import get_events
from app.scraping.match_details import match_details, is_record_existing, update_score
from app.models.hockey import HockeyPrediction
from datetime import datetime
from .h2h import h2h_hockey

"""
    Gets flashscore data for basketball
"""
def scrape_hockey(page: Page, db):
    events = get_events(page=page, href="https://www.flashscore.co.ke/basketball/")
    for link in events:
        match = match_details(page, link)

        home = match['home']
        away = match['away']
        time = match['time']
        score = match['score']

        record = is_record_existing(db=db, table=HockeyPrediction, home=home, away=away, time=time)

        if not record:
            # Check if a match is viable for prediction
            if datetime.strptime(time, "%d.%m.%Y %H:%M") > datetime.now():
                prediction = h2h_hockey(page, link[:link.rfind('#')] + "#/h2h", home, away, time, match['country'])
                if prediction:
                    new_pred = HockeyPrediction(
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
        elif record:
            # Update score
            update_score(db=db, table=HockeyPrediction, home=home, away=away, time=time, score=score)