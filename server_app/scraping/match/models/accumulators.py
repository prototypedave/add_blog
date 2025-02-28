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


def get_match_winner(stats, stat, type, h2h, home, away, markets, mkt):
    markets = markets
    if get_record(stats, stat, type, home, away):
        if get_loc_record(stats, stat, home, home):
            if get_h2h_record(stats, stat, type, h2h, home):
                markets.append(mkt)
    return markets


def get_other_stats(stats, stat, type, markets, mkt):
    markets = markets
    if get_loc_record(stats, stat, type, 'home') and get_loc_record(stats, stat, type, 'away'):
        if get_loc_record(stats, stat, 'home', 'team') and get_loc_record(stats, stat, 'away', 'team'):
            if get_loc_record(stats, stat, type, 'h2h'):
                markets.append(mkt)
    return markets


"""
Pick which team to win
"""
def perfect_options(stats):
    markets = []
    # Win Draw Win Markets : Home team
    markets = get_match_winner(stats, 'winDrawWin_stats', 'ovr', 'h2h', 'home', 'away', markets, 'home')
    # Win Draw Win Markets : Away 
    markets = get_match_winner(stats, 'winDrawWin_stats', 'ovr', 'h2h', 'away', 'home', markets, 'away') # change home and away loc
    # Over / Under : Over
    markets = get_other_stats(stats, 'over25_stats', 'ovr', markets, 'over 2.5')
    # Over / Under : Over
    markets = get_other_stats(stats, 'under25_stats', 'ovr', markets, 'under 2.5')
    # BTTS / No BTTS : BTTS
    markets = get_other_stats(stats, 'btts_stats', 'ovr', markets, 'btts')
    # BTTS / No BTTS : No BTTS
    markets = get_other_stats(stats, 'ng_stats', 'ovr', markets, 'no btts')

    return markets





