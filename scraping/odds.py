def extract_odds(match_page):
    """Extracts match odds."""
    try:
        match_page.locator('text="ODDS"').click()
        match_page.wait_for_load_state("networkidle")

        odds = match_page.locator(".oddsCell__odd").all_text_contents()  
        print(odds)
    except:
        odds = "N/A"

    return {"Odds": odds}