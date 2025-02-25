from .match_details import match_details
from .h2h import h2h
from .odds import odds
from .predictions.predict import get_prediction
import csv

def scrape_match_details(browser, href):
    """
        Gets data for individual games
    """
    # open a new page
    match_page = browser.new_page()
    match_page.goto(href)
    match_page.wait_for_selector(".duelParticipant")

    #match_data = match_details(match_page=match_page)
    # Navigate to h2h section
    h2h(browser=browser, href=href[:href.rfind('#')] + "#/h2h")
    
    
    # Navigate to odds section
    #odd = odds(browser=browser, href=href[:href.rfind('#')] + "#/odds-comparison")
    #print(odd)

    match_page.close()