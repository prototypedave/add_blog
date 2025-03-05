from server_app.models.sure import SurePrediction
from server_app.models.accumulator import AccumulatorPrediction
from server_app.models.best_picks import BestPicksPrediction

def assert_sure_btts(metrics: list):
    if assert_btts(metrics):
        if metrics[0]['conceeded'] > metrics[0]['played'] and metrics[1]['conceeded'] > metrics[1]['played']:
            return True
    return False
        
def assert_btts(metrics: list):
    if metrics[0]['scored'] > metrics[0]['played'] and metrics[1]['scored'] > metrics[1]['played']:
        return True
    return False


def assert_no_btts(metrics: list):
    if metrics[0]['scored'] < metrics[0]['played'] and metrics[1]['scored'] < metrics[1]['played']:
        return True
    return False

def assert_sure_no_btts(metrics: list):
    if assert_btts(metrics):
        if metrics[0]['conceeded'] < metrics[0]['played'] and metrics[1]['conceeded'] < metrics[1]['played']:
            return True
    return False
    
def assert_sure_over(metrics: list):
    expect = metrics[0]['played'] * 3
    if metrics[0]['scored'] + metrics[0]['conceeded'] > expect and metrics[1]['scored'] + metrics[1]['conceeded'] > expect:
        return True
    return False


def assert_over(metrics: list):
    expect = metrics[0]['played'] * 3
    total = metrics[0]['scored'] + metrics[0]['conceeded'] + metrics[1]['scored'] + metrics[1]['conceeded'] / 2
    if total > expect:
        return True
    return False


def assert_under(metrics: list):
    if metrics[0]['scored'] + metrics[1]['scored'] / metrics[0]['played'] < 1.5:
        return True
    return False


def assert_sure_under(metrics: list):
    home = (metrics[0]['scored'] + metrics[0]['conceeded']) / 2
    away = (metrics[1]['scored'] + metrics[1]['conceeded']) / 2

    if home / metrics[0]['played'] < 1.5 and away / metrics[1]['played']:
        return True
    return False


def save(db, prediction, country, home, away, score, time, table):
    new_pred = table(
        league=country,
        home_team=home,
        away_team=away,
        prediction=check_prediction(prediction),
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


def find_accumulators(metrics, met, db, prediction, country, home, away, score, time, h2h):
    if isinstance(prediction['prediction'], bool):
        if accumulator_btts(metrics, met, db, prediction, country, home, away, score, time, h2h):
            return
        return
    if assure_team_win(db, prediction, country, home, away, score, time):
        return
    if accumulator_total(metrics, met, db, prediction, country, home, away, score, time, h2h):
        return
    

def assure_team_win(db, prediction, country, home, away, score, time):
    # Check if its a home win
    if ('win' in prediction['market'] and home in prediction['prediction']) and prediction['confidence'] > 0.64:
        if prediction['confidence'] > 0.69:
            save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
            return True
        save(db, prediction, country, home, away, score, time, BestPicksPrediction)
        return True
    
    # If away
    if ('win' in prediction['market'] and away in prediction['prediction']) and prediction['confidence'] > 0.64:
        if prediction['confidence'] > 0.69:
            save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
            return True
        save(db, prediction, country, home, away, score, time, BestPicksPrediction)
        return True
    

def accumulator_btts(metrics, met, db, prediction, country, home, away, score, time, stats):
    if float(prediction['confidence']) > 0.65 and ('btts' in prediction['market'] and prediction['prediction']):
        if assert_btts(metrics):
            if assert_sure_btts and float(prediction['confidence']) > 0.70:
                if good_ovr_mkts(stats, 'btts_stats', 79, 69):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
                elif good_home_side_mkts(stats, 'btts_stats', 99, 79):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
            
            if good_ovr_mkts(stats, 'btts_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            elif good_home_side_mkts(stats, 'btts_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            save(db, prediction, country, home, away, score, time, BestPicksPrediction)
            return True
        
    if float(prediction['confidence']) > 0.65 and ('btts' in prediction['market'] and not prediction['prediction']):
        if assert_no_btts(metrics):
            if assert_sure_no_btts and float(prediction['confidence']) > 0.70:
                if good_ovr_mkts(stats, 'ng_stats', 79, 69):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
                elif good_home_side_mkts(stats, 'ng_stats', 99, 79):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
                
            if good_ovr_mkts(stats, 'ng_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            elif good_home_side_mkts(stats, 'ng_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            save(db, prediction, country, home, away, score, time, BestPicksPrediction)
            return True
            
    if prediction['prediction'] in met:
        save(db, prediction, country, home, away, score, time, BestPicksPrediction)
        return True
    
    return False


def accumulator_total(metrics, met, db, prediction, country, home, away, score, time, stats):
    print('over 25 runs')
    if float(prediction['confidence']) > 0.65 and ('total' in prediction['market'] and 'over' in prediction['prediction']):
        if assert_over(metrics):
            if assert_sure_over and float(prediction['confidence']) > 0.70:
                if good_ovr_mkts(stats, 'over25_stats', 79, 69):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
                elif good_home_side_mkts(stats, 'over25_stats', 99, 79):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
            
            if good_ovr_mkts(stats, 'over25_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            elif good_home_side_mkts(stats, 'over25_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            save(db, prediction, country, home, away, score, time, BestPicksPrediction)
            return True
        
    
    if float(prediction['confidence']) > 0.65 and ('total' in prediction['market'] and 'under' in prediction['prediction']):
        if assert_under(metrics):
            if assert_sure_under and float(prediction['confidence']) > 0.70:
                if good_ovr_mkts(stats, 'under25_stats', 79, 69):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
                elif good_home_side_mkts(stats, 'under25_stats', 99, 79):
                    save(db, prediction, country, home, away, score, time, SurePrediction)
                    return True
                
            if good_ovr_mkts(stats, 'under25_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            elif good_home_side_mkts(stats, 'under25_stats', 69, 50):
                save(db, prediction, country, home, away, score, time, AccumulatorPrediction)
                return True
            
            save(db, prediction, country, home, away, score, time, BestPicksPrediction)
            return True
            
    if prediction['prediction'] in met:
        save(db, prediction, country, home, away, score, time, BestPicksPrediction)
        return True
    
    return False


def good_ovr_mkts(stats, mkt, value, val):
    home = stats.get(mkt).get('ovr').get('home')
    away = stats.get(mkt).get('ovr').get('away')
    h2h = stats.get(mkt).get('ovr').get('h2h')

    if home > value and away > value:
        return True
    
    if h2h > value and (home > val and away > val):
        return True
    
    return False


def good_home_side_mkts(stats, mkt, value, val):
    home = stats.get(mkt).get('home').get('team')
    h2h_home = stats.get(mkt).get('home').get('h2h')
    away = stats.get(mkt).get('away').get('team')

    if h2h_home > value and (home > val and away > val):
        return True
    
    return False

def check_prediction(prediction):
    if 'win' in prediction['market']:
        return prediction['prediction']
    if 'btts' in prediction['market'] and prediction['prediction']:
        return 'BTTS Yes'
    if 'btts' in prediction['market'] and not prediction['prediction']:
        return 'BTTS No'
    if 'total' in prediction['market'] and 'over' in prediction['prediction']:
        return 'Over 2.5'
    if 'total' in prediction['market'] and 'under' in prediction['prediction']:
        return 'Under 2.5' 