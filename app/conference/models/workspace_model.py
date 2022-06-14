from ormar import Model, Integer, String
from conference.models.base_model import BaseMeta


class WorkspaceModel(Model):
    class Meta(BaseMeta):
        tablename = "workspaces"

    id: int = Integer(primary_key=True, index=True)
    name: str = String(max_length=4, unique=True, index=True, nullable=False)
