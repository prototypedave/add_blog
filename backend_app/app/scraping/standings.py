from playwright.sync_api import Page

def get_table_standings(page: Page, href: str):
    try: 
        page.goto(href)
        page.wait_for_selector(".tableWrapper")
        participants = page.locator(".table__row--selected").all()

        stats = []
            
        for participant in participants:
            team = participant.locator(".tableCellParticipant__name").inner_text().strip()
            played = participant.locator(".table__cell--value").first.inner_text().strip()
            scored, conceeded = format_goals(participant.locator(".table__cell--score").inner_text().strip())
            points = participant.locator(".table__cell--points").inner_text().strip()
            stats.append({'team' : team, 'played': int(played), 'scored': scored, 'conceeded': conceeded, 'points': int(points)})
        
        return stats
    except Exception:
        return []


def format_goals(gls: str):
    try:
        scored, conceeded = map(int, gls.split(':'))
        return scored, conceeded
    except ValueError:
        return None