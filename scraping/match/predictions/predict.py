from .markets import team_form, injury_predictions

def get_prediction(data):
    pred_form = team_form(data.get('home'), data.get('away'))
    pred_injury = injury_predictions(data.get('home'), data.get('away'))
    print(pred_injury)