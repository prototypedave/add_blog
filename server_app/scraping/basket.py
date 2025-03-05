from playwright.sync_api import Page
from server_app.algorithms.projected_outcome import prediction_markets
from server_app.algorithms.basket import predict_basketball
from server_app.automation.groq_assistant import predict
from server_app.models.basket import BasketPrediction
from datetime import datetime
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from sqlalchemy.orm.exc import NoResultFound
from .basket_stats.team_win import get_team_win
from .basket_stats.handicap import get_handicap_value
from .basket_stats.over import get_overall_over, get_team_over, define_total_value



def get_basket(page: Page, db):
    page.goto("https://www.flashscore.co.ke/basketball/")
    page.wait_for_selector(".event__match")
    events = page.locator(".event__match").all()
    links = []
    for event in events:
        links.append(event.locator("a").first.get_attribute("href"))

    for link in links:
        try:
            page.goto(link)
            home_team = page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
            away_team = page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
            score = page.locator(".detailScore__wrapper").inner_text().strip()
            time = page.locator(".duelParticipant__startTime div").inner_text().strip()
            country = page.locator(".tournamentHeader__country").inner_text().strip()
            existing_record = db.session.query(BasketPrediction).filter_by(
                home_team=home_team,
                away_team=away_team,
                time=time
            ).first()

            if not existing_record:
                prediction = get_h2h(page, link[:link.rfind('#')] + "#/h2h", home_team, away_team)
                if prediction:
                    new_pred = BasketPrediction(
                        league=country,
                        home_team=home_team,
                        away_team=away_team,
                        result=score,
                        time=time
                    )
                    new_pred.set_prediction(prediction)
                    db.session.add(new_pred)
                    db.session.commit()
            
        except PlaywrightTimeoutError:
            continue

def get_h2h(page: Page, link: str, home, away):
    ovr_link = link + "/overall"
    home_link = link + "/home"
    away_link = link + "/away"

    ovr_results  = get_h2h_details(page, ovr_link)
    home_results = get_h2h_details(page, home_link)
    away_results = get_h2h_details(page, away_link)

    ovr_total = get_overall_over(ovr_results, home, away)
    home_total = get_team_over(home_results, home)
    away_total = get_team_over(away_results, away)

    total = define_total_value(ovr_total, home_total, away_total)
    hc = get_handicap_value(ovr_results)
    win = get_team_win(ovr_results, home, away)
    return predict_basketball(ovr_results, total, hc, win)
    

def get_h2h_details(page: Page, link: str):
    page.goto(link)
    page.wait_for_selector(".h2h__section")
    h2h = page.locator(".h2h__section").all()
    _h2h = [] 
    for hh in h2h:
        _h2h.append(get_h2h_object(hh))

    return _h2h


def get_h2h_object(h2h):
    head = h2h.locator("div").first.inner_text().strip()
    previous = h2h.locator(".rows .h2h__row").all()
    matches = []
    for row in previous:
        matches.append(get_matches(row))    
    
    return({
        'header': head,
        'matches': matches
    })


def get_matches(row):
    return({
        'date': row.locator(".h2h__date").inner_text().strip(),
        'event': row.locator(".h2h__event").inner_text().strip(),
        'home': row.locator(".h2h__homeParticipant").inner_text().strip(),
        'away': row.locator(".h2h__awayParticipant").inner_text().strip(),
        'result': format_score(row.locator(".h2h__result").inner_text().strip()),
        'icon': row.locator(".h2h__icon").inner_text().strip()
    })

def format_score(raw_score):
    parts = raw_score.split("\n")  
    parts = [p.strip() for p in parts if p.strip()]
    return "-".join(parts)