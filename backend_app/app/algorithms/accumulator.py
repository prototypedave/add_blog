def find_accumulator_bets(prediction, market, metrics):
    prediction = prediction.lower()  

    # Extract relevant metrics
    home, away = metrics
    home_points, away_points = home['points'], away['points']
    home_score, away_score = home['scored'], away['scored']
    home_conceded, away_conceded = home['conceeded'], away['conceeded']
    played = home['played']

    # Calculate average total goals
    average_total = (home_score + home_conceded + away_score + away_conceded) / 8

    conditions = {
        'home win': home_points > away_points,
        'away win': away_points > home_points,
        'over 2.5': average_total > 3,
        'over 3.5': average_total > 4,
        'under 2.5': average_total < 1.5,
        'under 3.5': average_total < 2.5,
        'btts yes': (
            home_conceded > played and home_score > played and
            away_conceded > played and away_score > played
        ),
        'btts no': (
            home_conceded < played and home_score < played and
            away_conceded < played and away_score < played 
        )
    }

    return conditions.get(prediction, False) if prediction in market else False
