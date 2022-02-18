import json
import os

import requests
from flask import Blueprint, abort, jsonify
from src.api.helpers.logger_conf import logger

OPEN_WEATHER_URL = os.environ['OPEN_WEATHER_URL']
API_KEY = os.environ['OPEN_WEATHER_API_KEY']
OPEN_WEATHER_URL_BY_CITY = os.environ['OPEN_WEATHER_URL_BY_CITY']

base_json_endpoint = Blueprint('base_json_endpoint', __name__)


@base_json_endpoint.route('/get_base_json')
def get_base_json():
    cwd = os.getcwd()
    try:
        file = open(f'{cwd}/test.json', 'r')
    except FileNotFoundError as error:
        logger.error('JSON file is invalid, make sure you haven`t modify it')
        abort(404, {'detail': 'JSON file is invalid, make sure you haven`t modify it'})
    try:
        json_resp = json.load(file)
    except json.JSONDecodeError as _:
        logger.error('JSON file is invalid, make sure you haven`t modify it')
        abort(418, {'detail': 'JSON file is invalid, make sure you haven`t modify it'})
    return jsonify(json_resp)


@base_json_endpoint.route('/get_london_weather')
def get_london_weather():
    with requests.get(f'{OPEN_WEATHER_URL}{API_KEY}') as response:
        try:
            return jsonify(response.json())
        except Exception as error:
            logger.error(f'{error}')


@base_json_endpoint.route('/get_weather_by/<city>')
def get_city_weather(city):
    url = OPEN_WEATHER_URL_BY_CITY.format(city=city)
    with requests.get(f'{url}{API_KEY}') as response:
        try:
            return jsonify(response.json())
        except Exception as error:
            logger.error(f'{error}')
