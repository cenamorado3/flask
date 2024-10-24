import requests
import json
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert
import psycopg2

class NutritionAdapter:
    def request_data(self):
        json_set = requests.get('https://data.cdc.gov/api/views/hn4x-zwk7/rows.json').json()
        columns = [col['fieldName'] for col in json_set['meta']['view']['columns']]
        records = [dict(zip(columns, data)) for data in json_set['data']]
        
        geoloc = []
        for record in records:
            if(record['geolocation'] is not None):
                geo_set = json.loads(record['geolocation'][0])
                print(geo_set)
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


        engine = create_engine('postgresql://user:pass`@127.0.0.1:5432/flask')

        with engine.connect() as con:
            dnpao = Table('dnpao', MetaData(), autoload_with=engine)
            geolocation = Table('geolocation', MetaData(), autoload_with=engine)
            con.execute(dnpao.insert(), records)
            con.execute(geolocation.insert(), geoloc)
            con.commit()
        return records