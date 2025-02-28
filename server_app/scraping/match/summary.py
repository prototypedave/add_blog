from .match_details import match_details
from .h2h import h2h
from .odds import odds
from .predictions.predict import get_prediction
from .models.markets import find_perfect_market
from .automation.groq_assistant import predict
from .models.accumulators import perfect_options
from .models.algorithm import prediction_markets
from datetime import datetime
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from server_app.models.predictions import MatchPrediction
from playwright.sync_api import Page

def scrape_match_details(page, href, db):
    """
        Gets data for individual games
    """
    try:
        match_data = match_details(page, href)
        stats = h2h(page, href[:href.rfind('#')] + "#/h2h")
        print(match_data)

        if stats:
            #raw_data = find_perfect_market(stats)
            expected_mkts = perfect_options(stats)
            mkts = prediction_markets(stats)

            if datetime.strptime(match_data.get('time'), "%d.%m.%Y %H:%M") > datetime.now():
                if mkts:
                    prediction = predict(match_data.get('home'), match_data.get('away'), mkts)
                    print(f"{match_data.get('home')} : {prediction} : {mkts} : {expected_mkts}")
                    db_pred = MatchPrediction(
                        league=match_data["league"],
                        home_team=match_data["home"],
                        away_team=match_data["away"],
                        prediction=prediction["prediction"],
                        odds=prediction["odds"],
                        result=match_data["score"],
                        reason=prediction["reason"],
                        chance=prediction["chance"],
                        time=match_data["time"]
                    )
                    db.session.add(db_pred)
                    db.session.commit()

    except PlaywrightTimeoutError:
        print("Skipped")
    
    page.close()