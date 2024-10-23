from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api

from resources.health import Health
from resources.nutrition import Nutrition

app = Flask(__name__)


api = Api(app)

api.add_resource(Health, '/health')
api.add_resource(Nutrition, '/cod/nutrition')