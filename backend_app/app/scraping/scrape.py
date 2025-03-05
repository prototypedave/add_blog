from playwright.sync_api import sync_playwright, Page
from .basketball.basket import scrape_basketball


def run(page:Page, db):
    scrape_basketball(page, db)

"""
    Get flashscore matches for the day
"""
def flashscore(app, db):
    with app.app_context():
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            success = run(page, db)
            browser.close()

            return success