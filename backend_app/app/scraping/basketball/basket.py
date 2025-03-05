from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from app.scraping.events import get_events
from app.scraping.match_details import match_details

"""
    Gets flashscore data for basketball
"""
def scrape_basketball(page: Page, db):
    events = get_events(page=page, href="https://www.flashscore.co.ke/basketball/")
    for link in events:
        match = match_details(page, link)
        print(match)