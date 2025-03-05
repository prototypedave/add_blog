from flask import Blueprint, jsonify
from datetime import datetime
from storage.database import db
from models.hockey import HockeyPrediction

hockey_bp = Blueprint('hockey_bp', __name__)

@hockey_bp.route('/ice-hockey/general', methods=['GET'])
def get_basket():
    """
        API Endpoint for basketball predictions
    """
    today = datetime.now().date()
    predictions = HockeyPrediction.query.filter(
        db.func.date(HockeyPrediction.created_at) == today
    ).all()

    if not predictions:
        most_recent_date = db.session.query(
            db.func.date(HockeyPrediction.created_at)
        ).order_by(db.func.date(HockeyPrediction.created_at).desc()).first()

        if most_recent_date:
            predictions = HockeyPrediction.query.filter(
                db.func.date(HockeyPrediction.created_at) == most_recent_date[0]
            ).all()
    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)