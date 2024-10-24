import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert
class NutritionAdapter:
    def request_data(self):
        json_set = requests.get('https://data.cdc.gov/api/views/hn4x-zwk7/rows.json').json()
        columns = [col['fieldName'] for col in json_set['meta']['view']['columns']]
        return [dict(zip(columns, data)) for data in json_set['data']]



    def _create_table(self):
        engine = create_engine('postgresql://user:password@host:port/database')

        metadata = MetaData()
        users = Table('DNPAO', metadata,
            Column('id', Integer, primary_key=True),
            Column(':sid', String),
            Column(':id', String),
            Column(':position', String),
            Column(':created_at', String),
            Column(':created_meta', String),
            Column(':updated_at', String),
            Column(':updated_meta', String),
            Column(':meta', String),
            Column('yearstart', String),
            Column('yearend', String),
            Column('locationabbr', String),
            Column('locationdesc', String),
            Column('datasource', String),
            Column('class', String),
            Column('topic', String),
            Column('question', String),
            Column('data_value_unit', String),
            Column('data_value_type', String),
            Column('data_value', String),
            Column('data_value_alt', String),
            Column('data_value_footnote_symbol', String),
            Column('data_value_footnote', String),
            Column('low_confidence_limit', String),
            Column('high_confidence_limit', String),
            Column('sample_size', String),
            Column('total', String),
            Column('age_years', String),
            Column('education', String),
            Column('gender', String),
            Column('income', String),
            Column('race_ethnicity', String),
            Column('geolocation', String),
            Column('classid', String),
            Column('topicid', String),
            Column('questionid', String),
            Column('datavaluetypeid', String),
            Column('locationid', String),
            Column('stratificationcategory1', String),
            Column('stratification1', String),
            Column('stratificationcategoryid1', String),
            Column('stratificationid1', String)
        )
        metadata.create_all(engine)