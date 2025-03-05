from server_app.automation.groq_assistant import predict_hockey

def get_team_win(h2h: list, home: str, away: str, time: str, league: str):
    mkt = overall_team_win(h2h)
    if mkt:
        pred = predict_hockey(home, away, time, league)
        if home in pred['predictions'] and mkt == 'home win':
            return home
        if away in pred['predictions'] and mkt == 'away win':
            return away

    return "" 


def overall_team_win(h2h_list: list):
    home = calculate_percentage_win(h2h_list[0]['matches'])
    away = calculate_percentage_win(h2h_list[0]['matches'])
    h2h_home = calculate_percentage_win(h2h_list[0]['matches'])
    h2h_away = 100 - h2h_home
    
    if h2h_home > 90 and (home > 90 and away < 60):
        return 'home win'
    if h2h_away > 90 and (away > 90 and home < 60):
        return 'away win'
    return ''
    

def calculate_percentage_win(results: list):
    count = 0
    percent = 0

    for game in results:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-')) 
                if a > b:
                    count+=1
            except ValueError:
                continue
        else:
            continue
    percent= count / 5 * 100   # Assuming a good market requires atleast 5 games
    return percent  


