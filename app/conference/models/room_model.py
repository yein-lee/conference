from ormar import Model, Integer, String, ForeignKey
from conference.models.base_model import BaseMeta
from conference.models.workspace_model import WorkspaceModel


class RoomModel(Model):
    class Meta(BaseMeta):
        tablename = "rooms"

    id: int = Integer(primary_key=True, index=True)
    workspace_id: int = ForeignKey(WorkspaceModel)
    name: str = String(max_length=16)
