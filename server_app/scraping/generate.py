from playwright.sync_api import Page
from server_app.algorithms.projected_outcome import prediction_markets
from server_app.algorithms.analysis import find_accumulators
from server_app.algorithms.sure_bet import perfect_options
from server_app.automation.groq_assistant import predict
from server_app.models.predictions import MatchPrediction
from .stats.btts import get_btts_score, get_btts_score_ovr
from .stats.nobtts import get_ng_score, get_ng_score_ovr
from .stats.over25 import get_over25_ovr, get_over25_score
from .stats.under25 import get_under25_ovr, get_under25_score
from .stats.windrawwin import get_away_score, get_home_score, get_1x2_ovr
from datetime import datetime
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from sqlalchemy.orm.exc import NoResultFound


def is_generated_games_report(page: Page, db):
    page.goto("https://www.flashscoreusa.com/?rd=flashscore.us")
    page.wait_for_selector(".event__match")
    events = page.locator(".event__match").all()
    links = []
    for event in events:
        links.append(event.locator("a").first.get_attribute("href"))

    links = links[::-1]
    for link in links:
        page.goto(link)
        home_team = page.locator(".duelParticipant__home .participant__participantName a").first.inner_text().strip()
        away_team = page.locator(".duelParticipant__away .participant__participantName a").first.inner_text().strip()
        score = page.locator(".detailScore__wrapper").inner_text().strip()
        time = page.locator(".duelParticipant__startTime div").inner_text().strip()
        country = page.locator(".tournamentHeader__country").inner_text().strip()

        existing_record = db.session.query(MatchPrediction).filter_by(
            home_team=home_team,
            away_team=away_team,
            time=time
        ).first()

        # Prevents re-running the whole code again
        if existing_record:
            markets_to_predict = prediction_markets(h2h(page, link[:link.rfind('#')] + "#/h2h"))
            mets = perfect_options(h2h(page, link[:link.rfind('#')] + "#/h2h"))
            metrics = get_table_standings(page, link[:link.rfind('#')] + "#/standings/overall", home_team, away_team)
            # Only predict potential games
            if markets_to_predict:
                # Predict on markets that havent played yet
                if datetime.strptime(time, "%I:%M %p, %B %d, %Y") > datetime.now():
                    prediction = predict(home_team, away_team, markets_to_predict)
                    if metrics:
                        if find_accumulators(metrics, mets, db, prediction, country, home_team, away_team, score, time):
                            print(f"{home_team}: {prediction}")

                    print(f'{home_team}: {mets}')
                    new_pred = MatchPrediction(
                        league=country,
                        home_team=home_team,
                        away_team=away_team,
                        prediction=prediction["prediction"],
                        odds=prediction["odds"],
                        result=score,
                        reason=prediction["reason"],
                        chance=prediction["chance"],
                        time=time
                    )
                    db.session.add(new_pred)
                    db.session.commit()
                    print("Saved to db")


    return True


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

def organize_stats(func, func2, func3, page: Page, ovr, home, away):
    return {
        'ovr' : func(get_h2h_details(page, ovr)),
        'home' : func2(get_h2h_details(page, home)),
        'away': func3(get_h2h_details(page, home)),
    }

def get_stats(h2h_page: Page, ovr, home, away):
    return ({
        'btts_stats' : organize_stats(get_btts_score_ovr, get_btts_score, get_btts_score, h2h_page, ovr, home, away),
        'ng_stats' : organize_stats(get_ng_score_ovr, get_ng_score, get_btts_score, h2h_page, ovr, home, away),
        'over25_stats' : organize_stats(get_over25_ovr, get_over25_score, get_btts_score, h2h_page, ovr, home, away),
        'under25_stats' : organize_stats(get_under25_ovr, get_under25_score, get_btts_score, h2h_page, ovr, home, away),
        'winDrawWin_stats' : organize_stats(get_1x2_ovr, get_home_score, get_away_score, h2h_page, ovr, home, away)
    })

def h2h(page: Page, href):
    h2h_page = page
    ovr = href + "/overall"
    home = href + "/home"
    away = href + "/away"

    stats = get_stats(h2h_page, ovr, home, away)
    
    return stats


def get_table_standings(page: Page, href: str, home: str, away: str):
    try: 
        page.goto(href)
        page.wait_for_selector(".tableWrapper")
        participants = page.locator(".table__row--selected").all()

        stats = []
        
        for participant in participants:
            team = participant.locator(".tableCellParticipant__name").inner_text().strip()
            if team == (home or away):
                played = participant.locator(".table__cell--value").first.inner_text().strip()
                scored, conceeded = format_goals(participant.locator(".table__cell--score").inner_text().strip())
                points = participant.locator(".table__cell--points").inner_text().strip()
                stats.append({'team' : team, 'played': played, 'scored': scored, 'conceeded': conceeded, 'points': points})

        return stats
    except PlaywrightTimeoutError:
        return []


def format_goals(gls: str):
    try:
        scored, conceeded = map(int, gls.split(':'))
        return scored, conceeded
    except ValueError:
        return None
    

