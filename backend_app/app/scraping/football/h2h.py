from playwright.sync_api import Page
from app.scraping.h2h import get_h2h_details

def get_h2h_football(page: Page, link):
    ovr = link + "/overall"
    home = link + "/home"
    away = link + "/away"
    h2h = get_h2h_details(page, ovr)
    print(len(h2h))