def final_results_odds(page, href):
    page.goto(href)
    page.wait_for_selector(".filterOver")
    row = page.locator(".ui-table__row").first
    cells = row.locator(".oddsCell__odd").all()
    if len(cells) == 3:
        return({
            'home': cells[0].inner_text().strip(),
            'draw': cells[1].inner_text().strip(),
            'away': cells[2].inner_text().strip()
        })
    
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

    return over_under_1st_half

    # Both teams to Score


    # BTTS

    # DC

    # HC
    
    
    

