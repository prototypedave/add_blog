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
def get_h2h(h2h):
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
    Returns overall h2h section
"""
def get_overall_h2h(page, href):
    href = href + "/overall"
    page.goto(href)
    page.wait_for_selector(".h2h__section")

    overall = page.locator(".h2h__section").all()
    ovr_h2h = []
    
    for h2h in overall:
        ovr_h2h.append(get_h2h(h2h))

    return ovr_h2h

"""
    Returns H2H for home team
"""
def get_home_h2h(page, href):
    href = href + "/home"
    page.goto(href)
    page.wait_for_selector(".h2h__section")

    home = page.locator(".h2h__section").all()
    home_h2h = []

    for h2h in home:
        home_h2h.append(get_h2h(h2h))

    return home_h2h

"""
    Returns H2H data
"""
def h2h(browser, href):
    h2h_page = browser.new_page()
    
    # Overall head to head data
    ovr = get_overall_h2h(page=h2h_page, href=href)
    home = get_home_h2h(page=h2h_page, href=href)
    print(home)
    
    

