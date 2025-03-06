from app.models.football.general import GeneralPrediction
from app.models.football.sure import SurePrediction
from app.models.football.best import BestPicksPrediction
from app.models.football.accumulator import AccumulatorPrediction
from app.algorithms.accumulator import find_accumulator_bets
from app.algorithms.surebet import find_sure_bets

def save(db, prediction, country, home, away, score, time, table):
    new_pred = table(
        league=country,
        home_team=home,
        away_team=away,
        prediction=prediction['market'],
        odds=prediction["odds"],
        result=score,
        form=prediction["current form"],
        h2h=prediction["head-to-head"],
        missing=prediction["injury/suspension"],
        home_away=prediction["home/away form"],
        matchup=prediction["tactical matchups"],
        insights=prediction["expert insights"],
        chance=prediction["confidence"]*100,
        time=time
    )
    db.session.add(new_pred)
    db.session.commit()

def accumulators(db, prediction, country, home, away, score, time, metrics, market):
    if prediction['prediction']:
        if prediction['confidence'] > 0.84:
            if find_sure_bets(prediction['market'], market, metrics):
                save(db, prediction, country, home, away, score, time, SurePrediction)
            elif find_accumulator_bets(prediction['market'], market, metrics):
                save(db, prediction, country, home, away, score, time, BestPicksPrediction)
        if prediction['confidence'] > 0.74:
            if find_accumulator_bets(prediction['market'], market, metrics):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
        if find_accumulator_bets(prediction['market'], market, metrics):
            save(db, prediction, country, home, away, score, time, BestPicksPrediction)

        save(db, prediction, country, home, away, score, time, GeneralPrediction)
