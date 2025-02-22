from .match_details import match_details

def scrape_match_details(browser, href):
    """
        Gets data for individual games
    """
    # open a new page
    match_page = browser.new_page()
    match_page.goto(href, timeout=60000)
    match_page.wait_for_selector(".duelParticipant", timeout=10000)
    
    match_details(match_page=match_page)

    match_page.close()