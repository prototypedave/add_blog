from playwright.sync_api import sync_playwright, Page
from .results.evaluate import update_results


def run(page:Page, db):
    update_results(db, page)
    print('Results Updated')
    return True
            

"""
    Get flashscore matches for the day
"""
def flashscore_results(app, db):
    with app.app_context():
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            print("Scraping data...")
            success = run(page, db)
            browser.close()

            return success