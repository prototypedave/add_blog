"""
    Find the perfect winner
"""
def get_winner(stats):
    ovr_win = get_overall_winner(stats)
    side_win = get_side_win(stats)

    if (ovr_win and side_win) and ovr_win == side_win:
        return ovr_win
    if ovr_win and not side_win:
        return ovr_win
    if side_win and not ovr_win:
        return side_win
    return None


def get_overall_winner(stats):
    win_stats = stats['win_stats']['ovr']  
    home = win_stats['home']
    away = win_stats['away']
    h2h_home = win_stats['h2h']['home']
    h2h_away = 100 - h2h_home  

    def _check_winner(*args):
        """Helper function to check conditions in order."""
        for condition in args:
            winner = condition()
            if winner:
                return winner
        return None

    return _check_winner(
        lambda: get_above_70_form(home, h2h_home, 'home win'),
        lambda: get_h2h_advantage(home, h2h_home, 'home win'),
        lambda: get_above_70_form(away, h2h_away, 'away win'),
        lambda: get_h2h_advantage(away, h2h_away, 'away win'),
        lambda: get_outperforming_team(home, away, h2h_home, 'home win'),
        lambda: get_outperforming_team(away, home, h2h_away, 'away win')
    )


def get_side_win(stats):
    home = stats.get('win_stats').get('home').get('home')
    home_h2h = stats.get('win_stats').get('home').get('h2h').get('home')
    away = stats.get('win_stats').get('away').get('away')
    away_h2h = stats.get('win_stats').get('away').get('h2h').get('away')

    winner = best_side_win(home, home_h2h, 'home win')
    if winner:
        return winner
    
    winner = best_side_win(away, away_h2h, 'away win')
    if winner:
        return winner
    
    return None


def get_above_70_form(team, h2h, side):
    if team > 69 and h2h > 69:
       return side

def get_h2h_advantage(team, h2h, side):
    if h2h > 79 and team > 69:  # Good form and atleast won 4/5 of the last games
        return side 
    
def get_outperforming_team(teamA, teamB, h2h, side):
    if teamA > 69 and teamB < 30:   # Team B bad form
        if h2h > 59:  # Team A has won atleast 3/5 of the games
            return side
        
def best_side_win(team, h2h, side):
    if team > 79 and h2h > 79: # Almost perfect home record
        return side
