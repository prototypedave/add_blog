from .match_details import match_details
from .previous_matches import h2h

def scrape_match_details(browser, href):
    """
        Gets data for individual games
    """
    # open a new page
    match_page = browser.new_page()
    match_page.goto(href)
    match_page.wait_for_selector(".duelParticipant")

    # Navigate to h2h section
    h2h(browser=browser, href=href[:href.rfind('#')] + "#/h2h")

    match_page.close()