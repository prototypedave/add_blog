from playwright.sync_api import Page

"""
    Return match data
"""
def match_details(page: Page, href: str):
    page.goto(href)
    home = page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
    away = page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
    score = page.locator(".detailScore__wrapper").inner_text().strip()
    time = page.locator(".duelParticipant__startTime div").inner_text().strip()
    country = page.locator(".tournamentHeader__country").inner_text().strip()

    return {
        'home': home,
        'away': away,
        'score': score,
        'time': time,
        'country': country
    }


"""
    Checks if a match is already saved in DB
"""
def is_record_existing(db, table, home, away, time):
    if db.session.query(table).filter_by(
        home_team=home,
        away_team=away,
        time=time
    ).first():
        return True
    return False
    

"""
    Checks if we have current results is already saved in DB
"""
def update_score(db, table, home, away, time, score):
    record = db.session.query(table).filter_by(
        home_team=home,
        away_team=away,
        time=time,
    ).first()
    record.result = score
    db.session.commit()
