from .markets import team_form

def get_prediction(data):
    team_form(data.get('home'), data.get('away'))

