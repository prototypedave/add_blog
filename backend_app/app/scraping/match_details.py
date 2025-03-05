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