def get_handicap_value(h2h_list: list):
    home = get_handicap(h2h_list[0]['matches'])
    away = get_handicap(h2h_list[1]['matches'])
    h2h = get_handicap(h2h_list[2]['matches'])

    return (home + away + h2h) / 3


def get_handicap(results):
    hc = 0
    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-'))
                if hc < (abs(a - b)):
                    hc = abs(a - b)
            except ValueError:
                continue
        else:
            continue
    return hc