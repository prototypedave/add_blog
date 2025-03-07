from flask import Blueprint, jsonify
from datetime import datetime, timedelta
from app.storage.database import db
from app.models.football.general import GeneralPrediction
from app.models.football.sure import SurePrediction
from app.models.football.accumulator import AccumulatorPrediction
from app.models.football.best import BestPicksPrediction
from app.models.poll import poll_database

foot_bp = Blueprint('foot_bp', __name__)

@foot_bp.route('/football/general', methods=['GET'])
def get_today_match():
    """
        API Endpoint for general predictions
    """
    today = datetime.now().date()

    response_data = poll_database(db=db, table=GeneralPrediction, time=today)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)


@foot_bp.route('/football/general/previous', methods=['GET'])
def get_yesterday_match():
    """
        API Endpoint for general predictions
    """
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    response_data = poll_database(db=db, table=GeneralPrediction, time=yesterday)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)


@foot_bp.route('/football/sure', methods=['GET'])
def get_sure_pred():
    """
        API Endpoint for sure predictions
    """
    today = datetime.now().date()
    response_data = poll_database(db=db, table=SurePrediction, time=today)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)


@foot_bp.route('/football/sure/previous', methods=['GET'])
def get_yesterday_sure_pred():
    """
        API Endpoint for sure predictions
    """
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    response_data = poll_database(db=db, table=SurePrediction, time=yesterday)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]
    return jsonify(final_response)


@foot_bp.route('/football/accumulator', methods=['GET'])
def get_accumulator():
    """
        API Endpoint for Accumulator bets predictions
    """
    today = datetime.now().date()
    response_data = poll_database(db=db, table=AccumulatorPrediction, time=today)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)


@foot_bp.route('/football/accumulator/previous', methods=['GET'])
def get_previous_accumulator():
    """
        API Endpoint for Accumulator bets predictions
    """
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    response_data = poll_database(db=db, table=AccumulatorPrediction, time=yesterday)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)


@foot_bp.route('/football/best', methods=['GET'])
def get_best():
    """
        API Endpoint for Best bets predictions
    """
    today = datetime.now().date()
    response_data = poll_database(db=db, table=BestPicksPrediction, time=today)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)


@foot_bp.route('/football/best/previous', methods=['GET'])
def get_previous_best():
    """
        API Endpoint for Best bets predictions
    """
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    response_data = poll_database(db=db, table=BestPicksPrediction, time=yesterday)

    final_response = [{"league": league, "matches": matches} for league, matches in response_data.items()]

    return jsonify(final_response)
