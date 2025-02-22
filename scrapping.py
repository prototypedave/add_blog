from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape_flashscore():
    """
        Get flashscore matches for the day
    """
    with sync_playwright() as p:
        # create a browser instance and load the page of the given url
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()
        page.goto("https://www.flashscore.co.ke/", timeout=60000)

        # choose selector and wait for it to load
        page.wait_for_selector(".event__match", timeout=10000)

        # Get events
        events = page.locator(".event__match").all()
        
        for event in events:
            match_link = event.locator("a").first
            href = match_link.get_attribute("href")
            print(href)

        browser.close()
scrape_flashscore()