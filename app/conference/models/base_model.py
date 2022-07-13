from ormar import ModelMeta
from config.db_session import metadata, database
from pydantic import Extra


class BaseMeta(ModelMeta):
    metadata = metadata
    database = database


class BaseConfig:
    orm_mode = True
    arbitrary_types_allowed = True
    extra = Extra.ignore
