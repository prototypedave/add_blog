def get_team_win(h2h_list: list, home: str, away: str):
    hm = get_team_win_percent(h2h_list[0]['matches'], home)
    ay = get_team_win_percent(h2h_list[1]['matches'], away)
    h2h_home = get_team_win_percent(h2h_list[2]['matches'], home)
    h2h_away = 100 - h2h_home

    if (hm > 90 and h2h_home > 90) and ay < 50:
        return 'home win'
    if (ay > 90 and h2h_away > 90) and hm < 50:
        return 'away win'
    return None


def get_team_win_percent(results, team):
    count = 0 
    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-'))
                tm = game['home']
                if tm == team and a > b:
                    count += 1
                tm = game['away']
                if tm == team and b > a:
                    count += 1 
            except ValueError:
                continue
        else:
            continue
    return count / 5 * 100