import re
from playwright.sync_api import sync_playwright, Page, expect

def get_match_link(page: Page):
    page.goto("https://www.flashscoreusa.com/?rd=flashscore.us")
    page.wait_for_selector(".event__match")
    events = page.locator(".event__match").all()
    links = []
    for event in events:
        links.append(event.locator("a").first.get_attribute("href"))
        
    return links

def get_match_details(page: Page, links: list):
    for link in links:
        page.goto(link)
        home_team = page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
        away_team = page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
        score = page.locator(".detailScore__wrapper").inner_text().strip()
        time = page.locator(".duelParticipant__startTime div").inner_text().strip()
        country = page.locator(".tournamentHeader__country").inner_text().strip()
        
        h2h = get_h2h_details(page, link[:link.rfind('#')] + "#/h2h")
        match_data = {
            'home': home_team,
            'away': away_team,
            'score': score,
            'time': time,
            'league': country
        }

        print(h2h)

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


def run(page:Page):
    links = get_match_link(page)
    get_match_details(page, links)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    run(page)
    browser.close()