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
def get_h2h(page, href):
    page.goto(href)
    page.wait_for_selector(".h2h__section")

    h2h = page.locator(".h2h__section").all()
    _h2h = []
    
    for h2h in h2h:
        _h2h.append(get_h2h_object(h2h))

    return _h2h

"""
    Returns all fulltime h2h data
"""
def h2h(browser, href):
    h2h_page = browser.new_page()
    return ({
        'type': 'fulltime',
        'ovr': get_h2h(page=h2h_page, href = href + "/overall"), # Overall h2h
        'home': get_h2h(page=h2h_page, href = href + "/home"), # Home team h2h
        'away': get_h2h(page=h2h_page, href = href + "/away"), # Away team h2h
    })
    
    
    

