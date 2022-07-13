from ormar import Model, Integer, String
from conference.models.base_model import BaseMeta, BaseConfig


class WorkspaceModel(Model):
    class Meta(BaseMeta):
        tablename = "workspaces"

    class Config(BaseConfig):
        ...

    id: int = Integer(primary_key=True, index=True)
    name: str = String(max_length=20, unique=True, index=True, nullable=False)
