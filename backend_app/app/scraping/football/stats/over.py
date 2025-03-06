
def overall_percent_over(stats):
    home_stat = stats[0]['matches']
    away_stat = stats[1]['matches']
    h2h = stats[2]['matches']

    home_btts = get_percent_over(home_stat)
    away_btts = get_percent_over(away_stat)
    h2h_btts = get_percent_over(h2h)
    

    return {
        'home' : home_btts,
        'away' : away_btts,
        'h2h'  : h2h_btts
    }

def side_percent_over(stats):
    side_stat = stats[0]['matches']
    h2h = stats[0]['matches']

    side_btts = get_percent_over(side_stat)
    h2h_btts = get_percent_over(h2h)

    return {
        'team' : side_btts,
        'h2h'  : h2h_btts
    }


def get_percent_over(matches):
    count = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a + b  > 2:
                    count+=1
            except ValueError:
                continue
        else:
            continue  
    
    return count / 5 * 100