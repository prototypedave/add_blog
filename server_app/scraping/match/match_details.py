def match_details(match_page):
    home_team = match_page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
    away_team = match_page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
    score = match_page.locator(".detailScore__wrapper").inner_text().strip()
    time = match_page.locator(".duelParticipant__startTime div").inner_text().strip()
    country = match_page.locator(".tournamentHeader__country").inner_text().strip()

    match_data = {
        'home': home_team,
        'away': away_team,
        'score': score,
        'time': time,
        'league': country
    }

    return match_data