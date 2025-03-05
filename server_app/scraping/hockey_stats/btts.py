def overall_btts(h2h_list: list):
    home = calculate_percentage_btts(h2h_list[0]['matches'])
    away = calculate_percentage_btts(h2h_list[1]['matches'])
    h2h = calculate_percentage_btts(h2h_list[2]['matches'])

    if (h2h > 90 and (home > 79 and away > 79)):
        return 'btts'
    return ''
    
    
def calculate_percentage_btts(results: list):
    count = 0
    percent = 0

    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a > 2 and b > 2:
                    count+=1
                    percent= count / 5 * 100   # Assuming a good market requires atleast 5 games
            except ValueError:
                continue
        else:
            continue
    return percent  