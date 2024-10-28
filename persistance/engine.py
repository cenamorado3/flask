
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

class Engine:
    def __init__(self):
        engine = create_engine('postgresql://user:pass`@127.0.0.1:5432/flask')
        #self.Connection = engine.connect()
        self.base = automap_base()
        self.base.prepare(engine, reflect=True)
        self.session = Session(engine)


    #would like a better alternative; TypeError: Object of type InstanceState is not JSON serializable
    def serialize(self, instanceState):
        return {row.name: getattr(instanceState, row.name) for row in instanceState.__table__.columns}