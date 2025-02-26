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