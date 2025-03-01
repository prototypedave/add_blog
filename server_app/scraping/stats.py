def get_pct_score(matches):
    count = 0
    percent = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a > 0 and b > 0:
                    count+=1
                    percent=count/len(matches)*100
            except ValueError:
                continue
        else:
            continue  
    
    return percent

def get_btts_score_ovr(result):
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

def get_btts_score(result):
    # Home team
    home = get_pct_score(result[0].get('matches'))
    # h2h
    h2h = get_pct_score(result[1].get('matches'))

    return {
        'team': home,
        'h2h': h2h
    }

def get_pct_score(matches):
    count = 0
    percent = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-'))
                if a == 0 and b == 0:
                    count+=1
                    percent=count/len(matches)*100
            except ValueError:
                continue
        else:
            continue  
    
    return percent


def get_ng_score_ovr(result):
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

def get_ng_score(result):
    # Home team
    home = get_pct_score(result[0].get('matches'))
    # h2h
    h2h = get_pct_score(result[1].get('matches'))

    return {
        'team': home,
        'h2h': h2h
    }

def get_pct_score(matches):
    count = 0
    percent = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a + b > 2:
                    count+=1
                    percent=count/len(matches)*100
            except ValueError:
                continue
        else:
            continue  
    
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


def get_pct_home(matches):
    count = 0
    percent = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a > b:
                    count+=1
                    percent=count/len(matches)*100
            except ValueError:
                continue
        else:
            continue  
    
    return percent


def get_pct_draw(matches):
    count = 0
    percent = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a == b:
                    count+=1
                    percent=count/len(matches)*100
            except ValueError:
                continue
        else:
            continue  
    
    return percent

def get_pct_away(matches):
    count = 0
    percent = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a < b:
                    count+=1
                    percent=count/len(matches)*100
            except ValueError:
                continue
        else:
            continue  
    
    return percent

def get_1x2_ovr(result):
    # Home team
    home = get_pct_home(result[0].get('matches'))
    # Away team
    away = get_pct_away(result[1].get('matches'))

    # h2h
    h2h = {
        'home' : get_pct_home(result[2].get('matches')),
        'away' : get_pct_away(result[2].get('matches')),
        'draw' : get_pct_away(result[2].get('matches')),
    }

    return {
        'home': home,
        'away': away,
        'h2h': h2h
    }

def get_home_score(result):
    # Home team
    home = get_pct_home(result[0].get('matches'))
    # h2h
    h2h = {
        'home' : get_pct_home(result[1].get('matches')),
        'away' : get_pct_away(result[1].get('matches')),
        'draw' : get_pct_away(result[1].get('matches')),
    }

    return {
        'home': home,
        'h2h': h2h
    }

def get_away_score(result):
    # Home team
    away = get_pct_away(result[0].get('matches'))
    # h2h
    h2h = {
        'home' : get_pct_home(result[1].get('matches')),
        'away' : get_pct_away(result[1].get('matches')),
        'draw' : get_pct_away(result[1].get('matches')),
    }

    return {
        'away': away,
        'h2h': h2h
    }