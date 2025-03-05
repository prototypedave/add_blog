from playwright.sync_api import Page
from server_app.algorithms.projected_outcome import prediction_markets
from server_app.algorithms.hockey import get_hockey_prediction
from server_app.automation.groq_assistant import predict
from server_app.models.hockey import HockeyPrediction
from datetime import datetime
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from sqlalchemy.orm.exc import NoResultFound
from .hockey_stats.team_win import get_team_win
from .hockey_stats.btts import overall_btts
from .hockey_stats.over import overall_over


def get_hockey(page: Page, db):
    page.goto("https://www.flashscore.co.ke/ice-hockey/")
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
            h2h = get_h2h_details(page, link[:link.rfind('#')] + "#/h2h")
            win = get_team_win(h2h, home_team, away_team, time, country)
            existing_record = db.session.query(HockeyPrediction).filter_by(
                home_team=home_team,
                away_team=away_team,
                time=time
            ).first()
            if not existing_record:
                prediction = get_hockey_prediction(overall_over(h2h), overall_btts(h2h), win)
                if prediction:
                    new_pred = HockeyPrediction(
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