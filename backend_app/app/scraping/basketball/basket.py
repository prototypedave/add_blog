from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from app.scraping.events import get_events

"""
    Gets flashscore data for basketball
"""
def scrape_basketball(page: Page, db):
    events = get_events(page=page, href="https://www.flashscore.co.ke/basketball/")
    print(events)