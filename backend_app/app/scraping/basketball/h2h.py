from playwright.sync_api import Page
from app.scraping.h2h import get_h2h_details
from app.algorithms.basket import predict_basketball
from .stats.over import total_over
from .stats.handicap import get_handicap_value
from .stats.win import get_team_win

"""
    Returns prediction based on head-to-head analysis
"""
def get_h2h(page: Page, link: str, home: str, away: str):
    ovr_link = link + "/overall"
    home_link = link + "/home"
    away_link = link + "/away"

    ovr_results  = get_h2h_details(page, ovr_link)
    home_results = get_h2h_details(page, home_link)
    away_results = get_h2h_details(page, away_link)
    
    total = total_over(ovr_results, home_results, away_results, home, away)
    hc = get_handicap_value(ovr_results)
    win = get_team_win(ovr_results, home, away)
    return predict_basketball(ovr_results, total, hc, win)
