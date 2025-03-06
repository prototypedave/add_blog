"""
    Get perfect total markets
"""
def get_total_25(stats):
    over = get_overall_25(stats)
    over_home = get_home_over_25(stats)
    under = get_overall_under_25(stats)
    under_home = get_home_under_25(stats)

    if (over and over_home) and (not under and not under_home):
        return over
    
    if (over or over_home) and (not under and not under_home):
        if over:
            return over
        if over_home:
            return over_home
    
    if (not over and not over_home) and (under and under_home):
        return under
    
    if (not over and not over_home) and (under or under_home):
        if under:
            return under
        if under_home:
            return under_home
    
    return None

def get_overall_25(stats):
    over_25 = stats['ovr']
    home = over_25['home']
    away = over_25['away']
    h2h = over_25['h2h']
    
    return perfect_overall_25(home, away, h2h)


def get_overall_under_25(stats):
    over_25 = stats['ovr']
    home = over_25['home']
    away = over_25['away']
    h2h = over_25['h2h']
    
    return perfect_overall_under_25(home, away, h2h)


def get_home_over_25(stats):
    over_25 = stats['home']
    home = over_25['team']
    h2h = over_25['h2h']

    return perfect_home_25(home, h2h)


def get_home_under_25(stats):
    over_25 = stats['home']
    home = over_25['team']
    h2h = over_25['h2h']

    return perfect_home_under_25(home, h2h)


def perfect_overall_25(home, away, h2h):
    if (home > 79 and away > 79) and h2h > 79:
        return 'over 2.5'
    return None


def perfect_home_25(home, h2h):
    if home > 79 and h2h > 79:
        return 'over 2.5'
    return None


def perfect_overall_under_25(home, away, h2h):
    if (home < 21 and away < 21) and h2h < 21:
        return 'under 2.5'
    return None


def perfect_home_under_25(home, h2h):
    if home < 21 and h2h < 21:
        return 'under 2.5'
    return None