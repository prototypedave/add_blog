from flask import Blueprint
from .football import foot_bp
from .basket import basket_bp
from .hockey import hockey_bp
from .win_rate import win_bp


def register_routes(app):
    app.register_blueprint(foot_bp, url_prefix='/api')
    app.register_blueprint(basket_bp, url_prefix='/api')
    app.register_blueprint(hockey_bp, url_prefix='/api')
    app.register_blueprint(win_bp, url_prefix='/api')