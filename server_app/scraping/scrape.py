from playwright.sync_api import sync_playwright
from .match.summary import scrape_match_details
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

def flashscore(app, db):
    """
        Get flashscore matches for the day
    """
    with app.app_context():
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True) 
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.flashscore.com/")

            page.wait_for_selector(".event__match")

            events = page.locator(".event__match").all()
            track = len(events)
            success = False
                
            for event in events:
                match_link = event.locator("a").first
                href = match_link.get_attribute("href")
                scrape_match_details(browser=browser, href=href, db=db)
                if event == events[track-1]:
                    success = True
            
            context.close()    
            browser.close()

            return success