from playwright.sync_api import Page

"""
    Returns all the games for a given sport
"""
def get_events(page: Page, href: str):
    page.goto(href)
    page.wait_for_selector(".event__match")
    events = page.locator(".event__match").all()
    
    links = []
    
    for event in events:
        links.append(event.locator("a").first.get_attribute("href"))
    
    return links