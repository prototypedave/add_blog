def overall_over(h2h_list: list):
    home = calculate_percentage_over_45(h2h_list[0]['matches'])
    away = calculate_percentage_over_45(h2h_list[0]['matches'])
    h2h = calculate_percentage_over_45(h2h_list[0]['matches'])
    
    # Only get over 3.5 if h2h is not 100
    if h2h < 100:
        home = calculate_percentage_over_35(h2h_list[0]['matches'])
        away = calculate_percentage_over_35(h2h_list[0]['matches'])
        h2h = calculate_percentage_over_35(h2h_list[0]['matches'])

        if (h2h > 90 and (home > 79 and away > 79)):
            return 'over 3.5'
        return ''
    
    return 'over 4.5'
    

def calculate_percentage_over_45(results: list):
    count = 0
    percent = 0

    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a + b > 5:
                    count+=1
                    percent= count / 5 * 100   # Assuming a good market requires atleast 5 games
            except ValueError:
                continue
        else:
            continue
    return percent  


def calculate_percentage_over_35(results: list):
    count = 0
    percent = 0

    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a + b > 4:
                    count+=1
                    percent= count / 5 * 100   # Assuming a good market requires atleast 5 games
            except ValueError:
                continue
        else:
            continue
    return percent  

