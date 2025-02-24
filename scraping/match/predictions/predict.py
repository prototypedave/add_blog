from .markets import team_form
from .injury import injury_predictions
from .tactical import tactical_prediction
from .motivation import match_motivation
from .discipline import predict_discipline

def get_prediction(data):
    pred_form = team_form(data.get('home'), data.get('away'))
    pred_injury = injury_predictions(data.get('home'), data.get('away'))
    pred_tactical = tactical_prediction(data.get('home'), data.get('away'))
    pred_motivation = match_motivation(data.get('home'), data.get('away'))
    pred_discipline = predict_discipline(data.get('home'), data.get('away'))
    print(pred_form)