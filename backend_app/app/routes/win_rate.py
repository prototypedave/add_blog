from app.storage.database import db
from flask import Blueprint, jsonify
from app.algorithms.percentage import win_percentage

win_bp = Blueprint('win_bp', __name__)

@win_bp.route('/win-rate', methods=['GET'])
def get_hockey():
    """
        API Endpoint for basketball predictions
    """
    response = win_percentage(db)
    
    return jsonify(response)