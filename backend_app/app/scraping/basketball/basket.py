from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

"""
    Gets flashscore data for basketball
"""
def scrape_basketball(page: Page, db):
    page.goto("https://www.flashscore.co.ke/basketball/")
    page.wait_for_selector(".event__match")
    events = page.locator(".event__match").all()
    print(events)