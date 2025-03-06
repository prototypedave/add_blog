from playwright.sync_api import Page
from app.scraping.h2h import get_h2h_details
from .stats.win import overall_percent_win, side_percent_win
from .stats.btts import overall_percent_btts, side_percent_btts
from .stats.over import overall_percent_over, side_percent_over
from .stats.total import overall_percent_total, side_percent_total
from app.algorithms.football.btts import get_btts
from app.algorithms.football.over import get_total_25
from app.algorithms.football.total35 import get_total_35
from app.algorithms.football.win import get_winner


def get_h2h_data(page: Page, link: str, categories: list):
    return {category: get_h2h_details(page, f"{link}/{category}") for category in categories}


def get_stat_object(overall_func, side_func, overall, home_h2h, away_h2h, home=None, away=None):
    return {
        "ovr": overall_func(overall, home, away) if home and away else overall_func(overall),
        "home": side_func(home_h2h, home) if home else side_func(home_h2h),
        "away": side_func(away_h2h, away) if away else side_func(away_h2h),
    }

def get_h2h_football(page: Page, link, home, away):
    h2h_data = get_h2h_data(page, link, ["overall", "home", "away"])
    overall, home_h2h, away_h2h = h2h_data["overall"], h2h_data["home"], h2h_data["away"]
    
    # Generate statistic objects
    win_object = get_stat_object(overall_percent_win, side_percent_win, overall, home_h2h, away_h2h, home, away)
    btts_object = get_stat_object(overall_percent_btts, side_percent_btts, overall, home_h2h, away_h2h)
    over_object = get_stat_object(overall_percent_over, side_percent_over, overall, home_h2h, away_h2h)
    total_object = get_stat_object(overall_percent_total, side_percent_total, overall, home_h2h, away_h2h)

    # Calculate market outcomes
    market = [
        outcome for outcome in [
            get_btts(btts_object),
            get_total_25(over_object),
            get_total_35(total_object),
            get_winner(win_object)
        ] if outcome
    ]

    return market
