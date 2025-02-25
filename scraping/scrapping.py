from playwright.sync_api import sync_playwright
from match.summary import scrape_match_details


def scrape_flashscore():
    """
        Get flashscore matches for the day
    """
    with sync_playwright() as p:
        # create a browser instance and load the page of the given url
        browser = p.chromium.launch(headless=True) 
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.flashscore.co.ke/")

        # choose selector and wait for it to load
        page.wait_for_selector(".event__match")

        # Get events
        events = page.locator(".event__match").all()
        events  = events[::-1]
        
        for event in events:
            match_link = event.locator("a").first
            href = match_link.get_attribute("href")

            # get match details
            data = scrape_match_details(browser=browser, href=href)
            

        
        context.close()    
        browser.close()





scrape_flashscore()