def get_hockey_prediction(over, btts, win):
    if over:
        if btts:
            if win:
                return [over, btts, win]
            return [over, btts]
        return [over]
    
    elif btts:
        if win:
            return [btts, win]
        return [btts]
    elif win:
        return [win]
    return []