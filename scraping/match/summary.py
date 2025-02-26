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

def scrape_match_details(browser, href):
    """
        Gets data for individual games
    """
    # open a new page
    match_page = browser.new_page()
    try:
        match_page.goto(href)
        match_page.wait_for_selector(".duelParticipant")

        match_data = match_details(match_page=match_page)
        stats = h2h(browser=browser, href=href[:href.rfind('#')] + "#/h2h")

        if stats:
            #raw_data = find_perfect_market(stats)
            expected_mkts = perfect_options(stats)
            mkts = prediction_markets(stats)

            if datetime.strptime(match_data.get('time'), "%d.%m.%Y %H:%M") > datetime.now():
                if mkts:
                    prediction = predict(match_data.get('home'), match_data.get('away'), mkts)
                    print(f"{match_data.get('home')} : {prediction} : {mkts} : {expected_mkts}")
    except PlaywrightTimeoutError:
        print("Skipped")
    
    
    
    
    # Navigate to odds section
    #odd = odds(browser=browser, href=href[:href.rfind('#')] + "#/odds-comparison")
    #print(odd)

    match_page.close()