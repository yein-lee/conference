from databases import Database
from sqlalchemy import MetaData, create_engine

database = Database('sqlite:///./test.db', min_size=5, max_size=20)
metadata = MetaData()

engine = create_engine('sqlite:///./test.db')
metadata.create_all(engine)
