
def overall_percent_total(stats):
    home_stat = stats[0]['matches']
    away_stat = stats[1]['matches']
    h2h = stats[2]['matches']

    home_btts = get_percent_total(home_stat)
    away_btts = get_percent_total(away_stat)
    h2h_btts = get_percent_total(h2h)
    

    return {
        'home' : home_btts,
        'away' : away_btts,
        'h2h'  : h2h_btts
    }

def side_percent_total(stats):
    side_stat = stats[0]['matches']
    h2h = stats[0]['matches']

    side_btts = get_percent_total(side_stat)
    h2h_btts = get_percent_total(h2h)

    return {
        'team' : side_btts,
        'h2h'  : h2h_btts
    }


def get_percent_total(matches):
    count = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a + b  > 3:
                    count+=1
            except ValueError:
                continue
        else:
            continue  
    
    return count / 5 * 100