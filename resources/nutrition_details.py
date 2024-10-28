from flask_restful import Resource
from flask import jsonify, make_response
from persistance.engine import Engine
from sqlalchemy.orm import Query


class NutritionDetails(Resource):
    def get(self, id):
        if id is None:
            make_response({'error': f'An id was not provided'}, 400)
        engine = Engine()
        detail = engine.session.query(engine.base.classes.dnpao).filter(engine.base.classes.dnpao.id == id).first()
        return make_response(jsonify({'error': f'Detail for {id} not found'}), 404) if detail is None else jsonify(engine.serialize(detail))
        
