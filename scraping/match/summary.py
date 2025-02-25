from .match_details import match_details
from .h2h import h2h
from .odds import odds
from .predictions.predict import get_prediction
from .models.algorithms import perfect_away_record

def scrape_match_details(browser, href):
    """
        Gets data for individual games
    """
    # open a new page
    match_page = browser.new_page()
    match_page.goto(href)
    match_page.wait_for_selector(".duelParticipant")

    match_data = match_details(match_page=match_page)
    stats = h2h(browser=browser, href=href[:href.rfind('#')] + "#/h2h")
    print(perfect_away_record(stats))
    print(stats)

    
    
    
    # Navigate to odds section
    #odd = odds(browser=browser, href=href[:href.rfind('#')] + "#/odds-comparison")
    #print(odd)

    match_page.close()