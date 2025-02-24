from .markets import team_form

def get_prediction(data):
    pred_form = team_form(data.get('home'), data.get('away'))
    print(pred_form)

