from flask import Blueprint
from .football import foot_bp


def register_routes(app):
    app.register_blueprint(foot_bp, url_prefix='/api')