def predict_total(h2h, total):
    h2h = h2h[2]['matches']
    count = 0
    for game in h2h:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-'))
                if total < (a + b):
                    count += 1
            except ValueError:
                continue
        else:
            continue
    
    percent = count / 5 * 100
    if percent > 90:
        return total
    return None


def predict_handicap(h2h, hc):
    h2h = h2h[2]['matches']
    if hc > 15:
        return None
    
    count = 0
    for game in h2h:
        result = game.get('result', '').strip() 
        if result and '-' in result:  
            try:
                a, b = map(int, result.split('-'))
                if hc > (abs(a - b)):
                    count += 1
            except ValueError:
                continue
        else:
            continue
    
    percent = count / 5 * 100
    if percent > 90:
        return hc
    return None


def predict_basketball(h2h, total, hc, win):
    hc = predict_handicap(h2h, hc)
    total = predict_total(h2h, total)

    if hc:
        if total:
            if win:
                return {'handicap': hc, 'total': format_float(total), 'win': win}
            return {'handicap': hc, 'total': format_float(total)}
        return {'handicap'}
    if total:
        if win:
            return {'total': format_float(total), "win": win}
        return {'total': format_float(total)}
    
    if win:
        return {'win': win}
        

def format_float(value):
    integer_part = int(value)
    decimal_part = value - integer_part

    return integer_part if decimal_part < 0.5 else integer_part + 0.5