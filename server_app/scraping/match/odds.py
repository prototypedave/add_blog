def final_results_odds(page, href):
    page.goto(href)
    page.wait_for_selector(".filterOver")

    try:
        row = page.locator(".ui-table__row").first
        cells = row.locator(".oddsCell__odd").all()
        if len(cells) == 3:
            return({
                'home': cells[0].inner_text().strip(),
                'draw': cells[1].inner_text().strip(),
                'away': cells[2].inner_text().strip()
            })
    except Exception:
        return None


def over_under_odds(page, href):
    page.goto(href)
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


def both_team_to_score_odds(page, href):
    page.goto(href)
    page.wait_for_selector(".filterOver")
    
    try:
        # Assuming oddsCell__odd will always be two on this page
        return({
            'yes': page.locator(".ui-table__row .oddsCell__odd").first.inner_text().strip(),
            'no' : page.locator(".ui-table__row .oddsCell__odd").last.inner_text().strip()
        }) 
    except Exception:
        return None
    

def double_chance_results_odds(page, href):
    page.goto(href)
    page.wait_for_selector(".filterOver")

    try:
        row = page.locator(".ui-table__row").first
        cells = row.locator(".oddsCell__odd").all()
        if len(cells) == 3:
            return({
                '1x': cells[0].inner_text().strip(),
                '12': cells[1].inner_text().strip(),
                'x2': cells[2].inner_text().strip()
            })
    except Exception:
        return None
    

def handicap_odds(page, href):
    page.goto(href)
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


def arrange_objects(func, page, href, mkt):
    # Full time
    ft = func(page, href + '/' + mkt + '/' + 'full-time')

    # first half
    h1 = func(page, href + '/' + mkt + '/' + '1st-half')

    # second half
    h2 = func(page, href + '/' + mkt + '/' + '2nd-half')

    return ({
        'full_time' : ft,
        'first_half' : h1,
        'second_half' : h2
    })


def odds(browser, href):
    page = browser.new_page()

    # Final results odds
    final_results = arrange_objects(final_results_odds, page, href, '1x2-odds')

    # Over under
    over_under = arrange_objects(over_under_odds, page, href, 'over-under')
   
    # Both teams to Score
    both_team_to_score = arrange_objects(both_team_to_score_odds, page, href, 'both-teams-to-score')
    
    # Double chance
    double_chance = arrange_objects(double_chance_results_odds, page, href, 'double-chance')
    
    # Handicap
    handicap = arrange_objects(handicap_odds, page, href, 'asian-handicap')
    
    return ({
      'result' : final_results,
      'over/under' : over_under,
      'BTTS' : both_team_to_score,
      'DC' : double_chance,
      'handicap' : handicap  
    })
