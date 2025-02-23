def extract_odds(match_page, href):
    match_page.goto(href, timeout=60000)
    match_page.wait_for_load_state("networkidle") 

    locator = match_page.locator("//div[1]/div/div[8]/div/div[3]/div/div[2]/div[1]/a[1]/span")
    
    locator.wait_for(state="visible", timeout=10000)  

    home = locator.inner_text().strip() 
    print(home)

    