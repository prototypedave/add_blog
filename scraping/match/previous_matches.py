def format_score(raw_score):
    parts = raw_score.split("\n")  
    parts = [p.strip() for p in parts if p.strip()]
    return "-".join(parts)


def h2h(browser, href):
    h2h_page = browser.new_page()
    # for overall add overall to the link
    href = href + "/overall"
    h2h_page.goto(href)
    h2h_page.wait_for_selector(".h2h__section")

    overall = h2h_page.locator(".h2h__section").all()
    
    for h2h in overall:
        head = h2h.locator("div").first.inner_text().strip()
        previous = h2h.locator(".rows .h2h__row").all()
        matches = []
        for row in previous:
            matches.append({
                'date': row.locator(".h2h__date").inner_text().strip(),
                'event': row.locator(".h2h__event").inner_text().strip(),
                'home': row.locator(".h2h__homeParticipant").inner_text().strip(),
                'away': row.locator(".h2h__awayParticipant").inner_text().strip(),
                'result': format_score(row.locator(".h2h__result").inner_text().strip()),
                'icon': row.locator(".h2h__icon div").inner_text().strip()
            })
        print(matches)
