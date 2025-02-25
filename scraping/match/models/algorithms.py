"""
    Find perfect matches for home win
"""
def perfect_record(stats, mkt, team, tm):
    data = stats.get(mkt).get(team)
    team = tm or team
    if data.get(team) > 90:
        return True
    return False

def perfect_stats(stats):
    return ({
        'home_win': perfect_record(stats, 'winDrawWin_stats', 'home'),
        'away_win': perfect_record(stats, 'winDrawWin_stats', 'away'),
        'home_btts': perfect_record(stats, 'btts_stats', 'home', 'team'),
        'away_btts': perfect_record(stats, 'btts_stats', 'away', 'team'),
        'home_ng' : perfect_record(stats, 'ng_stats', 'home', 'team'),
        'away_ng' : perfect_record(stats, 'ng_stats', 'away', 'team'),
        'home_ov25': perfect_record(stats, 'over25_stats', 'home', 'team'),
        'away_ov25' : perfect_record(stats, 'over25_stats', 'away', 'team'),
        'home_un25': perfect_record(stats, 'under25_stats', 'home', 'team'),
        'away_un25': perfect_record(stats, 'under25_stats', 'away', 'team')
    })
    