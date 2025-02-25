def get_pct_score(matches):
    count = 0
    percent = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a + b <= 2:
                    count+=1
                    percent=count/len(matches)*100
            except ValueError:
                continue
        else:
            continue  
    
    return percent

def get_under25_ovr(result):
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

def get_under25_score(result):
    # Home team
    home = get_pct_score(result[0].get('matches'))
    # h2h
    h2h = get_pct_score(result[1].get('matches'))

    return {
        'team': home,
        'h2h': h2h
    }