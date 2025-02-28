from .algorithms import perfect_stats, perfect_h2h, on_form, on_form_h2h

def define_markets(mkts, markets):
    markets = markets
    if mkts:
        for mkt in mkts:
            if 'win' in mkt and '1x2' not in markets:
                markets.append('1x2')
            elif ('btts' in mkt or 'ng' in mkt) and 'BTTS / NO BTTS' not in markets:
                markets.append('BTTS / NO BTTS')
            elif ('ov25' in mkt or 'un25' in mkt) and 'Over/Under 2.5' not in markets:
                markets.append('Over/Under 2.5')
    return markets


def assign_mkts(mkts, h2h, on, form):
    markets = []
    markets = define_markets(mkts, markets)
    markets = define_markets(h2h, markets)
    markets = define_markets(on, markets)
    markets = define_markets(form, markets)
    
    return markets
                

"""
    Return perfect markets to bet on
"""
def find_perfect_market(stats):
    markets = [mkt for mkt, value in perfect_stats(stats).items() if value]
    h2h = [mkt for mkt, value in perfect_h2h(stats).items() if value]
    on_ = [mkt for mkt, value in on_form(stats).items() if value]
    on_h2h = [mkt for mkt, value in on_form_h2h(stats).items() if value]
    pred_mkts = assign_mkts(markets, h2h, on_, on_h2h)
    return ({
        'markets': [markets, h2h, on_, on_h2h],
        'predict': pred_mkts
    })