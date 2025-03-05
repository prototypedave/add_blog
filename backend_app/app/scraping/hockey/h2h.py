from playwright.sync_api import Page
from app.scraping.h2h import get_h2h_details
from .stats.win import get_team_win
from app.algorithms.hockey import get_hockey_prediction
from .stats.over import overall_over
from .stats.btts import overall_btts

def h2h_hockey(page: Page, link: str, home: str, away: str, time: str, country: str):
    h2h = get_h2h_details(page, link[:link.rfind('#')] + "#/h2h")
    win = get_team_win(h2h, home, away, time, country)
    over = overall_over(h2h)
    btts = overall_btts(h2h)
    return get_hockey_prediction(over, btts, win)