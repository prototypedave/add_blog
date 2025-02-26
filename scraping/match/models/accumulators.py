from .algorithms import perfect_stats, on_form

def get_record(stats, mkt, type, home, away):
    stat = stats.get(mkt).get(type)
    if stat.get(home) > 70 and stat.get(away) < 30:
        return True
    return 

def get_loc_record(stats, mkt, type, team):
    if stats.get(mkt).get(type).get(team) > 70:
        return True
    return False


def get_h2h_record(stats, mkt, type, h2h, team):
    if stats.get(mkt).get(type).get(h2h).get(team) > 70:
        return True
    return False


"""
Pick which team to win
"""
def perfect_options(stats):
    markets = []
   
    # Win Draw Win Markets : Home team
    if get_record(stats, 'winDrawWin_stats', 'ovr', 'home', 'away'):
        if get_loc_record(stats, 'winDrawWin_stats', 'home', 'home'):
            if get_h2h_record(stats, 'winDrawWin_stats', 'ovr', 'h2h', 'home'):
                markets.append('home')
                
    # Win Draw Win Markets : Away team
    if get_record(stats, 'winDrawWin_stats', 'ovr', 'away', 'home'):
        if get_loc_record(stats, 'winDrawWin_stats', 'away', 'away'):
            if get_h2h_record(stats, 'winDrawWin_stats', 'ovr', 'h2h', 'away'):
                markets.append('away')
    return markets


