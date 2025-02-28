from playwright.sync_api import sync_playwright, Page

def match_details(page: Page, href):
    page.goto(href)
    home_team = page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
    away_team = page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
    score = page.locator(".detailScore__wrapper").inner_text().strip()
    time = page.locator(".duelParticipant__startTime div").inner_text().strip()
    country = page.locator(".tournamentHeader__country").inner_text().strip()

    match_data = {
        'home': home_team,
        'away': away_team,
        'score': score,
        'time': time,
        'league': country
    }

    return match_data