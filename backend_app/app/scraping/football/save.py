from app.models.football.sure import SurePrediction
from app.models.football.best import BestPicksPrediction
from app.models.football.accumulator import AccumulatorPrediction
from app.algorithms.accumulator import find_accumulator_bets
from app.algorithms.surebet import find_sure_bets, convert_sure_bets
from app.scraping.odds import get_odds

def save(db, prediction, country, home, away, score, time, odds, link, table):
    new_pred = table(
        league=country,
        home_team=home,
        away_team=away,
        prediction=prediction['market'],
        odds=odds,
        result=score,
        form=prediction["current form"],
        h2h=prediction["head-to-head"],
        missing=prediction["injury/suspension"],
        home_away=prediction["home/away form"],
        matchup=prediction["tactical matchups"],
        insights=prediction["expert insights"],
        chance=prediction["confidence"]*100,
        href=link,
        time=time
    )
    db.session.add(new_pred)
    db.session.commit()

def accumulators(db, prediction, country, home, away, score, time, metrics, market, odds, link):
    pred = prediction['market']

    if prediction['prediction']:
        if prediction['confidence'] > 0.84:
            if find_sure_bets(pred, market, metrics):
                save(db, prediction, country, home, away, score, time, odds, link, SurePrediction)
                return
            elif convert_sure_bets(pred, market, metrics):
                prediction['market'] = 'over 1.5'
                save(db, prediction, country, home, away, score, time, odds, link, SurePrediction)
                return
            elif find_accumulator_bets(pred, market, metrics):
                save(db, prediction, country, home, away, score, time, odds, link, BestPicksPrediction)
                return
        if prediction['confidence'] > 0.74:
            if find_accumulator_bets(pred, market, metrics):
                save(db, prediction, country, home, away, score, time, odds, link, AccumulatorPrediction)
                return
        if find_accumulator_bets(pred, market, metrics):
            save(db, prediction, country, home, away, score, time, odds, link, BestPicksPrediction)
            return

    return


def football_odds(prediction, page, href):
    if 'win' in prediction['market']:
        return get_odds(page, href, prediction["market"], 'fulltime')
    if 'over' in prediction['market'] or 'under' in prediction['market']:
        return get_odds(page, href, prediction["market"], 'over_under')
    if 'btts' in prediction['market']:
        return get_odds(page, href, prediction["market"], 'btts')
