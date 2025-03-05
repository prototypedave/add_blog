from flask import Blueprint, jsonify
from datetime import datetime
from storage.database import db
from models.football.general import GeneralPrediction

foot_bp = Blueprint('foot_bp', __name__)

@foot_bp.route('/general', methods=['GET'])
def get_match():
    """
        API Endpoint for general predictions
    """
    today = datetime.now().date()

    # Query for today's predictions
    predictions = GeneralPrediction.query.filter(
        db.func.date(GeneralPrediction.created_at) == today
    ).all()

    # If no predictions exist for today, fetch the latest day with predictions
    if not predictions:
        most_recent_date = db.session.query(
            db.func.date(GeneralPrediction.created_at)
        ).order_by(db.func.date(GeneralPrediction.created_at).desc()).first()

        if most_recent_date:
            predictions = GeneralPrediction.query.filter(
                db.func.date(GeneralPrediction.created_at) == most_recent_date[0]
            ).all()
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
