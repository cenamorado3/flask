import requests
import json
import psycopg2
from persistance.engine import Engine
from sqlalchemy import insert, delete

class NutritionAdapter:
    def request_data(self):
        json_set = requests.get('https://data.cdc.gov/api/views/hn4x-zwk7/rows.json').json()
        columns = [col['fieldName'] for col in json_set['meta']['view']['columns']]
        records = [dict(zip(columns, data)) for data in json_set['data']]
        
        geoloc = []
        for record in records:
            if(record['geolocation'] is not None):
                geo_set = json.loads(record['geolocation'][0])
                geoloc.append({
                    ":id": record[':id'],
                    "Address": geo_set['address'],
                    "City": geo_set['city'],
                    "State": geo_set['state'],
                    "Zip": geo_set['zip'],
                    "Latitude": record['geolocation'][1],
                    "Longitude": record['geolocation'][2]
                })
            del record['geolocation']


        engine = Engine()
        engine.session.execute(delete(engine.base.classes.dnpao))#truncate...should casade delete geolocation

        engine.session.execute(insert(engine.base.classes.dnpao), records)
        engine.session.execute(insert(engine.base.classes.geolocation), geoloc)

        engine.session.commit()
        return records