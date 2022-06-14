from databases import Database
from sqlalchemy import MetaData, create_engine
import os


DATABASE_URL = '{driver_name}://{username}:{password}@{host}:{port}/{database}'\
    .format(driver_name='mysql+aiomysql',
            username=os.environ['MYSQL_USERNAME'],
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            host=os.environ['MYSQL_HOST'],
            port=os.environ['MYSQL_PORT'],
            database=os.environ['MYSQL_DATABASE'])
database = Database(DATABASE_URL, min_size=5, max_size=20)
metadata = MetaData()
