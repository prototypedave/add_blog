from .algorithms import perfect_stats


def assign_mkts(mkts):
    markets = []
    if mkts:
        for mkt in mkts:
            if 'win' in mkt and '1x2' not in markets:
                markets.append('1x2')
            elif 'btts' or 'ng' in mkt and 'BTTS / NO BTTS' not in markets:
                markets.append('BTTS / NO BTTS')
            elif 'ov25' or 'un25' in mkt and 'Over/Under 2.5' not in markets:
                markets.append('Over/Under 2.5')
                

"""
    Return perfect markets to bet on
"""
def find_perfect_market(stats):
    markets = [mkt for mkt, value in perfect_stats(stats).items() if value]
    pred_mkts = assign_mkts(markets)
    return ({
        'markets': markets,
        'predict': pred_mkts
    })