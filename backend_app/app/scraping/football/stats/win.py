
def overall_percent_win(stats, home, away):
    home_stat = stats[0]['matches']
    away_stat = stats[1]['matches']
    h2h = stats[2]['matches']

    home_win = get_percent_team_win(home_stat, home)
    away_win = get_percent_team_win(away_stat, away)
    h2h_home = get_percent_team_win(h2h, home)
    h2h_away = get_percent_team_win(h2h, away)

    return {
        'home' : home_win,
        'away' : away_win,
        'h2h'  : {
            'home' : h2h_home,
            'away' : h2h_away
        }
    }

def side_percent_win(stats, side):
    side_stat = stats[0]['matches']
    h2h = stats[0]['matches']

    side_win = get_percent_team_win(side_stat, side)
    h2h_win = get_percent_team_win(h2h, side)

    return {
        'team' : side_win,
        'h2h'  : h2h_win
    }


def get_percent_team_win(matches, side):
    count = 0
    for team in matches:
        result = team.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a > b and team['home'] == side:
                    count+=1
                if b > a and team['away'] == side:
                    count+=1
            except ValueError:
                continue
        else:
            continue  
    
    return count / 5 * 100