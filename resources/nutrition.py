import psutil
from flask_restful import Resource
from flask import jsonify, json

from adapters.NutritionAdapter import NutritionAdapter

class Nutrition(Resource):
    def get(self):
        data = NutritionAdapter().request_data()


        s = ''
        s += f'INSERT INTO public.dnpao ({','.join(data[0].keys())}) VALUES'
        for d in data:
            s += '('
            for k,v in d.items():
                
                if k != 'geolocation':
                    s += f'"{v}",'
            s += '),'
        return jsonify(s)