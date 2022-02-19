from flask import Flask
from flask_cors import CORS
from src.api.response_any_json.view import base_json_endpoint

_app = Flask(__name__)
_app.register_blueprint(base_json_endpoint)
CORS(_app)


def get_app():
    return _app
