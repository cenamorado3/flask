from flask import Flask
from flask_restful import Resource, Api

from resources.health import Health
from resources.nutrition import Nutrition
from resources.nutrition_details import NutritionDetails

app = Flask(__name__)


api = Api(app)

api.add_resource(Health, '/health')
api.add_resource(Nutrition, '/cod/nutrition/refresh')
api.add_resource(NutritionDetails, '/cod/nutrition/<int:id>')