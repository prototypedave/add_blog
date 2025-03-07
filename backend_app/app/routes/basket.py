from flask import Blueprint, jsonify
from datetime import datetime, timedelta
from app.storage.database import db
from app.models.basketball import BasketPrediction
from app.models.poll import poll_database

basket_bp = Blueprint('basket_bp', __name__)

@basket_bp.route('/basketball/general', methods=['GET'])
def get_today_basket():
    """
        API Endpoint for basketball predictions
    """
    today = datetime.now().date()
    response_data = poll_database(db=db, table=BasketPrediction, time=today)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)


@basket_bp.route('/basketball/general/previous', methods=['GET'])
def get_previous_basket():
    """
        API Endpoint for basketball predictions
    """
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    response_data = poll_database(db=db, table=BasketPrediction, time=yesterday)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)