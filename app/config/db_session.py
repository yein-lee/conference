from databases import Database
from sqlalchemy import MetaData

DATABASE_URL = 'sqlite:///./test.db'
database = Database(DATABASE_URL)
metadata = MetaData()
