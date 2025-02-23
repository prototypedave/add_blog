def odds(browser, href):
    page = browser.new_page()

    # 1x2 fulltime
    page.goto(href + '/1x2-odds/full-time')
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

    # over/under

    # BTTS

    # DC

    # HC
    
    
    

