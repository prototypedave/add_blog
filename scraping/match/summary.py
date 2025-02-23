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

    # buttons
    buttons = match_page.locator(".detailOver a").all()
    
    #match_details(match_page=match_page)
    if len(buttons) > 3:
        odds_href = href[:href.rfind('#')] + buttons[2].get_attribute("href")
        h2h(browser=browser, href=odds_href)

    match_page.close()