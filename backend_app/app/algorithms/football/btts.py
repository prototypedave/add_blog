"""
    Get perfect total markets
"""
def get_btts(stats):
    btts_yes = get_overall_btts_yes(stats)
    btts_yes_home = get_home_btts_yes(stats)
    btts_no = get_overall_btts_no(stats)
    btts_no_home = get_home_btts_no(stats)

    if (btts_yes and btts_yes_home) and (not btts_no and not btts_no_home):
        return btts_yes
    
    if (btts_yes or btts_yes_home) and (not btts_no and not btts_no_home):
        if btts_yes:
            return btts_yes
        if btts_yes_home:
            return btts_yes_home
    
    if (not btts_yes and not btts_yes_home) and (btts_no and btts_no_home):
        return btts_no
    
    if (not btts_yes and not btts_yes_home) and (btts_no or btts_no_home):
        if btts_no:
            return btts_no
        if btts_no_home:
            return btts_no_home
    
    return None

def get_overall_btts_yes(stats):
    btts = stats['ovr']
    home = btts['home']
    away = btts['away']
    h2h = btts['h2h']
    
    return perfect_overall_btts_yes(home, away, h2h)


def get_overall_btts_no(stats):
    btts = stats['ovr']
    home = btts['home']
    away = btts['away']
    h2h = btts['h2h']
    
    return perfect_overall_btts_no(home, away, h2h)


def get_home_btts_yes(stats):
    btts = stats['home']
    home = btts['team']
    h2h = btts['h2h']

    return perfect_home_btts_yes(home, h2h)


def get_home_btts_no(stats):
    btts = stats['home']
    home = btts['team']
    h2h = btts['h2h']

    return perfect_home_btts_no(home, h2h)


def perfect_overall_btts_yes(home, away, h2h):
    if (home > 79 and away > 79) and h2h > 79:
        return 'BTTS Yes'
    return None


def perfect_home_btts_yes(home, h2h):
    if home > 79 and h2h > 79:
        return 'BTTS Yes'
    return None


def perfect_overall_btts_no(home, away, h2h):
    if (home < 21 and away < 21) and h2h < 21:
        return 'BTTS No'
    return None


def perfect_home_btts_no(home, h2h):
    if home < 21 and h2h < 21:
        return 'BTTS No'
    return None