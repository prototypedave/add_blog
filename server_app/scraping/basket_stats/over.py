def get_overall_over(h2h_list: list, home: str, away: str):
    hm = get_total(h2h_list[0]['matches'])
    aw = get_total(h2h_list[1]['matches'])
    h2h = get_total(h2h_list[2]['matches'])

    hm_total_score = get_team_total(h2h_list[0]['matches'], home)
    aw_total_score = get_team_total(h2h_list[1]['matches'], away)
    
    return (hm + aw + h2h + (hm_total_score + aw_total_score)) / 4

def get_team_over(h2h_list: list, team: str):
    tm = get_total(h2h_list[0]['matches'])
    h2h = get_total(h2h_list[1]['matches'])

    team_score = get_team_total(h2h_list[0]['matches'], team)
    return {'team': team_score, 'total': (tm + h2h) / 2}


"""
Return average total for given result last 5 games
"""
def get_total(results: list):
    total = 0
    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-'))
                total += (a + b)
            except ValueError:
                continue
        else:
            continue
    return total / 5


"""
Return average of a team total
"""
def get_team_total(results: list, team: str):
    total = 0
    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-'))
                tm = game.get('home')
                if tm == team:
                    total += a
                tm = game.get('away')
                if tm == team:
                    total += b
            except ValueError:
                continue
        else:
            continue
    return total / 5
        
def define_total_value(ovr: float, home: object, away: object):
    total = (home['team'] + away['team']) / 2
    total = total + ovr + home['total'] + away['total']
    return total / 4
