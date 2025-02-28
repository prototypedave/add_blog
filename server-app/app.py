from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from models.predictions import MatchPrediction, delete_old_predictions

db.init_app(app)

with app.app_context():
    db.create_all()

# Checks if there is an update to be made
@app.route('/status', methods=['GET'])
def update_state():
    return jsonify({"status": True})
  

@app.route('/ovr-predictions', methods=['GET'])
def get_match():
    today = datetime.utcnow().date()
    predictions = MatchPrediction.query.filter(
        db.func.date(MatchPrediction.created_at) == today
    ).all()

    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    
    return jsonify(final_response)



if __name__ == '__main__':
    app.run(debug=True)
