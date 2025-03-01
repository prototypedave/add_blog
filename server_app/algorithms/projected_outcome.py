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
    if home_ovr > 69 and away_ovr < 50:
        if h2h_home > 69:
            return 'home win' # Home team to win
        
    # Away favourite
    if away_ovr > 69 and home_ovr < 50:
        if h2h_away > 69:
            return 'away win'

    # Poor recent performance but still favorite to win    
    if home_ovr > 60 and away_ovr < 30:
        if h2h_home > 69:
            return 'home win'
        
    # Away favourite
    if away_ovr > 60 and home_ovr < 30:
        if h2h_away > 69:
            return 'away win'
        
    # Poor overall performance but good location perf
    if home_ovr > 60 and away_ovr < 30:
        if home_home > 69 and away_away < 40:
            if home_home_h2h > 50:
                return 'home win'
        
    # Away favourite
    if away_ovr > 60 and home_ovr < 30:
        if away_away > 69 and home_home < 40:
            if away_away_h2h > 50:
                return 'away win'
    
    return ""
            
def home_away_h2h_algo_general_mkts(stats, mkt, pred):
    home_ou = stats.get(mkt).get('ovr').get('home')
    away_ou = stats.get(mkt).get('ovr').get('away')
    h2h_ou = stats.get(mkt).get('ovr').get('h2h')

    # High chance of the market if both home and away have high score and h2h above the 50% chance
    if (home_ou and away_ou > 69) and h2h_ou > 60:
        return pred
    
    # Capture mkt where h2h has a high score and recent form is above average (60%)
    elif ((home_ou or away_ou > 69) and h2h_ou > 69) and (home_ou and away_ou > 60):
        return pred
    # return none if merit not met
    return 


def get_other_markets(stats, mkt, pred):
    
    home_home_ou = stats.get(mkt).get('home').get('team')
    h2h_home = stats.get(mkt).get('home').get('h2h')
    away_away_ou = stats.get(mkt).get('away').get('team')
    
    if (home_ou > 69 or away_ou > 69) and h2h_ou > 69:
        return pred
    
    if (home_home_ou > 69 or away_away_ou > 69) and h2h_home > 69:
        return pred

    if h2h_ou > 90:
        return pred

    return '' 


def prediction_markets(stats):
    markets = []
    if get_winner(stats):
        markets.append(get_winner(stats))
    
    if get_other_markets(stats, 'btts_stats', 'btts yes'):
        markets.append(get_other_markets(stats, 'btts_stats', 'btts yes'))

    if get_other_markets(stats, 'ng_stats', 'btts no'):
        markets.append(get_other_markets(stats, 'ng_stats', 'btts no'))

    if get_other_markets(stats, 'over25_stats', 'over 2.5'):
        markets.append(get_other_markets(stats, 'over25_stats', 'over 2.5'))

    if get_other_markets(stats, 'under25_stats', 'under 2.5'):
        markets.append(get_other_markets(stats, 'under25_stats', 'under 2.5'))

    return markets