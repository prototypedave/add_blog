def form_advantange(teamA, teamB, h2h, side):
    if teamA > 69 and teamB < 40:
        if h2h > 69:
           return side

def h2h_advantange(teamA, teamB, h2h, side):
    if (teamA  > 60 and teamB > 60) and h2h > 69:
        return side

def based_on_side_advantange(team, h2h, side):
    if team > 69 and h2h > 69:
        return side
    
    
def get_winner(stats):
    home_ovr = stats.get('winDrawWin_stats').get('ovr').get('home')
    away_ovr = stats.get('winDrawWin_stats').get('ovr').get('home')
    h2h_home = stats.get('winDrawWin_stats').get('ovr').get('h2h').get('home')
    h2h_away = stats.get('winDrawWin_stats').get('ovr').get('h2h').get('away')
    home_home = stats.get('winDrawWin_stats').get('home').get('home')
    home_home_h2h = stats.get('winDrawWin_stats').get('home').get('h2h').get('home')
    away_away = stats.get('winDrawWin_stats').get('away').get('away')
    away_away_h2h = stats.get('winDrawWin_stats').get('away').get('h2h').get('away')

    # If home team favorite
    if form_advantange(home_ovr, away_ovr, h2h_home, 'full time match result'):
        return form_advantange(home_ovr, away_ovr, h2h_home, 'full time match result')

    # Away favourite
    if form_advantange(away_ovr, home_ovr, h2h_away, 'full time match result'):
        return form_advantange(away_ovr, home_ovr, h2h_away, 'full time match result')

    # Poor recent performance but still favorite to win
    if h2h_advantange(home_ovr, away_ovr, h2h_home, 'full time match result'):
        return h2h_advantange(home_ovr, away_ovr, h2h_home, 'full time match result')
    
    # Away favourite
    if h2h_advantange(away_ovr, home_ovr, h2h_away, 'full time match result'):
        return h2h_advantange(away_ovr, home_ovr, h2h_away, 'full time match result')

    # Poor overall performance but good location perf
    if based_on_side_advantange(home_home, home_home_h2h, 'full time match result'):
        return based_on_side_advantange(home_home, home_home_h2h, 'full time match result')

    # Away favourite
    if based_on_side_advantange(away_away, away_away_h2h, 'full time match result'):
        return based_on_side_advantange(away_away, away_away_h2h, 'full time match result')

    return ""
            
def home_away_h2h_algo_general_mkts(stats, mkt, pred):
    home = stats.get(mkt).get('ovr').get('home')
    away = stats.get(mkt).get('ovr').get('away')
    h2h = stats.get(mkt).get('ovr').get('h2h')

    # High chance of the market if both home and away have high score and h2h above the 50% chance
    if (home > 69 and away > 69) and h2h > 60:
        return pred
    
    # Capture mkt where h2h has a high score and recent form is above average (60%)
    elif ((home > 69 or away > 69) and h2h > 69) and (home > 60 and away > 60):
        return pred
    # return none if merit not met
    return


def home_or_away_algo_general_mkts(stats, mkt, pred):
    home = stats.get(mkt).get('home').get('team')
    h2h_home = stats.get(mkt).get('home').get('h2h')
    away = stats.get(mkt).get('away').get('team')

    # If home or away form is impressive with a good h2h record
    if ((home > 79 or away > 79) and (home > 60 and away > 60)) and h2h_home > 69:
        return pred
    return


def get_other_markets(stats, mkt, pred):
    if home_away_h2h_algo_general_mkts(stats, mkt, pred):
        return pred
    elif home_or_away_algo_general_mkts(stats, mkt, pred):
        return pred
    return


def prediction_markets(stats):
    markets = []
    if get_winner(stats):
        markets.append(get_winner(stats))
    
    if get_other_markets(stats, 'btts_stats', 'btts'):
        markets.append(get_other_markets(stats, 'btts_stats', 'btts'))

    if get_other_markets(stats, 'ng_stats', 'btts no'):
        markets.append(get_other_markets(stats, 'ng_stats', 'btts'))

    if get_other_markets(stats, 'over25_stats', 'total 2.5'):
        markets.append(get_other_markets(stats, 'over25_stats', 'total 2.5'))

    if get_other_markets(stats, 'under25_stats', 'under 2.5'):
        markets.append(get_other_markets(stats, 'under25_stats', 'total 2.5'))
    return markets