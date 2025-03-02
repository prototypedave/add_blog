from server_app.models.sure import SurePrediction
from server_app.models.accumulator import AccumulatorPrediction

def assert_sure_btts(metrics: list):
    if assert_btts(metrics):
        if (metrics[0].conceeded > metrics[0].played) and (metrics[1].conceeded > metrics[1].played):
            return True
    return False
        
def assert_btts(metrics: list):
    if (metrics[0].scored > metrics[0].played) and (metrics[1].scored > metrics[1].played):
        return True
    return False


def assert_no_btts(metrics: list):
    if (metrics[0].scored < metrics[0].played) and (metrics[1].scored < metrics[1].played):
        return True
    return False

def assert_sure_no_btts(metrics: list):
    if assert_btts(metrics):
        if (metrics[0].conceeded < metrics[0].played) and (metrics[1].conceeded < metrics[1].played):
            return True
    return False
    
def assert_sure_over(metrics: list):
    expect = metrics[0].played * 3
    if (metrics[0].scored + metrics[0].conceeded) > expect and (metrics[1].scored + metrics[1].conceeded) > expect:
        return True
    return False


def assert_over(metrics: list):
    expect = metrics[0].played * 3
    total = (metrics[0].scored + metrics[0].conceeded + metrics[1].scored + metrics[1].conceeded) / 2
    if total > expect:
        return True
    return False


def assert_under(metrics: list):
    if (metrics[0].scored + metrics[1].scored) / metrics[0].played < 1.5:
        return True
    return False


def assert_sure_under(metrics: list):
    home = (metrics[0].scored + metrics[0].conceeded) / 2
    away = (metrics[1].scored + metrics[1].conceeded) / 2

    if home / metrics[0].played < 1.5 and away / metrics[1].played:
        return True
    return False


def save_sure_predictions(db, prediction, country, home, away, score, time):
    new_pred = SurePrediction(
        league=country,
        home_team=home,
        away_team=away,
        prediction=prediction["prediction"],
        odds=prediction["odds"],
        result=score,
        reason=prediction["reason"],
        chance=prediction["chance"],
        time=time
    )
    db.session.add(new_pred)
    db.session.commit()


def save_predictions(db, prediction, country, home, away, score, time):
    new_pred = AccumulatorPrediction(
        league=country,
        home_team=home,
        away_team=away,
        prediction=prediction["prediction"],
        odds=prediction["odds"],
        result=score,
        reason=prediction["reason"],
        chance=prediction["chance"],
        time=time
    )
    db.session.add(new_pred)
    db.session.commit()


def sure_match(metrics, met, db, prediction, country, home, away, score, time):
    if len(metrics) == 2:
        if ('btts' in prediction['prediction']) and ('yes' in prediction['prediction']):
            if assert_sure_btts(metrics):
                save_sure_predictions(db, prediction, country, home, away, score, time)
                return True
        
        elif ('btts' in prediction['prediction']) and ('no' in prediction['prediction']):
            if assert_sure_no_btts(metrics):
                save_sure_predictions(db, prediction, country, home, away, score, time)
                return True

        elif ('over' in prediction['prediction']):
            if assert_sure_over(metrics):
                save_sure_predictions(db, prediction, country, home, away, score, time)
                return True
            
        elif ('under' in prediction['prediction']):
            if assert_sure_under(metrics):
                save_sure_predictions(db, prediction, country, home, away, score, time)
                return True
            
        elif met:
            save_sure_predictions(db, prediction, country, home, away, score, time)
            return True
    

def accumulators(metrics, met, db, prediction, country, home, away, score, time):
    if len(metrics) == 2:
        if ('btts' in prediction['prediction']) and ('yes' in prediction['prediction']):
            if assert_btts(metrics):
                save_predictions(db, prediction, country, home, away, score, time)
                return True
        
        elif ('btts' in prediction['prediction']) and ('no' in prediction['prediction']):
            if assert_no_btts(metrics):
                save_predictions(db, prediction, country, home, away, score, time)
                return True

        elif ('over' in prediction['prediction']):
            if assert_over(metrics):
                save_predictions(db, prediction, country, home, away, score, time)
                return True
            
        elif ('under' in prediction['prediction']):
            if assert_under(metrics):
                save_predictions(db, prediction, country, home, away, score, time)
                return True
            
        elif met:
            save_predictions(db, prediction, country, home, away, score, time)
            return True
        
def find_accumulators(metrics, met, db, prediction, country, home, away, score, time, chance):
    if assure_team_win(metrics, met, db, prediction, country, home, away, score, time, chance):
        return


def assure_team_win(metrics, met, db, prediction, country, home, away, score, time):
    # Form chance into an int
    chance = int(prediction['chance'][:-1]) if isinstance(prediction['chance'], str) and prediction['chance'].endswith('%') else int(prediction['chance'])
    
    # Check if its a home win
    if ('win' in prediction and home in prediction) and chance > 69:
        save_predictions(db, prediction, country, home, away, score, time)
        return True
    
    # If away
    if ('win' in prediction and away in prediction) and chance > 69:
        save_predictions(db, prediction, country, home, away, score, time)
        return True
