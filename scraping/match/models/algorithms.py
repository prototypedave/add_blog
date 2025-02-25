"""
    Find perfect matches for home win
"""
def perfect_record(stats, mkt, team, tm):
    data = stats.get(mkt).get(team)
    if tm is not None:
        team = tm
    if data.get(team) > 90:
        return True
    return False

def ovr_record(stats, mkt, team, h2h, tm):
    data = stats.get(mkt).get(team).get(h2h)
    if data.get(tm) > 90:
        return True
    return False

def perfect_stats(stats):
    return ({
        'home_win': perfect_record(stats, 'winDrawWin_stats', 'home', None),
        'away_win': perfect_record(stats, 'winDrawWin_stats', 'away', None),
        'home_btts': perfect_record(stats, 'btts_stats', 'home', 'team'),
        'away_btts': perfect_record(stats, 'btts_stats', 'away', 'team'),
        'home_ng' : perfect_record(stats, 'ng_stats', 'home', 'team'),
        'away_ng' : perfect_record(stats, 'ng_stats', 'away', 'team'),
        'home_ov25': perfect_record(stats, 'over25_stats', 'home', 'team'),
        'away_ov25' : perfect_record(stats, 'over25_stats', 'away', 'team'),
        'home_un25': perfect_record(stats, 'under25_stats', 'home', 'team'),
        'away_un25': perfect_record(stats, 'under25_stats', 'away', 'team')
    })
    

def perfect_h2h(stats):
    return ({
        'home_win': ovr_record(stats, 'winDrawWin_stats', 'ovr', 'h2h', 'home'),
        'away_win': ovr_record(stats, 'winDrawWin_stats', 'ovr', 'h2h', 'away'),
        'btts': perfect_record(stats, 'btts_stats', 'home', 'h2h'),
        'ng' : perfect_record(stats, 'ng_stats', 'home', 'h2h'),
        'ov25': perfect_record(stats, 'over25_stats', 'home', 'h2h'),
        'un25': perfect_record(stats, 'under25_stats', 'home', 'h2h')
    })


def on_form(stats):
    return ({
        'home_win': perfect_record(stats, 'winDrawWin_stats', 'ovr', 'home'),
        'away_win': perfect_record(stats, 'winDrawWin_stats', 'ovr', 'away'),
        'home_btts': perfect_record(stats, 'btts_stats', 'ovr', 'home'),
        'away_btts': perfect_record(stats, 'btts_stats', 'ovr', 'away'),
        'home_ng' : perfect_record(stats, 'ng_stats', 'ovr', 'home'),
        'away_ng' : perfect_record(stats, 'ng_stats', 'ovr', 'away'),
        'home_ov25': perfect_record(stats, 'over25_stats', 'ovr', 'home'),
        'away_ov25' : perfect_record(stats, 'over25_stats', 'ovr', 'away'),
        'home_un25': perfect_record(stats, 'under25_stats', 'ovr', 'home'),
        'away_un25': perfect_record(stats, 'under25_stats', 'ovr', 'away')
    })


def on_form_h2h(stats):
    home_data = stats.get('winDrawWin_stats').get('ovr').get('h2h').get('home')
    away_data = stats.get('winDrawWin_stats').get('ovr').get('h2h').get('away')
    return ({
        'home_win': home_data > 90,
        'away_win': away_data > 90,
    })
