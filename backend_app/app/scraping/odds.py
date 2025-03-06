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