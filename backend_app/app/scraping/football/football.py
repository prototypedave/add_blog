from playwright.sync_api import Page
from app.scraping.events import get_events
from app.scraping.match_details import match_details, is_record_existing, update_score
from app.models.football.general import GeneralPrediction
from datetime import datetime
from .h2h import get_h2h_football

"""
    Get flashscore data for football
"""
def scrape_football(page: Page, db):
    events = get_events(page=page, href="https://www.flashscoreusa.com/?rd=flashscore.us")
    
    for link in events:
        match = match_details(page, link)
        home, away, time, score = match['home'], match['away'], match['time'], match['score']

        if is_record_existing(db=db, table=GeneralPrediction, home=home, away=away, time=time):
            update_score(db=db, table=GeneralPrediction, home=home, away=away, time=time, score=score)
            continue

        if datetime.strptime(time, "%I:%M %p, %B %d, %Y") <= datetime.now():
            continue

        get_h2h_football(page, link[:link.rfind('#')] + "#/h2h")