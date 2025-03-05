from playwright.sync_api import Page

"""
    Returns prediction based on head-to-head analysis
"""
def get_h2h(page: Page, link: str, home: str, away: str):
    ovr_link = link + "/overall"
    home_link = link + "/home"
    away_link = link + "/away"
