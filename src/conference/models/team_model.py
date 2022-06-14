from ormar import Model, Integer, ForeignKey, Enum
from base_model import BaseMeta
from workspace_model import WorkspaceModel
from user_model import UserModel
from conference.schemas.user_schema import UserLevel


class TeamModel(Model):
    class Meta(BaseMeta):
        tablename = "team"

    id: int = Integer(primary_key=True, index=True)
    workspace_id: int = ForeignKey(WorkspaceModel)
    user_id: int = ForeignKey(UserModel)
    user_level: str = Enum(UserLevel)
