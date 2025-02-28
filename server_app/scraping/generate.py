from playwright.sync_api import Page
from server_app.algorithms.projected_outcome import prediction_markets
from server_app.automation.groq_assistant import predict
from datetime import datetime

def is_generated_games_report(page: Page, db):
    page.goto("https://www.flashscoreusa.com/?rd=flashscore.us")
    page.wait_for_selector(".event__match")
    events = page.locator(".event__match").all()
    links = []
    for event in events:
        links.append(event.locator("a").first.get_attribute("href"))

    for link in links:
        page.goto(link)
        home_team = page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
        away_team = page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
        score = page.locator(".detailScore__wrapper").inner_text().strip()
        time = page.locator(".duelParticipant__startTime div").inner_text().strip()
        country = page.locator(".tournamentHeader__country").inner_text().strip()

        markets_to_predict = prediction_markets(get_h2h_details(page, link[:link.rfind('#')] + "#/h2h"))

        # Only predict potential games
        if markets_to_predict:
            # Predict on markets that havent played yet
            if datetime.strptime(time, "%d.%m.%Y %H:%M") > datetime.now():
                prediction = predict(home_team, away_team, markets_to_predict)


    return True


def get_h2h_details(page: Page, link: str):
    page.goto(link)
    page.wait_for_selector(".h2h__section")
    h2h = page.locator(".h2h__section").all()
    _h2h = [] 
    for hh in h2h:
        _h2h.append(get_h2h_object(hh))

    return _h2h


def get_h2h_object(h2h):
    head = h2h.locator("div").first.inner_text().strip()
    previous = h2h.locator(".rows .h2h__row").all()
    matches = []
    
    for row in previous:
        matches.append(get_matches(row))    
    
    return({
        'header': head,
        'matches': matches
    })


def get_matches(row):
    return({
        'date': row.locator(".h2h__date").inner_text().strip(),
        'event': row.locator(".h2h__event").inner_text().strip(),
        'home': row.locator(".h2h__homeParticipant").inner_text().strip(),
        'away': row.locator(".h2h__awayParticipant").inner_text().strip(),
        'result': format_score(row.locator(".h2h__result").inner_text().strip()),
        'icon': row.locator(".h2h__icon").inner_text().strip()
    })


def format_score(raw_score):
    parts = raw_score.split("\n")  
    parts = [p.strip() for p in parts if p.strip()]
    return "-".join(parts)