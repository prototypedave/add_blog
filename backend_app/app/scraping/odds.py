from playwright.sync_api import Page

def odds_over_under(page: Page, href):
    try:
        page.goto(href+ '/' + 'over-under' + '/' + 'full-time')
        page.wait_for_selector(".filterOver")
        rows = page.locator(".ui-table__row").all()

        over_under = []
        
        for row in rows:
            try:
                over_under.append({
                    'total' : row.locator(".oddsCell__noOddsCell").first.inner_text().strip(),
                    'over' : row.locator(".oddsCell__odd").first.inner_text().strip(),
                    'under' : row.locator(".oddsCell__odd").last.inner_text().strip()
                })
            except Exception:
                continue
            
        return over_under
    except Exception:
        return []
    

def final_results_odds(page, href):
    try:
        page.goto(href + '/' + '1x2-odds' + '/' + 'full-time')
        page.wait_for_selector(".filterOver")
        row = page.locator(".ui-table__row").first
        cells = row.locator(".oddsCell__odd").all()
        if len(cells) == 3:
            return({
                'home': cells[0].inner_text().strip(),
                'draw': cells[1].inner_text().strip(),
                'away': cells[2].inner_text().strip()
            })
    except Exception:
        return []
    

def both_team_to_score_odds(page, href):
    try:
        page.goto(href + '/' + 'both-teams-to-score' + '/' + 'full-time')
        page.wait_for_selector(".filterOver")
        return({
            'yes': page.locator(".ui-table__row .oddsCell__odd").first.inner_text().strip(),
            'no' : page.locator(".ui-table__row .oddsCell__odd").last.inner_text().strip()
        })
         
    except Exception:
        return []
    

def handicap_odds(page, href):
    try:
        page.goto(href + '/' + 'asian-handicap/full-time')
        page.wait_for_selector(".filterOver")
        rows = page.locator(".ui-table__row").all()

        handicap = []
        
        for row in rows:
            try:
                handicap.append({
                    'handicap': row.locator(".oddsCell__noOddsCell").first.inner_text().strip(),
                    'home': row.locator(".oddsCell__odd").first.inner_text().strip(),
                    'away': row.locator(".oddsCell__odd").last.inner_text().strip()
                }) 
            except Exception:
                continue
        return handicap
    except Exception:
        return []
    

def get_odds(page: Page, href: str, prediction, bet_type: str):
    """
    Fetches the appropriate odds based on the bet type.
    
    :param page: The Page object used to scrape data.
    :param href: The URL to fetch odds from.
    :param prediction: The user's prediction (can be a string or dictionary).
    :param bet_type: The type of bet ('over_under', 'btts', 'fulltime', 'handicap').
    :return: The corresponding odds value or None if no matching odds are found.
    """

    # Map bet types to their respective fetching functions
    bet_functions = {
        "over_under": odds_over_under,
        "btts": both_team_to_score_odds,
        "fulltime": final_results_odds,
        "handicap": handicap_odds
    }

    fetch_odds = bet_functions.get(bet_type)
    
    if not fetch_odds:
        return None  

    odds_data = fetch_odds(page, href)
    
    if not odds_data:
        return None  

    # Over/Under odds
    if bet_type == "over_under":
        if isinstance(prediction, dict):
            for obj, key in prediction.items():
                if 'total' in obj:
                    best_odds = None
                    for k in odds_data:
                        total = float(k['total'])
                        if key <= total:
                            if best_odds is None or total < float(best_odds):
                                best_odds = k['over']
                    return best_odds
        elif isinstance(prediction, str):
            for k in odds_data:
                total = float(k['total'])
                if prediction.lower() == f"over {total}":
                    return k['over']
                if prediction.lower() == f"under {total}":
                    return k['under']

    # Both Teams to Score (BTTS) odds
    elif bet_type == "btts":
        if "btts no" in prediction:
            return odds_data['no']
        elif "btts" in prediction:
            return odds_data['yes']

    # Fulltime result odds
    elif bet_type == "fulltime":
        if isinstance(prediction, dict):
            for obj, key in prediction.items():
                if "win" in obj:
                    if "home" in key:
                        return odds_data["home"]
                    elif "away" in key:
                        return odds_data["away"]
        elif isinstance(prediction, str):
            if "home" in prediction:
                return odds_data["home"]
            elif "away" in prediction:
                return odds_data["away"]

    # Handicap odds
    elif bet_type == "handicap":
        if isinstance(prediction, dict):
            for obj, key in prediction.items():
                if "handicap" in obj:
                    best_odds = None
                    for k in odds_data:
                        total = float(k['handicap'])
                        if key <= total:
                            if best_odds is None or total < float(best_odds):
                                best_odds = k['over']
                    return best_odds

    return None  
