from flask import Blueprint, jsonify
from datetime import datetime, timedelta
from app.storage.database import db
from app.models.hockey import HockeyPrediction
from app.models.poll import poll_database

hockey_bp = Blueprint('hockey_bp', __name__)

@hockey_bp.route('/ice-hockey/general', methods=['GET'])
def get_hockey():
    """
        API Endpoint for basketball predictions
    """
    today = datetime.now().date()
    response_data = poll_database(db=db, table=HockeyPrediction, time=today)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)


@hockey_bp.route('/ice-hockey/general/previous', methods=['GET'])
def get_previous_hockey():
    """
        API Endpoint for basketball predictions
    """
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    response_data = poll_database(db=db, table=HockeyPrediction, time=yesterday)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)