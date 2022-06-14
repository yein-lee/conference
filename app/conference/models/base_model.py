from ormar import ModelMeta
from config.db_session import metadata, database


class BaseMeta(ModelMeta):
    metadata = metadata
    database = database
