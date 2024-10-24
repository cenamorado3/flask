import psutil
from flask_restful import Resource
from flask import jsonify, json

from adapters.NutritionAdapter import NutritionAdapter

class Nutrition(Resource):
    def get(self):
        data = NutritionAdapter().request_data()
        return jsonify(data)