from flask import Flask, jsonify
from flask_cors import CORS
from .models.storage import db
from datetime import datetime
from .scheduler import start_scheduler
from .models.predictions import MatchPrediction
from .models.sure import SurePrediction
from .models.accumulator import AccumulatorPrediction
from .models.best_picks import BestPicksPrediction

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  
    start_scheduler(app, db)  

@app.route('/api/status', methods=['GET'])
def update_state():
    today = datetime.now().date()

    exists = db.session.query(
        MatchPrediction.query.filter(
            db.func.date(MatchPrediction.created_at) == today
        ).exists()
    ).scalar()

    return jsonify({"status": exists})


@app.route('/api/ovr-predictions', methods=['GET'])
def get_match():
    today = datetime.now().date()

    # Query for today's predictions
    predictions = MatchPrediction.query.filter(
        db.func.date(MatchPrediction.created_at) == today
    ).all()

    # If no predictions exist for today, fetch the latest day with predictions
    if not predictions:
        # Find the most recent date with predictions
        most_recent_date = db.session.query(
            db.func.date(MatchPrediction.created_at)
        ).order_by(db.func.date(MatchPrediction.created_at).desc()).first()

        if most_recent_date:
            predictions = MatchPrediction.query.filter(
                db.func.date(MatchPrediction.created_at) == most_recent_date[0]
            ).all()

    # Prepare the response data
    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)


@app.route('/api/sure-predictions', methods=['GET'])
def get_sure_pred():
    today = datetime.now().date()

    # Query for today's predictions
    predictions = SurePrediction.query.filter(
        db.func.date(SurePrediction.created_at) == today
    ).all()

    # If no predictions exist for today, fetch the latest day with predictions
    if not predictions:
        # Find the most recent date with predictions
        most_recent_date = db.session.query(
            db.func.date(SurePrediction.created_at)
        ).order_by(db.func.date(SurePrediction.created_at).desc()).first()

        if most_recent_date:
            predictions = SurePrediction.query.filter(
                db.func.date(SurePrediction.created_at) == most_recent_date[0]
            ).all()

    # Prepare the response data
    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)


@app.route('/api/accu-predictions', methods=['GET'])
def get_sure():
    today = datetime.now().date()

    # Query for today's predictions
    predictions = AccumulatorPrediction.query.filter(
        db.func.date(AccumulatorPrediction.created_at) == today
    ).all()

    # If no predictions exist for today, fetch the latest day with predictions
    if not predictions:
        # Find the most recent date with predictions
        most_recent_date = db.session.query(
            db.func.date(AccumulatorPrediction.created_at)
        ).order_by(db.func.date(AccumulatorPrediction.created_at).desc()).first()

        if most_recent_date:
            predictions = AccumulatorPrediction.query.filter(
                db.func.date(AccumulatorPrediction.created_at) == most_recent_date[0]
            ).all()

    # Prepare the response data
    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)


@app.route('/api/best-predictions', methods=['GET'])
def get_best():
    today = datetime.now().date()

    # Query for today's predictions
    predictions = BestPicksPrediction.query.filter(
        db.func.date(BestPicksPrediction.created_at) == today
    ).all()

    # If no predictions exist for today, fetch the latest day with predictions
    if not predictions:
        # Find the most recent date with predictions
        most_recent_date = db.session.query(
            db.func.date(BestPicksPrediction.created_at)
        ).order_by(db.func.date(BestPicksPrediction.created_at).desc()).first()

        if most_recent_date:
            predictions = BestPicksPrediction.query.filter(
                db.func.date(BestPicksPrediction.created_at) == most_recent_date[0]
            ).all()

    # Prepare the response data
    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
