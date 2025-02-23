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
    print(len(rows))

    over_under = []
    
    for row in rows:
        try:
            total = row.locator(".oddsCell__noOddsCell").first.inner_text().strip()
            over = row.locator(".oddsCell__odd").first.inner_text().strip()
            under = row.locator(".oddsCell__odd").last.inner_text().strip()
        except Exception:
            continue
        
        over_under.append({
            'total': total,
            'over': over,
            'under': under
        })
        
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


def odds(browser, href):
    page = browser.new_page()

    # Final results odds
    full_time = final_results_odds(page=page, href=href + '/1x2-odds/full-time')
    first_half = final_results_odds(page=page, href=href + '/1x2-odds/1st-half')
    second_half = final_results_odds(page=page, href=href + '/1x2-odds/2nd-half')

    # Over under
    over_under_full_time = over_under_odds(page=page, href=href + '/over-under/full-time')
    over_under_1st_half = over_under_odds(page=page, href=href + '/over-under/1st-half')
    over_under_2nd_half = over_under_odds(page=page, href=href + '/over-under/2nd-half')

    # Both teams to Score
    btts_full_time = both_team_to_score_odds(page=page, href=href + '/both-teams-to-score/full-time')
    btts_1st_half = both_team_to_score_odds(page=page, href=href + '/both-teams-to-score/1st-half')
    btts_2nd_half = both_team_to_score_odds(page=page, href=href + '/both-teams-to-score/2nd-half')

    # Double chance
    dc_full_time = double_chance_results_odds(page=page, href=href + '/double-chance/full-time')
    dc_1st_half = double_chance_results_odds(page=page, href=href + '/double-chance/1st-half')
    dc_2nd_half = double_chance_results_odds(page=page, href=href + '/double_chance/2nd-half')

    return dc_1st_half

    # HC
    
    
    

