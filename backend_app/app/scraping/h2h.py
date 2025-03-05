from playwright.sync_api import Page

"""
    Returns list of h2h section based on the link provided
"""
def get_h2h_details(page: Page, link: str):
    page.goto(link)
    page.wait_for_selector(".h2h__section")
    h2h = page.locator(".h2h__section").all()
    _h2h = [] 
    for hh in h2h:
        _h2h.append(get_h2h_object(hh))

    return _h2h


"""
    Returns an object with all the matches found in the given h2h section
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
    Returns an object of match details and result from the h2h object
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
    Helper function
"""
def format_score(raw_score):
    parts = raw_score.split("\n")  
    parts = [p.strip() for p in parts if p.strip()]
    return "-".join(parts)