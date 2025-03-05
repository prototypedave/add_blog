from flask import Blueprint, jsonify
from datetime import datetime
from app.storage.database import db
from app.models.basketball import BasketPrediction

basket_bp = Blueprint('basket_bp', __name__)

@basket_bp.route('/basketball/general', methods=['GET'])
def get_basket():
    """
        API Endpoint for basketball predictions
    """
    today = datetime.now().date()
    predictions = BasketPrediction.query.filter(
        db.func.date(BasketPrediction.created_at) == today
    ).all()

    if not predictions:
        most_recent_date = db.session.query(
            db.func.date(BasketPrediction.created_at)
        ).order_by(db.func.date(BasketPrediction.created_at).desc()).first()

        if most_recent_date:
            predictions = BasketPrediction.query.filter(
                db.func.date(BasketPrediction.created_at) == most_recent_date[0]
            ).all()
    response_data = {}

    for match in predictions:
        if match.league not in response_data:
            response_data[match.league] = []
        response_data[match.league].append(match.to_dict())

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)