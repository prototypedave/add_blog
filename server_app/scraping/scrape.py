from playwright.sync_api import sync_playwright, Page
from .generate import is_generated_games_report
from .hockey import get_hockey
from .basket import get_basket

def run(page:Page, db):
    #get_basket(page, db)
    #get_hockey(page, db)
    return is_generated_games_report(page, db)

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