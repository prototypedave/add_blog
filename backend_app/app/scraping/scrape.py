from playwright.sync_api import sync_playwright, Page
from .basketball.basket import scrape_basketball
from .hockey.ice_hockey import scrape_hockey


def run(page:Page, db):
    scrape_basketball(page, db)
    scrape_hockey(page, db)
    

"""
    Get flashscore matches for the day
"""
def flashscore(app, db):
    with app.app_context():
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            print("Scraping data...")
            success = run(page, db)
            browser.close()

            return success