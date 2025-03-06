"""
    Get perfect total markets
"""
def get_total_35(stats):
    over = get_overall_35(stats)
    over_home = get_home_over_35(stats)
    under = get_overall_under_35(stats)
    under_home = get_home_under_35(stats)

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

def get_overall_35(stats):
    over_35 = stats['over_35']['ovr']
    home = over_35['home']
    away = over_35['away']
    h2h = over_35['h2h']
    
    return perfect_overall_35(home, away, h2h)


def get_overall_under_35(stats):
    over_35 = stats['over_35']['ovr']
    home = over_35['home']
    away = over_35['away']
    h2h = over_35['h2h']
    
    return perfect_overall_under_35(home, away, h2h)


def get_home_over_35(stats):
    over_35 = stats['over_35']['home']
    home = over_35['home']
    h2h = over_35['h2h']

    return perfect_home_35(home, h2h)


def get_home_under_35(stats):
    over_35 = stats['over_35']['home']
    home = over_35['home']
    h2h = over_35['h2h']

    return perfect_home_under_35(home, h2h)


def perfect_overall_35(home, away, h2h):
    if (home > 79 and away > 79) and h2h > 79:
        return 'over 3.5'
    return None


def perfect_home_35(home, h2h):
    if home > 79 and h2h > 79:
        return 'over 3.5'
    return None


def perfect_overall_under_35(home, away, h2h):
    if (home < 21 and away < 21) and h2h < 21:
        return 'under 3.5'
    return None


def perfect_home_under_35(home, h2h):
    if home < 21 and h2h < 21:
        return 'under 3.5'
    return None