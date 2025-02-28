from .stats.btts import get_btts_score, get_btts_score_ovr
from .stats.nobtts import get_ng_score, get_ng_score_ovr
from .stats.over25 import get_over25_ovr, get_over25_score
from .stats.under25 import get_under25_ovr, get_under25_score
from .stats.windrawwin import get_away_score, get_home_score, get_1x2_ovr 
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

"""
    Helper function
"""
def format_score(raw_score):
    parts = raw_score.split("\n")  
    parts = [p.strip() for p in parts if p.strip()]
    return "-".join(parts)

"""
    Returns an object containing an h2h match details
"""
def get_matches(row):
    return({
        'date': row.locator(".h2h__date").inner_text().strip(),
        'event': row.locator(".h2h__event").inner_text().strip(),
        'home': row.locator(".h2h__homeParticipant").inner_text().strip(),
        'away': row.locator(".h2h__awayParticipant").inner_text().strip(),
        'result': format_score(row.locator(".h2h__result").inner_text().strip()),
        'icon': row.locator(".h2h__icon").inner_text().strip()
    })

"""
    Returns a list of h2h matches
"""
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

"""
    Returns h2h data
"""
def get_h2h(page: Page, href):
    try:
        page.goto(href)
        page.wait_for_selector(".h2h__section")

        h2h = page.locator(".h2h__section").all()
        _h2h = []
        
        for h2h in h2h:
            _h2h.append(get_h2h_object(h2h))

        return _h2h
    except PlaywrightTimeoutError:
        return []


"""
    Returns stats in an organized object
"""
def organize_stats(func, func2, func3, page: Page, ovr, home, away):
    return {
        'ovr' : func(get_h2h(page, ovr)),
        'home' : func2(get_h2h(page, home)),
        'away': func3(get_h2h(page, away)),
    }

"""
    Returns a given match statistical data for the last 5 games
"""
def get_stats(h2h_page: Page, ovr, home, away):
    return ({
        'btts_stats' : organize_stats(get_btts_score_ovr, get_btts_score, get_btts_score, h2h_page, ovr, home, away),
        'ng_stats' : organize_stats(get_ng_score_ovr, get_ng_score, get_btts_score, h2h_page, ovr, home, away),
        'over25_stats' : organize_stats(get_over25_ovr, get_over25_score, get_btts_score, h2h_page, ovr, home, away),
        'under25_stats' : organize_stats(get_under25_ovr, get_under25_score, get_btts_score, h2h_page, ovr, home, away),
        'winDrawWin_stats' : organize_stats(get_1x2_ovr, get_home_score, get_away_score, h2h_page, ovr, home, away)
    })

"""
    Returns all h2h data
"""
def h2h(browser, href):
    h2h_page = browser.new_page()
    ovr = href + "/overall"
    home = href + "/home"
    away = href + "/away"

    stats = get_stats(h2h_page, ovr, home, away)
    
    return stats
    
    

    

