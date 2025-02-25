def get_pct_score(matches):
    count = 0
    percent = 0
    for team in matches:
        a, b = map(int, team.get('result').split('-'))
        if a + b > 2:
            count+=1
            percent=count/len(matches)*100
    
    return percent

def get_over25_ovr(result):
    # Home team
    home = get_pct_score(result[0].get('matches'))
    # Away team
    away = get_pct_score(result[1].get('matches'))
    # h2h
    h2h = get_pct_score(result[2].get('matches'))

    return {
        'home': home,
        'away': away,
        'h2h': h2h
    }

def get_over25_score(result):
    # Home team
    home = get_pct_score(result[0].get('matches'))
    # h2h
    h2h = get_pct_score(result[1].get('matches'))

    return {
        'team': home,
        'h2h': h2h
    }