from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape_match_details(browser, href):
    """
        Gets data for individual games
    """
    # open a new page
    match_page = browser.new_page()
    match_page.goto(href, timeout=60000)
    match_page.wait_for_selector(".duelParticipant", timeout=10000)

    home_team = match_page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
    away_team = match_page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
    score = match_page.locator(".detailScore__wrapper").inner_text().strip()
    time = match_page.locator(".duelParticipant__startTime div").inner_text().strip()

    match_data = {
        'home': home_team,
        'away': away_team,
        'score': score,
        'time': time
    }
    print(match_data)

    match_page.close()


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

            # get match details
            scrape_match_details(browser=browser, href=href)
            
        browser.close()





scrape_flashscore()