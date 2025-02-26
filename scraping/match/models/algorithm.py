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
            

def get_btts(stats):
    home_btts = stats.get('btts_stats').get('ovr').get('home')
    away_btts = stats.get('btts_stats').get('ovr').get('away')
    h2h_btts = stats.get('btts_stats').get('ovr').get('h2h')
    home_home_btts = stats.get('btts_stats').get('home').get('team')
    h2h_home = stats.get('btts_stats').get('home').get('h2h')
    away_away_btts = stats.get('btts_stats').get('away').get('team')

    if (home_btts > 69 or away_btts > 69) and h2h_btts > 69:
        return 'btts yes'
    
    if (home_home_btts > 69 or away_away_btts > 69) and h2h_home > 69:
        return 'btts yes' 

    if h2h_btts > 90:
        return 'btts yes'

    return '' 


def get_no_btts(stats):
    home_no_btts = stats.get('ng_stats').get('ovr').get('home')
    away_no_btts = stats.get('ng_stats').get('ovr').get('away')
    h2h_no_btts = stats.get('ng_stats').get('ovr').get('h2h')
    home_home_no_btts = stats.get('ng_stats').get('home').get('team')
    h2h_home = stats.get('ng_stats').get('home').get('h2h')
    away_away_no_btts = stats.get('ng_stats').get('away').get('team')

    if (home_no_btts > 69 or away_no_btts > 69) and h2h_no_btts > 69:
        return 'btts yes'
    
    if (home_home_no_btts > 69 or away_away_no_btts > 69) and h2h_home > 69:
        return 'btts yes' 

    if h2h_no_btts > 90:
        return 'btts yes'

    return '' 



